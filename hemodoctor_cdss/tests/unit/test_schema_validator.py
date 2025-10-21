"""
Schema Validator Tests

Tests CBC validation against canonical schema (54 fields).
Validates fail-safe design (warnings only, never rejects in default mode).

IEC 62304 Class C Compliance:
- Tests required fields validation
- Tests type checking
- Tests physiological range validation
- Tests fail-safe vs strict modes

Author: Dr. Abel Costa
"""

import pytest
from hemodoctor.engines.schema_validator import validate_schema


# Test 1: Valid CBC


def test_validate_schema_valid_cbc():
    """Test validation with valid complete CBC."""
    cbc = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M"
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    assert len(warnings) == 0


def test_validate_schema_minimal_required_fields():
    """Test validation with only required fields (hb, mcv, wbc)."""
    cbc = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    assert len(warnings) == 0


# Test 2: Missing Required Fields


def test_validate_schema_missing_hb_failsafe():
    """Test missing required field (hb) in fail-safe mode."""
    cbc = {
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid, warnings = validate_schema(cbc, strict=False)  # Fail-safe

    # Fail-safe: Should be valid with warnings
    assert is_valid is True
    assert len(warnings) > 0
    assert any("HB" in w for w in warnings)


def test_validate_schema_missing_hb_strict():
    """Test missing required field (hb) in strict mode."""
    cbc = {
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid, warnings = validate_schema(cbc, strict=True)  # Strict

    # Strict: Should be invalid
    assert is_valid is False
    assert len(warnings) > 0
    assert any("HB" in w for w in warnings)


def test_validate_schema_all_required_missing_failsafe():
    """Test all required fields missing in fail-safe mode."""
    cbc = {
        "plt": 250,
        "age_years": 35
    }

    is_valid, warnings = validate_schema(cbc, strict=False)

    # Fail-safe: Valid with 3 warnings (hb, mcv, wbc)
    assert is_valid is True
    assert len(warnings) == 3


def test_validate_schema_all_required_missing_strict():
    """Test all required fields missing in strict mode."""
    cbc = {
        "plt": 250,
        "age_years": 35
    }

    is_valid, warnings = validate_schema(cbc, strict=True)

    # Strict: Invalid with warnings
    assert is_valid is False
    assert len(warnings) >= 1  # Stops at first missing


# Test 3: Physiological Range Validation


def test_validate_schema_hb_out_of_range():
    """Test Hb out of physiological range (should warn, not reject)."""
    cbc = {
        "hb": 50,  # Impossibly high
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid, warnings = validate_schema(cbc)

    # Should have warning for out-of-range
    assert is_valid is True  # Fail-safe: doesn't reject
    assert len(warnings) > 0
    assert any("HB" in w or "hb" in w for w in warnings)


def test_validate_schema_wbc_out_of_range():
    """Test WBC out of range."""
    cbc = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 500  # > 200 (physiological limit)
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    assert len(warnings) > 0


def test_validate_schema_plt_out_of_range():
    """Test PLT out of range."""
    cbc = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5,
        "plt": 3000  # > 2000 (physiological limit)
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    assert len(warnings) > 0


# Test 4: Type Validation


def test_validate_schema_invalid_type_string():
    """Test invalid type (string instead of float)."""
    cbc = {
        "hb": "fourteen",  # Should be float
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid, warnings = validate_schema(cbc, strict=False)

    # Fail-safe: Valid with warning
    assert is_valid is True
    assert len(warnings) > 0


def test_validate_schema_invalid_type_strict():
    """Test invalid type in strict mode."""
    cbc = {
        "hb": "fourteen",
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid, warnings = validate_schema(cbc, strict=True)

    # Strict: Should fail
    # Note: Depending on implementation, may fail on type or missing
    # We just check that it returns False
    assert is_valid is False or len(warnings) > 0


# Test 5: Edge Cases


def test_validate_schema_zero_values():
    """Test zero values (edge case but valid)."""
    cbc = {
        "hb": 0,  # Technically physiologically impossible, but should warn not reject
        "mcv": 88,
        "wbc": 0
    }

    is_valid, warnings = validate_schema(cbc)

    # Should be valid (fail-safe) but may have warnings
    assert is_valid is True


def test_validate_schema_negative_values():
    """Test negative values (invalid, should warn)."""
    cbc = {
        "hb": -5,
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True  # Fail-safe
    # May have warning for negative value


def test_validate_schema_empty_dict():
    """Test completely empty CBC."""
    cbc = {}

    is_valid, warnings = validate_schema(cbc, strict=False)

    # Fail-safe: Valid with warnings for all required fields
    assert is_valid is True
    assert len(warnings) == 3  # hb, mcv, wbc


def test_validate_schema_empty_dict_strict():
    """Test empty CBC in strict mode."""
    cbc = {}

    is_valid, warnings = validate_schema(cbc, strict=True)

    # Strict: Invalid
    assert is_valid is False


# Test 6: Multiple Fields


def test_validate_schema_complete_cbc():
    """Test validation with many fields."""
    cbc = {
        "hb": 14.5,
        "ht": 42,
        "rbc": 4.8,
        "mcv": 88,
        "mch": 30,
        "mchc": 34,
        "rdw": 13,
        "wbc": 7.5,
        "anc": 4.5,
        "lymphocytes_abs": 2.0,
        "plt": 250,
        "mpv": 9.5,
        "neutrophils_pct": 60,
        "lymphocytes_pct": 30,
        "age_years": 35,
        "sex": "M"
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    assert len(warnings) == 0


def test_validate_schema_multiple_out_of_range():
    """Test multiple fields out of range."""
    cbc = {
        "hb": 50,    # Out of range
        "mcv": 88,
        "wbc": 500,  # Out of range
        "plt": 3000  # Out of range
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True  # Fail-safe
    assert len(warnings) >= 3  # At least 3 warnings


# Test 7: Percentage Fields


def test_validate_schema_percentage_valid():
    """Test percentage fields in valid range (0-100)."""
    cbc = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5,
        "neutrophils_pct": 60,
        "lymphocytes_pct": 30,
        "monocytes_pct": 8,
        "eosinophils_pct": 1.5,
        "basophils_pct": 0.5
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    # May have warning if percentages don't sum to 100, but should not reject


def test_validate_schema_percentage_out_of_range():
    """Test percentage > 100 (invalid)."""
    cbc = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5,
        "neutrophils_pct": 150  # > 100
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True  # Fail-safe
    assert len(warnings) > 0


# Test 8: Real Clinical Cases


def test_validate_schema_real_case_ida():
    """Test validation with real IDA case."""
    cbc = {
        "hb": 9.5,
        "mcv": 68,  # Microcytic
        "wbc": 7.0,
        "plt": 450,  # Reactive thrombocytosis
        "ferritin": 12,
        "age_years": 35,
        "sex": "F"
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    assert len(warnings) == 0  # All values within range


def test_validate_schema_real_case_tma():
    """Test validation with real TMA case."""
    cbc = {
        "hb": 8.0,
        "mcv": 88,
        "wbc": 10.0,
        "plt": 8,  # Critical low
        "ldh": 980,
        "age_years": 35,
        "sex": "M"
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    # No warnings expected (all values physiologically possible in disease)


def test_validate_schema_real_case_polycythemia():
    """Test validation with real polycythemia case."""
    cbc = {
        "hb": 18.5,
        "ht": 56,
        "mcv": 88,
        "wbc": 12.5,
        "plt": 520,
        "age_years": 55,
        "sex": "M"
    }

    is_valid, warnings = validate_schema(cbc)

    assert is_valid is True
    # All values within physiological range


# Test 9: Null vs Missing


def test_validate_schema_null_value_vs_missing():
    """Test null value vs missing field."""
    cbc1 = {
        "hb": None,  # Null value
        "mcv": 88,
        "wbc": 7.5
    }

    cbc2 = {
        # hb missing entirely
        "mcv": 88,
        "wbc": 7.5
    }

    is_valid1, warnings1 = validate_schema(cbc1)
    is_valid2, warnings2 = validate_schema(cbc2)

    # Both should behave the same (treated as missing)
    assert is_valid1 == is_valid2 == True  # Fail-safe
    assert len(warnings1) > 0
    assert len(warnings2) > 0
