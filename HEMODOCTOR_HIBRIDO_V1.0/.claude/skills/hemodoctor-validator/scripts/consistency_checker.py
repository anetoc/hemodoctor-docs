#!/usr/bin/env python3
"""
HemoDoctor Consistency Checker
Validates consistency across multiple YAML files
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, Set, List


class ConsistencyChecker:
    """Check consistency between related YAML files"""
    
    def __init__(self):
        self.schema_fields = set()
        self.config_units = set()
        self.evidence_ids = set()
        self.syndrome_ids = set()
        self.errors = []
        self.warnings = []
    
    def load_schema(self, schema_file: str) -> bool:
        """Load 01_schema_hybrid.yaml"""
        try:
            with open(schema_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if 'fields' in data:
                for field in data['fields']:
                    if 'name' in field:
                        self.schema_fields.add(field['name'])
            
            print(f"✓ Loaded {len(self.schema_fields)} schema fields")
            return True
        except Exception as e:
            self.errors.append(f"Failed to load schema: {e}")
            return False
    
    def load_config(self, config_file: str) -> bool:
        """Load 00_config_hybrid.yaml"""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if 'units' in data:
                self.config_units = set(data['units'].keys())
            
            print(f"✓ Loaded {len(self.config_units)} config units")
            return True
        except Exception as e:
            self.errors.append(f"Failed to load config: {e}")
            return False
    
    def load_evidence(self, evidence_file: str) -> bool:
        """Load 02_evidence_hybrid.yaml"""
        try:
            with open(evidence_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if 'evidences' in data:
                for ev in data['evidences']:
                    if 'id' in ev:
                        self.evidence_ids.add(ev['id'])
            
            print(f"✓ Loaded {len(self.evidence_ids)} evidence IDs")
            return True
        except Exception as e:
            self.errors.append(f"Failed to load evidence: {e}")
            return False
    
    def load_syndromes(self, syndrome_file: str) -> bool:
        """Load 03_syndromes_hybrid.yaml"""
        try:
            with open(syndrome_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if 'syndromes' in data:
                for syn in data['syndromes']:
                    if 'id' in syn:
                        self.syndrome_ids.add(syn['id'])
            
            print(f"✓ Loaded {len(self.syndrome_ids)} syndrome IDs")
            return True
        except Exception as e:
            self.errors.append(f"Failed to load syndromes: {e}")
            return False
    
    def check_schema_config_consistency(self):
        """Check if schema fields have units in config"""
        missing_units = []
        
        for field in self.schema_fields:
            if field not in self.config_units:
                # Some fields may not need units (enums, booleans, etc.)
                if field not in ['sex', 'age_years']:
                    missing_units.append(field)
        
        if missing_units:
            self.warnings.append(
                f"Schema fields without units in config ({len(missing_units)}): {', '.join(sorted(missing_units)[:5])}..."
            )
    
    def check_syndrome_evidence_references(self, syndrome_file: str):
        """Check if syndromes reference valid evidence IDs"""
        try:
            with open(syndrome_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            invalid_refs = []
            
            if 'syndromes' in data:
                for syndrome in data['syndromes']:
                    syndrome_id = syndrome.get('id', 'unknown')
                    evidences = syndrome.get('evidences', [])
                    
                    for ev_id in evidences:
                        if ev_id not in self.evidence_ids:
                            invalid_refs.append(f"{syndrome_id} → {ev_id}")
            
            if invalid_refs:
                self.errors.append(
                    f"Syndromes reference non-existent evidence IDs ({len(invalid_refs)}): {invalid_refs[:3]}"
                )
        
        except Exception as e:
            self.errors.append(f"Failed to check syndrome-evidence refs: {e}")
    
    def check_field_usage(self, evidence_file: str):
        """Check if evidence rules reference valid schema fields"""
        try:
            with open(evidence_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            referenced_fields = set()
            
            if 'evidences' in data:
                for evidence in data['evidences']:
                    # Extract field names from conditions (simple heuristic)
                    condition = evidence.get('condition', '')
                    for field in self.schema_fields:
                        if field in condition:
                            referenced_fields.add(field)
            
            unused_fields = self.schema_fields - referenced_fields
            
            if unused_fields:
                self.warnings.append(
                    f"Schema fields not used in evidence rules ({len(unused_fields)}): {', '.join(sorted(unused_fields)[:5])}..."
                )
        
        except Exception as e:
            self.warnings.append(f"Could not check field usage: {e}")
    
    def print_report(self):
        """Print consistency report"""
        print("\n" + "="*60)
        print("CONSISTENCY REPORT")
        print("="*60)
        
        if not self.errors and not self.warnings:
            print("\n✅ All consistency checks passed!")
            return True
        
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")
        
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        print("="*60)
        return len(self.errors) == 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python consistency_checker.py <yaml_directory>")
        print("\nExample:")
        print("  python consistency_checker.py /path/to/yamls/")
        sys.exit(1)
    
    yaml_dir = Path(sys.argv[1])
    
    if not yaml_dir.is_dir():
        print(f"❌ Directory not found: {yaml_dir}")
        sys.exit(1)
    
    checker = ConsistencyChecker()
    
    print("🔍 Checking consistency across YAML files...\n")
    
    # Load files
    schema_file = yaml_dir / "01_schema_hybrid.yaml"
    config_file = yaml_dir / "00_config_hybrid.yaml"
    evidence_file = yaml_dir / "02_evidence_hybrid.yaml"
    syndrome_file = yaml_dir / "03_syndromes_hybrid.yaml"
    
    files_loaded = True
    
    if schema_file.exists():
        files_loaded &= checker.load_schema(str(schema_file))
    else:
        checker.warnings.append(f"Schema file not found: {schema_file.name}")
    
    if config_file.exists():
        files_loaded &= checker.load_config(str(config_file))
    else:
        checker.warnings.append(f"Config file not found: {config_file.name}")
    
    if evidence_file.exists():
        files_loaded &= checker.load_evidence(str(evidence_file))
    else:
        checker.warnings.append(f"Evidence file not found: {evidence_file.name}")
    
    if syndrome_file.exists():
        files_loaded &= checker.load_syndromes(str(syndrome_file))
    else:
        checker.warnings.append(f"Syndrome file not found: {syndrome_file.name}")
    
    print()
    
    # Run consistency checks
    if checker.schema_fields and checker.config_units:
        checker.check_schema_config_consistency()
    
    if checker.syndrome_ids and checker.evidence_ids and syndrome_file.exists():
        checker.check_syndrome_evidence_references(str(syndrome_file))
    
    if checker.schema_fields and checker.evidence_ids and evidence_file.exists():
        checker.check_field_usage(str(evidence_file))
    
    success = checker.print_report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
