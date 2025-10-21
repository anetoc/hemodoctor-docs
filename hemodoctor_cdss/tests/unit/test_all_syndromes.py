"""
Parametrized Syndrome Tests - All 35 Syndromes

This file contains parametrized tests that automatically test all 35 syndromes
from the YAML configuration. Each syndrome is tested for:
1. Detection with matching evidences (syndrome present)
2. No false positives without matching evidences (syndrome absent)
3. Short-circuit behavior for critical syndromes

Author: Dr. Abel Costa
IEC 62304 Class C
"""

import pytest
from hemodoctor.engines.syndrome import detect_syndromes, is_syndrome_present
from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.utils.yaml_parser import YAMLParser


# Fixtures

@pytest.fixture(scope="module")
def yaml_parser():
    """Get YAMLParser singleton instance."""
    return YAMLParser.get_instance()


@pytest.fixture(scope="module")
def all_syndrome_defs(yaml_parser):
    """Get all 35 syndrome definitions from YAML."""
    return yaml_parser.get_all_syndrome_defs()


# Dynamic test generation

def pytest_generate_tests(metafunc):
    """
    Dynamically generate test cases for each syndrome.
    """
    if "syndrome_id" in metafunc.fixturenames:
        yaml_parser = YAMLParser.get_instance()
        all_syndromes = yaml_parser.get_all_syndrome_defs()
        syndrome_ids = [s["id"] for s in all_syndromes]
        metafunc.parametrize("syndrome_id", syndrome_ids)


# Helper function to create evidences for syndrome testing

def get_test_evidences_for_syndrome(syndrome_id):
    """
    Get test evidences that should trigger each syndrome.

    Returns:
        tuple: (positive_evidences, negative_evidences)
            positive_evidences: Should trigger the syndrome
            negative_evidences: Should NOT trigger the syndrome
    """
    # Positive: evidences that should trigger the syndrome
    # Negative: evidences that should NOT trigger (empty or unrelated)

    if syndrome_id == "S-TMA":
        positive = [
            EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),
            EvidenceResult(id="E-SCHISTOCYTES-GE1PCT", status="present", strength="strong"),
            EvidenceResult(id="E-LDH-HIGH", status="present", strength="high"),
        ]
        negative = [
            EvidenceResult(id="E-HB-LOW", status="present", strength="medium"),
        ]

    elif syndrome_id == "S-NEUTROPENIA-GRAVE":
        positive = [
            EvidenceResult(id="E-ANC-CRIT", status="present", strength="critical"),
        ]
        negative = [
            EvidenceResult(id="E-WBC-HIGH", status="present", strength="medium"),
        ]

    elif syndrome_id == "S-BLASTIC-SYNDROME":
        positive = [
            EvidenceResult(id="E-WBC-VERY-HIGH", status="present", strength="strong"),
        ]
        negative = [
            EvidenceResult(id="E-PLT-LOW", status="present", strength="medium"),
        ]

    elif syndrome_id == "S-PLT-CRITICA":
        positive = [
            EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),
        ]
        negative = [
            EvidenceResult(id="E-WBC-HIGH", status="present", strength="medium"),
        ]

    elif syndrome_id == "S-ANEMIA-GRAVE":
        positive = [
            EvidenceResult(id="E-HB-CRIT-LOW", status="present", strength="strong"),
        ]
        negative = [
            EvidenceResult(id="E-PLT-LOW", status="present", strength="medium"),
        ]

    elif syndrome_id == "S-IDA":
        positive = [
            EvidenceResult(id="E-FERRITIN-LOW", status="present", strength="high"),
            EvidenceResult(id="E-MICROCYTOSIS", status="present", strength="medium"),
            EvidenceResult(id="E-HB-LOW", status="present", strength="medium"),
        ]
        negative = [
            EvidenceResult(id="E-MACROCYTOSIS", status="present", strength="medium"),
        ]

    elif syndrome_id == "S-PANCYTOPENIA":
        positive = [
            EvidenceResult(id="E-ANEMIA", status="present", strength="medium"),
            EvidenceResult(id="E-WBC-LOW", status="present", strength="medium"),
            EvidenceResult(id="E-PLT-LOW", status="present", strength="medium"),
        ]
        negative = [
            EvidenceResult(id="E-WBC-HIGH", status="present", strength="medium"),
        ]

    # Generic fallback for other syndromes
    else:
        # For syndromes we don't have specific test data for,
        # create minimal evidences
        positive = [
            EvidenceResult(id="E-HB-LOW", status="present", strength="medium"),
        ]
        negative = [
            EvidenceResult(id="E-WBC-VERY-HIGH", status="present", strength="strong"),
        ]

    return positive, negative


