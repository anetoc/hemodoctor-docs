# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**HemoDoctor Hybrid V1.0** is a clinical decision support system (SaMD Class III) for complete blood count (CBC) analysis. The system classifies cases into 34 hematological syndromes using a deterministic YAML-based rule engine with regulatory compliance for ANVISA/FDA/ISO 13485.

**Key Facts:**
- 15 modular YAML files (~7,350 lines) define the clinical logic
- 34 syndromes (8 critical, 23 priority, 1 review_sample, 2 routine)
- 75 atomic evidence rules (E-XXX)
- Always-output design (6-level fallback chain)
- WORM log with HMAC-SHA256 for audit compliance

---

## Repository Structure

```
HEMODOCTOR_HIBRIDO_V1.0/
├── YAMLs/                          # 15 YAML modules (CORE LOGIC)
│   ├── 00_config_hybrid.yaml       # Units, cutoffs, normalization
│   ├── 01_schema_hybrid.yaml       # Canonical schema
│   ├── 02_evidence_hybrid.yaml     # 75 evidence rules
│   ├── 03_syndromes_hybrid.yaml    # 34 syndromes (DAG fusion)
│   ├── 04_output_templates_hybrid.yaml
│   ├── 05_missingness_hybrid_v2.3.yaml  # Proxy logic + guaranteed output
│   ├── 06_route_policy_hybrid.yaml      # Deterministic routing
│   ├── 07_conflict_matrix_hybrid.yaml
│   ├── 07_normalization_heuristics.yaml
│   ├── 08_wormlog_hybrid.yaml           # WORM audit log
│   ├── 09_next_steps_engine_hybrid.yaml # Clinical next steps
│   ├── 10_runbook_hybrid.yaml           # Implementation roadmap
│   ├── 11_case_state_hybrid.yaml        # State machine
│   └── 12_output_policies_hybrid.yaml   # Output orchestration
│
├── Analise_Comparativa/            # Design decisions
│   ├── ANALISE_COMPARATIVA_TRIPLA_*.md
│   └── COMPARACAO_HIBRIDO_vs_SADMH_V2.3.md
│
├── Especificacoes_Dev/             # Dev team specs
│   └── DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md
│
├── README.md                       # Project overview
├── INDEX_COMPLETO.md               # Complete file index
└── QUICKSTART_IMPLEMENTACAO.md     # Dev quick start
```

---

## Core Architecture (Data Flow)

```
CBC Input (CSV/HL7/JSON)
  ↓
[00_config] Normalization (units, site-specific)
  ↓
[01_schema] Validation (canonical schema)
  ↓
[02_evidence] Evidence evaluation (75 rules → E-XXX)
  ↓
[03_syndromes] DAG fusion (34 syndromes → S-XXX)
  ↓
[05_missingness] Proxy logic + guaranteed output
  ↓
[06_route_policy] Precedence + route_id (SHA256)
  ↓
[09_next_steps] Prioritized clinical recommendations
  ↓
[12_output] Card rendering (markdown/HTML/JSON/FHIR)
  ↓
[08_wormlog] Immutable audit log (HMAC)
```

---

## Development Workflow

### Reading Order (First Time)

1. **README.md** (5 min) - Project overview
2. **QUICKSTART_IMPLEMENTACAO.md** (15 min) - Dev guide
3. **YAMLs/10_runbook_hybrid.yaml** (10 min) - Implementation roadmap
4. **YAMLs/00_config_hybrid.yaml** - Configuration reference
5. **YAMLs/01_schema_hybrid.yaml** - Schema reference

### Implementation Phases (from 10_runbook_hybrid.yaml)

**V0 (8 weeks) - Deterministic:**
- Sprint 0 (1 week): Parsers + normalization
- Sprint 1 (2 weeks): Evidence engine + syndromes
- Sprint 2 (2 weeks): Missingness + next_steps + output
- Sprint 3 (1 week): Audit (WORM log + routing)
- Sprint 4 (2 weeks): Red List validation (FN=0 critical)

**V1 (4 weeks) - Calibration:**
- Sprint 5-6: Platt scaling + confidence (C0/C1/C2)

**V2 (4-6 weeks) - ML/GNN (optional):**
- Sprint 7-9: Explainable ML + fairness audit

