"""
Edge Cases Integration Tests
Tests extreme values, all missing data, conflicting evidences
5 comprehensive edge case tests
"""

import pytest
from hemodoctor.api.pipeline import analyze_cbc


# ============================================================================
# EDGE CASES (5 tests)
# ============================================================================

def test_edge_all_missing_data():
    """Test CBC with all optional fields missing (only required fields)"""
    cbc = {
        "hb": 12.0,
        "wbc": 7.0,
        "plt": 200,
        "mcv": 88,
        "age_years": 30,
        "sex": "F"
        # No differential, no iron panel, no morphology, no LDH, etc.
    }

    result = analyze_cbc(cbc)

    # Should complete successfully (fail-safe design)
    assert result is not None
    assert "top_syndromes" in result
    assert "evidences_present" in result

    # May detect S-NORMAL or S-INCONCLUSIVO
    assert len(result["top_syndromes"]) > 0


def test_edge_extreme_values_high():
    """Test CBC with extremely high values (but physiologically possible)"""
    cbc = {
        "hb": 22.0,  # Very high (polycythemia)
        "wbc": 500,  # Extremely high (leukemia)
        "plt": 2000,  # Extremely high (thrombocytosis)
        "mcv": 120,  # Very high (macrocytic)
        "age_years": 50,
        "sex": "M"
    }

    result = analyze_cbc(cbc)

    # Should handle extreme values gracefully
    assert result is not None
    assert len(result["top_syndromes"]) > 0


def test_edge_extreme_values_low():
    """Test CBC with extremely low values"""
    cbc = {
        "hb": 3.0,  # Critically low (life-threatening)
        "wbc": 0.1,  # Critically low (severe neutropenia)
        "plt": 2,  # Critically low (severe thrombocytopenia)
        "mcv": 50,  # Very low (severe microcytosis)
        "age_years": 30,
        "sex": "F"
    }

    result = analyze_cbc(cbc)

    # Should handle extreme values
    assert result is not None
    assert len(result["top_syndromes"]) > 0


def test_edge_conflicting_evidences():
    """Test CBC with seemingly conflicting evidences"""
    cbc = {
        "hb": 18.0,  # High (polycythemia)
        "wbc": 2.0,  # Low (leukopenia)
        "plt": 600,  # High (thrombocytosis)
        "mcv": 70,  # Low (microcytic)
        "ferritin": 500,  # High (not IDA)
        "age_years": 60,
        "sex": "M"
    }

    result = analyze_cbc(cbc)

    # Should resolve conflicts and produce output
    assert result is not None
    assert len(result["top_syndromes"]) > 0


def test_edge_boundary_values():
    """Test CBC with values exactly at cutoff boundaries"""
    cbc = {
        "hb": 13.0,  # Exactly at lower limit for adult male
        "wbc": 4.0,  # Exactly at lower limit
        "plt": 150,  # Exactly at lower limit
        "mcv": 80,  # Exactly at lower limit
        "age_years": 35,
        "sex": "M"
    }

    result = analyze_cbc(cbc)

    # Should handle boundary values consistently
    assert result is not None
    assert len(result["top_syndromes"]) > 0
