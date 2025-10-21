---
name: clinical-test-generator
description: Generate synthetic CBC test cases with ground truth for HemoDoctor validation. Creates Red List critical cases (FN=0 required), balanced validation sets, and missing-data scenarios. Exports to JSON/CSV/YAML. Use when building test suites, validating clinical rules, or creating training datasets for medical decision support systems.
license: Complete terms in LICENSE.txt
---

# Clinical Test Case Generator

Generate high-quality synthetic Complete Blood Count (CBC) test cases with ground truth labels for validating HemoDoctor clinical rules.

## When to Use This Skill

- **Building test suites** - Generate Red List cases (40+ per critical syndrome)
- **Validation testing** - Create balanced datasets (500+ cases) for retrospective validation
- **Testing edge cases** - Generate borderline cases, missing data scenarios
- **Training datasets** - Create labeled datasets for ML model training
- **Always-output testing** - Validate missingness engine and proxy logic
- **Regulatory compliance** - Generate test cases for ANVISA/FDA submissions

## Quick Start

### Generate Red List (Critical Cases)

```bash
python scripts/generate_test_cases.py red-list 40 red_list.json
```

**Output:** 320 critical cases (40 × 8 syndromes)
- S-NEUTROPENIA-GRAVE (severe & very critical variants)
- S-TMA (with & without hemolysis)
- S-BLASTIC-SYNDROME
- S-ANEMIA-GRAVE (M & F variants)
- S-PLT-CRITICA

**Why Red List?** FN=0 requirement - zero false negatives allowed for critical syndromes.

### Generate Validation Set

```bash
python scripts/generate_test_cases.py validation 500 validation_set.csv
```

**Output:** 500 balanced cases
- 10% Critical (50 cases)
- 40% Priority (200 cases: IDA, B12 def, thal trait, eosinophilia)
- 50% Normal/routine (250 cases)

### Generate Missing Data Cases

```bash
python scripts/generate_test_cases.py missing 50 missing_data.json
```

**Output:** 50 cases with 20-40% complementary tests randomly missing
- Tests missingness engine
- Tests proxy logic (infer from morphology)
- Tests always-output behavior

## Syndrome Coverage

### Critical (8 syndromes):
1. **S-NEUTROPENIA-GRAVE** - ANC <0.5 (critical) or <0.2 (very critical)
2. **S-TMA** - PLT <25 + schistocytes + hemolysis
3. **S-BLASTIC-SYNDROME** - WBC >100 + blasts
4. **S-ANEMIA-GRAVE** - Hb <6.5 (M) or <6.0 (F)
5. **S-PLT-CRITICA** - PLT <10
6. **S-NEUTROFILIA-LEFTSHIFT-CRIT** - WBC >11 + ANC >10 + left shift
7. **S-THROMBOCITOSE-CRIT** - PLT >650 (clonal threshold)
8. **S-CIVD** - D-dimer + low fibrinogen + PT/APTT prolonged

### Priority (Examples):
- **S-IDA** - Microcytic anemia + low ferritin/TSAT
- **S-B12-DEFICIENCY** - Macrocytic anemia + low B12
- **S-BETA-THAL-TRAIT** - Microcytic + high RBC + elevated HbA2
- **S-EOSINOPHILIA** - Eosinophils >1.5

### Routine:
- **NORMAL** - All parameters within range
- **BORDERLINE-MICROCYTOSIS** - MCV 78-82 (suggests repeat/workup)

## Export Formats

### JSON (Recommended for Testing)
```json
[
  {
    "case_id": "NEUT-CRIT-1234",
    "hb": 13.2,
    "mcv": 88.5,
    "wbc": 2.1,
    "anc": 0.35,
    "plt": 245.0,
    "age_years": 52.3,
    "sex": "F",
    "ground_truth_syndrome": "S-NEUTROPENIA-GRAVE",
    "ground_truth_priority": "critical",
    "notes": "Severe neutropenia ANC=0.35"
  }
]
```

### CSV (Good for Spreadsheets)
```csv
case_id,hb,mcv,wbc,anc,plt,ground_truth_syndrome,ground_truth_priority
NEUT-CRIT-1234,13.2,88.5,2.1,0.35,245.0,S-NEUTROPENIA-GRAVE,critical
```

### YAML (Human-Readable)
```yaml
- case_id: NEUT-CRIT-1234
  hb: 13.2
  mcv: 88.5
  wbc: 2.1
  anc: 0.35
  plt: 245.0
  ground_truth_syndrome: S-NEUTROPENIA-GRAVE
  ground_truth_priority: critical
```

## Clinical Patterns

### Iron Deficiency Anemia (IDA)
```
Hb:       <13 (M) or <12 (F)
MCV:      <80 (microcytic)
RDW:      >14 (anisocytosis)
Ferritin: <30 ng/mL
TSAT:     <20%
PLT:      Often elevated (200-450)
```

**Stages:**
- **Classic:** Ferritin 5-20, TSAT 5-15
- **Borderline:** Ferritin 20-30, TSAT 15-20  
- **Severe:** Ferritin <10, TSAT <10

### Beta-Thalassemia Trait
```
Hb:   10.5-13.0 (mild anemia)
MCV:  60-72 (microcytic)
RDW:  Normal (11-14)
RBC:  HIGH (5.5-7.0) ← KEY FEATURE
HbA2: >3.5% (elevated)
```

