---
name: next-steps-debugger
description: Debug and test HemoDoctor next_steps_engine triggers (module 09). Simulate cases, find dead code (triggers that never fire), detect syntax errors in 'when' expressions. Use when developing triggers, debugging missing recommendations, or ensuring 100% trigger coverage before deployment.
license: Complete terms in LICENSE.txt
---

# Next Steps Debugger

Debug, test, and validate triggers in HemoDoctor's next_steps_engine (module 09). Find dead code, test edge cases, simulate clinical scenarios.

## When to Use This Skill

- **Developing triggers** - Test new 'when' expressions before deployment
- **Debugging** - Why isn't a trigger firing for this case?
- **Coverage testing** - Ensure all 34 triggers are reachable
- **Regression testing** - Verify triggers after YAML changes
- **Code review** - Validate trigger logic before merge

## Quick Start

### Test Triggers with Case File

```bash
python scripts/debug_next_steps.py test 09_next_steps_engine_hybrid.yaml test_cases.json --verbose
```

**Output:** Shows which triggers fire for each case, finds dead triggers, detects syntax errors.

### Simulate a Single Case

```bash
python scripts/debug_next_steps.py simulate 09_next_steps_engine_hybrid.yaml \
  --hb=9.5 --sex=F --mcv=72 --rdw=16 --ferritin=8
```

**Output:** Shows which triggers fire and what tests are recommended.

### Check Trigger Syntax

```bash
python scripts/debug_next_steps.py check 09_next_steps_engine_hybrid.yaml
```

**Output:** Validates all 'when' expressions without running test cases.

## Commands

| Command | Purpose | Example Use Case |
|---------|---------|------------------|
| `test` | Test triggers against JSON cases | Regression testing with 100 cases |
| `simulate` | Test single case with parameters | Debug why IDA trigger isn't firing |
| `check` | Validate syntax only | Quick syntax check before commit |

## Debugging Workflows

### Workflow 1: Why Isn't My Trigger Firing?

**Problem:** You added `trigger-ida` but it never fires for IDA cases.

**Solution:**
```bash
# Simulate an IDA case
python scripts/debug_next_steps.py simulate 09_next_steps.yaml \
  --hb=9.5 \
  --sex=F \
  --mcv=72 \
  --rdw=16 \
  --ferritin=8 \
  --tsat=12

# Output shows:
#   ✅ trigger-ida: FIRED
# or
#   ❌ trigger-ida: NOT FIRED
```

**Common Issues:**
- Missing field in 'when' expression (e.g., forgot `ferritin is None`)
- Wrong comparison operator (`<` vs `<=`)
- Typo in field name (`ferritin` vs `ferritin_ng_ml`)

---

### Workflow 2: Find Dead Triggers

**Problem:** Some triggers in your YAML never fire in testing.

**Solution:**
```bash
# Test with comprehensive case set
python scripts/debug_next_steps.py test 09_next_steps.yaml validation_set.json

# Report shows:
# ❌ Dead Triggers (3) - Never fired in ≥10 tests:
#   • trigger-folate-def
#   • trigger-g6pd
#   • trigger-hpn
```

**Action:** Either:
1. Add test cases for these syndromes
2. Verify triggers are correct (maybe condition is too strict)
3. Remove trigger if syndrome is obsolete

---

### Workflow 3: Test Trigger After Editing

**Problem:** You modified a trigger's 'when' expression and want to verify it still works.

**Solution:**
```bash
# Before edit - generate baseline
python scripts/debug_next_steps.py test 09_next_steps_OLD.yaml test_cases.json > before.txt

# After edit - compare
python scripts/debug_next_steps.py test 09_next_steps_NEW.yaml test_cases.json > after.txt

# Diff the outputs
diff before.txt after.txt
```

---

### Workflow 4: Validate All Triggers Pre-Commit

```bash
#!/bin/bash
# validate_triggers.sh

echo "🔍 Validating next_steps triggers..."

# 1. Check syntax
python scripts/debug_next_steps.py check 09_next_steps_engine_hybrid.yaml || exit 1

# 2. Test with validation set
python scripts/debug_next_steps.py test \
  09_next_steps_engine_hybrid.yaml \
  validation_set.json > trigger_test_report.txt

# 3. Check for dead triggers
grep "Dead Triggers" trigger_test_report.txt
if [ $? -eq 0 ]; then
  echo "⚠️  Warning: Some triggers never fired"
  cat trigger_test_report.txt
fi

echo "✅ Trigger validation complete"
```

## Simulation Examples

### Example 1: Iron Deficiency Anemia

```bash
python scripts/debug_next_steps.py simulate 09_next_steps.yaml \
  --hb=9.5 \
  --sex=F \
  --mcv=72 \
  --rdw=16
```

**Without ferritin/TSat:**
```
✅ trigger-ida: FIRED
  Suggested: Ferritin, TSat, CRP
```

**With ferritin/TSat:**
```bash
python scripts/debug_next_steps.py simulate 09_next_steps.yaml \
  --hb=9.5 \
  --sex=F \
  --mcv=72 \
  --rdw=16 \
  --ferritin=8 \
  --tsat=12
```
```
❌ trigger-ida: NOT FIRED
  (Already has ferritin/TSat - no further tests needed)
```

### Example 2: TMA (Thrombotic Microangiopathy)

```bash
python scripts/debug_next_steps.py simulate 09_next_steps.yaml \
  --plt=25 \
  --esquistocitos=true \
  --ldh=980
```

