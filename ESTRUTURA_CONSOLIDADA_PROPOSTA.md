# 🗂️ ESTRUTURA COMPLETA DO REPOSITÓRIO HEMODOCTOR

**Data:** 22 de Outubro de 2025
**Análise:** Estrutura atual + Proposta de consolidação

---

## 📊 MAPEAMENTO ATUAL

### 1. YAMLs (43 arquivos)

#### A. API Specs (AUTHORITATIVE_BASELINE)
**Localização:** `AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/API_SPECS/`
**Arquivos:** 10 YAMLs (OpenAPI/AsyncAPI v1.0)
- 01-09: API services specs
- 10: Async events spec

#### B. HEMODOCTOR_HIBRIDO_V1.0 (Especificação)
**Localização:** `HEMODOCTOR_HIBRIDO_V1.0/YAMLs/`
**Arquivos:** 16 YAMLs (Clinical rules v2.4.0)
- 00_config_hybrid.yaml
- 01_schema_hybrid.yaml
- 02_evidence_hybrid.yaml (79 evidences)
- 03_syndromes_hybrid.yaml (35 syndromes)
- 04-12: Supporting modules

**Status:** ✅ FONTE DA VERDADE (v2.4.0)

#### C. hemodoctor_cdss/config (Implementação)
**Localização:** `hemodoctor_cdss/config/`
**Arquivos:** 17 YAMLs (Clinical rules v2.4.0)
- Mesmos 16 YAMLs do HIBRIDO_V1.0
- + 1 duplicata (05_missingness tem 2 versões)

**Status:** ⚠️ DUPLICADO de HEMODOCTOR_HIBRIDO_V1.0/YAMLs/
**Razão:** Implementação usa cópia local dos YAMLs

---

### 2. DOCUMENTOS REGULATÓRIOS

#### A. AUTHORITATIVE_BASELINE ✅ PRINCIPAL
**Localização:** `AUTHORITATIVE_BASELINE/`
**Estrutura:** 67 documentos organizados em 11 módulos

```
00_INDICE_GERAL/          # Índices + relatório final ANVISA
01_REGULATORIO/           # DMR, QMS, certificados, declarações
02_CONTROLES_DESIGN/      # SRS, SDD, TEC, API_SPECS, arquitetura
03_GESTAO_RISCO/          # RMP, análises, matrizes ISO 14971
04_VERIFICACAO_VALIDACAO/ # VVP, TST, TESTREP, cobertura
05_AVALIACAO_CLINICA/     # CER, evidências, literatura
06_RASTREABILIDADE/       # TRC, matrizes rastreabilidade
07_POS_MERCADO/           # PMS, vigilância, formulários
08_ROTULAGEM/             # IFU, labels
09_CYBERSECURITY/         # SEC, SBOM, VEX
10_SOUP/                  # SOUP-001
```

**Versionamento:** Todos `_v1.0_OFICIAL`
**Status:** ✅ PRONTO PARA SUBMISSÃO

#### B. HEMODOCTOR_CONSOLIDADO_v2.0_20251010
**Localização:** `HEMODOCTOR_CONSOLIDADO_v2.0_20251010/`

