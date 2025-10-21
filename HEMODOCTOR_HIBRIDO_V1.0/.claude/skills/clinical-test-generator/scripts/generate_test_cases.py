#!/usr/bin/env python3
"""
Clinical Test Case Generator for HemoDoctor
Generates synthetic CBC test cases with ground truth for validation
"""

import json
import csv
import random
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, asdict
import sys


@dataclass
class CBCTestCase:
    """Complete Blood Count test case"""
    # Core CBC
    hb: float
    ht: Optional[float] = None
    rbc: Optional[float] = None
    mcv: float = 90.0
    mch: Optional[float] = None
    mchc: Optional[float] = None
    rdw: float = 13.0
    wbc: float = 7.0
    anc: Optional[float] = None
    lymphocytes_abs: Optional[float] = None
    eosinophils_abs: Optional[float] = None
    basophils_abs: Optional[float] = None
    monocytes_abs: Optional[float] = None
    plt: float = 250.0
    mpv: Optional[float] = None
    reticulocytes: Optional[float] = None
    
    # Complementary
    ferritin: Optional[float] = None
    tsat: Optional[float] = None
    crp: Optional[float] = None
    ldh: Optional[float] = None
    bt_indireta: Optional[float] = None
    haptoglobin: Optional[float] = None
    b12: Optional[float] = None
    folate: Optional[float] = None
    hba2: Optional[float] = None
    
    # Morphology (tristate: True/False/None)
    esquistocitos: Optional[bool] = None
    esferocitos: Optional[bool] = None
    dacriocitos: Optional[bool] = None
    policromasia: Optional[bool] = None
    blastos: Optional[bool] = None
    bastoes: Optional[bool] = None
    
    # Metadata
    age_years: float = 45.0
    sex: str = "M"
    case_id: str = "TEST-001"
    ground_truth_syndrome: str = "NORMAL"
    ground_truth_priority: str = "routine"
    notes: str = ""


