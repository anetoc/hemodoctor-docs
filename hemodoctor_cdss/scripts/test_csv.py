#!/usr/bin/env python3
"""
HemoDoctor CSV Testing Script

Tests HemoDoctor CDSS API using CSV input files.
Validates results against expected syndromes and generates test reports.

Usage:
    python scripts/test_csv.py --input test_cases.csv
    python scripts/test_csv.py --input test_cases.csv --output results.csv --verbose
    python scripts/test_csv.py --input test_cases.csv --api http://production:8000

Features:
    - Reads CSV test cases
    - Sends POST requests to /analyze endpoint
    - Compares results with expected syndromes
    - Generates summary metrics (TP, FP, FN, sensitivity, precision)
    - Saves detailed results to CSV
    - Colored terminal output

Author: Dr. Abel Costa
Version: 1.0.0
Date: 2025-10-23
"""

import argparse
import csv
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

import requests
from requests.exceptions import RequestException

# Try to import optional dependencies
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    print("⚠️  Warning: pandas not installed. Using csv module (slower for large files)")
    print("   Install: pip install pandas")

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(text: str):
    """Print colored header."""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{text}{Colors.ENDC}")


def print_success(text: str):
    """Print success message."""
    print(f"{Colors.OKGREEN}{text}{Colors.ENDC}")


def print_warning(text: str):
    """Print warning message."""
    print(f"{Colors.WARNING}{text}{Colors.ENDC}")


def print_error(text: str):
    """Print error message."""
    print(f"{Colors.FAIL}{text}{Colors.ENDC}")


def print_info(text: str):
    """Print info message."""
    print(f"{Colors.OKCYAN}{text}{Colors.ENDC}")


def load_csv_pandas(filepath: Path) -> List[Dict[str, Any]]:
    """Load CSV using pandas (faster for large files)."""
    df = pd.read_csv(filepath)

    # Convert NaN to None
    df = df.where(pd.notnull(df), None)

    # Convert to list of dicts
    cases = df.to_dict('records')

    return cases


def load_csv_stdlib(filepath: Path) -> List[Dict[str, Any]]:
    """Load CSV using standard library csv module."""
    cases = []

    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert empty strings to None
            case = {k: (None if v == '' else v) for k, v in row.items()}
            cases.append(case)

    return cases


def load_test_cases(filepath: Path, verbose: bool = False) -> List[Dict[str, Any]]:
    """
    Load test cases from CSV file.

    Args:
        filepath: Path to CSV file
        verbose: Print detailed loading info

    Returns:
        List of test case dictionaries
    """
    if not filepath.exists():
        raise FileNotFoundError(f"CSV file not found: {filepath}")

    if verbose:
        print_info(f"Loading test cases from: {filepath}")

    # Use pandas if available (faster), otherwise csv module
    if HAS_PANDAS:
        cases = load_csv_pandas(filepath)
        if verbose:
            print_info(f"  Loaded using pandas (fast mode)")
    else:
        cases = load_csv_stdlib(filepath)
        if verbose:
            print_info(f"  Loaded using csv module (standard mode)")

    if verbose:
        print_success(f"  Found {len(cases)} test cases")

    return cases


