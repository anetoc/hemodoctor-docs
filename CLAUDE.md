# 🏥 HemoDoctor - Contexto Completo para IA Agents

**Última Atualização:** 12 de Outubro de 2025 - 23:30 BRT  
**Versão do Projeto:** v2.0.0  
**Completude Geral:** 90%  
**Responsável:** Dr. Abel Costa (abel.costa@hemodoctor.com)

---

## 📋 LEIA ISTO PRIMEIRO (5 MINUTOS)

### O Que É HemoDoctor?

**HemoDoctor** é um **SaMD (Software as a Medical Device) Classe II** para apoio à decisão clínica em hematologia pediátrica, desenvolvido para atender regulações **ANVISA (RDC 751/657)**, **FDA**, e **ISO 13485/IEC 62304**.

**Classificação:** 
- ANVISA: Classe II (Risco Moderado)
- FDA: 510(k) Class II
- IEC 62304: Class C (Maior Risco)

**Status Atual:** 90% completo, pronto para submissão ANVISA e CEP

---

## 🎯 SITUAÇÃO ATUAL (12 Out 2025)

| Milestone | Status | Prazo | Completude |
|-----------|--------|-------|------------|
| **Documentação Regulatória** | ⚠️ | - | 90% (falta V&V) |
| **Código-Fonte Python** | ✅ | - | 90% (72% pass rate) |
| **Submissão ANVISA** | ⏳ | 20 Out | 85% |
| **Submissão CEP** | ⏳ | 14 Nov | 100% (docs) |
| **Testes Automatizados** | ⚠️ | 18 Out | 72% pass |

### Bloqueadores P0 (Próximos 8 dias)

1. **22 bugs críticos** no classificador de plaquetas → Corrigir → 90% pass rate
2. **3 annexos ANVISA** (CER-001) → Compilar PDFs
3. **3 sign-offs** (Medical, RA, QA) → Obter assinaturas
4. **Módulo 04 V&V** → Criar 5 documentos (VVP-001 + 3 TESTREP + COV-001)

---

## 📁 ESTRUTURA DO PROJETO

```
/Users/abelcosta/Documents/HemoDoctor/docs/
│
├── 📄 AUTHORITATIVE_BASELINE/        # 61 documentos oficiais (90%)
│   ├── 00-10 Módulos Regulatórios    # 9/10 completos (falta V&V)
│   └── README_FINAL.md               # Guia principal
│
├── 🔥 HEMODOCTOR_CONSOLIDADO_v2.0/   # CÓDIGO-FONTE! (5,571 arquivos)
│   ├── 01_SUBMISSAO_CEP/             # 29 docs, 100% completo
│   ├── 02_SUBMISSAO_ANVISA/          # 52 docs, 85% completo
│   ├── 03_DESENVOLVIMENTO/           # 2,217 arquivos Python
│   │   ├── CODIGO_FONTE/             # FastAPI + middlewares
│   │   ├── TESTES/                   # 95 test cases (pytest)
│   │   ├── API_SPECS/                # OpenAPI + JSON schemas
│   │   └── ESPECIFICACOES/           # SRS v2.3, SDD, TEC-002
│   ├── 04_ANALISES_ESTRATEGICAS/     # Roadmap 18 meses
│   └── 05_MASTER_DOCUMENTATION/      # Inventários + Specs
│
├── 🤖 HEMODOCTOR_AGENTES/            # 13 agentes especializados
│   ├── anvisa-regulatory-specialist/
│   ├── cep-protocol-specialist/
│   ├── quality-systems-specialist/
│   ├── software-architecture-specialist/
│   └── [+9 outros]
│
├── 🏢 WORKSPACES/                    # 6 contextos de trabalho
│   ├── 01_ETHICS_CEP/                # 27 docs CEP
│   ├── 02_DEV_TECHNICAL/
│   ├── 03_CLINICAL_DECISION/
│   ├── 04_REGULATORY_SUBMISSION/
│   ├── 05_CLINICAL_VALIDATION/
│   └── 06_RISK_QUALITY/
│
├── 📚 BMAD-METHOD/                   # Framework (165 MB)
├── 📊 HEMODOCTOR_REFERENCIAS/        # Artigos + PPTs (83 MB)
├── 📝 docs/                          # Relatórios (37 arquivos)
│   ├── reports/                      # 19 relatórios técnicos
│   ├── archive/                      # Documentos históricos
│   └── ceo-consultant/               # Materiais executivos
│
├── 🛠️ scripts/                       # 11 utilitários
├── ⚙️ .github/                       # CI/CD templates
└── 📋 [20 docs raiz]                 # README, VERSION, CHANGELOG
```

