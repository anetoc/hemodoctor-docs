"""
HemoDoctor FastAPI Batch Processor
===================================

Script para processar dados CBC em batch através do sistema FastAPI completo.
Integra com o endpoint de análise do HemoDoctor para análise hematológica completa.

Features:
- Ingestão de CSV
- Requisições HTTP para FastAPI
- Análise hematológica completa (não apenas plaquetas)
- Processamento paralelo
- Relatórios consolidados
- Retry logic e error handling

Autor: Claude AI Agent
Data: 22 de Outubro de 2025
Versão: 1.0.0
"""

import csv
import json
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from urllib.parse import urljoin
import sys


# ============================================================================
# CONFIGURATION
# ============================================================================

@dataclass
class Config:
    """Configuration for HemoDoctor API connection."""
    api_base_url: str = "http://localhost:8000"  # Default FastAPI URL
    api_timeout: int = 30  # Request timeout in seconds
    max_workers: int = 5  # Parallel requests
    retry_attempts: int = 3  # Retry failed requests
    retry_delay: int = 2  # Seconds between retries


# ============================================================================
# CSV READER (Reuse from previous script)
# ============================================================================

class CBCCSVReader:
    """CSV reader for CBC data with multiple format support."""

    COLUMN_MAPPINGS = {
        'patient_id': ['patient_id', 'id', 'patient', 'mrn', 'Patient ID'],
        'age_months': ['age_months', 'age_m', 'age_in_months', 'Age (months)'],
        'age_years': ['age_years', 'age_y', 'age_in_years', 'Age (years)'],
        'platelet_count': ['platelet_count', 'platelets', 'plt', 'PLT', 'Platelet Count'],
        'hemoglobin': ['hemoglobin', 'hb', 'Hb', 'HGB', 'Hemoglobin'],
        'hematocrit': ['hematocrit', 'hct', 'HCT', 'Hematocrit'],
        'wbc': ['wbc', 'white_blood_cells', 'WBC', 'leukocytes'],
        'rbc': ['rbc', 'red_blood_cells', 'RBC', 'erythrocytes'],
        'mcv': ['mcv', 'MCV', 'mean_corpuscular_volume'],
        'mch': ['mch', 'MCH', 'mean_corpuscular_hemoglobin'],
        'mchc': ['mchc', 'MCHC', 'mean_corpuscular_hemoglobin_concentration'],
    }

    def __init__(self, csv_path: str, delimiter: str = ','):
        self.csv_path = Path(csv_path)
        self.delimiter = delimiter
        self.warnings = []

        if not self.csv_path.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_path}")

    def detect_column_mapping(self, headers: List[str]) -> Dict[str, str]:
        """Auto-detect column mapping from CSV headers."""
        mapping = {}
        for standard_name, possible_names in self.COLUMN_MAPPINGS.items():
            for header in headers:
                if header in possible_names or header.lower() in [n.lower() for n in possible_names]:
                    mapping[standard_name] = header
                    break
        return mapping

    def parse_value(self, value: str, field_type: str = 'float') -> Optional[float]:
        """Parse numeric value from string."""
        if not value or value.strip() == '':
            return None

        value_str = value.strip().replace(',', '')

        try:
            if field_type == 'float':
                return float(value_str)
            elif field_type == 'int':
                return int(float(value_str))
        except ValueError:
            return None

    def read_csv(self) -> List[Dict[str, Any]]:
        """Read and parse CSV file."""
        data = []

        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=self.delimiter)
            headers = reader.fieldnames

            column_mapping = self.detect_column_mapping(headers)

            if not column_mapping.get('patient_id'):
                self.warnings.append("⚠️ Patient ID column not found, using row numbers")
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
                    if 'age_months' in column_mapping:
                        age_months = self.parse_value(row[column_mapping['age_months']])
                    elif 'age_years' in column_mapping:
                        age_years = self.parse_value(row[column_mapping['age_years']])
                        age_months = age_years * 12 if age_years else None
                    else:
                        age_months = None

                    if age_months is None:
                        raise ValueError("Age could not be parsed")

                    # Build complete CBC data
                    cbc_data = {
                        'patient_id': patient_id,
                        'age_months': age_months,
                        'row_number': i
                    }

                    # Add all available CBC parameters
                    for param in ['platelet_count', 'hemoglobin', 'hematocrit', 'wbc', 'rbc', 'mcv', 'mch', 'mchc']:
                        if param in column_mapping:
                            value = self.parse_value(row[column_mapping[param]])
                            if value is not None:
                                # Handle special conversions
                                if param == 'platelet_count' and value < 1000:
                                    value = value * 1000
                                cbc_data[param] = value

                    data.append(cbc_data)

                except Exception as e:
                    self.warnings.append(f"⚠️ Row {i}: {str(e)}")
                    continue

        return data