**Output:**
```
✅ trigger-tma: FIRED
  Suggested:
    • [critical] Esfregaço URGENTE
    • [priority] ADAMTS13 atividade + inibidor
    • [priority] Complemento (C3, C4, CH50)
```

### Example 3: Severe Neutropenia

```bash
python scripts/debug_next_steps.py simulate 09_next_steps.yaml \
  --anc=0.35 \
  --wbc=2.1
```

**Output:**
```
✅ trigger-neutropenia-grave: FIRED
  Suggested:
    • [critical] Repetir CBC urgente
    • [priority] CRP e hemoculturas se febre
    • [priority] G-CSF se indicação
```

### Example 4: Borderline Microcytosis

```bash
python scripts/debug_next_steps.py simulate 09_next_steps.yaml \
  --hb=13.5 \
  --sex=M \
  --mcv=81 \
  --rdw=12
```

**Output:**
```
✅ trigger-borderline-microcytosis: FIRED
  Suggested:
    • [routine] CBC repeat (2-6 semanas)
    • [routine] Ferritina se anemia limítrofe
```

## Report Interpretation

### Summary Section
```
📊 Summary:
  Total triggers: 34
  Never fired: 3
  With errors: 0
  Coverage: 91.2%
```

- **Total triggers:** Number in YAML
- **Never fired:** Triggers that didn't activate in any test
- **With errors:** Triggers with syntax errors
- **Coverage:** % of triggers that fired at least once

**Target:** Coverage ≥95% (max 1-2 dead triggers acceptable)

### Dead Triggers Section
```
❌ Dead Triggers (3) - Never fired in ≥10 tests:
  • trigger-folate-def
  • trigger-g6pd
  • trigger-hpn
```

**Action:** Generate test cases for these syndromes or review trigger conditions.

### Error Section
```
⚠️  Triggers with Errors (1):
  • trigger-ida:
    - Eval error: name 'ferritn' is not defined
```

**Common Errors:**
- Typo in field name (`ferritn` → `ferritin`)
- Missing comparison operator
- Invalid Python syntax

### Top Firing Triggers
```
🔥 Top 10 Firing Triggers:
  • trigger-normal: 250/500 (50.0%)
  • trigger-ida: 45/500 (9.0%)
  • trigger-neutropenia: 25/500 (5.0%)
```

**Interpretation:**
- Normal trigger fires most (expected for balanced validation set)
- IDA trigger fires 9% (reasonable for 10% priority cases)
- If critical trigger fires <1%, add more test cases

## Test Case Format (JSON)

```json
[
  {
    "case_id": "IDA-001",
    "hb": 9.5,
    "sex": "F",
    "mcv": 72,
    "rdw": 16,
    "ferritin": null,
    "tsat": null,
    "age_years": 35
  },
  {
    "case_id": "TMA-001",
    "plt": 25,
    "esquistocitos": true,
    "ldh": 980,
    "hb": 7.5
  }
]
```

**Fields:**
- Include all CBC fields (hb, mcv, wbc, plt, etc.)
- Use `null` for missing data
- Booleans for morphology (esquistocitos, blastos, etc.)

## Integration with Test Generator

```bash
# Generate test cases
python scripts/generate_test_cases.py validation 500 test_cases.json

# Debug triggers with generated cases
python scripts/debug_next_steps.py test 09_next_steps.yaml test_cases.json --verbose

# Analyze coverage
grep "Coverage:" trigger_report.txt
# Should show ≥95%
```

## CI/CD Integration

```yaml
# .github/workflows/test-triggers.yml
name: Test Next Steps Triggers

on:
  push:
    paths:
      - 'yamls/09_next_steps*.yaml'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install dependencies
        run: pip install pyyaml simpleeval
      
      - name: Check trigger syntax
        run: python scripts/debug_next_steps.py check yamls/09_next_steps_engine_hybrid.yaml
      
      - name: Test triggers
        run: |
          python scripts/debug_next_steps.py test \
            yamls/09_next_steps_engine_hybrid.yaml \
            test_data/validation_set.json \
            > trigger_report.txt
      
      - name: Check coverage
        run: |
          COVERAGE=$(grep "Coverage:" trigger_report.txt | awk '{print $2}' | tr -d '%')
          if (( $(echo "$COVERAGE < 95" | bc -l) )); then
            echo "❌ Coverage too low: $COVERAGE%"
            exit 1
          fi
          echo "✅ Coverage OK: $COVERAGE%"
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'simpleeval'"
```bash
pip install simpleeval
```

### "Eval error: name 'X' is not defined"
Field `X` is referenced in trigger but not in case. Either:
1. Add field to case JSON
2. Check for typos in trigger 'when' expression
3. Add `X is None` check in trigger

### Coverage Stuck at Low %
- Not enough test cases
- Test cases don't cover all syndrome patterns
- Triggers have unreachable conditions (logic bugs)

## Best Practices

1. **Test after every trigger edit** - Catch errors early
2. **Aim for 95%+ coverage** - Most triggers should fire in testing
3. **Use verbose mode** - See exactly which triggers fire
4. **Generate diverse test cases** - Cover edge cases, borderline values
5. **Keep dead triggers log** - Track intentionally unused triggers

## Expected Metrics

| Metric | Target | Critical? |
|--------|--------|-----------|
| Syntax errors | 0 | ✅ Yes |
| Coverage | ≥95% | ✅ Yes |
| Dead triggers | ≤2 | ⚠️ Recommended |
| Fire rate (critical) | >5% | ⚠️ Recommended |

## Resources

- **scripts/debug_next_steps.py** - Main debugger with 3 commands
- Use with **clinical-test-generator** skill for test case generation
- Reference **DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md** for trigger design patterns