---

## 🚀 QUICK START PARA NOVO AGENTE

### Passo 1: Ler Documentos Essenciais (15 min)

1. **Este arquivo** (`CLAUDE.md`) - Você está aqui! ✅
2. **`README.md`** - Visão geral do projeto
3. **`VERSION.md`** - Status atual de cada módulo
4. **`PLANO_CONSOLIDACAO_COMPLETO_20251012.md`** - TODO list + roadmap
5. **`RELATORIO_EXPLORACAO_CONSOLIDADO_20251012.md`** - Código-fonte descoberto

### Passo 2: Entender o Código (10 min)

**Localização:** `HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/`

**Stack Tecnológica:**
```python
Framework: FastAPI 0.114.1
Runtime: Python 3.9+
ASGI Server: Uvicorn 0.30.6
Authentication: JWT (python-jose)
Validation: Pydantic 2.9.2
Testing: pytest 7.4.0+
```

**Arquivos-Chave:**
- `CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex/api/main.py` - FastAPI app
- `CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex/api/requirements.txt` - Dependências
- `TESTES/test_automation/` - 95 test cases
- `TESTES/BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md` - 22 bugs críticos

### Passo 3: Verificar TODO List (5 min)

**19 itens** priorizados (P0, P1, P2, P3)

**Ver:** Cursor sidebar (TODO plugin integrado) ou `PLANO_CONSOLIDACAO_COMPLETO_20251012.md`

### Passo 4: Escolher Agente Especializado

| Tarefa | Agente |
|--------|--------|
| Corrigir bugs Python | `@software-architecture-specialist` |
| Criar docs V&V | `@quality-systems-specialist` |
| Compilar annexos ANVISA | `@clinical-evidence-specialist` |
| Atualizar docs CEP | `@cep-protocol-specialist` |

**Localização:** `HEMODOCTOR_AGENTES/[nome-agente]/`

---

## 📊 COMPLETUDE POR MÓDULO

| Módulo | Status | % | Docs | Pendências |
|--------|--------|---|------|------------|
| **00 - Índice Geral** | ✅ | 100% | 11 | - |
| **01 - Regulatório** | ✅ | 100% | 5 | - |
| **02 - Controles Design** | ✅ | 100% | 15 | - |
| **03 - Gestão Risco** | ✅ | 100% | 4 | - |
| **04 - V&V** | ⚠️ | 50% | 2 | 5 docs |
| **05 - Avaliação Clínica** | ✅ | 100% | 4 | - |
| **06 - Rastreabilidade** | ✅ | 100% | 5 | - |
| **07 - Pós-Mercado** | ✅ | 100% | 8 | - |
| **08 - Rotulagem** | ✅ | 100% | 3 | - |
| **09 - Cybersecurity** | ✅ | 100% | 3 | - |
| **10 - SOUP** | ✅ | 100% | 1 | - |

**Total:** 61/66 documentos (faltam 5 docs V&V)

---

## 🔥 DESCOBERTAS RECENTES (12 Out 2025)

### 1. Código-Fonte Descoberto! 🎉

**Arquivo:** `HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip` (49 MB, nunca explorado antes!)

**Conteúdo:**
- ✅ 5,571+ arquivos organizados
- ✅ 2,217 arquivos Python (.py)
- ✅ FastAPI application completa
- ✅ 95 test cases automatizados
- ✅ 15 scripts Python de automação
- ✅ OpenAPI specs + 7 JSON schemas
- ✅ Documentação técnica completa

### 2. Arquitetura Identificada

