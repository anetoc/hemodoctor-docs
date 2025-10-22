# HemoDoctor CSV Format Specification

**Version:** 1.0.0
**Date:** 2025-10-23
**Author:** Dr. Abel Costa
**Purpose:** Define CSV format for batch testing HemoDoctor CDSS

---

## Overview

This document specifies the CSV format for testing HemoDoctor CDSS via batch uploads or scripted testing. The CSV format supports all 54 fields from the CBC input model, plus test metadata.

---

## CSV Structure

### Required Fields (3)

These fields MUST be present in every test case:

| Field | Type | Unit | Range | Description |
|-------|------|------|-------|-------------|
| `hb` | float | g/dL | 0-25 | Hemoglobin |
| `mcv` | float | fL | 50-150 | Mean Corpuscular Volume |
| `wbc` | float | 10^9/L | 0-200 | White Blood Cells |

### Optional CBC Fields (12)

| Field | Type | Unit | Range | Description |
|-------|------|------|-------|-------------|
| `plt` | float | 10^9/L | 0-2000 | Platelets |
| `anc` | float | 10^9/L | 0-50 | Absolute Neutrophil Count |
| `ht` | float | % | 0-75 | Hematocrit |
| `rbc` | float | 10^12/L | 0-10 | Red Blood Cells |
| `mch` | float | pg | 15-50 | Mean Corpuscular Hemoglobin |
| `mchc` | float | g/dL | 25-38 | MCHC |
| `rdw` | float | % | 9-20 | RDW |
| `lymphocytes_abs` | float | 10^9/L | 0-50 | Absolute Lymphocytes |
| `eosinophils_abs` | float | 10^9/L | 0-10 | Absolute Eosinophils |
| `basophils_abs` | float | 10^9/L | 0-2 | Absolute Basophils |
| `monocytes_abs` | float | 10^9/L | 0-10 | Absolute Monocytes |
| `mpv` | float | fL | 5-15 | Mean Platelet Volume |
| `reticulocytes` | float | 10^9/L | 0-500 | Reticulocytes |

### Optional Complementary Tests (9)

| Field | Type | Unit | Range | Description |
|-------|------|------|-------|-------------|
| `ferritin` | float | ng/mL | 0-10000 | Ferritin |
| `tsat` | float | % | 0-100 | Transferrin Saturation |
| `crp` | float | mg/L | 0-500 | C-Reactive Protein |
| `ldh` | float | U/L | 0-5000 | Lactate Dehydrogenase |
| `bt_indireta` | float | mg/dL | 0-50 | Indirect Bilirubin |
| `haptoglobin` | float | mg/dL | 0-300 | Haptoglobin |
| `b12` | float | pg/mL | 0-2000 | Vitamin B12 |
| `folate` | float | ng/mL | 0-50 | Folate |
| `hba2` | float | % | 0-10 | Hemoglobin A2 |
| `epo` | float | mIU/mL | 0-200 | Erythropoietin |

### Optional Molecular Markers (9)

Boolean fields (use `True`, `False`, or leave empty for `None`):

| Field | Description |
|-------|-------------|
| `coombs_pos` | Coombs Direct positive |
| `bcr_abl_pos` | BCR-ABL positive (CML) |
| `jak2_pos` | JAK2 V617F positive (MPN) |
| `calr_pos` | CALR mutation positive (MPN) |
| `mpl_pos` | MPL mutation positive (MPN) |
| `hpn_pos` | PNH clone (CD55/CD59 deficient) |
| `flc_ratio_abnormal` | Free Light Chains ratio abnormal |
| `g6pd_deficient` | G6PD deficient |
| `pk_deficient` | Pyruvate Kinase deficient |

### Optional Morphology Tokens (17)

Boolean fields (use `True`, `False`, or leave empty for `None`):

Prefix: `morphology.` (e.g., `morphology.schistocytes`)

