#!/usr/bin/env python3
"""
YAML DAG Visualizer for HemoDoctor
Generates Mermaid diagrams from evidence/syndrome YAMLs
"""

import yaml
import sys
from pathlib import Path
from typing import Dict, List, Set


class YAMLDAGVisualizer:
    """Generate DAG visualizations from HemoDoctor YAMLs"""
    
    def __init__(self):
        self.evidences = {}
        self.syndromes = {}
        self.evidence_to_syndromes = {}
    
    def load_evidence(self, evidence_file: str):
        """Load evidence from 02_evidence_hybrid.yaml"""
        with open(evidence_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if 'evidences' in data:
            for ev in data['evidences']:
                self.evidences[ev['id']] = ev
        
        print(f"✓ Loaded {len(self.evidences)} evidences")
    
    def load_syndromes(self, syndrome_file: str):
        """Load syndromes from 03_syndromes_hybrid.yaml"""
        with open(syndrome_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Handle categorized structure
        syndrome_keys = ['critical_syndromes', 'priority_syndromes', 'review_syndromes', 'routine_syndromes']
        syndromes = []
        
        for key in syndrome_keys:
            if key in data:
                syndromes.extend(data[key])
        
        if not syndromes and 'syndromes' in data:
            syndromes = data['syndromes']
        
        for syn in syndromes:
            self.syndromes[syn['id']] = syn
            
            # Extract evidence references from combine logic
            evidences = self._extract_evidences(syn.get('combine', {}))
            for ev_id in evidences:
                if ev_id not in self.evidence_to_syndromes:
                    self.evidence_to_syndromes[ev_id] = []
                self.evidence_to_syndromes[ev_id].append(syn['id'])
        
        print(f"✓ Loaded {len(self.syndromes)} syndromes")
    
    def _extract_evidences(self, combine) -> Set[str]:
        """Extract evidence IDs from combine logic (recursive)"""
        evidences = set()
        
        if isinstance(combine, dict):
            for key, value in combine.items():
                if key in ['all', 'any']:
                    if isinstance(value, list):
                        for item in value:
                            if isinstance(item, str) and item.startswith('E-'):
                                evidences.add(item)
                            elif isinstance(item, dict):
                                evidences.update(self._extract_evidences(item))
        elif isinstance(combine, list):
            for item in combine:
                if isinstance(item, str) and item.startswith('E-'):
                    evidences.add(item)
        
        return evidences
    
    def generate_mermaid_full(self) -> str:
        """Generate full DAG: Evidence → Syndromes"""
        lines = ["```mermaid", "graph TD"]
        
        # Add evidence nodes (grouped by category)
        lines.append("    %% Evidence Nodes")
        for ev_id, ev in self.evidences.items():
            category = ev.get('category', 'moderate')
            shape = {
                'critical': f'[{ev_id}]',  # Rectangle
                'strong': f'({ev_id})',    # Rounded
                'moderate': f'{{{ev_id}}}', # Diamond
                'weak': f'({ev_id})'       # Rounded
            }.get(category, f'[{ev_id}]')
            lines.append(f"    {ev_id}{shape}")
        
        # Add syndrome nodes (grouped by priority)
        lines.append("")
        lines.append("    %% Syndrome Nodes")
        for syn_id, syn in self.syndromes.items():
            priority = syn.get('priority') or syn.get('criticality', 'routine')
            color = {
                'critical': ':::critical',
                'priority': ':::priority',
                'review': ':::review',
                'routine': ':::routine'
            }.get(priority, '')
            lines.append(f"    {syn_id}[{syn_id}]{color}")
        
        # Add edges
        lines.append("")
        lines.append("    %% Evidence → Syndrome Edges")
        for ev_id, syn_ids in self.evidence_to_syndromes.items():
            for syn_id in syn_ids:
                lines.append(f"    {ev_id} --> {syn_id}")
        
        # Add styling
        lines.append("")
        lines.append("    %% Styling")
        lines.append("    classDef critical fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px")
        lines.append("    classDef priority fill:#ffd43b,stroke:#f59f00")
        lines.append("    classDef review fill:#74c0fc,stroke:#339af0")
        lines.append("    classDef routine fill:#b2f2bb,stroke:#51cf66")
        
        lines.append("```")
        return "\n".join(lines)
    
    def generate_mermaid_syndrome(self, syndrome_id: str) -> str:
        """Generate DAG for a single syndrome"""
        if syndrome_id not in self.syndromes:
            return f"# Error: Syndrome {syndrome_id} not found"
        
        syndrome = self.syndromes[syndrome_id]
        evidences = self._extract_evidences(syndrome.get('combine', {}))
        
        lines = ["```mermaid", "graph TD"]
        lines.append(f"    %% {syndrome_id}")
        
        # Add evidence nodes
        for ev_id in evidences:
            if ev_id in self.evidences:
                ev = self.evidences[ev_id]
                category = ev.get('category', 'moderate')
                lines.append(f"    {ev_id}[{ev_id}<br/>{category}]")
        
        # Add syndrome node
        priority = syndrome.get('priority') or syndrome.get('criticality', 'routine')
        lines.append(f"    {syndrome_id}[{syndrome_id}<br/>{priority}]:::highlight")
        
        # Add edges
        lines.append("")
        for ev_id in evidences:
            lines.append(f"    {ev_id} --> {syndrome_id}")
        
        # Styling
        lines.append("")
        lines.append("    classDef highlight fill:#ff6b6b,stroke:#c92a2a,stroke-width:4px")
        
        lines.append("```")
        return "\n".join(lines)
    
    def generate_mermaid_priority(self, priority: str = "critical") -> str:
        """Generate DAG for syndromes of specific priority"""
        filtered = {sid: syn for sid, syn in self.syndromes.items() 
                   if syn.get('priority', syn.get('criticality')) == priority}
        
        if not filtered:
            return f"# No syndromes with priority '{priority}' found"
        
        lines = ["```mermaid", "graph TD"]
        lines.append(f"    %% {priority.upper()} Syndromes")
        
        # Collect all evidences used by these syndromes
        used_evidences = set()
        for syn in filtered.values():
            used_evidences.update(self._extract_evidences(syn.get('combine', {})))
        
        # Add evidence nodes
        lines.append("    %% Evidence Nodes")
        for ev_id in used_evidences:
            if ev_id in self.evidences:
                lines.append(f"    {ev_id}[{ev_id}]")
        
        # Add syndrome nodes
        lines.append("")
        lines.append("    %% Syndrome Nodes")
        for syn_id in filtered.keys():
            lines.append(f"    {syn_id}[{syn_id}]:::highlight")
        
        # Add edges
        lines.append("")
        lines.append("    %% Edges")
        for syn_id, syn in filtered.items():
            evidences = self._extract_evidences(syn.get('combine', {}))
            for ev_id in evidences:
                lines.append(f"    {ev_id} --> {syn_id}")
        
        # Styling
        lines.append("")
        lines.append("    classDef highlight fill:#ff6b6b,stroke:#c92a2a,stroke-width:3px")
        
        lines.append("```")
        return "\n".join(lines)
    
    def generate_module_dependencies(self) -> str:
        """Generate module dependency diagram"""
        lines = ["```mermaid", "graph LR"]
        lines.append("    %% HemoDoctor Module Dependencies")
        
        modules = [
            ("00_config", "Configuration"),
            ("01_schema", "Schema"),
            ("02_evidence", "Evidence"),
            ("03_syndromes", "Syndromes"),
            ("05_missingness", "Missingness"),
            ("09_next_steps", "Next Steps"),
            ("12_output", "Output")
        ]
        
        for mod_id, mod_name in modules:
            lines.append(f"    {mod_id}[\"{mod_name}\"]")
        
        # Dependencies
        lines.append("")
        lines.append("    00_config --> 01_schema")
        lines.append("    01_schema --> 02_evidence")
        lines.append("    02_evidence --> 03_syndromes")
        lines.append("    03_syndromes --> 05_missingness")
        lines.append("    03_syndromes --> 09_next_steps")
        lines.append("    05_missingness --> 12_output")
        lines.append("    09_next_steps --> 12_output")
        
        lines.append("```")
        return "\n".join(lines)
    
    def generate_stats(self) -> str:
        """Generate statistics summary"""
        lines = ["# HemoDoctor DAG Statistics\n"]
        
        lines.append(f"**Total Evidences:** {len(self.evidences)}")
        lines.append(f"**Total Syndromes:** {len(self.syndromes)}\n")
        
        # Evidences by category
        lines.append("## Evidence Categories")
        categories = {}
        for ev in self.evidences.values():
            cat = ev.get('category', 'unknown')
            categories[cat] = categories.get(cat, 0) + 1
        
        for cat, count in sorted(categories.items()):
            lines.append(f"- **{cat}**: {count}")
        
        # Syndromes by priority
        lines.append("\n## Syndrome Priorities")
        priorities = {}
        for syn in self.syndromes.values():
            pri = syn.get('priority') or syn.get('criticality', 'unknown')
            priorities[pri] = priorities.get(pri, 0) + 1
        
        for pri, count in sorted(priorities.items()):
            lines.append(f"- **{pri}**: {count}")
        
        # Most connected evidences
        lines.append("\n## Top 10 Most Referenced Evidences")
        sorted_ev = sorted(self.evidence_to_syndromes.items(), 
                          key=lambda x: len(x[1]), reverse=True)[:10]
        for ev_id, syn_ids in sorted_ev:
            lines.append(f"- **{ev_id}**: Used by {len(syn_ids)} syndromes")
        
        return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print("Usage: python visualize_dag.py <command> <evidence.yaml> <syndromes.yaml> [output.md]")
        print("\nCommands:")
        print("  full        - Generate complete DAG (all evidences → all syndromes)")
        print("  syndrome <ID> - Generate DAG for specific syndrome")
        print("  priority <level> - Generate DAG for priority level (critical/priority/review/routine)")
        print("  modules     - Generate module dependency diagram")
        print("  stats       - Generate statistics summary")
        print("\nExamples:")
        print("  python visualize_dag.py full 02_evidence.yaml 03_syndromes.yaml dag_full.md")
        print("  python visualize_dag.py syndrome 02_evidence.yaml 03_syndromes.yaml S-IDA ida_dag.md")
        print("  python visualize_dag.py priority 02_evidence.yaml 03_syndromes.yaml critical critical_dag.md")
        print("  python visualize_dag.py stats 02_evidence.yaml 03_syndromes.yaml stats.md")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "modules":
        output = sys.argv[2] if len(sys.argv) > 2 else "module_dependencies.md"
        viz = YAMLDAGVisualizer()
        diagram = viz.generate_module_dependencies()
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write("# HemoDoctor Module Dependencies\n\n")
            f.write(diagram)
        
        print(f"✅ Module dependency diagram saved to {output}")
        return
    
    evidence_file = sys.argv[2]
    syndrome_file = sys.argv[3]
    
    viz = YAMLDAGVisualizer()
    viz.load_evidence(evidence_file)
    viz.load_syndromes(syndrome_file)
    
    if command == "full":
        output = sys.argv[4] if len(sys.argv) > 4 else "dag_full.md"
        diagram = viz.generate_mermaid_full()
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write("# HemoDoctor Complete DAG\n\n")
            f.write(diagram)
        
        print(f"✅ Full DAG saved to {output}")
    
    elif command == "syndrome":
        if len(sys.argv) < 5:
            print("❌ Missing syndrome ID")
            sys.exit(1)
        
        syndrome_id = sys.argv[4]
        output = sys.argv[5] if len(sys.argv) > 5 else f"dag_{syndrome_id}.md"
        diagram = viz.generate_mermaid_syndrome(syndrome_id)
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write(f"# DAG for {syndrome_id}\n\n")
            f.write(diagram)
        
        print(f"✅ Syndrome DAG saved to {output}")
    
    elif command == "priority":
        if len(sys.argv) < 5:
            print("❌ Missing priority level")
            sys.exit(1)
        
        priority = sys.argv[4]
        output = sys.argv[5] if len(sys.argv) > 5 else f"dag_{priority}.md"
        diagram = viz.generate_mermaid_priority(priority)
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write(f"# DAG for {priority.upper()} Syndromes\n\n")
            f.write(diagram)
        
        print(f"✅ Priority DAG saved to {output}")
    
    elif command == "stats":
        output = sys.argv[4] if len(sys.argv) > 4 else "dag_stats.md"
        stats = viz.generate_stats()
        
        with open(output, 'w', encoding='utf-8') as f:
            f.write(stats)
        
        print(f"✅ Statistics saved to {output}")
    
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
