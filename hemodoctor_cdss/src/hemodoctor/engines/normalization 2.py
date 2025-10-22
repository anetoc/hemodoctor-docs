"""
Normalization Engine - CBC Unit Conversion

Converts CBC values to canonical units using heuristics.
Implements fail-safe design (never rejects cases, always logs conversions).

Based on: 07_normalization_heuristics.yaml v1.0.0

Canonical Units (per 01_schema_hybrid.yaml):
    - WBC, PLT, ANC, lymphocytes_abs, monocytes_abs, eosinophils_abs, basophils_abs: ×10⁹/L
    - Hb: g/dL
    - Ht: % (0-100)
    - RBC: ×10¹²/L
    - MCV, MCH, MCHC, RDW: As measured

V0 Implementation:
    - Single-case heuristics only (fallback mode)
    - Batch-based (p50) and site-specific learning deferred to V1

Safety:
    - Fail-safe: Never rejects case on conversion error
    - Audit log: All conversions logged for traceability
    - Physiological validation: Detects impossible values

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from typing import Dict, Any, List, Tuple
from copy import deepcopy


def normalize_cbc(
    cbc_data: Dict[str, Any],
    yaml_parser: Any = None
) -> Tuple[Dict[str, Any], List[str]]:
    """
    Normalize CBC units to canonical format.

    Args:
        cbc_data: Raw CBC data dictionary
        yaml_parser: YAMLParser instance (optional, for V1)

    Returns:
        Tuple of (normalized_cbc, conversion_log)
            - normalized_cbc: CBC with canonical units
            - conversion_log: List of conversion messages for audit trail

    Canonical Units:
        - WBC, PLT, ANC, lymphocytes_abs, etc.: ×10⁹/L
        - Hb: g/dL
        - Ht: % (0-100)
        - RBC: ×10¹²/L

    Heuristics (V0 - single case):
        - WBC > 200 → Divide by 1000 (assumed /μL)
        - PLT > 2000 → Divide by 1000 (assumed /μL)
        - ANC > 50 → Divide by 1000 (assumed /μL)
        - Hb > 25 → Divide by 10 (assumed g/L)
        - lymphocytes_abs > 50 → Divide by 1000
        - monocytes_abs > 20 → Divide by 1000
        - eosinophils_abs > 20 → Divide by 1000
        - basophils_abs > 5 → Divide by 1000

    Example:
        >>> cbc = {"wbc": 8500, "plt": 250000, "hb": 152, "age_years": 35, "sex": "M"}
        >>> normalized, log = normalize_cbc(cbc)
        >>> normalized["wbc"]
        8.5
        >>> normalized["plt"]
        250.0
        >>> normalized["hb"]
        15.2
        >>> len(log)
        3
    """
    # Deep copy to avoid mutating input
    normalized = deepcopy(cbc_data)
    conversion_log = []

    # Define normalization rules (V0 - fallback single case)
    rules = [
        # WBC (leucócitos)
        {
            "field": "wbc",
            "threshold": 200,
            "divisor": 1000,
            "canonical_unit": "×10⁹/L",
            "inferred_unit": "/μL",
            "reason": "WBC fisiologicamente impossível >200×10⁹/L; assumido /μL"
        },
        # PLT (plaquetas)
        {
            "field": "plt",
            "threshold": 2000,
            "divisor": 1000,
            "canonical_unit": "×10⁹/L",
            "inferred_unit": "/μL",
            "reason": "PLT fisiologicamente impossível >2000×10⁹/L; assumido /μL"
        },
        # ANC (neutrófilos absolutos)
        {
            "field": "anc",
            "threshold": 50,
            "divisor": 1000,
            "canonical_unit": "×10⁹/L",
            "inferred_unit": "/μL",
            "reason": "ANC fisiologicamente improvável >50×10⁹/L; assumido /μL"
        },
        # Linfócitos absolutos
        {
            "field": "lymphocytes_abs",
            "threshold": 50,
            "divisor": 1000,
            "canonical_unit": "×10⁹/L",
            "inferred_unit": "/μL",
            "reason": "Linfócitos absolutos fisiologicamente improvável >50×10⁹/L; assumido /μL"
        },
        # Monócitos absolutos
        {
            "field": "monocytes_abs",
            "threshold": 20,
            "divisor": 1000,
            "canonical_unit": "×10⁹/L",
            "inferred_unit": "/μL",
            "reason": "Monócitos absolutos fisiologicamente impossível >20×10⁹/L; assumido /μL"
        },
        # Eosinófilos absolutos
        {
            "field": "eosinophils_abs",
            "threshold": 20,
            "divisor": 1000,
            "canonical_unit": "×10⁹/L",
            "inferred_unit": "/μL",
            "reason": "Eosinófilos absolutos fisiologicamente impossível >20×10⁹/L; assumido /μL"
        },
        # Basófilos absolutos
        {
            "field": "basophils_abs",
            "threshold": 5,
            "divisor": 1000,
            "canonical_unit": "×10⁹/L",
            "inferred_unit": "/μL",
            "reason": "Basófilos absolutos fisiologicamente impossível >5×10⁹/L; assumido /μL"
        },
        # Hb (hemoglobina) - g/L → g/dL
        {
            "field": "hb",
            "threshold": 25,
            "divisor": 10,
            "canonical_unit": "g/dL",
            "inferred_unit": "g/L",
            "reason": "Hb fisiologicamente impossível >25 g/dL; assumido g/L"
        },
    ]

    # Apply rules
    for rule in rules:
        field = rule["field"]
        value = normalized.get(field)

        # Skip if field missing or not numeric
        if value is None:
            continue

        try:
            value = float(value)
        except (ValueError, TypeError):
            continue

        # Check threshold
        if value > rule["threshold"]:
            # Convert
            original_value = value
            converted_value = value / rule["divisor"]
            normalized[field] = converted_value

            # Log conversion
            log_msg = (
                f"{field.upper()}: {original_value} {rule['inferred_unit']} "
                f"→ {converted_value:.2f} {rule['canonical_unit']} "
                f"({rule['reason']})"
            )
            conversion_log.append(log_msg)

    return normalized, conversion_log


def validate_physiological_ranges(
    cbc_data: Dict[str, Any]
) -> List[str]:
    """
    Validate CBC values against physiological ranges (warnings only).

    Args:
        cbc_data: Normalized CBC data

    Returns:
        List of warning messages for out-of-range values

    Ranges (extreme bounds for validation):
        - WBC: 0.1 - 200 ×10⁹/L
        - PLT: 1 - 2000 ×10⁹/L
        - Hb: 2 - 25 g/dL
        - ANC: 0 - 50 ×10⁹/L
        - RBC: 0.5 - 10 ×10¹²/L
        - Ht: 5 - 75 %
        - MCV: 40 - 150 fL

    Note:
        - Never rejects case (fail-safe)
        - Warnings only for audit/review

    Example:
        >>> cbc = {"wbc": 300, "plt": 5, "hb": 2.5}
        >>> warnings = validate_physiological_ranges(cbc)
        >>> len(warnings)
        2
    """
    warnings = []

    # Define ranges
    ranges = {
        "wbc": (0.1, 200, "×10⁹/L"),
        "plt": (1, 2000, "×10⁹/L"),
        "hb": (2, 25, "g/dL"),
        "anc": (0, 50, "×10⁹/L"),
        "rbc": (0.5, 10, "×10¹²/L"),
        "ht": (5, 75, "%"),
        "mcv": (40, 150, "fL"),
        "lymphocytes_abs": (0, 50, "×10⁹/L"),
        "monocytes_abs": (0, 20, "×10⁹/L"),
        "eosinophils_abs": (0, 20, "×10⁹/L"),
        "basophils_abs": (0, 5, "×10⁹/L"),
    }

    for field, (min_val, max_val, unit) in ranges.items():
        value = cbc_data.get(field)

        if value is None:
            continue

        try:
            value = float(value)
        except (ValueError, TypeError):
            warnings.append(f"{field.upper()}: valor não numérico ({value})")
            continue

        if value < min_val or value > max_val:
            warnings.append(
                f"{field.upper()}: {value} {unit} fora da faixa fisiológica "
                f"({min_val}-{max_val} {unit})"
            )

    return warnings


def compute_absolute_counts(cbc_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compute absolute counts from percentages if missing.

    Args:
        cbc_data: CBC data (normalized)

    Returns:
        CBC data with computed absolute counts (if WBC available)

    Formulas:
        - ANC = WBC × neutrophils_pct / 100
        - lymphocytes_abs = WBC × lymphocytes_pct / 100
        - monocytes_abs = WBC × monocytes_pct / 100
        - eosinophils_abs = WBC × eosinophils_pct / 100
        - basophils_abs = WBC × basophils_pct / 100

    Example:
        >>> cbc = {"wbc": 10.0, "neutrophils_pct": 60, "lymphocytes_pct": 30}
        >>> computed = compute_absolute_counts(cbc)
        >>> computed["anc"]
        6.0
        >>> computed["lymphocytes_abs"]
        3.0
    """
    cbc = deepcopy(cbc_data)
    wbc = cbc.get("wbc")

    if wbc is None:
        return cbc

    # Compute absolute counts from percentages
    percentages = {
        "neutrophils_pct": "anc",
        "lymphocytes_pct": "lymphocytes_abs",
        "monocytes_pct": "monocytes_abs",
        "eosinophils_pct": "eosinophils_abs",
        "basophils_pct": "basophils_abs",
    }

    for pct_field, abs_field in percentages.items():
        # Skip if absolute already present
        if cbc.get(abs_field) is not None:
            continue

        # Compute from percentage
        pct_value = cbc.get(pct_field)
        if pct_value is not None:
            try:
                pct_value = float(pct_value)
                abs_value = wbc * pct_value / 100.0
                cbc[abs_field] = abs_value
            except (ValueError, TypeError):
                pass

    return cbc