| Token | Description |
|-------|-------------|
| `schistocytes` | Schistocytes present (≥1%) |
| `spherocytes` | Spherocytes present |
| `dacriocytes` | Dacriocytes (tear-drop cells) present |
| `elliptocytes` | Elliptocytes present |
| `target_cells` | Target cells present |
| `burr_cells` | Burr cells present |
| `acanthocytes` | Acanthocytes present |
| `sickle_cells` | Sickle cells present |
| `nucleated_rbc` | Nucleated RBCs present |
| `blasts` | Blasts present |
| `left_shift` | Left shift (bands/myelocytes/metamyelocytes) |
| `hypersegmented_neutrophils` | Hypersegmented neutrophils present |
| `auer_rods` | Auer rods present (APL) |
| `pelger_huet` | Pelger-Huët anomaly |
| `toxic_granulation` | Toxic granulation present |
| `dohle_bodies` | Döhle bodies present |
| `giant_platelets` | Giant platelets present |

### Optional Coagulation Tests (4)

| Field | Type | Unit | Range | Description |
|-------|------|------|-------|-------------|
| `d_dimer` | float | ng/mL | 0+ | D-dimer |
| `fibrinogenio` | float | mg/dL | 0+ | Fibrinogen |
| `pt` | float | s | 0+ | Prothrombin Time |
| `aptt` | float | s | 0+ | Activated Partial Thromboplastin Time |

### Metadata Fields (4)

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `age_years` | float | 0-120 | Age in years (optional for test, defaults to 35) |
| `sex` | string | M/F/U | Sex (M=Male, F=Female, U=Unknown, defaults to U) |
| `case_id` | string | - | **Test metadata: Case identifier** |
| `expected_syndrome` | string | - | **Test metadata: Expected syndrome(s) for validation** |

**Note:**
- `case_id`: Identifies the test case (required for test CSVs)
- `expected_syndrome`: Comma-separated list of expected syndromes (e.g., `S-NORMAL`, `S-PLT-CRITICA,S-NEUTROPENIA-GRAVE`)
- `age_years` and `sex`: Optional for API, but recommended for testing

---

## Validation Rules

### Field Validation

1. **Numeric Fields:**
   - Must be within specified ranges
   - Use `.` for decimal separator (not `,`)
   - Empty cells = `None` (missing data)

2. **Boolean Fields:**
   - Use `True`, `False`, or leave empty (case-insensitive)
   - Empty = `None` (unknown)

3. **String Fields:**
   - `sex`: Must be `M`, `F`, or `U`
   - `case_id`: Alphanumeric + hyphens (e.g., `CASE-001`)
   - `expected_syndrome`: Syndrome IDs separated by `,` or `+` (e.g., `S-PLT-CRITICA,S-ANEMIA-GRAVE`)

### Clinical Validation

1. **Consistency Checks (handled by API):**
   - RBC indices consistency (MCV, MCH, MCHC)
   - Age-appropriate ranges
   - Impossible combinations flagged

2. **Missing Data:**
   - Only `hb`, `mcv`, `wbc` are required
   - Other fields can be empty (missing data is handled gracefully)

---

## Example CSV Files

### Example 1: Basic Testing (10 cases)

```csv
case_id,hb,mcv,wbc,plt,anc,age_years,sex,expected_syndrome,notes
CASE-001,15.2,88,8.5,250,4.0,35,M,S-NORMAL,Normal healthy adult
CASE-002,5.8,65,12.0,180,8.0,8,M,S-ANEMIA-GRAVE,Severe microcytic anemia (pediatric)
CASE-003,14.0,110,4.2,8,0.3,42,F,S-PLT-CRITICA+S-NEUTROPENIA-GRAVE,Multiple critical syndromes
CASE-004,8.5,92,15.0,450,12.0,5,M,S-LEUKOCYTOSIS-REACTIVE,Reactive leukocytosis (infection?)
CASE-005,10.2,75,9.5,220,5.5,28,F,S-ANEMIA-MILD,Mild microcytic anemia
CASE-006,16.8,95,32.5,550,28.0,45,M,S-LEUKOCYTOSIS-SUSPECT,Leukocytosis suspicious for malignancy
CASE-007,9.0,105,7.2,95,4.0,65,F,S-THROMBOCYTOPENIA-MODERATE,Moderate thrombocytopenia
CASE-008,7.2,88,3.5,22,0.8,12,M,S-PANCYTOPENIA-SEVERE,Severe pancytopenia (aplastic anemia?)
CASE-009,11.5,78,8.0,180,4.5,18,F,S-IDA-PROBABLE,Iron deficiency anemia probable
CASE-010,13.0,88,8.2,120,4.2,52,M,S-THROMBOCYTOPENIA-MILD,Mild thrombocytopenia
```

