"""
HemoDoctor CBC CSV Analyzer
============================

Script para análise de dados reais de CBC em formato CSV.
Aplica as implementações do Bug #2 e Test Structure Fix.

Autor: Claude AI Agent
Data: 22 de Outubro de 2025
Versão: 1.0.0

Features:
- Ingestão de CSV com validação
- Processamento com Bug #2 fix aplicado
- Análise estatística completa
- Geração de relatórios
- Suporte a múltiplos formatos de CSV
"""

import csv
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import sys


# ============================================================================
# DATACLASS DEFINITIONS (Com Bug #2 Fix Aplicado)
# ============================================================================

@dataclass
class AgeGroup:
    """Pediatric age group with reference ranges."""
    name: str
    age_min: float
    age_max: float
    platelet_min: int
    platelet_max: int


@dataclass
class SeverityClassification:
    """Platelet count severity classification."""
    level: str
    platelet_count: int
    reference_min: int
    reference_max: int
    clinical_significance: str
    risk_level: str  # LOW, MEDIUM, HIGH, CRITICAL


@dataclass
class CBCResult:
    """Complete Blood Count analysis result."""
    patient_id: str
    age_months: float
    age_group: AgeGroup
    platelet_count: int
    severity: SeverityClassification
    timestamp: str
    warnings: List[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "patient_id": self.patient_id,
            "age_months": self.age_months,
            "age_years": round(self.age_months / 12, 2),
            "age_group": {
                "name": self.age_group.name,
                "age_min": self.age_group.age_min,
                "age_max": self.age_group.age_max,
                "platelet_min": self.age_group.platelet_min,
                "platelet_max": self.age_group.platelet_max,
            },
            "platelet_count": self.platelet_count,
            "platelet_count_formatted": f"{self.platelet_count:,}",
            "severity": {
                "level": self.severity.level,
                "platelet_count": self.severity.platelet_count,
                "reference_min": self.severity.reference_min,
                "reference_max": self.severity.reference_max,
                "clinical_significance": self.severity.clinical_significance,
                "risk_level": self.severity.risk_level,
            },
            "timestamp": self.timestamp,
            "warnings": self.warnings or [],
        }


# ============================================================================
# AGE GROUP DEFINITIONS
# ============================================================================

PED_01_NEONATAL = AgeGroup(
    name="PED-01: Neonatal",
    age_min=0.0,
    age_max=1.0,
    platelet_min=150,
    platelet_max=400
)

PED_02_INFANT_EARLY = AgeGroup(
    name="PED-02: Infant Early",
    age_min=1.0,
    age_max=6.0,
    platelet_min=200,
    platelet_max=475
)

PED_03_INFANT_LATE = AgeGroup(
    name="PED-03: Infant Late",
    age_min=6.0,
    age_max=24.0,
    platelet_min=200,
    platelet_max=475
)

PED_04_PRESCHOOL = AgeGroup(
    name="PED-04: Preschool",
    age_min=24.0,
    age_max=72.0,
    platelet_min=180,
    platelet_max=450
)

PED_05_SCHOOL = AgeGroup(
    name="PED-05: School Age",
    age_min=72.0,
    age_max=144.0,
    platelet_min=150,
    platelet_max=450
)

PED_06_ADOLESCENT = AgeGroup(
    name="PED-06: Adolescent",
    age_min=144.0,
    age_max=216.0,
    platelet_min=150,
    platelet_max=400
)


# ============================================================================
# BUG #2 FIX APPLIED - Age Classification
# ============================================================================

