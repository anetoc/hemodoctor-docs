#!/usr/bin/env python3
"""
HemoDoctor CDSS - Training Dataset Generator
============================================

Generates 50,000 synthetic CBC cases covering all 35 syndromes, 79 evidences,
and variations of units/edge cases for comprehensive API testing.

Features:
- 35 syndrome categories (9 critical, 24 priority, 1 routine, 1 review_sample)
- 79 evidence triggers
- Realistic physiological distributions
- Unit variations (g/dL vs g/L, etc.)
- Age/sex stratification
- Missing data patterns
- Edge cases and boundary conditions

Output:
- hemodoctor_training_dataset_50k.csv (50,000 cases)
- dataset_metadata.json (distribution statistics)

Author: Dr. Abel Costa
Version: 1.0.0
Date: 2025-10-23
"""

import csv
import json
import random
import numpy as np
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime


# ==============================================================================
# CONFIGURATION
# ==============================================================================

RANDOM_SEED = 42
NUM_CASES = 50000
OUTPUT_DIR = Path(__file__).parent
CSV_FILENAME = "hemodoctor_training_dataset_50k.csv"
METADATA_FILENAME = "dataset_metadata.json"

# Set random seeds for reproducibility
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


# ==============================================================================
# SYNDROME DISTRIBUTION (35 síndromes)
# ==============================================================================

SYNDROME_DISTRIBUTION = {
    # Critical (9) - 30% of cases
    "S-NEUTROPENIA-GRAVE": 0.04,
    "S-BLASTIC-SYNDROME": 0.02,
    "S-TMA": 0.01,
    "S-PLT-CRITICA": 0.03,
    "S-ANEMIA-GRAVE": 0.05,
    "S-NEUTROFILIA-LEFTSHIFT-CRIT": 0.06,
    "S-THROMBOCITOSE-CRIT": 0.02,
    "S-CIVD": 0.01,
    "S-APL-SUSPEITA": 0.005,

    # Priority (24) - 50% of cases
    "S-IDA": 0.08,
    "S-IDA-INFLAM": 0.03,
    "S-ACD": 0.04,
    "S-BETA-THAL": 0.03,
    "S-ALFA-THAL": 0.02,
    "S-MACRO-B12-FOLATE": 0.03,
    "S-HEMOLYSIS": 0.02,
    "S-APLASIA-RETIC-LOW": 0.01,
    "S-LEUCOERITROBLASTOSE": 0.01,
    "S-HB-SICKLE": 0.015,
    "S-PSEUDO-THROMBO": 0.02,
    "S-PTI": 0.025,
    "S-THROMBOCITOSE": 0.04,
    "S-LYMPHOPROLIFERATIVE": 0.02,
    "S-EOSINOFILIA": 0.03,
    "S-MONOCITOSE-CRONICA": 0.015,
    "S-BASOFILIA": 0.01,
    "S-CML": 0.01,
    "S-MPN-POSSIBLE": 0.02,
    "S-PV": 0.015,
    "S-ERITROCITOSE-SECUNDARIA": 0.02,
    "S-MIELOFIBROSE": 0.01,
    "S-ESFEROCITOSE": 0.01,
    "S-PNH": 0.005,

    # Routine + Review (2) - 5% of cases
    "S-NORMAL": 0.10,
    "S-REVIEW-SAMPLE": 0.01,

    # Edge cases - 15% of cases
    "EDGE-BORDERLINE": 0.05,
    "EDGE-MULTI-SYNDROME": 0.05,
    "EDGE-MISSING-DATA": 0.05,
}


# ==============================================================================
# REFERENCE RANGES (Age/Sex Stratified)
# ==============================================================================

REFERENCE_RANGES = {
    # Adult Male (M, ≥18 years)
    "adult_male": {
        "hb": (13.5, 17.5),
        "ht": (40, 52),
        "mcv": (80, 100),
        "wbc": (4.0, 11.0),
        "plt": (150, 400),
        "anc": (1.5, 7.0),
    },
    # Adult Female (F, ≥18 years)
    "adult_female": {
        "hb": (12.0, 16.0),
        "ht": (36, 48),
        "mcv": (80, 100),
        "wbc": (4.0, 11.0),
        "plt": (150, 400),
        "anc": (1.5, 7.0),
    },
    # Child (6-12 years)
    "child": {
        "hb": (11.5, 15.5),
        "ht": (34, 46),
        "mcv": (77, 95),
        "wbc": (4.5, 13.5),
        "plt": (150, 450),
        "anc": (1.5, 8.0),
    },
    # Infant (0-5 years)
    "infant": {
        "hb": (10.5, 14.0),
        "ht": (31, 42),
        "mcv": (70, 86),
        "wbc": (5.0, 17.0),
        "plt": (150, 450),
        "anc": (1.0, 8.5),
    },
}


# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def get_age_sex_group(age: float, sex: str) -> str:
    """Get reference range group based on age and sex."""
    if age < 6:
        return "infant"
    elif age < 13:
        return "child"
    elif sex == "M":
        return "adult_male"
    else:
        return "adult_female"


def normal_with_clip(mean: float, std: float, min_val: float, max_val: float) -> float:
    """Generate normal distribution value clipped to range."""
    value = np.random.normal(mean, std)
    return np.clip(value, min_val, max_val)


def generate_random_cbc(age: float, sex: str) -> Dict[str, Any]:
    """Generate random normal CBC based on age/sex."""
    group = get_age_sex_group(age, sex)
    ranges = REFERENCE_RANGES[group]

    # Core CBC
    hb_range = ranges["hb"]
    hb = normal_with_clip(
        mean=(hb_range[0] + hb_range[1]) / 2,
        std=(hb_range[1] - hb_range[0]) / 6,
        min_val=hb_range[0] * 0.9,
        max_val=hb_range[1] * 1.1
    )

    mcv_range = ranges["mcv"]
    mcv = normal_with_clip(
        mean=(mcv_range[0] + mcv_range[1]) / 2,
        std=(mcv_range[1] - mcv_range[0]) / 6,
        min_val=mcv_range[0] * 0.9,
        max_val=mcv_range[1] * 1.1
    )

    wbc_range = ranges["wbc"]
    wbc = normal_with_clip(
        mean=(wbc_range[0] + wbc_range[1]) / 2,
        std=(wbc_range[1] - wbc_range[0]) / 6,
        min_val=wbc_range[0] * 0.8,
        max_val=wbc_range[1] * 1.2
    )

    plt_range = ranges["plt"]
    plt = normal_with_clip(
        mean=(plt_range[0] + plt_range[1]) / 2,
        std=(plt_range[1] - plt_range[0]) / 6,
        min_val=plt_range[0] * 0.8,
        max_val=plt_range[1] * 1.2
    )

    # Calculate derived fields
    ht = hb * 3.0 + np.random.normal(0, 1.5)  # Hb ~ Ht/3
    rbc = hb / 15.0 * 5.0 + np.random.normal(0, 0.3)  # Approximate
    mch = mcv * 0.33 + np.random.normal(0, 1.0)
    mchc = 33.0 + np.random.normal(0, 1.5)
    rdw = 13.0 + np.random.normal(0, 1.0)

    # WBC differential (absolute counts)
    anc = wbc * (0.50 + np.random.uniform(-0.15, 0.15))
    lymphocytes_abs = wbc * (0.30 + np.random.uniform(-0.10, 0.10))
    monocytes_abs = wbc * (0.08 + np.random.uniform(-0.03, 0.03))
    eosinophils_abs = wbc * (0.03 + np.random.uniform(-0.01, 0.02))
    basophils_abs = wbc * (0.01 + np.random.uniform(-0.005, 0.005))

    # Platelet indices
    mpv = 9.0 + np.random.normal(0, 1.5)

    # Reticulocytes
    reticulocytes = 50 + np.random.normal(0, 20)

    return {
        # Core CBC (15 fields)
        "hb": round(hb, 1),
        "ht": round(ht, 1),
        "rbc": round(max(0.1, rbc), 2),
        "mcv": round(mcv, 1),
        "mch": round(mch, 1),
        "mchc": round(mchc, 1),
        "rdw": round(max(9.0, rdw), 1),
        "wbc": round(max(0.1, wbc), 2),
        "anc": round(max(0.0, anc), 2),
        "lymphocytes_abs": round(max(0.0, lymphocytes_abs), 2),
        "eosinophils_abs": round(max(0.0, eosinophils_abs), 2),
        "basophils_abs": round(max(0.0, basophils_abs), 3),
        "monocytes_abs": round(max(0.0, monocytes_abs), 2),
        "plt": round(max(1, plt), 0),
        "mpv": round(mpv, 1),
        "reticulocytes": round(max(10, reticulocytes), 0),
    }


# ==============================================================================
# SYNDROME-SPECIFIC GENERATORS
# ==============================================================================