```
┌─────────────────────────────────────────────────────────┐
│                FASTAPI APPLICATION (main.py)             │
├─────────────────────────────────────────────────────────┤
│  CORS Middleware | CorrelationID | Idempotency          │
├─────────────────────────────────────────────────────────┤
│  JWT Authentication (Bearer Token + Scopes)             │
├─────────────────────────────────────────────────────────┤
│  Engine (Decision) | RULES Storage | META Storage       │
├─────────────────────────────────────────────────────────┤
│  POST /decide (+ outros endpoints)                      │
└─────────────────────────────────────────────────────────┘
```

### 3. Testes Automatizados

- ✅ Framework: pytest 7.4.0+
- ✅ 95 test cases documentados
- ⚠️ **72% pass rate** (68/95 passed)
- ⚠️ **22 bugs críticos** (principalmente plaquetas pediátricas)
- ✅ Coverage configurado
- ✅ CI/CD ready

### 4. Status Submissões

#### ANVISA (Prazo: 20 Out - 8 dias) 🔥
- **Status:** 85% completo
- **Faltam:**
  - 3 annexos PDF (CER-001)
  - 3 sign-offs (Medical, RA, QA)
  - Cover letter + Petition
  - Manifest v2.0

#### CEP (Prazo: 14 Nov - 33 dias)
- **Status:** 100% (documentos criados)
- **Faltam:**
  - Definir equipe (PI, Co-PI, Estatístico, DPO)
  - Obter 5 anuências institucionais
  - Submeter Plataforma Brasil

---

## 📅 TIMELINE

```
┌────────────────────────────────────────────────────────┐
│ 14-18 Out │ SPRINT 1: ANVISA + BUGS                   │
│           │ ✅ Corrigir 22 bugs                        │
│           │ ✅ Compilar annexos                        │
│           │ ✅ 90% pass rate                           │
│           │ 🎯 SUBMISSÃO ANVISA (20/10)               │
├────────────────────────────────────────────────────────┤
│ 21-25 Out │ SPRINT 2: V&V                             │
│           │ ✅ VVP-001 + TESTREP + COV-001            │
│           │ 🎯 MÓDULO 04 100% (02/11)                 │
├────────────────────────────────────────────────────────┤
│ 28 Out-8 Nov │ SPRINT 3: CEP                          │
│              │ ✅ Definir equipe + anuências          │
├────────────────────────────────────────────────────────┤
│ 11-15 Nov │ SPRINT 4: SUBMISSÃO CEP                   │
│           │ 🎯 SUBMISSÃO (14/11)                      │
└────────────────────────────────────────────────────────┘
```

---

## 🤖 AGENTES ESPECIALIZADOS (13 total)

### Regulatórios

1. **anvisa-regulatory-specialist**
   - Expertise: RDC 751/657, DMR, Petição ANVISA
   - Usar para: Compilar annexos, criar formulários

2. **external-regulatory-consultant**
   - Expertise: FDA 510(k), CE-MDR, IMDRF
   - Usar para: Consultas internacionais

3. **regulatory-review-specialist**
   - Expertise: Revisão final, compliance check
   - Usar para: Auditoria pré-submissão

### Qualidade & Testes

4. **quality-systems-specialist**
   - Expertise: ISO 13485, V&V, DHF
   - Usar para: VVP-001, TESTREP, procedimentos QMS

5. **risk-management-specialist**
   - Expertise: ISO 14971, FMEA, RMP
   - Usar para: Análises de risco, PROC-002

### Técnicos

6. **software-architecture-specialist**
   - Expertise: IEC 62304, Python, FastAPI
   - Usar para: Corrigir bugs, TESTREP-002

7. **hematology-technical-specialist**
   - Expertise: Hematologia pediátrica, thresholds clínicos
   - Usar para: Validação de regras de decisão

### Clínicos

8. **clinical-evidence-specialist**
   - Expertise: CER, literatura científica, annexos
   - Usar para: Compilar annexos CER-001

9. **biostatistics-specialist**
   - Expertise: Sample size, power analysis, SAP
   - Usar para: Análises estatísticas CEP

