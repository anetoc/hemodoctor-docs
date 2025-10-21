---
name: Test Suite
description: Create and run tests for HemoDoctor Hybrid V1.0 using pytest. Use when implementing Sprint 0 tests, debugging test failures, or validating Red List requirements (FN=0 critical).
---

# Test Suite

Pytest-based testing for HemoDoctor's clinical decision engine.

## Quick start

Run all tests:

```bash
pytest -v
```

Run specific test file:

```bash
pytest test_sprint0.py -v
```

Run specific test:

```bash
pytest test_sprint0.py::test_evidence_anc_critical -v
```

## Test structure (Sprint 0)

**Sprint 0 test requirements (20 test cases minimum):**

1. **Parser tests (3):**
   - Adult male normal CBC
   - Adult female normal CBC
   - Pediatric CBC

2. **Pre-analytical tests (3):**
   - MCHC >38 (implausible)
   - Cold agglutinin (MCV >130)
   - Pseudo-thrombocytopenia (aglomerados)

3. **Evidence tests (8):**
   - E-ANC-CRIT (present/absent/unknown)
   - E-IDA-LABS (present/absent/unknown)
   - E-SCHISTOCYTES-GE1PCT (morphology)

4. **Syndrome tests (3):**
   - S-TMA (critical)
   - S-IDA (priority)
   - S-NEUTROPENIA-GRAVE (critical)

5. **Short-circuit test (1):**
   - Critical syndrome stops processing

6. **End-to-end tests (2):**
   - TMA case (CSV → card)
   - IDA case (CSV → card)

## Test template

```python
import pytest
import yaml


@pytest.fixture
def config():
    """Load configuration"""
    with open("YAMLs/00_config_hybrid.yaml") as f:
        return yaml.safe_load(f)


def test_evidence_anc_critical(config):
    """Test critical ANC evidence"""
    evidence = {
        "id": "E-ANC-CRIT",
        "rule": "anc < anc_critical",
        "requires": ["anc"]
    }

    # Positive case
    cbc = {"anc": 0.3}
    assert evaluate_evidence(evidence, cbc, config) == "present"

    # Negative case
    cbc = {"anc": 2.0}
    assert evaluate_evidence(evidence, cbc, config) == "absent"

    # Missing data
    cbc = {}
    assert evaluate_evidence(evidence, cbc, config) == "unknown"
```

## Red List validation

**FN = 0 for critical syndromes is MANDATORY:**

```python
@pytest.mark.redlist
def test_redlist_tma():
    """Red List: TMA cases must be detected (FN=0)"""

    # Load 40 TMA cases
    cases = load_cases("test_data/redlist_tma.csv")

    false_negatives = 0
    for case in cases:
        syndromes = pipeline(case)
        if "S-TMA" not in [s.id for s in syndromes]:
            false_negatives += 1
            print(f"MISSED: {case['case_id']}")

    # MUST be zero
    assert false_negatives == 0, f"FN critical = {false_negatives} (MUST be 0)"
```

**Run Red List tests:**

```bash
pytest -v -m redlist
```

## Coverage target

**V0 requirements:**
- Line coverage: ≥80%
- Branch coverage: ≥70%
- Critical paths: 100%

**Generate coverage report:**

```bash
pytest --cov=. --cov-report=html
open htmlcov/index.html
```

## Common test patterns

**Parametrized tests:**

```python
@pytest.mark.parametrize("anc,expected", [
    (0.1, "present"),
    (0.3, "present"),
    (0.5, "absent"),
    (2.0, "absent"),
    (None, "unknown"),
])
def test_anc_critical_cases(anc, expected):
    evidence = load_evidence("E-ANC-CRIT")
    cbc = {"anc": anc} if anc is not None else {}
    assert evaluate_evidence(evidence, cbc) == expected
```

**Fixtures for test data:**

```python
@pytest.fixture
def cbc_normal_adult_male():
    return {
        "hb": 15.2,
        "ht": 45.0,
        "rbc": 5.0,
        "wbc": 7.5,
        "anc": 4.5,
        "plt": 250,
        "mcv": 90,
        "mch": 30,
        "mchc": 33,
        "rdw": 13,
        "sex": "M",
        "age_years": 45
    }
```

## Troubleshooting tests

**Test fails unexpectedly:**
1. Check YAML files loaded correctly
2. Verify cutoff values match config
3. Print intermediate values
4. Check for type mismatches

**Coverage too low:**
1. Add edge case tests
2. Test error conditions
3. Test missing data handling
4. Test boundary values

**Slow tests:**
1. Use fixtures for expensive setup
2. Mock external dependencies
3. Parallelize with pytest-xdist: `pytest -n auto`
