# HemoDoctor CSV Testing Workflow

**Version:** 1.0.0
**Date:** 2025-10-23
**Author:** Dr. Abel Costa
**Purpose:** Complete guide for testing HemoDoctor CDSS using CSV files

---

## Overview

This guide covers the complete workflow for testing HemoDoctor CDSS using CSV input files. Whether you're validating clinical rules, regression testing, or preparing Red List FN=0 validation, this workflow provides a systematic approach.

---

## Prerequisites

### 1. HemoDoctor Installation

Ensure HemoDoctor CDSS is installed and configured:

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# Check Python version (3.10+)
python3 --version

# Install dependencies
pip install -r requirements.txt

# Optional: Install pandas for faster CSV processing
pip install pandas
```

### 2. Verify Installation

```bash
# Set PYTHONPATH
export PYTHONPATH=src

# Run quick tests
python3 -m pytest tests/core/test_pipeline.py -v

# Check YAML configs
ls -lh config/*.yaml
```

Expected output:
```
✅ 16 YAML files loaded
✅ All tests passing
```

---

## Workflow Steps

### Step 1: Start API Server

**Terminal 1 - Start server:**

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# Set PYTHONPATH
export PYTHONPATH=src

# Start server (development mode with auto-reload)
uvicorn hemodoctor.api.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345]
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Verify server is running:**

```bash
# Terminal 2
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "version": "2.4.0",
  "timestamp": "2025-10-23T12:00:00.000Z",
  "yamls_loaded": 16
}
```

### Step 2: Prepare Test CSV

**Option A: Use Example CSV Template**

Download/create `test_cases.csv`:

```csv
case_id,hb,mcv,wbc,plt,anc,age_years,sex,expected_syndrome,notes
CASE-001,15.2,88,8.5,250,4.0,35,M,S-NORMAL,Normal healthy adult
CASE-002,5.8,65,12.0,180,8.0,8,M,S-ANEMIA-GRAVE,Severe anemia pediatric
CASE-003,14.0,110,4.2,8,0.3,42,F,S-PLT-CRITICA+S-NEUTROPENIA-GRAVE,Multiple critical
```

**Option B: Use Pre-made Test Sets**

```bash
# Copy example test sets to your working directory
cp data/example_test_cases.csv test_cases.csv

# Or create from scratch using template
cp docs/CSV_FORMAT_SPEC.md test_cases_template.csv
# Edit in your favorite editor
```

**Option C: Generate Synthetic Cases**

```bash
# Use clinical-test-generator skill (if available)
# Or create manually based on CSV_FORMAT_SPEC.md
```

**Validation Checklist:**
- [ ] CSV has header row
- [ ] Required fields present: `hb`, `mcv`, `wbc`
- [ ] `case_id` unique for each row
- [ ] `expected_syndrome` specified (for validation)
- [ ] Numeric fields use `.` decimal separator
- [ ] Boolean fields use `True`/`False` or empty

### Step 3: Run Test Script

**Basic usage:**

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# Run tests
python3 scripts/test_csv.py --input test_cases.csv
```

**Expected output:**

```
================================================================================
HemoDoctor CSV Testing Script v1.0
================================================================================

Loading test cases from: test_cases.csv
Found 3 cases to test

Testing API at: http://localhost:8000/analyze
✅ API health check: OK
   Version: 2.4.0
   YAMLs loaded: 16

Processing cases:
  1/3 CASE-001: ✅ PASS (Exact match: S-NORMAL)
  2/3 CASE-002: ✅ PASS (Exact match: S-ANEMIA-GRAVE)
  3/3 CASE-003: ✅ PASS (Exact match: S-PLT-CRITICA, S-NEUTROPENIA-GRAVE)

RESULTS
  Total:   3
  Passed:  3 (100.0%)

METRICS
  True Positives:  4
  False Positives: 0
  False Negatives: 0
  Sensitivity:     100.0%
  Precision:       100.0%

PERFORMANCE
  Total time:      1.2s
  Avg per case:    0.40s

Saving results...

✅ Testing complete!
  Results: results.csv
  Report:  test_report.txt
```

### Step 4: Review Results

**4.1 Check Results CSV**

```bash
cat results.csv
```

Example output:
```csv
case_id,status,message,expected_syndrome,detected_syndromes,evidences_count,next_steps_count,route_id,timestamp,notes
CASE-001,PASS,Exact match: S-NORMAL,S-NORMAL,S-NORMAL,0,0,sha256:abc123...,2025-10-23T12:00:00Z,Normal healthy adult
CASE-002,PASS,Exact match: S-ANEMIA-GRAVE,S-ANEMIA-GRAVE,S-ANEMIA-GRAVE,3,5,sha256:def456...,2025-10-23T12:00:01Z,Severe anemia pediatric
CASE-003,PASS,Exact match: S-PLT-CRITICA S-NEUTROPENIA-GRAVE,S-PLT-CRITICA+S-NEUTROPENIA-GRAVE,S-PLT-CRITICA,S-NEUTROPENIA-GRAVE,5,8,sha256:ghi789...,2025-10-23T12:00:02Z,Multiple critical
```

**4.2 Check Test Report**

```bash
cat test_report.txt
```

Example output:
```
================================================================================
HemoDoctor CSV Testing Report
================================================================================

Generated: 2025-10-23 12:00:00
Total Cases: 3

SUMMARY
--------------------------------------------------------------------------------
  Passed:  3 (100.0%)
  Failed:  0
  Partial: 0
  Skipped: 0
  Errors:  0

METRICS
--------------------------------------------------------------------------------
  True Positives:  4
  False Positives: 0
  False Negatives: 0
  Sensitivity:     100.0%
  Precision:       100.0%

================================================================================
End of Report
```

**4.3 Analyze Failures (if any)**

If you see failures:

```bash
# View only failed cases
cat results.csv | grep "FAIL"

# Or use verbose mode to debug
python3 scripts/test_csv.py --input test_cases.csv --verbose
```

### Step 5: Debug Failures

**Common failure scenarios:**

**5.1 False Negative (Expected syndrome not detected)**

```
CASE-010: ❌ FAIL (Expected: S-ANEMIA-GRAVE, Got: S-NORMAL)
```

**Debug steps:**
1. Check if CBC values actually meet syndrome criteria
2. Verify YAML rule conditions (`config/04_syndromes_hybrid.yaml`)
3. Test case manually via API:
   ```bash
   curl -X POST http://localhost:8000/analyze \
     -H "Content-Type: application/json" \
     -d '{"hb": 5.8, "mcv": 65, "wbc": 12.0, "plt": 180}'
   ```
4. Check evidences detected: `evidences_present` field
5. Review syndrome logic: Does it require missing fields?

**5.2 False Positive (Unexpected syndrome detected)**

```
CASE-020: ❌ FAIL (Expected: S-NORMAL, Got: S-ANEMIA-MILD, S-NORMAL)
```

**Debug steps:**
1. Review extra syndromes in `detected_syndromes` column
2. Check if values are borderline (near cutoffs)
3. Verify age/sex-specific rules (some syndromes have age gates)
4. Review precedence rules (Critical > Priority > Routine)

**5.3 Partial Match**

```
CASE-030: ⚠️ PARTIAL (Partial match: S-PLT-CRITICA (missing: S-ANEMIA-GRAVE))
```

**Debug steps:**
1. Check if all expected syndromes should trigger
2. Verify co-occurrence rules (some syndromes block others)
3. Review missing syndrome conditions
4. Check if implementation matches specification

**5.4 API Errors**

```
CASE-040: 💥 ERROR (API request failed)
```

**Debug steps:**
1. Check API logs (Terminal 1)
2. Verify CSV data validity (ranges, types)
3. Test individual fields:
   ```bash
   curl -X POST http://localhost:8000/analyze \
     -H "Content-Type: application/json" \
     -d '{"hb": INVALID_VALUE, ...}'
   ```
4. Review API error response (use `--verbose`)

---

## Advanced Usage

### Verbose Mode

Get detailed debugging information:

```bash
python3 scripts/test_csv.py --input test_cases.csv --verbose
```

Additional output:
- CSV loading method (pandas vs csv)
- API health check details
- Individual case conversion details
- API request/response details for errors

### Custom Output Files

```bash
python3 scripts/test_csv.py \
  --input test_cases.csv \
  --output my_results.csv \
  --report my_report.txt
```

### Custom API URL

Test against production or staging:

```bash
python3 scripts/test_csv.py \
  --input test_cases.csv \
  --api http://production-server:8000
```

### Large Test Sets

For 100+ cases, use pandas (faster):

```bash
# Install pandas if not already
pip install pandas

# Run test (automatically uses pandas)
python3 scripts/test_csv.py --input large_test_set.csv
```

Expected performance:
- **10 cases:** ~3 seconds
- **100 cases:** ~30 seconds
- **1000 cases:** ~5 minutes

### Red List FN=0 Validation

For critical syndrome validation (FN must be exactly 0):

```bash
# Run Red List test set (240 cases, 8 syndromes × 30)
python3 scripts/test_csv.py --input red_list_240_cases.csv

# Check results
cat test_report.txt | grep "False Negatives"

# MUST show: False Negatives: 0
```

If FN > 0:
1. Identify failed cases: `cat results.csv | grep "FAIL"`
2. Debug each failure individually
3. Fix YAML rules or evidence detection
4. Re-run until FN = 0

---

## Integration with CI/CD

### GitHub Actions Example

```yaml
name: HemoDoctor CSV Tests

on: [push, pull_request]

jobs:
  csv-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pandas

      - name: Start API server
        run: |
          export PYTHONPATH=src
          uvicorn hemodoctor.api.main:app &
          sleep 5

      - name: Run CSV tests
        run: |
          python3 scripts/test_csv.py --input tests/data/test_cases.csv

      - name: Check pass rate
        run: |
          PASS_RATE=$(cat test_report.txt | grep "Passed:" | awk '{print $3}' | tr -d '()%')
          if (( $(echo "$PASS_RATE < 90" | bc -l) )); then
            echo "FAIL: Pass rate $PASS_RATE% < 90%"
            exit 1
          fi
```

### Pre-commit Hook Example

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Run quick smoke test before commit
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss
export PYTHONPATH=src

# Start API in background
uvicorn hemodoctor.api.main:app &
API_PID=$!
sleep 3

# Run tests
python3 scripts/test_csv.py --input tests/data/smoke_tests.csv

# Capture exit code
TEST_EXIT=$?

# Kill API
kill $API_PID

# Exit with test result
exit $TEST_EXIT
```

---

## Troubleshooting

### Issue 1: "API health check failed"

**Symptoms:**
```
❌ API health check failed: Connection refused
   Make sure API is running at: http://localhost:8000
```

**Solutions:**
1. Start API server: `uvicorn hemodoctor.api.main:app --reload`
2. Check port 8000 not in use: `lsof -i :8000`
3. Verify PYTHONPATH: `export PYTHONPATH=src`
4. Check firewall settings

### Issue 2: "No module named 'hemodoctor'"

**Symptoms:**
```
ModuleNotFoundError: No module named 'hemodoctor'
```

**Solutions:**
1. Set PYTHONPATH: `export PYTHONPATH=src`
2. Verify directory structure: `ls src/hemodoctor/`
3. Install in development mode: `pip install -e .`

### Issue 3: "Invalid input data: hb value exceeds max"

**Symptoms:**
```
API error for case CASE-001: 422 Unprocessable Entity
  Response: {"detail": "Invalid input data: hb value 30.0 exceeds max 25.0"}
```

**Solutions:**
1. Review CSV data validity (see CSV_FORMAT_SPEC.md ranges)
2. Check for typos (e.g., `30.0` vs `3.0`)
3. Use lenient mode (future feature) to skip invalid rows

### Issue 4: "Slow performance (>1s per case)"

**Symptoms:**
```
Total time:      125.0s
Avg per case:    1.25s
```

**Solutions:**
1. Install pandas: `pip install pandas` (10x faster CSV parsing)
2. Check API server performance (should be <100ms per case)
3. Use local API (avoid network latency)
4. Consider batch endpoint (future feature)

### Issue 5: "Permission denied: test_csv.py"

**Symptoms:**
```
zsh: permission denied: ./scripts/test_csv.py
```

**Solutions:**
1. Make executable: `chmod +x scripts/test_csv.py`
2. Or use: `python3 scripts/test_csv.py` (no need for executable bit)

---

## Best Practices

### 1. Test Case Design

**Good practices:**
- Use descriptive `case_id` (e.g., `RL-NEUT-001` for Red List neutropenia)
- Add `notes` column for documentation
- Group similar cases together (e.g., all S-ANEMIA-GRAVE cases)
- Include edge cases (boundaries, missing data, pre-analytical errors)
- Test co-occurring syndromes (multiple critical)

**Example:**
```csv
case_id,hb,mcv,wbc,plt,anc,expected_syndrome,notes
# Normal cases
NORM-001,15.2,88,8.5,250,4.0,S-NORMAL,Healthy adult male
NORM-002,13.5,88,7.5,220,3.8,S-NORMAL,Healthy adult female

# Severe anemia (pediatric)
ANEM-PED-001,5.8,65,12.0,180,8.0,S-ANEMIA-GRAVE,Age 8 - critical Hb
ANEM-PED-002,4.5,70,10.5,200,7.5,S-ANEMIA-GRAVE,Age 5 - very severe

# Edge cases
EDGE-001,4.9,88,8.5,250,4.0,S-ANEMIA-GRAVE,Borderline critical (Hb = 4.9)
EDGE-002,5.0,88,8.5,250,4.0,S-ANEMIA-SEVERE,Just above critical (Hb = 5.0)
```

### 2. Incremental Testing

**Strategy:**
1. Start with **10 smoke tests** (basic cases)
2. Expand to **30 representative cases** (all syndrome categories)
3. Add **100 validation cases** (comprehensive coverage)
4. Include **240 Red List cases** (FN=0 validation)
5. Optionally add **1000+ regression tests** (full dataset)

### 3. Version Control

**Track test evolution:**

```bash
# Commit test cases with descriptive messages
git add test_cases_v1.0.csv
git commit -m "test: Add 30 representative test cases for Sprint 2"

# Tag releases
git tag -a test-baseline-v1.0 -m "Baseline test set (30 cases, 100% pass)"
git push origin test-baseline-v1.0
```

### 4. Regression Testing

**Before major changes:**

```bash
# Run full test suite
python3 scripts/test_csv.py --input regression_1000_cases.csv

# Save baseline results
cp results.csv results_baseline.csv
cp test_report.txt test_report_baseline.txt

# After changes, compare
python3 scripts/test_csv.py --input regression_1000_cases.csv
diff results_baseline.csv results.csv
```

### 5. Documentation

**Document test rationale:**

```csv
case_id,hb,mcv,wbc,plt,notes
DOC-001,5.8,65,12.0,180,Tests E-HB-CRIT trigger (Hb < 6.0 pediatric)
DOC-002,14.0,110,4.2,8,Tests multiple critical co-occurrence (PLT + ANC)
DOC-003,15.2,88,8.5,250,Negative control (should be S-NORMAL)
```

---

## Performance Benchmarks

### Expected Performance

| Test Set Size | Time (pandas) | Time (csv) | Throughput |
|---------------|---------------|------------|------------|
| 10 cases | 3s | 5s | ~3 cases/s |
| 30 cases | 8s | 15s | ~3.5 cases/s |
| 100 cases | 30s | 60s | ~3 cases/s |
| 240 cases (Red List) | 70s | 140s | ~3.5 cases/s |
| 1000 cases | 5 min | 10 min | ~3 cases/s |

**Note:** API latency dominates (avg 2.5ms per case). CSV parsing is negligible with pandas.

### Optimization Tips

1. **Use pandas:** 2x faster CSV parsing
2. **Parallel requests:** Future feature (10x speedup)
3. **Batch endpoint:** Future feature (single upload)
4. **Local API:** Avoid network latency
5. **Warm cache:** First request slower (YAML loading)

---

## Example Test Sets

### Smoke Test (10 cases)

**File:** `smoke_tests.csv`

**Purpose:** Quick validation (30 seconds)

**Coverage:**
- 1 normal case
- 3 critical syndromes (anemia, neutropenia, thrombocytopenia)
- 2 priority syndromes
- 2 routine syndromes
- 2 edge cases

### Comprehensive Test (30 cases)

**File:** `comprehensive_30_cases.csv`

**Purpose:** All syndrome categories (2 minutes)

**Coverage:**
- All 9 critical syndromes
- All 15 priority syndromes
- Sample of 6 routine syndromes
- 5 edge cases (missing data, boundaries)

### Red List Validation (240 cases)

**File:** `red_list_240_cases.csv`

**Purpose:** FN=0 validation for critical syndromes (5 minutes)

**Coverage:**
- 8 critical syndromes × 30 cases each
- Boundary testing (near cutoffs)
- Co-occurrence testing
- Must achieve FN=0 (100% sensitivity)

### Regression Suite (1000 cases)

**File:** `regression_1000_cases.csv`

**Purpose:** Full coverage regression testing (30 minutes)

**Coverage:**
- All 35 syndromes
- All evidence combinations
- All age groups
- All morphology tokens
- Performance benchmarking

---

## Next Steps

After successful CSV testing:

1. **Integrate with CI/CD** (GitHub Actions)
2. **Create custom test sets** for your use cases
3. **Automate regression testing** (nightly builds)
4. **Generate test reports** for regulatory submission
5. **Implement batch endpoint** (optional, for >100 cases)

---

## References

- **CSV Format Spec:** `docs/CSV_FORMAT_SPEC.md`
- **Test Script:** `scripts/test_csv.py`
- **API Docs:** http://localhost:8000/docs (after starting server)
- **CBC Model:** `src/hemodoctor/models/cbc.py` (54 fields)
- **YAML Configs:** `config/*.yaml` (16 files)

---

## Support

**Issues or questions?**

1. Check this guide first
2. Review CSV_FORMAT_SPEC.md
3. Check API documentation: http://localhost:8000/docs
4. Review test script help: `python3 scripts/test_csv.py --help`
5. Contact: Dr. Abel Costa (abel.costa@hemodoctor.com)

---

**End of Testing Workflow Guide**