### Example 2: Red List Critical Cases (8 syndromes × 5 cases = 40)

```csv
case_id,hb,mcv,wbc,plt,anc,age_years,sex,morphology.schistocytes,morphology.blasts,morphology.left_shift,expected_syndrome,notes
RL-NEUT-001,12.5,88,4.5,250,0.3,8,M,,,,,S-NEUTROPENIA-GRAVE,ANC < 0.5 (critical neutropenia)
RL-NEUT-002,14.0,90,3.2,180,0.2,5,F,,,,,S-NEUTROPENIA-GRAVE,ANC = 0.2 (severe)
RL-NEUT-003,13.2,85,5.8,220,0.45,12,M,,,,,S-NEUTROPENIA-GRAVE,ANC = 0.45 (borderline critical)
RL-NEUT-004,11.8,92,2.8,200,0.1,15,F,,,,,S-NEUTROPENIA-GRAVE,ANC = 0.1 (very severe)
RL-NEUT-005,10.5,88,4.0,190,0.35,6,M,,,,,S-NEUTROPENIA-GRAVE,ANC = 0.35 (critical)
RL-BLAST-001,8.5,95,45.0,85,,,M,,True,,,,S-BLASTIC-SYNDROME,Blasts present + WBC high (acute leukemia)
RL-BLAST-002,10.2,88,120.0,120,,,F,,True,,,,S-BLASTIC-SYNDROME,Blasts + WBC very high
RL-BLAST-003,9.5,90,28.5,95,,,M,,True,,,,S-BLASTIC-SYNDROME,Blasts detected (30% expected)
RL-BLAST-004,7.8,92,75.0,65,,,F,,True,,,,S-BLASTIC-SYNDROME,High blast count
RL-BLAST-005,11.0,88,52.0,110,,,M,,True,,,,S-BLASTIC-SYNDROME,Blasts present (ALL/AML)
RL-TMA-001,7.5,85,12.0,35,8.0,8,M,True,,,,S-TMA,Schistocytes + anemia + thrombocytopenia (TMA)
RL-TMA-002,6.8,88,9.5,22,6.5,5,F,True,,,,S-TMA,Classic TMA triad
RL-TMA-003,8.2,90,11.0,45,7.8,12,M,True,,,,S-TMA,HUS suspected
RL-TMA-004,7.0,92,10.5,28,7.2,6,F,True,,,,S-TMA,TTP suspected
RL-TMA-005,6.5,88,13.2,18,9.0,10,M,True,,,,S-TMA,Severe TMA
RL-PLT-001,12.5,88,8.5,8,4.0,35,M,,,,,S-PLT-CRITICA,Platelets < 10 (critical)
RL-PLT-002,14.0,90,7.2,5,4.5,28,F,,,,,S-PLT-CRITICA,Platelets = 5 (very severe)
RL-PLT-003,13.5,85,9.0,9,5.0,42,M,,,,,S-PLT-CRITICA,Platelets = 9 (borderline critical)
RL-PLT-004,11.8,92,8.0,3,3.8,38,F,,,,,S-PLT-CRITICA,Platelets = 3 (extremely low)
RL-PLT-005,10.5,88,7.5,7,4.2,45,M,,,,,S-PLT-CRITICA,Platelets = 7 (critical)
RL-ANEM-001,4.8,85,8.0,220,4.5,8,M,,,,,S-ANEMIA-GRAVE,Hb < 5.0 (life-threatening)
RL-ANEM-002,4.5,88,7.5,200,4.0,5,F,,,,,S-ANEMIA-GRAVE,Hb = 4.5 (critical)
RL-ANEM-003,4.9,90,8.2,180,4.8,12,M,,,,,S-ANEMIA-GRAVE,Hb = 4.9 (borderline critical)
RL-ANEM-004,4.2,92,7.8,210,4.2,6,F,,,,,S-ANEMIA-GRAVE,Hb = 4.2 (very severe)
RL-ANEM-005,4.7,88,8.5,195,4.5,10,M,,,,,S-ANEMIA-GRAVE,Hb = 4.7 (critical)
RL-LEUK-001,13.5,88,45.0,250,38.0,8,M,,,True,,S-NEUTROFILIA-LEFTSHIFT-CRIT,Neutrophilia + left shift (sepsis/leukemia)
RL-LEUK-002,14.0,90,55.0,220,45.0,5,F,,,True,,S-NEUTROFILIA-LEFTSHIFT-CRIT,Very high ANC + left shift
RL-LEUK-003,12.8,85,38.5,200,32.0,12,M,,,True,,S-NEUTROFILIA-LEFTSHIFT-CRIT,Left shift critical
RL-LEUK-004,15.2,92,62.0,240,50.0,6,F,,,True,,S-NEUTROFILIA-LEFTSHIFT-CRIT,Extreme leukocytosis
RL-LEUK-005,13.0,88,42.0,210,35.0,10,M,,,True,,S-NEUTROFILIA-LEFTSHIFT-CRIT,ANC > 30 + left shift
RL-THRO-001,14.5,88,8.5,1850,4.5,45,M,,,,,S-THROMBOCITOSE-CRIT,Platelets > 1800 (critical thrombocytosis)
RL-THRO-002,15.0,90,9.0,1920,5.0,52,F,,,,,S-THROMBOCITOSE-CRIT,Platelets = 1920 (very high)
RL-THRO-003,13.8,85,8.0,1880,4.8,38,M,,,,,S-THROMBOCITOSE-CRIT,Platelets = 1880 (MPN?)
RL-THRO-004,14.2,92,7.5,1950,4.2,48,F,,,,,S-THROMBOCITOSE-CRIT,Platelets = 1950 (extreme)
RL-THRO-005,15.5,88,8.8,1900,5.2,55,M,,,,,S-THROMBOCITOSE-CRIT,Platelets = 1900 (critical)
RL-CIVD-001,9.5,88,15.0,45,12.0,42,M,True,,,,,S-CIVD,CIVD suspected (schistocytes + thrombocytopenia + WBC high)
RL-CIVD-002,8.8,90,18.5,38,14.0,38,F,True,,,,,S-CIVD,CIVD classic presentation
RL-CIVD-003,10.2,85,12.5,52,10.5,50,M,True,,,,,S-CIVD,CIVD (sepsis-related?)
RL-CIVD-004,9.0,92,16.8,42,13.5,45,F,True,,,,,S-CIVD,CIVD with hemolysis
RL-CIVD-005,8.5,88,14.2,48,11.8,55,M,True,,,,,S-CIVD,CIVD severe
```

