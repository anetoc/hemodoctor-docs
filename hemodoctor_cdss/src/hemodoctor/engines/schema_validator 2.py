"""
Schema Validator - CBC Data Validation Engine

Validates CBC data against canonical schema (54 fields).
Implements fail-safe design (warnings only, never rejects cases).

Based on: 01_schema_hybrid.yaml v2.3.1

Validation Rules:
    - Type checking (float, int, string, dict)
    - Required fields check (hb, mcv, wbc)
    - Physiological range validation
    - LOINC code validation (optional)

Fail-Safe:
    - Never raises exceptions on validation errors
    - Returns warnings list for audit/review
    - Missing non-required fields → OK
    - Out-of-range values → Warning (not error)

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from typing import Dict, Any, List, Tuple


def validate_schema(
    cbc_data: Dict[str, Any],
    yaml_parser: Any = None,
    strict: bool = False
) -> Tuple[bool, List[str]]:
    """
    Validate CBC data against schema.

    Args:
        cbc_data: CBC data dictionary
        yaml_parser: YAMLParser instance (optional, for schema loading)
        strict: If True, fail on required field missing. If False, warn only.

    Returns:
        Tuple of (is_valid, warnings)
            - is_valid: True if passes validation (or fail-safe mode)
            - warnings: List of warning messages

    Required Fields (V0):
        - hb: Hemoglobin (g/dL)
        - mcv: Mean Corpuscular Volume (fL)
        - wbc: White Blood Cells (×10⁹/L)

    Optional Fields (54 total):
        - See 01_schema_hybrid.yaml for complete list

    Fail-Safe Mode (strict=False, default):
        - Missing required → Warning (not error)
        - Out-of-range → Warning (not error)
        - Invalid type → Warning (not error)
        - Returns (True, warnings)

    Strict Mode (strict=True):
        - Missing required → Returns (False, warnings)
        - Out-of-range → Warning only
        - Invalid type → Returns (False, warnings)

    Example:
        >>> cbc = {"hb": 15.2, "mcv": 88, "wbc": 8.5, "age_years": 35, "sex": "M"}
        >>> valid, warnings = validate_schema(cbc)
        >>> valid
        True
        >>> len(warnings)
        0

        >>> cbc = {"hb": "invalid"}  # Invalid type
        >>> valid, warnings = validate_schema(cbc, strict=False)
        >>> valid  # Fail-safe: True
        True
        >>> len(warnings)
        3

        >>> valid, warnings = validate_schema(cbc, strict=True)
        >>> valid  # Strict: False
        False
    """
    warnings = []

    # Define required fields (V0 - minimal set)
    required_fields = ["hb", "mcv", "wbc"]

    # Check required fields
    for field in required_fields:
        if field not in cbc_data or cbc_data[field] is None:
            warning = f"Campo obrigatório ausente: {field.upper()}"
            warnings.append(warning)

            if strict:
                return (False, warnings)

    # Define field schemas (subset for V0 - expand in V1)
    field_schemas = {
        "hb": {"type": "float", "range": (0, 25), "unit": "g/dL"},
        "ht": {"type": "float", "range": (0, 75), "unit": "%"},
        "rbc": {"type": "float", "range": (0, 10), "unit": "×10¹²/L"},
        "mcv": {"type": "float", "range": (50, 150), "unit": "fL"},
        "mch": {"type": "float", "range": (15, 50), "unit": "pg"},
        "mchc": {"type": "float", "range": (25, 38), "unit": "g/dL"},
        "rdw": {"type": "float", "range": (9, 20), "unit": "%"},
        "wbc": {"type": "float", "range": (0, 200), "unit": "×10⁹/L"},
        "anc": {"type": "float", "range": (0, 50), "unit": "×10⁹/L"},
        "lymphocytes_abs": {"type": "float", "range": (0, 50), "unit": "×10⁹/L"},
        "monocytes_abs": {"type": "float", "range": (0, 20), "unit": "×10⁹/L"},
        "eosinophils_abs": {"type": "float", "range": (0, 20), "unit": "×10⁹/L"},
        "basophils_abs": {"type": "float", "range": (0, 5), "unit": "×10⁹/L"},
        "plt": {"type": "float", "range": (0, 2000), "unit": "×10⁹/L"},
        "mpv": {"type": "float", "range": (5, 15), "unit": "fL"},
        "neutrophils_pct": {"type": "float", "range": (0, 100), "unit": "%"},
        "lymphocytes_pct": {"type": "float", "range": (0, 100), "unit": "%"},
        "monocytes_pct": {"type": "float", "range": (0, 100), "unit": "%"},
        "eosinophils_pct": {"type": "float", "range": (0, 100), "unit": "%"},
        "basophils_pct": {"type": "float", "range": (0, 100), "unit": "%"},
        "blasts_pct": {"type": "float", "range": (0, 100), "unit": "%"},
        "age_years": {"type": "float", "range": (0, 120), "unit": "anos"},
        "sex": {"type": "string", "enum": ["M", "F"], "unit": None},
    }

    # Validate each field
    for field, value in cbc_data.items():
        # Skip metadata fields
        if field.startswith("_"):
            continue

        # Skip if field not in schema (allow extra fields)
        if field not in field_schemas:
            continue

        schema = field_schemas[field]

        # Type validation
        expected_type = schema["type"]
        if expected_type == "float":
            if value is not None:
                try:
                    value = float(value)
                except (ValueError, TypeError):
                    warning = f"{field.upper()}: tipo inválido (esperado: float, recebido: {type(value).__name__})"
                    warnings.append(warning)

                    if strict:
                        return (False, warnings)
                    continue

        elif expected_type == "string":
            if value is not None and not isinstance(value, str):
                warning = f"{field.upper()}: tipo inválido (esperado: string, recebido: {type(value).__name__})"
                warnings.append(warning)

                if strict:
                    return (False, warnings)
                continue

        # Enum validation (for sex)
        if "enum" in schema:
            if value not in schema["enum"]:
                warning = f"{field.upper()}: valor inválido '{value}' (esperado: {schema['enum']})"
                warnings.append(warning)

        # Range validation
        if "range" in schema and value is not None:
            try:
                value_float = float(value)
                min_val, max_val = schema["range"]

                if value_float < min_val or value_float > max_val:
                    warning = (
                        f"{field.upper()}: {value_float} {schema.get('unit', '')} "
                        f"fora da faixa fisiológica ({min_val}-{max_val})"
                    )
                    warnings.append(warning)
                    # Range violations are warnings only (even in strict mode)
            except (ValueError, TypeError):
                pass

    # Final verdict
    is_valid = True if not strict else len(warnings) == 0

    return (is_valid, warnings)


def check_required_fields(cbc_data: Dict[str, Any]) -> List[str]:
    """
    Check if required fields are present.

    Args:
        cbc_data: CBC data dictionary

    Returns:
        List of missing required fields

    Required Fields:
        - hb: Hemoglobin
        - mcv: Mean Corpuscular Volume
        - wbc: White Blood Cells

    Example:
        >>> cbc = {"hb": 15.2, "mcv": 88}
        >>> missing = check_required_fields(cbc)
        >>> missing
        ['wbc']
    """
    required = ["hb", "mcv", "wbc"]
    missing = []

    for field in required:
        if field not in cbc_data or cbc_data[field] is None:
            missing.append(field)

    return missing


def validate_physiological_consistency(cbc_data: Dict[str, Any]) -> List[str]:
    """
    Validate physiological consistency between related fields.

    Args:
        cbc_data: CBC data dictionary

    Returns:
        List of consistency warnings

    Checks:
        - Hb/Ht/RBC relationship (Hb ~ Ht/3, MCH ~ Hb/RBC*10)
        - WBC differential sum (~100%)
        - ANC vs neutrophils_pct consistency

    Example:
        >>> cbc = {"hb": 15, "ht": 30, "rbc": 5}  # Inconsistent: Hb ~ Ht/3
        >>> warnings = validate_physiological_consistency(cbc)
        >>> len(warnings)
        1
    """
    warnings = []

    # Check Hb ~ Ht / 3 (rule of thumb)
    hb = cbc_data.get("hb")
    ht = cbc_data.get("ht")

    if hb is not None and ht is not None:
        try:
            expected_ht = hb * 3
            diff = abs(ht - expected_ht)

            # Allow 10% deviation
            if diff > expected_ht * 0.15:
                warnings.append(
                    f"Inconsistência Hb/Ht: Hb={hb} g/dL, Ht={ht}% "
                    f"(esperado: Ht ~ {expected_ht:.1f}%)"
                )
        except (ValueError, TypeError):
            pass

    # Check WBC differential sum (~100%)
    diff_fields = [
        "neutrophils_pct",
        "lymphocytes_pct",
        "monocytes_pct",
        "eosinophils_pct",
        "basophils_pct",
    ]

    diff_values = []
    for field in diff_fields:
        value = cbc_data.get(field)
        if value is not None:
            try:
                diff_values.append(float(value))
            except (ValueError, TypeError):
                pass

    if len(diff_values) >= 3:  # At least 3 components present
        total = sum(diff_values)

        # Allow 5% deviation from 100%
        if abs(total - 100) > 5:
            warnings.append(
                f"Soma do diferencial WBC: {total:.1f}% "
                f"(esperado: ~100%)"
            )

    # Check ANC vs neutrophils_pct consistency
    anc = cbc_data.get("anc")
    wbc = cbc_data.get("wbc")
    neut_pct = cbc_data.get("neutrophils_pct")

    if anc is not None and wbc is not None and neut_pct is not None:
        try:
            expected_anc = wbc * neut_pct / 100.0
            diff = abs(anc - expected_anc)

            # Allow 10% deviation
            if diff > expected_anc * 0.15:
                warnings.append(
                    f"Inconsistência ANC: ANC={anc:.2f}, "
                    f"WBC={wbc:.2f}, neutrófilos%={neut_pct:.1f}% "
                    f"(esperado ANC: {expected_anc:.2f})"
                )
        except (ValueError, TypeError, ZeroDivisionError):
            pass

    return warnings
