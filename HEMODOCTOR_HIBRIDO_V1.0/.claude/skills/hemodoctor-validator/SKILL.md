---
name: hemodoctor-validator
description: Validates HemoDoctor clinical rule YAMLs against schema, checks consistency across files, ensures all 34 syndromes have triggers, and verifies regulatory compliance (ANVISA, FDA). Use when working with HemoDoctor YAML files or implementing medical decision support systems with complex rule-based logic.
license: Complete terms in LICENSE.txt
---

# HemoDoctor YAML Validator

Comprehensive validation toolkit for HemoDoctor clinical rule YAMLs. Ensures syntactic correctness, semantic consistency, complete syndrome coverage, and regulatory compliance.

## When to Use This Skill

- **Editing HemoDoctor YAMLs** - Validate after every change to catch errors early
- **Before deployment** - Run full validation suite to ensure production readiness
- **Code review** - Verify all 34 syndromes have triggers and evidence references are valid
- **CI/CD integration** - Automate validation in your pipeline
- **Debugging** - Identify inconsistencies across related YAML files
- **Compliance audits** - Generate reports for ANVISA/FDA submissions

## Quick Start

### 1. Validate a Single YAML File

```bash
python scripts/validate_yaml.py 03_syndromes_hybrid.yaml
```

**What it checks:**
- YAML syntax correctness
- Required fields present
- Valid values for enums (priority, category, combine)
- Duplicate IDs
- Expected counts (34 syndromes, 75 evidences, 34 triggers)

### 2. Validate Entire Directory

```bash
python scripts/validate_yaml.py /path/to/yamls/
```

Validates all `.yaml` and `.yml` files in the directory.

### 3. Check Syndrome Coverage

```bash
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml
```

**What it checks:**
- All 34 syndromes have at least one trigger
- Identifies uncovered syndromes
- Shows syndromes with multiple triggers
- Generates missing trigger templates

**Optional**: Generate templates for missing triggers

```bash
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml missing_triggers.yaml
```

### 4. Check Cross-File Consistency

```bash
python scripts/consistency_checker.py /path/to/yamls/
```

**What it checks:**
- Schema fields have units defined in config
- Syndromes reference valid evidence IDs
- Evidence rules reference valid schema fields
- No orphaned definitions

## Validation Rules by File Type

### 00_config_hybrid.yaml

**Required keys:**
- `version` - Config version string
- `units` - Field units mapping
- `cutoffs` - Clinical thresholds
- `age_groups` - Age stratification

**Validated:**
- All units are strings
- Cutoff values are numeric or dict of numeric
- Age groups have min/max ranges

### 01_schema_hybrid.yaml

**Required keys:**
- `fields` - Array of field definitions

**Required fields:**
- `hb`, `mcv`, `wbc`, `plt`, `age_years`, `sex`

**Field requirements:**
- `name` (required)
- `type` (required: float, int, enum, tri_bool)
- `unit` (required for numeric fields)
- `loinc` (recommended)
- `physiological_range` (recommended)

### 02_evidence_hybrid.yaml

**Required keys:**
- `evidences` - Array of evidence definitions

**Evidence requirements:**
- `id` (required, unique)
- `category` (required: critical, strong, moderate, weak)
- `description` (required)
- `weight` (required: 0.0 to 1.0)
- `condition` (recommended)

**Expected count:** 75 evidences

### 03_syndromes_hybrid.yaml

**Required keys:**
- `syndromes` - Array of syndrome definitions

**Syndrome requirements:**
- `id` (required, unique)
- `name` (required)
- `priority` (required: critical, priority, review, routine)
- `combine` (required: all, any)
- `evidences` (required: array of evidence IDs)

**Expected counts:**
- 8 critical syndromes
- 23 priority syndromes
- 1 review syndrome
- 2 routine syndromes
- **Total: 34 syndromes**

### 09_next_steps_engine_hybrid.yaml

**Required keys:**
- `triggers` - Array of trigger definitions

**Trigger requirements:**
- `id` (required, unique)
- `when` (required: Python expression)
- `syndromes` (required: array of syndrome IDs)
- `suggest` (required: array of test recommendations)

**Suggest item requirements:**
- `test` (required)
- `level` (required: critical, priority, routine)
- `rationale` (required)
- `cost` (recommended)
- `turnaround` (recommended)

**Expected count:** 34 triggers (one per syndrome minimum)

## Understanding Validation Output

### Success

```
✅ All validations passed!
```

All checks passed - safe to deploy.

### Warnings

```
⚠️  WARNINGS (2):
  • Expected 34 triggers, found 32
  • Schema fields without units in config (3): blastos, cd34_pct, mielocitos
```

Non-critical issues - review before deployment. Some warnings may be intentional (e.g., future fields without units yet).

### Errors

```
❌ ERRORS (3):
  • 03_syndromes_hybrid.yaml: Duplicate syndrome ID 'S-IDA'
  • Syndromes reference non-existent evidence IDs (1): S-TMA → E-PLT-CRIT-UNKNOWN
  • 09_next_steps_engine_hybrid.yaml: Trigger 'trigger-ida' missing 'when'
```

