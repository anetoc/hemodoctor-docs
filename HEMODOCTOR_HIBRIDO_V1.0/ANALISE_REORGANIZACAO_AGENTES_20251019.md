# 🔄 ANÁLISE E REORGANIZAÇÃO - ECOSSISTEMA DE AGENTES

**Data:** 19 de Outubro de 2025
**Versão:** 1.0
**Projeto:** HemoDoctor Hybrid V1.0
**Objetivo:** Limpar e reorganizar arquitetura de agentes considerando skills, plugins e tools

---

## 📊 SITUAÇÃO ATUAL (MAPEAMENTO COMPLETO)

### **INVENTÁRIO TOTAL**

| Categoria | Quantidade | Localização |
|-----------|------------|-------------|
| **Agents Instalados** | 31 | `~/.claude/agents/` |
| **Agents HemoDoctor** | 13 | `docs/HEMODOCTOR_AGENTES/` |
| **Agents BMAD/General** | 18 | `~/.claude/agents/` |
| **User-Level Skills** | 12 | `~/.claude/plugins/marketplaces/` |
| **Project-Level Skills** | 9 | `.claude/skills/` |
| **MCPs Configurados** | 19 | `~/.claude.json` |

**Total de Capabilities:** 31 agents + 21 skills + 19 MCPs = **71 ferramentas**

---

## 🤖 AGENTES DETALHADOS

### **A. HemoDoctor Regulatory (13 agents)**

#### Instalados em AMBOS os locais:

| # | Agent | Função | Status |
|---|-------|--------|--------|
| 1 | `anvisa-regulatory-specialist` | ANVISA RDC 657/751 compliance | ✅ Ativo |
| 2 | `biostatistics-specialist` | Sample size, SAP, power analysis | ✅ Ativo |
| 3 | `cep-protocol-specialist` | CEP/Ethics, TCLE, Plataforma Brasil | ✅ Ativo |
| 4 | `clinical-evidence-specialist` | Clinical validation, N=2,900 | ✅ Ativo |
| 5 | `documentation-finalization-specialist` | ANVISA/FDA packages | ✅ Ativo |
| 6 | `external-regulatory-consultant` | Global regulatory (FDA/CE-MDR) | ✅ Ativo |
| 7 | `hematology-technical-specialist` | CBC workflows, reference ranges | ✅ Ativo |
| 8 | `hemodoctor-orchestrator` | Multi-agent coordination | ✅ Ativo (LEAD) |
| 9 | `quality-systems-specialist` | ISO 13485 QMS | ✅ Ativo |
| 10 | `regulatory-review-specialist` | Document review, submission | ✅ Ativo |
| 11 | `risk-management-specialist` | ISO 14971, FMEA | ✅ Ativo |
| 12 | `software-architecture-specialist` | IEC 62304 Class C | ✅ Ativo |
| 13 | `traceability-specialist` | Requirements tracing | ✅ Ativo |

### **B. BMAD/General Purpose (18 agents)**

#### Core Workflow (5):
| # | Agent | Função | Status |
|---|-------|--------|--------|
| 14 | `spec-writer` | Specification writing + research | ✅ Ativo |
| 15 | `coder-agent` | Development + TDD | ✅ Ativo |
| 16 | `analyzer-agent` | Metrics analysis | ✅ Ativo |
| 17 | `debugger-agent` | Auto-fix bugs (~70% success) | ✅ Ativo |
| 18 | `consultant-agent` | Critical review ⭐ | ✅ Ativo |

#### Research & Planning (2):
| # | Agent | Função | Status |
|---|-------|--------|--------|
| 19 | `research-agent` | Deep research ($0/mês) | ✅ Ativo |
| 20 | `strategist-agent` | Roadmaps, ADRs, planning | ✅ Ativo |

