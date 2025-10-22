"""
TEST STRUCTURE FIX - Pass Rate 81% → 95%+
===========================================

Issue: Test structure mismatch
Problem: Tests expect dict, but receive CBCResult dataclass
Impact: 13 test failures
Solution: Add result extraction helper function

Expected Impact: +13 tests passing (81% → 95%)
Target: 90/95 tests (95% pass rate)
"""

from dataclasses import dataclass, asdict
from typing import Dict, Any, Union, Optional
import json


# ============================================================================
# DATACLASS DEFINITIONS (Example)
# ============================================================================

@dataclass
class AgeGroup:
    """Pediatric age group with reference ranges."""
    name: str
    age_min: float
    age_max: float
    platelet_min: int
    platelet_max: int


@dataclass
class SeverityClassification:
    """Platelet count severity classification."""
    level: str  # "Normal", "Mild", "Moderate", "Severe", "Critical"
    platelet_count: int
    reference_min: int
    reference_max: int
    clinical_significance: str


@dataclass
class CBCResult:
    """Complete Blood Count analysis result."""
    patient_id: str
    age_months: float
    age_group: AgeGroup
    platelet_count: int
    severity: SeverityClassification
    timestamp: str
    warnings: list = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert CBCResult dataclass to dictionary.

        This method enables compatibility with tests that expect dict format.
        All nested dataclasses are also converted to dicts.

        Returns:
            Dictionary representation of CBCResult

        Examples:
            >>> result = CBCResult(...)
            >>> result_dict = result.to_dict()
            >>> assert isinstance(result_dict, dict)
            >>> assert "patient_id" in result_dict
        """
        return {
            "patient_id": self.patient_id,
            "age_months": self.age_months,
            "age_group": {
                "name": self.age_group.name,
                "age_min": self.age_group.age_min,
                "age_max": self.age_group.age_max,
                "platelet_min": self.age_group.platelet_min,
                "platelet_max": self.age_group.platelet_max,
            },
            "platelet_count": self.platelet_count,
            "severity": {
                "level": self.severity.level,
                "platelet_count": self.severity.platelet_count,
                "reference_min": self.severity.reference_min,
                "reference_max": self.severity.reference_max,
                "clinical_significance": self.severity.clinical_significance,
            },
            "timestamp": self.timestamp,
            "warnings": self.warnings or [],
        }


# ============================================================================
# FIX #1: Result Extraction Helper (PRIMARY FIX)
# ============================================================================

def extract_result(response: Union[CBCResult, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Extract result as dictionary from either dataclass or dict.

    This is the PRIMARY FIX for test structure issues.
    Tests expect dict format, but code may return dataclass.
    This function normalizes the return type.

    Args:
        response: Either CBCResult dataclass or dict

    Returns:
        Dictionary representation of result

    Raises:
        TypeError: If response is neither dict nor CBCResult

    Examples:
        >>> # Test receives dataclass
        >>> result = analyze_cbc(patient_data)
        >>> result_dict = extract_result(result)
        >>> assert result_dict["patient_id"] == "PAT001"

        >>> # Test receives dict (already correct format)
        >>> result_dict = extract_result({"patient_id": "PAT001"})
        >>> assert result_dict["patient_id"] == "PAT001"

    Usage in tests:
        # BEFORE (fails when receiving dataclass):
        result = analyze_cbc(patient_data)
        assert result["patient_id"] == "PAT001"  # KeyError if dataclass!

        # AFTER (works with both):
        result = analyze_cbc(patient_data)
        result_dict = extract_result(result)
        assert result_dict["patient_id"] == "PAT001"  # Always works!
    """
    if isinstance(response, dict):
        return response
    elif hasattr(response, 'to_dict'):
        return response.to_dict()
    elif hasattr(response, '__dataclass_fields__'):
        # Fallback: use asdict for standard dataclasses
        return asdict(response)
    else:
        raise TypeError(
            f"Expected dict or dataclass, got {type(response).__name__}. "
            f"Response must be either a dictionary or have a to_dict() method."
        )


# ============================================================================
# FIX #2: Test Fixture Update (conftest.py)
# ============================================================================

def pytest_configure_fixtures():
    """
    Update conftest.py with result extraction fixture.

    Add this to conftest.py in the test directory:
    """
    return """
import pytest
from typing import Union, Dict, Any

@pytest.fixture
def extract_result():
    '''Fixture to extract dictionary from test results.'''
    def _extract(response: Union[object, Dict[str, Any]]) -> Dict[str, Any]:
        if isinstance(response, dict):
            return response
        elif hasattr(response, 'to_dict'):
            return response.to_dict()
        elif hasattr(response, '__dataclass_fields__'):
            from dataclasses import asdict
            return asdict(response)
        else:
            raise TypeError(f"Cannot extract result from {type(response)}")
    return _extract
"""


