---
name: YAML Validation
description: Validate YAML syntax and structure for HemoDoctor Hybrid V1.0 configuration files. Use when checking YAMLs in the YAMLs/ directory, validating schema compliance, or troubleshooting YAML syntax errors.
---

# YAML Validation

Validates the 15 YAML configuration files that define HemoDoctor's clinical logic.

## Quick start

Validate a single YAML:

```bash
python .claude/skills/yaml-validation/scripts/validate_yaml.py YAMLs/00_config_hybrid.yaml
```

Validate all YAMLs:

```bash
python .claude/skills/yaml-validation/scripts/validate_all.py
```

## YAML modules

The system has 15 YAML modules (~7,350 lines total):

**Core pipeline (sequential):**
- `00_config_hybrid.yaml` - Units, cutoffs, normalization
- `01_schema_hybrid.yaml` - Canonical schema
- `02_evidence_hybrid.yaml` - 75 evidence rules
- `03_syndromes_hybrid.yaml` - 34 syndromes

**Always-output (V2.3):**
- `04_output_templates_hybrid.yaml` - Card templates
- `05_missingness_hybrid_v2.3.yaml` - Proxy logic + guaranteed output
- `09_next_steps_engine_hybrid.yaml` - Clinical next steps
- `12_output_policies_hybrid.yaml` - Output orchestration

**Audit trail:**
- `06_route_policy_hybrid.yaml` - Deterministic routing
- `07_conflict_matrix_hybrid.yaml` - Conflict resolution
- `07_normalization_heuristics.yaml` - Site-specific normalization
- `08_wormlog_hybrid.yaml` - WORM audit log

**Operational:**
- `10_runbook_hybrid.yaml` - Implementation roadmap
- `11_case_state_hybrid.yaml` - State machine

## Validation workflow

1. **Syntax check**: Verify YAML parses without errors
2. **Structure validation**: Check required fields exist
3. **Cross-reference check**: Verify references between files
4. **Report errors**: Show specific line numbers and issues

## Common YAML errors

**Indentation issues:**
```yaml
# ❌ WRONG - Inconsistent indentation
syndromes:
  - id: S-TMA
   criticality: critical  # Off by 1 space

# ✅ CORRECT - Consistent 2-space indentation
syndromes:
  - id: S-TMA
    criticality: critical
```

**Missing quotes:**
```yaml
# ❌ WRONG - Special characters need quotes
description: Use when: analyzing data  # Colon breaks parsing

# ✅ CORRECT - Quote strings with special chars
description: "Use when: analyzing data"
```

**List syntax:**
```yaml
# ❌ WRONG - Mixed syntax
combine:
  all: E-ANC-CRIT, E-PLT-LOW  # Comma-separated not valid

# ✅ CORRECT - Array syntax
combine:
  all: ["E-ANC-CRIT", "E-PLT-LOW"]
```

## Script reference

**validate_yaml.py**: Validate single file
- Checks syntax (YAML parsing)
- Checks structure (required fields)
- Returns exit code 0 (success) or 1 (failure)

**validate_all.py**: Validate all 15 YAMLs
- Runs validation on each file
- Reports summary (X/15 passed)
- Lists all errors found

## Troubleshooting

**"YAML syntax error at line X":**
- Check indentation (use spaces, not tabs)
- Check for missing quotes around special characters
- Check for unclosed brackets/quotes

**"Required field missing":**
- Each YAML module has required fields
- Check the schema in INDEX_COMPLETO.md
- Compare with working examples in other modules

**"Invalid reference":**
- Evidence IDs must start with `E-`
- Syndrome IDs must start with `S-`
- Flow IDs must start with `F-`
- Referenced IDs must exist in the appropriate module
