# HemoDoctor CDSS v2.4.0

**Clinical Decision Support System for Hematology**

SaMD Class III (ANVISA RDC 657/751) | IEC 62304 Class C | ISO 14971:2019

---

## Overview

HemoDoctor is a YAML-driven clinical decision support system for CBC (Complete Blood Count) analysis, implementing:

- **79 clinical evidences** (E-XXX) from `02_evidence_hybrid.yaml` v2.4.0
- **35 hematological syndromes** (S-XXX) from `03_syndromes_hybrid.yaml` v2.3.1
- **40 next-steps triggers** from `09_next_steps_engine_hybrid.yaml`
- **WORM audit log** with HMAC-SHA256 integrity
- **Deterministic routing** with SHA256 route_id

---

## Key Features

✅ **100% YAML-driven** - All clinical logic in declarative YAML files
✅ **Safe evaluation** - Uses `simpleeval` (NEVER `eval()`)
✅ **Deterministic** - Reproducible results with SHA256 routing
✅ **Always-output** - 6-level fallback guarantees useful result
✅ **Audit compliant** - Immutable WORM log (1825-day retention)
✅ **IEC 62304 Class C** - Full regulatory compliance

---

## Project Structure

```
hemodoctor_cdss/
├── src/hemodoctor/
│   ├── engines/           # Clinical engines
│   │   ├── evidence.py    # Evidence evaluation (79 rules)
│   │   ├── syndrome.py    # Syndrome detection (35 syndromes)
│   │   ├── next_steps.py  # Next steps (40 triggers)
│   │   ├── normalization.py
│   │   ├── routing.py
│   │   └── worm_log.py
│   ├── models/            # Data models (Pydantic)
│   ├── utils/             # YAML parsers, helpers
│   └── api/               # FastAPI endpoints
├── tests/
│   ├── unit/              # 160 unit tests (Sprint 0)
│   └── integration/       # E2E tests
├── config/                # YAML files (16 modules)
├── data/                  # Test data
└── docs/                  # Documentation
```

---

## Installation

```bash
# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Coverage report
pytest --cov=src/hemodoctor --cov-report=html
```

---

## Usage

```python
from hemodoctor.api import analyze_cbc

# Analyze CBC
cbc_data = {
    "hb": 8.2,
    "wbc": 2.1,
    "plt": 45,
    "age_years": 7,
    "sex": "M"
}

result = analyze_cbc(cbc_data)

print(result["top_syndromes"])  # ['S-PANCYTOPENIA', 'S-ANEMIA-GRAVE']
print(result["next_steps"])      # Clinical recommendations
print(result["route_id"])        # SHA256 deterministic hash
```

---

## Testing

### Sprint 0 (160 tests)

- ✅ 79 evidence unit tests (`TEST-HD-080`)
- ✅ 35 syndrome unit tests (`TEST-HD-081`)
- ✅ 40 next steps tests (`TEST-HD-084`)
- ✅ 6 integration tests (`TEST-HD-085`)

**Target:** Pass rate ≥90%, Coverage ≥85%

```bash
# Run all tests
pytest

# Run only evidence tests
pytest -m evidence

# Run only critical syndrome tests
pytest -m critical

# Generate coverage report
pytest --cov --cov-report=html
open htmlcov/index.html
```

---

## Regulatory Compliance

- **ANVISA RDC 657/2022 + 751/2022** (SaMD Class III)
- **FDA 21 CFR Part 820** (Quality System)
- **IEC 62304:2006+A1:2015** (Software Lifecycle - Class C)
- **ISO 14971:2019** (Risk Management)
- **ISO 13485:2016** (QMS)

---

## YAML Source Files

All clinical logic is defined in 16 YAML modules (9,063 lines):

1. `00_config_hybrid.yaml` - Units, cutoffs, LOINC codes
2. `01_schema_hybrid.yaml` - Canonical schema (54 fields)
3. `02_evidence_hybrid.yaml` v2.4.0 - **79 evidences** ⭐
4. `03_syndromes_hybrid.yaml` v2.3.1 - **35 syndromes** ⭐
5. `04_output_templates_hybrid.yaml` - Markdown/HTML/JSON/FHIR
6. `05_missingness_hybrid_v2.3.yaml` - Proxy logic
7. `06_route_policy_hybrid.yaml` - Deterministic routing
8. `07_conflict_matrix_hybrid.yaml` - Conflict resolution
9. `07_normalization_heuristics.yaml` - Unit detection
10. `08_wormlog_hybrid.yaml` - WORM audit log
11. `09_next_steps_engine_hybrid.yaml` - **40 triggers** ⭐
12. `10_runbook_hybrid.yaml` - Implementation roadmap
13. `11_case_state_hybrid.yaml` - State machine
14. `12_output_policies_hybrid.yaml` - Output orchestration

---

## API Endpoints

**FastAPI REST API:**

- `POST /api/v1/cbc/analyze` - Analyze CBC
- `GET /api/v1/results/{case_id}` - Get results
- `GET /api/v1/trace/{order_id}` - Audit trail
- `GET /api/v1/audit/{case_id}` - Complete audit log

---

## License

Proprietary - HemoDoctor by Dr. Abel Costa

---

## Authors

- **Dr. Abel Costa** - Clinical development
- **@hemodoctor-orchestrator** - Code generation from YAMLs v2.4.0

---

**Generated:** 2025-10-20
**Version:** v2.4.0 (YAML-based reconstruction)
**Status:** Sprint 0 - Implementation in progress