#### Operations (3):
| # | Agent | Função | Status |
|---|-------|--------|--------|
| 21 | `monitor-agent` | Observability 24/7 | ✅ Ativo |
| 22 | `refactor-agent` | Code quality | ✅ Ativo |
| 23 | `update-manager` | Agent maintenance | ✅ Ativo |

#### Specialized (3):
| # | Agent | Função | Status |
|---|-------|--------|--------|
| 24 | `orchestrator-agent` | Multi-agent coordinator (general) | ⚠️ Redundante? |
| 25 | `n8n-agent` | n8n workflows | ✅ Ativo |
| 26 | `rag-agent` | RAG systems | ✅ Ativo |

#### Product & PM (3):
| # | Agent | Função | Status |
|---|-------|--------|--------|
| 27 | `project-manager-agent` | Agile PM, milestones | ✅ Ativo |
| 28 | `qa-lead-agent` | Test automation, quality | ✅ Ativo |
| 29 | `product-owner-agent` | Requirements, backlog | ✅ Ativo |

#### Executive (2):
| # | Agent | Função | Status |
|---|-------|--------|--------|
| 30 | `ceo-consultant-agent` | Executive decision-making | ✅ Ativo |
| 31 | `bmad` | Complete BMAD workflow | ⚠️ Meta-agent? |

---

## 🎨 SKILLS DISPONÍVEIS

### **User-Level (12 skills)**

| Category | Skills | Use Case |
|----------|--------|----------|
| **Document** | document-skills | PDF, XLSX, DOCX, PPTX manipulation |
| **Creative** | algorithmic-art, canvas-design, slack-gif-creator | Art, designs, GIFs |
| **Development** | artifacts-builder, webapp-testing | Web components, E2E tests |
| **Enterprise** | brand-guidelines, internal-comms, theme-factory | Branding, communication |
| **Meta** | skill-creator, template-skill, mcp-builder | Create skills/MCPs |

### **Project-Level (9 skills)**

| Category | Skills | Use Case |
|----------|--------|----------|
| **Core** | yaml-validation, evidence-engine, test-suite, documentation | YAML work, tests, docs |
| **Advanced** | hemodoctor-validator, code-helper, next-steps-debugger, yaml-dag-visualizer, clinical-test-generator | Validation, code gen, debug, viz, test gen |

---

## 🔌 MCPs CONFIGURADOS (19)

| Category | MCPs | Função |
|----------|------|--------|
| **Core** | filesystem, github, postgresql, memory, sequential-thinking, jetbrains | Basic operations |
| **GraphRAG** | qdrant, neo4j | Vector + Knowledge graph |
| **AI/LLM** | ollama | Local LLM (privacy) |
| **Processing** | grobid, presidio, playwright | PDF parse, de-id, web scraping |
| **Clinical** | terminology, fhir | SNOMED/ICD-10, FHIR R4 |
| **Governance** | policy-guard | Privacy enforcement |
| **Automation** | n8n, firecrawl | Workflows, crawling |
| **Web** | brave-search | Web search (optional) |
| **UI** | shadcn | UI components (on-demand) |

---

## 🔍 ANÁLISE DE REDUNDÂNCIAS E GAPS

### **🟡 REDUNDÂNCIAS IDENTIFICADAS**

#### 1. **Orchestrator Agents (2)**
**Problema:**
- `hemodoctor-orchestrator` (HemoDoctor-specific)
- `orchestrator-agent` (General-purpose)

**Análise:**
- `hemodoctor-orchestrator`: Cold start, backlog management, HemoDoctor-specific
- `orchestrator-agent`: General multi-agent coordination

**Recomendação:** ✅ **MANTER AMBOS** (propósitos diferentes)
- `hemodoctor-orchestrator` → Lead agent para HemoDoctor
- `orchestrator-agent` → General-purpose para outros projetos

#### 2. **Meta-Agents**
**Problema:**
- `bmad` (meta-agent que chama outros)
- Outros agents já fazem o trabalho