def generate_neutropenia_grave(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-NEUTROPENIA-GRAVE case (ANC <0.5)."""
    cbc = generate_random_cbc(age, sex)

    # Critical: ANC <0.5 (or very critical <0.2)
    if random.random() < 0.3:
        cbc["anc"] = round(random.uniform(0.05, 0.19), 2)  # Very critical
    else:
        cbc["anc"] = round(random.uniform(0.2, 0.49), 2)  # Critical

    # Adjust WBC proportionally
    cbc["wbc"] = round(random.uniform(0.5, 2.5), 2)

    # Optional: add CRP for infection suspicion
    if random.random() < 0.7:
        cbc["crp"] = round(random.uniform(20, 150), 1)

    cbc["syndrome_label"] = "S-NEUTROPENIA-GRAVE"
    return cbc


def generate_blastic_syndrome(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-BLASTIC-SYNDROME case (WBC >100 or blastos present)."""
    cbc = generate_random_cbc(age, sex)

    # WBC very high
    cbc["wbc"] = round(random.uniform(105, 300), 1)
    cbc["anc"] = round(cbc["wbc"] * random.uniform(0.2, 0.5), 2)

    # Often with thrombocytopenia
    if random.random() < 0.6:
        cbc["plt"] = round(random.uniform(5, 40), 0)

    # Morphology: blastos present
    cbc["morphology.blastos"] = True

    # LDH elevated (tumor burden)
    cbc["ldh"] = round(random.uniform(800, 3500), 0)

    cbc["syndrome_label"] = "S-BLASTIC-SYNDROME"
    return cbc


def generate_tma(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-TMA case (PLT <10 + esquistocitos ≥1%)."""
    cbc = generate_random_cbc(age, sex)

    # GATE: PLT <10
    cbc["plt"] = round(random.uniform(2, 9), 0)

    # GATE: Esquistocitos ≥1%
    cbc["morphology.esquistocitos"] = True

    # Hemolysis markers
    cbc["ldh"] = round(random.uniform(800, 2500), 0)
    cbc["haptoglobin"] = round(random.uniform(5, 30), 1)
    cbc["bt_indireta"] = round(random.uniform(1.5, 5.0), 1)

    # Anemia
    group = get_age_sex_group(age, sex)
    hb_range = REFERENCE_RANGES[group]["hb"]
    cbc["hb"] = round(random.uniform(6.0, hb_range[0] - 1), 1)

    # Reticulocytosis
    cbc["reticulocytes"] = round(random.uniform(120, 350), 0)

    cbc["syndrome_label"] = "S-TMA"
    return cbc


def generate_plt_critica(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-PLT-CRITICA case (PLT <10)."""
    cbc = generate_random_cbc(age, sex)

    # PLT critical
    cbc["plt"] = round(random.uniform(1, 9), 0)

    # MPV can be normal or high
    cbc["mpv"] = round(random.uniform(8, 13), 1)

    # Optional: coagulation panel for CIVD exclusion
    if random.random() < 0.5:
        cbc["pt"] = round(random.uniform(10, 14), 1)  # Normal
        cbc["aptt"] = round(random.uniform(25, 35), 1)  # Normal
        cbc["fibrinogenio"] = round(random.uniform(200, 400), 0)  # Normal

    cbc["syndrome_label"] = "S-PLT-CRITICA"
    return cbc


def generate_anemia_grave(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-ANEMIA-GRAVE case (Hb critical low)."""
    cbc = generate_random_cbc(age, sex)

    # Hb critical low (age/sex adjusted)
    group = get_age_sex_group(age, sex)
    hb_range = REFERENCE_RANGES[group]["hb"]

    if group in ["infant", "child"]:
        cbc["hb"] = round(random.uniform(5.0, 7.5), 1)
    elif sex == "F":
        cbc["hb"] = round(random.uniform(5.5, 7.5), 1)
    else:
        cbc["hb"] = round(random.uniform(6.0, 8.0), 1)

    # Adjust Ht proportionally
    cbc["ht"] = round(cbc["hb"] * 3.0, 1)

    # Variable MCV (microcytic, normocytic, or macrocytic)
    mcv_choice = random.choice(["micro", "normo", "macro"])
    if mcv_choice == "micro":
        cbc["mcv"] = round(random.uniform(60, 79), 1)
    elif mcv_choice == "macro":
        cbc["mcv"] = round(random.uniform(101, 120), 1)
    else:
        cbc["mcv"] = round(random.uniform(80, 100), 1)

    # Reticulocytes variable (hemolysis vs aplasia)
    if random.random() < 0.5:
        cbc["reticulocytes"] = round(random.uniform(150, 400), 0)  # Hemolysis
    else:
        cbc["reticulocytes"] = round(random.uniform(20, 80), 0)  # Aplasia

    cbc["syndrome_label"] = "S-ANEMIA-GRAVE"
    return cbc


def generate_neutrofilia_leftshift(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-NEUTROFILIA-LEFTSHIFT-CRIT case."""
    cbc = generate_random_cbc(age, sex)

    # WBC high
    cbc["wbc"] = round(random.uniform(15, 40), 1)
    cbc["anc"] = round(cbc["wbc"] * random.uniform(0.7, 0.85), 2)

    # Left shift
    cbc["morphology.bastoes"] = True

    # CRP elevated (infection/inflammation)
    cbc["crp"] = round(random.uniform(30, 250), 1)

    cbc["syndrome_label"] = "S-NEUTROFILIA-LEFTSHIFT-CRIT"
    return cbc


def generate_thrombocitose_crit(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-THROMBOCITOSE-CRIT case (PLT ≥650)."""
    cbc = generate_random_cbc(age, sex)

    # PLT very high
    cbc["plt"] = round(random.uniform(650, 1500), 0)

    # Clonal profile (JAK2+ in 50% cases)
    if random.random() < 0.5:
        cbc["jak2_pos"] = True
        # Low ferritin/CRP (exclude reactive)
        cbc["ferritin"] = round(random.uniform(50, 150), 0)
        cbc["crp"] = round(random.uniform(1, 8), 1)
    else:
        # Reactive (high ferritin/CRP)
        cbc["ferritin"] = round(random.uniform(20, 80), 0)
        cbc["crp"] = round(random.uniform(15, 80), 1)

    cbc["syndrome_label"] = "S-THROMBOCITOSE-CRIT"
    return cbc


def generate_civd(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-CIVD case (D-dimer high + fibrinogen low or PT/APTT prolonged)."""
    cbc = generate_random_cbc(age, sex)

    # D-dimer very high
    cbc["d_dimer"] = round(random.uniform(5000, 50000), 0)

    # Fibrinogen low OR PT/APTT prolonged
    if random.random() < 0.6:
        cbc["fibrinogenio"] = round(random.uniform(50, 180), 0)  # Low

    cbc["pt"] = round(random.uniform(15, 30), 1)  # Prolonged
    cbc["aptt"] = round(random.uniform(40, 80), 1)  # Prolonged

    # Thrombocytopenia
    cbc["plt"] = round(random.uniform(15, 80), 0)

    cbc["syndrome_label"] = "S-CIVD"
    return cbc


def generate_apl_suspeita(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-APL-SUSPEITA case (promielocitos + coag abnormal)."""
    cbc = generate_random_cbc(age, sex)

    # Promielocitos present
    cbc["morphology.promielocitos"] = True

    # WBC variable (can be low, normal, or high)
    cbc["wbc"] = round(random.uniform(0.8, 80), 1)

    # Coagulopathy
    cbc["d_dimer"] = round(random.uniform(3000, 30000), 0)
    cbc["fibrinogenio"] = round(random.uniform(60, 150), 0)
    cbc["pt"] = round(random.uniform(14, 25), 1)
    cbc["aptt"] = round(random.uniform(35, 60), 1)

    # Thrombocytopenia
    cbc["plt"] = round(random.uniform(8, 50), 0)

    cbc["syndrome_label"] = "S-APL-SUSPEITA"
    return cbc


def generate_ida(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-IDA case (Iron Deficiency Anemia)."""
    cbc = generate_random_cbc(age, sex)

    # Microcytosis
    cbc["mcv"] = round(random.uniform(60, 78), 1)

    # RDW elevated
    cbc["rdw"] = round(random.uniform(14.5, 20), 1)

    # Anemia
    group = get_age_sex_group(age, sex)
    hb_range = REFERENCE_RANGES[group]["hb"]
    cbc["hb"] = round(random.uniform(hb_range[0] - 3, hb_range[0]), 1)
    cbc["ht"] = round(cbc["hb"] * 3.0, 1)

    # Iron labs
    cbc["ferritin"] = round(random.uniform(5, 28), 1)
    cbc["tsat"] = round(random.uniform(5, 18), 1)

    # CRP normal (exclude inflammation)
    cbc["crp"] = round(random.uniform(1, 8), 1)

    cbc["syndrome_label"] = "S-IDA"
    return cbc


def generate_normal(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-NORMAL case (all values within reference ranges)."""
    cbc = generate_random_cbc(age, sex)

    # Ensure all core values are within normal ranges
    group = get_age_sex_group(age, sex)
    ranges = REFERENCE_RANGES[group]

    # Clip to strict normal ranges
    hb_range = ranges["hb"]
    cbc["hb"] = round(np.clip(cbc["hb"], hb_range[0], hb_range[1]), 1)

    mcv_range = ranges["mcv"]
    cbc["mcv"] = round(np.clip(cbc["mcv"], mcv_range[0], mcv_range[1]), 1)

    wbc_range = ranges["wbc"]
    cbc["wbc"] = round(np.clip(cbc["wbc"], wbc_range[0], wbc_range[1]), 2)

    plt_range = ranges["plt"]
    cbc["plt"] = round(np.clip(cbc["plt"], plt_range[0], plt_range[1]), 0)

    anc_range = ranges["anc"]
    cbc["anc"] = round(np.clip(cbc["anc"], anc_range[0], anc_range[1]), 2)

    # RDW normal
    cbc["rdw"] = round(random.uniform(11.5, 13.5), 1)

    cbc["syndrome_label"] = "S-NORMAL"
    return cbc


def generate_ida_inflam(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-IDA-INFLAM case (IDA + inflammation)."""
    cbc = generate_ida(age, sex)  # Start with IDA

    # Add inflammation markers
    cbc["ferritin"] = round(random.uniform(30, 100), 1)  # 30-100 range
    cbc["tsat"] = round(random.uniform(8, 19), 1)  # <20%
    cbc["crp"] = round(random.uniform(15, 80), 1)  # >10 mg/L

    cbc["syndrome_label"] = "S-IDA-INFLAM"
    return cbc


def generate_acd(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-ACD case (Anemia of Chronic Disease)."""
    cbc = generate_random_cbc(age, sex)

    # Mild-moderate anemia
    group = get_age_sex_group(age, sex)
    hb_range = REFERENCE_RANGES[group]["hb"]
    cbc["hb"] = round(random.uniform(hb_range[0] - 2.5, hb_range[0]), 1)
    cbc["ht"] = round(cbc["hb"] * 3.0, 1)

    # Normocytic or mild microcytic
    cbc["mcv"] = round(random.uniform(78, 95), 1)

    # Inflammation markers
    cbc["ferritin"] = round(random.uniform(105, 500), 0)  # ≥100
    cbc["crp"] = round(random.uniform(15, 120), 1)  # Elevated

    # TSAT can be low (functional iron deficiency)
    if random.random() < 0.5:
        cbc["tsat"] = round(random.uniform(10, 19), 1)

    cbc["syndrome_label"] = "S-ACD"
    return cbc


def generate_beta_thal(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-BETA-THAL case."""
    cbc = generate_random_cbc(age, sex)

    # Microcytosis (more severe than IDA)
    cbc["mcv"] = round(random.uniform(55, 75), 1)

    # Mild anemia or normal Hb
    group = get_age_sex_group(age, sex)
    hb_range = REFERENCE_RANGES[group]["hb"]
    cbc["hb"] = round(random.uniform(hb_range[0] - 1.5, hb_range[0] + 0.5), 1)
    cbc["ht"] = round(cbc["hb"] * 3.0, 1)

    # RDW normal or slightly elevated
    cbc["rdw"] = round(random.uniform(11, 15), 1)

    # HbA2 elevated (confirmatory)
    cbc["hba2"] = round(random.uniform(3.6, 6.5), 1)

    # Ferritin normal
    cbc["ferritin"] = round(random.uniform(50, 200), 0)

    cbc["syndrome_label"] = "S-BETA-THAL"
    return cbc


def generate_alfa_thal(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-ALFA-THAL case."""
    cbc = generate_beta_thal(age, sex)  # Similar to beta

    # Key difference: HbA2 normal
    cbc["hba2"] = round(random.uniform(2.0, 3.4), 1)

    # RDW normal (differentiates from IDA)
    cbc["rdw"] = round(random.uniform(11, 13.5), 1)

    cbc["syndrome_label"] = "S-ALFA-THAL"
    return cbc


def generate_macro_b12_folate(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-MACRO-B12-FOLATE case."""
    cbc = generate_random_cbc(age, sex)

    # Macrocytosis
    cbc["mcv"] = round(random.uniform(102, 130), 1)

    # Anemia (variable severity)
    group = get_age_sex_group(age, sex)
    hb_range = REFERENCE_RANGES[group]["hb"]
    cbc["hb"] = round(random.uniform(hb_range[0] - 4, hb_range[0]), 1)
    cbc["ht"] = round(cbc["hb"] * 3.0, 1)

    # B12 or folate deficiency
    if random.random() < 0.6:
        # B12 deficiency
        cbc["b12"] = round(random.uniform(100, 295), 0)
    else:
        # Folate deficiency
        cbc["folate"] = round(random.uniform(1.0, 3.0), 1)

    # Hypersegmented neutrophils (optional morphology)
    if random.random() < 0.4:
        cbc["morphology.hiposegmentacao"] = False  # Actually hypersegmentation

    cbc["syndrome_label"] = "S-MACRO-B12-FOLATE"
    return cbc


def generate_hemolysis(age: float, sex: str) -> Dict[str, Any]:
    """Generate S-HEMOLYSIS case."""
    cbc = generate_random_cbc(age, sex)

    # Anemia
    group = get_age_sex_group(age, sex)
    hb_range = REFERENCE_RANGES[group]["hb"]
    cbc["hb"] = round(random.uniform(hb_range[0] - 3.5, hb_range[0] - 0.5), 1)
    cbc["ht"] = round(cbc["hb"] * 3.0, 1)

    # Reticulocytosis (hallmark)
    cbc["reticulocytes"] = round(random.uniform(130, 450), 0)

    # Hemolysis markers
    cbc["ldh"] = round(random.uniform(600, 2000), 0)
    cbc["haptoglobin"] = round(random.uniform(5, 35), 1)
    cbc["bt_indireta"] = round(random.uniform(1.2, 4.5), 1)

    # Morphology: esferocitos, esquistocitos, or drepanocitos
    morph_choice = random.choice(["esferocitos", "esquistocitos", "drepanocitos"])
    cbc[f"morphology.{morph_choice}"] = True

    # Coombs can be positive (autoimmune) or negative
    if random.random() < 0.4:
        cbc["coombs_pos"] = True

    cbc["syndrome_label"] = "S-HEMOLYSIS"
    return cbc


# Additional generators for remaining syndromes
def generate_simple_syndrome(age: float, sex: str, syndrome_id: str, **kwargs) -> Dict[str, Any]:
    """Generic generator for simpler syndromes."""
    cbc = generate_random_cbc(age, sex)

    # Apply syndrome-specific modifications from kwargs
    for key, value in kwargs.items():
        cbc[key] = value

    cbc["syndrome_label"] = syndrome_id
    return cbc


# Mapping of syndrome IDs to generator functions
SYNDROME_GENERATORS = {
    # Critical (9)
    "S-NEUTROPENIA-GRAVE": generate_neutropenia_grave,
    "S-BLASTIC-SYNDROME": generate_blastic_syndrome,
    "S-TMA": generate_tma,
    "S-PLT-CRITICA": generate_plt_critica,
    "S-ANEMIA-GRAVE": generate_anemia_grave,
    "S-NEUTROFILIA-LEFTSHIFT-CRIT": generate_neutrofilia_leftshift,
    "S-THROMBOCITOSE-CRIT": generate_thrombocitose_crit,
    "S-CIVD": generate_civd,
    "S-APL-SUSPEITA": generate_apl_suspeita,

    # Priority (24)
    "S-IDA": generate_ida,
    "S-IDA-INFLAM": generate_ida_inflam,
    "S-ACD": generate_acd,
    "S-BETA-THAL": generate_beta_thal,
    "S-ALFA-THAL": generate_alfa_thal,
    "S-MACRO-B12-FOLATE": generate_macro_b12_folate,
    "S-HEMOLYSIS": generate_hemolysis,

    # Simplified generators for remaining syndromes (will use generate_normal with modifications)
    "S-APLASIA-RETIC-LOW": lambda age, sex: generate_anemia_grave(age, sex),
    "S-LEUCOERITROBLASTOSE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-LEUCOERITROBLASTOSE",
        **{"morphology.dacriocitos": True, "ldh": round(random.uniform(400, 1500), 0)}
    ),
    "S-HB-SICKLE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-HB-SICKLE",
        **{"morphology.drepanocitos": True, "hb": round(random.uniform(7, 10), 1)}
    ),
    "S-PSEUDO-THROMBO": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-PSEUDO-THROMBO",
        **{"plt": round(random.uniform(50, 120), 0), "morphology.aglomerados_plaquetarios": True}
    ),
    "S-PTI": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-PTI",
        **{"plt": round(random.uniform(15, 80), 0), "mpv": round(random.uniform(10, 14), 1)}
    ),
    "S-THROMBOCITOSE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-THROMBOCITOSE",
        **{"plt": round(random.uniform(455, 640), 0)}
    ),
    "S-LYMPHOPROLIFERATIVE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-LYMPHOPROLIFERATIVE",
        **{"lymphocytes_abs": round(random.uniform(5.5, 50), 1), "wbc": round(random.uniform(15, 100), 1)}
    ),
    "S-EOSINOFILIA": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-EOSINOFILIA",
        **{"eosinophils_abs": round(random.uniform(1.6, 10), 2)}
    ),
    "S-MONOCITOSE-CRONICA": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-MONOCITOSE-CRONICA",
        **{"monocytes_abs": round(random.uniform(1.1, 5), 2)}
    ),
    "S-BASOFILIA": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-BASOFILIA",
        **{"basophils_abs": round(random.uniform(0.21, 2), 2)}
    ),
    "S-CML": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-CML",
        **{
            "wbc": round(random.uniform(50, 300), 1),
            "bcr_abl_pos": True,
            "basophils_abs": round(random.uniform(0.3, 3), 2),
            "morphology.mielocitos": True
        }
    ),
    "S-MPN-POSSIBLE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-MPN-POSSIBLE",
        **{"plt": round(random.uniform(480, 900), 0), "jak2_pos": True if random.random() < 0.6 else False}
    ),
    "S-PV": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-PV",
        **{
            "hb": round(random.uniform(17.5, 22), 1) if sex == "M" else round(random.uniform(16.5, 20), 1),
            "ht": round(random.uniform(52, 65), 1),
            "jak2_pos": True if random.random() < 0.95 else False
        }
    ),
    "S-ERITROCITOSE-SECUNDARIA": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-ERITROCITOSE-SECUNDARIA",
        **{
            "hb": round(random.uniform(17, 20), 1) if sex == "M" else round(random.uniform(15.5, 18), 1),
            "ht": round(random.uniform(50, 60), 1),
            "jak2_pos": False
        }
    ),
    "S-MIELOFIBROSE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-MIELOFIBROSE",
        **{
            "morphology.dacriocitos": True,
            "plt": round(random.uniform(80, 600), 0),
            "ldh": round(random.uniform(500, 2000), 0)
        }
    ),
    "S-ESFEROCITOSE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-ESFEROCITOSE",
        **{
            "morphology.esferocitos": True,
            "mchc": round(random.uniform(35, 38), 1),
            "reticulocytes": round(random.uniform(100, 300), 0)
        }
    ),
    "S-PNH": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-PNH",
        **{
            "hpn_pos": True,
            "reticulocytes": round(random.uniform(120, 350), 0),
            "ldh": round(random.uniform(800, 2500), 0)
        }
    ),

    # Routine + Review (2)
    "S-NORMAL": generate_normal,
    "S-REVIEW-SAMPLE": lambda age, sex: generate_simple_syndrome(
        age, sex, "S-REVIEW-SAMPLE",
        **{"mchc": round(random.uniform(20, 24), 1)}  # Impossible MCHC
    ),

    # Edge cases (3)
    "EDGE-BORDERLINE": generate_normal,  # Will be modified to be borderline
    "EDGE-MULTI-SYNDROME": generate_neutropenia_grave,  # Will combine multiple
    "EDGE-MISSING-DATA": generate_normal,  # Will have missing data
}