10. **cep-protocol-specialist**
    - Expertise: Protocolos CEP/CONEP, Plataforma Brasil
    - Usar para: Atualizar docs CEP, submissão

### Outros

11. **traceability-specialist**
    - Expertise: Matrizes de rastreabilidade, TRC
    - Usar para: COV-001, RTM

12. **documentation-finalization-specialist**
    - Expertise: Consolidação, padronização, v1.0
    - Usar para: Consolidar baseline

13. **hemodoctor-orchestrator**
    - Expertise: Coordenação geral, priorização
    - Usar para: Gestão de múltiplos agentes

---

## 📚 DOCUMENTOS IMPORTANTES

### Regulatórios (AUTHORITATIVE_BASELINE)

| Documento | Localização | Status | Tamanho |
|-----------|-------------|--------|---------|
| SRS-001 | 02_CONTROLES_DESIGN/SRS/ | ✅ | 35 KB |
| SDD-001 | 02_CONTROLES_DESIGN/SDD/ | ✅ | 25 KB |
| TEC-002 (RMP) | 02_CONTROLES_DESIGN/TEC/ | ✅ | 55 KB |
| CER-001 | 05_AVALIACAO_CLINICA/CER/ | ⚠️ | 65 KB |
| SEC-001 | 09_CYBERSECURITY/SEC/ | ✅ | 30 KB |
| PMS-001 | 07_POS_MERCADO/PMS/ | ✅ | 22 KB |
| PROC-001/002/003 | 07_POS_MERCADO/Vigilancia/ | ✅ | 201 KB |

### Técnicos (CONSOLIDADO v2.0)

| Documento | Localização | Uso |
|-----------|-------------|-----|
| main.py | 03_DESENVOLVIMENTO/CODIGO_FONTE/.../api/ | FastAPI app |
| requirements.txt | 03_DESENVOLVIMENTO/CODIGO_FONTE/.../api/ | Dependências |
| BUG-001 | 03_DESENVOLVIMENTO/TESTES/ | 22 bugs críticos |
| TEST-HD-016 | 03_DESENVOLVIMENTO/TESTES/ | 95 test cases |
| ROADMAP_SRS_v3.0 | 03_DESENVOLVIMENTO/ | Consolidação SRS |

### Estratégicos (docs/)

| Documento | Tamanho | Propósito |
|-----------|---------|-----------|
| PLANO_CONSOLIDACAO_COMPLETO_20251012.md | 30 KB | TODO list + roadmap |
| RELATORIO_EXPLORACAO_CONSOLIDADO_20251012.md | 40 KB | Análise código-fonte |
| MAPEAMENTO_COMPLETO_REPOSITORIO_20251012.md | 38 KB | Estrutura completa |
| PROXIMOS_PASSOS_POS_V1.0.md | 25 KB | Roadmap até v3.0 |

---

## 🎯 PRIORIDADES P0 (CRÍTICO)

### 1. Corrigir Bugs (Prazo: 18 Out)

**Objetivo:** 72% → 90% pass rate

**Ações:**
- [ ] Ler `BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md`
- [ ] Corrigir 22 bugs (foco: plaquetas pediátricas)
- [ ] Re-run pytest suite
- [ ] Validar com hematologista

**Agente:** `@software-architecture-specialist`

**Comando:**
```bash
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/TESTES
cat BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md
# Analisar bugs e corrigir código-fonte
cd ../CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex
# Corrigir arquivos Python
pytest test_automation/ -v
```

### 2. Completar ANVISA (Prazo: 20 Out)

**Objetivo:** 85% → 100%

**Ações:**
- [ ] Compilar Annex B (15 páginas PDF)
- [ ] Compilar Annex D (32 páginas PDF)
- [ ] Compilar Annex E (80 páginas PDF)
- [ ] Obter 3 sign-offs
- [ ] Criar cover letter + petition
- [ ] Gerar manifest v2.0

**Agente:** `@anvisa-regulatory-specialist` + `@clinical-evidence-specialist`

### 3. Completar V&V (Prazo: 02 Nov)

**Objetivo:** 50% → 100%