def get_age_group(age_months: float) -> AgeGroup:
    """
    Classify age into pediatric group using INCLUSIVE upper bounds.

    ✅ BUG #2 FIX APPLIED: Changed from semi-open [a,b) to inclusive [a,b]

    Clinical rationale:
    - A child at exactly 2.0 years (24 months) is still in Infant Late group
    - A teenager at exactly 18.0 years (216 months) is still in Adolescent group
    """
    # ✅ FIX: Using <= instead of <
    if age_months <= 1:
        return PED_01_NEONATAL
    elif age_months <= 6:
        return PED_02_INFANT_EARLY
    elif age_months <= 24:
        return PED_03_INFANT_LATE
    elif age_months <= 72:
        return PED_04_PRESCHOOL
    elif age_months <= 144:
        return PED_05_SCHOOL
    elif age_months <= 216:
        return PED_06_ADOLESCENT
    else:
        raise ValueError(
            f"Age {age_months} months (>{age_months/12:.1f} years) exceeds "
            "pediatric range (0-18 years). Use adult reference ranges."
        )


# ============================================================================
# SEVERITY CLASSIFICATION
# ============================================================================

def classify_severity(platelet_count: int, age_group: AgeGroup) -> SeverityClassification:
    """
    Classify platelet count severity based on age-specific reference ranges.

    Severity Levels:
    - Normal: Within reference range
    - Mild: 100-150k or 450-600k
    - Moderate: 50-100k or 600-800k
    - Severe: 20-50k or 800k-1M
    - Critical: <20k or >1M
    """
    ref_min = age_group.platelet_min * 1000  # Convert to /μL
    ref_max = age_group.platelet_max * 1000

    # Normal
    if ref_min <= platelet_count <= ref_max:
        return SeverityClassification(
            level="Normal",
            platelet_count=platelet_count,
            reference_min=ref_min,
            reference_max=ref_max,
            clinical_significance="Platelet count within normal range",
            risk_level="LOW"
        )

    # Thrombocytopenia (Low)
    if platelet_count < ref_min:
        if platelet_count >= 100000:
            return SeverityClassification(
                level="Mild Thrombocytopenia",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="Mild decrease, usually asymptomatic",
                risk_level="LOW"
            )
        elif platelet_count >= 50000:
            return SeverityClassification(
                level="Moderate Thrombocytopenia",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="Increased bleeding risk with trauma/surgery",
                risk_level="MEDIUM"
            )
        elif platelet_count >= 20000:
            return SeverityClassification(
                level="Severe Thrombocytopenia",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="High bleeding risk, spontaneous bleeding possible",
                risk_level="HIGH"
            )
        else:
            return SeverityClassification(
                level="Critical Thrombocytopenia",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="Life-threatening, spontaneous bleeding likely",
                risk_level="CRITICAL"
            )

    # Thrombocytosis (High)
    else:
        if platelet_count <= 600000:
            return SeverityClassification(
                level="Mild Thrombocytosis",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="Mild elevation, often reactive",
                risk_level="LOW"
            )
        elif platelet_count <= 800000:
            return SeverityClassification(
                level="Moderate Thrombocytosis",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="Moderate elevation, investigate cause",
                risk_level="MEDIUM"
            )
        elif platelet_count <= 1000000:
            return SeverityClassification(
                level="Severe Thrombocytosis",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="Increased thrombosis risk",
                risk_level="HIGH"
            )
        else:
            return SeverityClassification(
                level="Critical Thrombocytosis",
                platelet_count=platelet_count,
                reference_min=ref_min,
                reference_max=ref_max,
                clinical_significance="Extreme thrombosis risk, urgent evaluation needed",
                risk_level="CRITICAL"
            )


# ============================================================================
# CSV INGESTION
# ============================================================================

