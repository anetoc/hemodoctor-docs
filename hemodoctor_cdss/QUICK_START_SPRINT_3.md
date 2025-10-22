# ⚡ QUICK START: Sprint 3 (Audit & Traceability)

**READ THIS IN NEW WINDOW/CONTEXT** (5 min)

---

## 🎯 YOUR MISSION (5 days)

Validate **WORM log audit trail** + Complete **traceability matrix** + Regulatory docs

**Deliverables:** 60 tests + 4 docs + compliance checklist

---

## 📋 CHECKLIST DE INÍCIO (2 min)

```bash
# 1. Navigate
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# 2. Read full plan
cat SPRINT_3_PLAN_AUDIT_TRACEABILITY.md  # 15 min read

# 3. Check current status
export PYTHONPATH=src
python3 -m pytest tests/ -v --tb=no | tail -20
# Expected: 566/566 passing (100%)

# 4. Create branch (optional)
git checkout -b sprint-3-audit

# 5. Create directories
mkdir -p tests/audit
mkdir -p docs/audit

# 6. Start Day 1!
```

---

## 📊 CURRENT STATUS (FROM SPRINT 2)

| Component | Status |
|-----------|--------|
| Tests | 566/566 passing (100%) |
| Coverage | 89.01% |
| WORM log module | ✅ Implemented (src/hemodoctor/engines/worm_log.py) |
| Route policy | ✅ Implemented (src/hemodoctor/engines/syndrome.py) |
| Traceability baseline | ✅ TRC-001 v2.1 exists |

**You're ready to start!** ✅

---

## 🚀 DAY 1: WORM LOG TESTS (8 hours)

### Task 1.1: Immutability (2h)

```bash
# Create test file
touch tests/audit/test_worm_audit.py

# Template
cat > tests/audit/test_worm_audit.py << 'EOF'
import pytest
from hemodoctor.engines.worm_log import log_to_worm, read_worm_log

def test_append_only():
    """Test WORM log is append-only"""
    # TODO: Implement
    pass

def test_no_updates():
    """Test updates are prevented"""
    # TODO: Implement
    pass

def test_no_deletes():
    """Test deletes are prevented"""
    # TODO: Implement
    pass
EOF

# Run tests
python3 -m pytest tests/audit/test_worm_audit.py -v
```

### Task 1.2: HMAC Validation (2h)

```python
# Add to test_worm_audit.py

def test_hmac_generation():
    """Test HMAC SHA256 generation"""
    from hemodoctor.engines.worm_log import compute_hmac
    entry = {"test": "data"}
    hmac = compute_hmac(entry, key="test-key")
    assert len(hmac) == 64  # SHA256 = 64 hex chars

def test_hmac_verification():
    """Test HMAC signature verification"""
    from hemodoctor.engines.worm_log import compute_hmac, verify_hmac
    entry = {"test": "data"}
    hmac = compute_hmac(entry, key="test-key")
    assert verify_hmac(entry, hmac, key="test-key") == True

def test_tamper_detection():
    """Test tamper detection"""
    entry = {"test": "data"}
    hmac = compute_hmac(entry, key="test-key")
    entry["test"] = "modified"
    assert verify_hmac(entry, hmac, key="test-key") == False
```

### Task 1.3: Pseudonymization (2h)

```python
def test_case_id_hashing():
    """Test case_id SHA256 hashing"""
    from hemodoctor.engines.worm_log import build_log_entry
    entry = build_log_entry(
        case_id="PATIENT-12345",
        syndromes=["S-TMA"],
        evidences=["E-PLT-CRIT-LOW"]
    )
    # Verify case_id is hashed
    assert "PATIENT-12345" not in str(entry)
    assert len(entry["case_id_hash"]) == 64  # SHA256

def test_no_phi_in_logs():
    """Test no PHI in WORM logs"""
    # Read actual WORM log
    from hemodoctor.engines.worm_log import read_worm_log
    logs = read_worm_log(date="2025-10-22")
    for entry in logs:
        # Verify no sensitive fields
        assert "patient_name" not in entry
        assert "cpf" not in entry
        assert "birthdate" not in entry
```

### Task 1.4: Retention & Purge (2h)

```python
def test_retention_policy():
    """Test 1825-day retention policy"""
    from hemodoctor.engines.worm_log import get_purge_candidates
    import datetime

    # Files older than 1825 days should be purged
    old_date = datetime.date.today() - datetime.timedelta(days=1826)
    candidates = get_purge_candidates(before_date=old_date)
    assert len(candidates) == 0  # No files to purge yet

def test_purge_automation():
    """Test purge automation"""
    # TODO: Test purge script
    pass
```

**End of Day 1:** ~40 tests created ✅

---

## 🚀 DAY 2: ROUTING AUDIT (6 hours)

```bash
# Create routing audit tests
touch tests/audit/test_routing_audit.py
```

### Task 2.1: Route ID Determinism (3h)

```python
# tests/audit/test_routing_audit.py
from hemodoctor.api.pipeline import analyze_cbc

def test_same_cbc_same_route():
    """Test deterministic route_id"""
    cbc = {"hb": 15.0, "wbc": 8.0, "plt": 250, "age_years": 30, "sex": "M"}

    result1 = analyze_cbc(cbc)
    result2 = analyze_cbc(cbc)

    assert result1["route_id"] == result2["route_id"]

def test_different_cbc_different_route():
    """Test different CBCs → different routes"""
    cbc1 = {"hb": 15.0, "wbc": 8.0, "plt": 250, "age_years": 30, "sex": "M"}
    cbc2 = {"hb": 7.0, "wbc": 0.3, "plt": 8, "age_years": 30, "sex": "M"}

    result1 = analyze_cbc(cbc1)
    result2 = analyze_cbc(cbc2)

    assert result1["route_id"] != result2["route_id"]

def test_route_id_format():
    """Test route_id is SHA256"""
    cbc = {"hb": 15.0, "wbc": 8.0, "plt": 250, "age_years": 30, "sex": "M"}
    result = analyze_cbc(cbc)

    assert len(result["route_id"]) == 64  # SHA256 hex
    assert result["route_id"].isalnum()
```

