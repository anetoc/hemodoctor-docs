# SPRINT 4: Red List FN=0 Validation

**Duration:** 2 weeks (23 Nov - 6 Dec 2025)
**Objective:** Validate FN=0 for 9 critical syndromes (MANDATORY REGULATORY GATE)
**Parallel:** Can run in parallel with Sprint 3 (Audit & Traceability)
**Status:** ⏳ READY TO START

---

## 🎯 OBJECTIVES

**PRIMARY GOAL: FN = 0 for all critical syndromes** ⚠️ NON-NEGOTIABLE

1. **Generate 240 Red List Cases** (Week 1)
   - 9 critical syndromes × 30 cases each = 270 cases (safety margin: +30)
   - Synthetic + real-world mix (if available)
   - Blind adjudication by 2 hematologists
   - Gold standard labels

2. **Execute Validation** (Week 1-2)
   - Run all 240 cases through pipeline
   - Collect predictions
   - Compute FN/FP/TP/TN
   - Validate FN=0 for critical syndromes

3. **Clinical Review** (Week 2)
   - Hematologist adjudication
   - Discrepancy resolution
   - Clinical rationale documentation
   - Approval for submission

4. **Report Generation** (Week 2)
   - RED_LIST_VALIDATION_REPORT.md
   - Clinical evidence package
   - Regulatory submission artifacts

---

## 🚨 RED LIST (9 CRITICAL SYNDROMES)

**FN=0 MANDATORY** for these syndromes:

1. **S-NEUTROPENIA-GRAVE** (ANC <0.5 ×10⁹/L)
   - Risk: Febrile neutropenia, sepsis
   - Action: Immediate hospitalization + G-CSF

2. **S-BLASTIC-SYNDROME** (blasts present or WBC very high)
   - Risk: Acute leukemia, tumor lysis
   - Action: Urgent hematology referral

3. **S-TMA** (schistocytes + PLT <10 + hemolysis)
   - Risk: Thrombotic microangiopathy, organ failure
   - Action: Emergency plasmapheresis

4. **S-PLT-CRITICA** (PLT <10 ×10⁹/L)
   - Risk: Life-threatening bleeding
   - Action: Immediate platelet transfusion

5. **S-ANEMIA-GRAVE** (Hb <6.5 g/dL M / <6.0 F)
   - Risk: Cardiac decompensation
   - Action: Urgent transfusion

6. **S-NEUTROFILIA-LEFTSHIFT-CRIT** (neutrophilia + left shift)
   - Risk: Leukemoid reaction, CML
   - Action: Urgent hematology referral

7. **S-THROMBOCITOSE-CRIT** (PLT ≥1000 ×10⁹/L)
   - Risk: Thrombosis + bleeding paradox
   - Action: Cytoreduction + aspirin

8. **S-CIVD** (DIC - ≥2 markers altered)
   - Risk: Disseminated intravascular coagulation
   - Action: ICU admission + supportive care

9. **S-APL** (Acute promyelocytic leukemia pattern)
   - Risk: Catastrophic bleeding
   - Action: Emergency ATRA + chemotherapy

---

## 📋 TASKS BREAKDOWN

### Week 1: Case Generation & Validation Setup

#### Day 1-2: Synthetic Case Generation (16h)

**Task 1.1: Critical Cases** (8h)
- [ ] Generate 30 cases per critical syndrome (270 total)
- [ ] Use clinical-test-generator skill
- [ ] Ensure coverage of edge cases (borderline, extreme)
- [ ] Add clinical context (age, sex, morphology)

**Task 1.2: Gold Standard Labels** (4h)
- [ ] Create ground truth JSON
- [ ] Document clinical rationale
- [ ] Add expected evidence list
- [ ] Add expected next steps

**Task 1.3: Quality Check** (4h)
- [ ] Review all 270 cases
- [ ] Verify clinical plausibility
- [ ] Check data completeness
- [ ] Validate against YAMLs

**Deliverable:** `data/red_list/critical_cases.json` (270 cases)

---

#### Day 3-4: Real-World Cases (Optional) (16h)

