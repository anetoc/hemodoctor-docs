#!/usr/bin/env python3
"""
Next Steps Debugger for HemoDoctor
Test triggers, simulate cases, find dead code
"""

import yaml
import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Any
from simpleeval import simple_eval


class NextStepsDebugger:
    """Debug next_steps_engine triggers"""
    
    def __init__(self):
        self.triggers = []
        self.trigger_stats = {}
    
    def load_triggers(self, trigger_file: str):
        """Load triggers from 09_next_steps_engine_hybrid.yaml"""
        with open(trigger_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if 'triggers' not in data:
            print("❌ No 'triggers' key in file")
            return False
        
        self.triggers = data['triggers']
        
        # Initialize stats
        for trigger in self.triggers:
            trigger_id = trigger.get('id', 'unknown')
            self.trigger_stats[trigger_id] = {
                'tested': 0,
                'fired': 0,
                'errors': []
            }
        
        print(f"✓ Loaded {len(self.triggers)} triggers")
        return True
    
    def eval_when(self, when_expr: str, case: Dict) -> tuple:
        """Safely evaluate 'when' expression"""
        try:
            # Prepare safe names (all case fields + None/True/False)
            safe_names = {k: v for k, v in case.items()}
            safe_names.update({
                'None': None,
                'True': True,
                'False': False,
                'true': True,
                'false': False
            })
            
            result = simple_eval(when_expr, names=safe_names)
            return (bool(result), None)
        
        except Exception as e:
            return (False, str(e))
    
    def test_case(self, case: Dict, verbose: bool = False) -> List[Dict]:
        """Test a case against all triggers"""
        fired_triggers = []
        
        for trigger in self.triggers:
            trigger_id = trigger.get('id', 'unknown')
            when_expr = trigger.get('when', '')
            
            self.trigger_stats[trigger_id]['tested'] += 1
            
            if not when_expr:
                self.trigger_stats[trigger_id]['errors'].append("Missing 'when' expression")
                continue
            
            result, error = self.eval_when(when_expr, case)
            
            if error:
                self.trigger_stats[trigger_id]['errors'].append(f"Eval error: {error}")
                if verbose:
                    print(f"  ⚠️  {trigger_id}: ERROR - {error}")
                continue
            
            if result:
                self.trigger_stats[trigger_id]['fired'] += 1
                fired_triggers.append({
                    'trigger_id': trigger_id,
                    'syndromes': trigger.get('syndromes', []),
                    'suggest': trigger.get('suggest', [])
                })
                
                if verbose:
                    print(f"  ✅ {trigger_id}: FIRED")
            elif verbose:
                print(f"  ❌ {trigger_id}: NOT FIRED")
        
        return fired_triggers
    
    def test_file(self, case_file: str, verbose: bool = False) -> Dict:
        """Test cases from JSON file"""
        with open(case_file, 'r', encoding='utf-8') as f:
            cases = json.load(f)
        
        if not isinstance(cases, list):
            cases = [cases]
        
        print(f"\n🧪 Testing {len(cases)} cases...")
        
        for i, case in enumerate(cases, 1):
            if verbose:
                case_id = case.get('case_id', f'Case-{i}')
                print(f"\n📋 {case_id}")
            
            self.test_case(case, verbose=verbose)
        
        return self.get_stats()
    
    def simulate_case(self, **kwargs) -> List[Dict]:
        """Simulate a case with given parameters"""
        case = {
            'hb': kwargs.get('hb'),
            'mcv': kwargs.get('mcv'),
            'wbc': kwargs.get('wbc'),
            'anc': kwargs.get('anc'),
            'plt': kwargs.get('plt'),
            'rdw': kwargs.get('rdw'),
            'ferritin': kwargs.get('ferritin'),
            'tsat': kwargs.get('tsat'),
            'crp': kwargs.get('crp'),
            'ldh': kwargs.get('ldh'),
            'sex': kwargs.get('sex', 'M'),
            'age_years': kwargs.get('age_years', 45),
            'esquistocitos': kwargs.get('esquistocitos'),
            'blastos': kwargs.get('blastos'),
            'bastoes': kwargs.get('bastoes'),
        }
        
        # Remove None values
        case = {k: v for k, v in case.items() if v is not None}
        
        return self.test_case(case, verbose=True)
    
    def find_dead_triggers(self, min_tests: int = 10) -> List[str]:
        """Find triggers that never fire"""
        dead = []
        
        for trigger_id, stats in self.trigger_stats.items():
            if stats['tested'] >= min_tests and stats['fired'] == 0:
                dead.append(trigger_id)
        
        return dead
    
    def find_error_triggers(self) -> List[tuple]:
        """Find triggers with evaluation errors"""
        errors = []
        
        for trigger_id, stats in self.trigger_stats.items():
            if stats['errors']:
                errors.append((trigger_id, stats['errors']))
        
        return errors
    
    def get_stats(self) -> Dict:
        """Get statistics summary"""
        total_triggers = len(self.triggers)
        never_fired = sum(1 for s in self.trigger_stats.values() if s['fired'] == 0)
        with_errors = sum(1 for s in self.trigger_stats.values() if s['errors'])
        
        return {
            'total_triggers': total_triggers,
            'never_fired': never_fired,
            'with_errors': with_errors,
            'coverage': (total_triggers - never_fired) / total_triggers if total_triggers > 0 else 0,
            'details': self.trigger_stats
        }
    
    def print_report(self, min_tests: int = 10):
        """Print comprehensive report"""
        stats = self.get_stats()
        
        print("\n" + "="*60)
        print("NEXT STEPS DEBUGGER REPORT")
        print("="*60)
        
        print(f"\n📊 Summary:")
        print(f"  Total triggers: {stats['total_triggers']}")
        print(f"  Never fired: {stats['never_fired']}")
        print(f"  With errors: {stats['with_errors']}")
        print(f"  Coverage: {stats['coverage']:.1%}")
        
        # Dead triggers
        dead = self.find_dead_triggers(min_tests)
        if dead:
            print(f"\n❌ Dead Triggers ({len(dead)}) - Never fired in ≥{min_tests} tests:")
            for trigger_id in dead:
                print(f"  • {trigger_id}")
        
        # Error triggers
        errors = self.find_error_triggers()
        if errors:
            print(f"\n⚠️  Triggers with Errors ({len(errors)}):")
            for trigger_id, error_list in errors:
                print(f"  • {trigger_id}:")
                for error in set(error_list):  # Dedupe
                    print(f"    - {error}")
        
        # Top firing triggers
        sorted_triggers = sorted(
            self.trigger_stats.items(),
            key=lambda x: x[1]['fired'],
            reverse=True
        )[:10]
        
        print(f"\n🔥 Top 10 Firing Triggers:")
        for trigger_id, stats in sorted_triggers:
            if stats['fired'] > 0:
                fire_rate = stats['fired'] / stats['tested'] if stats['tested'] > 0 else 0
                print(f"  • {trigger_id}: {stats['fired']}/{stats['tested']} ({fire_rate:.1%})")
        
        print("="*60)


def main():
    if len(sys.argv) < 2:
        print("Usage: python debug_next_steps.py <command> [options]")
        print("\nCommands:")
        print("  test <trigger_file> <case_file> [--verbose]")
        print("    Test triggers against cases from JSON file")
        print("  ")
        print("  simulate <trigger_file> --hb=X --mcv=Y --plt=Z ...")
        print("    Simulate a single case with given parameters")
        print("  ")
        print("  check <trigger_file>")
        print("    Check trigger syntax without running cases")
        print("\nExamples:")
        print("  python debug_next_steps.py test 09_next_steps.yaml test_cases.json --verbose")
        print("  python debug_next_steps.py simulate 09_next_steps.yaml --hb=9.5 --mcv=72 --ferritin=8")
        print("  python debug_next_steps.py check 09_next_steps.yaml")
        sys.exit(1)
    
    command = sys.argv[1]
    debugger = NextStepsDebugger()
    
    if command == "test":
        if len(sys.argv) < 4:
            print("❌ Usage: debug_next_steps.py test <trigger_file> <case_file> [--verbose]")
            sys.exit(1)
        
        trigger_file = sys.argv[2]
        case_file = sys.argv[3]
        verbose = '--verbose' in sys.argv or '-v' in sys.argv
        
        if not debugger.load_triggers(trigger_file):
            sys.exit(1)
        
        debugger.test_file(case_file, verbose=verbose)
        debugger.print_report(min_tests=1)
    
    elif command == "simulate":
        if len(sys.argv) < 3:
            print("❌ Usage: debug_next_steps.py simulate <trigger_file> --param=value ...")
            sys.exit(1)
        
        trigger_file = sys.argv[2]
        
        # Parse parameters
        params = {}
        for arg in sys.argv[3:]:
            if arg.startswith('--'):
                key, value = arg[2:].split('=', 1)
                
                # Try to convert to appropriate type
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                elif value.lower() == 'none':
                    value = None
                else:
                    try:
                        value = float(value)
                    except ValueError:
                        pass  # Keep as string
                
                params[key] = value
        
        if not params:
            print("❌ No parameters provided. Example: --hb=9.5 --mcv=72")
            sys.exit(1)
        
        print(f"\n🧪 Simulating case with parameters:")
        for k, v in params.items():
            print(f"  {k}: {v}")
        
        if not debugger.load_triggers(trigger_file):
            sys.exit(1)
        
        fired = debugger.simulate_case(**params)
        
        print(f"\n🎯 Result: {len(fired)} trigger(s) fired")
        
        if fired:
            print("\n📋 Suggested next steps:")
            for trigger in fired:
                print(f"\n  Trigger: {trigger['trigger_id']}")
                print(f"  Syndromes: {', '.join(trigger['syndromes'])}")
                for item in trigger['suggest']:
                    print(f"    • [{item.get('level', 'N/A')}] {item.get('test', 'N/A')}")
                    print(f"      Rationale: {item.get('rationale', 'N/A')}")
    
    elif command == "check":
        if len(sys.argv) < 3:
            print("❌ Usage: debug_next_steps.py check <trigger_file>")
            sys.exit(1)
        
        trigger_file = sys.argv[2]
        
        if not debugger.load_triggers(trigger_file):
            sys.exit(1)
        
        print("\n🔍 Checking trigger syntax...")
        
        # Test with empty case to check syntax
        empty_case = {
            'hb': None, 'mcv': None, 'wbc': None, 'plt': None,
            'anc': None, 'ferritin': None, 'sex': 'M', 'age_years': 45
        }
        
        errors = debugger.find_error_triggers()
        
        if errors:
            print(f"\n❌ Found {len(errors)} trigger(s) with syntax errors:")
            for trigger_id, error_list in errors:
                print(f"\n  {trigger_id}:")
                for error in set(error_list):
                    print(f"    • {error}")
        else:
            print("\n✅ All triggers have valid syntax!")
    
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
