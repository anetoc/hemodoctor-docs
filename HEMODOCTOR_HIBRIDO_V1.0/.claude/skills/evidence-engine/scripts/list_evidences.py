#!/usr/bin/env python3
"""
List all 75 evidence rules from 02_evidence_hybrid.yaml

Usage:
    python list_evidences.py [--category CATEGORY]

Options:
    --category    Filter by category (critical_gates, red_series, white_series, platelet_series, coagulation, complementary)
"""

import sys
import yaml
from pathlib import Path


def list_evidences(category_filter=None):
    """List all evidences, optionally filtered by category"""

    # Load evidences YAML
    yaml_path = Path("YAMLs/02_evidence_hybrid.yaml")
    if not yaml_path.exists():
        print("❌ ERROR: YAMLs/02_evidence_hybrid.yaml not found")
        sys.exit(1)

    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)

    if 'evidences' not in data:
        print("❌ ERROR: No 'evidences' key found in YAML")
        sys.exit(1)

    evidences = data['evidences']

    # Group by category
    by_category = {}
    for evidence in evidences:
        category = evidence.get('category', 'unknown')
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(evidence)

    # Filter if requested
    if category_filter:
        if category_filter not in by_category:
            print(f"❌ ERROR: Category '{category_filter}' not found")
            print(f"Available categories: {', '.join(by_category.keys())}")
            sys.exit(1)
        by_category = {category_filter: by_category[category_filter]}

    # Display
    total = 0
    for category, evs in sorted(by_category.items()):
        print(f"\n{'='*60}")
        print(f"{category.upper().replace('_', ' ')} ({len(evs)} evidences)")
        print(f"{'='*60}")

        for ev in sorted(evs, key=lambda x: x.get('id', '')):
            ev_id = ev.get('id', 'NO_ID')
            strength = ev.get('strength', 'unknown')
            rule = ev.get('rule', 'NO_RULE')

            print(f"\n{ev_id} [{strength}]")
            print(f"  Rule: {rule}")

            if 'requires' in ev:
                print(f"  Requires: {', '.join(ev['requires'])}")

        total += len(evs)

    print(f"\n{'='*60}")
    print(f"TOTAL: {total} evidences")
    print(f"{'='*60}")


if __name__ == "__main__":
    category = None
    if len(sys.argv) > 1:
        if sys.argv[1] == '--category' and len(sys.argv) > 2:
            category = sys.argv[2]
        else:
            print("Usage: python list_evidences.py [--category CATEGORY]")
            sys.exit(1)

    list_evidences(category)
