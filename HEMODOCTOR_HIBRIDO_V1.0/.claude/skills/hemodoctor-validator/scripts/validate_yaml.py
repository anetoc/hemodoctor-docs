#!/usr/bin/env python3
"""
HemoDoctor YAML Validator
Validates clinical rule YAMLs against schema and consistency checks
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Any
import json


class HemoDoctorValidator:
    """Main validator for HemoDoctor YAML files"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.schema = None
        self.config = None
        
    def validate_file(self, file_path: str) -> bool:
        """Validate a single YAML file"""
        path = Path(file_path)
        
        if not path.exists():
            self.errors.append(f"File not found: {file_path}")
            return False
            
        if not path.suffix in ['.yaml', '.yml']:
            self.errors.append(f"Not a YAML file: {file_path}")
            return False
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            self.errors.append(f"YAML syntax error in {path.name}: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Failed to read {path.name}: {e}")
            return False
        
        # Validate based on file type
        file_name = path.stem
        
        if file_name.startswith('00_config'):
            return self._validate_config(data, path.name)
        elif file_name.startswith('01_schema'):
            return self._validate_schema(data, path.name)
        elif file_name.startswith('02_evidence'):
            return self._validate_evidence(data, path.name)
        elif file_name.startswith('03_syndromes'):
            return self._validate_syndromes(data, path.name)
        elif file_name.startswith('05_missingness'):
            return self._validate_missingness(data, path.name)
        elif file_name.startswith('09_next_steps'):
            return self._validate_next_steps(data, path.name)
        else:
            self.warnings.append(f"Unknown YAML type: {path.name} (skipping validation)")
            return True
    
    def _validate_config(self, data: Dict, filename: str) -> bool:
        """Validate 00_config_hybrid.yaml"""
        required_keys = ['version', 'units', 'cutoffs', 'age_groups']
        
        for key in required_keys:
            if key not in data:
                self.errors.append(f"{filename}: Missing required key '{key}'")
                return False
        
        # Store config for cross-validation
        self.config = data
        
        # Validate units
        if 'units' in data:
            for field, unit in data['units'].items():
                if not isinstance(unit, str):
                    self.errors.append(f"{filename}: Invalid unit for '{field}': {unit}")
        
        # Validate cutoffs
        if 'cutoffs' in data:
            for cutoff, value in data['cutoffs'].items():
                if isinstance(value, dict):
                    for sub_key, sub_val in value.items():
                        if not isinstance(sub_val, (int, float, str)):
                            self.warnings.append(f"{filename}: Unusual cutoff value for '{cutoff}.{sub_key}': {sub_val}")
        
        return len(self.errors) == 0
    
    def _validate_schema(self, data: Dict, filename: str) -> bool:
        """Validate 01_schema_hybrid.yaml"""
        if 'fields' not in data:
            self.errors.append(f"{filename}: Missing 'fields' key")
            return False
        
        # Store schema for cross-validation
        self.schema = data
        
        required_fields = ['hb', 'mcv', 'wbc', 'plt', 'age_years', 'sex']
        fields = data.get('fields', [])
        field_names = [f.get('name') for f in fields]
        
        for req_field in required_fields:
            if req_field not in field_names:
                self.errors.append(f"{filename}: Missing required field '{req_field}'")
        
        # Validate field structure
        for field in fields:
            if 'name' not in field:
                self.errors.append(f"{filename}: Field missing 'name' attribute")
                continue
            
            field_name = field['name']
            
            if 'type' not in field:
                self.errors.append(f"{filename}: Field '{field_name}' missing 'type'")
            
            if field.get('required') and 'unit' not in field and field.get('type') not in ['enum', 'tri_bool']:
                self.warnings.append(f"{filename}: Required field '{field_name}' missing 'unit'")
        
        return len(self.errors) == 0
    
    def _validate_evidence(self, data: Dict, filename: str) -> bool:
        """Validate 02_evidence_hybrid.yaml"""
        if 'evidences' not in data:
            self.errors.append(f"{filename}: Missing 'evidences' key")
            return False
        
        evidences = data['evidences']
        evidence_ids = set()
        
        for evidence in evidences:
            if 'id' not in evidence:
                self.errors.append(f"{filename}: Evidence missing 'id'")
                continue
            
            ev_id = evidence['id']
            
            # Check for duplicates
            if ev_id in evidence_ids:
                self.errors.append(f"{filename}: Duplicate evidence ID '{ev_id}'")
            evidence_ids.add(ev_id)
            
            # Validate required fields
            required = ['id', 'category', 'description', 'weight']
            for key in required:
                if key not in evidence:
                    self.errors.append(f"{filename}: Evidence '{ev_id}' missing '{key}'")
            
            # Validate category
            valid_categories = ['critical', 'strong', 'moderate', 'weak']
            if evidence.get('category') not in valid_categories:
                self.errors.append(f"{filename}: Evidence '{ev_id}' has invalid category: {evidence.get('category')}")
            
            # Validate weight
            weight = evidence.get('weight')
            if weight is not None and not (0 <= weight <= 1):
                self.warnings.append(f"{filename}: Evidence '{ev_id}' has unusual weight: {weight}")
        
        print(f"✓ Found {len(evidence_ids)} unique evidences")
        return len(self.errors) == 0
    
    def _validate_syndromes(self, data: Dict, filename: str) -> bool:
        """Validate 03_syndromes_hybrid.yaml"""
        
        # HemoDoctor uses categorized syndrome lists
        syndrome_keys = ['critical_syndromes', 'priority_syndromes', 'review_syndromes', 'routine_syndromes']
        
        # Try new structure first (categorized)
        if any(key in data for key in syndrome_keys):
            syndromes = []
            for key in syndrome_keys:
                if key in data:
                    syndromes.extend(data[key])
        # Fallback to flat list
        elif 'syndromes' in data:
            syndromes = data['syndromes']
        else:
            self.errors.append(f"{filename}: Missing syndrome definitions (expected 'syndromes' or categorized lists)")
            return False
        syndrome_ids = set()
        priority_counts = {'critical': 0, 'priority': 0, 'review': 0, 'routine': 0}
        
        # Priority mapping for categorized structure
        priority_map = {
            'critical_syndromes': 'critical',
            'priority_syndromes': 'priority',
            'review_syndromes': 'review',
            'routine_syndromes': 'routine'
        }
        
        for syndrome in syndromes:
            if 'id' not in syndrome:
                self.errors.append(f"{filename}: Syndrome missing 'id'")
                continue
            
            syn_id = syndrome['id']
            
            # Check for duplicates
            if syn_id in syndrome_ids:
                self.errors.append(f"{filename}: Duplicate syndrome ID '{syn_id}'")
            syndrome_ids.add(syn_id)
            
            # Infer priority from structure if needed
            if 'priority' not in syndrome and 'criticality' not in syndrome:
                # Try to infer from the category list it came from
                for key, priority in priority_map.items():
                    if key in data and syndrome in data[key]:
                        syndrome['priority'] = priority
                        break
            
            # Validate priority (can be in 'priority' or 'criticality')
            priority = syndrome.get('priority') or syndrome.get('criticality')
            if priority in priority_counts:
                priority_counts[priority] += 1
            elif priority:
                self.warnings.append(f"{filename}: Syndrome '{syn_id}' has unusual priority: {priority}")
            
            # Validate combine logic (flexible)
            combine = syndrome.get('combine')
            if combine:
                if isinstance(combine, str):
                    # Simple combine: 'all' or 'any'
                    if combine not in ['all', 'any']:
                        self.warnings.append(f"{filename}: Syndrome '{syn_id}' has unusual combine value: {combine}")
                elif isinstance(combine, dict):
                    # Complex combine: {'all': [...], 'any': [...]} - valid in HemoDoctor
                    pass
                else:
                    self.warnings.append(f"{filename}: Syndrome '{syn_id}' has unusual combine type")
            
            # Check evidences field (flexible)
            if 'evidences' not in syndrome and 'combine' not in syndrome:
                self.warnings.append(f"{filename}: Syndrome '{syn_id}' has no evidences or combine logic")
        
        print(f"✓ Found {len(syndrome_ids)} unique syndromes")
        print(f"  Critical: {priority_counts['critical']}")
        print(f"  Priority: {priority_counts['priority']}")
        print(f"  Review: {priority_counts['review']}")
        print(f"  Routine: {priority_counts['routine']}")
        
        # Flexible expected counts - warn if too far off
        total = sum(priority_counts.values())
        if total < 30:
            self.warnings.append(f"{filename}: Found only {total} syndromes, expected ~34")
        elif total > 40:
            self.warnings.append(f"{filename}: Found {total} syndromes, expected ~34")
        
        return len(self.errors) == 0
    
    def _validate_missingness(self, data: Dict, filename: str) -> bool:
        """Validate 05_missingness_hybrid.yaml"""
        if 'missingness_engine' not in data:
            self.errors.append(f"{filename}: Missing 'missingness_engine' key")
            return False
        
        engine = data['missingness_engine']
        
        # Validate proxy logic
        if 'proxy_logic' in engine:
            for proxy in engine['proxy_logic']:
                if 'target' not in proxy or 'proxy_from' not in proxy:
                    self.errors.append(f"{filename}: Proxy rule missing 'target' or 'proxy_from'")
        
        # Validate borderline rules
        if 'borderline_rules' in engine:
            for rule in engine['borderline_rules']:
                if 'condition' not in rule:
                    self.errors.append(f"{filename}: Borderline rule missing 'condition'")
        
        return len(self.errors) == 0
    
    def _validate_next_steps(self, data: Dict, filename: str) -> bool:
        """Validate 09_next_steps_engine_hybrid.yaml"""
        if 'triggers' not in data:
            self.errors.append(f"{filename}: Missing 'triggers' key")
            return False
        
        triggers = data['triggers']
        trigger_ids = set()
        
        for trigger in triggers:
            if 'id' not in trigger:
                self.errors.append(f"{filename}: Trigger missing 'id'")
                continue
            
            trig_id = trigger['id']
            
            # Check for duplicates
            if trig_id in trigger_ids:
                self.errors.append(f"{filename}: Duplicate trigger ID '{trig_id}'")
            trigger_ids.add(trig_id)
            
            # Validate required fields
            required = ['id', 'when', 'suggest']
            for key in required:
                if key not in trigger:
                    self.errors.append(f"{filename}: Trigger '{trig_id}' missing '{key}'")
            
            # Validate 'when' expression (basic check)
            when = trigger.get('when', '')
            if when and not any(op in when for op in ['<', '>', '==', 'and', 'or', 'is']):
                self.warnings.append(f"{filename}: Trigger '{trig_id}' 'when' may be invalid: {when}")
            
            # Validate suggest items
            if 'suggest' in trigger:
                for item in trigger['suggest']:
                    if 'test' not in item:
                        self.errors.append(f"{filename}: Trigger '{trig_id}' suggest missing 'test'")
                    if 'level' not in item:
                        self.errors.append(f"{filename}: Trigger '{trig_id}' suggest missing 'level'")
                    
                    # Validate level
                    valid_levels = ['critical', 'priority', 'routine']
                    if item.get('level') not in valid_levels:
                        self.errors.append(f"{filename}: Invalid level '{item.get('level')}' in trigger '{trig_id}'")
        
        print(f"✓ Found {len(trigger_ids)} triggers")
        
        # Expected 34 triggers from documentation
        if len(trigger_ids) != 34:
            self.warnings.append(f"{filename}: Expected 34 triggers, found {len(trigger_ids)}")
        
        return len(self.errors) == 0
    
    def print_report(self):
        """Print validation report"""
        print("\n" + "="*60)
        print("VALIDATION REPORT")
        print("="*60)
        
        if not self.errors and not self.warnings:
            print("✅ All validations passed!")
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
        print("Usage: python validate_yaml.py <yaml_file_or_directory>")
        print("\nExample:")
        print("  python validate_yaml.py 03_syndromes_hybrid.yaml")
        print("  python validate_yaml.py /path/to/yamls/")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    validator = HemoDoctorValidator()
    
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = sorted(target.glob("*.yaml")) + sorted(target.glob("*.yml"))
    else:
        print(f"❌ Path not found: {target}")
        sys.exit(1)
    
    if not files:
        print(f"❌ No YAML files found in {target}")
        sys.exit(1)
    
    print(f"🔍 Validating {len(files)} YAML file(s)...")
    print()
    
    for file_path in files:
        print(f"📄 {file_path.name}...")
        validator.validate_file(str(file_path))
        print()
    
    success = validator.print_report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