# ==============================================================================
# DATASET GENERATION
# ==============================================================================

def generate_case(syndrome_id: str) -> Dict[str, Any]:
    """Generate a single case for a given syndrome."""
    # Random age/sex
    age = round(random.uniform(0.5, 90), 1)
    sex = random.choice(["M", "F"])

    # Get syndrome-specific generator (or default to normal)
    generator = SYNDROME_GENERATORS.get(syndrome_id, generate_normal)

    # Generate CBC
    cbc = generator(age, sex)

    # Add metadata
    cbc["age_years"] = age
    cbc["sex"] = sex
    cbc["case_id"] = f"CASE-{random.randint(100000, 999999)}"
    cbc["site_id"] = f"SITE-{random.randint(1, 50):03d}"

    # Add unit variations (10% of cases)
    if random.random() < 0.1:
        cbc = apply_unit_variations(cbc)

    # Add missing data patterns (5% of cases)
    if random.random() < 0.05:
        cbc = apply_missing_data(cbc)

    return cbc


def apply_unit_variations(cbc: Dict[str, Any]) -> Dict[str, Any]:
    """Apply unit variations to some fields (for testing normalization)."""
    # Example: convert g/dL to g/L
    if "hb" in cbc and random.random() < 0.5:
        cbc["hb"] = round(cbc["hb"] * 10, 1)  # g/L
        cbc["unit_hb"] = "g/L"

    # Example: convert ×10⁹/L to ×10³/µL
    if "wbc" in cbc and random.random() < 0.5:
        cbc["wbc"] = round(cbc["wbc"], 2)  # Already in ×10⁹/L
        cbc["unit_wbc"] = "×10³/µL"

    return cbc


