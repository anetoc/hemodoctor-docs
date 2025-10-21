#!/usr/bin/env python3
"""
Validate all 15 YAML files in the YAMLs/ directory

Usage:
    python validate_all.py

Exit codes:
    0 - All validations passed
    1 - One or more validations failed
"""

import sys
from pathlib import Path
import yaml


YAML_FILES = [
    "00_config_hybrid.yaml",
    "01_schema_hybrid.yaml",
    "02_evidence_hybrid.yaml",
    "03_syndromes_hybrid.yaml",
    "04_output_templates_hybrid.yaml",
    "05_missingness_hybrid_v2.3.yaml",
    "05_missingness_hybrid.yaml",  # Legacy version
    "06_route_policy_hybrid.yaml",
    "07_conflict_matrix_hybrid.yaml",
    "07_normalization_heuristics.yaml",
    "08_wormlog_hybrid.yaml",
    "09_next_steps_engine_hybrid.yaml",
    "10_runbook_hybrid.yaml",
    "11_case_state_hybrid.yaml",
    "12_output_policies_hybrid.yaml",
]


def validate_yaml(file_path):
    """Validate a single YAML file"""
    try:
        with open(file_path, 'r') as f:
            yaml.safe_load(f)
        return True, None
    except yaml.YAMLError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)


def main():
    """Validate all YAML files"""

    # Find YAMLs directory
    yamls_dir = Path("YAMLs")
    if not yamls_dir.exists():
        print("❌ ERROR: YAMLs/ directory not found")
        print("   Run this script from the project root directory")
        sys.exit(1)

    print("🔍 Validating HemoDoctor Hybrid V1.0 YAMLs...\n")

    passed = 0
    failed = 0
    errors = []

    for yaml_file in YAML_FILES:
        file_path = yamls_dir / yaml_file

        # Skip if file doesn't exist (e.g., legacy versions)
        if not file_path.exists():
            print(f"⏭️  SKIP: {yaml_file} (not found)")
            continue

        # Validate
        success, error = validate_yaml(file_path)

        if success:
            print(f"✅ PASSED: {yaml_file}")
            passed += 1
        else:
            print(f"❌ FAILED: {yaml_file}")
            print(f"   Error: {error}")
            failed += 1
            errors.append((yaml_file, error))

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY: {passed} passed, {failed} failed")
    print(f"{'='*60}")

    if failed > 0:
        print("\n❌ ERRORS FOUND:")
        for yaml_file, error in errors:
            print(f"\n{yaml_file}:")
            print(f"  {error}")
        sys.exit(1)
    else:
        print("\n✅ All YAML files validated successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