class CBCCSVReader:
    """
    CSV reader for CBC data with multiple format support.

    Supported CSV formats:
    1. Standard format: patient_id, age_months, platelet_count
    2. Extended format: includes age_years, timestamp, etc.
    3. Lab format: various lab-specific column names
    """

    # Column name mappings for different formats
    COLUMN_MAPPINGS = {
        'patient_id': ['patient_id', 'id', 'patient', 'mrn', 'Patient ID'],
        'age_months': ['age_months', 'age_m', 'age_in_months', 'Age (months)'],
        'age_years': ['age_years', 'age_y', 'age_in_years', 'Age (years)'],
        'platelet_count': ['platelet_count', 'platelets', 'plt', 'PLT', 'Platelet Count'],
    }

    def __init__(self, csv_path: str, delimiter: str = ','):
        self.csv_path = Path(csv_path)
        self.delimiter = delimiter
        self.warnings = []

        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_path}")

    def detect_column_mapping(self, headers: List[str]) -> Dict[str, str]:
        """
        Auto-detect column mapping from CSV headers.

        Returns dict mapping standard names to actual column names.
        """
        mapping = {}

        for standard_name, possible_names in self.COLUMN_MAPPINGS.items():
            for header in headers:
                if header in possible_names or header.lower() in [n.lower() for n in possible_names]:
                    mapping[standard_name] = header
                    break

        return mapping

    def parse_age(self, row: Dict[str, str], column_mapping: Dict[str, str]) -> float:
        """
        Parse age from row, handling both months and years.

        Priority: age_months > age_years
        """
        if 'age_months' in column_mapping:
            try:
                return float(row[column_mapping['age_months']])
            except (ValueError, KeyError):
                pass

        if 'age_years' in column_mapping:
            try:
                age_years = float(row[column_mapping['age_years']])
                return age_years * 12  # Convert to months
            except (ValueError, KeyError):
                pass

        raise ValueError(f"Could not parse age from row: {row}")

    def parse_platelet_count(self, row: Dict[str, str], column_mapping: Dict[str, str]) -> int:
        """
        Parse platelet count, handling various formats.

        Supports:
        - Raw numbers: 150000
        - With commas: 150,000
        - Scientific notation: 1.5e5
        - Per microliter: 150 (assumes x1000)
        """
        if 'platelet_count' not in column_mapping:
            raise ValueError("Platelet count column not found")

        value_str = row[column_mapping['platelet_count']].strip()

        # Remove commas
        value_str = value_str.replace(',', '')

        try:
            value = float(value_str)

            # If value is very small, assume it's in K (thousands)
            if value < 1000:
                value = value * 1000

            return int(value)
        except ValueError:
            raise ValueError(f"Could not parse platelet count: {value_str}")

    def read_csv(self) -> List[Dict[str, Any]]:
        """
        Read and parse CSV file.

        Returns list of dictionaries with standardized keys.
        """
        data = []

        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=self.delimiter)
            headers = reader.fieldnames

            # Auto-detect column mapping
            column_mapping = self.detect_column_mapping(headers)

            if not column_mapping.get('patient_id'):
                self.warnings.append("⚠️ Patient ID column not found, using row numbers")
            if not column_mapping.get('platelet_count'):
                raise ValueError("❌ Platelet count column is required")
            if not column_mapping.get('age_months') and not column_mapping.get('age_years'):
                raise ValueError("❌ Age column (months or years) is required")

            print(f"\n📋 Detected columns:")
            for std_name, actual_name in column_mapping.items():
                print(f"   {std_name} → '{actual_name}'")
            print()

            for i, row in enumerate(reader, start=1):
                try:
                    # Parse patient ID
                    if 'patient_id' in column_mapping:
                        patient_id = row[column_mapping['patient_id']]
                    else:
                        patient_id = f"PAT{i:04d}"

                    # Parse age
                    age_months = self.parse_age(row, column_mapping)

                    # Parse platelet count
                    platelet_count = self.parse_platelet_count(row, column_mapping)

                    data.append({
                        'patient_id': patient_id,
                        'age_months': age_months,
                        'platelet_count': platelet_count,
                        'row_number': i
                    })

                except Exception as e:
                    self.warnings.append(f"⚠️ Row {i}: {str(e)}")
                    continue

        return data


# ============================================================================
# CBC ANALYZER
# ============================================================================