**Análise:**
- `bmad` é um wrapper/conveniente para workflow completo
- Útil para usuários que querem workflow pré-definido

**Recomendação:** ✅ **MANTER** (conveniência)

### **🔴 GAPS IDENTIFICADOS**

#### 1. **No HemoDoctor: Data Analysis Agent**
**Gap:** Análise de dados clínicos (CBC datasets)
**Capability Missing:**
- Statistical analysis beyond biostatistics
- Data visualization
- Exploratory data analysis

**Recomendação:** ⚠️ **CONSIDERAR** criar `data-analyst-agent`
- Ou usar `analyzer-agent` (já existe)

#### 2. **No HemoDoctor: Clinical Validation Agent**
**Gap:** Validation protocols execution
**Capability Missing:**
- Protocol execution automation
- Adjudication workflows
- Ground truth comparison

**Recomendação:** ⚠️ **CONSIDERAR** criar `clinical-validation-agent`
- Ou usar `qa-lead-agent` com clinical context

#### 3. **Skills: Missing Integration Test Skill**
**Gap:** Integration testing guidance
**Capability Missing:**
- Integration test patterns
- API testing
- End-to-end test scenarios

**Recomendação:** ⚠️ **CONSIDERAR** criar skill em `.claude/skills/`

### **🟢 COMPLEMENTARIDADES (BEM FEITAS)**

#### Skills ↔ Agents
✅ **EXCELENTE complementaridade:**
- `yaml-validation` skill → usado por agents
- `hemodoctor-validator` skill → usado por `regulatory-review-specialist`
- `clinical-test-generator` skill → usado por `qa-lead-agent`
- `document-skills` → usado por `documentation-finalization-specialist`

#### MCPs ↔ Agents
✅ **BOA integração:**
- `postgresql` MCP → usado por agents para queries
- `github` MCP → usado por `coder-agent`, `spec-writer`
- `jetbrains` MCP → usado por development agents
- `ollama` MCP → usado por privacy-sensitive tasks

---

## 🎯 PROPOSTA DE REORGANIZAÇÃO

### **ARQUITETURA RECOMENDADA**

```
┌────────────────────────────────────────────────────────────┐
│                    USER REQUEST                            │
└─────────────────────────┬──────────────────────────────────┘
                          │
                          ▼
        ┌─────────────────────────────────────────┐
        │     ROUTING LAYER                       │
        │  - Detect project context               │
        │  - Route to appropriate lead agent      │
        └────────┬─────────────────┬──────────────┘
                 │                 │
    ┌────────────┴────────┐       └──────────────────┐
    │                     │                          │
    ▼                     ▼                          ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ HEMODOCTOR      │  │ BMAD/GENERAL    │  │ OTHER PROJECTS  │
│ LEAD AGENT      │  │ LEAD AGENT      │  │ LEAD AGENT      │
└────────┬────────┘  └────────┬────────┘  └────────┬────────┘
         │                    │                     │
         └────────────────────┴─────────────────────┘
                              │
                              ▼
                ┌─────────────────────────────┐
                │  EXECUTION LAYER            │
                │  - 31 Specialized Agents    │
                │  - 21 Skills                │
                │  - 19 MCPs                  │
                └─────────────────────────────┘
```

### **LEAD AGENTS DEFINIDOS**

| Project Context | Lead Agent | Sub-Agents |
|----------------|------------|------------|
| **HemoDoctor** | `hemodoctor-orchestrator` | 13 HemoDoctor agents + BMAD quando necessário |
| **General Development** | `project-manager-agent` | 18 BMAD agents |
| **n8n Workflows** | `n8n-agent` | Support agents as needed |
| **RAG Systems** | `rag-agent` | Support agents as needed |

---

## 🛠️ AÇÕES RECOMENDADAS

### **🟢 PRIORIDADE ALTA (Fazer Agora)**

