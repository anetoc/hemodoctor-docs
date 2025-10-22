# SPRINT 3: Audit & Traceability

**Duration:** 5 days (29 Oct - 2 Nov 2025)
**Objective:** Complete WORM audit validation + traceability matrix + regulatory compliance
**Parallel:** Can run in parallel with Sprint 4 (Red List validation)
**Status:** ⏳ READY TO START

---

## 🎯 OBJECTIVES

1. **WORM Log Audit Trail Validation** (Day 1-2)
   - Verify immutability (append-only)
   - Validate HMAC signatures (integrity)
   - Test pseudonymization (privacy)
   - Verify retention policy (1825 days)
   - Test purge automation

2. **Traceability Matrix Completion** (Day 3)
   - Complete REQ → RISK → TEST mapping
   - Verify 100% bidirectional traceability
   - Validate regulatory coverage (IEC/ANVISA/FDA)
   - Generate traceability reports

3. **Regulatory Documentation** (Day 4)
   - Update compliance checklists
   - Create audit trail report
   - Generate regulatory evidence package
   - Prepare submission artifacts

4. **Final Review** (Day 5)
   - Cross-check all deliverables
   - Validate compliance status
   - Create executive summary
   - Ready for Sprint 4 integration

---

## 📋 TASKS BREAKDOWN

### Day 1: WORM Log Testing (8 hours)

**Task 1.1: Immutability Tests** (2h)
- [ ] Test append-only writes (no updates/deletes)
- [ ] Verify file permissions (read-only after write)
- [ ] Test concurrent writes (thread safety)
- [ ] Validate daily rotation (YYYY-MM-DD format)

**Task 1.2: HMAC Validation** (2h)
- [ ] Test HMAC generation (SHA256)
- [ ] Verify signature integrity
- [ ] Test key rotation
- [ ] Validate tamper detection

**Task 1.3: Pseudonymization** (2h)
- [ ] Test case_id hashing (SHA256)
- [ ] Verify no PHI in logs
- [ ] Test site_id pseudonymization
- [ ] Validate LGPD compliance

**Task 1.4: Retention & Purge** (2h)
- [ ] Test 1825-day retention policy
- [ ] Verify purge automation
- [ ] Test log archival
- [ ] Validate backup integrity

**Deliverable:** `test_worm_audit.py` (~40 tests)

---

### Day 2: Route ID & Determinism (6 hours)

**Task 2.1: Route ID Testing** (3h)
- [ ] Test SHA256 generation (deterministic)
- [ ] Verify same CBC → same route_id
- [ ] Test different CBC → different route_id
- [ ] Validate reproducibility

**Task 2.2: Alternative Routes** (3h)
- [ ] Test alt_routes computation
- [ ] Verify conflict detection
- [ ] Test tie-breaking logic
- [ ] Validate clinical rationale

**Deliverable:** `test_routing_audit.py` (~20 tests)

---

### Day 3: Traceability Matrix (8 hours)

**Task 3.1: Requirements Mapping** (3h)
- [ ] Map all 32 requirements (REQ-HD-001 to 032)
- [ ] Link to design artifacts (SDD sections)
- [ ] Verify implementation (code modules)
- [ ] Map to test cases (TEST-HD-XXX)

**Task 3.2: Risk Mapping** (3h)
- [ ] Map all 49 hazards (RISK-HD-001 to 049)
- [ ] Link to mitigation controls
- [ ] Verify residual risk levels
- [ ] Map to validation tests

**Task 3.3: Bidirectional Verification** (2h)
- [ ] Verify REQ → RISK → TEST forward links
- [ ] Verify TEST → RISK → REQ backward links
- [ ] Identify orphaned items
- [ ] Complete missing links

**Deliverable:** `TRACEABILITY_MATRIX_COMPLETE.md` (~100 entries)

---

### Day 4: Regulatory Documentation (8 hours)

**Task 4.1: IEC 62304 Compliance** (2h)
- [ ] Software lifecycle documentation
- [ ] Risk management evidence
- [ ] V&V documentation
- [ ] SOUP management

**Task 4.2: ANVISA RDC 657/751** (2h)
- [ ] Technical file completeness
- [ ] Clinical evidence
- [ ] Post-market surveillance plan
- [ ] Quality management system

**Task 4.3: FDA 510(k)** (2h)
- [ ] Device description
- [ ] Predicate device comparison
- [ ] Performance testing
- [ ] Labeling compliance

**Task 4.4: LGPD Compliance** (2h)
- [ ] Data protection impact assessment
- [ ] Privacy by design evidence
- [ ] Pseudonymization validation
- [ ] Retention policy documentation

**Deliverable:** `REGULATORY_COMPLIANCE_CHECKLIST.md`

---

### Day 5: Final Review & Integration (6 hours)

**Task 5.1: Test Execution** (2h)
- [ ] Run all audit tests (60 total)
- [ ] Verify 100% pass rate
- [ ] Check coverage maintenance (≥89%)
- [ ] Generate test report

**Task 5.2: Document Review** (2h)
- [ ] Review traceability matrix
- [ ] Review compliance checklist
- [ ] Review audit reports
- [ ] Verify completeness

**Task 5.3: Executive Summary** (2h)
- [ ] Create AUDIT_EXECUTIVE_SUMMARY.md
- [ ] Highlight key findings
- [ ] Document compliance status
- [ ] Prepare for submission