### Example 3: Edge Cases

```csv
case_id,hb,mcv,wbc,plt,anc,age_years,sex,expected_syndrome,notes
EDGE-001,0.5,88,8.5,250,4.0,35,M,S-REVIEW-SAMPLE,Impossible Hb (pre-analytical error)
EDGE-002,25.0,88,8.5,250,4.0,35,M,S-POLYCYTHEMIA-VERA,Extreme Hb high
EDGE-003,12.5,49,8.5,250,4.0,35,M,S-REVIEW-SAMPLE,MCV out of range
EDGE-004,12.5,151,8.5,250,4.0,35,M,S-REVIEW-SAMPLE,MCV out of range
EDGE-005,12.5,88,0.1,250,0.05,35,M,S-NEUTROPENIA-GRAVE,Extreme leukopenia
EDGE-006,12.5,88,201.0,250,180.0,35,M,S-REVIEW-SAMPLE,WBC out of range
EDGE-007,12.5,88,8.5,2100,4.0,35,M,S-REVIEW-SAMPLE,Platelets out of range
EDGE-008,12.5,88,8.5,,,35,M,S-MISSING-PLT,Missing platelet count
EDGE-009,12.5,88,8.5,250,,35,M,S-MISSING-ANC,Missing ANC
EDGE-010,12.5,88,8.5,250,4.0,0.5,M,S-NEONATAL,Neonatal case (age < 1 year)
```

---

## Missing Data Handling

### Semantics

- **Empty cell**: `None` (unknown/not measured)
- **`0`**: Explicitly zero (e.g., ANC = 0 in agranulocytosis)
- **`NaN`**: Not allowed (use empty cell)

### Example