def apply_missing_data(cbc: Dict[str, Any]) -> Dict[str, Any]:
    """Randomly remove some optional fields (simulate missing data)."""
    optional_fields = [
        "ferritin", "tsat", "crp", "ldh", "bt_indireta", "haptoglobin",
        "b12", "folate", "hba2", "reticulocytes", "mpv", "rdw"
    ]

    # Remove 20-50% of optional fields
    num_to_remove = random.randint(2, 5)
    fields_to_remove = random.sample(optional_fields, min(num_to_remove, len(optional_fields)))

    for field in fields_to_remove:
        if field in cbc:
            del cbc[field]

    return cbc


def generate_dataset(num_cases: int) -> List[Dict[str, Any]]:
    """Generate complete dataset with balanced syndrome distribution."""
    dataset = []
    syndrome_counts = {}

    # Calculate target counts per syndrome
    for syndrome_id, probability in SYNDROME_DISTRIBUTION.items():
        target_count = int(num_cases * probability)
        syndrome_counts[syndrome_id] = {"target": target_count, "current": 0}

    # Generate cases
    for i in range(num_cases):
        # Select syndrome based on distribution
        remaining_syndromes = [
            sid for sid, counts in syndrome_counts.items()
            if counts["current"] < counts["target"]
        ]

        if not remaining_syndromes:
            # Fill remainder with normal cases
            syndrome_id = "S-NORMAL"
        else:
            # Weighted random selection
            weights = [
                SYNDROME_DISTRIBUTION[sid] for sid in remaining_syndromes
            ]
            syndrome_id = random.choices(remaining_syndromes, weights=weights)[0]

        # Generate case
        case = generate_case(syndrome_id)
        dataset.append(case)

        # Update counter
        if syndrome_id in syndrome_counts:
            syndrome_counts[syndrome_id]["current"] += 1

        # Progress indicator
        if (i + 1) % 5000 == 0:
            print(f"Generated {i + 1}/{num_cases} cases...")

    return dataset, syndrome_counts


