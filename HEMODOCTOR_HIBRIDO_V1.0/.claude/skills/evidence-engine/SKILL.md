---
name: Evidence Engine
description: Work with HemoDoctor's 75 atomic evidence rules (E-XXX) for CBC analysis. Use when implementing evidence evaluation, testing evidence logic, or debugging syndrome detection.
---

# Evidence Engine

Implements the 75 atomic evidence rules that detect patterns in CBC (complete blood count) data.

## Evidence structure

Each evidence is defined in `YAMLs/02_evidence_hybrid.yaml`:

```yaml
- id: E-ANC-CRIT
  strength: critical
  rule: "anc < anc_critical"
  requires: ["anc"]
  category: white_series
```

**Fields:**
- `id`: Unique identifier (E-XXX format)
- `strength`: critical/strong/moderate/weak
- `rule`: Expression to evaluate (use simpleeval, NOT eval())
- `requires`: Fields needed from CBC input
- `category`: red_series/white_series/platelet_series/coagulation/complementary

## Evidence categories

**Critical gates (11):** Life-threatening conditions
- `E-ANC-CRIT`: ANC <0.2 (severe neutropenia)
- `E-PLT-CRIT-LOW`: PLT <10 (critical thrombocytopenia)
- `E-HB-CRIT-LOW`: Hb <6.5 M / <6.0 F (severe anemia)
- `E-WBC-CRIT-HIGH`: WBC >100 (hyperleukocytosis)
- `E-SCHISTOCYTES-GE1PCT`: Schistocytes ≥1% (TMA)

**Red series (18):** Anemia patterns
- `E-MICROCYTOSIS`: MCV <80
- `E-MACROCYTOSIS`: MCV >100
- `E-RDW-HIGH`: RDW >15%
- `E-IDA-LABS`: Ferritin <30, transferrin saturation <20%

**White series (23):** Leukocyte patterns
- `E-NEUTROPENIA`: ANC <1.5
- `E-LEUKOCYTOSIS`: WBC >11
- `E-BLASTS-PRESENT`: Blasts >0%
- `E-LEFT-SHIFT`: Bands + metamyelocytes + myelocytes >10%

**Platelet series (12):** Thrombocyte patterns
- `E-THROMBOCYTOPENIA`: PLT <150
- `E-THROMBOCYTOSIS`: PLT >450
- `E-MPV-HIGH`: MPV >11

**Coagulation (5):** Hemostasis markers
- `E-D-DIMER-HIGH`: D-dimer >500
- `E-FIBRINOGEN-LOW`: Fibrinogen <150

**Complementary (6):** Supporting tests
- `E-CRP-HIGH`: CRP >10
- `E-LDH-HIGH`: LDH >480

## Safe expression evaluation

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

## Handling missing data

Evidence evaluation must handle missing fields gracefully:

```python
def evaluate_evidence(evidence, cbc, config):
    """
    Returns:
        - "present": Evidence condition is met
        - "absent": Evidence condition is not met
        - "unknown": Required data is missing
    """

    # Check required fields
    for field in evidence["requires"]:
        if cbc.get(field) is None:
            return "unknown"

    # Evaluate rule safely
    try:
        result = simple_eval(
            evidence["rule"],
            names={**cbc, **config["cutoffs"]}
        )
        return "present" if result else "absent"
    except:
        return "unknown"
```

## Testing evidence

Test each evidence with:
1. **Positive case**: Condition met → "present"
2. **Negative case**: Condition not met → "absent"
3. **Missing data**: Required field absent → "unknown"

**Example test:**

```python
def test_evidence_anc_critical():
    config = load_config("YAMLs/00_config_hybrid.yaml")
    evidence = {
        "id": "E-ANC-CRIT",
        "rule": "anc < anc_critical",
        "requires": ["anc"]
    }

    # Positive case
    cbc = {"anc": 0.1}
    assert evaluate_evidence(evidence, cbc, config) == "present"

    # Negative case
    cbc = {"anc": 2.0}
    assert evaluate_evidence(evidence, cbc, config) == "absent"

    # Missing data
    cbc = {}
    assert evaluate_evidence(evidence, cbc, config) == "unknown"
```

## Common patterns

**Range check:**
```yaml
rule: "mcv >= 80 and mcv <= 100"  # Normal MCV
```

**Multiple conditions (AND):**
```yaml
rule: "ferritin < 30 and transferrin_sat < 0.20"  # IDA labs
```

**Morphology (tristate):**
```yaml
rule: "morphology.esquistocitos == true"  # Schistocytes present
```

**Percentage calculation:**
```yaml
rule: "(bands + metamielocitos + mielocitos) / wbc > 0.10"  # Left shift
```

## Debugging evidence

**Evidence not firing:**
1. Check required fields are present in CBC
2. Verify cutoff values in `00_config_hybrid.yaml`
3. Test rule evaluation with sample values
4. Check for type mismatches (string vs number)

**Unexpected results:**
1. Print intermediate values
2. Check unit normalization (g/L vs g/dL)
3. Verify morphology tristate logic (true/false/unknown)
4. Check for edge cases (e.g., anc = exactly cutoff value)

## Script reference

**list_evidences.py**: List all 75 evidences with IDs and categories

```bash
python .claude/skills/evidence-engine/scripts/list_evidences.py
```

**test_evidence.py**: Test a single evidence with sample CBC

```bash
python .claude/skills/evidence-engine/scripts/test_evidence.py E-ANC-CRIT --anc=0.3
```

## Integration with syndromes

Evidences feed into syndrome logic (`03_syndromes_hybrid.yaml`):

```yaml
- id: S-TMA
  combine:
    all: ["E-SCHISTOCYTES-GE1PCT", "E-PLT-CRIT-LOW"]
    any: ["E-HEMOLYSIS-PATTERN", "E-LDH-HIGH"]
```

Claude evaluates all 75 evidences first, then uses their results to determine which syndromes are present.
