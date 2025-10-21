---
name: yaml-dag-visualizer
description: Generate Mermaid DAG diagrams from HemoDoctor evidence/syndrome YAMLs. Visualizes decision trees, module dependencies, and evidence-to-syndrome mappings. Exports to Markdown for documentation, regulatory submissions (ANVISA/FDA), and code review. Use when documenting clinical logic, reviewing rule changes, or creating regulatory artifacts.
license: Complete terms in LICENSE.txt
---

# YAML DAG Visualizer

Generate visual Directed Acyclic Graph (DAG) diagrams from HemoDoctor clinical rule YAMLs using Mermaid syntax.

## When to Use This Skill

- **Documentation** - Generate visual diagrams for technical docs
- **Code review** - Visualize rule changes before/after
- **Regulatory submissions** - Create decision tree artifacts for ANVISA/FDA
- **Debugging** - Understand evidence-to-syndrome relationships
- **Onboarding** - Help new team members understand system architecture
- **Presentations** - Create slides showing clinical logic

## Quick Start

### Generate Full DAG (All Evidences → All Syndromes)

```bash
python scripts/visualize_dag.py full 02_evidence_hybrid.yaml 03_syndromes_hybrid.yaml dag_full.md
```

**Output:** Mermaid diagram showing all 75 evidences connecting to 34 syndromes with color-coded priorities.

### Generate Syndrome-Specific DAG

```bash
python scripts/visualize_dag.py syndrome 02_evidence_hybrid.yaml 03_syndromes_hybrid.yaml S-IDA ida_dag.md
```

**Output:** Focused diagram showing only evidences relevant to Iron Deficiency Anemia (S-IDA).

### Generate Priority-Level DAG

```bash
python scripts/visualize_dag.py priority 02_evidence_hybrid.yaml 03_syndromes_hybrid.yaml critical critical_dag.md
```

**Output:** All critical syndromes and their evidences (for regulatory review).

### Generate Module Dependencies

```bash
python scripts/visualize_dag.py modules module_deps.md
```

**Output:** High-level diagram showing how HemoDoctor modules depend on each other.

### Generate Statistics

```bash
python scripts/visualize_dag.py stats 02_evidence_hybrid.yaml 03_syndromes_hybrid.yaml stats.md
```

**Output:** Text summary with evidence counts, syndrome counts, and most-referenced evidences.

## Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `full` | Complete evidence→syndrome DAG | All 75 evidences, all 34 syndromes |
| `syndrome <ID>` | Single syndrome focus | `S-IDA`, `S-TMA`, `S-NEUTROPENIA-GRAVE` |
| `priority <level>` | Filter by priority | `critical`, `priority`, `review`, `routine` |
| `modules` | Module dependency diagram | Config → Schema → Evidence → ... |
| `stats` | Statistics summary | Counts, categories, top evidences |

## Output Format

### Mermaid Diagram (in Markdown)

```markdown
# DAG for S-IDA

\`\`\`mermaid
graph TD
    E-HB-LOW[E-HB-LOW<br/>strong] --> S-IDA
    E-MCV-LOW[E-MCV-LOW<br/>strong] --> S-IDA
    E-RDW-HIGH[E-RDW-HIGH<br/>moderate] --> S-IDA
    E-FERRITIN-LOW[E-FERRITIN-LOW<br/>critical] --> S-IDA
    
    S-IDA[S-IDA<br/>priority]:::highlight
    
    classDef highlight fill:#ff6b6b,stroke:#c92a2a,stroke-width:4px
\`\`\`
```

### Rendered Diagram

When viewed in GitHub, GitLab, or Markdown viewers that support Mermaid, this renders as an interactive diagram.

## Color Coding

### Evidence Categories
- **Critical** - Rectangle `[E-ID]` (most important)
- **Strong** - Rounded `(E-ID)`
- **Moderate** - Diamond `{E-ID}`
- **Weak** - Rounded `(E-ID)`

### Syndrome Priorities
- **Critical** - Red `#ff6b6b` (thick border)
- **Priority** - Yellow `#ffd43b`
- **Review** - Blue `#74c0fc`
- **Routine** - Green `#b2f2bb`

## Use Cases

### 1. Regulatory Documentation

```bash
# Generate critical syndromes DAG for ANVISA submission
python scripts/visualize_dag.py priority 02_evidence.yaml 03_syndromes.yaml critical anvisa_critical_dag.md

# Include in regulatory package as decision tree evidence
```

### 2. Code Review Workflow

```bash
# Before rule changes
python scripts/visualize_dag.py syndrome 02_evidence_OLD.yaml 03_syndromes_OLD.yaml S-IDA ida_before.md

# After rule changes
python scripts/visualize_dag.py syndrome 02_evidence_NEW.yaml 03_syndromes_NEW.yaml S-IDA ida_after.md

# Compare ida_before.md vs ida_after.md in PR
```

### 3. Technical Documentation

```bash
# Generate all diagrams for docs/
python scripts/visualize_dag.py full 02_evidence.yaml 03_syndromes.yaml docs/dag_full.md
python scripts/visualize_dag.py modules docs/module_deps.md
python scripts/visualize_dag.py stats 02_evidence.yaml 03_syndromes.yaml docs/stats.md
```

### 4. Debugging Rule Issues