**Task 2.1: Data Collection** (8h)
- [ ] Request anonymized real cases from UNIMED Vale do SF
- [ ] Dr. Lucyo Diniz approval
- [ ] Ethics committee review (if needed)
- [ ] Pseudonymization (Presidio)

**Task 2.2: Gold Standard Adjudication** (8h)
- [ ] Blind review by 2 hematologists
- [ ] Discrepancy resolution protocol
- [ ] Consensus labels
- [ ] Clinical notes

**Deliverable:** `data/red_list/real_cases.json` (optional, 30-50 cases)

---

#### Day 5: Validation Framework (8h)

**Task 3.1: Test Infrastructure** (4h)
- [ ] Create test_red_list_validation.py
- [ ] Implement metrics computation (FN, FP, TP, TN)
- [ ] Create confusion matrix generator
- [ ] Add per-syndrome breakdown

**Task 3.2: Reporting Framework** (4h)
- [ ] Create RED_LIST_VALIDATION_REPORT.md template
- [ ] Add clinical evidence sections
- [ ] Add regulatory compliance checklist
- [ ] Add executive summary

**Deliverable:** `tests/clinical/test_red_list_validation.py`

---

### Week 2: Execution & Clinical Review

#### Day 6-7: Validation Execution (16h)

**Task 4.1: Run All Cases** (8h)
- [ ] Execute 270 critical cases
- [ ] Collect predictions
- [ ] Save results to JSON
- [ ] Generate WORM log entries

**Task 4.2: Metrics Computation** (4h)
- [ ] Compute per-syndrome metrics:
  - Sensitivity (must be 100% for critical)
  - Specificity
  - PPV, NPV
  - F1 score
- [ ] Generate confusion matrices
- [ ] Identify FN cases (if any)

**Task 4.3: Failure Analysis** (4h)
- [ ] If FN > 0: Root cause analysis
- [ ] Review evidence evaluation
- [ ] Check syndrome fusion logic
- [ ] Document discrepancies

**Deliverable:** `results/red_list_metrics.json`

---

#### Day 8-9: Clinical Review & Tuning (16h)

**Task 5.1: Hematologist Review** (8h)
- [ ] Review all FN cases (if any)
- [ ] Validate FP cases (acceptable?)
- [ ] Clinical rationale for discrepancies
- [ ] Approval for each syndrome

**Task 5.2: Tuning (if needed)** (8h)
- [ ] If FN > 0: Adjust thresholds
- [ ] Re-run validation
- [ ] Verify FN=0 achieved
- [ ] Document changes

**Deliverable:** Clinical approval signatures

---

#### Day 10: Report Generation (8h)

**Task 6.1: Main Report** (4h)
- [ ] Complete RED_LIST_VALIDATION_REPORT.md
- [ ] Add metrics tables
- [ ] Add confusion matrices
- [ ] Add clinical evidence

**Task 6.2: Regulatory Package** (4h)
- [ ] Create CLINICAL_EVIDENCE_PACKAGE.md
- [ ] Add hematologist signatures
- [ ] Add validation protocol
- [ ] Add raw data references

**Deliverable:** RED_LIST_VALIDATION_REPORT.md + CLINICAL_EVIDENCE_PACKAGE.md

---

## 📊 SUCCESS METRICS

### PRIMARY METRIC (MANDATORY)

| Syndrome | Sensitivity | FN | Status |
|----------|-------------|----|----|
| S-NEUTROPENIA-GRAVE | **100%** | **0** | ✅ MANDATORY |
| S-BLASTIC-SYNDROME | **100%** | **0** | ✅ MANDATORY |
| S-TMA | **100%** | **0** | ✅ MANDATORY |
| S-PLT-CRITICA | **100%** | **0** | ✅ MANDATORY |
| S-ANEMIA-GRAVE | **100%** | **0** | ✅ MANDATORY |
| S-NEUTROFILIA-LEFTSHIFT-CRIT | **100%** | **0** | ✅ MANDATORY |
| S-THROMBOCITOSE-CRIT | **100%** | **0** | ✅ MANDATORY |
| S-CIVD | **100%** | **0** | ✅ MANDATORY |
| S-APL | **100%** | **0** | ✅ MANDATORY |

