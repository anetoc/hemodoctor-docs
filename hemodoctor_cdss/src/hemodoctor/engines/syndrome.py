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

from typing import List, Dict, Any, Set
from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.models.syndrome import SyndromeResult
from hemodoctor.utils.yaml_parser import YAMLParser


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

    WARNING (BUG-014):
        Current implementation does NOT support nested logic (e.g., all/any within any).
        Only flat all/any/negative lists are supported.

        Affected syndromes: S-BLASTIC-SYNDROME (1/35 = 3%)

        Example of unsupported nested logic:
        combine:
          any:
            - E-WBC-VERY-HIGH
            - all: [E-WBC-VERY-HIGH, E-PLT-CRIT-LOW]  # <- nested (NOT supported)

        Fix planned for Sprint 1 (recursive evaluator).
        See: /Users/abelcosta/Documents/HemoDoctor/docs/BUGS.md (BUG-014)
    """
    combine = syndrome_def.get("combine", {})

    # Check "all" logic (AND)
    if "all" in combine:
        required_evidences = combine["all"]
        # DEFENSIVE: Skip if nested logic detected (dict in list)
        if any(isinstance(item, dict) for item in required_evidences):
            return False  # BUG-014: Nested logic not supported
        if not all(eid in present_ids for eid in required_evidences):
            return False

    # Check "any" logic (OR)
    if "any" in combine:
        any_evidences = combine["any"]
        # DEFENSIVE: Skip if nested logic detected (dict in list)
        if any(isinstance(item, dict) for item in any_evidences):
            return False  # BUG-014: Nested logic not supported
        if not any(eid in present_ids for eid in any_evidences):
            return False

    # Check "negative" logic (NOT)
    if "negative" in combine:
        negative_evidences = combine["negative"]
        # DEFENSIVE: Skip if nested logic detected (dict in list)
        if any(isinstance(item, dict) for item in negative_evidences):
            return False  # BUG-014: Nested logic not supported
        if any(eid in present_ids for eid in negative_evidences):
            return False

    # All checks passed
    return True


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