def convert_types(case: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert CSV string values to appropriate types.

    Args:
        case: Test case dictionary

    Returns:
        Converted dictionary
    """
    converted = {}

    # Numeric fields
    numeric_fields = [
        'hb', 'ht', 'rbc', 'mcv', 'mch', 'mchc', 'rdw',
        'wbc', 'anc', 'lymphocytes_abs', 'eosinophils_abs',
        'basophils_abs', 'monocytes_abs', 'plt', 'mpv', 'reticulocytes',
        'ferritin', 'tsat', 'crp', 'ldh', 'bt_indireta',
        'haptoglobin', 'b12', 'folate', 'hba2', 'epo',
        'd_dimer', 'fibrinogenio', 'pt', 'aptt', 'age_years'
    ]

    # Boolean fields
    boolean_fields = [
        'coombs_pos', 'bcr_abl_pos', 'jak2_pos', 'calr_pos',
        'mpl_pos', 'hpn_pos', 'flc_ratio_abnormal',
        'g6pd_deficient', 'pk_deficient'
    ]

    # Morphology boolean fields (with prefix)
    morphology_tokens = [
        'schistocytes', 'spherocytes', 'dacriocytes', 'elliptocytes',
        'target_cells', 'burr_cells', 'acanthocytes', 'sickle_cells',
        'nucleated_rbc', 'blasts', 'left_shift', 'hypersegmented_neutrophils',
        'auer_rods', 'pelger_huet', 'toxic_granulation', 'dohle_bodies',
        'giant_platelets'
    ]

    for key, value in case.items():
        # Skip None values
        if value is None:
            continue

        # Convert numeric fields
        if key in numeric_fields:
            try:
                converted[key] = float(value)
            except (ValueError, TypeError):
                print_warning(f"  Warning: Could not convert {key}={value} to float, skipping")
                continue

        # Convert boolean fields
        elif key in boolean_fields:
            if isinstance(value, str):
                if value.lower() in ['true', '1', 'yes']:
                    converted[key] = True
                elif value.lower() in ['false', '0', 'no']:
                    converted[key] = False
                # Else: skip (treat as None/unknown)
            elif isinstance(value, bool):
                converted[key] = value

        # Convert morphology tokens (with prefix)
        elif key.startswith('morphology.'):
            token = key.replace('morphology.', '')
            if token in morphology_tokens:
                if 'morphology' not in converted:
                    converted['morphology'] = {}

                if isinstance(value, str):
                    if value.lower() in ['true', '1', 'yes']:
                        converted['morphology'][token] = True
                    elif value.lower() in ['false', '0', 'no']:
                        converted['morphology'][token] = False
                elif isinstance(value, bool):
                    converted['morphology'][token] = value

        # Keep string fields as-is
        elif key in ['sex', 'case_id', 'site_id', 'expected_syndrome', 'notes']:
            converted[key] = str(value)

    return converted


def check_api_health(api_url: str, verbose: bool = False) -> bool:
    """
    Check if API is healthy.

    Args:
        api_url: Base API URL
        verbose: Print detailed info

    Returns:
        True if healthy, False otherwise
    """
    health_url = f"{api_url}/health"

    try:
        response = requests.get(health_url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if data.get('status') == 'healthy':
            if verbose:
                print_success(f"✅ API health check: OK")
                print_info(f"   Version: {data.get('version', 'unknown')}")
                print_info(f"   YAMLs loaded: {data.get('yamls_loaded', 'unknown')}")
            return True
        else:
            print_error(f"❌ API unhealthy: {data.get('error', 'unknown error')}")
            return False

    except RequestException as e:
        print_error(f"❌ API health check failed: {e}")
        print_info(f"   Make sure API is running at: {api_url}")
        print_info(f"   Start with: uvicorn hemodoctor.api.main:app --reload")
        return False


def analyze_case(case: Dict[str, Any], api_url: str, verbose: bool = False) -> Optional[Dict[str, Any]]:
    """
    Analyze a single CBC case via API.

    Args:
        case: CBC data dictionary
        api_url: Base API URL
        verbose: Print detailed info

    Returns:
        API response dictionary or None on error
    """
    analyze_url = f"{api_url}/analyze"

    # Extract metadata (not sent to API)
    case_id = case.pop('case_id', 'UNKNOWN')
    expected_syndrome = case.pop('expected_syndrome', None)
    notes = case.pop('notes', None)

    try:
        response = requests.post(analyze_url, json=case, timeout=30)
        response.raise_for_status()

        result = response.json()

        # Add metadata back to result
        result['case_id'] = case_id
        result['expected_syndrome'] = expected_syndrome
        result['notes'] = notes

        return result

    except RequestException as e:
        print_error(f"  API error for case {case_id}: {e}")
        if verbose and hasattr(e, 'response') and e.response is not None:
            print_error(f"    Response: {e.response.text[:200]}")
        return None


def parse_expected_syndromes(expected: Optional[str]) -> List[str]:
    """
    Parse expected syndrome string to list.

    Args:
        expected: Comma or plus separated syndrome IDs

    Returns:
        List of syndrome IDs

    Examples:
        "S-NORMAL" -> ["S-NORMAL"]
        "S-PLT-CRITICA,S-ANEMIA-GRAVE" -> ["S-PLT-CRITICA", "S-ANEMIA-GRAVE"]
        "S-PLT-CRITICA+S-ANEMIA-GRAVE" -> ["S-PLT-CRITICA", "S-ANEMIA-GRAVE"]
    """
    if not expected:
        return []

    # Split by comma or plus
    syndromes = expected.replace('+', ',').split(',')

    # Strip whitespace
    syndromes = [s.strip() for s in syndromes if s.strip()]

    return syndromes


def compare_syndromes(detected: List[str], expected: List[str]) -> Tuple[str, str]:
    """
    Compare detected vs expected syndromes.

    Args:
        detected: Detected syndrome IDs
        expected: Expected syndrome IDs

    Returns:
        Tuple of (status, message)
        status: 'PASS' | 'PARTIAL' | 'FAIL' | 'SKIP'
    """
    # No expected syndromes -> can't validate
    if not expected:
        return 'SKIP', 'No expected syndrome specified'

    detected_set = set(detected)
    expected_set = set(expected)

    # Exact match
    if detected_set == expected_set:
        return 'PASS', f'Exact match: {", ".join(sorted(detected))}'

    # Partial match (some overlap)
    overlap = detected_set & expected_set
    if overlap:
        missing = expected_set - detected_set
        extra = detected_set - expected_set
        msg = f'Partial match: {", ".join(sorted(overlap))}'
        if missing:
            msg += f' (missing: {", ".join(sorted(missing))})'
        if extra:
            msg += f' (extra: {", ".join(sorted(extra))})'
        return 'PARTIAL', msg

    # No match
    return 'FAIL', f'Expected: {", ".join(sorted(expected))}, Got: {", ".join(sorted(detected))}'


def calculate_metrics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate test metrics.

    Args:
        results: List of test results

    Returns:
        Dictionary of metrics
    """
    total = len(results)
    passed = sum(1 for r in results if r['status'] == 'PASS')
    failed = sum(1 for r in results if r['status'] == 'FAIL')
    partial = sum(1 for r in results if r['status'] == 'PARTIAL')
    skipped = sum(1 for r in results if r['status'] == 'SKIP')
    errors = sum(1 for r in results if r['status'] == 'ERROR')

    # Calculate syndrome-level metrics (for non-skipped cases)
    validated = total - skipped - errors
    if validated > 0:
        # True Positives: syndromes correctly detected
        # False Positives: syndromes detected but not expected
        # False Negatives: syndromes expected but not detected
        tp = 0
        fp = 0
        fn = 0

        for r in results:
            if r['status'] in ['PASS', 'PARTIAL', 'FAIL']:
                expected_set = set(parse_expected_syndromes(r['expected_syndrome']))
                detected_set = set(r['top_syndromes'])

                tp += len(expected_set & detected_set)  # Overlap
                fp += len(detected_set - expected_set)  # Extra detections
                fn += len(expected_set - detected_set)  # Missed detections

        sensitivity = tp / (tp + fn) * 100 if (tp + fn) > 0 else 0
        precision = tp / (tp + fp) * 100 if (tp + fp) > 0 else 0
    else:
        tp = fp = fn = 0
        sensitivity = precision = 0

    return {
        'total': total,
        'passed': passed,
        'failed': failed,
        'partial': partial,
        'skipped': skipped,
        'errors': errors,
        'pass_rate': passed / total * 100 if total > 0 else 0,
        'tp': tp,
        'fp': fp,
        'fn': fn,
        'sensitivity': sensitivity,
        'precision': precision,
    }


def print_progress(case_num: int, total: int, case_id: str, status: str, message: str):
    """Print progress for single case."""
    # Progress indicator
    progress = f"  {case_num}/{total}"

    # Status emoji and color
    if status == 'PASS':
        status_str = f"{Colors.OKGREEN}✅ PASS{Colors.ENDC}"
    elif status == 'PARTIAL':
        status_str = f"{Colors.WARNING}⚠️  PARTIAL{Colors.ENDC}"
    elif status == 'FAIL':
        status_str = f"{Colors.FAIL}❌ FAIL{Colors.ENDC}"
    elif status == 'SKIP':
        status_str = f"{Colors.OKCYAN}⏭️  SKIP{Colors.ENDC}"
    else:  # ERROR
        status_str = f"{Colors.FAIL}💥 ERROR{Colors.ENDC}"

    print(f"{progress} {case_id}: {status_str} ({message})")


def save_results(results: List[Dict[str, Any]], output_path: Path, verbose: bool = False):
    """
    Save results to CSV file.

    Args:
        results: List of test results
        output_path: Output CSV path
        verbose: Print detailed info
    """
    if not results:
        print_warning("No results to save")
        return

    # Define output columns
    columns = [
        'case_id', 'status', 'message',
        'expected_syndrome', 'detected_syndromes',
        'evidences_count', 'next_steps_count',
        'route_id', 'timestamp', 'notes'
    ]

    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()

        for r in results:
            row = {
                'case_id': r.get('case_id', 'UNKNOWN'),
                'status': r.get('status', 'UNKNOWN'),
                'message': r.get('message', ''),
                'expected_syndrome': r.get('expected_syndrome', ''),
                'detected_syndromes': ','.join(r.get('top_syndromes', [])),
                'evidences_count': len(r.get('evidences_present', [])),
                'next_steps_count': len(r.get('next_steps', [])),
                'route_id': r.get('route_id', ''),
                'timestamp': r.get('timestamp', ''),
                'notes': r.get('notes', ''),
            }
            writer.writerow(row)

    if verbose:
        print_success(f"  Results saved to: {output_path}")


def save_report(metrics: Dict[str, Any], results: List[Dict[str, Any]],
                report_path: Path, verbose: bool = False):
    """
    Save test report to text file.

    Args:
        metrics: Test metrics
        results: List of test results
        report_path: Output report path
        verbose: Print detailed info
    """
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("HemoDoctor CSV Testing Report\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Cases: {metrics['total']}\n\n")

        f.write("SUMMARY\n")
        f.write("-" * 80 + "\n")
        f.write(f"  Passed:  {metrics['passed']} ({metrics['pass_rate']:.1f}%)\n")
        f.write(f"  Failed:  {metrics['failed']}\n")
        f.write(f"  Partial: {metrics['partial']}\n")
        f.write(f"  Skipped: {metrics['skipped']}\n")
        f.write(f"  Errors:  {metrics['errors']}\n\n")

        f.write("METRICS\n")
        f.write("-" * 80 + "\n")
        f.write(f"  True Positives:  {metrics['tp']}\n")
        f.write(f"  False Positives: {metrics['fp']}\n")
        f.write(f"  False Negatives: {metrics['fn']}\n")
        f.write(f"  Sensitivity:     {metrics['sensitivity']:.1f}%\n")
        f.write(f"  Precision:       {metrics['precision']:.1f}%\n\n")

        # Failed cases details
        failed_cases = [r for r in results if r['status'] == 'FAIL']
        if failed_cases:
            f.write("FAILED CASES\n")
            f.write("-" * 80 + "\n")
            for r in failed_cases:
                f.write(f"  {r['case_id']}: {r['message']}\n")
                if r.get('notes'):
                    f.write(f"    Notes: {r['notes']}\n")
            f.write("\n")

        # Partial cases details
        partial_cases = [r for r in results if r['status'] == 'PARTIAL']
        if partial_cases:
            f.write("PARTIAL MATCHES\n")
            f.write("-" * 80 + "\n")
            for r in partial_cases:
                f.write(f"  {r['case_id']}: {r['message']}\n")
            f.write("\n")

        f.write("=" * 80 + "\n")
        f.write("End of Report\n")

    if verbose:
        print_success(f"  Report saved to: {report_path}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Test HemoDoctor CDSS API using CSV input files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage
  python scripts/test_csv.py --input test_cases.csv

  # Save results to custom file
  python scripts/test_csv.py --input test_cases.csv --output my_results.csv

  # Verbose mode with custom API URL
  python scripts/test_csv.py --input test_cases.csv --api http://prod:8000 --verbose

  # Generate report only
  python scripts/test_csv.py --input test_cases.csv --report-only
        """
    )

    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Input CSV file with test cases'
    )

    parser.add_argument(
        '--output', '-o',
        type=Path,
        default=Path('results.csv'),
        help='Output CSV file for results (default: results.csv)'
    )

    parser.add_argument(
        '--report', '-r',
        type=Path,
        default=Path('test_report.txt'),
        help='Output text file for report (default: test_report.txt)'
    )

    parser.add_argument(
        '--api',
        type=str,
        default='http://localhost:8000',
        help='API base URL (default: http://localhost:8000)'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )

    parser.add_argument(
        '--report-only',
        action='store_true',
        help='Generate report without running tests (requires existing results.csv)'
    )

    args = parser.parse_args()

    # Print header
    print_header("=" * 80)
    print_header("HemoDoctor CSV Testing Script v1.0")
    print_header("=" * 80)

    # Report-only mode
    if args.report_only:
        print_info("\nReport-only mode: Loading existing results...")
        # TODO: Implement loading existing results
        print_error("Report-only mode not yet implemented")
        return 1

    # Load test cases
    print_info(f"\nLoading test cases from: {args.input}")
    try:
        cases = load_test_cases(args.input, verbose=args.verbose)
    except Exception as e:
        print_error(f"Failed to load test cases: {e}")
        return 1

    print_success(f"Found {len(cases)} cases to test")

    # Check API health
    print_info(f"\nTesting API at: {args.api}/analyze")
    if not check_api_health(args.api, verbose=args.verbose):
        print_error("\nAPI health check failed. Exiting.")
        return 1

    # Process cases
    print_info("\nProcessing cases:")
    results = []
    start_time = time.time()

    for i, case in enumerate(cases, 1):
        # Convert types
        converted_case = convert_types(case)

        # Extract case_id for logging
        case_id = case.get('case_id', f'CASE-{i:03d}')
        expected = case.get('expected_syndrome')

        # Analyze case
        result = analyze_case(converted_case, args.api, verbose=args.verbose)

        if result is None:
            # API error
            status = 'ERROR'
            message = 'API request failed'
            result = {
                'case_id': case_id,
                'expected_syndrome': expected,
                'top_syndromes': [],
                'evidences_present': [],
                'next_steps': [],
                'route_id': '',
                'timestamp': '',
                'notes': case.get('notes', ''),
            }
        else:
            # Compare results
            detected = result.get('top_syndromes', [])
            expected_list = parse_expected_syndromes(expected)
            status, message = compare_syndromes(detected, expected_list)

        # Add status to result
        result['status'] = status
        result['message'] = message

        # Print progress
        print_progress(i, len(cases), case_id, status, message)

        results.append(result)

    elapsed = time.time() - start_time

    # Calculate metrics
    print_info("\nCalculating metrics...")
    metrics = calculate_metrics(results)

    # Print summary
    print_header("\nRESULTS")
    print_info(f"  Total:   {metrics['total']}")
    print_success(f"  Passed:  {metrics['passed']} ({metrics['pass_rate']:.1f}%)")
    if metrics['failed'] > 0:
        print_error(f"  Failed:  {metrics['failed']}")
    if metrics['partial'] > 0:
        print_warning(f"  Partial: {metrics['partial']}")
    if metrics['skipped'] > 0:
        print_info(f"  Skipped: {metrics['skipped']}")
    if metrics['errors'] > 0:
        print_error(f"  Errors:  {metrics['errors']}")

    print_header("\nMETRICS")
    print_info(f"  True Positives:  {metrics['tp']}")
    print_info(f"  False Positives: {metrics['fp']}")
    print_info(f"  False Negatives: {metrics['fn']}")
    print_success(f"  Sensitivity:     {metrics['sensitivity']:.1f}%")
    print_success(f"  Precision:       {metrics['precision']:.1f}%")

    print_header("\nPERFORMANCE")
    print_info(f"  Total time:      {elapsed:.1f}s")
    print_info(f"  Avg per case:    {elapsed/len(cases):.2f}s")

    # Save results
    print_info("\nSaving results...")
    save_results(results, args.output, verbose=args.verbose)
    save_report(metrics, results, args.report, verbose=args.verbose)

    print_success(f"\n✅ Testing complete!")
    print_info(f"  Results: {args.output}")
    print_info(f"  Report:  {args.report}")

    # Exit code based on pass rate
    if metrics['pass_rate'] == 100:
        return 0
    elif metrics['pass_rate'] >= 80:
        return 0  # Still success if ≥80%
    else:
        return 1  # Fail if <80%


if __name__ == '__main__':
    sys.exit(main())