#### 1. Atualizar `AGENTS_INDEX.md`
**Ação:** Corrigir contagem de 28 → 31 agents
**Arquivo:** `~/.claude/agents/AGENTS_INDEX.md`
**Impacto:** Documentação correta

#### 2. Criar `AGENTS_MATRIX.md`
**Ação:** Matriz completa Agent ↔ Skills ↔ MCPs
**Arquivo:** Novo em `~/.claude/agents/`
**Impacto:** Visibilidade de capabilities

#### 3. Limpar Arquivos Duplicados
**Ação:** Remover arquivos "* 2.md" em HEMODOCTOR_HIBRIDO_V1.0
**Arquivos:**
- CLAUDE 2.md
- INDEX_COMPLETO 2.md
- INSTRUCOES_GIT 2.md
- etc. (6 arquivos)
**Impacto:** Limpeza

#### 4. Atualizar STATUS_ATUAL.md
**Ação:** Atualizar data 13 Out → 19 Out
**Arquivo:** `docs/STATUS_ATUAL.md`
**Impacto:** Status atual correto

### **🟡 PRIORIDADE MÉDIA (Próxima Semana)**

#### 5. Criar `data-analyst-agent` (se necessário)
**Decisão:** Avaliar se `analyzer-agent` é suficiente
**Ação:** Se não, criar novo agent especializado em CBC data

#### 6. Documentar Workflows por Projeto
**Ação:** Criar `WORKFLOWS_HEMODOCTOR.md`, `WORKFLOWS_BMAD.md`
**Impacto:** Guias de uso específicos

#### 7. Testar Integration Patterns
**Ação:** Testar agent → skill → MCP pipelines
**Impacto:** Validar arquitetura

### **⚪ PRIORIDADE BAIXA (Futuro)**

#### 8. Considerar `clinical-validation-agent`
**Decisão:** Avaliar necessidade após Sprint 0

#### 9. Criar Integration Test Skill
**Ação:** Skill específica para integration testing

#### 10. Otimizar Cold Start
**Ação:** Melhorar `hemodoctor-orchestrator` cold start (<2 min)

---

## 📋 MATRIZ DE RESPONSABILIDADES (PROPOSTA)

### **HemoDoctor Project**

| Fase | Lead Agent | Sub-Agents | Skills | MCPs |
|------|-----------|------------|--------|------|
| **Requirements** | `hemodoctor-orchestrator` | `product-owner-agent`, `cep-protocol-specialist` | documentation | github |
| **Design** | `hemodoctor-orchestrator` | `software-architecture-specialist`, `risk-management-specialist` | yaml-validation | jetbrains |
| **Implementation** | `hemodoctor-orchestrator` | `coder-agent`, `hematology-technical-specialist` | code-helper, evidence-engine | ollama, jetbrains |
| **Testing** | `hemodoctor-orchestrator` | `qa-lead-agent`, `software-architecture-specialist` | test-suite, clinical-test-generator | pytest |
| **Validation** | `hemodoctor-orchestrator` | `clinical-evidence-specialist`, `biostatistics-specialist` | hemodoctor-validator | postgresql |
| **Regulatory** | `hemodoctor-orchestrator` | `anvisa-regulatory-specialist`, `regulatory-review-specialist` | documentation, yaml-dag-visualizer | document-skills |
| **Submission** | `hemodoctor-orchestrator` | `documentation-finalization-specialist`, `traceability-specialist` | document-skills | - |

---

## 🎯 NOVA ESTRUTURA DE DOCUMENTAÇÃO

### **Arquivos a Criar/Atualizar**