**Deliverable:** `SPRINT_3_COMPLETE_REPORT.md`

---

## 📊 SUCCESS METRICS

| Metric | Target | Validation |
|--------|--------|------------|
| **Audit tests** | 60 | 100% passing |
| **Traceability coverage** | 100% | All REQ/RISK/TEST linked |
| **WORM log integrity** | 100% | All HMAC valid |
| **Regulatory compliance** | ≥98% | IEC/ANVISA/FDA/LGPD |
| **Documentation** | Complete | All deliverables ready |

---

## 🎯 DELIVERABLES

### Test Files (2 files, ~60 tests)
1. `tests/audit/test_worm_audit.py` (40 tests)
2. `tests/audit/test_routing_audit.py` (20 tests)

### Documentation (4 files)
3. `TRACEABILITY_MATRIX_COMPLETE.md` (~100 entries)
4. `REGULATORY_COMPLIANCE_CHECKLIST.md` (compliance status)
5. `AUDIT_TRAIL_VALIDATION_REPORT.md` (WORM log evidence)
6. `AUDIT_EXECUTIVE_SUMMARY.md` (executive summary)

### Total: 6 deliverables

---

## 🔗 PARALLEL EXECUTION WITH SPRINT 4

### Independence
- ✅ Sprint 3 focuses on **audit & documentation**
- ✅ Sprint 4 focuses on **clinical validation**
- ✅ **No dependencies** between sprints (can run in parallel)

### Coordination Points

**Before Starting:**
- Both sprints use same codebase (hemodoctor_cdss/)
- Avoid modifying same files simultaneously
- Sprint 3: tests/audit/, docs/
- Sprint 4: tests/clinical/, data/red_list/

**During Execution:**
- Independent commits (no merge conflicts)
- Sprint 3 commits: `test(audit): ...` or `docs(audit): ...`
- Sprint 4 commits: `test(clinical): ...` or `data(red_list): ...`

**After Completion:**
- Merge both branches to main
- Combine final reports
- Total tests: 566 (current) + 60 (Sprint 3) + 240 (Sprint 4) = 866 tests!

---

## 🚀 QUICK START (NEW WINDOW)

```bash
# 1. Navigate to project
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# 2. Read context
cat SPRINT_3_PLAN_AUDIT_TRACEABILITY.md

# 3. Create branch (optional)
git checkout -b sprint-3-audit

# 4. Start Day 1
export PYTHONPATH=src
mkdir -p tests/audit
touch tests/audit/test_worm_audit.py

# 5. See WORM log module
cat config/08_wormlog_hybrid.yaml
cat src/hemodoctor/engines/worm_log.py

# 6. Start coding tests!
```

---

## 📝 TESTING TEMPLATE

```python
# tests/audit/test_worm_audit.py
import pytest
from hemodoctor.engines.worm_log import build_log_entry, compute_hmac, verify_hmac

def test_worm_immutability():
    """Test append-only WORM log"""
    # Test logic here
    pass

def test_hmac_integrity():
    """Test HMAC signature validation"""
    entry = build_log_entry(...)
    hmac = compute_hmac(entry, key="test-key")
    assert verify_hmac(entry, hmac, key="test-key") == True

def test_pseudonymization():
    """Test case_id SHA256 hashing"""
    # Verify no PHI in logs
    pass
```

---

## 🎯 COORDINATION WITH SPRINT 4

### Merge Strategy

**Option A: Sequential Merge** (safer)
```bash
# Sprint 3 finishes first
git checkout main
git merge sprint-3-audit
git push

# Sprint 4 finishes later
git checkout main
git pull
git merge sprint-4-red-list
git push
```

**Option B: Parallel Merge** (faster, if no conflicts)
```bash
# Create integration branch
git checkout -b integration-sprint-3-4
git merge sprint-3-audit
git merge sprint-4-red-list
# Resolve conflicts if any
git push
```

---

## 📊 ESTIMATED TIMELINE

```
Day 1 (29 Oct): WORM log tests (40 tests)
Day 2 (30 Oct): Routing audit (20 tests)
Day 3 (31 Oct): Traceability matrix (100 entries)
Day 4 (1 Nov):  Regulatory docs (4 checklists)
Day 5 (2 Nov):  Final review + executive summary

Total: 5 days (SHORT SPRINT)
```

---

## ✅ READY TO START

**Prerequisites:**
- ✅ Sprint 2 complete (566 tests, 89% coverage)
- ✅ WORM log module implemented (src/hemodoctor/engines/worm_log.py)
- ✅ Route policy implemented (src/hemodoctor/engines/syndrome.py)
- ✅ Traceability baseline (TRC-001 v2.1 exists)

**Next Action:**
1. Read this plan completely (15 min)
2. Open new terminal window
3. Execute Quick Start commands
4. Start Day 1: WORM log testing

---

**Status:** ⏳ READY TO START
**Duration:** 5 days
**Parallel:** Yes (with Sprint 4)
**Timeline:** 30 Nov 2025 - ON TRACK ✅

---

**Last Updated:** 22 Oct 2025 - 01:15 BRT
**Version:** v1.0
**Owner:** Sprint 3 Team (Audit & Traceability)
