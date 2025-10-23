# HemoDoctor CSV Testing - Quick Start Guide

**Version:** 1.0.0
**Date:** 2025-10-23
**Time to Complete:** 5 minutes

---

## What This Guide Does

This quick start gets you testing HemoDoctor CDSS with CSV files in **under 5 minutes**. Perfect for:
- First-time users
- Quick validation
- Demo/POC scenarios
- Learning the workflow

---

## Prerequisites (1 minute)

**Required:**
- HemoDoctor CDSS installed
- Python 3.10+
- Terminal access

**Optional (recommended):**
```bash
pip install pandas  # 2x faster CSV processing
```

---

## Quick Start (4 minutes)

### Step 1: Start API Server (1 min)

Open **Terminal 1**:

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss
export PYTHONPATH=src
uvicorn hemodoctor.api.main:app --reload
```

Wait for:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**✅ Checkpoint:** API is running

---

### Step 2: Run Example Test (2 min)

Open **Terminal 2**:

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# Run test with example CSV (20 cases)
python3 scripts/test_csv.py --input data/example_test_cases.csv
```

**Expected output:**
```
================================================================================
HemoDoctor CSV Testing Script v1.0
================================================================================

Loading test cases from: data/example_test_cases.csv
Found 20 cases to test

Testing API at: http://localhost:8000/analyze
✅ API health check: OK
   Version: 2.4.0

Processing cases:
  1/20 CASE-001: ✅ PASS (Exact match: S-NORMAL)
  2/20 CASE-002: ✅ PASS (Exact match: S-NORMAL)
  3/20 CASE-003: ✅ PASS (Exact match: S-ANEMIA-GRAVE)
  ...
  20/20 CASE-020: ✅ PASS (Exact match: S-CIVD)

RESULTS
  Total:   20
  Passed:  20 (100.0%)

METRICS
  True Positives:  22
  False Positives: 0
  False Negatives: 0
  Sensitivity:     100.0%
  Precision:       100.0%

✅ Testing complete!
  Results: results.csv
  Report:  test_report.txt
```

**✅ Checkpoint:** All 20 tests passed

---

### Step 3: Review Results (1 min)

**Check results CSV:**

```bash
cat results.csv | head -5
```

**Check test report:**

```bash
cat test_report.txt
```

**✅ Checkpoint:** Results saved successfully

---

## What You Just Did

1. ✅ Started HemoDoctor API server
2. ✅ Ran 20 CBC test cases via CSV
3. ✅ Validated syndrome detection (100% pass rate)
4. ✅ Generated test report + results CSV

**Total time:** ~4 minutes

---

## Next Steps

### Option A: Test Your Own Cases

Create `my_test_cases.csv`:

```csv
case_id,hb,mcv,wbc,plt,anc,age_years,sex,expected_syndrome,notes
MY-001,15.2,88,8.5,250,4.0,35,M,S-NORMAL,My first test case
MY-002,5.8,65,12.0,180,8.0,8,M,S-ANEMIA-GRAVE,My second test case
```

Run test:

```bash
python3 scripts/test_csv.py --input my_test_cases.csv
```

### Option B: Explore Advanced Features

**Verbose mode:**
```bash
python3 scripts/test_csv.py --input data/example_test_cases.csv --verbose
```

**Custom output:**
```bash
python3 scripts/test_csv.py \
  --input data/example_test_cases.csv \
  --output my_results.csv \
  --report my_report.txt
```

**Custom API URL:**
```bash
python3 scripts/test_csv.py \
  --input data/example_test_cases.csv \
  --api http://production-server:8000
```

### Option C: Read Full Documentation

**Detailed guides:**
- **CSV Format:** `docs/CSV_FORMAT_SPEC.md` (complete field reference)
- **Testing Workflow:** `docs/TESTING_WORKFLOW_CSV.md` (advanced usage)
- **API Docs:** http://localhost:8000/docs (interactive OpenAPI)

---

## Common Issues

### Issue: "API health check failed"

**Solution:** Start API server in Terminal 1

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss
export PYTHONPATH=src
uvicorn hemodoctor.api.main:app --reload
```

### Issue: "No module named 'hemodoctor'"

**Solution:** Set PYTHONPATH

```bash
export PYTHONPATH=src
```

### Issue: "File not found: data/example_test_cases.csv"

**Solution:** Make sure you're in the right directory

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss
ls data/example_test_cases.csv  # Should exist
```

---

## Help

**Get help:**

```bash
python3 scripts/test_csv.py --help
```

**Check API:**

```bash
curl http://localhost:8000/health
```

**Read docs:**

```bash
open http://localhost:8000/docs  # Interactive API docs
```

---

## Summary

**What you learned:**
1. How to start HemoDoctor API server
2. How to test CBC cases via CSV
3. How to interpret test results
4. Where to find detailed documentation

**Files created:**
- `results.csv` - Detailed test results
- `test_report.txt` - Summary report

**Time invested:** 5 minutes

**Next:** Create your own test cases or read full documentation!

---

**End of Quick Start Guide**