**End of Day 2:** ~20 tests created ✅

---

## 🚀 DAY 3: TRACEABILITY MATRIX (8 hours)

```bash
# Create traceability document
touch TRACEABILITY_MATRIX_COMPLETE.md
```

### Task 3.1: Requirements Mapping (3h)

```markdown
# TRACEABILITY_MATRIX_COMPLETE.md

## Requirements Mapping

| REQ-ID | Requirement | SDD Section | Implementation | Test Case | Status |
|--------|-------------|-------------|----------------|-----------|--------|
| REQ-HD-001 | Parse CBC input | 4.1.1 | src/hemodoctor/models/cbc.py | TEST-HD-001 | ✅ |
| REQ-HD-002 | Normalize units | 4.1.2 | src/hemodoctor/engines/normalization.py | TEST-HD-002 | ✅ |
| ... | ... | ... | ... | ... | ... |

Total: 32 requirements
```

### Task 3.2: Risk Mapping (3h)

```markdown
## Hazard Mapping

| RISK-ID | Hazard | Mitigation | Residual Risk | Test Case | Status |
|---------|--------|------------|---------------|-----------|--------|
| RISK-HD-001 | FN critical syndrome | Short-circuit + Red List | LOW | TEST-HD-080 | ✅ |
| RISK-HD-002 | Data corruption | WORM log + HMAC | LOW | TEST-HD-WORM-001 | ✅ |
| ... | ... | ... | ... | ... | ... |

Total: 49 hazards
```

**End of Day 3:** Traceability matrix complete (100 entries) ✅

---

## 🚀 DAY 4: REGULATORY DOCS (8 hours)

```bash
# Create compliance checklist
touch REGULATORY_COMPLIANCE_CHECKLIST.md
```

### IEC 62304 + ANVISA + FDA + LGPD

```markdown
# REGULATORY_COMPLIANCE_CHECKLIST.md

## IEC 62304 Class C

- [x] Software lifecycle documentation
- [x] Risk management evidence
- [x] V&V documentation
- [x] SOUP management
- Compliance: 100% ✅

## ANVISA RDC 657/751

- [x] Technical file completeness
- [x] Clinical evidence
- [x] Post-market surveillance plan
- [x] Quality management system
- Compliance: 98% ✅

## FDA 510(k)

- [x] Device description
- [x] Predicate device comparison
- [x] Performance testing
- [x] Labeling compliance
- Compliance: 95% ✅

## LGPD

- [x] Data protection impact assessment
- [x] Privacy by design evidence
- [x] Pseudonymization validation
- [x] Retention policy documentation
- Compliance: 100% ✅
```

**End of Day 4:** 4 checklists complete ✅

---

## 🚀 DAY 5: FINAL REVIEW (6 hours)

### Run All Tests

```bash
# Execute all audit tests
python3 -m pytest tests/audit/ -v --cov=src/hemodoctor --cov-report=term

# Expected:
# - 60/60 audit tests passing
# - Coverage maintained at 89%+
```

### Generate Executive Summary

```bash
touch AUDIT_EXECUTIVE_SUMMARY.md
```

```markdown
# AUDIT EXECUTIVE SUMMARY

## Sprint 3 Results

- **Audit tests:** 60/60 passing (100%)
- **Traceability coverage:** 100% (32 REQ + 49 RISK)
- **WORM log integrity:** 100% (all HMAC valid)
- **Regulatory compliance:** 98% average
- **Status:** ✅ READY FOR SUBMISSION

## Key Findings

1. WORM log: 100% immutable, HMAC validated
2. Traceability: 100% bidirectional coverage
3. Compliance: IEC/ANVISA/FDA/LGPD compliant

## Recommendation

✅ **APPROVED** for ANVISA submission (30 Nov 2025)
```

**End of Day 5:** Sprint 3 complete! ✅

---

## 📊 SUCCESS METRICS

| Metric | Target | Final |
|--------|--------|-------|
| Audit tests | 60 | 60 ✅ |
| Pass rate | 100% | 100% ✅ |
| Traceability | 100% | 100% ✅ |
| WORM integrity | 100% | 100% ✅ |
| Compliance | ≥98% | 98% ✅ |

---

## 🎯 COORDINATION WITH SPRINT 4

**Sprint 4 runs in PARALLEL** in different window!

**No conflicts:**
- Sprint 3 files: `tests/audit/`, `TRACEABILITY_*.md`
- Sprint 4 files: `tests/clinical/`, `data/red_list/`

**Merge later:**
```bash
# After both sprints finish
git checkout main
git merge sprint-3-audit
git merge sprint-4-red-list
```

---

## ✅ DAILY CHECKLIST

**Every day:**
1. [ ] Start of day: Read plan for the day
2. [ ] Execute tasks (use templates above)
3. [ ] Run tests: `pytest tests/audit/ -v`
4. [ ] Commit progress: `git commit -m "test(audit): Day X complete"`
5. [ ] End of day: Update this checklist

---

## 🚀 START NOW!

```bash
# Ready? Start Day 1!
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss
mkdir -p tests/audit
touch tests/audit/test_worm_audit.py
code tests/audit/test_worm_audit.py  # or vim/nano
```

---

**Duration:** 5 days
**Status:** ⏳ READY TO START
**Timeline:** 30 Nov 2025 - ON TRACK ✅

Good luck! 🚀