def apply_age_sex_cutoffs(
    cbc_data: Dict[str, Any],
    yaml_parser: Any
) -> Dict[str, Any]:
    """
    Apply age/sex-specific cutoffs for interpretation.

    Args:
        cbc_data: Normalized CBC data
        yaml_parser: YAMLParser instance

    Returns:
        CBC data with added cutoff values for evidence evaluation

    Cutoffs (from 00_config_hybrid.yaml):
        - Hb, Ht: Age/sex specific
        - WBC, PLT, ANC: Age specific (infant vs adult)

    Note:
        - Cutoffs stored as metadata (not mutating original values)
        - Used by evidence engine for dynamic thresholds

    Example:
        >>> cbc = {"hb": 13.5, "age_years": 10, "sex": "M"}
        >>> with_cutoffs = apply_age_sex_cutoffs(cbc, yaml_parser)
        >>> with_cutoffs["_cutoffs"]["hb_lower"]  # Pediatric male cutoff
        11.5
    """
    cbc = deepcopy(cbc_data)

    # Get age and sex
    age_years = cbc.get("age_years")
    sex = cbc.get("sex")

    if age_years is None or sex is None:
        # Cannot apply age/sex cutoffs without both
        return cbc

    # Load cutoffs from config (00_config_hybrid.yaml)
    config = yaml_parser.config if yaml_parser else {}
    cutoffs_config = config.get("cutoffs", {})

    # Add cutoffs as metadata
    cbc["_cutoffs"] = {}

    # Hb cutoffs (age/sex specific)
    if age_years < 18:
        # Pediatric
        if sex == "M":
            cbc["_cutoffs"]["hb_lower"] = 11.5  # Example - load from YAML
        else:
            cbc["_cutoffs"]["hb_lower"] = 11.0
    else:
        # Adult
        if sex == "M":
            cbc["_cutoffs"]["hb_lower"] = 13.0
        else:
            cbc["_cutoffs"]["hb_lower"] = 12.0

    # TODO: Load actual cutoffs from 00_config_hybrid.yaml in V1

    return cbc
