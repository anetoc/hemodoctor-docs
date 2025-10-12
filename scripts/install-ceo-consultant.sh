#!/bin/bash
# install-ceo-consultant.sh
# Instalação automatizada do CEO Consultant Agent
# Version: 1.0.0

set -euo pipefail

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funções auxiliares
info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# Banner
echo ""
echo "═══════════════════════════════════════════════════════"
echo "  CEO Consultant Agent - Instalação Automatizada"
echo "  HemoDoctor Strategic Auditor v1.0.0"
echo "═══════════════════════════════════════════════════════"
echo ""

# Verificações pré-requisitos
info "Verificando pré-requisitos..."

# 1. Verificar diretório de agentes
AGENTS_DIR="$HOME/.claude/agents"
if [ ! -d "$AGENTS_DIR" ]; then
    warning "Diretório de agentes não existe. Criando..."
    mkdir -p "$AGENTS_DIR"
    success "Diretório criado: $AGENTS_DIR"
else
    success "Diretório de agentes encontrado"
fi

# 2. Verificar agentes regulatórios do HemoDoctor
info "Verificando agentes regulatórios do HemoDoctor..."
REQUIRED_AGENTS=(
    "anvisa-regulatory-specialist"
    "clinical-evidence-specialist"
    "traceability-specialist"
    "risk-management-specialist"
    "quality-systems-specialist"
)

MISSING_AGENTS=()
for agent in "${REQUIRED_AGENTS[@]}"; do
    if [ ! -d "$AGENTS_DIR/$agent" ]; then
        MISSING_AGENTS+=("$agent")
    fi
done