# ============================================================================
# FIX #3: Update Test Files (test_pediatric_platelet.py)
# ============================================================================

class TestUpdater:
    """
    Helper class to show how to update test files.
    """

    @staticmethod
    def show_before_after():
        """Show test update examples."""

        before = """
def test_platelet_classification_24_months():
    '''Test 2-year-old classification.'''
    patient_data = {
        "age_months": 24.0,
        "platelet_count": 120000
    }

    result = analyze_cbc(patient_data)

    # PROBLEM: Fails if result is dataclass
    assert result["age_group"]["name"] == "PED-03: Infant Late"
    assert result["severity"]["level"] == "Mild"
"""

        after = """
def test_platelet_classification_24_months(extract_result):
    '''Test 2-year-old classification.'''
    patient_data = {
        "age_months": 24.0,
        "platelet_count": 120000
    }

    result = analyze_cbc(patient_data)

    # FIX: Extract dict first
    result_dict = extract_result(result)

    # Now works with both dict and dataclass
    assert result_dict["age_group"]["name"] == "PED-03: Infant Late"
    assert result_dict["severity"]["level"] == "Mild"
"""

        return {
            "before": before,
            "after": after,
            "changes": [
                "1. Add 'extract_result' fixture parameter",
                "2. Call extract_result(result) to normalize format",
                "3. Use result_dict instead of result for assertions"
            ]
        }


# ============================================================================
# FIX #4: Batch Update Script
# ============================================================================

def generate_test_update_script():
    """
    Generate sed/awk script to batch update test files.

    This script can be applied to all test files to add extract_result calls.
    """
    return """#!/bin/bash
# Batch update test files to use extract_result

TEST_DIR="test_automation"
TEST_FILE="test_pediatric_platelet.py"

# Backup original
cp "${TEST_DIR}/${TEST_FILE}" "${TEST_DIR}/${TEST_FILE}.backup"

# Find all test functions that use result assertions
grep -n 'result\\[' "${TEST_DIR}/${TEST_FILE}" | while read -r line; do
    line_num=$(echo "$line" | cut -d: -f1)
    echo "Updating line $line_num"
done

# Add extract_result fixture to test functions
# (Manual approach recommended for precision)

echo "✅ Test files backed up"
echo "⚠️  Manual update recommended - see TEST_STRUCTURE_FIX_IMPLEMENTATION.py"
"""


# ============================================================================
# VALIDATION TESTS
# ============================================================================

def test_extract_result_with_dict():
    """Test extract_result with dictionary input."""
    test_dict = {
        "patient_id": "PAT001",
        "age_months": 24.0,
        "platelet_count": 120000
    }

    result = extract_result(test_dict)
    assert result == test_dict
    assert isinstance(result, dict)
    print("✅ Test 1 PASSED: Dict input preserved")


def test_extract_result_with_dataclass():
    """Test extract_result with CBCResult dataclass."""
    age_group = AgeGroup(
        name="PED-03: Infant Late",
        age_min=6.0,
        age_max=24.0,
        platelet_min=200,
        platelet_max=475
    )

    severity = SeverityClassification(
        level="Mild",
        platelet_count=120000,
        reference_min=200000,
        reference_max=475000,
        clinical_significance="Mild thrombocytopenia"
    )

    cbc_result = CBCResult(
        patient_id="PAT001",
        age_months=24.0,
        age_group=age_group,
        platelet_count=120000,
        severity=severity,
        timestamp="2025-10-22T10:00:00Z",
        warnings=[]
    )

    result = extract_result(cbc_result)

    assert isinstance(result, dict)
    assert result["patient_id"] == "PAT001"
    assert result["age_months"] == 24.0
    assert result["age_group"]["name"] == "PED-03: Infant Late"
    assert result["severity"]["level"] == "Mild"
    print("✅ Test 2 PASSED: Dataclass converted to dict")


def test_extract_result_error_handling():
    """Test extract_result with invalid input."""
    try:
        result = extract_result(12345)  # Invalid type
        assert False, "Should have raised TypeError"
    except TypeError as e:
        assert "Expected dict or dataclass" in str(e)
        print("✅ Test 3 PASSED: Invalid input raises TypeError")


# ============================================================================
# EXPECTED IMPACT ANALYSIS
# ============================================================================

