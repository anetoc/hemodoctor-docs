# Clinical Test Case Patterns Reference

## Syndrome Definitions & Expected Lab Patterns

### Critical Syndromes (8)

#### 1. S-NEUTROPENIA-GRAVE (Severe Neutropenia)
**Lab Pattern:**
- ANC: <0.5 (critical) or <0.2 (very critical)
- WBC: Usually 1.0-3.0
- Hb: Often normal
- PLT: Often normal
- CRP: May be elevated if infection

**Clinical Context:** Chemotherapy, autoimmune, drug-induced

---

#### 2. S-TMA (Thrombotic Microangiopathy)
**Lab Pattern:**
- PLT: <25 (critical thrombocytopenia)
- Schistocytes: Present (≥1%)
- Hb: 6.0-9.0 (hemolytic anemia)
- LDH: 500-2000 (hemolysis)
- Haptoglobin: <40 (consumed)
- Bilirubin indirect: >1.0

**Clinical Context:** TTP, HUS, HELLP, malignant hypertension

---

#### 3. S-BLASTIC-SYNDROME (Acute Leukemia)
**Lab Pattern:**
- WBC: >100 (or >50 with blasts)
- Blasts: Present
- Hb: 6.0-10.0 (anemia)
- PLT: 10-80 (thrombocytopenia)

**Clinical Context:** Acute leukemia (AML, ALL, APL)

---

#### 4. S-ANEMIA-GRAVE (Severe Anemia)
**Lab Pattern:**
- Hb: <6.5 (M) or <6.0 (F)
- MCV: Variable (depends on etiology)
- WBC: Often normal
- PLT: Often normal

**Clinical Context:** Severe blood loss, hemolysis, bone marrow failure

---

#### 5. S-PLT-CRITICA (Critical Thrombocytopenia)
**Lab Pattern:**
- PLT: <10
- Hb: Usually normal
- WBC: Usually normal
- MCV: Normal

**Clinical Context:** ITP, drug-induced, bone marrow failure

---

### Priority Syndromes (Selected Examples)

#### S-IDA (Iron Deficiency Anemia)
**Lab Pattern:**
- Hb: <13 (M) or <12 (F)
- MCV: <80 (microcytic)
- RDW: >14 (anisocytosis)
- Ferritin: <30
- TSAT: <20%
- PLT: May be elevated (200-450)

**Stages:**
- Classic: Ferritin 5-20, TSAT 5-15
- Borderline: Ferritin 20-30, TSAT 15-20
- Severe: Ferritin <10, TSAT <10

---

#### S-B12-DEFICIENCY (Vitamin B12 Deficiency)
**Lab Pattern:**
- Hb: 8.0-11.0
- MCV: >100 (macrocytic)
- RDW: >14
- WBC: May be low (3-6)
- PLT: May be low (100-200)
- B12: <300 pg/mL

**Clinical Context:** Pernicious anemia, malabsorption, vegan diet

---

#### S-BETA-THAL-TRAIT (Beta-Thalassemia Trait)
**Lab Pattern:**
- Hb: 10.5-13.0 (mild anemia)
- MCV: 60-72 (microcytic)
- RDW: Normal or slightly high (11-14)
- RBC: HIGH (5.5-7.0) - KEY FEATURE
- HbA2: >3.5% (elevated)
- Ferritin: Normal or high

**Distinguishing from IDA:**
- IDA: Low RBC, high RDW, low ferritin
- Thal trait: High RBC, normal RDW, normal/high ferritin

---

#### S-EOSINOPHILIA (Eosinophilia)
**Lab Pattern:**
- Eosinophils absolute: >1.5
- WBC: Often elevated (10-20)
- Hb: Normal
- PLT: Normal

**Severity:**
- Moderate: 1.5-3.0
- Severe: >3.0

**Clinical Context:** Parasites, allergies, drugs, eosinophilic disorders

---

### Normal/Routine

#### NORMAL (Normal CBC)
**Lab Pattern:**
- Hb: 13.5-16.0 (M) or 12.0-15.0 (F)
- MCV: 82-98
- RDW: 11.5-14.0
- WBC: 4.5-10.0
- PLT: 150-400

---

#### BORDERLINE-MICROCYTOSIS (Borderline MCV)
**Lab Pattern:**
- Hb: 12.5-14.0
- MCV: 78-82 (borderline low)
- RDW: 12-14
- WBC: Normal
- PLT: Normal

**Action:** Repeat CBC in 2-6 weeks, consider ferritin

---

## Data Generation Strategies

### 1. Red List Cases (FN=0 Required)
Generate 40+ cases per critical syndrome with:
- Extreme values (worst-case scenarios)
- Edge cases (borderline critical)
- Variants (with/without complications)

**Example:**
```python
# Generate 40 neutropenia cases
for i in range(40):
    case = generator.generate_severe_neutropenia("critical")
    # ANC will be 0.2-0.5, WBC 1-3
```

---

### 2. Validation Set (Balanced)
Distribution:
- 10% Critical syndromes
- 40% Priority syndromes
- 50% Normal/routine

**Example:**
```python
# Generate 500-case validation set
cases = generator.generate_validation_set(n_total=500)
# ~50 critical, ~200 priority, ~250 normal
```

---

### 3. Missing Data Cases
Simulate real-world incomplete lab panels:
- Remove 20-40% of complementary tests randomly
- Test missingness engine and proxy logic
- Test always-output behavior

**Example:**
```python
# Generate 50 cases with missing data
cases = generator.generate_missing_data_cases(n=50)
# Ferritin, TSAT, B12, CRP randomly missing
```

---

## Clinical Correlations

### Why High RBC in Thalassemia Trait?
- **Mechanism:** Ineffective erythropoiesis → bone marrow compensates by producing MORE (but smaller) RBCs
- **Lab:** High RBC count despite low Hb/MCV
- **Contrast IDA:** Low RBC count due to lack of iron substrate

### Why High RDW in IDA?
- **Mechanism:** Mixed population of microcytic (new) and normocytic (old) RBCs during iron depletion
- **Lab:** Anisocytosis (variable cell sizes)
- **Contrast Thal trait:** All cells uniformly small → normal RDW

### Why Schistocytes in TMA?
- **Mechanism:** Mechanical fragmentation of RBCs in microthrombi
- **Lab:** Helmet cells, fragmented cells on smear
- **Clinical:** Consumptive thrombocytopenia + hemolytic anemia

---

## Test Case Quality Checklist

- [ ] Ground truth syndrome clearly labeled
- [ ] Priority level assigned (critical/priority/routine)
- [ ] Lab values physiologically plausible
- [ ] Complementary tests consistent with syndrome
- [ ] Age/sex appropriate for syndrome
- [ ] Notes explain key features
- [ ] Case ID unique and traceable

---

## Export Formats

### JSON (Best for testing)
- Preserves null values
- Easy to parse
- Supports nested data

### CSV (Best for spreadsheets)
- Simple format
- Easy to view/edit in Excel
- Good for manual review

### YAML (Best for config)
- Human-readable
- Good for documentation
- Supports comments