```csv
case_id,hb,mcv,wbc,plt,anc,ferritin,jak2_pos,expected_syndrome
MISSING-001,8.5,75,8.0,220,,12.0,True,S-IDA-CONFIRMED
MISSING-002,8.5,75,8.0,220,,,True,S-IDA-PROBABLE
```

Row 1: ANC not measured, ferritin = 12, JAK2 positive
Row 2: ANC not measured, ferritin not measured, JAK2 positive

---

## Morphology Tokens Format

### Option 1: Separate Columns (Recommended)

```csv
case_id,hb,mcv,wbc,plt,morphology.schistocytes,morphology.blasts,morphology.left_shift,expected_syndrome
MORPH-001,7.5,85,12.0,35,True,False,False,S-TMA
MORPH-002,9.0,88,45.0,85,False,True,True,S-BLASTIC-SYNDROME
```

### Option 2: JSON String (Advanced)

```csv
case_id,hb,mcv,wbc,plt,morphology,expected_syndrome
MORPH-001,7.5,85,12.0,35,"{""schistocytes"": true, ""blasts"": false}",S-TMA
```

**Recommendation:** Use Option 1 (separate columns) for simplicity.

---

## Expected Syndrome Format

### Single Syndrome

```csv
expected_syndrome
S-NORMAL
S-ANEMIA-GRAVE
S-PLT-CRITICA
```

### Multiple Syndromes

Use `,` or `+` as separator (both accepted):

```csv
expected_syndrome
S-PLT-CRITICA,S-NEUTROPENIA-GRAVE
S-PLT-CRITICA+S-ANEMIA-GRAVE
S-TMA,S-ANEMIA-GRAVE,S-PLT-CRITICA
```

**Processing:** Split by `,` or `+`, strip whitespace, compare sets.

---

## Template CSV

Download ready-to-use template:

**File:** `test_cases_template.csv`

```csv
case_id,hb,mcv,wbc,plt,anc,age_years,sex,expected_syndrome,notes
CASE-001,,,,,,,,,
CASE-002,,,,,,,,,
CASE-003,,,,,,,,,
```

**Instructions:**
1. Fill in at least `hb`, `mcv`, `wbc` (required)
2. Add `plt`, `anc` for better analysis
3. Add `age_years`, `sex` for age-specific rules
4. Add `expected_syndrome` for validation
5. Add `notes` for documentation

---

## Validation Errors

### Common Errors

1. **Missing required fields:**
   ```
   ERROR: Row 5 missing required field 'hb'
   ```

2. **Out of range:**
   ```
   ERROR: Row 3 field 'hb' value 30.0 exceeds max 25.0
   ```

3. **Invalid sex:**
   ```
   ERROR: Row 7 field 'sex' value 'X' not in [M, F, U]
   ```

4. **Invalid boolean:**
   ```
   ERROR: Row 10 field 'jak2_pos' value 'YES' not boolean (use True/False)
   ```

### Error Handling Modes

**Strict Mode (default):**
- Stop on first error
- Report error details
- Exit with error code

**Lenient Mode:**
- Skip invalid rows
- Continue processing
- Report all errors at end

---

## Performance Considerations

### Batch Size Recommendations

| Rows | Method | Est. Time |
|------|--------|-----------|
| 1-10 | Script (sequential POST) | <1s |
| 10-100 | Script (sequential POST) | <10s |
| 100-1000 | Script (parallel POST) | <30s |
| 1000+ | Batch endpoint (future) | <60s |

**Note:** Current `/analyze` endpoint processes cases sequentially. For >100 cases, use batch endpoint (when available) or parallel script.

---

## Best Practices

1. **Always include `case_id`** for traceability
2. **Use descriptive IDs** (e.g., `RL-NEUT-001` for Red List neutropenia case 1)
3. **Document edge cases** in `notes` column
4. **Validate CSV** before testing (use schema validator)
5. **Start small** (10 cases) before scaling to 100+
6. **Review failures** manually (don't trust automation blindly)

---

## References

- API Schema: `src/hemodoctor/models/cbc.py` (54 fields)
- YAML Schema: `config/01_schema_hybrid.yaml` v2.3.1
- FastAPI Docs: http://localhost:8000/docs (after starting server)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-10-23 | Initial specification |

---

**End of CSV Format Specification**