class ClinicalTestGenerator:
    """Generate synthetic clinical test cases"""
    
    def __init__(self, seed: Optional[int] = None):
        if seed:
            random.seed(seed)
        self.cases = []
    
    def _derive_rbc(self, hb: float, mcv: float, mchc: float) -> float:
        """Derive RBC from Hb, MCV, MCHC"""
        # RBC = Hb / MCH, where MCH = MCV × MCHC / 100
        mch = (mcv * mchc) / 100
        return hb / mch if mch > 0 else 5.0
    
    def _derive_ht(self, rbc: float, mcv: float) -> float:
        """Derive Ht from RBC and MCV"""
        # Ht = RBC × MCV / 10
        return (rbc * mcv) / 10
    
    def _derive_anc(self, wbc: float, neut_pct: float = 60.0) -> float:
        """Derive ANC from WBC"""
        return wbc * (neut_pct / 100)
    
    # =============================================================================
    # CRITICAL SYNDROME GENERATORS
    # =============================================================================
    
    def generate_severe_neutropenia(self, anc_level: str = "critical") -> CBCTestCase:
        """Generate severe neutropenia case (S-NEUTROPENIA-GRAVE)"""
        if anc_level == "very_critical":
            anc = random.uniform(0.1, 0.2)  # <0.2
        else:  # critical
            anc = random.uniform(0.2, 0.5)  # 0.2-0.5
        
        wbc = random.uniform(1.0, 3.0)
        hb = random.uniform(11.0, 14.0)  # Normal Hb
        mcv = random.uniform(85, 95)
        plt = random.uniform(150, 350)
        
        crp = random.uniform(15, 100) if random.random() > 0.3 else None
        
        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, anc=anc, plt=plt,
            crp=crp,
            age_years=random.uniform(20, 70),
            sex=random.choice(["M", "F"]),
            case_id=f"NEUT-CRIT-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-NEUTROPENIA-GRAVE",
            ground_truth_priority="critical",
            notes=f"Severe neutropenia ANC={anc:.2f}"
        )
    
    def generate_tma(self, with_hemolysis: bool = True) -> CBCTestCase:
        """Generate TMA case (S-TMA)"""
        plt = random.uniform(5, 25)  # Critical thrombocytopenia
        hb = random.uniform(6.0, 9.0)  # Anemia
        mcv = random.uniform(80, 95)
        wbc = random.uniform(5, 12)
        
        # Hemolysis markers
        ldh = random.uniform(500, 2000) if with_hemolysis else None
        bt_indireta = random.uniform(1.5, 4.0) if with_hemolysis else None
        haptoglobin = random.uniform(5, 30) if with_hemolysis else None
        
        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            ldh=ldh, bt_indireta=bt_indireta, haptoglobin=haptoglobin,
            esquistocitos=True,  # CRITICAL for TMA
            policromasia=True if with_hemolysis else None,
            age_years=random.uniform(30, 65),
            sex=random.choice(["M", "F"]),
            case_id=f"TMA-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-TMA",
            ground_truth_priority="critical",
            notes=f"TMA: PLT={plt:.0f}, schistocytes present, hemolysis={with_hemolysis}"
        )
    
    def generate_blastic_syndrome(self, wbc_level: str = "very_high") -> CBCTestCase:
        """Generate blastic syndrome (S-BLASTIC-SYNDROME)"""
        if wbc_level == "very_high":
            wbc = random.uniform(100, 200)
        else:
            wbc = random.uniform(50, 100)
        
        hb = random.uniform(6.0, 10.0)  # Anemia
        plt = random.uniform(10, 80)  # Thrombocytopenia
        mcv = random.uniform(85, 100)
        
        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            blastos=True,  # CRITICAL
            age_years=random.uniform(40, 75),
            sex=random.choice(["M", "F"]),
            case_id=f"BLAST-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-BLASTIC-SYNDROME",
            ground_truth_priority="critical",
            notes=f"Blastic syndrome: WBC={wbc:.0f}, blasts present"
        )
    
    def generate_severe_anemia(self, sex: str = "F") -> CBCTestCase:
        """Generate severe anemia (S-ANEMIA-GRAVE)"""
        if sex == "F":
            hb = random.uniform(5.0, 6.5)
        else:  # M
            hb = random.uniform(5.5, 7.0)
        
        mcv = random.uniform(70, 110)  # Variable
        wbc = random.uniform(5, 10)
        plt = random.uniform(150, 400)
        
        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            age_years=random.uniform(20, 80),
            sex=sex,
            case_id=f"ANEMIA-CRIT-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-ANEMIA-GRAVE",
            ground_truth_priority="critical",
            notes=f"Severe anemia: Hb={hb:.1f} g/dL"
        )
    
    def generate_critical_thrombocytopenia(self) -> CBCTestCase:
        """Generate critical thrombocytopenia (S-PLT-CRITICA)"""
        plt = random.uniform(2, 10)  # <10
        hb = random.uniform(11, 15)
        mcv = random.uniform(80, 95)
        wbc = random.uniform(5, 10)
        
        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            age_years=random.uniform(20, 70),
            sex=random.choice(["M", "F"]),
            case_id=f"PLT-CRIT-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-PLT-CRITICA",
            ground_truth_priority="critical",
            notes=f"Critical thrombocytopenia: PLT={plt:.0f}"
        )
    
    # =============================================================================
    # PRIORITY SYNDROME GENERATORS
    # =============================================================================
    
    def generate_ida(self, stage: str = "classic") -> CBCTestCase:
        """Generate Iron Deficiency Anemia (S-IDA)"""
        if stage == "classic":
            ferritin = random.uniform(5, 20)
            tsat = random.uniform(5, 15)
            hb_m = random.uniform(10, 12)
            hb_f = random.uniform(9, 11)
        elif stage == "borderline":
            ferritin = random.uniform(20, 30)
            tsat = random.uniform(15, 20)
            hb_m = random.uniform(12, 13)
            hb_f = random.uniform(11, 12)
        else:  # severe
            ferritin = random.uniform(2, 10)
            tsat = random.uniform(3, 10)
            hb_m = random.uniform(7, 10)
            hb_f = random.uniform(6, 9)
        
        sex = random.choice(["M", "F"])
        hb = hb_m if sex == "M" else hb_f
        mcv = random.uniform(65, 78)  # Microcytic
        rdw = random.uniform(15, 20)  # High RDW
        
        wbc = random.uniform(5, 9)
        plt = random.uniform(200, 450)  # May be elevated
        
        return CBCTestCase(
            hb=hb, mcv=mcv, rdw=rdw, wbc=wbc, plt=plt,
            ferritin=ferritin, tsat=tsat,
            crp=random.uniform(1, 5) if random.random() > 0.5 else None,
            age_years=random.uniform(18, 50),
            sex=sex,
            case_id=f"IDA-{stage.upper()}-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-IDA",
            ground_truth_priority="priority",
            notes=f"IDA {stage}: Hb={hb:.1f}, MCV={mcv:.0f}, Ferritin={ferritin:.0f}"
        )
    
    def generate_b12_deficiency(self) -> CBCTestCase:
        """Generate B12 deficiency (S-B12-DEFICIENCY)"""
        hb = random.uniform(8.0, 11.0)
        mcv = random.uniform(105, 120)  # Macrocytic
        rdw = random.uniform(15, 20)
        wbc = random.uniform(3, 6)  # May be low
        plt = random.uniform(100, 200)  # May be low
        
        b12 = random.uniform(50, 250)  # Low B12
        
        return CBCTestCase(
            hb=hb, mcv=mcv, rdw=rdw, wbc=wbc, plt=plt,
            b12=b12,
            age_years=random.uniform(50, 85),
            sex=random.choice(["M", "F"]),
            case_id=f"B12-DEF-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-B12-DEFICIENCY",
            ground_truth_priority="priority",
            notes=f"B12 deficiency: MCV={mcv:.0f}, B12={b12:.0f}"
        )
    
    def generate_beta_thalassemia_trait(self) -> CBCTestCase:
        """Generate beta-thalassemia trait (S-BETA-THAL-TRAIT)"""
        hb = random.uniform(10.5, 13.0)
        mcv = random.uniform(60, 72)  # Microcytic
        rdw = random.uniform(11, 14)  # Normal or slightly high
        rbc = random.uniform(5.5, 7.0)  # HIGH RBC count
        
        hba2 = random.uniform(3.6, 6.5)  # Elevated HbA2
        
        wbc = random.uniform(5, 10)
        plt = random.uniform(200, 400)
        ferritin = random.uniform(50, 200) if random.random() > 0.5 else None
        
        return CBCTestCase(
            hb=hb, mcv=mcv, rdw=rdw, rbc=rbc, wbc=wbc, plt=plt,
            ferritin=ferritin, hba2=hba2,
            age_years=random.uniform(20, 60),
            sex=random.choice(["M", "F"]),
            case_id=f"THAL-TRAIT-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-BETA-THAL-TRAIT",
            ground_truth_priority="priority",
            notes=f"Beta-thal trait: MCV={mcv:.0f}, RBC={rbc:.2f}, HbA2={hba2:.1f}%"
        )
    
    def generate_eosinophilia(self, severity: str = "moderate") -> CBCTestCase:
        """Generate eosinophilia (S-EOSINOPHILIA)"""
        if severity == "severe":
            eosinophils_abs = random.uniform(3.0, 10.0)
        else:  # moderate
            eosinophils_abs = random.uniform(1.5, 3.0)
        
        wbc = random.uniform(10, 20)
        hb = random.uniform(12, 15)
        mcv = random.uniform(80, 95)
        plt = random.uniform(200, 400)
        
        return CBCTestCase(
            hb=hb, mcv=mcv, wbc=wbc, plt=plt,
            eosinophils_abs=eosinophils_abs,
            age_years=random.uniform(20, 70),
            sex=random.choice(["M", "F"]),
            case_id=f"EOSINO-{severity.upper()}-{random.randint(1000, 9999)}",
            ground_truth_syndrome="S-EOSINOPHILIA",
            ground_truth_priority="priority",
            notes=f"Eosinophilia {severity}: Eos={eosinophils_abs:.2f}"
        )
    
    # =============================================================================
    # NORMAL/BORDERLINE GENERATORS
    # =============================================================================
    
    def generate_normal(self, sex: str = None) -> CBCTestCase:
        """Generate normal CBC"""
        if sex is None:
            sex = random.choice(["M", "F"])
        
        hb = random.uniform(13.5, 16.0) if sex == "M" else random.uniform(12.0, 15.0)
        mcv = random.uniform(82, 98)
        rdw = random.uniform(11.5, 14.0)
        wbc = random.uniform(4.5, 10.0)
        plt = random.uniform(150, 400)
        
        return CBCTestCase(
            hb=hb, mcv=mcv, rdw=rdw, wbc=wbc, plt=plt,
            age_years=random.uniform(20, 70),
            sex=sex,
            case_id=f"NORMAL-{random.randint(1000, 9999)}",
            ground_truth_syndrome="NORMAL",
            ground_truth_priority="routine",
            notes="Normal CBC"
        )
    
    def generate_borderline_microcytosis(self) -> CBCTestCase:
        """Generate borderline microcytosis (testing always-output)"""
        hb = random.uniform(12.5, 14.0)
        mcv = random.uniform(78, 82)  # Borderline low
        rdw = random.uniform(12, 14)
        wbc = random.uniform(5, 9)
        plt = random.uniform(200, 350)
        
        return CBCTestCase(
            hb=hb, mcv=mcv, rdw=rdw, wbc=wbc, plt=plt,
            age_years=random.uniform(25, 55),
            sex=random.choice(["M", "F"]),
            case_id=f"BORDER-MCV-{random.randint(1000, 9999)}",
            ground_truth_syndrome="BORDERLINE-MICROCYTOSIS",
            ground_truth_priority="routine",
            notes=f"Borderline MCV={mcv:.0f}, suggest repeat/ferritin"
        )
    
    # =============================================================================
    # BATCH GENERATION
    # =============================================================================
    
    def generate_red_list(self, n_per_syndrome: int = 40) -> List[CBCTestCase]:
        """Generate Red List cases (critical syndromes, FN=0 required)"""
        cases = []
        
        # Critical syndromes
        for i in range(n_per_syndrome):
            cases.append(self.generate_severe_neutropenia("critical"))
            cases.append(self.generate_severe_neutropenia("very_critical"))
            cases.append(self.generate_tma(with_hemolysis=True))
            cases.append(self.generate_tma(with_hemolysis=False))
            cases.append(self.generate_blastic_syndrome("very_high"))
            cases.append(self.generate_severe_anemia("M"))
            cases.append(self.generate_severe_anemia("F"))
            cases.append(self.generate_critical_thrombocytopenia())
        
        self.cases.extend(cases)
        return cases
    
    def generate_validation_set(self, n_total: int = 500) -> List[CBCTestCase]:
        """Generate balanced validation set"""
        cases = []
        
        # Distribution: 10% critical, 40% priority, 50% normal/routine
        n_critical = int(n_total * 0.10)
        n_priority = int(n_total * 0.40)
        n_normal = n_total - n_critical - n_priority
        
        # Critical
        for _ in range(n_critical // 8):
            cases.append(self.generate_severe_neutropenia())
            cases.append(self.generate_tma())
            cases.append(self.generate_blastic_syndrome())
            cases.append(self.generate_severe_anemia())
            cases.append(self.generate_critical_thrombocytopenia())
        
        # Priority
        for _ in range(n_priority // 5):
            cases.append(self.generate_ida("classic"))
            cases.append(self.generate_ida("borderline"))
            cases.append(self.generate_b12_deficiency())
            cases.append(self.generate_beta_thalassemia_trait())
            cases.append(self.generate_eosinophilia())
        
        # Normal/Routine
        for _ in range(n_normal):
            if random.random() > 0.8:
                cases.append(self.generate_borderline_microcytosis())
            else:
                cases.append(self.generate_normal())
        
        self.cases.extend(cases)
        return cases
    
    def generate_missing_data_cases(self, n: int = 50) -> List[CBCTestCase]:
        """Generate cases with missing data (test missingness engine)"""
        cases = []
        
        for _ in range(n):
            # Start with a random syndrome
            generators = [
                self.generate_ida,
                self.generate_b12_deficiency,
                self.generate_eosinophilia,
                self.generate_normal
            ]
            case = random.choice(generators)()
            
            # Randomly remove 20-40% of complementary tests
            if random.random() > 0.6:
                case.ferritin = None
            if random.random() > 0.6:
                case.tsat = None
            if random.random() > 0.7:
                case.b12 = None
            if random.random() > 0.7:
                case.crp = None
            if random.random() > 0.8:
                case.ldh = None
            
            case.notes += " [MISSING DATA TEST]"
            cases.append(case)
        
        self.cases.extend(cases)
        return cases
    
    # =============================================================================
    # EXPORT
    # =============================================================================
    
    def export_json(self, filename: str, cases: List[CBCTestCase] = None):
        """Export cases to JSON"""
        if cases is None:
            cases = self.cases
        
        data = [asdict(case) for case in cases]
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Exported {len(cases)} cases to {filename}")
    
    def export_csv(self, filename: str, cases: List[CBCTestCase] = None):
        """Export cases to CSV"""
        if cases is None:
            cases = self.cases
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            if not cases:
                return
            
            fieldnames = asdict(cases[0]).keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            for case in cases:
                writer.writerow(asdict(case))
        
        print(f"✅ Exported {len(cases)} cases to {filename}")
    
    def export_yaml(self, filename: str, cases: List[CBCTestCase] = None):
        """Export cases to YAML"""
        if cases is None:
            cases = self.cases
        
        data = [asdict(case) for case in cases]
        
        with open(filename, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
        
        print(f"✅ Exported {len(cases)} cases to {filename}")
    
    def print_summary(self):
        """Print summary statistics"""
        if not self.cases:
            print("No cases generated yet")
            return
        
        syndromes = {}
        for case in self.cases:
            syn = case.ground_truth_syndrome
            syndromes[syn] = syndromes.get(syn, 0) + 1
        
        print("\n" + "="*60)
        print("TEST CASE SUMMARY")
        print("="*60)
        print(f"Total cases: {len(self.cases)}")
        print(f"\nBy syndrome:")
        for syn, count in sorted(syndromes.items(), key=lambda x: -x[1]):
            print(f"  {syn}: {count}")
        print("="*60)


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_test_cases.py <command> [options]")
        print("\nCommands:")
        print("  red-list [n_per_syndrome] [output_file]")
        print("    Generate Red List critical cases (default: 40 per syndrome)")
        print("  ")
        print("  validation [n_total] [output_file]")
        print("    Generate balanced validation set (default: 500 cases)")
        print("  ")
        print("  missing [n] [output_file]")
        print("    Generate cases with missing data (default: 50)")
        print("  ")
        print("  custom --ida=10 --tma=5 --normal=20 [output_file]")
        print("    Generate custom mix of syndromes")
        print("\nExamples:")
        print("  python generate_test_cases.py red-list 40 red_list.json")
        print("  python generate_test_cases.py validation 500 validation.csv")
        print("  python generate_test_cases.py missing 50 missing_data.json")
        sys.exit(1)
    
    command = sys.argv[1]
    generator = ClinicalTestGenerator(seed=42)  # Reproducible
    
    if command == "red-list":
        n_per = int(sys.argv[2]) if len(sys.argv) > 2 else 40
        output = sys.argv[3] if len(sys.argv) > 3 else "red_list_cases.json"
        
        print(f"🧪 Generating Red List ({n_per} per critical syndrome)...")
        cases = generator.generate_red_list(n_per)
        generator.print_summary()
        
        if output.endswith('.csv'):
            generator.export_csv(output, cases)
        elif output.endswith('.yaml') or output.endswith('.yml'):
            generator.export_yaml(output, cases)
        else:
            generator.export_json(output, cases)
    
    elif command == "validation":
        n_total = int(sys.argv[2]) if len(sys.argv) > 2 else 500
        output = sys.argv[3] if len(sys.argv) > 3 else "validation_set.json"
        
        print(f"🧪 Generating validation set ({n_total} cases)...")
        cases = generator.generate_validation_set(n_total)
        generator.print_summary()
        
        if output.endswith('.csv'):
            generator.export_csv(output, cases)
        elif output.endswith('.yaml') or output.endswith('.yml'):
            generator.export_yaml(output, cases)
        else:
            generator.export_json(output, cases)
    
    elif command == "missing":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        output = sys.argv[3] if len(sys.argv) > 3 else "missing_data_cases.json"
        
        print(f"🧪 Generating missing data cases ({n})...")
        cases = generator.generate_missing_data_cases(n)
        generator.print_summary()
        
        if output.endswith('.csv'):
            generator.export_csv(output, cases)
        elif output.endswith('.yaml') or output.endswith('.yml'):
            generator.export_yaml(output, cases)
        else:
            generator.export_json(output, cases)
    
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
