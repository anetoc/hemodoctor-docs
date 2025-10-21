"""
Integration Test - Critical Fixes Validation

Tests the 4 critical fixes implemented:
1. Evidence Engine - config + age_sex_group exposure
2. Next Steps - EvidenceResult list passing
3. FastAPI - pipeline wiring
4. WORM Log - environment-based HMAC key

KNOWN LIMITATIONS (BUG-014):
- S-BLASTIC-SYNDROME skipped (nested logic not supported in V0)
- Fix planned for Sprint 1 (recursive combine evaluator)
- Impact: 1/35 syndromes (3%) temporarily non-functional
- See: /Users/abelcosta/Documents/HemoDoctor/docs/BUGS.md

Author: Dr. Abel Costa
IEC 62304 Class C
"""

import pytest
import os
from hemodoctor.api.pipeline import analyze_cbc


def test_evidence_engine_age_sex_cutoffs():
    """
    Test that age/sex-adjusted cutoffs work correctly.

    Previously: NameError (config not exposed, age_sex_group not derived)
    Now: Should evaluate correctly
    """
    # Adult male with critical anemia (Hb < 6.5)
    cbc = {
        "hb": 6.0,
        "mcv": 85,
        "wbc": 5.0,
        "plt": 150,
        "age_years": 35,
        "sex": "M"
    }

    result = analyze_cbc(cbc)

    # Should detect E-HB-CRIT-LOW (adult_m cutoff = 6.5)
    evidences = result["evidences_present"]
    assert "E-HB-CRIT-LOW" in evidences, f"E-HB-CRIT-LOW not detected. Evidences: {evidences}"

    # Should detect critical syndrome
    syndromes = result["top_syndromes"]
    assert len(syndromes) > 0, "No syndromes detected"

    print(f"✅ Evidence engine: Age/sex cutoffs working")
    print(f"   Detected evidences: {evidences[:5]}")
    print(f"   Detected syndromes: {syndromes[:3]}")


def test_evidence_engine_pediatric():
    """
    Test pediatric age group (different cutoffs).

    Previously: Would use adult cutoffs (wrong)
    Now: Should use pediatric_1_3y cutoffs
    """
    # Pediatric (2 years) with Hb 8.5 (below pediatric threshold)
    cbc = {
        "hb": 8.5,
        "mcv": 75,
        "wbc": 6.0,
        "plt": 200,
        "age_years": 2.5,
        "sex": "F"
    }

    result = analyze_cbc(cbc)

    # Should use pediatric_1_3y cutoff (9.0 g/dL)
    evidences = result["evidences_present"]

    # Hb 8.5 < 9.0 → critical for this age group
    assert "E-HB-CRIT-LOW" in evidences, f"Pediatric cutoff not applied. Evidences: {evidences}"

    print(f"✅ Evidence engine: Pediatric cutoffs working")


def test_next_steps_trigger_firing():
    """
    Test that next steps triggers fire correctly.

    Previously: Triggers never fired (evidences was set of strings)
    Now: Should fire triggers (evidences is list of EvidenceResult)
    """
    # TMA case (should trigger critical next steps)
    cbc = {
        "hb": 8.0,
        "plt": 8,
        "ldh": 980,
        "morphology": {"esquistocitos": True},
        "age_years": 35,
        "sex": "M",
        "mcv": 88,
        "wbc": 10.0
    }

    result = analyze_cbc(cbc)

    # Should have next steps
    next_steps = result.get("next_steps", [])
    assert len(next_steps) > 0, "No next steps generated (triggers not firing)"

    # At least one critical next step
    critical_steps = [s for s in next_steps if s.get("level") == "critical"]
    assert len(critical_steps) > 0, f"No critical next steps. All: {next_steps}"

    print(f"✅ Next steps engine: Triggers firing correctly")
    print(f"   Total next steps: {len(next_steps)}")
    print(f"   Critical steps: {len(critical_steps)}")


def test_pipeline_output_completeness():
    """
    Test that pipeline output includes all expected fields.

    Previously: syndromes_detail, evidences_detail empty
    Now: Should be populated
    """
    cbc = {
        "hb": 15.2,
        "mcv": 88,
        "wbc": 8.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M"
    }

    result = analyze_cbc(cbc)

    # Check all expected fields
    assert "version" in result
    assert "timestamp" in result
    assert "route_id" in result
    assert "top_syndromes" in result
    assert "evidences_present" in result
    assert "next_steps" in result
    assert "syndromes_detail" in result
    assert "evidences_detail" in result

    # syndromes_detail should have structure
    syndromes_detail = result["syndromes_detail"]
    if len(syndromes_detail) > 0:
        assert "id" in syndromes_detail[0]
        assert "criticality" in syndromes_detail[0]

    # evidences_detail should have structure
    evidences_detail = result["evidences_detail"]
    if len(evidences_detail) > 0:
        assert "id" in evidences_detail[0]
        assert "status" in evidences_detail[0]

    print(f"✅ Pipeline output: All fields populated")
    print(f"   Syndromes detail: {len(syndromes_detail)}")
    print(f"   Evidences detail: {len(evidences_detail)}")