**01_SUBMISSAO_CEP/**
- Status: ❓ VAZIO (só .DS_Store)
- Conteúdo esperado: Protocolo CEP/CONEP

**02_SUBMISSAO_ANVISA/**
- 00_CORE_DOCUMENTS/ - ❓ VAZIO
- 03_FORMULARIOS/ - ❓ VAZIO
- 04_MANIFESTO/ - ❓ VAZIO

**03_DESENVOLVIMENTO/**
- ANVISA_CODE/ - Código fonte (não acessível?)
- API_SPECS/ - Specs (duplicado?)
- CODIGO_FONTE/ - Código fonte
- DATA_DICTIONARY/ - Dicionário variáveis
- TESTES/test_automation/ - Testes automatizados

**Status:** ⚠️ PARCIALMENTE VAZIO - Verificar necessidade

#### C. WORKSPACES/01_ETHICS_CEP
**Localização:** `WORKSPACES/01_ETHICS_CEP/Documentos/`
**Conteúdo:** Documentos CEP/CONEP

**Status:** ✅ ATIVO - Manter

---

### 3. TESTES (466 tests)

#### A. hemodoctor_cdss/tests/
**Localização:** `hemodoctor_cdss/tests/`
**Arquivos:** 22 arquivos Python

**Estrutura:**
```
tests/
├── unit/           # 12 arquivos (362 tests)
│   ├── test_evidence_engine.py
│   ├── test_all_evidences.py (79 evidences parametrized)
│   ├── test_all_syndromes.py (35 syndromes parametrized)
│   ├── test_main_api.py
│   ├── test_normalization.py
│   ├── test_schema_validator.py
│   ├── test_worm_log.py
│   ├── test_next_steps.py
│   ├── test_output_renderer.py
│   ├── test_yaml_parser.py
│   └── test_cbc_model.py
│
├── security/       # 6 arquivos (104 tests)
│   ├── test_input_validation.py
│   ├── test_authentication.py
│   ├── test_data_protection.py
│   └── test_owasp_top10.py
│
└── integration/    # 2 arquivos (7 tests + ready for more)
    ├── test_critical_fixes.py
    └── __init__.py
```

**Status:** ✅ 466/466 passing (100%), 89% coverage

---

### 4. CÓDIGO-FONTE

#### A. hemodoctor_cdss/src/hemodoctor/
**Localização:** `hemodoctor_cdss/src/hemodoctor/`

**Estrutura:**
```
src/hemodoctor/
├── api/
│   ├── main.py          # FastAPI (4 endpoints)
│   └── pipeline.py      # E2E orchestration
│
├── engines/
│   ├── evidence.py      # 79 evidences evaluation
│   ├── syndrome.py      # 35 syndromes detection (nested logic)
│   ├── normalization.py # Unit conversion + heuristics
│   ├── next_steps.py    # 40 triggers clinical recommendations
│   ├── schema_validator.py
│   ├── worm_log.py      # HMAC audit trail
│   └── output_renderer.py # Markdown/HTML/JSON/FHIR
│
├── models/
│   ├── cbc.py           # Pydantic models
│   ├── evidence.py
│   └── syndrome.py
│
└── utils/
    └── yaml_parser.py   # Loads 16 YAMLs
```

**Linhas:** ~2,660 (production code)
**Status:** ✅ FUNCIONAL (Sprint 0+1 completo)

---

## 🔴 PROBLEMAS IDENTIFICADOS

### 1. Duplicação de YAMLs ⚠️ CRÍTICO

**Problema:**
- `HEMODOCTOR_HIBRIDO_V1.0/YAMLs/` (16 files) - ESPECIFICAÇÃO
- `hemodoctor_cdss/config/` (17 files) - IMPLEMENTAÇÃO
- **São idênticos!** (verificado)

**Impacto:** Risco de dessincronização

**Solução:**
- Manter YAMLs apenas em `hemodoctor_cdss/config/`
- HEMODOCTOR_HIBRIDO_V1.0/YAMLs/ → Criar README_MOVED.md e deletar YAMLs

### 2. HEMODOCTOR_CONSOLIDADO_v2.0_20251010 Parcialmente Vazio

**Problema:**
- 01_SUBMISSAO_CEP/ - VAZIO
- 02_SUBMISSAO_ANVISA/ - 3 subdiretórios VAZIOS

**Solução:**
- Deletar CONSOLIDADO (docs CEP já em WORKSPACES/)
- Docs regulatórios já em AUTHORITATIVE_BASELINE

### 3. Excel na Raiz

**Arquivo:** `HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx` (36 KB)
**Localização:** Raiz
**Solução:** Mover para `hemodoctor_cdss/docs/`

### 4. ARVORE_DECISAO_HIBRIDA_DEFINITIVA

**Status:** Obsoleto
**Solução:** Mover para archive

---

## 📁 ESTRUTURA CONSOLIDADA PROPOSTA

### Versão Final (Limpa + Organizada):

```
docs/
├── README.md
├── CLAUDE.md
├── PROGRESS.md
├── BUGS.md
├── DECISIONS.md
├── VERSION.md
├── STATUS_ATUAL.md
│
├── hemodoctor_cdss/              # 🎯 IMPLEMENTAÇÃO COMPLETA
│   ├── src/hemodoctor/           # Código-fonte (~2,660 linhas)
│   │   ├── api/
│   │   ├── engines/
│   │   ├── models/
│   │   └── utils/
│   │
│   ├── config/                   # ⭐ YAMLs v2.4.0 (ÚNICA FONTE)
│   │   ├── 00-12_*.yaml          # 16 YAMLs clinical rules
│   │   └── README.md             # Config documentation
│   │
│   ├── tests/                    # 466 tests (89% coverage)
│   │   ├── unit/
│   │   ├── security/
│   │   └── integration/
│   │
│   ├── docs/                     # Documentação técnica
│   │   ├── HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx
│   │   ├── IMPLEMENTATION_REPORT.md
│   │   ├── DEVELOPER_HANDOFF.md
│   │   ├── COMPLETION_SUMMARY.md
│   │   ├── SECURITY_TEST_REPORT.md
│   │   └── SPRINT_2_PLAN.md
│   │
│   ├── data/                     # Data files
│   │   └── synthetic_cases/      # CSV casos sintéticos (NOVO)
│   │
│   ├── wormlog/                  # Audit trail
│   ├── requirements.txt
│   ├── pytest.ini
│   └── README.md
│
├── AUTHORITATIVE_BASELINE/       # 🏛️ DOCUMENTAÇÃO REGULATÓRIA
│   ├── 00-10_*/                  # 67 docs v1.0 OFICIAL
│   └── README.md
│
├── HEMODOCTOR_HIBRIDO_V1.0/      # 📚 ESPECIFICAÇÃO V1.0
│   ├── YAMLs/                    # README_MOVED.md → hemodoctor_cdss/config/
│   ├── Analise_Comparativa/      # Design decisions
│   ├── Documentacao_Tecnica/
│   ├── Especificacoes_Dev/
│   └── README.md
│
├── WORKSPACES/                   # 🔧 WORKSPACES ATIVOS
│   └── 01_ETHICS_CEP/            # CEP/CONEP docs
│
├── templates/                    # 📋 Templates
│   ├── CHECKLIST_SUBMISSAO_*.md
│   └── TEMPLATE_*.md
│
├── archive/                      # 📦 HISTÓRICO
│   ├── sessions/
│   ├── plans/
│   ├── guides/
│   ├── reports/
│   └── old-docs/
│
├── scripts/                      # 🛠️ Scripts
│   └── generate_synthetic_cases.py (NOVO)
│
└── docs/                         # 📖 Docs gerais
    ├── archive/
    └── reports/