```
~/.claude/agents/
├── AGENTS_INDEX.md           ← Atualizar (28 → 31)
├── AGENTS_MATRIX.md          ← NOVO (Agent ↔ Skills ↔ MCPs)
├── WORKFLOWS_HEMODOCTOR.md   ← NOVO (HemoDoctor-specific)
├── WORKFLOWS_BMAD.md         ← NOVO (General development)
└── BMAD_WORKFLOW.md          ← Já existe ✅

docs/HEMODOCTOR_HIBRIDO_V1.0/
├── CLAUDE.md                 ← Atualizar (nova arquitetura)
├── AGENTS_GUIDE.md           ← NOVO (Como usar agents)
├── SKILLS_GUIDE.md           ← Já existe (.claude/skills/README.md)
└── STATUS_ATUAL.md           ← Atualizar (13 Out → 19 Out)

docs/
├── STATUS_ATUAL.md           ← Atualizar
└── ANALISE_REORGANIZACAO_AGENTES_20251019.md ← ESTE ARQUIVO
```

---

## ✅ CHECKLIST DE EXECUÇÃO

### **Fase 1: Limpeza (30 min)**
- [ ] Remover arquivos "* 2.md" (6 arquivos)
- [ ] Atualizar STATUS_ATUAL.md (data 13 → 19 Out)
- [ ] Arquivar backups antigos em ~/.claude/agents/

### **Fase 2: Documentação (1h)**
- [ ] Atualizar AGENTS_INDEX.md (28 → 31 agents)
- [ ] Criar AGENTS_MATRIX.md (matrix completa)
- [ ] Atualizar CLAUDE.md em HEMODOCTOR_HIBRIDO_V1.0

### **Fase 3: Workflows (1h)**
- [ ] Criar WORKFLOWS_HEMODOCTOR.md
- [ ] Criar WORKFLOWS_BMAD.md
- [ ] Criar AGENTS_GUIDE.md

### **Fase 4: Validação (30 min)**
- [ ] Testar workflow com `hemodoctor-orchestrator`
- [ ] Testar agent → skill → MCP pipeline
- [ ] Documentar results

**Tempo Total Estimado:** 3 horas

---

## 🎊 CONCLUSÕES

### **✅ PONTOS FORTES ATUAIS**

1. **Cobertura Excelente:** 31 agents + 21 skills + 19 MCPs = 71 capabilities
2. **Complementaridade:** Skills e agents trabalham bem juntos
3. **Organização:** Separação clara HemoDoctor vs BMAD
4. **Lead Agent:** `hemodoctor-orchestrator` bem definido
5. **Custo:** $0/mês (incluído no plano Max)

### **⚠️ ÁREAS DE MELHORIA**

1. **Documentação:** Índice desatualizado (28 vs 31)
2. **Arquivos Duplicados:** 6 arquivos "* 2.md" para remover
3. **Status:** STATUS_ATUAL.md desatualizado (6 dias)
4. **Workflows:** Faltam guias específicos por projeto
5. **Matrix:** Falta matriz Agent ↔ Skills ↔ MCPs

### **🎯 PRÓXIMOS PASSOS IMEDIATOS**

1. ⚡ **Limpar** arquivos duplicados (10 min)
2. ⚡ **Atualizar** AGENTS_INDEX.md (15 min)
3. ⚡ **Criar** AGENTS_MATRIX.md (30 min)
4. 📅 **Agendar** validação workflows (próxima semana)

---

## 📊 MÉTRICAS DE SUCESSO

| Métrica | Antes | Depois | Meta |
|---------|-------|--------|------|
| **Agents Documentados** | 28 | 31 | 31 ✅ |
| **Arquivos Duplicados** | 6 | 0 | 0 ⚡ |
| **Status Atualizado** | 13 Out | 19 Out | Current ⚡ |
| **Workflows Documentados** | 1 | 3 | 3 ⚡ |
| **Matrix Completa** | ❌ | ✅ | ✅ ⚡ |

---

**Status:** ✅ ANÁLISE COMPLETA
**Próximo:** Executar Fase 1 (Limpeza)
**Responsável:** Dr. Abel Costa
**Data:** 19 de Outubro de 2025
**Versão:** 1.0