**Ações:**
- [ ] VVP-001 (usar `@quality-systems-specialist`)
- [ ] TESTREP-001 (Unit Tests)
- [ ] TESTREP-002 (Integration Tests)
- [ ] TESTREP-003 (System Tests)
- [ ] COV-001 (usar `@traceability-specialist`)

**Template:** `INSTRUCOES_AGENTES_FASES_A_B.md`

---

## 🛠️ COMANDOS ÚTEIS

### Navegação

```bash
# Ir para projeto
cd /Users/abelcosta/Documents/HemoDoctor/docs

# Ver estrutura
tree -L 2

# Ver status
git status
git log --oneline -10
```

### Explorar Código

```bash
# Navegar para CONSOLIDADO
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010

# Ver código-fonte
cd 03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex
cat api/main.py
cat api/requirements.txt

# Ver testes
cd ../../TESTES/test_automation
pytest -v
pytest --cov
```

### Executar Scripts

```bash
# Scripts de automação
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex/tools

# Gerar manifest
python build_pre_anvisa_pack.py

# Gerar coverage
python coverage_report.py

# Gerar TRC
python generate_trc.py
```

### Ver Documentação

```bash
# Relatórios recentes
ls -lh docs/reports/

# BASELINE oficial
cd AUTHORITATIVE_BASELINE
ls -R

# Ver TODO list
# (Integrado no Cursor - sidebar)
```

---

## 📞 CONTATOS

| Função | Nome | Email |
|--------|------|-------|
| **Responsável Técnico** | Dr. Abel Costa | abel.costa@hemodoctor.com |
| **Colaborador UNIMED** | Dr. Lucyo Diniz | (via UNIMED Vale do São Francisco) |
| **PI (CEP)** | {A DEFINIR} | - |
| **Estatístico** | {A DEFINIR} | - |
| **DPO** | {A DEFINIR} | - |

**Instituição:** HemoDoctor (anteriormente IDOR São Paulo)

---

## 🔄 HISTÓRICO DE MUDANÇAS RECENTES

### 12 de Outubro de 2025

**Commits (5):**
- 42a3835: Atualização institucional completa (IDOR → HemoDoctor, 41 arquivos)
- fd8c85c: Relatório de atualização institucional
- 105bcda: Análise de status global do projeto
- 3937952: Mapeamento completo do repositório (770 linhas)
- 0ded85e: Exploração CONSOLIDADO v2.0 (725 linhas)

**Descobertas:**
- ✅ Código-fonte Python (FastAPI) encontrado
- ✅ 5,571 arquivos organizados
- ✅ 95 test cases identificados
- ✅ Arquitetura moderna confirmada
- ⚠️ 22 bugs críticos documentados
- ⚠️ 72% pass rate (meta: 90%)

**Atualizações:**
- ✅ IDOR → HemoDoctor (41 arquivos)
- ✅ @idor.org → @hemodoctor.com (21 arquivos)
- ✅ UNIMED adicionada (Dr. Lucyo Diniz)
- ✅ TODO list criada (19 itens)
- ✅ Plano de consolidação criado

---

## 🎯 MÉTRICAS DE SUCESSO

| Métrica | Atual | Meta | Prazo |
|---------|-------|------|-------|
| **Completude Geral** | 90% | 100% | 02 Nov |
| **Pass Rate Testes** | 72% | 90% | 18 Out |
| **Docs Oficiais** | 61 | 66 | 02 Nov |
| **Bugs Críticos** | 22 | 0 | 18 Out |
| **Módulos Completos** | 9/10 | 10/10 | 02 Nov |
| **Submissões** | 0 | 2 | 14 Nov |

---

## 🚦 REGRAS DE OURO

### Para Novos Agentes

1. **SEMPRE** leia este `CLAUDE.md` primeiro
2. **SEMPRE** verifique TODO list antes de começar
3. **SEMPRE** use agente especializado apropriado
4. **SEMPRE** faça commit descritivo após mudanças
5. **NUNCA** modifique `AUTHORITATIVE_BASELINE` sem revisar
6. **NUNCA** crie documentos duplicados
7. **NUNCA** ignore bugs críticos (P0)

