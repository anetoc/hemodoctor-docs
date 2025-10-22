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
from datetime import datetime, timezone

from hemodoctor.utils.yaml_parser import YAMLParser
from hemodoctor.engines.evidence import evaluate_all_evidences, get_present_evidences
from hemodoctor.engines.syndrome import detect_syndromes, detect_all_syndromes, generate_alt_routes
from hemodoctor.engines.normalization import normalize_cbc as normalize_units
from hemodoctor.engines.schema_validator import validate_schema as validate_cbc_schema
from hemodoctor.engines.next_steps import generate_next_steps
from hemodoctor.engines.worm_log import log_to_worm
from hemodoctor.engines.output_renderer import render_output


def compute_route_id(
    evidences: List,
    syndromes: List,
    alt_routes: List[Dict[str, Any]] = None
) -> str:
    """
    Compute deterministic SHA256 hash for routing/audit.

    Args:
        evidences: List of EvidenceResult objects
        syndromes: List of SyndromeResult objects
        alt_routes: Optional list of alternative routes (v2.6.0+)

    Returns:
        str: SHA256 hash (64 hex chars)

    Determinism:
        - Same input always produces same hash
        - Used for routing, audit trail, deduplication
        - Alt_routes included for complete traceability (v2.6.0+)

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

    # Extract alt_route syndrome IDs (sorted for determinism)
    alt_route_ids = []
    if alt_routes:
        alt_route_ids = sorted([r["syndrome_id"] for r in alt_routes])

    # Build deterministic data structure
    route_data = {
        "evidences": present_evidence_ids,
        "syndromes": syndrome_ids,
        "alt_routes": alt_route_ids,  # v2.6.0+
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

    # 2. Normalize units (with heuristics + conversion log)
    normalized_cbc, conversion_log = normalize_units(cbc_data, yaml_parser)

    # 3. Validate schema (full validation with warnings)
    is_valid, validation_warnings = validate_cbc_schema(normalized_cbc, yaml_parser, strict=False)

    # 4. Evidences (79 rules)
    evidences = evaluate_all_evidences(normalized_cbc, yaml_parser)

    # 5. Syndromes (35 syndromes, short-circuit on critical)
    syndromes = detect_syndromes(evidences, yaml_parser)

    # 5b. All syndromes (for alt_routes - v2.6.0+)
    all_syndromes = detect_all_syndromes(evidences, yaml_parser)

    # 5c. Alternative routes (v2.6.0+)
    alt_routes = generate_alt_routes(syndromes, all_syndromes, evidences, yaml_parser)

    # 6. Next Steps (40 triggers)
    next_steps_list = generate_next_steps(syndromes, evidences, normalized_cbc, yaml_parser)

    # 7. Routing (deterministic hash with alt_routes)
    route_id = compute_route_id(evidences, syndromes, alt_routes)

    # 8. WORM Log (audit trail)
    log_to_worm(cbc_data, syndromes, evidences, route_id, yaml_parser)

    # 9. Build result
    result = {
        "top_syndromes": [s.id for s in syndromes],
        "evidences_present": [e.id for e in evidences if e.status == "present"],
        "alt_routes": alt_routes,  # v2.6.0+
        "route_id": route_id,
        "version": "2.6.0",  # Updated for alt_routes feature
        "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
        "next_steps": next_steps_list,
        "conversion_log": conversion_log,
        "validation_warnings": validation_warnings,
        "syndromes_detail": [
            {
                "id": s.id,
                "criticality": s.criticality,
                "actions": s.actions,
                "next_steps": s.next_steps,
            }
            for s in syndromes
        ],
        "evidences_detail": [
            {
                "id": e.id,
                "status": e.status,
                "strength": e.strength,
            }
            for e in evidences
            if e.status == "present"
        ],
    }

    return result


# Note: normalize_cbc and validate_schema are now imported from engines
# (normalization.py and schema_validator.py)


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