**GATE:** If FN > 0 for ANY critical syndrome → Additional tuning sprint (1 week)

### SECONDARY METRICS (TARGETS)

| Metric | Target | Validation |
|--------|--------|------------|
| **Specificity overall** | ≥80% | Acceptable FP rate |
| **Alert burden** | <20% | <54 alerts per 270 cases |
| **Abstention rate (C0)** | <10% | <27 abstentions |
| **Clinical approval** | 100% | All hematologists sign |

---

## 🎯 DELIVERABLES

### Data Files (3 files)
1. `data/red_list/critical_cases.json` (270 synthetic cases)
2. `data/red_list/real_cases.json` (optional, 30-50 real cases)
3. `results/red_list_metrics.json` (validation results)

### Test Files (1 file, ~270 tests)
4. `tests/clinical/test_red_list_validation.py` (270 parametrized tests)

### Documentation (3 files)
5. `RED_LIST_VALIDATION_REPORT.md` (main report, ~50 pages)
6. `CLINICAL_EVIDENCE_PACKAGE.md` (regulatory submission)
7. `SPRINT_4_COMPLETE_REPORT.md` (executive summary)

### Total: 7 deliverables

---

## 🔗 PARALLEL EXECUTION WITH SPRINT 3

### Independence
- ✅ Sprint 3 focuses on **audit & documentation**
- ✅ Sprint 4 focuses on **clinical validation**
- ✅ **No dependencies** between sprints (can run in parallel)

### File Organization (NO CONFLICTS)

**Sprint 3 files:**
- tests/audit/test_worm_audit.py
- tests/audit/test_routing_audit.py
- TRACEABILITY_MATRIX_COMPLETE.md
- REGULATORY_COMPLIANCE_CHECKLIST.md

**Sprint 4 files:**
- tests/clinical/test_red_list_validation.py
- data/red_list/critical_cases.json
- RED_LIST_VALIDATION_REPORT.md
- CLINICAL_EVIDENCE_PACKAGE.md

**No overlap!** ✅

---

## 🚀 QUICK START (NEW WINDOW)

```bash
# 1. Navigate to project
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# 2. Read context
cat SPRINT_4_PLAN_RED_LIST_VALIDATION.md

# 3. Create branch (optional)
git checkout -b sprint-4-red-list

# 4. Start Week 1 Day 1
mkdir -p data/red_list
mkdir -p tests/clinical
mkdir -p results

# 5. Use clinical-test-generator skill
# Generate critical cases

# 6. Start coding tests!
```

---

## 📝 CASE GENERATION TEMPLATE

```python
# Use clinical-test-generator skill

# Example: S-NEUTROPENIA-GRAVE
{
  "case_id": "RL-001-NEU-GRAVE",
  "syndrome_gold_standard": "S-NEUTROPENIA-GRAVE",
  "clinical_context": {
    "age_years": 45,
    "sex": "F",
    "history": "Chemotherapy Day +10"
  },
  "cbc": {
    "wbc": 0.8,
    "anc": 0.3,  # CRITICAL (<0.5)
    "hb": 9.2,
    "plt": 45,
    "neutrophils": 35.0,
    "lymphocytes": 50.0
  },
  "expected_evidences": ["E-ANC-CRIT", "E-NEUTROPENIA-SEVERE"],
  "expected_syndrome": "S-NEUTROPENIA-GRAVE",
  "expected_next_steps": ["G-CSF", "Hospitalization", "Blood cultures"],
  "criticality": "critical",
  "fn_allowed": false  # FN=0 MANDATORY
}
```

---

## 📝 VALIDATION TEST TEMPLATE

