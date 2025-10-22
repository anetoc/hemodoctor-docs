#!/usr/bin/env python3
"""
Sprint 4: Red List Test Case Generator
Generate 270 critical cases (30 per syndrome) for FN=0 validation

9 Critical Syndromes:
1. S-NEUTROPENIA-GRAVE (ANC <0.5)
2. S-BLASTIC-SYNDROME (blasts present or WBC >100)
3. S-TMA (schistocytes + PLT <10)
4. S-PLT-CRITICA (PLT <10)
5. S-ANEMIA-GRAVE (Hb <6.5 M / <6.0 F)
6. S-NEUTROFILIA-LEFTSHIFT-CRIT (neutrophilia + left shift)
7. S-THROMBOCITOSE-CRIT (PLT ≥1000)
8. S-CIVD (DIC - ≥2 markers)
9. S-APL (APL pattern)
"""

import json
import random
from dataclasses import dataclass, asdict
from typing import Optional, List


@dataclass
class CBCTestCase:
    """Complete Blood Count test case with morphology"""
    # Core CBC
    hb: float
    ht: Optional[float] = None
    rbc: Optional[float] = None
    mcv: float = 90.0
    mch: Optional[float] = None
    mchc: Optional[float] = None
    rdw: float = 13.0
    wbc: float = 7.0
    neutrophils: Optional[float] = None  # Percentage
    lymphocytes: Optional[float] = None
    monocytes: Optional[float] = None
    eosinophils: Optional[float] = None
    basophils: Optional[float] = None
    anc: Optional[float] = None  # Absolute
    plt: float = 250.0
    mpv: Optional[float] = None
    reticulocytes: Optional[float] = None

    # Complementary tests
    ferritin: Optional[float] = None
    tsat: Optional[float] = None
    crp: Optional[float] = None
    ldh: Optional[float] = None
    bt_indireta: Optional[float] = None
    haptoglobin: Optional[float] = None
    b12: Optional[float] = None
    folate: Optional[float] = None
    hba2: Optional[float] = None

    # Coagulation (for CIVD)
    pt: Optional[float] = None
    aptt: Optional[float] = None
    fibrinogenio: Optional[float] = None
    d_dimer: Optional[float] = None

    # Morphology (structured as dict for nested access)
    morphology: Optional[dict] = None

    # Metadata
    age_years: float = 45.0
    sex: str = "M"
    case_id: str = "TEST-001"
    expected_syndrome: str = "NORMAL"
    expected_evidences: Optional[List[str]] = None
    expected_next_steps: Optional[List[str]] = None
    criticality: str = "routine"
    fn_allowed: bool = True
    notes: str = ""