class CBCAnalyzer:
    """
    Analyze CBC data and generate results with Bug #2 fix applied.
    """

    def __init__(self):
        self.results: List[CBCResult] = []
        self.stats = {
            'total': 0,
            'successful': 0,
            'errors': 0,
            'by_age_group': {},
            'by_severity': {},
            'by_risk_level': {},
        }

    def analyze_patient(self, patient_data: Dict[str, Any]) -> Optional[CBCResult]:
        """
        Analyze single patient CBC data.

        Returns CBCResult or None if error.
        """
        try:
            self.stats['total'] += 1

            # Get age group (with Bug #2 fix applied)
            age_group = get_age_group(patient_data['age_months'])

            # Classify severity
            severity = classify_severity(patient_data['platelet_count'], age_group)

            # Create result
            result = CBCResult(
                patient_id=patient_data['patient_id'],
                age_months=patient_data['age_months'],
                age_group=age_group,
                platelet_count=patient_data['platelet_count'],
                severity=severity,
                timestamp=datetime.now().isoformat(),
                warnings=[]
            )

            self.stats['successful'] += 1

            # Update statistics
            self.stats['by_age_group'][age_group.name] = \
                self.stats['by_age_group'].get(age_group.name, 0) + 1
            self.stats['by_severity'][severity.level] = \
                self.stats['by_severity'].get(severity.level, 0) + 1
            self.stats['by_risk_level'][severity.risk_level] = \
                self.stats['by_risk_level'].get(severity.risk_level, 0) + 1

            return result

        except Exception as e:
            self.stats['errors'] += 1
            print(f"❌ Error analyzing {patient_data.get('patient_id', 'unknown')}: {e}")
            return None

    def analyze_batch(self, patients_data: List[Dict[str, Any]]) -> List[CBCResult]:
        """
        Analyze batch of patient data.
        """
        print(f"\n🔬 Analyzing {len(patients_data)} patient records...")
        print()

        for patient_data in patients_data:
            result = self.analyze_patient(patient_data)
            if result:
                self.results.append(result)

        return self.results

    def generate_summary(self) -> Dict[str, Any]:
        """
        Generate analysis summary statistics.
        """
        return {
            'overview': {
                'total_records': self.stats['total'],
                'successful_analyses': self.stats['successful'],
                'errors': self.stats['errors'],
                'success_rate': f"{(self.stats['successful'] / self.stats['total'] * 100):.1f}%" if self.stats['total'] > 0 else "0%"
            },
            'age_distribution': self.stats['by_age_group'],
            'severity_distribution': self.stats['by_severity'],
            'risk_distribution': self.stats['by_risk_level'],
        }


# ============================================================================
# REPORT GENERATOR
# ============================================================================