def analyze_expected_impact():
    """
    Analyze expected impact of test structure fix.
    """

    impact = {
        "current_status": {
            "pass_rate": "81%",
            "tests_passing": "77/95",
            "tests_failing": "18",
            "bugs_resolved": "7/7 (Bug #2 fixed)"
        },

        "failing_test_categories": {
            "test_structure_issues": {
                "count": 13,
                "cause": "Tests expect dict, receive CBCResult dataclass",
                "affected_tests": [
                    "TC-PED-02-*",  # Infant Early tests
                    "TC-PED-03-*",  # Infant Late tests
                    "TC-PED-04-*",  # Preschool tests
                    "TC-PED-05-*",  # School Age tests
                    "TC-SEVERITY-*"  # Severity classification tests
                ],
                "fix": "Add extract_result() calls"
            },

            "other_issues": {
                "count": 5,
                "potential_causes": [
                    "Floating point precision (tolerance needed)",
                    "Timestamp format mismatches",
                    "Edge cases not covered",
                    "Mock data inconsistencies",
                    "Assertion logic errors"
                ],
                "investigation_needed": True
            }
        },

        "after_fix": {
            "expected_pass_rate": "95%",
            "expected_passing": "90/95",
            "improvement": "+13 tests",
            "remaining_failures": "5 tests (need investigation)"
        },

        "stretch_goal": {
            "target": "100%",
            "passing": "95/95",
            "additional_work": "Investigate and fix remaining 5 tests",
            "estimated_time": "2-4 hours"
        }
    }

    return impact


# ============================================================================
# IMPLEMENTATION CHECKLIST
# ============================================================================

def get_implementation_checklist():
    """
    Return step-by-step implementation checklist.
    """
    return """
TEST STRUCTURE FIX - IMPLEMENTATION CHECKLIST
=============================================

□ PHASE 1: Update Test Infrastructure (30 min)
  □ Add extract_result() to conftest.py
  □ Add pytest fixture
  □ Test fixture works with sample data

□ PHASE 2: Update Test Files (1 hour)
  □ Backup test_pediatric_platelet.py
  □ Add extract_result fixture to test functions
  □ Update ~13 test functions with result_dict = extract_result(result)
  □ Replace result["..."] with result_dict["..."]

□ PHASE 3: Validation (30 min)
  □ Run pytest -v
  □ Verify 90/95 tests passing (95%)
  □ Document which 5 tests still failing

□ PHASE 4: Investigate Remaining Failures (2-4 hours)
  □ Run pytest -vv on failing tests
  □ Analyze error messages
  □ Fix issues (likely minor):
    - Floating point tolerances
    - Timestamp formats
    - Edge case handling
  □ Retest until 95-100% pass rate

□ PHASE 5: Documentation (30 min)
  □ Update CHANGELOG.md
  □ Update test documentation
  □ Update pass rate in STATUS_ATUAL.md
  □ Commit changes

TOTAL TIME: 4-6 hours
EXPECTED RESULT: 95-100% pass rate
"""


# ============================================================================
# MAIN VALIDATION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("TEST STRUCTURE FIX VALIDATION")
    print("=" * 70)
    print()

    print("Running validation tests...")
    print()

    try:
        test_extract_result_with_dict()
        test_extract_result_with_dataclass()
        test_extract_result_error_handling()

        print()
        print("=" * 70)
        print("✅ ALL VALIDATION TESTS PASSED!")
        print("=" * 70)
        print()

        print("EXPECTED IMPACT:")
        print("-" * 70)
        impact = analyze_expected_impact()
        print(f"Current:  {impact['current_status']['tests_passing']} ({impact['current_status']['pass_rate']})")
        print(f"After:    {impact['after_fix']['expected_passing']} ({impact['after_fix']['expected_pass_rate']})")
        print(f"Improvement: {impact['after_fix']['improvement']}")
        print()
        print(f"Stretch Goal: {impact['stretch_goal']['passing']} (100%)")
        print()

        print("IMPLEMENTATION STEPS:")
        print("-" * 70)
        print(get_implementation_checklist())

        print()
        print("NEXT STEPS:")
        print("-" * 70)
        print("1. Copy extract_result() to conftest.py")
        print("2. Update test_pediatric_platelet.py (~13 functions)")
        print("3. Run pytest -v to verify 95% pass rate")
        print("4. Investigate remaining 5 failures (if any)")
        print("5. Commit changes")
        print()
        print("FILES TO UPDATE:")
        print("-" * 70)
        print("- conftest.py: Add extract_result fixture")
        print("- test_pediatric_platelet.py: Update ~13 test functions")
        print()

    except AssertionError as e:
        print()
        print("=" * 70)
        print("❌ VALIDATION FAILED!")
        print("=" * 70)
        print(f"Error: {e}")
        exit(1)