class RedListGenerator:
    """Generate 270 critical cases for Sprint 4"""

    def __init__(self, seed: int = 42):
        random.seed(seed)
        self.case_counter = 0

    def _next_case_id(self, syndrome_prefix: str) -> str:
        """Generate sequential case ID"""
        self.case_counter += 1
        return f"RL-{self.case_counter:03d}-{syndrome_prefix}"

    # =========================================================================
    # 1. S-NEUTROPENIA-GRAVE (ANC <0.5)
    # =========================================================================

    def generate_neutropenia_grave(self) -> CBCTestCase:
        """Generate S-NEUTROPENIA-GRAVE case"""
        anc_level = random.choice(["critical", "very_critical"])

        if anc_level == "very_critical":
            anc = random.uniform(0.05, 0.19)  # <0.2
        else:
            anc = random.uniform(0.2, 0.49)  # 0.2-0.5

        wbc = random.uniform(0.5, 3.0)
        neutrophils = (anc / wbc) * 100 if wbc > 0 else 10.0

        hb = random.uniform(10.0, 14.0)
        mcv = random.uniform(85, 95)
        plt = random.uniform(100, 350)

        crp = random.uniform(15, 150) if random.random() > 0.3 else None

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, anc=anc, neutrophils=neutrophils,
            plt=plt, crp=crp,
            age_years=random.uniform(20, 75),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("NEU-GRAVE"),
            expected_syndrome="S-NEUTROPENIA-GRAVE",
            expected_evidences=["E-ANC-CRIT"] if anc >= 0.2 else ["E-ANC-VCRIT"],
            expected_next_steps=["G-CSF", "Hospitalization", "Blood cultures"],
            criticality="critical",
            fn_allowed=False,
            notes=f"Severe neutropenia ANC={anc:.2f} ({anc_level})"
        )

    # =========================================================================
    # 2. S-BLASTIC-SYNDROME (blasts present or WBC >100)
    # =========================================================================

    def generate_blastic_syndrome(self) -> CBCTestCase:
        """Generate S-BLASTIC-SYNDROME case"""
        variant = random.choice(["very_high_wbc", "high_wbc_blasts", "moderate_wbc_blasts"])

        if variant == "very_high_wbc":
            wbc = random.uniform(100, 250)
            blastos = True
        elif variant == "high_wbc_blasts":
            wbc = random.uniform(50, 99)
            blastos = True
        else:
            wbc = random.uniform(20, 50)
            blastos = True

        hb = random.uniform(6.0, 10.0)
        plt = random.uniform(10, 80)
        mcv = random.uniform(85, 100)
        anc = wbc * random.uniform(0.3, 0.6)

        morphology = {"blastos": blastos}

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, anc=anc, plt=plt,
            morphology=morphology,
            age_years=random.uniform(40, 80),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("BLASTIC"),
            expected_syndrome="S-BLASTIC-SYNDROME",
            expected_evidences=["E-WBC-VERY-HIGH", "E-BLASTS-PRESENT"] if wbc > 100 else ["E-BLASTS-PRESENT"],
            expected_next_steps=["Immunophenotyping", "BCR-ABL", "Bone marrow"],
            criticality="critical",
            fn_allowed=False,
            notes=f"Blastic syndrome: WBC={wbc:.0f}, blasts present"
        )

    # =========================================================================
    # 3. S-TMA (schistocytes + PLT <10)
    # =========================================================================

    def generate_tma(self) -> CBCTestCase:
        """Generate S-TMA case (GATE RÍGIDO: PLT <10 + schistocytes)"""
        plt = random.uniform(2, 9.9)  # <10 CRITICAL
        hb = random.uniform(6.0, 9.0)  # Hemolytic anemia
        mcv = random.uniform(80, 95)
        wbc = random.uniform(5, 15)

        # Hemolysis markers
        with_hemolysis = random.random() > 0.2
        ldh = random.uniform(500, 2500) if with_hemolysis else random.uniform(200, 499)
        bt_indireta = random.uniform(1.5, 4.5) if with_hemolysis else None
        haptoglobin = random.uniform(5, 30) if with_hemolysis else None

        # CRITICAL: schistocytes MUST be present
        morphology = {"esquistocitos": True}

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            ldh=ldh, bt_indireta=bt_indireta, haptoglobin=haptoglobin,
            morphology=morphology,
            age_years=random.uniform(20, 70),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("TMA"),
            expected_syndrome="S-TMA",
            expected_evidences=["E-PLT-CRIT-LOW", "E-SCHISTOCYTES-GE1PCT", "E-LDH-HIGH"],
            expected_next_steps=["ADAMTS13", "Plasmapheresis", "Nephrology referral"],
            criticality="critical",
            fn_allowed=False,
            notes=f"TMA: PLT={plt:.1f}, schistocytes ≥1%, hemolysis={with_hemolysis}"
        )

    # =========================================================================
    # 4. S-PLT-CRITICA (PLT <10)
    # =========================================================================

    def generate_plt_critica(self) -> CBCTestCase:
        """Generate S-PLT-CRITICA case"""
        plt = random.uniform(1, 9.9)  # <10
        hb = random.uniform(11, 15)  # Normal Hb (isolate thrombocytopenia)
        mcv = random.uniform(80, 95)
        wbc = random.uniform(4, 10)
        mpv = random.uniform(8, 12)

        # Exclude TMA (no schistocytes)
        morphology = {"esquistocitos": False, "aglomerados_plaquetarios": False}

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt, mpv=mpv,
            morphology=morphology,
            age_years=random.uniform(20, 75),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("PLT-CRIT"),
            expected_syndrome="S-PLT-CRITICA",
            expected_evidences=["E-PLT-CRIT-LOW"],
            expected_next_steps=["Platelet transfusion", "TP/APTT", "Exclude CIVD"],
            criticality="critical",
            fn_allowed=False,
            notes=f"Critical thrombocytopenia: PLT={plt:.1f}"
        )

    # =========================================================================
    # 5. S-ANEMIA-GRAVE (Hb <6.5 M / <6.0 F)
    # =========================================================================

    def generate_anemia_grave(self) -> CBCTestCase:
        """Generate S-ANEMIA-GRAVE case"""
        sex = random.choice(["M", "F"])

        if sex == "F":
            hb = random.uniform(4.5, 5.99)
        else:  # M
            hb = random.uniform(5.0, 6.49)

        mcv = random.uniform(70, 110)  # Variable (IDA, B12, hemolysis)
        wbc = random.uniform(4, 10)
        plt = random.uniform(150, 400)
        reticulocytes = random.uniform(20, 150) if random.random() > 0.5 else None

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt, reticulocytes=reticulocytes,
            age_years=random.uniform(20, 80),
            sex=sex,
            case_id=self._next_case_id("ANEMIA-GRAVE"),
            expected_syndrome="S-ANEMIA-GRAVE",
            expected_evidences=["E-HB-CRIT-LOW"],
            expected_next_steps=["Transfusion", "Reticulocytes", "LDH/haptoglobin"],
            criticality="critical",
            fn_allowed=False,
            notes=f"Severe anemia: Hb={hb:.1f} g/dL ({sex})"
        )

    # =========================================================================
    # 6. S-NEUTROFILIA-LEFTSHIFT-CRIT (neutrophilia + left shift)
    # =========================================================================

    def generate_neutrofilia_leftshift_crit(self) -> CBCTestCase:
        """Generate S-NEUTROFILIA-LEFTSHIFT-CRIT case"""
        wbc = random.uniform(15, 50)
        neutrophils = random.uniform(70, 90)
        anc = wbc * (neutrophils / 100)

        hb = random.uniform(11, 15)
        mcv = random.uniform(80, 95)
        plt = random.uniform(200, 500)

        crp = random.uniform(50, 300)  # Inflammatory

        # Left shift markers
        morphology = {
            "bastoes": True,  # Band neutrophils
            "metamielocitos": random.choice([True, False]),
            "mielocitos": random.choice([True, False])
        }

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, anc=anc, neutrophils=neutrophils,
            plt=plt, crp=crp,
            morphology=morphology,
            age_years=random.uniform(30, 75),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("NEUTRO-LEFT"),
            expected_syndrome="S-NEUTROFILIA-LEFTSHIFT-CRIT",
            expected_evidences=["E-WBC-HIGH", "E-ANC-HIGH", "E-LEFT-SHIFT", "E-CRP-HIGH"],
            expected_next_steps=["Blood cultures", "Chest X-ray", "Rule out sepsis"],
            criticality="critical",
            fn_allowed=False,
            notes=f"Neutrophilia + left shift: WBC={wbc:.1f}, ANC={anc:.1f}"
        )

    # =========================================================================
    # 7. S-THROMBOCITOSE-CRIT (PLT ≥1000)
    # =========================================================================

    def generate_thrombocitose_crit(self) -> CBCTestCase:
        """Generate S-THROMBOCITOSE-CRIT case"""
        plt = random.uniform(1000, 2000)  # ≥1000

        hb = random.uniform(12, 16)
        mcv = random.uniform(80, 95)
        wbc = random.uniform(8, 20)

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            age_years=random.uniform(40, 80),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("THROMB-CRIT"),
            expected_syndrome="S-THROMBOCITOSE-CRIT",
            expected_evidences=["E-PLT-VERY-HIGH"],
            expected_next_steps=["JAK2 V617F", "BCR-ABL", "Bone marrow"],
            criticality="critical",
            fn_allowed=False,
            notes=f"Critical thrombocytosis: PLT={plt:.0f}"
        )

    # =========================================================================
    # 8. S-CIVD (DIC - ≥2 markers)
    # =========================================================================

    def generate_civd(self) -> CBCTestCase:
        """Generate S-CIVD (DIC) case"""
        plt = random.uniform(20, 80)  # Thrombocytopenia
        hb = random.uniform(7, 10)  # Anemia
        mcv = random.uniform(85, 95)
        wbc = random.uniform(3, 15)

        # DIC markers (≥2 required)
        pt = random.uniform(16, 30)  # Prolonged (normal 11-15)
        aptt = random.uniform(40, 80)  # Prolonged (normal 25-35)
        fibrinogenio = random.uniform(50, 150)  # Low (normal 200-400)
        d_dimer = random.uniform(2000, 10000)  # Very high (normal <500)

        # Schistocytes may be present
        morphology = {"esquistocitos": random.choice([True, False])}

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            pt=pt, aptt=aptt, fibrinogenio=fibrinogenio, d_dimer=d_dimer,
            morphology=morphology,
            age_years=random.uniform(40, 80),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("CIVD"),
            expected_syndrome="S-CIVD",
            expected_evidences=["E-D-DIMER-HIGH", "E-FIBRINOGEN-LOW", "E-PT-PROLONGED", "E-APTT-PROLONGED"],
            expected_next_steps=["ICU admission", "Treat underlying cause", "Supportive care"],
            criticality="critical",
            fn_allowed=False,
            notes=f"DIC: PLT={plt:.0f}, D-dimer={d_dimer:.0f}, Fib={fibrinogenio:.0f}"
        )

    # =========================================================================
    # 9. S-APL (Acute Promyelocytic Leukemia pattern)
    # =========================================================================

    def generate_apl(self) -> CBCTestCase:
        """Generate S-APL case"""
        wbc = random.uniform(2, 50)  # Variable
        hb = random.uniform(6, 10)  # Anemia
        plt = random.uniform(5, 40)  # Thrombocytopenia
        mcv = random.uniform(85, 95)

        # APL pattern: promyelocytes + DIC markers
        morphology = {
            "promielocitos": True,
            "bastonetes_auer": True,
            "blastos": True
        }

        # DIC pattern (common in APL)
        pt = random.uniform(16, 25)
        aptt = random.uniform(40, 70)
        fibrinogenio = random.uniform(80, 150)
        d_dimer = random.uniform(3000, 15000)

        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            pt=pt, aptt=aptt, fibrinogenio=fibrinogenio, d_dimer=d_dimer,
            morphology=morphology,
            age_years=random.uniform(20, 60),
            sex=random.choice(["M", "F"]),
            case_id=self._next_case_id("APL"),
            expected_syndrome="S-APL",
            expected_evidences=["E-BLASTS-PRESENT", "E-D-DIMER-HIGH", "E-PLT-CRIT-LOW"],
            expected_next_steps=["ATRA immediately", "PML-RARA", "ICU admission"],
            criticality="critical",
            fn_allowed=False,
            notes=f"APL pattern: promyelocytes + DIC, WBC={wbc:.1f}"
        )

    # =========================================================================
    # BATCH GENERATION
    # =========================================================================

    def generate_all_red_list(self, n_per_syndrome: int = 30) -> List[CBCTestCase]:
        """Generate 270 cases (30 per syndrome)"""
        cases = []

        print(f"\n🧪 Generating Red List Cases ({n_per_syndrome} per syndrome)...\n")

        # 1. S-NEUTROPENIA-GRAVE
        print("1/9: S-NEUTROPENIA-GRAVE...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_neutropenia_grave())

        # 2. S-BLASTIC-SYNDROME
        print("2/9: S-BLASTIC-SYNDROME...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_blastic_syndrome())

        # 3. S-TMA
        print("3/9: S-TMA...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_tma())

        # 4. S-PLT-CRITICA
        print("4/9: S-PLT-CRITICA...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_plt_critica())

        # 5. S-ANEMIA-GRAVE
        print("5/9: S-ANEMIA-GRAVE...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_anemia_grave())

        # 6. S-NEUTROFILIA-LEFTSHIFT-CRIT
        print("6/9: S-NEUTROFILIA-LEFTSHIFT-CRIT...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_neutrofilia_leftshift_crit())

        # 7. S-THROMBOCITOSE-CRIT
        print("7/9: S-THROMBOCITOSE-CRIT...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_thrombocitose_crit())

        # 8. S-CIVD
        print("8/9: S-CIVD...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_civd())

        # 9. S-APL
        print("9/9: S-APL...")
        for _ in range(n_per_syndrome):
            cases.append(self.generate_apl())

        print(f"\n✅ Generated {len(cases)} critical cases!")
        return cases

    def export_json(self, filename: str, cases: List[CBCTestCase]):
        """Export cases to JSON"""
        data = [asdict(case) for case in cases]

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Exported {len(cases)} cases to {filename}")

    def print_summary(self, cases: List[CBCTestCase]):
        """Print summary statistics"""
        syndromes = {}
        for case in cases:
            syn = case.expected_syndrome
            syndromes[syn] = syndromes.get(syn, 0) + 1

        print("\n" + "="*70)
        print("RED LIST TEST CASE SUMMARY (SPRINT 4)")
        print("="*70)
        print(f"Total cases: {len(cases)}")
        print(f"\nBy syndrome (all CRITICAL, FN=0 MANDATORY):")
        for syn, count in sorted(syndromes.items()):
            print(f"  {syn}: {count}")
        print("="*70)


def main():
    """Generate 270 Red List cases for Sprint 4"""
    generator = RedListGenerator(seed=42)

    cases = generator.generate_all_red_list(n_per_syndrome=30)

    generator.print_summary(cases)

    output_file = "data/red_list/critical_cases.json"
    generator.export_json(output_file, cases)

    print(f"\n🎯 Ready for validation testing!")
    print(f"   File: {output_file}")
    print(f"   Cases: {len(cases)}")
    print(f"   FN=0 MANDATORY for all {len(cases)} cases!")


if __name__ == "__main__":
    main()