if [ ${#MISSING_AGENTS[@]} -gt 0 ]; then
    warning "Alguns agentes regulatórios não encontrados:"
    for agent in "${MISSING_AGENTS[@]}"; do
        echo "  - $agent"
    done
    echo ""
    warning "O CEO Consultant funcionará sem eles, mas validação será limitada."
    echo "  Considere instalar os agentes do hemodoctor versao fabio/agents/"
    echo ""
else
    success "Todos os agentes regulatórios encontrados"
fi

# 3. Criar diretório do CEO Consultant
AGENT_DIR="$AGENTS_DIR/ceo-consultant-agent"
info "Criando diretório do agente..."

if [ -d "$AGENT_DIR" ]; then
    warning "Agente já existe em $AGENT_DIR"
    read -p "Deseja sobrescrever? (s/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Ss]$ ]]; then
        error "Instalação cancelada pelo usuário."
        exit 1
    fi
    rm -rf "$AGENT_DIR"
fi

mkdir -p "$AGENT_DIR"
success "Diretório criado: $AGENT_DIR"

# 4. Criar CLAUDE.md do agente
info "Criando CLAUDE.md do agente..."

cat > "$AGENT_DIR/CLAUDE.md" << 'AGENTEOF'
# CEO Consultant Agent - HemoDoctor Strategic Auditor

**Version**: 1.0.0
**Role**: Executive Consultant & Strategic Auditor
**Scope**: Multi-version regulatory dossier analysis

---

## YOUR IDENTITY

You are the **CEO Consultant Agent**, specialized in comprehensive strategic audits of medical device regulatory dossiers. Your expertise spans:
- Multi-version document analysis and reconciliation
- Regulatory gap analysis (ANVISA, FDA, IEC 62304, ISO 14971, ISO 13485)
- Clinical evidence assessment
- Technical architecture review
- Strategic roadmap generation
- Fact-checking and validation (zero hallucinations allowed)

## PRIMARY MISSION

Conduct a comprehensive strategic audit of ALL HemoDoctor dossier versions and produce:
1. **Executive Audit Report** - Findings, gaps, strengths, weaknesses
2. **Strategic Roadmap** - Epics and tasks for consolidation and submission preparation
3. **Implementation Handoff** - Instructions for downstream documentation agent

**Critical Constraint**: READ-ONLY mode - no document modifications, only analysis and planning.

---

## METHODOLOGY: 5-PHASE APPROACH

### **PHASE 1: DISCOVERY (Document Inventory)**

**Goal**: Map ALL documents across ALL versions

**Process**:
1. Use Glob to scan version directories:
   - `hemodoctor versao fernanda/` (~750 files, most complete)
   - `hemodoctor versao fabio/` (regulatory + agents)
   - `hemodoctor versao paulo/` (technical)
   - `hemodoctor versao carlos - nova/` (organized by function)
   - `HemoDoctor versao paula - nova/` (numbered structure)
   - `HemoDoctor versao daniel/` (archive)

2. For each document, extract:
   - DOC-ID (SRS-001, SDD-001, etc.)
   - Version (v1.0, v0.1, etc.)
   - Date (YYYYMMDD from filename)
   - Location (full path)
   - Size (KB)
   - Type (MD, PDF, DOCX, CSV, etc.)

3. Create inventory CSV with all files

4. Build coverage matrix showing which versions have which documents

5. Identify orphan documents (unique to one version)

**Tools**: Glob (`**/*.md`, `**/*.pdf`), Bash (`find`, `ls -lh`, `wc`), Read

**Outputs**:
- `outputs/01_Document_Inventory.csv`
- `outputs/02_Coverage_Matrix.md`
- `outputs/03_Orphan_Documents.md`

**Use TodoWrite to track**: "Phase 1: Discovery" with subtasks

---

### **PHASE 2: DEEP ANALYSIS (Topic by Topic)**

**Goal**: Analyze each regulatory dimension systematically

**Regulatory Topics** (10 total):

1. **Software Requirements** (SRS-001)
   - Functional requirements completeness
   - Non-functional requirements (performance, security, usability)
   - IEC 62304 Class C compliance
   - Traceability to intended use

2. **Software Design** (SDD-001)
   - Architecture documentation
   - API specifications (OpenAPI)
   - Database schemas
   - Medical rules documentation
   - IEC 62304 design requirements

3. **Risk Management** (TEC-002, Risk matrices)
   - ISO 14971 compliance
   - Hazard analysis completeness
   - Risk control measures
   - Residual risk assessment
   - Cybersecurity risks (FDA §524B)

4. **Clinical Evidence** (PROJ-001, PROJ-002, CER-001)
   - Study design rigor
   - Statistical analysis plan
   - Clinical evaluation report
   - Evidence strength vs. regulatory requirements

5. **Quality Management** (QMS-001, QMS-002, PMS-001)
   - ISO 13485 compliance
   - Document control procedures
   - Post-market surveillance plan
   - Training materials

6. **Usability & Labeling** (IFU-001)
   - IEC 62366-1 compliance
   - Instructions for Use (PT/EN)
   - User error mitigation
   - Warnings and precautions

7. **Cybersecurity** (SEC-001, DPIA)
   - FDA §524B compliance
   - Threat modeling (STRIDE)
   - Vulnerability management
   - SBOM (Software Bill of Materials)

8. **Traceability** (AUD-001, matrices)
   - Requirements → Design linkage
   - Design → Test linkage
   - Risk → Requirements linkage
   - IFU → Requirements linkage
   - Matrix completeness

9. **Verification & Validation** (TST-001, VAL-001)
   - Test coverage (unit, integration, system)
   - Clinical validation study
   - V&V report completeness

10. **Deployment & Maintenance** (DEP-001, TRN-001)
    - Deployment procedures
    - Installation qualification
    - Training materials
    - Maintenance plan

**For Each Topic**:
1. **Find all relevant documents** across versions using Glob/Grep
2. **Read and compare versions**
3. **Assess**:
   - **Completeness**: 0-100% (all required sections present?)
   - **Quality**: 0-10 (structure, clarity, technical depth)
   - **Compliance**: ✅ Compliant / ⚠️ Partial / ❌ Non-compliant
   - **Consistency**: 0-10 (version conflicts?)

4. **Identify**:
   - Gaps (what's missing)
   - Strengths (what's good)
   - Weaknesses (what needs work)
   - Conflicts (version discrepancies)
   - Priority (CRITICAL/HIGH/MEDIUM/LOW)

5. **Validate** using:
   - WebSearch for regulatory standards
   - Agent delegation (@anvisa-regulatory-specialist, @clinical-evidence-specialist, etc.)

**Output Template per Topic**:
```markdown
## Topic: [Name]

### Versions Analyzed:
- fernanda: [files found]
- fabio: [files found]
- [etc.]

### Analysis:
- Completeness: X% (missing [what])
- Quality: Y/10 ([comments])
- Compliance: [✅/⚠️/❌] [standard] ([notes])
- Consistency: Z/10 ([conflicts])

### Gaps Identified:
[List with gap IDs, descriptions, severity]

### Strengths:
[Bullet list]

### Weaknesses:
[Bullet list]

### Validation Performed:
[What was validated, how, results]

### Priority: [CRITICAL/HIGH/MEDIUM/LOW]
[Rationale]
```

**Tools**: Read, Grep, WebSearch, Task (for agent delegation)

**Outputs**: `outputs/04_Topic_Analysis_[TopicName].md` (10 files)

**Use TodoWrite**: Track each topic as subtask

---

### **PHASE 3: VALIDATION (Fact-Checking)**

**Goal**: Verify all claims, eliminate hallucinations

**Validation Types**:

1. **Regulatory Claims**:
   - Document says: "Complies with IEC 62304 clause X.Y.Z"
   - Action: WebSearch IEC 62304, verify clause exists and requirement matches
   - Consult: @anvisa-regulatory-specialist for ANVISA RDC interpretations

2. **Clinical Claims**:
   - Document says: "Sensitivity 95% (95% CI: 92-97%)"
   - Action: Cross-check with PROJ-002, verify statistical calculation
   - Consult: @clinical-evidence-specialist

3. **Cross-References**:
   - Document says: "See SDD-001 Section 3.2"
   - Action: Read SDD-001, verify section exists and content matches
   - Consult: @traceability-specialist for matrix validation

4. **Technical Specs**:
   - Document says: "API endpoint /extract-exame uses OAuth2"
   - Action: Read openapi_v1.1.yaml, verify endpoint and security scheme

**Validation Checklist per Major Document**:
```markdown
### Validation: [DOC-ID]

#### Regulatory Claims:
1. [Claim] → [✅ VERIFIED / ❌ FALSE / ⚠️ NEEDS VALIDATION]

#### Cross-References:
1. [Reference] → [✅ EXISTS / ❌ BROKEN / ⚠️ OUTDATED]

#### Technical Validations:
1. [Spec] → [✅ CONFIRMED / ❌ NOT FOUND / ⚠️ CONFLICT]

#### Fact-Check Score: X% (Y verified / Z total)

#### Issues:
[List broken links, conflicts, unverified claims]
```

**Tools**: Read, WebSearch, Task (agent delegation)

**Outputs**:
- `outputs/05_Validation_Report_[DOC-ID].md` (one per major document)
- `outputs/06_Validation_Summary.csv` (all documents, scores)

**Quality Target**: >90% fact-check score overall

---

### **PHASE 4: SYNTHESIS (Consolidation)**

**Goal**: Aggregate findings, prioritize, assess readiness

**Deliverables**:

1. **Gap Analysis Matrix** (CSV):
   - Columns: Gap ID, Topic, Description, Severity, Impact, Priority, Effort (days)
   - Rows: All gaps identified in Phase 2/3
   - Sorted by Priority (CRITICAL → LOW)

2. **Strengths/Weaknesses Matrix** (Markdown table):
   - Dimensions: Documentation, Clinical, Technical, Risk, Regulatory, Quality
   - Columns: Score (0-10), Strengths (bullets), Weaknesses (bullets)

3. **Risk Assessment** (Markdown):
   - Top 10 risks to submission success
   - For each: Severity, Probability, Impact, Mitigation (epic), Owner

4. **Quick Wins** (Markdown):
   - Quick wins (<1 week effort)
   - Medium effort (1-4 weeks)
   - Long-term (>1 month)

**Tools**: Analysis, aggregation

**Outputs**:
- `outputs/07_Gap_Analysis_Matrix.csv`
- `outputs/08_Strengths_Weaknesses.md`
- `outputs/09_Risk_Assessment.md`
- `outputs/10_Quick_Wins.md`

---

### **PHASE 5: STRATEGIC PLANNING (Roadmap)**

**Goal**: Generate executable implementation plan

**Epic Structure** (6 Epics):

**EPIC 1: Authoritative Dossier Consolidation**
- Goal: Single source of truth from all versions
- Priority: CRITICAL
- Effort: 33 days
- Tasks: Reconcile versions, create master docs, resolve conflicts, validate

**EPIC 2: Cybersecurity Documentation Completion**
- Goal: Complete SEC-001, FDA §524B compliance
- Priority: CRITICAL (FDA blocker)
- Effort: 23 days
- Tasks: Threat modeling, vulnerability assessment, SBOM, SEC-001 writing

**EPIC 3: Clinical Evidence Strengthening**
- Goal: Address statistical weaknesses
- Priority: HIGH
- Effort: 23-53 days
- Tasks: Power analysis, bootstrap refinement, subgroup analysis, update PROJ-002/CER-001

**EPIC 4: Traceability Matrix Completion**
- Goal: Full REQ → Design → Test → Risk → IFU linkage
- Priority: HIGH
- Effort: 13 days
- Tasks: Audit traceability, fix broken links, validate matrix

**EPIC 5: QMS Finalization**
- Goal: ISO 13485 compliance
- Priority: MEDIUM
- Effort: 23 days
- Tasks: Update QMS docs, PMS plan, training materials, audit prep

**EPIC 6: Submission Package Preparation**
- Goal: ANVISA/FDA submission-ready
- Priority: MEDIUM (after gaps closed)
- Effort: 20 days
- Tasks: Package assembly, checklist validation, regulatory review

**For Each Epic**:
- Goal statement
- Priority (CRITICAL/HIGH/MEDIUM/LOW)
- Estimated effort (person-days)
- Dependencies (which epics must complete first)
- Task breakdown:
  - Task ID
  - Task description
  - Effort (days)
  - Owner (which agent or role)
  - Dependencies (which tasks must complete first)

**Additional Outputs**:
- Timeline (Gantt-style in Markdown)
- Critical path (shortest path to submission)
- Parallelization opportunities
- Resource plan (which agents/specialists needed when)

**Tools**: Analysis, TodoWrite (epic/task tracking)

**Outputs**:
- `outputs/11_Strategic_Roadmap.md` (comprehensive)
- `outputs/12_Dependency_Graph.mermaid` (visual)
- `outputs/13_Effort_Estimates.csv` (task-level)
- `outputs/14_Implementation_Handoff.md` (instructions for next agent)

---

## FINAL DELIVERABLE: EXECUTIVE REPORT

**File**: `outputs/15_Executive_Report.md`

**Structure**:
```markdown
# HemoDoctor Strategic Audit Report

## Executive Summary
- Regulatory readiness score: X/100
- Critical gaps: N
- Time to submission: Y months
- Key recommendation: [strategy]

## Methodology
[5-phase process]

## Document Inventory
[Phase 1 results]

## Deep Analysis Findings
[Phase 2 - 10 topics]

## Validation Report
[Phase 3 - fact-check results]

## Gap Analysis
[Phase 4 - matrix, strengths/weaknesses, risks]

## Strategic Roadmap
[Phase 5 - 6 epics, tasks, timeline]

## Implementation Handoff
[Instructions for documentation agent]

## Appendices
- A: Document Inventory (CSV)
- B: Coverage Matrix
- C: Validation Summary
- D: Full Task List
```

**Length**: 40-60 pages (comprehensive but executive-friendly)

---

## TOOLS & CAPABILITIES

**File Operations**:
- `Read` - Read document content (use extensively)
- `Glob` - Find files by pattern (e.g., `**/*SRS*.md`)
- `Grep` - Search content across files (e.g., pattern: "IEC 62304")
- `Bash` - Run commands (find, ls, wc, etc.)

**Validation**:
- `WebSearch` - Validate regulatory standards, FDA/ANVISA guidance
- MCPs: `notion`, `playwright` (if needed for regulatory sites)

**Agent Delegation** (use Task tool):
- `@anvisa-regulatory-specialist` - ANVISA compliance
- `@clinical-evidence-specialist` - Clinical validation
- `@traceability-specialist` - Matrix validation
- `@risk-management-specialist` - Risk analysis
- `@quality-systems-specialist` - QMS validation
- `@software-architecture-specialist` - Technical design

**Progress Tracking**:
- `TodoWrite` - Track phase progress, create task lists

---

## QUALITY PRINCIPLES

**Always**:
✅ Work phase by phase (Discovery → Analysis → Validation → Synthesis → Planning)
✅ Use TodoWrite to show progress
✅ Validate every claim before including in report
✅ Delegate to specialist agents for domain validation
✅ Document version conflicts with proposed resolution
✅ Prioritize gaps by regulatory risk and submission impact
✅ Generate actionable, executable roadmap with realistic estimates
✅ Create outputs incrementally (save after each phase)

**Never**:
❌ Modify existing documents (READ-ONLY mode)
❌ Skip validation (no hallucinations)
❌ Make assumptions without evidence
❌ Generate roadmap without effort estimates or dependencies
❌ Omit cross-references from validation
❌ Create report without executive summary

---

## SUCCESS CRITERIA

**Phase Completion**:
- Phase 1 ✅: Inventory complete, coverage matrix clear
- Phase 2 ✅: All 10 topics analyzed, gaps identified
- Phase 3 ✅: >90% fact-check score, cross-refs validated
- Phase 4 ✅: Gap matrix prioritized, risks assessed
- Phase 5 ✅: 6 epics with task breakdown, dependencies mapped

**Final Report Quality**:
- Comprehensive (all regulatory dimensions covered)
- Validated (no unverified claims)
- Actionable (roadmap is executable)
- Executive-ready (clear, concise, strategic)

---

## OUTPUT LOCATIONS

All outputs go to: `/Users/abelcosta/Documents/HemoDoctor/docs/outputs/`

Create this directory if it doesn't exist.

---

## USAGE EXAMPLES

**Full audit**:
"Start comprehensive strategic audit of all HemoDoctor dossier versions. Follow 5-phase methodology and generate executive report with roadmap."

**Specific topic**:
"Analyze only Clinical Evidence topic across all versions and generate gap list."

**Validation only**:
"Validate all claims in SRS-001 from fernanda version. Fact-check regulatory standards, cross-references, and technical specs."

**Comparison**:
"Compare SDD-001 between fernanda and fabio versions. Identify conflicts and recommend resolution."

**Roadmap generation**:
"Generate strategic roadmap with epics and tasks based on gaps already identified."

---

**You are now ready to conduct the audit. Begin with Phase 1 when the user requests.**

Use TodoWrite to create:
```
☐ Phase 1: Discovery (Document Inventory)
  ☐ Scan all version directories
  ☐ Create inventory CSV
  ☐ Build coverage matrix
  ☐ Identify orphan documents
☐ Phase 2: Deep Analysis (10 topics)
  ☐ Requirements
  ☐ Design
  ☐ Risk
  ☐ Clinical
  ☐ Quality
  ☐ Labeling
  ☐ Cyber
  ☐ Traceability
  ☐ Verification
  ☐ Deployment
☐ Phase 3: Validation
  ☐ Validate major documents
  ☐ Cross-check references
  ☐ Fact-check claims
☐ Phase 4: Synthesis
  ☐ Gap analysis matrix
  ☐ Strengths/weaknesses
  ☐ Risk assessment
  ☐ Quick wins
☐ Phase 5: Strategic Planning
  ☐ Define 6 epics
  ☐ Break down tasks
  ☐ Estimate effort
  ☐ Map dependencies
  ☐ Create roadmap
☐ Final Report
  ☐ Write executive summary
  ☐ Compile all findings
  ☐ Generate handoff doc
```

**Estimated duration**: 8-12 hours of continuous work. You can save state and resume between phases.
AGENTEOF

success "CLAUDE.md criado com sucesso"

# 5. Criar diretório de outputs
OUTPUTS_DIR="/Users/abelcosta/Documents/HemoDoctor/docs/outputs"
info "Criando diretório de outputs..."

if [ ! -d "$OUTPUTS_DIR" ]; then
    mkdir -p "$OUTPUTS_DIR"
    success "Diretório de outputs criado: $OUTPUTS_DIR"
else
    success "Diretório de outputs já existe"
fi

# 6. Criar README no diretório de outputs
cat > "$OUTPUTS_DIR/README.md" << 'OUTPUTREADME'
# CEO Consultant Agent - Outputs

Este diretório contém os outputs gerados pelo CEO Consultant Agent durante a auditoria estratégica do dossiê HemoDoctor.

## Estrutura de Outputs

### Phase 1: Discovery
- `01_Document_Inventory.csv` - Inventário completo de documentos
- `02_Coverage_Matrix.md` - Matriz de cobertura (versões × documentos)
- `03_Orphan_Documents.md` - Documentos únicos por versão

### Phase 2: Deep Analysis
- `04_Topic_Analysis_Requirements.md`
- `04_Topic_Analysis_Design.md`
- `04_Topic_Analysis_Risk.md`
- `04_Topic_Analysis_Clinical.md`
- `04_Topic_Analysis_Quality.md`
- `04_Topic_Analysis_Labeling.md`
- `04_Topic_Analysis_Cyber.md`
- `04_Topic_Analysis_Traceability.md`
- `04_Topic_Analysis_Verification.md`
- `04_Topic_Analysis_Deployment.md`

### Phase 3: Validation
- `05_Validation_Report_[DOC-ID].md` - Relatórios de validação por documento
- `06_Validation_Summary.csv` - Resumo de fact-checking

### Phase 4: Synthesis
- `07_Gap_Analysis_Matrix.csv` - Matriz de gaps priorizados
- `08_Strengths_Weaknesses.md` - Análise de forças/fraquezas
- `09_Risk_Assessment.md` - Avaliação de riscos
- `10_Quick_Wins.md` - Ganhos rápidos identificados

### Phase 5: Strategic Planning
- `11_Strategic_Roadmap.md` - Roadmap completo (6 épicos)
- `12_Dependency_Graph.mermaid` - Grafo de dependências
- `13_Effort_Estimates.csv` - Estimativas de esforço
- `14_Implementation_Handoff.md` - Handoff para agente de implementação

### Final Report
- `15_Executive_Report.md` - **Relatório Executivo Completo** (40-60 páginas)

## Como Usar

Os outputs são gerados automaticamente pelo agente durante a execução da auditoria.

**Iniciar auditoria completa**:
```
@ceo-consultant "Start comprehensive audit"
```

**Verificar progresso**:
```
@ceo-consultant "Show current phase and progress"
```

**Gerar relatório parcial**:
```
@ceo-consultant "Generate interim report based on phases completed so far"
```

## Formato dos Arquivos

- **CSV**: Importável em Excel/Google Sheets para análise
- **Markdown**: Legível diretamente no GitHub/VS Code
- **Mermaid**: Diagramas renderizáveis (usar Mermaid plugin)

## Timestamps

Cada execução do agente pode gerar outputs com timestamps para manter histórico:
- `15_Executive_Report_20251008.md`
- `15_Executive_Report_20251015.md` (após Epic 1)

---

**Gerado por**: CEO Consultant Agent
**Versão**: 1.0.0
OUTPUTREADME

success "README de outputs criado"

# 7. Criar arquivo de exemplo de uso
cat > "$AGENT_DIR/USAGE_EXAMPLES.md" << 'USAGEEOF'
# CEO Consultant Agent - Exemplos de Uso

## Auditoria Completa

```bash
@ceo-consultant "Start comprehensive strategic audit of all HemoDoctor dossier versions. Follow 5-phase methodology systematically. Generate full executive report with strategic roadmap. Use TodoWrite to track progress."
```

**Duração esperada**: 8-12 horas
**Output principal**: `outputs/15_Executive_Report.md`

---

## Análises Específicas

### Analisar apenas Clinical Evidence

```bash
@ceo-consultant "Analyze only the Clinical Evidence topic (PROJ-001, PROJ-002, CER-001) across all dossier versions. Identify gaps, assess quality, and validate statistical claims. Generate topic analysis report."
```

### Validar documento específico

```bash
@ceo-consultant "Validate all claims in SRS-001 from fernanda version. Fact-check all regulatory standard references, cross-references to other documents, and technical specifications. Generate validation report with fact-check score."
```

### Comparar versões

```bash
@ceo-consultant "Compare SDD-001 (Software Design Document) between fernanda and fabio versions. Identify all conflicts, assess which version is more complete, and recommend resolution strategy."
```

### Análise de gaps de cibersegurança

```bash
@ceo-consultant "Analyze cybersecurity documentation (SEC-001, DPIA) across all versions. Assess FDA §524B compliance, identify critical gaps, and generate action plan for cyber documentation completion."
```

---

## Consultas de Progresso

### Verificar status atual

```bash
@ceo-consultant "What phase are you currently working on? Show detailed progress with percentage completion and estimated time remaining."
```

### Mostrar resultados parciais

```bash
@ceo-consultant "Show me the gap analysis matrix generated so far, even if Phase 4 isn't complete. Prioritize gaps by CRITICAL/HIGH/MEDIUM/LOW."
```

### Listar documentos encontrados

```bash
@ceo-consultant "Show document inventory for all SRS (Software Requirements) documents found across all versions. Include version numbers, dates, and file sizes."
```

---

## Geração de Roadmap

### Roadmap completo

```bash
@ceo-consultant "Generate comprehensive strategic roadmap with 6 epics and detailed task breakdown. Include effort estimates, dependencies, critical path, and parallelization opportunities. Based on gaps identified in previous phases."
```

### Roadmap focado em gaps críticos

```bash
@ceo-consultant "Generate roadmap focusing only on CRITICAL priority gaps. Create epics and tasks specifically to address submission blockers. Estimate fastest path to regulatory submission readiness."
```

---

## Validação e Fact-Checking

### Validar claim regulatório específico

```bash
@ceo-consultant "Validate the claim in SRS-001 that states 'Complies with IEC 62304 Class C requirements per clause 5.2.6'. Use WebSearch to verify the standard clause and consult @anvisa-regulatory-specialist for interpretation."
```

### Checar referências cruzadas

```bash
@ceo-consultant "Check all cross-references in TEC-002 (Risk Management File). Verify that all referenced documents and sections exist. Identify broken links and generate fix list."
```

### Validar estatísticas clínicas

```bash
@ceo-consultant "Validate all statistical claims in PROJ-002 (Statistical Analysis Plan). Cross-check with CER-001 for consistency. Verify bootstrap methodology and confidence interval calculations. Consult @clinical-evidence-specialist."
```

---

## Consultas Ad-Hoc

### Identificar versão mais recente

```bash
@ceo-consultant "For each major document type (SRS, SDD, TEC, QMS, IFU), identify which version folder contains the most recent version based on date stamps and version numbers."
```

### Listar documentos órfãos

```bash
@ceo-consultant "Identify all orphan documents - documents that exist in only ONE version folder. Assess if they are important and should be incorporated into the authoritative dossier."
```

### Análise de completude ANVISA

```bash
@ceo-consultant "Check completeness against ANVISA RDC 751/2022 requirements. List all required documents per the regulation and indicate which are present, partially complete, or missing. Consult @anvisa-regulatory-specialist."
```

---

## Re-execução e Refinamento

### Re-executar com critérios mais rigorosos

```bash
@ceo-consultant "Re-run Phase 3 (Validation) with stricter criteria: fact-check score threshold 95% (instead of 90%). Flag any claim that cannot be directly verified from source documents or regulatory standards."
```

### Análise incremental após mudanças

```bash
@ceo-consultant "Re-audit only the Clinical Evidence topic. Previous audit was completed on 2025-10-08. Identify what has changed since then and update gap analysis accordingly."
```

### Adicionar novo tópico de análise

```bash
@ceo-consultant "Add new analysis topic: SOUP (Software of Unknown Provenance) management. Analyze all versions for SOUP lists, license compliance, and IEC 62304 SOUP requirements. Generate topic analysis report."
```

---

## Relatórios Customizados

### Relatório executivo resumido

```bash
@ceo-consultant "Generate executive summary only (2-3 pages): regulatory readiness score, top 5 critical gaps, estimated time to submission, and #1 strategic recommendation."
```

### Relatório técnico detalhado

```bash
@ceo-consultant "Generate detailed technical report for software architecture topic. Include all SDD versions, API specifications, database schemas, medical rules, and deployment architecture. Assess completeness for IEC 62304 Class C software design requirements."
```

### Relatório de traceability

```bash
@ceo-consultant "Generate comprehensive traceability report. Map all requirements (SRS) to design (SDD) to tests (TST) to risks (TEC-002) to labeling (IFU). Identify all broken links and gaps. Consult @traceability-specialist."
```

---

## Delegação para Agentes Especializados

### Revisão regulatória ANVISA

```bash
@ceo-consultant "Delegate to @anvisa-regulatory-specialist: Review SRS-001, SDD-001, and TEC-002 from fernanda version for ANVISA RDC 657/2022 and RDC 751/2022 compliance. Generate compliance report with gaps."
```

### Validação clínica

```bash
@ceo-consultant "Delegate to @clinical-evidence-specialist: Validate PROJ-001 (Clinical Protocol) and PROJ-002 (Statistical Analysis Plan) for scientific rigor. Assess if study design meets regulatory requirements for Class III SaMD. Identify weaknesses."
```

### Análise de risco

```bash
@ceo-consultant "Delegate to @risk-management-specialist: Review TEC-002 Risk Management File for ISO 14971 compliance. Check if all hazards are identified, risk controls are adequate, and residual risks are acceptable. Identify gaps."
```

---

## Exemplos de Output

### Coverage Matrix (exemplo)

```markdown
## Coverage Matrix

| Document  | fernanda | fabio | paulo | carlos | paula | daniel |
|-----------|----------|-------|-------|--------|-------|--------|
| SRS-001   |    ✓     |   ✓   |   ✓   |   ✓    |   ✓   |   -    |
| SDD-001   |    ✓     |   ✓   |   -   |   ✓    |   -   |   -    |
| TEC-002   |    ✓     |   -   |   ✓   |   ✓    |   ✓   |   ✓    |
| IFU-001   |    ✓     |   ✓   |   ✓   |   -    |   ✓   |   -    |
| QMS-001   |    ✓     |   -   |   -   |   ✓    |   ✓   |   -    |
```

### Gap Analysis (exemplo)

```csv
Gap ID,Topic,Description,Severity,Priority,Effort
GAP-001,Requirements,Missing NFRs (perf/sec),CRITICAL,CRITICAL,5 days
GAP-002,Risk,Incomplete cyber risk analysis,CRITICAL,CRITICAL,10 days
GAP-003,Clinical,Small sample size,HIGH,HIGH,30 days
GAP-004,Traceability,35 broken cross-refs,HIGH,HIGH,3 days
```

### Strategic Roadmap (exemplo)

```markdown
## EPIC 1: Authoritative Dossier Consolidation
**Priority**: CRITICAL
**Effort**: 33 days

### Tasks:
- Task 1.1: Reconcile SRS-001 versions (3 days)
- Task 1.2: Create master SRS-001 (5 days)
- Task 1.3: Reconcile SDD-001 versions (3 days)
- Task 1.4: Create master SDD-001 (5 days)
- [... more tasks ...]
```

---

**Dica**: Comece sempre com a auditoria completa. Depois use consultas específicas para deep dives em áreas de interesse.

**Duração típica**:
- Auditoria completa: 8-12 horas
- Análise de tópico específico: 1-2 horas
- Validação de documento: 30-60 min
- Comparação entre versões: 20-40 min
USAGEEOF

success "Arquivo de exemplos de uso criado"

# 8. Verificar instalação no Claude Code
info "Verificando configuração do Claude Code..."

CLAUDE_CONFIG="$HOME/.claude.json"
if [ ! -f "$CLAUDE_CONFIG" ]; then
    warning "Arquivo .claude.json não encontrado em $CLAUDE_CONFIG"
    warning "Você precisará registrar o agente manualmente no Claude Code"
else
    success "Claude Code configurado"
    info "Certifique-se de que o agente está registrado em ~/.claude.json"
fi

# 9. Resumo da instalação
echo ""
echo "═══════════════════════════════════════════════════════"
echo "  ✅ Instalação Concluída com Sucesso!"
echo "═══════════════════════════════════════════════════════"
echo ""
echo "📁 Agente instalado em:"
echo "   $AGENT_DIR"
echo ""
echo "📄 Arquivos criados:"
echo "   ✓ CLAUDE.md (prompt do agente)"
echo "   ✓ USAGE_EXAMPLES.md (exemplos de uso)"
echo ""
echo "📂 Diretório de outputs:"
echo "   $OUTPUTS_DIR"
echo ""
echo "🚀 Próximos Passos:"
echo ""
echo "1. Registrar agente no Claude Code (se necessário):"
echo "   - Abrir ~/.claude.json"
echo "   - Adicionar 'ceo-consultant-agent' à lista de agents"
echo ""
echo "2. Iniciar auditoria:"
echo "   @ceo-consultant \"Start comprehensive audit\""
echo ""
echo "3. Consultar documentação:"
echo "   cat $AGENT_DIR/USAGE_EXAMPLES.md"
echo ""
echo "📚 Documentação adicional:"
echo "   - Especificação completa: $(dirname "$0")/ceo-consultant-agent-spec.md"
echo "   - Guia de instalação: $(dirname "$0")/CEO_CONSULTANT_INSTALLATION_GUIDE.md"
echo ""
echo "═══════════════════════════════════════════════════════"
echo ""

# 10. Criar link simbólico para fácil acesso (opcional)
read -p "Criar link simbólico em ~/bin/ceo-consultant para fácil acesso? (s/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    BIN_DIR="$HOME/bin"
    if [ ! -d "$BIN_DIR" ]; then
        mkdir -p "$BIN_DIR"
    fi

    # Criar script wrapper
    cat > "$BIN_DIR/ceo-consultant" << 'WRAPPEREOF'
#!/bin/bash
# Wrapper para invocar CEO Consultant Agent
echo "Invocando CEO Consultant Agent..."
echo "Use no Claude Code: @ceo-consultant \"$*\""
WRAPPEREOF

    chmod +x "$BIN_DIR/ceo-consultant"
    success "Link simbólico criado em $BIN_DIR/ceo-consultant"

    # Verificar se ~/bin está no PATH
    if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
        warning "$BIN_DIR não está no PATH"
        echo "Adicione ao ~/.zshrc ou ~/.bashrc:"
        echo "  export PATH=\"\$HOME/bin:\$PATH\""
    fi
fi

echo ""
info "Instalação finalizada! Bom trabalho! 🎉"
echo ""
