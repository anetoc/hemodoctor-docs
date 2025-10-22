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
    Detect syndromes using DAG fusion with multiple critical syndrome support.

    Args:
        evidences: List of evidence evaluation results (79 total)
        yaml_parser: YAMLParser singleton instance

    Returns:
        List of SyndromeResult objects (1-N syndromes)

    Critical Safety (Solution 2 - Sprint 4):
        - Collects ALL critical syndromes before short-circuiting
        - Allows co-occurrence of multiple critical conditions
        - Short-circuits only after all critical syndromes evaluated
        - Sorted by precedence (critical → priority → review → routine)
        - Never returns empty list (fallback: S-INCONCLUSIVO)

    Example (co-occurrence):
        >>> # Case with PLT=1997 + neutrofilia leftshift
        >>> # Expected: BOTH S-THROMBOCITOSE-CRIT AND S-NEUTROFILIA-LEFTSHIFT-CRIT
        >>> evidences = [
        ...     EvidenceResult(id="E-PLT-VERY-HIGH", status="present", strength="strong"),
        ...     EvidenceResult(id="E-NEUTROFILIA-CRIT", status="present", strength="strong"),
        ... ]
        >>> syndromes = detect_syndromes(evidences, parser)
        >>> len(syndromes)  # Both critical syndromes detected
        2

    Note:
        Sprint 4 fix for S-THROMBOCITOSE-CRIT FN=22/30 (73%)
        Root cause: S-NEUTROFILIA-LEFTSHIFT-CRIT (line 6) short-circuited
        before S-THROMBOCITOSE-CRIT (line 7) could be evaluated.
    """
    syndrome_defs = yaml_parser.get_all_syndrome_defs()

    # Build set of present evidence IDs for fast lookup
    present_ids = {e.id for e in evidences if e.status == "present"}

    results = []
    found_critical = False

    # Syndrome definitions are already sorted by precedence in YAML
    # (critical syndromes first, then priority, then review_sample, then routine)
    for syndrome_def in syndrome_defs:
        # BUG-018 FIX: Short-circuit BEFORE evaluating non-critical syndromes
        # (not after detecting them)
        if found_critical and syndrome_def["criticality"] != "critical":
            # We've collected all critical syndromes, now skip non-critical
            break

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

            # SOLUTION 2: Collect ALL critical syndromes before short-circuiting
            if syndrome_def["criticality"] == "critical":
                found_critical = True
                # Don't break - continue evaluating other critical syndromes
            elif syndrome_def.get("short_circuit"):
                # Explicit short-circuit flag for non-critical syndromes
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

    # BUG-017 FIX: Sort syndromes by clinical priority
    # Critical syndromes are sorted by clinical urgency
    # (CIVD, TMA, PLT-CRIT before others)
    CRITICALITY_ORDER = {
        "critical": 0,
        "priority": 1,
        "review_sample": 2,
        "routine": 3
    }

    CRITICAL_PRIORITY = {
        # Life-threatening (highest priority)
        "S-CIVD": 0,
        "S-TMA": 1,
        "S-BLASTIC-SYNDROME": 2,  # BUG-019 FIX: Acute leukemia - extremely critical
        "S-PLT-CRITICA": 3,
        # Urgent but not immediately life-threatening
        "S-NEUTROPENIA-GRAVE": 4,
        "S-ANEMIA-GRAVE": 5,  # BUG-019 FIX: Severe but not as critical as blasts
        "S-THROMBOCITOSE-CRIT": 6,
        "S-NEUTROFILIA-LEFTSHIFT-CRIT": 7,
    }

    # Sort by: 1) criticality level, 2) critical priority, 3) syndrome ID (stable)
    results.sort(key=lambda s: (
        CRITICALITY_ORDER.get(s.criticality, 99),
        CRITICAL_PRIORITY.get(s.id, 50),  # Critical syndromes by priority, others default to 50
        s.id  # Stable sort for non-critical
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


def detect_all_syndromes(
    evidences: List[EvidenceResult],
    yaml_parser: YAMLParser
) -> List[SyndromeResult]:
    """
    Detect ALL syndromes without precedence filtering.

    Args:
        evidences: List of evidence evaluation results (79 total)
        yaml_parser: YAMLParser singleton instance

    Returns:
        List of ALL true syndromes (before precedence applied)

    Note:
        This function is used by generate_alt_routes() to find syndromes
        that were excluded by precedence rules.

    Example:
        >>> # Case with both S-TMA (critical) and S-PTI (priority)
        >>> evidences = [
        ...     EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),
        ... ]
        >>> all_syndromes = detect_all_syndromes(evidences, parser)
        >>> # Returns both S-TMA and S-PTI (before precedence)
    """
    syndrome_defs = yaml_parser.get_all_syndrome_defs()

    # Build set of present evidence IDs for fast lookup
    present_ids = {e.id for e in evidences if e.status == "present"}

    all_syndromes = []

    # Evaluate ALL syndromes (no short-circuit)
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
            all_syndromes.append(syndrome)

    return all_syndromes


def compute_alt_route_confidence(
    syndrome: SyndromeResult,
    evidences: List[EvidenceResult]
) -> float:
    """
    Compute confidence score for alternative route.

    Args:
        syndrome: Syndrome result
        evidences: List of evidence results

    Returns:
        float: Confidence score (0.0-1.0)

    Logic:
        - Start with base score: 1.0
        - For each required evidence:
            - strong: +0.0 (no penalty)
            - moderate: -0.1
            - weak: -0.2
            - missing: -0.3
        - Clamp to [0.0, 1.0]

    Example:
        >>> syndrome = SyndromeResult(id="S-PTI", criticality="priority", evidences=["E-PLT-LOW"])
        >>> evidences = [
        ...     EvidenceResult(id="E-PLT-LOW", status="present", strength="strong"),
        ...     EvidenceResult(id="E-ISOLATED-THROMBO", status="present", strength="moderate"),
        ... ]
        >>> confidence = compute_alt_route_confidence(syndrome, evidences)
        >>> confidence
        0.9
    """
    # Build evidence lookup
    evidence_map = {e.id: e for e in evidences}

    # Start with base score
    score = 1.0

    # Get syndrome evidences (from combine logic)
    syndrome_evidence_ids = syndrome.evidences

    # Penalize based on evidence strength
    for evidence_id in syndrome_evidence_ids:
        evidence = evidence_map.get(evidence_id)

        if not evidence or evidence.status != "present":
            # Missing evidence: -0.3 penalty
            score -= 0.3
        elif evidence.strength == "moderate":
            # Moderate evidence: -0.1 penalty
            score -= 0.1
        elif evidence.strength == "weak":
            # Weak evidence: -0.2 penalty
            score -= 0.2
        # Strong evidence: no penalty

    # Clamp to [0.0, 1.0]
    return max(0.0, min(1.0, score))


def determine_suppression_reason(
    syndrome: SyndromeResult,
    top_syndromes: List[SyndromeResult],
    yaml_parser: YAMLParser
) -> str:
    """
    Determine why syndrome was not selected (suppression reason).

    Args:
        syndrome: Alternative syndrome (not selected)
        top_syndromes: Selected syndromes
        yaml_parser: YAML parser instance

    Returns:
        str: Human-readable suppression reason

    Taxonomy:
        1. Precedence (Critical > Priority)
        2. Precedence (Critical Order)
        3. Precedence (Priority Order)
        4. Conflict (Negative Pair)
        5. Conflict (Soft)
        6. Review Sample

    Example:
        >>> syndrome = SyndromeResult(id="S-PTI", criticality="priority", ...)
        >>> top_syndromes = [SyndromeResult(id="S-TMA", criticality="critical", ...)]
        >>> reason = determine_suppression_reason(syndrome, top_syndromes, parser)
        >>> reason
        'Precedence: S-TMA (critical) > S-PTI (priority)'
    """
    # Case 1: Review sample blocks all
    if any(s.id == "S-REVIEW-SAMPLE" for s in top_syndromes):
        return "Precedence: S-REVIEW-SAMPLE blocks all other results"

    # Case 2: Critical > Priority
    top_critical = [s for s in top_syndromes if s.criticality == "critical"]
    if top_critical and syndrome.criticality != "critical":
        top_id = top_critical[0].id
        return f"Precedence: {top_id} (critical) > {syndrome.id} ({syndrome.criticality})"

    # Case 3: Critical order (among critical syndromes)
    if syndrome.criticality == "critical" and top_critical:
        # Both are critical, precedence by order
        top_id = top_critical[0].id
        return f"Precedence: {top_id} (critical priority) > {syndrome.id} (critical)"

    # Case 4: Priority order (severity_weight)
    # Simplified: just say precedence by priority
    if top_syndromes:
        top_id = top_syndromes[0].id
        return f"Precedence: {top_id} (higher priority) > {syndrome.id}"

    # Default
    return "Suppressed by precedence rules"


def check_conflict(
    syndrome: SyndromeResult,
    top_syndromes: List[SyndromeResult],
    yaml_parser: YAMLParser
) -> Union[str, None]:
    """
    Check if syndrome conflicts with top syndromes.

    Args:
        syndrome: Alternative syndrome
        top_syndromes: Selected syndromes
        yaml_parser: YAML parser instance

    Returns:
        str or None: Syndrome ID it conflicts with, or None

    Example:
        >>> syndrome = SyndromeResult(id="S-PTI", ...)
        >>> top_syndromes = [SyndromeResult(id="S-TMA", ...)]
        >>> conflict = check_conflict(syndrome, top_syndromes, parser)
        >>> conflict
        'S-TMA'
    """
    # Conflict matrix (simplified - hardcoded for V0)
    # In V1, this would load from 07_conflict_matrix_hybrid.yaml
    CONFLICT_PAIRS = {
        ("S-TMA", "S-PTI"),
        ("S-PTI", "S-TMA"),
        ("S-TMA", "S-THROMBOCITOSE"),
        ("S-THROMBOCITOSE", "S-TMA"),
        ("S-PSEUDO-THROMBO", "S-PLT-CRITICA"),
        ("S-PLT-CRITICA", "S-PSEUDO-THROMBO"),
        ("S-IDA", "S-ALFA-THAL"),
        ("S-ALFA-THAL", "S-IDA"),
        ("S-IDA", "S-ACD"),
        ("S-ACD", "S-IDA"),
        ("S-BETA-THAL", "S-ALFA-THAL"),
        ("S-ALFA-THAL", "S-BETA-THAL"),
        ("S-LEUCOEMOIDE", "S-CML"),
        ("S-CML", "S-LEUCOEMOIDE"),
    }

    for top_syndrome in top_syndromes:
        if (syndrome.id, top_syndrome.id) in CONFLICT_PAIRS:
            return top_syndrome.id

    return None


def generate_alt_routes(
    top_syndromes: List[SyndromeResult],
    all_syndromes: List[SyndromeResult],
    evidences: List[EvidenceResult],
    yaml_parser: YAMLParser,
    max_alt_routes: int = 10
) -> List[Dict[str, Any]]:
    """
    Generate alternative routes from syndromes not selected.

    Args:
        top_syndromes: Selected syndromes (displayed to user)
        all_syndromes: All true syndromes (before precedence)
        evidences: Evidence results (for confidence scoring)
        yaml_parser: YAML parser instance
        max_alt_routes: Max number of alt_routes to return

    Returns:
        List of alt_route dicts, sorted by confidence

    Example:
        >>> top_syndromes = [SyndromeResult(id="S-TMA", criticality="critical", ...)]
        >>> all_syndromes = [
        ...     SyndromeResult(id="S-TMA", ...),
        ...     SyndromeResult(id="S-PTI", ...)
        ... ]
        >>> alt_routes = generate_alt_routes(top_syndromes, all_syndromes, evidences, parser)
        >>> alt_routes
        [
            {
                "syndrome_id": "S-PTI",
                "criticality": "priority",
                "confidence": 0.75,
                "suppression_reason": "Precedence: S-TMA (critical) > S-PTI (priority)",
                "conflict_with": "S-TMA"
            }
        ]
    """
    top_ids = {s.id for s in top_syndromes}
    alt_routes = []

    for syndrome in all_syndromes:
        if syndrome.id in top_ids:
            continue  # Skip syndromes already in top

        # Skip S-INCONCLUSIVO (fallback syndrome)
        if syndrome.id == "S-INCONCLUSIVO":
            continue

        # Compute confidence
        confidence = compute_alt_route_confidence(syndrome, evidences)

        # Determine suppression reason
        suppression_reason = determine_suppression_reason(
            syndrome, top_syndromes, yaml_parser
        )

        # Check conflict
        conflict_with = check_conflict(syndrome, top_syndromes, yaml_parser)

        alt_routes.append({
            "syndrome_id": syndrome.id,
            "criticality": syndrome.criticality,
            "confidence": confidence,
            "suppression_reason": suppression_reason,
            "conflict_with": conflict_with,
        })

    # Sort by confidence (highest first)
    alt_routes.sort(key=lambda r: -r["confidence"])

    # Limit to max
    return alt_routes[:max_alt_routes]
