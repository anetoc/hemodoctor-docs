# HemoDoctor YAML Validation - Quick Reference

## Common Validation Errors

### YAML Syntax Errors

**Error**: `YAML syntax error: mapping values are not allowed here`
**Fix**: Check for missing quotes around strings with colons or special characters

**Error**: `YAML syntax error: expected <block end>, but found '-'`
**Fix**: Check indentation - YAML is whitespace-sensitive (use 2 spaces per level)

### Schema Validation Errors

**Error**: `Field missing 'name' attribute`
**Fix**: Every field in 01_schema must have a `name` key

**Error**: `Missing required field 'hb'`
**Fix**: Ensure all required fields exist: hb, mcv, wbc, plt, age_years, sex

**Error**: `Field 'X' missing 'type'`
**Fix**: Add type (float, int, enum, tri_bool) to field definition

### Evidence Validation Errors

**Error**: `Duplicate evidence ID 'XXX'`
**Fix**: Each evidence must have a unique `id`

**Error**: `Evidence 'XXX' has invalid category`
**Fix**: Category must be one of: critical, strong, moderate, weak

**Error**: `Evidence 'XXX' missing 'weight'`
**Fix**: Add weight field (0.0 to 1.0)

### Syndrome Validation Errors

**Error**: `Duplicate syndrome ID 'XXX'`
**Fix**: Each syndrome must have a unique `id`

**Error**: `Syndrome 'XXX' has invalid priority`
**Fix**: Priority must be one of: critical, priority, review, routine

**Error**: `Syndrome 'XXX' has invalid combine`
**Fix**: Combine logic must be 'all' or 'any'

**Error**: `Expected 34 syndromes, found XX`
**Fix**: Verify all syndromes are defined (8 critical, 23 priority, 1 review, 2 routine)

### Next Steps Validation Errors

**Error**: `Trigger 'XXX' missing 'when'`
**Fix**: Add `when` condition (Python expression)

**Error**: `Invalid level 'XXX' in trigger`
**Fix**: Level must be one of: critical, priority, routine

**Error**: `Expected 34 triggers, found XX`
**Fix**: Ensure all 34 syndromes have corresponding triggers

### Cross-File Consistency Errors

**Error**: `Syndromes reference non-existent evidence IDs`
**Fix**: Verify evidence IDs in 02_evidence match those referenced in 03_syndromes

**Error**: `Schema fields without units in config`
**Fix**: Add missing units to 00_config (or confirm they don't need units)

## Validation Workflow

### Step 1: Individual File Validation
```bash
python scripts/validate_yaml.py 03_syndromes_hybrid.yaml
```

### Step 2: Directory Validation
```bash
python scripts/validate_yaml.py /path/to/yamls/
```

### Step 3: Coverage Check
```bash
python scripts/coverage_checker.py 03_syndromes_hybrid.yaml 09_next_steps_engine_hybrid.yaml
```

### Step 4: Consistency Check
```bash
python scripts/consistency_checker.py /path/to/yamls/
```

## Expected Outputs

### Successful Validation
```
✅ All validations passed!
```

### Validation with Warnings
```
⚠️  WARNINGS (2):
  • Schema fields without units in config (5): blastos, cd34_pct...
  • Expected 34 triggers, found 32
```

### Validation Failures
```
❌ ERRORS (3):
  • 03_syndromes_hybrid.yaml: Duplicate syndrome ID 'S-IDA'
  • 09_next_steps_engine_hybrid.yaml: Trigger missing 'when'
  • Syndromes reference non-existent evidence IDs (2): S-TMA → E-PLT-UNKNOWN
```

## Regulatory Compliance Checklist

- [ ] All YAMLs pass syntax validation
- [ ] All 34 syndromes defined (8 critical, 23 priority, 1 review, 2 routine)
- [ ] All 75 evidences defined with valid categories
- [ ] All 34 syndromes have corresponding triggers
- [ ] No duplicate IDs (evidences, syndromes, triggers)
- [ ] All syndrome-evidence references valid
- [ ] All critical syndromes have priority='critical'
- [ ] All next_steps triggers have valid 'when' conditions
- [ ] Schema-config consistency validated

## Best Practices

1. **Run validation after every YAML edit**
2. **Fix errors before warnings**
3. **Use coverage_checker before committing**
4. **Validate entire directory before deployment**
5. **Document any intentional warnings**

## CI/CD Integration

Add to your pipeline:

```yaml
# .github/workflows/validate-yamls.yml
name: Validate YAMLs
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: pip install pyyaml
      - name: Validate YAMLs
        run: |
          python scripts/validate_yaml.py yamls/
          python scripts/coverage_checker.py yamls/03_syndromes_hybrid.yaml yamls/09_next_steps_engine_hybrid.yaml
          python scripts/consistency_checker.py yamls/
```
