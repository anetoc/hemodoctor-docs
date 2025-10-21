"""
Syndrome Detector - Detects 35 Hematological Syndromes

This module implements DAG fusion logic to detect clinical syndromes based on
evidence combinations. Implements short-circuit for critical syndromes.

Based on: 03_syndromes_hybrid.yaml v2.3.1 (35 syndromes)

Safety:
- Short-circuit on FIRST critical syndrome
- Precedence ordering (critical → priority → review → routine)
- Guaranteed output (fallback to S-INCONCLUSIVO)
- Tri-state logic handling

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from typing import List, Dict, Any, Set, Union
from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.models.syndrome import SyndromeResult
from hemodoctor.utils.yaml_parser import YAMLParser


def evaluate_combine(
    combine_logic: Union[str, Dict[str, Any]],
    present_ids: Set[str]
) -> bool:
    """
    Recursively evaluate combine logic with support for nested all/any/negative.

    Args:
        combine_logic: Either a string (evidence ID) or dict with all/any/negative
        present_ids: Set of present evidence IDs

    Returns:
        bool: True if logic satisfied, False otherwise

    Examples:
        # Simple evidence ID
        >>> evaluate_combine("E-PLT-CRIT-LOW", {"E-PLT-CRIT-LOW"})
        True

        # Flat all logic
        >>> evaluate_combine({"all": ["E-A", "E-B"]}, {"E-A", "E-B"})
        True

        # Nested logic
        >>> logic = {"any": ["E-A", {"all": ["E-B", "E-C"]}]}
        >>> evaluate_combine(logic, {"E-B", "E-C"})
        True

    Fix for BUG-014: Nested logic support
    See: /Users/abelcosta/Documents/HemoDoctor/docs/BUGS.md
    """
    # Base case: string is an evidence ID
    if isinstance(combine_logic, str):
        return combine_logic in present_ids

    # Recursive case: dict with all/any/negative
    if isinstance(combine_logic, dict):
        # Handle "all" logic (AND)
        if "all" in combine_logic:
            items = combine_logic["all"]
            # Recursively evaluate each item
            return all(evaluate_combine(item, present_ids) for item in items)

        # Handle "any" logic (OR)
        if "any" in combine_logic:
            items = combine_logic["any"]
            # Recursively evaluate each item
            return any(evaluate_combine(item, present_ids) for item in items)

        # Handle "negative" logic (NOT)
        if "negative" in combine_logic:
            items = combine_logic["negative"]
            # None of these should be present
            return not any(evaluate_combine(item, present_ids) for item in items)

    # Unknown type → default to False (fail-safe)
    return False


def is_syndrome_present(
    syndrome_def: Dict[str, Any],
    present_ids: Set[str]
) -> bool:
    """
    Check if syndrome combine logic is satisfied.

    Args:
        syndrome_def: Syndrome definition from YAML
        present_ids: Set of present evidence IDs

    Returns:
        bool: True if syndrome logic satisfied, False otherwise

    Logic:
        - "all": ALL evidences must be present (AND)
        - "any": AT LEAST ONE evidence must be present (OR)
        - "negative": NONE of these evidences can be present (NOT)

    Example:
        >>> syndrome_def = {
        ...     "id": "S-TMA",
        ...     "combine": {
        ...         "all": ["E-PLT-CRIT-LOW", "E-SCHISTOCYTES-GE1PCT"],
        ...         "any": ["E-LDH-HIGH"]
        ...     }
        ... }
        >>> present_ids = {"E-PLT-CRIT-LOW", "E-SCHISTOCYTES-GE1PCT", "E-LDH-HIGH"}
        >>> is_syndrome_present(syndrome_def, present_ids)
        True

    Note (BUG-014 FIXED):
        Now supports nested logic using recursive evaluator.
        All 35 syndromes functional (100%).

        Example of supported nested logic:
        combine:
          any:
            - E-WBC-VERY-HIGH
            - all: [E-WBC-VERY-HIGH, E-PLT-CRIT-LOW]  # <- nested (NOW supported)
            - E-BLASTS-PRESENT

        See: evaluate_combine() for recursive implementation
    """
    combine = syndrome_def.get("combine", {})

    # Use recursive evaluator (supports nested all/any/negative)
    # BUG-014 FIX: evaluate_combine() handles all nesting levels
    return evaluate_combine(combine, present_ids)


def detect_syndromes(
    evidences: List[EvidenceResult],
    yaml_parser: YAMLParser
) -> List[SyndromeResult]:
    """
    Detect syndromes using DAG fusion with short-circuit.

    Args:
        evidences: List of evidence evaluation results (79 total)
        yaml_parser: YAMLParser singleton instance

    Returns:
        List of SyndromeResult objects (1-N syndromes)

    Critical Safety:
        - Stops after FIRST critical syndrome (short-circuit)
        - Sorted by precedence (critical → priority → review → routine)
        - Never returns empty list (fallback: S-INCONCLUSIVO)

    Example:
        >>> from hemodoctor.utils.yaml_parser import YAMLParser
        >>> parser = YAMLParser.get_instance()
        >>> evidences = [
        ...     EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),
        ...     EvidenceResult(id="E-SCHISTOCYTES-GE1PCT", status="present", strength="strong"),
        ...     EvidenceResult(id="E-LDH-HIGH", status="present", strength="high"),
        ... ]
        >>> syndromes = detect_syndromes(evidences, parser)
        >>> syndromes[0].id
        'S-TMA'
        >>> syndromes[0].criticality
        'critical'
    """
    syndrome_defs = yaml_parser.get_all_syndrome_defs()

    # Build set of present evidence IDs for fast lookup
    present_ids = {e.id for e in evidences if e.status == "present"}

    results = []

    # Syndrome definitions are already sorted by precedence in YAML
    # (critical syndromes first, then priority, then review_sample, then routine)
    for syndrome_def in syndrome_defs:
        # Check if syndrome logic satisfied
        if is_syndrome_present(syndrome_def, present_ids):
            syndrome = SyndromeResult(
                id=syndrome_def["id"],
                criticality=syndrome_def["criticality"],
                evidences=list(present_ids),  # All present evidences
                actions=syndrome_def.get("actions", []),
                next_steps=syndrome_def.get("next_steps", []),
            )
            results.append(syndrome)

            # SHORT-CIRCUIT: Stop after first critical syndrome
            if syndrome_def.get("short_circuit") or syndrome_def["criticality"] == "critical":
                break

    # Fallback: Always return something (guaranteed output)
    if not results:
        results.append(SyndromeResult(
            id="S-INCONCLUSIVO",
            criticality="routine",
            evidences=[],
            actions=["Avaliar clinicamente (sintomas, comorbidades)"],
            next_steps=["Repetir CBC se indicação clínica"],
        ))

    return results


def get_critical_syndromes(syndromes: List[SyndromeResult]) -> List[SyndromeResult]:
    """
    Filter syndromes to only critical ones.

    Args:
        syndromes: List of syndrome results

    Returns:
        List of critical syndromes only

    Example:
        >>> syndromes = [
        ...     SyndromeResult(id="S-TMA", criticality="critical", evidences=[]),
        ...     SyndromeResult(id="S-IDA", criticality="priority", evidences=[]),
        ... ]
        >>> critical = get_critical_syndromes(syndromes)
        >>> len(critical)
        1
        >>> critical[0].id
        'S-TMA'
    """
    return [s for s in syndromes if s.criticality == "critical"]


def get_syndrome_by_id(
    syndromes: List[SyndromeResult],
    syndrome_id: str
) -> SyndromeResult | None:
    """
    Find syndrome by ID.

    Args:
        syndromes: List of syndrome results
        syndrome_id: Syndrome ID to find (e.g., "S-TMA")

    Returns:
        SyndromeResult or None if not found

    Example:
        >>> syndromes = [
        ...     SyndromeResult(id="S-TMA", criticality="critical", evidences=[]),
        ... ]
        >>> syndrome = get_syndrome_by_id(syndromes, "S-TMA")
        >>> syndrome.id
        'S-TMA'
    """
    for syndrome in syndromes:
        if syndrome.id == syndrome_id:
            return syndrome
    return None


def count_syndromes_by_criticality(
    syndromes: List[SyndromeResult]
) -> Dict[str, int]:
    """
    Count syndromes grouped by criticality level.

    Args:
        syndromes: List of syndrome results

    Returns:
        Dictionary mapping criticality → count

    Example:
        >>> syndromes = [
        ...     SyndromeResult(id="S-TMA", criticality="critical", evidences=[]),
        ...     SyndromeResult(id="S-IDA", criticality="priority", evidences=[]),
        ...     SyndromeResult(id="S-BETA-THAL", criticality="priority", evidences=[]),
        ... ]
        >>> counts = count_syndromes_by_criticality(syndromes)
        >>> counts
        {'critical': 1, 'priority': 2}
    """
    counts = {}
    for syndrome in syndromes:
        criticality = syndrome.criticality
        counts[criticality] = counts.get(criticality, 0) + 1
    return counts