# ============================================================================
# HEMODOCTOR API CLIENT
# ============================================================================

class HemoDoctorClient:
    """Client for HemoDoctor FastAPI endpoints."""

    def __init__(self, config: Config):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'HemoDoctor-BatchProcessor/1.0'
        })

    def check_health(self) -> bool:
        """Check if API is available."""
        try:
            url = urljoin(self.config.api_base_url, '/health')
            response = self.session.get(url, timeout=5)
            return response.status_code == 200
        except Exception:
            return False

    def analyze_cbc(self, cbc_data: Dict[str, Any], retry: int = 0) -> Dict[str, Any]:
        """
        Send CBC data to HemoDoctor API for analysis.

        Endpoint: POST /api/v1/analyze/cbc
        """
        url = urljoin(self.config.api_base_url, '/api/v1/analyze/cbc')

        try:
            response = self.session.post(
                url,
                json=cbc_data,
                timeout=self.config.api_timeout
            )

            if response.status_code == 200:
                return {
                    'success': True,
                    'data': response.json(),
                    'patient_id': cbc_data.get('patient_id'),
                    'status_code': 200
                }
            else:
                error_msg = f"HTTP {response.status_code}: {response.text[:200]}"

                # Retry on server errors
                if response.status_code >= 500 and retry < self.config.retry_attempts:
                    time.sleep(self.config.retry_delay * (retry + 1))
                    return self.analyze_cbc(cbc_data, retry + 1)

                return {
                    'success': False,
                    'error': error_msg,
                    'patient_id': cbc_data.get('patient_id'),
                    'status_code': response.status_code
                }

        except requests.exceptions.Timeout:
            error_msg = "Request timeout"
            if retry < self.config.retry_attempts:
                time.sleep(self.config.retry_delay)
                return self.analyze_cbc(cbc_data, retry + 1)
            return {
                'success': False,
                'error': error_msg,
                'patient_id': cbc_data.get('patient_id'),
                'status_code': 408
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'patient_id': cbc_data.get('patient_id'),
                'status_code': 0
            }


# ============================================================================
# BATCH PROCESSOR
# ============================================================================