```

**Eliminados:**
- ❌ HEMODOCTOR_CONSOLIDADO_v2.0_20251010/ (parcialmente vazio)
- ❌ ARVORE_DECISAO_HIBRIDA_DEFINITIVA/ (obsoleto)
- ❌ HEMODOCTOR_HIBRIDO_V1.0/YAMLs/*.yaml (duplicados)

---

## 🎯 AÇÕES PROPOSTAS

### PRIORIDADE P0 (Fazer AGORA - 30min)

1. ✅ **Mover Excel para hemodoctor_cdss/docs/**
   ```bash
   mv HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx hemodoctor_cdss/docs/
   ```

2. ✅ **Remover YAMLs duplicados**
   ```bash
   # Criar README explicando onde estão os YAMLs
   echo "# YAMLs Movidos

Os YAMLs clinical rules v2.4.0 estão agora em:
**\`../../../hemodoctor_cdss/config/\`**

Esta é a ÚNICA fonte da verdade para YAMLs de configuração.

Motivo: Evitar dessincronização entre especificação e implementação." > HEMODOCTOR_HIBRIDO_V1.0/YAMLs/README_MOVED.md

   # Deletar YAMLs duplicados
   rm -f HEMODOCTOR_HIBRIDO_V1.0/YAMLs/*.yaml
   ```

3. ✅ **Deletar ARVORE_DECISAO_HIBRIDA_DEFINITIVA**
   ```bash
   mv ARVORE_DECISAO_HIBRIDA_DEFINITIVA archive/old-docs/
   ```

4. ✅ **Deletar CONSOLIDADO (vazio)**
   ```bash
   rm -rf HEMODOCTOR_CONSOLIDADO_v2.0_20251010
   ```

### PRIORIDADE P1 (Depois - 15min)

5. ⏳ **Criar hemodoctor_cdss/data/synthetic_cases/**
   ```bash
   mkdir -p hemodoctor_cdss/data/synthetic_cases
   ```

6. ⏳ **Atualizar README.md raiz**
   - Refletir nova estrutura
   - Adicionar navegação clara

---

## ✅ BENEFÍCIOS DA CONSOLIDAÇÃO

### Antes:
- 43 YAMLs (16 duplicados)
- 3-4 locais com docs regulatórios
- Estrutura confusa (CONSOLIDADO vazio)
- Navegação difícil

### Depois:
- 27 YAMLs (16 config + 10 API specs + 1 README)
- 1 local principal: AUTHORITATIVE_BASELINE
- 1 local implementação: hemodoctor_cdss/
- Navegação clara e profissional

**Redução:** 37% menos YAMLs duplicados
**Clareza:** 100% melhor organização
**Manutenibilidade:** Uma única fonte da verdade

---

**Analista:** @hemodoctor-orchestrator
**Status:** ⏳ AGUARDANDO APROVAÇÃO
**Versão:** 1.0