---

## Working with YAMLs

### YAML Module Dependencies

**Core pipeline (sequential):**
```
00_config → 01_schema → 02_evidence → 03_syndromes → 04_templates
```

**Always-output (V2.3):**
```
03_syndromes → 05_missingness → 09_next_steps → 12_output
```

**Audit trail:**
```
03_syndromes → 06_route_policy → 07_conflict_matrix → 08_wormlog
```

**Operational:**
```
09_next_steps → 11_case_state → 12_output
```

### Validation

```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('YAMLs/00_config_hybrid.yaml'))"

# Validate all YAMLs
for f in YAMLs/*.yaml; do python -c "import yaml; yaml.safe_load(open('$f'))"; done
```

### Common Patterns

**Evidence rules (02_evidence_hybrid.yaml):**
```yaml
- id: E-ANC-CRIT
  strength: critical
  rule: "anc < anc_critical"  # Use safe eval (simpleeval, NOT eval())
  requires: ["anc"]
```

**Syndrome logic (03_syndromes_hybrid.yaml):**
```yaml
- id: S-TMA
  criticality: critical
  combine:
    all: ["E-SCHISTOCYTES-GE1PCT", "E-PLT-CRIT-LOW"]
    any: ["E-HEMOLYSIS-PATTERN", "E-LDH-HIGH"]
  threshold: 0.0  # All required evidences must be present
```

**Next steps (09_next_steps_engine_hybrid.yaml):**
```yaml
- id: trigger_tma
  when: "'S-TMA' in syndromes and syndromes['S-TMA'].criticality == 'critical'"
  suggest:
    - level: urgent
      test: "Blood smear + LDH + indirect bilirubin + creatinine"
      rationale: "Confirm microangiopathic hemolysis and assess organ damage"
      cost: low
      turnaround: "<2h"
```

---

## Common Development Tasks

### Setup Development Environment

```bash
# Navigate to project
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_HIBRIDO_V1.0

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pyyaml jsonschema pytest simpleeval python-dateutil

# Validate YAML files
python -c "import yaml; yaml.safe_load(open('YAMLs/00_config_hybrid.yaml'))"
```

### Run Tests (Sprint 0)

```python
# test_sprint0.py
import pytest
import yaml

def test_parse_cbc():
    """Test CBC parsing to canonical schema"""
    cbc = parse_csv("data/adult_male_normal.csv")
    assert cbc["hb"] == 15.2
    assert cbc["sex"] == "M"

def test_evidence_anc_critical():
    """Test critical ANC evidence"""
    cbc = {"anc": 0.3}
    evidences = evaluate_evidences(cbc, config)
    assert "E-ANC-CRIT" in [e.id for e in evidences if e.status == "present"]

def test_syndrome_tma_critical():
    """Test TMA syndrome detection"""
    cbc = {
        "plt": 8,
        "ldh": 980,
        "morphology": {"esquistocitos": True}
    }
    evidences = evaluate_evidences(cbc, config)
    syndromes = fuse_syndromes(evidences, config)
    assert "S-TMA" in [s.id for s in syndromes]
    assert syndromes[0].criticality == "critical"
```

### Safe Expression Evaluation

**NEVER use `eval()` directly:**

```python
# ❌ WRONG - Security vulnerability
result = eval(f"{cbc['anc']} < {config['anc_critical']}")

# ✅ CORRECT - Use simpleeval
from simpleeval import simple_eval

result = simple_eval(
    "anc < anc_critical",
    names={
        "anc": cbc.get("anc"),
        "anc_critical": config["cutoffs"]["anc_critical"]
    }
)
```

### Handle Missing Data

```python
# ❌ WRONG - Raises KeyError
if cbc["ferritin"] < 30:
    return "present"

# ✅ CORRECT - Handle missing gracefully
if cbc.get("ferritin") is not None and cbc["ferritin"] < 30:
    return "present"
else:
    return "unknown"  # Explicit unknown status
```

### Unit Normalization

```python
# Convert based on site-specific patterns (07_normalization_heuristics.yaml)
def normalize_units(value, from_unit, to_unit, config):
    """
    Example: Hb g/L → g/dL
    If median > 50, assume g/L and divide by 10
    """
    if from_unit == "g/L" and to_unit == "g/dL":
        return value / 10.0
    return value
```