**vs. IDA:** Thal has HIGH RBC count, IDA has LOW

### TMA (Thrombotic Microangiopathy)
```
PLT:         <25 (critical)
Schistocytes: Present (≥1%)
Hb:          6.0-9.0 (hemolytic anemia)
LDH:         500-2000 (hemolysis)
Haptoglobin: <40 (consumed)
Bilirubin:   >1.0 (indirect)
```

## Advanced Usage

### Custom Mix of Syndromes

```python
from generate_test_cases import ClinicalTestGenerator

gen = ClinicalTestGenerator(seed=42)

# Generate specific mix
cases = []
for _ in range(10):
    cases.append(gen.generate_ida("classic"))
    cases.append(gen.generate_ida("borderline"))
    cases.append(gen.generate_tma(with_hemolysis=True))
    cases.append(gen.generate_normal("F"))

gen.export_json("custom_mix.json", cases)
gen.print_summary()
```

### Generate Single Case Type

```python
from generate_test_cases import ClinicalTestGenerator

gen = ClinicalTestGenerator()

# Just TMA cases
tma_cases = [gen.generate_tma() for _ in range(20)]
gen.export_csv("tma_only.csv", tma_cases)
```

### Add Custom Fields

```python
case = gen.generate_ida()
case.notes = "Patient on PPI therapy"
case.custom_field = "Additional metadata"
```

## Validation Workflow

### Step 1: Generate Test Cases
```bash
python scripts/generate_test_cases.py validation 500 test_cases.json
```

### Step 2: Run Through HemoDoctor
```python
import json
from hemodoctor import HemoDoctorEngine

engine = HemoDoctorEngine()

with open('test_cases.json') as f:
    cases = json.load(f)

results = []
for case in cases:
    prediction = engine.analyze(case)
    results.append({
        'case_id': case['case_id'],
        'ground_truth': case['ground_truth_syndrome'],
        'predicted': prediction['primary_syndrome'],
        'match': case['ground_truth_syndrome'] == prediction['primary_syndrome']
    })
```

### Step 3: Calculate Metrics
```python
# False negatives for critical cases
critical_cases = [r for r in results if r['ground_truth'].startswith('S-')]
fn_critical = sum(1 for r in critical_cases if not r['match'])

print(f"Critical FN: {fn_critical} (MUST BE 0)")

# Overall accuracy
accuracy = sum(r['match'] for r in results) / len(results)
print(f"Accuracy: {accuracy:.2%}")
```

## Test Case Quality

### Physiologically Plausible Values
- All values within physiological ranges (e.g., Hb 0-25 g/dL)
- Derived values consistent (MCHC, RBC calculated correctly)
- Age/sex appropriate for syndrome

### Ground Truth Labeling
- Clear syndrome ID (matches 03_syndromes_hybrid.yaml)
- Priority level (critical/priority/routine)
- Descriptive notes

### Reproducibility
- Uses seed=42 for reproducible generation
- Same seed → same cases

## Use Cases by Role

### For Developers
```bash
# Quick sanity check
python scripts/generate_test_cases.py validation 10 quick_test.json
```

### For QA Engineers
```bash
# Full regression suite
python scripts/generate_test_cases.py red-list 40 critical_cases.json
python scripts/generate_test_cases.py validation 500 validation.csv
python scripts/generate_test_cases.py missing 50 missing_data.json
```

### For Clinical Validators
```bash
# Export to CSV for manual review
python scripts/generate_test_cases.py validation 100 review.csv
# Open review.csv in Excel, verify clinical accuracy
```

### For Regulatory Submissions
```bash
# Generate test evidence for ANVISA/FDA
python scripts/generate_test_cases.py red-list 50 regulatory_critical.json
python scripts/generate_test_cases.py validation 1000 regulatory_validation.csv
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'yaml'"
```bash
pip install pyyaml
```

### Cases Look Unrealistic
- Check seed (should be 42 for consistency)
- Review references/clinical_patterns.md for expected ranges
- Verify generators match clinical guidelines

### Need More Syndrome Types
- Edit scripts/generate_test_cases.py
- Add new generator method (e.g., `generate_folate_deficiency()`)
- Follow existing pattern in script

## Resources

- **scripts/generate_test_cases.py** - Main generator with 15+ syndrome generators
- **references/clinical_patterns.md** - Clinical correlations, lab patterns, quality checklist

## Expected Output Statistics

### Red List (40 per syndrome)
- Total: 320 cases
- All critical priority
- FN=0 required

### Validation Set (500 cases)
- Critical: ~50 (10%)
- Priority: ~200 (40%)
- Normal/routine: ~250 (50%)

### Missing Data (50 cases)
- 20-40% fields missing
- Tests always-output behavior
- Ground truth still labeled

## Best Practices

1. **Always use seed=42** for reproducibility
2. **Review first 10 cases** manually before generating 100s
3. **Export to CSV** for clinical review
4. **Export to JSON** for automated testing
5. **Generate fresh cases** for each sprint/release
6. **Keep ground truth** separate from predictions during testing

## Regulatory Compliance

Generated test cases support:
- **ANVISA RDC 657/2022** - SaMD validation evidence
- **FDA 21 CFR Part 11** - Electronic test records
- **ISO 13485** - Quality management for medical devices
- **IEC 62304** - Software lifecycle validation

**Test cases can be used as evidence in regulatory submissions.**