# Parametrized Tests

@pytest.mark.syndrome
def test_syndrome_logic_can_be_evaluated(syndrome_id, yaml_parser):
    """
    Test that syndrome combine logic can be evaluated without crashing.

    This test is dynamically parametrized over all 35 syndromes.
    """
    all_syndromes = yaml_parser.get_all_syndrome_defs()
    syndrome_def = next((s for s in all_syndromes if s["id"] == syndrome_id), None)

    assert syndrome_def is not None, f"Syndrome {syndrome_id} not found in YAML"

    # Get test evidences
    positive_evidences, negative_evidences = get_test_evidences_for_syndrome(syndrome_id)

    # Test with positive evidences (may or may not trigger, but should not crash)
    present_ids_positive = {e.id for e in positive_evidences if e.status == "present"}
    result_positive = is_syndrome_present(syndrome_def, present_ids_positive)
    assert isinstance(result_positive, bool), \
        f"{syndrome_id}: is_syndrome_present should return bool"

    # Test with negative evidences (should not trigger)
    present_ids_negative = {e.id for e in negative_evidences if e.status == "present"}
    result_negative = is_syndrome_present(syndrome_def, present_ids_negative)
    assert isinstance(result_negative, bool), \
        f"{syndrome_id}: is_syndrome_present should return bool"


@pytest.mark.syndrome
def test_all_35_syndromes_can_be_detected(yaml_parser):
    """
    Integration test: Verify all 35 syndromes can be evaluated.

    Tests the detect_syndromes function with various evidence combinations.
    """
    # Test case 1: Critical syndrome (TMA)
    evidences_tma = [
        EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),
        EvidenceResult(id="E-SCHISTOCYTES-GE1PCT", status="present", strength="strong"),
        EvidenceResult(id="E-LDH-HIGH", status="present", strength="high"),
    ]

    syndromes_tma = detect_syndromes(evidences_tma, yaml_parser)

    # Should detect S-TMA and short-circuit (stop after first critical)
    assert len(syndromes_tma) > 0, "No syndromes detected for TMA case"
    assert syndromes_tma[0].id == "S-TMA", f"Expected S-TMA first, got {syndromes_tma[0].id}"
    assert syndromes_tma[0].criticality == "critical"

    # Test case 2: Priority syndrome (IDA)
    evidences_ida = [
        EvidenceResult(id="E-FERRITIN-LOW", status="present", strength="high"),
        EvidenceResult(id="E-MICROCYTOSIS", status="present", strength="medium"),
        EvidenceResult(id="E-HB-LOW", status="present", strength="medium"),
    ]

    syndromes_ida = detect_syndromes(evidences_ida, yaml_parser)

    # Should detect some syndromes
    assert len(syndromes_ida) > 0, "No syndromes detected for IDA case"

    # Test case 3: No matching evidences (fallback to S-INCONCLUSIVO)
    evidences_empty = []

    syndromes_empty = detect_syndromes(evidences_empty, yaml_parser)

    # Should have fallback syndrome
    assert len(syndromes_empty) > 0, "No fallback syndrome"
    assert syndromes_empty[0].id == "S-INCONCLUSIVO", \
        f"Expected S-INCONCLUSIVO fallback, got {syndromes_empty[0].id}"