### Para Commits

```bash
# Formato preferido:
git commit -m "🎯 [Categoria] Ação realizada

Detalhes:
- Item 1
- Item 2
- Item 3

Impacto: [P0/P1/P2/P3]
Módulo: [01-10]"
```

**Emojis:**
- 🎯 Feature/implementação
- 🐛 Bug fix
- 📄 Documentação
- 🔧 Configuração
- ✅ Teste
- 🏢 Atualização institucional
- 🔍 Análise/exploração

---

## 📖 GLOSSÁRIO

| Termo | Significado |
|-------|-------------|
| **SaMD** | Software as a Medical Device |
| **ANVISA** | Agência Nacional de Vigilância Sanitária (Brasil) |
| **CEP** | Comitê de Ética em Pesquisa |
| **CONEP** | Comissão Nacional de Ética em Pesquisa |
| **RDC** | Resolução da Diretoria Colegiada (ANVISA) |
| **DMR** | Device Master Record |
| **DHF** | Design History File |
| **SRS** | Software Requirements Specification |
| **SDD** | Software Design Description |
| **RMP** | Risk Management Plan |
| **CER** | Clinical Evaluation Report |
| **V&V** | Verification & Validation |
| **VVP** | Verification & Validation Plan |
| **TESTREP** | Test Report |
| **COV** | Coverage Analysis |
| **PROC** | Procedimento |
| **FORM** | Formulário |
| **TRC** | Traceability Matrix |
| **RTM** | Requirements Traceability Matrix |
| **SOUP** | Software of Unknown Provenance |
| **PMS** | Post-Market Surveillance |
| **CAPA** | Corrective and Preventive Action |

---

## 🏆 STATUS BADGES

```
✅ BASELINE: 90% Completo
⚠️ V&V: 50% Completo
🔥 ANVISA: 85% Completo (Prazo: 8 dias)
✅ CEP: 100% Docs Criados
⚠️ Testes: 72% Pass Rate
✅ Código: FastAPI Funcional
```

---

## 📍 LINKS RÁPIDOS

### Documentação Essencial
- [README.md](README.md) - Visão geral
- [VERSION.md](VERSION.md) - Status por módulo
- [CHANGELOG.md](CHANGELOG.md) - Histórico
- [PLANO_CONSOLIDACAO_COMPLETO_20251012.md](PLANO_CONSOLIDACAO_COMPLETO_20251012.md) - TODO + Roadmap

### Análises Recentes
- [RELATORIO_EXPLORACAO_CONSOLIDADO_20251012.md](RELATORIO_EXPLORACAO_CONSOLIDADO_20251012.md)
- [MAPEAMENTO_COMPLETO_REPOSITORIO_20251012.md](MAPEAMENTO_COMPLETO_REPOSITORIO_20251012.md)
- [ANALISE_STATUS_GLOBAL_PROJETO.md](ANALISE_STATUS_GLOBAL_PROJETO.md)

### Guias Operacionais
- [PROXIMOS_PASSOS_POS_V1.0.md](PROXIMOS_PASSOS_POS_V1.0.md)
- [INSTRUCOES_AGENTES_FASES_A_B.md](INSTRUCOES_AGENTES_FASES_A_B.md)
- [GUIA_USO_WORKSPACES.md](GUIA_USO_WORKSPACES.md)

---

## 🎉 MENSAGEM FINAL

**Status:** 🟢 EXCELENTE (90% completo)

**Próxima Milestone:** ANVISA Submission (20/10/2025 - 8 dias)

**Código:** ✅ FastAPI funcional com 95 test cases

**Documentação:** ✅ 61/66 documentos oficiais

**Equipe:** ✅ 13 agentes especializados prontos

---

**Este contexto está PRONTO para qualquer novo agente continuar o trabalho!**

**Boa sorte! 🚀**

---

**Última Atualização:** 12 de Outubro de 2025 - 23:30 BRT  
**Próxima Revisão:** 14 de Outubro de 2025 (início Sprint 1)  
**Mantenedor:** Dr. Abel Costa (abel.costa@hemodoctor.com)