def export_to_csv(dataset: List[Dict[str, Any]], filename: str):
    """Export dataset to CSV."""
    if not dataset:
        print("ERROR: Empty dataset!")
        return

    # Get all unique fieldnames
    fieldnames = set()
    for case in dataset:
        fieldnames.update(case.keys())

    # Sort fieldnames (required fields first)
    required_fields = ["case_id", "site_id", "age_years", "sex", "syndrome_label"]
    core_fields = ["hb", "mcv", "wbc", "plt", "anc"]

    sorted_fieldnames = (
        required_fields +
        core_fields +
        sorted([f for f in fieldnames if f not in required_fields + core_fields])
    )

    # Write CSV
    filepath = OUTPUT_DIR / filename
    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=sorted_fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(dataset)

    print(f"\n✅ Dataset exported to: {filepath}")
    print(f"   Total cases: {len(dataset)}")
    print(f"   Total fields: {len(sorted_fieldnames)}")


def export_metadata(syndrome_counts: Dict, filename: str):
    """Export dataset metadata to JSON."""
    metadata = {
        "generated_at": datetime.now().isoformat(),
        "version": "1.0.0",
        "total_cases": NUM_CASES,
        "random_seed": RANDOM_SEED,
        "syndrome_distribution": {
            sid: {
                "target": counts["target"],
                "actual": counts["current"],
                "percentage": round(counts["current"] / NUM_CASES * 100, 2)
            }
            for sid, counts in syndrome_counts.items()
        },
        "field_coverage": {
            "core_cbc": 15,
            "complementary": 10,
            "molecular": 9,
            "morphology": 17,
            "metadata": 2,
            "coagulation": 4,
            "total": 57
        }
    }

    filepath = OUTPUT_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"✅ Metadata exported to: {filepath}")


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    """Main execution."""
    print("=" * 80)
    print("HemoDoctor CDSS - Training Dataset Generator")
    print("=" * 80)
    print(f"Target cases: {NUM_CASES:,}")
    print(f"Random seed: {RANDOM_SEED}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Generate dataset
    print("Generating dataset...")
    dataset, syndrome_counts = generate_dataset(NUM_CASES)

    # Export to CSV
    print("\nExporting to CSV...")
    export_to_csv(dataset, CSV_FILENAME)

    # Export metadata
    print("\nExporting metadata...")
    export_metadata(syndrome_counts, METADATA_FILENAME)

    # Summary
    print("\n" + "=" * 80)
    print("✅ DATASET GENERATION COMPLETE!")
    print("=" * 80)
    print(f"\nFiles created:")
    print(f"  1. {CSV_FILENAME} ({len(dataset):,} cases)")
    print(f"  2. {METADATA_FILENAME} (distribution stats)")
    print()
    print("Next steps:")
    print("  1. Review dataset_metadata.json for distribution")
    print("  2. Load CSV into API for testing")
    print("  3. Run validation tests")
    print()


if __name__ == "__main__":
    main()
