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
from simpleeval import simple_eval, EvalWithCompoundTypes, DEFAULT_NAMES, DEFAULT_FUNCTIONS
from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.utils.yaml_parser import YAMLParser


class DictWrapper:
    """Wrapper that allows dict access via dot notation for simpleeval"""
    def __init__(self, data: dict):
        self._data = data

    def __getattr__(self, key):
        try:
            return self._data[key]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{key}'")


def derive_age_sex_group(age_years: float, sex: str) -> str:
    """
    Derive age/sex group for cutoff selection.

    Args:
        age_years: Age in years
        sex: M/F/U

    Returns:
        str: Age/sex group key (e.g., "adult_m", "pediatric_1_3y")

    Groups:
        - adult_m: Age ≥18, Male
        - adult_f: Age ≥18, Female
        - pediatric_0_28d: 0-28 days (~0-0.077 years)
        - pediatric_1_12m: 1-12 months (0.077-1 years)
        - pediatric_1_3y: 1-3 years
        - pediatric_4_12y: 4-12 years
        - pediatric_13_18y: 13-17 years

    Example:
        >>> derive_age_sex_group(35, "M")
        'adult_m'
        >>> derive_age_sex_group(2.5, "F")
        'pediatric_1_3y'
    """
    # Adults (≥18 years)
    if age_years >= 18:
        if sex == "M":
            return "adult_m"
        elif sex == "F":
            return "adult_f"
        else:  # U (unknown)
            return "adult_m"  # Default to male cutoffs (conservative)

    # Pediatric age groups
    if age_years < 0.077:  # ~28 days
        return "pediatric_0_28d"
    elif age_years < 1:
        return "pediatric_1_12m"
    elif age_years < 4:
        return "pediatric_1_3y"
    elif age_years < 13:
        return "pediatric_4_12y"
    else:  # 13-17
        return "pediatric_13_18y"


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

    # Derive age_sex_group from CBC (required for age/sex-adjusted cutoffs)
    age_years = cbc.get("age_years")
    sex = cbc.get("sex", "M")  # Default to M if missing (conservative)

    if age_years is None:
        age_sex_group = "adult_m"  # Default if age missing
    else:
        age_sex_group = derive_age_sex_group(age_years, sex)

    # Build safe evaluation context
    # CRITICAL: Expose config object (not just cutoffs) + age_sex_group
    # YAML rules use: config.cutoffs.hb_critical_low[age_sex_group]
    names = {
        **cbc,
        "config": config,  # Expose entire config object
        "age_sex_group": age_sex_group,  # Derived from age/sex
        "true": True,  # YAML-style boolean (lowercase)
        "false": False,  # YAML-style boolean (lowercase)
    }

    # Handle morphology namespace (nested dict)
    # Support both dot notation (morphology.esquistocitos) and flat (esquistocitos)
    if "morphology" in cbc and isinstance(cbc["morphology"], dict):
        # Create DictWrapper that supports dot notation for simpleeval
        names["morphology"] = DictWrapper(cbc["morphology"])
        # Also add flat keys for backward compatibility
        names.update(cbc["morphology"])

    # Safe evaluation using simpleeval with compound types (allows object attributes)
    try:
        evaluator = EvalWithCompoundTypes(names=names)
        result = evaluator.eval(rule)

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