```python
# tests/clinical/test_red_list_validation.py
import pytest
import json
from hemodoctor.api.pipeline import analyze_cbc

# Load critical cases
with open('data/red_list/critical_cases.json') as f:
    CRITICAL_CASES = json.load(f)

@pytest.mark.parametrize("case", CRITICAL_CASES)
def test_red_list_fn_zero(case):
    """Test FN=0 for critical syndromes"""
    cbc = case["cbc"]
    expected = case["expected_syndrome"]

    # Run pipeline
    result = analyze_cbc(cbc)

    # MANDATORY: FN=0
    assert expected in result["top_syndromes"], \
        f"FN DETECTED! Expected {expected}, got {result['top_syndromes']}"

    # Critical syndrome must be first
    assert result["top_syndromes"][0] == expected, \
        f"Critical not prioritized: {result['top_syndromes']}"

def test_compute_metrics():
    """Compute sensitivity/specificity per syndrome"""
    results = []
    for case in CRITICAL_CASES:
        result = analyze_cbc(case["cbc"])
        results.append({
            "expected": case["expected_syndrome"],
            "predicted": result["top_syndromes"][0] if result["top_syndromes"] else None
        })

    # Compute per-syndrome metrics
    metrics = {}
    for syndrome in set(c["expected_syndrome"] for c in CRITICAL_CASES):
        tp = sum(1 for r in results if r["expected"] == syndrome and r["predicted"] == syndrome)
        fn = sum(1 for r in results if r["expected"] == syndrome and r["predicted"] != syndrome)

        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        metrics[syndrome] = {
            "sensitivity": sensitivity,
            "fn": fn,
            "tp": tp
        }

    # Assert FN=0 for all critical
    for syndrome, m in metrics.items():
        assert m["fn"] == 0, f"FN > 0 for {syndrome}: FN={m['fn']}"
        assert m["sensitivity"] == 1.0, f"Sensitivity < 100% for {syndrome}"
```

---

## 🎯 COORDINATION WITH SPRINT 3

### Timeline Alignment

```
Sprint 3 (5 days):  29 Oct - 2 Nov
Sprint 4 (2 weeks): 23 Nov - 6 Dec  (starts AFTER Sprint 3)

Note: Sprint 4 can start earlier if Sprint 3 finishes early!
```

### Merge Strategy

**Sequential Merge** (recommended):
```bash
# Sprint 3 finishes first (2 Nov)
git checkout main
git merge sprint-3-audit
git push

# Sprint 4 continues independently
# Merges later (6 Dec)
git checkout main
git pull  # Get Sprint 3 changes
git merge sprint-4-red-list
git push
```

---

## 📊 ESTIMATED TIMELINE

```
Week 1:
  Day 1-2: Generate 270 critical cases
  Day 3-4: Collect real cases (optional)
  Day 5:   Validation framework

Week 2:
  Day 6-7: Execute validation + metrics
  Day 8-9: Clinical review + tuning (if needed)
  Day 10:  Report generation

Total: 10 working days (2 weeks)
```

---

## ⚠️ RISK MITIGATION

### If FN > 0 Detected

**Protocol:**
1. **Immediate halt** - Do not proceed
2. **Root cause analysis** (2 hours)
   - Which evidence failed?
   - Which syndrome logic failed?
   - Data quality issue?
3. **Fix implementation** (4-8 hours)
   - Adjust thresholds
   - Fix evidence rules
   - Update syndrome logic
4. **Re-run validation** (2 hours)
5. **Verify FN=0** ✅

**Additional Sprint (if needed):**
- Duration: 1 week
- Objective: Tune system until FN=0
- Timeline impact: 30 Nov → 7 Dec

---

## ✅ READY TO START

**Prerequisites:**
- ✅ Sprint 2 complete (30 clinical syndromes validated)
- ✅ 9/9 critical syndromes functional
- ✅ clinical-test-generator skill available
- ✅ Pipeline latency <100ms (ready for batch)

**Next Action:**
1. Read this plan completely (20 min)
2. Wait for Sprint 3 to finish (2 Nov)
3. Start Week 1 Day 1: Case generation (23 Nov)
4. Execute validation protocol

---

**Status:** ⏳ READY TO START (after Sprint 3)
**Duration:** 2 weeks
**Parallel:** Partially (Week 1 can overlap with Sprint 3)
**Timeline:** 30 Nov 2025 - ON TRACK ✅

---

**Last Updated:** 22 Oct 2025 - 01:30 BRT
**Version:** v1.0
**Owner:** Sprint 4 Team (Red List Validation)