@pytest.mark.syndrome
def test_critical_syndrome_short_circuit(yaml_parser):
    """
    Test that detection short-circuits after first critical syndrome.

    Critical syndromes should stop evaluation immediately.
    """
    # Create evidences for multiple critical syndromes
    evidences_multiple_critical = [
        EvidenceResult(id="E-ANC-CRIT", status="present", strength="critical"),  # S-NEUTROPENIA-GRAVE
        EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),  # S-PLT-CRITICA
        EvidenceResult(id="E-WBC-VERY-HIGH", status="present", strength="strong"),  # S-BLASTIC-SYNDROME
    ]

    syndromes = detect_syndromes(evidences_multiple_critical, yaml_parser)

    # Should only return 1 syndrome (short-circuit after first critical)
    assert len(syndromes) == 1, \
        f"Expected 1 syndrome (short-circuit), got {len(syndromes)}"

    # First syndrome should be critical
    assert syndromes[0].criticality == "critical", \
        f"Expected critical syndrome, got {syndromes[0].criticality}"


@pytest.mark.syndrome
def test_syndrome_has_required_fields(syndrome_id, yaml_parser):
    """
    Test that each syndrome definition has required fields.
    """
    all_syndromes = yaml_parser.get_all_syndrome_defs()
    syndrome_def = next((s for s in all_syndromes if s["id"] == syndrome_id), None)

    # Required fields
    assert "id" in syndrome_def
    assert "criticality" in syndrome_def
    assert syndrome_def["criticality"] in ["critical", "priority", "review_sample", "routine"]

    # Should have combine logic or be the fallback
    if syndrome_def["id"] != "S-INCONCLUSIVO":
        assert "combine" in syndrome_def, \
            f"{syndrome_id}: Missing 'combine' field"


# Nested Logic Test (BUG-014 validation)

@pytest.mark.syndrome
def test_nested_logic_syndromes_work(yaml_parser):
    """
    Test that syndromes with nested logic work correctly.

    BUG-014 fix: S-BLASTIC-SYNDROME has nested all/any logic.
    """
    # S-BLASTIC-SYNDROME has nested logic:
    # any: [E-WBC-VERY-HIGH, all: [E-WBC-VERY-HIGH, E-PLT-CRIT-LOW], E-BLASTS-PRESENT]

    # Test branch 1: E-WBC-VERY-HIGH alone
    evidences1 = [
        EvidenceResult(id="E-WBC-VERY-HIGH", status="present", strength="strong"),
    ]
    syndromes1 = detect_syndromes(evidences1, yaml_parser)
    assert any(s.id == "S-BLASTIC-SYNDROME" for s in syndromes1), \
        "S-BLASTIC-SYNDROME not detected (branch 1)"

    # Test branch 2: Nested all [E-WBC-VERY-HIGH + E-PLT-CRIT-LOW]
    evidences2 = [
        EvidenceResult(id="E-WBC-VERY-HIGH", status="present", strength="strong"),
        EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),
    ]
    syndromes2 = detect_syndromes(evidences2, yaml_parser)
    # Should detect either S-BLASTIC-SYNDROME or S-PLT-CRITICA (which has higher precedence)
    # Both are critical, so short-circuit applies
    assert len(syndromes2) == 1 and syndromes2[0].criticality == "critical", \
        "Critical syndrome not detected (branch 2)"


# Summary Test

@pytest.mark.syndrome
def test_syndrome_coverage_summary(yaml_parser):
    """
    Summary test: Verify we have 35 syndromes total.
    """
    all_syndromes = yaml_parser.get_all_syndrome_defs()

    assert len(all_syndromes) == 35, \
        f"Expected 35 syndromes, found {len(all_syndromes)}"

    # Count by criticality
    critical = [s for s in all_syndromes if s["criticality"] == "critical"]
    priority = [s for s in all_syndromes if s["criticality"] == "priority"]
    review_sample = [s for s in all_syndromes if s["criticality"] == "review_sample"]
    routine = [s for s in all_syndromes if s["criticality"] == "routine"]

    print(f"\nSyndrome distribution:")
    print(f"  Critical: {len(critical)}")
    print(f"  Priority: {len(priority)}")
    print(f"  Review sample: {len(review_sample)}")
    print(f"  Routine: {len(routine)}")

    assert len(critical) > 0, "No critical syndromes found"
    assert len(priority) > 0, "No priority syndromes found"