Critical issues - **must fix before deployment**. Errors indicate invalid YAML structure or missing required fields.

## Common Workflows

### After Editing a YAML

```bash
# 1. Validate the specific file
python scripts/validate_yaml.py 03_syndromes_hybrid.yaml

# 2. Check consistency with related files
python scripts/consistency_checker.py /path/to/yamls/
```

### Before Committing Changes

```bash
# Run full validation suite
python scripts/validate_yaml.py /path/to/yamls/
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml
python scripts/consistency_checker.py /path/to/yamls/
```

### Adding a New Syndrome

```bash
# 1. Add syndrome to 03_syndromes_hybrid.yaml
# 2. Add evidence(s) to 02_evidence_hybrid.yaml if needed
# 3. Validate syndromes file
python scripts/validate_yaml.py 03_syndromes_hybrid.yaml

# 4. Check coverage (will show new syndrome as uncovered)
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml missing_triggers.yaml

# 5. Add trigger to 09_next_steps_engine_hybrid.yaml using template from missing_triggers.yaml
# 6. Validate next_steps file
python scripts/validate_yaml.py 09_next_steps_engine_hybrid.yaml

# 7. Verify coverage is now 100%
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml
```

### Regulatory Audit Preparation

```bash
# Generate full validation report
python scripts/validate_yaml.py /path/to/yamls/ > validation_report.txt
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml >> validation_report.txt
python scripts/consistency_checker.py /path/to/yamls/ >> validation_report.txt

# Review validation_report.txt for any errors or warnings
# Address all issues before submitting to ANVISA/FDA
```

## Integration with CI/CD

### GitHub Actions

Create `.github/workflows/validate-yamls.yml`:

```yaml
name: Validate HemoDoctor YAMLs
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: pip install pyyaml
      
      - name: Validate YAML syntax and structure
        run: python scripts/validate_yaml.py yamls/
      
      - name: Check syndrome coverage
        run: python scripts/coverage_checker.py yamls/03_syndromes_hybrid.yaml yamls/09_next_steps_engine_hybrid.yaml
      
      - name: Check cross-file consistency
        run: python scripts/consistency_checker.py yamls/
```

### Pre-commit Hook

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python scripts/validate_yaml.py yamls/ || exit 1
python scripts/coverage_checker.py yamls/03_syndromes_hybrid.yaml yamls/09_next_steps_engine_hybrid.yaml || exit 1
```

## Troubleshooting

### "YAML syntax error: mapping values are not allowed here"

**Cause:** Missing quotes around strings with special characters (colons, brackets)

**Fix:**
```yaml
# ❌ Wrong
description: condition: x > 5

# ✅ Correct
description: "condition: x > 5"
```

### "Expected 34 syndromes, found 33"

**Cause:** Missing or commented-out syndrome definition

**Fix:** Check 03_syndromes_hybrid.yaml for missing/commented syndromes

### "Syndromes reference non-existent evidence IDs"

**Cause:** Typo in evidence ID or evidence not yet defined

**Fix:** 
1. Check spelling in syndrome's `evidences` array
2. Verify evidence exists in 02_evidence_hybrid.yaml

### "Expected 34 triggers, found 32"

**Cause:** Missing triggers for some syndromes

**Fix:**
```bash
# Generate missing trigger templates
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml missing_triggers.yaml

# Review and add triggers from missing_triggers.yaml to 09_next_steps_engine_hybrid.yaml
```

## Resources

- **scripts/validate_yaml.py** - Main validator for individual YAML files and directories
- **scripts/coverage_checker.py** - Ensures all syndromes have triggers, generates missing templates
- **scripts/consistency_checker.py** - Cross-file validation (schema ↔ config ↔ evidence ↔ syndromes)
- **references/quick_reference.md** - Common errors, fixes, and validation workflows

## Regulatory Compliance

This validator helps ensure compliance with:

- **ANVISA RDC 657/2022** - Software as Medical Device (SaMD) validation
- **FDA 21 CFR Part 11** - Electronic records and signatures
- **ISO 13485:2016** - Quality management systems for medical devices
- **IEC 62304:2015** - Medical device software lifecycle

**Validation reports can be used as evidence in regulatory submissions.**

## Best Practices

1. **Validate after every edit** - Catch errors early
2. **Run full suite before commit** - Ensure nothing breaks
3. **Check coverage when adding syndromes** - Don't leave syndromes without triggers
4. **Review warnings** - Some are intentional, document why
5. **Integrate with CI/CD** - Automate validation in pipeline
6. **Generate reports for audits** - Save validation output for regulatory submissions

## Expected Metrics

| Metric | Target | Critical? |
|--------|--------|-----------|
| Syntax errors | 0 | ✅ Yes |
| Missing required fields | 0 | ✅ Yes |
| Duplicate IDs | 0 | ✅ Yes |
| Invalid evidence references | 0 | ✅ Yes |
| Syndrome count | 34 | ✅ Yes |
| Evidence count | 75 | ⚠️ Recommended |
| Trigger count | 34 | ✅ Yes |
| Coverage | 100% | ✅ Yes |
