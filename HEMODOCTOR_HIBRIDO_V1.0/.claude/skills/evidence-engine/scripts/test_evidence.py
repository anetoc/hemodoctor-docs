#!/usr/bin/env python3
"""
Test a single evidence rule with sample CBC data

Usage:
    python test_evidence.py E-ANC-CRIT --anc=0.3
    python test_evidence.py E-MICROCYTOSIS --mcv=72

This is a simplified tester for quick validation.
For production use, implement full simpleeval integration.
"""

import sys
import yaml
from pathlib import Path


def test_evidence(evidence_id, cbc_data):
    """Test an evidence rule with sample data"""

    # Load evidences
    yaml_path = Path("YAMLs/02_evidence_hybrid.yaml")
    if not yaml_path.exists():
        print("❌ ERROR: YAMLs/02_evidence_hybrid.yaml not found")
        sys.exit(1)

    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    # Find evidence
    evidence = None
    for ev in data.get('evidences', []):
        if ev.get('id') == evidence_id:
            evidence = ev
            break

    if not evidence:
        print(f"❌ ERROR: Evidence '{evidence_id}' not found")
        sys.exit(1)

    # Display evidence
    print(f"\n{'='*60}")
    print(f"Testing: {evidence_id}")
    print(f"{'='*60}")
    print(f"Strength: {evidence.get('strength', 'unknown')}")
    print(f"Rule: {evidence.get('rule', 'NO_RULE')}")
    print(f"Requires: {', '.join(evidence.get('requires', []))}")

    # Check required fields
    print(f"\n{'='*60}")
    print("Input data:")
    print(f"{'='*60}")

    missing = []
    for field in evidence.get('requires', []):
        value = cbc_data.get(field)
        if value is not None:
            print(f"✅ {field} = {value}")
        else:
            print(f"❌ {field} = MISSING")
            missing.append(field)

    if missing:
        print(f"\n⚠️  RESULT: UNKNOWN (missing fields: {', '.join(missing)})")
        print("\nTo test this evidence, provide the required fields:")
        for field in missing:
            print(f"  --{field}=VALUE")
        sys.exit(0)

    # Note about evaluation
    print(f"\n{'='*60}")
    print("Evaluation:")
    print(f"{'='*60}")
    print("⚠️  NOTE: This is a simplified tester.")
    print("For actual evaluation, implement using simpleeval:")
    print()
    print("from simpleeval import simple_eval")
    print()
    print(f"result = simple_eval(")
    print(f"    '{evidence.get('rule')}',")
    print(f"    names={cbc_data}")
    print(")")
    print()
    print("See SKILL.md for full implementation example.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_evidence.py E-XXX --field=value [--field2=value2 ...]")
        print("\nExample:")
        print("  python test_evidence.py E-ANC-CRIT --anc=0.3")
        sys.exit(1)

    evidence_id = sys.argv[1]

    # Parse CBC data from command line
    cbc_data = {}
    for arg in sys.argv[2:]:
        if arg.startswith('--'):
            try:
                key, value = arg[2:].split('=')
                # Try to convert to number
                try:
                    cbc_data[key] = float(value)
                except ValueError:
                    # Keep as string (for morphology etc)
                    if value.lower() == 'true':
                        cbc_data[key] = True
                    elif value.lower() == 'false':
                        cbc_data[key] = False
                    else:
                        cbc_data[key] = value
            except ValueError:
                print(f"⚠️  Warning: Invalid argument format: {arg}")

    test_evidence(evidence_id, cbc_data)