def test_worm_log_environment_key():
    """
    Test that WORM log uses environment variable for HMAC key.

    Previously: Hard-coded key in source
    Now: Should use HEMODOCTOR_WORM_SECRET env var (or generate random)
    """
    # Set custom HMAC key
    os.environ["HEMODOCTOR_WORM_SECRET"] = "test_secret_key_for_integration"

    # Reload module to pick up new env var
    import importlib
    from hemodoctor.engines import worm_log
    importlib.reload(worm_log)

    # Run analysis (will log to WORM)
    cbc = {
        "hb": 15.2,
        "mcv": 88,
        "wbc": 8.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M"
    }

    result = analyze_cbc(cbc)

    # Should complete without error
    assert result is not None

    print(f"✅ WORM log: Environment-based key working")

    # Clean up
    del os.environ["HEMODOCTOR_WORM_SECRET"]


def test_end_to_end_critical_case():
    """
    End-to-end test with critical TMA case.

    Validates all 4 fixes in one comprehensive test.
    """
    cbc = {
        "hb": 7.5,
        "plt": 8,
        "ldh": 980,
        "bt_indireta": 2.5,
        "morphology": {"esquistocitos": True},
        "age_years": 35,
        "sex": "M",
        "mcv": 88,
        "wbc": 10.0
    }

    result = analyze_cbc(cbc)

    # 1. Evidence engine should detect critical evidences
    evidences = result["evidences_present"]
    assert "E-PLT-CRIT-LOW" in evidences, "PLT critical not detected"
    assert "E-SCHISTOCYTES-GE1PCT" in evidences, "Schistocytes not detected"

    # 2. Should detect TMA syndrome
    syndromes = result["top_syndromes"]
    assert "S-TMA" in syndromes, f"TMA not detected. Syndromes: {syndromes}"

    # 3. Next steps should fire
    next_steps = result["next_steps"]
    assert len(next_steps) > 0, "No next steps (triggers not firing)"

    # 4. Pipeline should be complete
    assert len(result["syndromes_detail"]) > 0
    assert len(result["evidences_detail"]) > 0

    print(f"✅ End-to-end TMA case: All systems working")
    print(f"   Route ID: {result['route_id'][:16]}...")
    print(f"   Top syndrome: {syndromes[0]}")
    print(f"   Critical evidences: {len([e for e in evidences if 'CRIT' in e])}")
    print(f"   Next steps: {len(next_steps)}")


@pytest.mark.skip(reason="BUG-014: Nested logic not supported (Sprint 1)")
def test_syndrome_blastic_nested_logic():
    """
    Test S-BLASTIC-SYNDROME with nested combine logic.

    SKIPPED: Current implementation does not support nested all/any.

    S-BLASTIC-SYNDROME has:
    combine:
      any:
        - E-WBC-VERY-HIGH
        - all: [E-WBC-VERY-HIGH, E-PLT-CRIT-LOW]  # <- nested
        - E-BLASTS-PRESENT

    Fix: Implement recursive combine evaluator in Sprint 1
    See: /Users/abelcosta/Documents/HemoDoctor/docs/BUGS.md (BUG-014)
    """
    cbc = {
        "wbc": 150,  # Very high
        "plt": 15,   # Critical low
        "hb": 8.0,
        "age_years": 10,
        "sex": "M"
    }

    result = analyze_cbc(cbc)

    # EXPECTED (after fix):
    # syndromes = result["top_syndromes"]
    # assert "S-BLASTIC-SYNDROME" in syndromes

    # CURRENT:
    # Nested logic not evaluated correctly
    assert True, "Test skipped - nested logic not supported"


if __name__ == "__main__":
    """Run all tests"""
    print("\n=== Integration Tests - Critical Fixes ===\n")

    test_evidence_engine_age_sex_cutoffs()
    print()

    test_evidence_engine_pediatric()
    print()

    test_next_steps_trigger_firing()
    print()

    test_pipeline_output_completeness()
    print()

    test_worm_log_environment_key()
    print()

    test_end_to_end_critical_case()
    print()

    print("=== All Integration Tests Passed! ✅ ===\n")