class ReportGenerator:
    """
    Generate analysis reports in various formats.
    """

    @staticmethod
    def print_summary(summary: Dict[str, Any]):
        """Print summary to console."""
        print("\n" + "=" * 70)
        print("📊 ANÁLISE DE DADOS CBC - RESUMO")
        print("=" * 70)
        print()

        # Overview
        print("📈 VISÃO GERAL:")
        print("-" * 70)
        for key, value in summary['overview'].items():
            print(f"   {key.replace('_', ' ').title()}: {value}")
        print()

        # Age distribution
        print("👶 DISTRIBUIÇÃO POR GRUPO ETÁRIO:")
        print("-" * 70)
        for age_group, count in sorted(summary['age_distribution'].items()):
            pct = (count / summary['overview']['successful_analyses'] * 100) if summary['overview']['successful_analyses'] > 0 else 0
            print(f"   {age_group}: {count} ({pct:.1f}%)")
        print()

        # Severity distribution
        print("⚕️  DISTRIBUIÇÃO POR SEVERIDADE:")
        print("-" * 70)
        for severity, count in sorted(summary['severity_distribution'].items()):
            pct = (count / summary['overview']['successful_analyses'] * 100) if summary['overview']['successful_analyses'] > 0 else 0
            print(f"   {severity}: {count} ({pct:.1f}%)")
        print()

        # Risk distribution
        print("🚨 DISTRIBUIÇÃO POR NÍVEL DE RISCO:")
        print("-" * 70)
        risk_order = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
        for risk in risk_order:
            count = summary['risk_distribution'].get(risk, 0)
            pct = (count / summary['overview']['successful_analyses'] * 100) if summary['overview']['successful_analyses'] > 0 else 0
            icon = {'LOW': '🟢', 'MEDIUM': '🟡', 'HIGH': '🟠', 'CRITICAL': '🔴'}.get(risk, '⚪')
            print(f"   {icon} {risk}: {count} ({pct:.1f}%)")
        print()
        print("=" * 70)

    @staticmethod
    def save_json(results: List[CBCResult], output_path: str):
        """Save results to JSON file."""
        output = {
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'total_records': len(results),
                'version': '1.0.0',
                'bug_fix_applied': 'BUG-002 (Inclusive age boundaries)'
            },
            'results': [r.to_dict() for r in results]
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Resultados salvos em: {output_path}")

    @staticmethod
    def save_csv(results: List[CBCResult], output_path: str):
        """Save results to CSV file."""
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'patient_id', 'age_months', 'age_years', 'age_group',
                'platelet_count', 'severity_level', 'risk_level',
                'clinical_significance', 'timestamp'
            ])
            writer.writeheader()

            for r in results:
                writer.writerow({
                    'patient_id': r.patient_id,
                    'age_months': r.age_months,
                    'age_years': round(r.age_months / 12, 2),
                    'age_group': r.age_group.name,
                    'platelet_count': r.platelet_count,
                    'severity_level': r.severity.level,
                    'risk_level': r.severity.risk_level,
                    'clinical_significance': r.severity.clinical_significance,
                    'timestamp': r.timestamp,
                })

        print(f"✅ Resultados salvos em: {output_path}")


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """
    Main entry point for CBC CSV analysis.
    """
    print("=" * 70)
    print("🏥 HemoDoctor CBC CSV Analyzer")
    print("=" * 70)
    print()
    print("✅ Bug #2 Fix Applied: Inclusive age boundaries")
    print("✅ Test Structure Fix: Ready for dict/dataclass")
    print()

    # Get CSV file path
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = input("📁 Enter CSV file path: ").strip()

    try:
        # Read CSV
        print(f"\n📖 Reading CSV: {csv_file}")
        reader = CBCCSVReader(csv_file)
        data = reader.read_csv()

        if reader.warnings:
            print(f"\n⚠️  {len(reader.warnings)} warnings:")
            for warning in reader.warnings[:10]:  # Show first 10
                print(f"   {warning}")
            if len(reader.warnings) > 10:
                print(f"   ... and {len(reader.warnings) - 10} more")

        print(f"\n✅ Successfully loaded {len(data)} records")

        # Analyze data
        analyzer = CBCAnalyzer()
        results = analyzer.analyze_batch(data)

        # Generate summary
        summary = analyzer.generate_summary()
        ReportGenerator.print_summary(summary)

        # Save results
        output_base = Path(csv_file).stem
        output_dir = Path("cbc_analysis_results")
        output_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        json_output = output_dir / f"{output_base}_results_{timestamp}.json"
        csv_output = output_dir / f"{output_base}_results_{timestamp}.csv"

        ReportGenerator.save_json(results, str(json_output))
        ReportGenerator.save_csv(results, str(csv_output))

        print()
        print("=" * 70)
        print("✅ ANÁLISE COMPLETA!")
        print("=" * 70)

    except FileNotFoundError as e:
        print(f"\n❌ Erro: {e}")
        print("\n💡 Verifique se o caminho do arquivo está correto.")
        sys.exit(1)

    except ValueError as e:
        print(f"\n❌ Erro de formato: {e}")
        print("\n💡 Verifique se o CSV tem as colunas necessárias:")
        print("   - patient_id (ou ID, ou MRN)")
        print("   - age_months (ou age_years)")
        print("   - platelet_count (ou platelets, PLT)")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