```bash
# Why is S-TMA not triggering?
python scripts/visualize_dag.py syndrome 02_evidence.yaml 03_syndromes.yaml S-TMA tma_debug.md

# Review diagram - are all required evidences present?
```

### 5. Onboarding New Developers

```bash
# Show system architecture
python scripts/visualize_dag.py modules onboarding/architecture.md

# Show example syndromes
python scripts/visualize_dag.py syndrome 02_evidence.yaml 03_syndromes.yaml S-IDA onboarding/ida_example.md
python scripts/visualize_dag.py syndrome 02_evidence.yaml 03_syndromes.yaml S-TMA onboarding/tma_example.md
```

## Integration with GitHub/GitLab

### Automatic Diagram Generation (GitHub Actions)

```yaml
# .github/workflows/generate-diagrams.yml
name: Generate DAG Diagrams

on:
  push:
    paths:
      - 'yamls/02_evidence*.yaml'
      - 'yamls/03_syndromes*.yaml'

jobs:
  diagrams:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Generate diagrams
        run: |
          python scripts/visualize_dag.py full yamls/02_evidence.yaml yamls/03_syndromes.yaml docs/dag_full.md
          python scripts/visualize_dag.py priority yamls/02_evidence.yaml yamls/03_syndromes.yaml critical docs/dag_critical.md
          python scripts/visualize_dag.py modules docs/modules.md
      
      - name: Commit diagrams
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add docs/*.md
          git commit -m "Auto-generate DAG diagrams" || exit 0
          git push
```

### Viewing in GitHub

Mermaid diagrams render automatically in:
- README.md
- Pull request descriptions
- Issue comments
- Wiki pages

## Advanced Usage

### Generate Multiple Syndrome Diagrams

```bash
#!/bin/bash
# generate_all_syndromes.sh

SYNDROMES=(
  "S-IDA"
  "S-TMA"
  "S-NEUTROPENIA-GRAVE"
  "S-BLASTIC-SYNDROME"
  "S-B12-DEFICIENCY"
  "S-BETA-THAL-TRAIT"
)

for syn in "${SYNDROMES[@]}"; do
  echo "Generating $syn..."
  python scripts/visualize_dag.py syndrome \
    02_evidence.yaml 03_syndromes.yaml \
    "$syn" "docs/syndromes/${syn}.md"
done

echo "✅ Generated ${#SYNDROMES[@]} syndrome diagrams"
```

### Custom Styling (Edit Script)

```python
# In visualize_dag.py, customize colors:
lines.append("    classDef critical fill:#YOUR_COLOR,stroke:#BORDER")
```

## Statistics Output Example

```markdown
# HemoDoctor DAG Statistics

**Total Evidences:** 75
**Total Syndromes:** 34

## Evidence Categories
- **critical**: 12
- **strong**: 28
- **moderate**: 25
- **weak**: 10

## Syndrome Priorities
- **critical**: 9
- **priority**: 23
- **review**: 0
- **routine**: 2

## Top 10 Most Referenced Evidences
- **E-HB-LOW**: Used by 8 syndromes
- **E-PLT-LOW**: Used by 6 syndromes
- **E-WBC-HIGH**: Used by 5 syndromes
...
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'yaml'"
```bash
pip install pyyaml
```

### Diagrams Not Rendering in GitHub
- Ensure file extension is `.md`
- Verify Mermaid syntax (triple backticks with `mermaid`)
- Check GitHub's Mermaid support (enabled by default since 2022)

### "Syndrome S-XXX not found"
- Check syndrome ID matches exactly (case-sensitive)
- Run `stats` command to see all available syndrome IDs

### Diagram Too Large
- Use `syndrome` or `priority` commands for smaller diagrams
- For full DAG, render in specialized tools (Mermaid Live Editor)

## Mermaid Tools

### Online Viewers
- **Mermaid Live Editor**: https://mermaid.live/
- **GitHub**: Renders natively in `.md` files
- **GitLab**: Renders natively in `.md` files

### Local Viewers
- **VS Code**: Markdown Preview Mermaid Support extension
- **IntelliJ/PyCharm**: Built-in Markdown preview
- **Obsidian**: Built-in Mermaid support

## Regulatory Compliance

DAG diagrams support:
- **ANVISA RDC 657/2022** - Decision tree documentation
- **FDA 21 CFR Part 11** - Electronic records traceability
- **ISO 13485** - Quality management documentation
- **IEC 62304** - Software architecture artifacts

**Diagrams can be included in regulatory submissions as visual evidence of clinical logic.**

## Best Practices

1. **Generate diagrams in CI/CD** - Keep docs in sync with YAMLs
2. **Use priority filters** - Critical syndromes deserve separate diagrams
3. **Include in PRs** - Show rule changes visually
4. **Export to PDF** - For regulatory submissions (via Mermaid Live Editor)
5. **Keep archived versions** - Track rule evolution over time

## Limitations

- Maximum ~100 nodes per diagram (browser rendering limits)
- For full DAG, use specialized viewers or split by priority
- Mermaid syntax may vary slightly across renderers

## Resources

- **scripts/visualize_dag.py** - Main visualizer with 5 commands
- **Mermaid Documentation**: https://mermaid.js.org/
- **GitHub Mermaid Support**: https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/
