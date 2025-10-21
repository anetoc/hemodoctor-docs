"""
Main Analysis Pipeline - Orchestrates CBC Analysis

This module coordinates the complete CBC analysis pipeline from raw input
to clinical output. Orchestrates all 7 clinical engines.

Flow:
    1. Load YAMLs (singleton cached)
    2. Normalize units (basic passthrough for V0)
    3. Validate schema (basic check)
    4. Evaluate 79 evidences
    5. Detect 35 syndromes (short-circuit on critical)
    6. Compute deterministic route_id (SHA256)
    7. Return result

Performance: <100ms target (V0), <50ms goal (V1)

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from typing import Dict, Any, List
import hashlib
import json
from datetime import datetime

from hemodoctor.utils.yaml_parser import YAMLParser
from hemodoctor.engines.evidence import evaluate_all_evidences, get_present_evidences
from hemodoctor.engines.syndrome import detect_syndromes


def compute_route_id(
    evidences: List,
    syndromes: List
) -> str:
    """
    Compute deterministic SHA256 hash for routing/audit.

    Args:
        evidences: List of EvidenceResult objects
        syndromes: List of SyndromeResult objects

    Returns:
        str: SHA256 hash (64 hex chars)

    Determinism:
        - Same input always produces same hash
        - Used for routing, audit trail, deduplication

    Example:
        >>> from hemodoctor.models.evidence import EvidenceResult
        >>> from hemodoctor.models.syndrome import SyndromeResult
        >>> evidences = [
        ...     EvidenceResult(id="E-ANC-CRIT", status="present", strength="strong")
        ... ]
        >>> syndromes = [
        ...     SyndromeResult(id="S-NEUTROPENIA-GRAVE", criticality="critical", evidences=[])
        ... ]
        >>> route_id = compute_route_id(evidences, syndromes)
        >>> len(route_id)
        64
    """
    # Extract present evidence IDs (sorted for determinism)
    present_evidence_ids = sorted([e.id for e in evidences if e.status == "present"])

    # Extract syndrome IDs (sorted for determinism)
    syndrome_ids = sorted([s.id for s in syndromes])

    # Build deterministic data structure
    route_data = {
        "evidences": present_evidence_ids,
        "syndromes": syndrome_ids,
    }

    # Compute SHA256 hash
    route_json = json.dumps(route_data, sort_keys=True)
    route_hash = hashlib.sha256(route_json.encode()).hexdigest()

    return route_hash


def analyze_cbc(cbc_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main analysis pipeline for CBC.

    Args:
        cbc_data: CBC data dictionary (raw or normalized)

    Returns:
        dict: Complete analysis result with:
            - top_syndromes: List of syndrome IDs
            - evidences_present: List of present evidence IDs
            - route_id: Deterministic SHA256 hash
            - version: Software version
            - timestamp: ISO 8601 timestamp

    Flow:
        1. Load YAMLs (singleton cached)
        2. Normalize units (V0: passthrough)
        3. Validate schema (V0: basic check)
        4. Evaluate 79 evidences
        5. Detect 35 syndromes (short-circuit on critical)
        6. Compute route_id (SHA256)
        7. Return result

    Performance: <100ms target

    Example:
        >>> cbc = {
        ...     "plt": 8,
        ...     "ldh": 980,
        ...     "morphology": {"esquistocitos": True},
        ...     "age_years": 35,
        ...     "sex": "M"
        ... }
        >>> result = analyze_cbc(cbc)
        >>> "S-TMA" in result["top_syndromes"]
        True
        >>> "E-PLT-CRIT-LOW" in result["evidences_present"]
        True
        >>> len(result["route_id"])
        64
    """
    # 1. Load YAML configs (cached singleton)
    yaml_parser = YAMLParser.get_instance()

    # 2. Normalize units (V0: passthrough - implement in V1)
    normalized_cbc = normalize_cbc(cbc_data)

    # 3. Validate schema (V0: basic check - implement full validation in V1)
    validate_schema(normalized_cbc)

    # 4. Evidences (79 rules)
    evidences = evaluate_all_evidences(normalized_cbc, yaml_parser)

    # 5. Syndromes (35 syndromes, short-circuit on critical)
    syndromes = detect_syndromes(evidences, yaml_parser)

    # 6. Routing (deterministic hash)
    route_id = compute_route_id(evidences, syndromes)

    # 7. Build result
    result = {
        "top_syndromes": [s.id for s in syndromes],
        "evidences_present": [e.id for e in evidences if e.status == "present"],
        "route_id": route_id,
        "version": "2.4.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "syndromes_detail": [
            {
                "id": s.id,
                "criticality": s.criticality,
                "actions": s.actions,
                "next_steps": s.next_steps,
            }
            for s in syndromes
        ],
    }

    return result


def normalize_cbc(cbc_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize CBC units (V0: passthrough).

    Args:
        cbc_data: Raw CBC data

    Returns:
        dict: Normalized CBC data

    V0 Implementation:
        - Passthrough (no normalization)
        - Unit conversion to be implemented in Sprint 1

    V1 Implementation (future):
        - Convert Hb g/L → g/dL
        - Convert WBC/PLT units if needed
        - Apply site-specific heuristics (07_normalization_heuristics.yaml)

    Example:
        >>> cbc = {"hb": 152, "age_years": 35, "sex": "M"}
        >>> normalized = normalize_cbc(cbc)
        >>> normalized == cbc  # V0: passthrough
        True
    """
    # V0: Passthrough
    return cbc_data


def validate_schema(cbc_data: Dict[str, Any]) -> None:
    """
    Validate CBC schema (V0: basic check).

    Args:
        cbc_data: CBC data dictionary

    Raises:
        ValueError: If critical validation fails

    V0 Implementation:
        - Basic type checking only
        - Full schema validation to be implemented in Sprint 1

    V1 Implementation (future):
        - Validate all 54 fields against 01_schema_hybrid.yaml
        - Range checking (e.g., Hb 0-25 g/dL)
        - Consistency checks (e.g., Hb vs Ht)

    Example:
        >>> validate_schema({"hb": 15.2, "age_years": 35})  # OK
        >>> validate_schema({})  # Raises ValueError
        Traceback (most recent call last):
        ...
        ValueError: CBC data cannot be empty
    """
    if not cbc_data:
        raise ValueError("CBC data cannot be empty")

    # V0: Basic check only
    # Full validation in Sprint 1


def get_analysis_summary(result: Dict[str, Any]) -> str:
    """
    Generate human-readable summary of analysis.

    Args:
        result: Analysis result from analyze_cbc()

    Returns:
        str: Human-readable summary

    Example:
        >>> result = {
        ...     "top_syndromes": ["S-TMA"],
        ...     "evidences_present": ["E-PLT-CRIT-LOW", "E-SCHISTOCYTES-GE1PCT"],
        ...     "route_id": "abc123...",
        ... }
        >>> summary = get_analysis_summary(result)
        >>> "S-TMA" in summary
        True
    """
    top_syndromes = result.get("top_syndromes", [])
    evidences_present = result.get("evidences_present", [])

    lines = []
    lines.append("=== HemoDoctor Analysis Summary ===")
    lines.append(f"Syndromes Detected: {len(top_syndromes)}")
    for syndrome_id in top_syndromes:
        lines.append(f"  - {syndrome_id}")
    lines.append(f"Evidences Present: {len(evidences_present)}")
    lines.append(f"Route ID: {result.get('route_id', 'N/A')}")

    return "\n".join(lines)
