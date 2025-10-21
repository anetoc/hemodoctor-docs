"""
Evidence Engine - Evaluates 79 Clinical Evidence Rules

This module implements safe evaluation of clinical evidence rules using
simpleeval (NEVER eval()). Handles tri-state logic and missing data gracefully.

Based on: 02_evidence_hybrid.yaml v2.4.0 (79 evidences)

Safety:
- Uses simpleeval for expression evaluation
- Handles missing data (returns "unknown")
- Never uses eval() or exec()
- All field access uses .get() with None checks

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from typing import List, Dict, Any, Optional
from simpleeval import simple_eval
from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.utils.yaml_parser import YAMLParser


def evaluate_evidence(
    evidence_def: Dict[str, Any],
    cbc: Dict[str, Any],
    config: Dict[str, Any]
) -> str:
    """
    Evaluate a single clinical evidence rule.

    Args:
        evidence_def: Evidence definition from YAML (id, rule, requires, etc.)
        cbc: CBC data dictionary (normalized)
        config: Configuration dictionary (cutoffs, units, etc.)

    Returns:
        str: "present" | "absent" | "unknown"

    Safety:
        - Uses simpleeval (NEVER eval())
        - Returns "unknown" for missing required fields
        - Returns "unknown" on any evaluation error

    Example:
        >>> evidence_def = {
        ...     "id": "E-ANC-CRIT",
        ...     "rule": "anc < 0.5",
        ...     "requires": ["anc"]
        ... }
        >>> cbc = {"anc": 0.3}
        >>> config = {"cutoffs": {"anc_critical": 0.5}}
        >>> evaluate_evidence(evidence_def, cbc, config)
        'present'
    """
    rule = evidence_def.get("rule", "")
    requires = evidence_def.get("requires", [])

    if not rule:
        return "unknown"

    # Check if all required fields are present (not None)
    for field in requires:
        if cbc.get(field) is None:
            return "unknown"

    # Build safe evaluation context
    # Combine CBC data + config cutoffs
    names = {**cbc, **config.get("cutoffs", {})}

    # Handle morphology namespace
    if "morphology" in cbc and isinstance(cbc["morphology"], dict):
        # Add morphology fields to namespace (e.g., esquistocitos, esferocitos)
        names.update(cbc["morphology"])

    # Safe evaluation using simpleeval
    try:
        result = simple_eval(rule, names=names)

        # Convert to tri-state
        if result is True:
            return "present"
        elif result is False:
            return "absent"
        else:
            return "unknown"

    except (KeyError, TypeError, ValueError, NameError, AttributeError):
        # Missing field or evaluation error → unknown
        return "unknown"
    except Exception:
        # Any other error → fail safe to unknown
        return "unknown"


def evaluate_all_evidences(
    cbc: Dict[str, Any],
    yaml_parser: YAMLParser
) -> List[EvidenceResult]:
    """
    Evaluate all 79 clinical evidences from YAML.

    Args:
        cbc: CBC data dictionary (normalized)
        yaml_parser: YAMLParser singleton instance

    Returns:
        List of EvidenceResult objects (79 total)

    Example:
        >>> from hemodoctor.utils.yaml_parser import YAMLParser
        >>> parser = YAMLParser.get_instance()
        >>> cbc = {"hb": 8.2, "anc": 0.3, "plt": 45, "age_years": 35, "sex": "M"}
        >>> evidences = evaluate_all_evidences(cbc, parser)
        >>> len(evidences)
        79
        >>> critical_evidences = [e for e in evidences if e.status == "present" and e.strength == "strong"]
    """
    evidence_defs = yaml_parser.get_all_evidence_defs()
    config = yaml_parser.config

    results = []

    for evidence_def in evidence_defs:
        status = evaluate_evidence(evidence_def, cbc, config)

        result = EvidenceResult(
            id=evidence_def["id"],
            status=status,
            strength=evidence_def.get("strength", "moderate"),
            requires=evidence_def.get("requires", []),
            clinical_significance=evidence_def.get("clinical_significance", ""),
            rule=evidence_def.get("rule", ""),
        )

        results.append(result)

    return results


def get_present_evidences(evidences: List[EvidenceResult]) -> List[EvidenceResult]:
    """
    Filter evidences to only those present.

    Args:
        evidences: List of all evidence results

    Returns:
        List of present evidences only

    Example:
        >>> evidences = [
        ...     EvidenceResult(id="E-ANC-CRIT", status="present", strength="strong"),
        ...     EvidenceResult(id="E-PLT-LOW", status="absent", strength="moderate"),
        ... ]
        >>> present = get_present_evidences(evidences)
        >>> len(present)
        1
        >>> present[0].id
        'E-ANC-CRIT'
    """
    return [e for e in evidences if e.status == "present"]


def get_unknown_evidences(evidences: List[EvidenceResult]) -> List[EvidenceResult]:
    """
    Filter evidences to only those with unknown status (missing data).

    Args:
        evidences: List of all evidence results

    Returns:
        List of unknown evidences

    Example:
        >>> evidences = [
        ...     EvidenceResult(id="E-ANC-CRIT", status="unknown", strength="strong"),
        ...     EvidenceResult(id="E-PLT-LOW", status="present", strength="moderate"),
        ... ]
        >>> unknown = get_unknown_evidences(evidences)
        >>> len(unknown)
        1
    """
    return [e for e in evidences if e.status == "unknown"]


def get_missing_rate(evidences: List[EvidenceResult]) -> float:
    """
    Calculate proportion of evidences with unknown status.

    Args:
        evidences: List of all evidence results

    Returns:
        Missing rate (0.0 to 1.0)

    Example:
        >>> evidences = [
        ...     EvidenceResult(id="E-1", status="present", strength="high"),
        ...     EvidenceResult(id="E-2", status="unknown", strength="high"),
        ...     EvidenceResult(id="E-3", status="absent", strength="high"),
        ... ]
        >>> get_missing_rate(evidences)
        0.333...
    """
    if not evidences:
        return 0.0

    unknown_count = len(get_unknown_evidences(evidences))
    return unknown_count / len(evidences)