---

## Critical Safety Rules

### Short-Circuit for Critical Syndromes

```python
# ✅ CORRECT - Stop after first critical syndrome
syndromes = []
for s in sorted_by_precedence(syndrome_list):
    syndrome = evaluate(s)
    syndromes.append(syndrome)
    if syndrome.criticality == "critical":
        break  # Short-circuit

# ❌ WRONG - Processes all syndromes
syndromes = [evaluate(s) for s in syndrome_list]
```

### Red List Validation (Gate Crítico)

**FN = 0 for critical syndromes is MANDATORY:**

- 240 minimum cases (40 per critical syndrome)
- Blind adjudication by 2 hematologists
- If FN > 0 → Extra Sprint 4 (2 weeks) for tuning

**Critical syndromes:**
1. S-NEUTROPENIA-GRAVE (ANC <0.5)
2. S-BLASTIC-SYNDROME (blasts present)
3. S-TMA (schistocytes + PLT <30)
4. S-PLT-CRITICA (PLT <20)
5. S-ANEMIA-GRAVE (Hb <6.5 M / <6.0 F)
6. S-NEUTROFILIA-LEFTSHIFT-CRIT
7. S-THROMBOCITOSE-CRIT (PLT ≥1000)
8. S-CIVD (≥2 markers altered)

### WORM Log (Audit Compliance)

```python
# Immutable append-only JSONL log
# Module: 08_wormlog_hybrid.yaml

log_entry = {
    "event_ts": "2025-10-19T12:34:56Z",
    "case_id_hash": sha256(case_id),  # Pseudonymization
    "route_id": sha256(evidences + syndromes + output_class),
    "top_syndromes": ["S-TMA", "S-PLT-CRITICA"],
    "fired_evidences": ["E-SCHISTOCYTES-GE1PCT", "E-PLT-CRIT-LOW"],
    "hmac_signature": hmac_sha256(entry, kms_key)  # KMS-backed key
}
```

---

## Quality Metrics

### V0 Targets (Mandatory)

- **FN critical:** 0 (zero false negatives in Red List)
- **Sensitivity critical:** ≥99%
- **Specificity overall:** ≥80%
- **Alert burden:** <20% (<200/1000 cases)
- **Abstention rate (C0):** <10%

### V1 Targets (Ideal)

- **ECE (Expected Calibration Error):** <0.05
- **Calibration curves:** Reliability diagram OK
- **C0/C1/C2 distribution:** Balanced

---

## Regulatory Context

**Standards:**
- **ANVISA RDC 657/2022:** SaMD Class III (high risk)
- **FDA 21 CFR Part 11:** Electronic records
- **ISO 13485:2016:** Quality management
- **IEC 62304:** Software Class C (highest risk)
- **LGPD:** Data protection (90d retention)

**Key Requirements:**
- Immutable audit trail (WORM log)
- Pseudonymization (SHA256 hashing)
- Traceability (route_id + alt_routes)
- Transparency (clinical rationale for all decisions)

---

## Troubleshooting

### YAML Syntax Errors

```bash
# Check specific file
python -c "import yaml; yaml.safe_load(open('YAMLs/03_syndromes_hybrid.yaml'))"

# If error, check indentation and special characters
```

### Missing Data Handling

See module `05_missingness_hybrid_v2.3.yaml`:
- Global policy: >30% missing → C0 (abstain with guidance)
- Proxy logic: Infer missing values from correlated fields
- Guaranteed output: 6-level fallback (never empty result)

### Performance Target

- **Pipeline latency:** <100ms per case (V0 target: <50ms)
- **Throughput:** >1000 cases/hour

---

## Contact & Support

**Clinical Owner:** Dr. Abel Costa (IDOR-SP)
**Version:** V1.0
**Status:** ✅ 100% Specified - Ready for Sprint 0
**Date:** October 2025

---

## Additional Resources

- **Complete index:** INDEX_COMPLETO.md
- **Design decisions:** Analise_Comparativa/ANALISE_COMPARATIVA_TRIPLA_*.md
- **Dev spec example:** Especificacoes_Dev/DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md
- **Implementation roadmap:** YAMLs/10_runbook_hybrid.yaml (8-14 weeks)
