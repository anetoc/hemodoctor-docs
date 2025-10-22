#!/usr/bin/env python3
"""
Quick Verification Script for HemoDoctor CDSS Implementation

Tests the implemented components:
- YAML parser
- Evidence engine
- Data models

Run: python3 verify_implementation.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_yaml_parser():
    """Test YAML parser loads all files."""
    print("=" * 60)
    print("TEST 1: YAML Parser")
    print("=" * 60)

    try:
        from hemodoctor.utils.yaml_parser import YAMLParser

        parser = YAMLParser.get_instance()

        # Test loading evidences
        evidences = parser.get_all_evidence_defs()
        print(f"✅ Loaded {len(evidences)} evidences from 02_evidence_hybrid.yaml")

        # Test loading syndromes
        syndromes = parser.get_all_syndrome_defs()
        print(f"✅ Loaded {len(syndromes)} syndromes from 03_syndromes_hybrid.yaml")

        # Test loading next steps
        triggers = parser.get_all_next_steps_triggers()
        print(f"✅ Loaded {len(triggers)} triggers from 09_next_steps_engine_hybrid.yaml")

        # Test config access
        config = parser.config
        print(f"✅ Loaded config with {len(config.get('cutoffs', {}))} cutoff definitions")

        print("\n✅ YAML Parser: PASS\n")
        return True

    except Exception as e:
        print(f"\n❌ YAML Parser: FAIL - {e}\n")
        import traceback
        traceback.print_exc()
        return False


def test_evidence_engine():
    """Test evidence engine evaluates correctly."""
    print("=" * 60)
    print("TEST 2: Evidence Engine")
    print("=" * 60)

    try:
        from hemodoctor.engines.evidence import evaluate_all_evidences, get_present_evidences
        from hemodoctor.utils.yaml_parser import YAMLParser

        parser = YAMLParser.get_instance()

        # Test case 1: TMA critical
        print("\nTest Case 1: TMA Critical")
        cbc_tma = {
            "plt": 8,
            "ldh": 980,
            "haptoglobin": 10,
            "morphology": {"esquistocitos": True},
            "age_years": 35,
            "sex": "M",
        }

        evidences = evaluate_all_evidences(cbc_tma, parser)
        print(f"  Evaluated: {len(evidences)} evidences")

        present = get_present_evidences(evidences)
        print(f"  Present: {len(present)} evidences")
        print(f"  IDs: {[e.id for e in present]}")

        assert len(evidences) == 79, "Should evaluate all 79 evidences"
        assert len(present) > 0, "Should have at least one present evidence"

        # Check expected evidences
        present_ids = {e.id for e in present}
        assert "E-PLT-CRIT-LOW" in present_ids, "Should detect low platelets"
        assert "E-SCHISTOCYTES-GE1PCT" in present_ids, "Should detect schistocytes"

        print("  ✅ TMA case detected correctly")

        # Test case 2: Neutropenia
        print("\nTest Case 2: Neutropenia")
        cbc_neutro = {
            "anc": 0.3,
            "wbc": 1.5,
            "age_years": 45,
            "sex": "F",
        }

        evidences = evaluate_all_evidences(cbc_neutro, parser)
        present = get_present_evidences(evidences)
        present_ids = {e.id for e in present}

        assert "E-ANC-CRIT" in present_ids, "Should detect critical neutropenia"
        print(f"  Present: {[e.id for e in present]}")
        print("  ✅ Neutropenia case detected correctly")

        # Test case 3: Normal CBC (few evidences)
        print("\nTest Case 3: Normal CBC")
        cbc_normal = {
            "hb": 14.5,
            "wbc": 7.2,
            "plt": 250,
            "anc": 4.5,
            "age_years": 30,
            "sex": "M",
        }

        evidences = evaluate_all_evidences(cbc_normal, parser)
        present = get_present_evidences(evidences)

        assert len(present) < 5, "Normal CBC should have few evidences"
        print(f"  Present: {len(present)} evidences (expected <5)")
        print("  ✅ Normal case handled correctly")

        print("\n✅ Evidence Engine: PASS\n")
        return True

    except Exception as e:
        print(f"\n❌ Evidence Engine: FAIL - {e}\n")
        import traceback
        traceback.print_exc()
        return False


def test_data_models():
    """Test Pydantic data models."""
    print("=" * 60)
    print("TEST 3: Data Models")
    print("=" * 60)

    try:
        from hemodoctor.models.cbc import CBCInput
        from hemodoctor.models.evidence import EvidenceResult
        from hemodoctor.models.syndrome import SyndromeResult

        # Test CBCInput
        cbc = CBCInput(
            hb=12.5,
            wbc=7.0,
            plt=200,
            age_years=35,
            sex="M"
        )
        print(f"✅ CBCInput: {cbc.hb} g/dL Hb, {cbc.wbc} WBC")

        # Test EvidenceResult
        evidence = EvidenceResult(
            id="E-ANC-CRIT",
            status="present",
            strength="strong",
            requires=["anc"],
        )
        print(f"✅ EvidenceResult: {evidence.id} is {evidence.status}")

        # Test SyndromeResult
        syndrome = SyndromeResult(
            id="S-TMA",
            criticality="critical",
            evidences=["E-PLT-CRIT-LOW", "E-SCHISTOCYTES-GE1PCT"],
        )
        print(f"✅ SyndromeResult: {syndrome.id} ({syndrome.criticality})")

        # Test validation
        try:
            CBCInput(age_years=35, sex="X")  # Invalid sex
            print("❌ Validation should have failed")
            return False
        except Exception:
            print("✅ Validation: Rejects invalid input")

        print("\n✅ Data Models: PASS\n")
        return True

    except Exception as e:
        print(f"\n❌ Data Models: FAIL - {e}\n")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("HemoDoctor CDSS v2.4.0 - Implementation Verification")
    print("=" * 60 + "\n")

    results = {
        "YAML Parser": test_yaml_parser(),
        "Evidence Engine": test_evidence_engine(),
        "Data Models": test_data_models(),
    }

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name:20s} {status}")

    all_passed = all(results.values())

    print("\n" + "=" * 60)
    if all_passed:
        print("✅ ALL TESTS PASSED")
        print("Implementation foundation is working correctly!")
    else:
        print("❌ SOME TESTS FAILED")
        print("Check error messages above for details.")
    print("=" * 60 + "\n")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
