"""
Evidence Engine Unit Tests

79 tests total (one per evidence).

Test pattern:
- Test positive case (evidence present)
- Test negative case (evidence absent)
- Test missing data (evidence unknown)

Markers: @pytest.mark.evidence

Author: Dr. Abel Costa
IEC 62304 Class C
"""

import pytest
from hemodoctor.engines.evidence import evaluate_evidence, evaluate_all_evidences
from hemodoctor.utils.yaml_parser import YAMLParser


# Fixtures

@pytest.fixture
def yaml_parser():
    """Get YAMLParser singleton instance."""
    return YAMLParser.get_instance()


@pytest.fixture
def basic_config():
    """Basic configuration for tests."""
    return {
        "cutoffs": {
            "anc_critical": 0.5,
            "anc_very_critical": 0.2,
            "wbc_very_high": 100,
            "plt_critical_low": 10,
            "hb_critical_low": {"adult_m": 6.5, "adult_f": 6.0},
            "mcv_low_adult": 80,
            "mcv_high_adult": 100,
            "rdw_high": 14,
            "ldh_high": 500,
        }
    }


# Critical Evidences Tests (6 tests)

@pytest.mark.evidence
def test_E_ANC_VCRIT_present(basic_config):
    """Test E-ANC-VCRIT: anc < 0.2 (very critical)"""
    evidence = {
        "id": "E-ANC-VCRIT",
        "rule": "anc < 0.2",
        "requires": ["anc"],
        "strength": "strong",
    }
    cbc = {"anc": 0.1}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


@pytest.mark.evidence
def test_E_ANC_VCRIT_absent(basic_config):
    """Test E-ANC-VCRIT absent"""
    evidence = {
        "id": "E-ANC-VCRIT",
        "rule": "anc < 0.2",
        "requires": ["anc"],
    }
    cbc = {"anc": 1.5}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "absent"


@pytest.mark.evidence
def test_E_ANC_VCRIT_unknown(basic_config):
    """Test E-ANC-VCRIT with missing data"""
    evidence = {
        "id": "E-ANC-VCRIT",
        "rule": "anc < 0.2",
        "requires": ["anc"],
    }
    cbc = {}  # Missing anc

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "unknown"


@pytest.mark.evidence
def test_E_ANC_CRIT_present(basic_config):
    """Test E-ANC-CRIT: anc < 0.5"""
    evidence = {
        "id": "E-ANC-CRIT",
        "rule": "anc < 0.5",
        "requires": ["anc"],
    }
    cbc = {"anc": 0.3}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


@pytest.mark.evidence
def test_E_WBC_VERY_HIGH_present(basic_config):
    """Test E-WBC-VERY-HIGH: wbc > 100"""
    evidence = {
        "id": "E-WBC-VERY-HIGH",
        "rule": "wbc > 100",
        "requires": ["wbc"],
    }
    cbc = {"wbc": 150}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


@pytest.mark.evidence
def test_E_PLT_CRIT_LOW_present(basic_config):
    """Test E-PLT-CRIT-LOW: plt < 10"""
    evidence = {
        "id": "E-PLT-CRIT-LOW",
        "rule": "plt < 10",
        "requires": ["plt"],
    }
    cbc = {"plt": 8}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


@pytest.mark.evidence
def test_E_SCHISTOCYTES_GE1PCT_present(basic_config):
    """Test E-SCHISTOCYTES-GE1PCT: esquistocitos == true"""
    evidence = {
        "id": "E-SCHISTOCYTES-GE1PCT",
        "rule": "esquistocitos == true",
        "requires": ["esquistocitos"],
    }
    cbc = {"morphology": {"esquistocitos": True}}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


# Red Blood Cell Evidences (sample tests)

@pytest.mark.evidence
def test_E_MICROCYTOSIS_present(basic_config):
    """Test E-MICROCYTOSIS: mcv < 80"""
    evidence = {
        "id": "E-MICROCYTOSIS",
        "rule": "mcv < 80",
        "requires": ["mcv"],
    }
    cbc = {"mcv": 72}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


@pytest.mark.evidence
def test_E_MACROCYTOSIS_present(basic_config):
    """Test E-MACROCYTOSIS: mcv > 100"""
    evidence = {
        "id": "E-MACROCYTOSIS",
        "rule": "mcv > 100",
        "requires": ["mcv"],
    }
    cbc = {"mcv": 110}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


@pytest.mark.evidence
def test_E_RDW_HIGH_present(basic_config):
    """Test E-RDW-HIGH: rdw > 14"""
    evidence = {
        "id": "E-RDW-HIGH",
        "rule": "rdw > 14",
        "requires": ["rdw"],
    }
    cbc = {"rdw": 16}

    result = evaluate_evidence(evidence, cbc, basic_config)

    assert result == "present"


# Integration test: Evaluate all evidences

@pytest.mark.evidence
def test_evaluate_all_evidences_tma_case(yaml_parser):
    """Integration test: TMA critical case with multiple evidences"""
    cbc = {
        "plt": 8,
        "ldh": 980,
        "haptoglobin": 10,
        "bt_indireta": 2.5,
        "morphology": {"esquistocitos": True},
        "age_years": 35,
        "sex": "M",
    }

    evidences = evaluate_all_evidences(cbc, yaml_parser)

    assert len(evidences) == 79  # All evidences evaluated

    present_evidences = [e for e in evidences if e.status == "present"]
    present_ids = {e.id for e in present_evidences}

    # Check expected evidences are present
    assert "E-PLT-CRIT-LOW" in present_ids
    assert "E-SCHISTOCYTES-GE1PCT" in present_ids
    assert "E-LDH-HIGH" in present_ids


@pytest.mark.evidence
def test_evaluate_all_evidences_missing_data(yaml_parser):
    """Test with minimal data (many evidences should be unknown)"""
    cbc = {
        "hb": 12.5,
        "age_years": 25,
        "sex": "F",
    }

    evidences = evaluate_all_evidences(cbc, yaml_parser)

    assert len(evidences) == 79

    unknown_evidences = [e for e in evidences if e.status == "unknown"]

    # Most evidences should be unknown (missing data)
    assert len(unknown_evidences) > 50


# TODO: Add remaining 70 evidence tests (one per evidence)
# Pattern: test_{evidence_id}_present, _absent, _unknown
# Use yaml_parser fixture to load actual evidence definitions

# Example template for remaining tests:
# @pytest.mark.evidence
# def test_E_{EVIDENCE_ID}_present(basic_config):
#     evidence = yaml_parser.get_all_evidence_defs()
#     evidence_def = [e for e in evidence if e["id"] == "E-{EVIDENCE_ID}"][0]
#     cbc = {...}  # Test data for positive case
#     result = evaluate_evidence(evidence_def, cbc, basic_config)
#     assert result == "present"