class BatchProcessor:
    """Process multiple CBC records in batch."""

    def __init__(self, client: HemoDoctorClient, max_workers: int = 5):
        self.client = client
        self.max_workers = max_workers
        self.results = []
        self.stats = {
            'total': 0,
            'successful': 0,
            'failed': 0,
            'start_time': None,
            'end_time': None,
        }

    def process_batch(self, cbc_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process batch of CBC records with parallel requests."""
        self.stats['total'] = len(cbc_records)
        self.stats['start_time'] = datetime.now()

        print(f"\n🚀 Processing {len(cbc_records)} records with {self.max_workers} workers...")
        print()

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self.client.analyze_cbc, record): record
                for record in cbc_records
            }

            for i, future in enumerate(as_completed(futures), 1):
                result = future.result()
                self.results.append(result)

                if result['success']:
                    self.stats['successful'] += 1
                    print(f"✅ [{i}/{len(cbc_records)}] {result['patient_id']}")
                else:
                    self.stats['failed'] += 1
                    print(f"❌ [{i}/{len(cbc_records)}] {result['patient_id']}: {result['error']}")

        self.stats['end_time'] = datetime.now()
        return self.results

    def generate_summary(self) -> Dict[str, Any]:
        """Generate processing summary."""
        duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds()

        return {
            'total_records': self.stats['total'],
            'successful': self.stats['successful'],
            'failed': self.stats['failed'],
            'success_rate': f"{(self.stats['successful'] / self.stats['total'] * 100):.1f}%" if self.stats['total'] > 0 else "0%",
            'duration_seconds': round(duration, 2),
            'throughput_per_second': round(self.stats['total'] / duration, 2) if duration > 0 else 0,
        }


# ============================================================================
# REPORT GENERATOR
# ============================================================================

class ReportGenerator:
    """Generate reports from batch processing results."""

    @staticmethod
    def print_summary(summary: Dict[str, Any], results: List[Dict[str, Any]]):
        """Print processing summary."""
        print("\n" + "=" * 70)
        print("📊 BATCH PROCESSING SUMMARY")
        print("=" * 70)
        print()

        print("🔢 OVERVIEW:")
        print("-" * 70)
        print(f"   Total Records: {summary['total_records']}")
        print(f"   Successful: {summary['successful']} ✅")
        print(f"   Failed: {summary['failed']} ❌")
        print(f"   Success Rate: {summary['success_rate']}")
        print()

        print("⏱️  PERFORMANCE:")
        print("-" * 70)
        print(f"   Duration: {summary['duration_seconds']}s")
        print(f"   Throughput: {summary['throughput_per_second']} records/sec")
        print()

        if summary['failed'] > 0:
            print("❌ FAILED RECORDS:")
            print("-" * 70)
            failed = [r for r in results if not r['success']]
            for r in failed[:10]:  # Show first 10
                print(f"   {r['patient_id']}: {r['error']}")
            if len(failed) > 10:
                print(f"   ... and {len(failed) - 10} more")
            print()

        print("=" * 70)

    @staticmethod
    def save_results(results: List[Dict[str, Any]], output_path: str):
        """Save results to JSON file."""
        output = {
            'metadata': {
                'timestamp': datetime.now().isoformat(),
                'total_records': len(results),
                'successful': sum(1 for r in results if r['success']),
                'failed': sum(1 for r in results if not r['success']),
                'version': '1.0.0'
            },
            'results': results
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Results saved to: {output_path}")


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main entry point for batch processing."""
    print("=" * 70)
    print("🏥 HemoDoctor FastAPI Batch Processor")
    print("=" * 70)
    print()

    # Get configuration
    api_url = input("API Base URL [http://localhost:8000]: ").strip() or "http://localhost:8000"
    csv_file = input("CSV file path: ").strip()

    config = Config(api_base_url=api_url)

    try:
        # Initialize client
        print(f"\n🔌 Connecting to HemoDoctor API at {api_url}...")
        client = HemoDoctorClient(config)

        # Check API health
        if not client.check_health():
            print("❌ Error: Cannot connect to HemoDoctor API")
            print("\n💡 Make sure the FastAPI server is running:")
            print("   cd /path/to/HEMODOCTOR_CONSOLIDADO_v2.0/03_DESENVOLVIMENTO/CODIGO_FONTE")
            print("   uvicorn main:app --reload")
            sys.exit(1)

        print("✅ API connection successful!")

        # Read CSV
        print(f"\n📖 Reading CSV: {csv_file}")
        reader = CBCCSVReader(csv_file)
        data = reader.read_csv()

        if reader.warnings:
            print(f"\n⚠️  {len(reader.warnings)} warnings:")
            for warning in reader.warnings[:5]:
                print(f"   {warning}")
            if len(reader.warnings) > 5:
                print(f"   ... and {len(reader.warnings) - 5} more")

        print(f"\n✅ Loaded {len(data)} records")

        # Process batch
        processor = BatchProcessor(client, max_workers=config.max_workers)
        results = processor.process_batch(data)

        # Generate summary
        summary = processor.generate_summary()
        ReportGenerator.print_summary(summary, results)

        # Save results
        output_dir = Path("hemodoctor_batch_results")
        output_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = output_dir / f"batch_results_{timestamp}.json"

        ReportGenerator.save_results(results, str(output_file))

        print()
        print("=" * 70)
        print("✅ BATCH PROCESSING COMPLETE!")
        print("=" * 70)

    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
