"""
Normalization Engine Tests

Tests unit conversion heuristics and validation for CBC normalization.
Covers the 8 key normalization scenarios from YAML config.

IEC 62304 Class C Compliance:
- Tests physiological validation
- Tests conversion accuracy
- Tests edge cases and missing data

Author: Dr. Abel Costa
"""

import pytest
from hemodoctor.engines.normalization import (
    normalize_cbc,
    compute_absolute_counts,
)


# Test 1: WBC /1000 Conversion


def test_normalize_wbc_per_1000_conversion():
    """Test WBC /1000 conversion when WBC >200."""
    cbc_input = {
        "wbc": 7500,  # Should be divided by 1000 → 7.5
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["wbc"] == 7.5, \
        f"Expected 7.5, got {normalized['wbc']}"
    assert len(log) > 0, "Expected conversion log entry"
    assert any("WBC" in entry and "7500" in entry for entry in log)


def test_normalize_wbc_edge_case_200():
    """Test WBC edge case at exactly 200 (no conversion)."""
    cbc_input = {
        "wbc": 200,  # Exactly 200 → no conversion
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    # Should NOT convert (threshold is >200, not >=200)
    assert normalized["wbc"] == 200
    assert len(log) == 0, "Should not convert at threshold"


def test_normalize_wbc_below_threshold():
    """Test WBC below threshold (no conversion)."""
    cbc_input = {
        "wbc": 15.5,  # Normal value
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["wbc"] == 15.5
    assert len(log) == 0


# Test 2: PLT /1000 Conversion


def test_normalize_plt_per_1000_conversion():
    """Test PLT /1000 conversion when PLT >2000."""
    cbc_input = {
        "plt": 250000,  # Should be divided by 1000 → 250
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["plt"] == 250
    assert len(log) > 0
    assert any("PLT" in entry and "250000" in entry for entry in log)


def test_normalize_plt_edge_case_2000():
    """Test PLT edge case at exactly 2000 (no conversion)."""
    cbc_input = {
        "plt": 2000,  # Exactly 2000 → no conversion
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["plt"] == 2000
    assert len(log) == 0


# Test 3: Hb /10 Conversion


def test_normalize_hb_per_10_conversion():
    """Test Hb /10 conversion when Hb >25."""
    cbc_input = {
        "hb": 145,  # Should be divided by 10 → 14.5
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["hb"] == 14.5
    assert len(log) > 0
    assert any("HB" in entry for entry in log)


def test_normalize_hb_edge_case_25():
    """Test Hb edge case at exactly 25 (no conversion)."""
    cbc_input = {
        "hb": 25,  # Exactly 25 → no conversion
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["hb"] == 25
    assert len(log) == 0


# Test 4: No Conversion Needed


def test_normalize_no_conversion_needed():
    """Test that normal values are not converted."""
    cbc_input = {
        "wbc": 7.5,
        "plt": 250,
        "hb": 14.5,
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    # Should be unchanged
    assert normalized["wbc"] == 7.5
    assert normalized["plt"] == 250
    assert normalized["hb"] == 14.5
    assert len(log) == 0, "No conversions should occur"


# Test 5: Multiple Conversions


def test_normalize_multiple_conversions():
    """Test multiple simultaneous conversions."""
    cbc_input = {
        "wbc": 7500,   # /1000 → 7.5
        "plt": 250000, # /1000 → 250
        "hb": 145,     # /10 → 14.5
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["wbc"] == 7.5
    assert normalized["plt"] == 250
    assert normalized["hb"] == 14.5
    assert len(log) == 3, f"Expected 3 conversions, got {len(log)}"


# Test 6: Missing Data Handling


def test_normalize_missing_fields():
    """Test normalization with missing CBC fields."""
    cbc_input = {
        "wbc": 7500,  # Will convert
        # No plt, hb
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["wbc"] == 7.5
    assert "plt" not in normalized
    assert "hb" not in normalized
    assert len(log) == 1


def test_normalize_empty_cbc():
    """Test normalization with minimal data."""
    cbc_input = {
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    # Should not crash
    assert normalized["age_years"] == 35
    assert normalized["sex"] == "M"
    assert len(log) == 0


# Test 7: ANC Conversion


def test_normalize_anc_per_1000_conversion():
    """Test ANC /1000 conversion when ANC >50."""
    cbc_input = {
        "anc": 7500,  # >50 → /1000 → 7.5
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["anc"] == 7.5
    assert len(log) > 0


# Test 8: Compute Absolute Counts


def test_compute_absolute_counts_anc():
    """Test computation of ANC from WBC + neutrophil %."""
    cbc_input = {
        "wbc": 10.0,
        "neutrophils_pct": 70,
        "age_years": 35,
        "sex": "M"
    }

    computed = compute_absolute_counts(cbc_input)

    # ANC = WBC × neutrophils_pct / 100
    expected_anc = 10.0 * 70 / 100
    assert computed["anc"] == expected_anc, \
        f"Expected ANC {expected_anc}, got {computed.get('anc')}"


def test_compute_absolute_counts_alc():
    """Test computation of ALC from WBC + lymphocyte %."""
    cbc_input = {
        "wbc": 8.0,
        "lymphocytes_pct": 30,
        "age_years": 35,
        "sex": "M"
    }

    computed = compute_absolute_counts(cbc_input)

    # ALC = WBC × lymphocytes_pct / 100
    expected_alc = 8.0 * 30 / 100
    assert computed["lymphocytes_abs"] == expected_alc


def test_compute_absolute_counts_all():
    """Test computation of all absolute counts."""
    cbc_input = {
        "wbc": 10.0,
        "neutrophils_pct": 60,
        "lymphocytes_pct": 30,
        "monocytes_pct": 8,
        "eosinophils_pct": 1.5,
        "basophils_pct": 0.5,
    }

    computed = compute_absolute_counts(cbc_input)

    assert computed["anc"] == 6.0
    assert computed["lymphocytes_abs"] == 3.0
    assert computed["monocytes_abs"] == 0.8
    assert computed["eosinophils_abs"] == 0.15
    assert computed["basophils_abs"] == 0.05


def test_compute_absolute_counts_missing_wbc():
    """Test that absolute counts are not computed if WBC is missing."""
    cbc_input = {
        # No wbc
        "neutrophils_pct": 70,
        "age_years": 35,
        "sex": "M"
    }

    computed = compute_absolute_counts(cbc_input)

    # Should NOT compute anc without wbc
    assert "anc" not in computed


def test_compute_absolute_counts_skips_if_already_present():
    """Test that absolute counts are not recomputed if already present."""
    cbc_input = {
        "wbc": 10.0,
        "neutrophils_pct": 70,
        "anc": 5.0,  # Already present, should not recompute
    }

    computed = compute_absolute_counts(cbc_input)

    # Should keep original value
    assert computed["anc"] == 5.0  # NOT 7.0


# Test 9: Edge Cases


def test_normalize_zero_values():
    """Test normalization with zero values."""
    cbc_input = {
        "wbc": 0,
        "plt": 0,
        "hb": 0,
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    # Zero values should not be converted
    assert normalized["wbc"] == 0
    assert normalized["plt"] == 0
    assert normalized["hb"] == 0
    assert len(log) == 0


def test_normalize_negative_values():
    """Test normalization with negative values (invalid but should not crash)."""
    cbc_input = {
        "wbc": -10,
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    # Should not crash, just pass through
    assert normalized["wbc"] == -10


def test_normalize_non_numeric_values():
    """Test normalization with non-numeric values (should skip)."""
    cbc_input = {
        "wbc": "invalid",
        "plt": "250",  # String but convertible
        "age_years": 35,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    # Should skip non-numeric
    assert normalized["wbc"] == "invalid"
    # Note: Implementation may try to convert "250" string


# Test 10: Integration with Real Cases


def test_normalize_real_case_ida():
    """Test normalization with real IDA case."""
    cbc_input = {
        "hb": 95,       # /10 → 9.5 (anemia)
        "mcv": 68,      # No conversion (already correct)
        "plt": 450000,  # /1000 → 450 (thrombocytosis)
        "age_years": 35,
        "sex": "F"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["hb"] == 9.5
    assert normalized["mcv"] == 68
    assert normalized["plt"] == 450
    assert len(log) == 2, "Expected 2 conversions (hb + plt)"


def test_normalize_real_case_polycythemia():
    """Test normalization with real polycythemia case."""
    cbc_input = {
        "hb": 185,      # /10 → 18.5 (high)
        "hct": 56,      # No conversion
        "wbc": 12500,   # /1000 → 12.5
        "plt": 520000,  # /1000 → 520
        "age_years": 55,
        "sex": "M"
    }

    normalized, log = normalize_cbc(cbc_input)

    assert normalized["hb"] == 18.5
    assert normalized["hct"] == 56
    assert normalized["wbc"] == 12.5
    assert normalized["plt"] == 520
    assert len(log) == 3, "Expected 3 conversions (hb + wbc + plt)"


# Test 11: Integration normalize + compute_absolute


def test_integration_normalize_then_compute():
    """Test integration: normalize units then compute absolute counts."""
    cbc_input = {
        "wbc": 8500,  # /1000 → 8.5
        "neutrophils_pct": 70,
        "age_years": 35,
        "sex": "M"
    }

    # Step 1: Normalize
    normalized, log = normalize_cbc(cbc_input)
    assert normalized["wbc"] == 8.5

    # Step 2: Compute absolute counts
    computed = compute_absolute_counts(normalized)
    expected_anc = 8.5 * 70 / 100
    assert computed["anc"] == expected_anc


# Test 12: validate_physiological_ranges()


def test_validate_physiological_ranges_all_normal():
    """Test validation with all values in normal range."""
    from hemodoctor.engines.normalization import validate_physiological_ranges

    cbc = {
        "wbc": 7.5,
        "plt": 250,
        "hb": 14.5,
        "anc": 4.0,
        "rbc": 4.8,
        "ht": 42,
        "mcv": 88
    }

    warnings = validate_physiological_ranges(cbc)

    assert len(warnings) == 0


def test_validate_physiological_ranges_wbc_out_of_range():
    """Test validation warns for WBC out of range."""
    from hemodoctor.engines.normalization import validate_physiological_ranges

    cbc = {
        "wbc": 250,  # > 200 (max)
        "age_years": 35,
        "sex": "M"
    }

    warnings = validate_physiological_ranges(cbc)

    assert len(warnings) > 0
    assert any("WBC" in w for w in warnings)
    assert any("fora da faixa" in w for w in warnings)


def test_validate_physiological_ranges_hb_too_low():
    """Test validation warns for Hb too low."""
    from hemodoctor.engines.normalization import validate_physiological_ranges

    cbc = {
        "hb": 1.0,  # < 2 (min)
    }

    warnings = validate_physiological_ranges(cbc)

    assert len(warnings) > 0
    assert any("HB" in w for w in warnings)


def test_validate_physiological_ranges_plt_too_high():
    """Test validation warns for PLT too high."""
    from hemodoctor.engines.normalization import validate_physiological_ranges

    cbc = {
        "plt": 2500,  # > 2000 (max)
    }

    warnings = validate_physiological_ranges(cbc)

    assert len(warnings) > 0
    assert any("PLT" in w for w in warnings)


def test_validate_physiological_ranges_non_numeric_value():
    """Test validation warns for non-numeric values."""
    from hemodoctor.engines.normalization import validate_physiological_ranges

    cbc = {
        "wbc": "invalid",  # Non-numeric
    }

    warnings = validate_physiological_ranges(cbc)

    assert len(warnings) > 0
    assert any("WBC" in w and "não numérico" in w for w in warnings)


def test_validate_physiological_ranges_missing_values():
    """Test validation skips missing values (None)."""
    from hemodoctor.engines.normalization import validate_physiological_ranges

    cbc = {
        "wbc": None,
        "plt": None
    }

    warnings = validate_physiological_ranges(cbc)

    # Should not warn about missing values
    assert len(warnings) == 0


def test_validate_physiological_ranges_multiple_out_of_range():
    """Test validation warns for multiple values out of range."""
    from hemodoctor.engines.normalization import validate_physiological_ranges

    cbc = {
        "wbc": 250,   # Out of range
        "plt": 3000,  # Out of range
        "hb": 30      # Out of range
    }

    warnings = validate_physiological_ranges(cbc)

    # Should have 3 warnings
    assert len(warnings) == 3


# Test 13: apply_age_sex_cutoffs()


def test_apply_age_sex_cutoffs_adult_male():
    """Test age/sex cutoffs for adult male."""
    from hemodoctor.engines.normalization import apply_age_sex_cutoffs

    cbc = {
        "hb": 14.5,
        "age_years": 35,
        "sex": "M"
    }

    result = apply_age_sex_cutoffs(cbc, yaml_parser=None)

    # Should add cutoffs metadata
    assert "_cutoffs" in result
    assert "hb_lower" in result["_cutoffs"]
    # Adult male: hb_lower = 13.0
    assert result["_cutoffs"]["hb_lower"] == 13.0


def test_apply_age_sex_cutoffs_adult_female():
    """Test age/sex cutoffs for adult female."""
    from hemodoctor.engines.normalization import apply_age_sex_cutoffs

    cbc = {
        "hb": 12.5,
        "age_years": 35,
        "sex": "F"
    }

    result = apply_age_sex_cutoffs(cbc, yaml_parser=None)

    # Adult female: hb_lower = 12.0
    assert result["_cutoffs"]["hb_lower"] == 12.0


def test_apply_age_sex_cutoffs_pediatric_male():
    """Test age/sex cutoffs for pediatric male."""
    from hemodoctor.engines.normalization import apply_age_sex_cutoffs

    cbc = {
        "hb": 12.0,
        "age_years": 10,
        "sex": "M"
    }

    result = apply_age_sex_cutoffs(cbc, yaml_parser=None)

    # Pediatric male: hb_lower = 11.5
    assert result["_cutoffs"]["hb_lower"] == 11.5


def test_apply_age_sex_cutoffs_pediatric_female():
    """Test age/sex cutoffs for pediatric female."""
    from hemodoctor.engines.normalization import apply_age_sex_cutoffs

    cbc = {
        "hb": 11.5,
        "age_years": 10,
        "sex": "F"
    }

    result = apply_age_sex_cutoffs(cbc, yaml_parser=None)

    # Pediatric female: hb_lower = 11.0
    assert result["_cutoffs"]["hb_lower"] == 11.0


def test_apply_age_sex_cutoffs_missing_age():
    """Test cutoffs when age is missing."""
    from hemodoctor.engines.normalization import apply_age_sex_cutoffs

    cbc = {
        "hb": 14.5,
        # age_years missing
        "sex": "M"
    }

    result = apply_age_sex_cutoffs(cbc, yaml_parser=None)

    # Should return unchanged (no cutoffs applied)
    assert "_cutoffs" not in result


def test_apply_age_sex_cutoffs_missing_sex():
    """Test cutoffs when sex is missing."""
    from hemodoctor.engines.normalization import apply_age_sex_cutoffs

    cbc = {
        "hb": 14.5,
        "age_years": 35
        # sex missing
    }

    result = apply_age_sex_cutoffs(cbc, yaml_parser=None)

    # Should return unchanged (no cutoffs applied)
    assert "_cutoffs" not in result


def test_apply_age_sex_cutoffs_doesnt_modify_original():
    """Test that apply_age_sex_cutoffs doesn't modify original dict."""
    from hemodoctor.engines.normalization import apply_age_sex_cutoffs

    cbc = {
        "hb": 14.5,
        "age_years": 35,
        "sex": "M"
    }

    result = apply_age_sex_cutoffs(cbc, yaml_parser=None)

    # Original should not have _cutoffs
    assert "_cutoffs" not in cbc
    # Result should have _cutoffs
    assert "_cutoffs" in result
