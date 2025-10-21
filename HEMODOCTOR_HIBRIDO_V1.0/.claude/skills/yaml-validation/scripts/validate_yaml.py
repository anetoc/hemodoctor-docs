#!/usr/bin/env python3
"""
Validate a single YAML file for HemoDoctor Hybrid V1.0

Usage:
    python validate_yaml.py <path_to_yaml>

Exit codes:
    0 - Validation passed
    1 - Validation failed
"""

import sys
import yaml
from pathlib import Path


def validate_yaml(file_path):
    """Validate YAML syntax and basic structure"""

    try:
        # Check file exists
        path = Path(file_path)
        if not path.exists():
            print(f"❌ ERROR: File not found: {file_path}")
            return False

        # Parse YAML
        with open(path, 'r') as f:
            data = yaml.safe_load(f)

        if data is None:
            print(f"❌ ERROR: Empty YAML file: {file_path}")
            return False

        # Basic structure checks
        if not isinstance(data, dict):
            print(f"❌ ERROR: YAML root must be a dictionary")
            return False

        # File-specific validation
        file_name = path.name

        if file_name.startswith('02_evidence'):
            # Evidence file should have 'evidences' key
            if 'evidences' not in data:
                print(f"⚠️  WARNING: Evidence file missing 'evidences' key")

        elif file_name.startswith('03_syndromes'):
            # Syndrome file should have 'syndromes' key
            if 'syndromes' not in data:
                print(f"⚠️  WARNING: Syndrome file missing 'syndromes' key")

        # Success
        print(f"✅ PASSED: {file_path}")
        return True

    except yaml.YAMLError as e:
        print(f"❌ YAML SYNTAX ERROR in {file_path}:")
        print(f"   {str(e)}")
        return False

    except Exception as e:
        print(f"❌ ERROR validating {file_path}:")
        print(f"   {str(e)}")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_yaml.py <path_to_yaml>")
        sys.exit(1)

    file_path = sys.argv[1]
    success = validate_yaml(file_path)

    sys.exit(0 if success else 1)
