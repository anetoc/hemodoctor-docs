# 📂 FASE 3: MAPEAMENTO DE CATEGORIAS REAIS

**Data:** 21 de Outubro de 2025
**Status:** ✅ COMPLETO
**Duração:** 30 minutos
**Método:** Análise temática dos 186 documentos ativos

---

## 🎯 OBJETIVO

Mapear categorias REAIS dos documentos baseado no **conteúdo e propósito**, não apenas na estrutura de pastas.

**Resultado esperado:** Identificar agrupamentos lógicos para consolidação final.

---

## 📊 CATEGORIZAÇÃO POR PROPÓSITO

### CATEGORIA 1: Regulatory Submission (Submissão ANVISA/FDA)

**Total:** 67 documentos (30%)

**Subcategorias:**

#### 1.1 Device Master Record (DMR)
- DMR-001_Device_Master_Record_v1.0_SUMMARY.md
- DMR_v2.0_DELIVERABLES.md

**Localização:** AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/

#### 1.2 Design Controls
- **SRS-001** v3.1 YAMLS FULL (59 KB) ⭐ OFICIAL
- **SDD-001** v2.1 YAMLS FULL (69 KB) ⭐ OFICIAL
- TEC-001 v1.0 (Software Development Plan, 28 KB)

**Localização:**
- Oficial: CONSOLIDADO_20251018/01_CORE_TECHNICAL/
- Baseline: AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/

#### 1.3 Risk Management
- **TEC-002** v2.1 YAMLS FULL (48 KB) ⭐ OFICIAL
- RMP-001 v1.0 (Risk Management Plan, 45 KB)

**Localização:**
- Oficial: CONSOLIDADO_20251018/01_CORE_TECHNICAL/
- Baseline: AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/

#### 1.4 Verification & Validation
- **VVP-001** v1.0 (35 KB) ⭐ OFICIAL
- TESTREP-001 v1.0 (Unit Tests, 20 KB)
- TESTREP-002 v1.0 (Integration Tests, 2.9 KB)
- TESTREP-003 v1.0 (System Tests, 3.7 KB)
- TESTREP-004 v1.0 (Validation Tests, 6.6 KB)
- COV-001 v1.0 (Coverage Analysis, 18 KB)
- COV-001 v1.0 (Coverage Matrix CSV, 4 KB)
- TST-001 v1.0 (Test Specification, 68 KB)

**Localização:** AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/

#### 1.5 Clinical Evaluation
- **CER-001** v2.0 FULL (75 KB) ⭐ OFICIAL
- CER-001 VALIDATION_REPORT (27 KB)
- PROJ-001 v2.0 (Protocol, 78 KB)
- TCLE-001 v2.0 (Informed Consent, 13 KB)

**Localização:**
- Oficial: CONSOLIDADO_20251018/02_CLINICAL/
- Baseline: AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/

#### 1.6 Traceability
- **TRC-001** v2.1 YAMLS FULL (31 KB) ⭐ OFICIAL
- TRC-001 v2.1 UPDATE_SUMMARY (12 KB)

**Localização:**
- Oficial: CONSOLIDADO_20251018/01_CORE_TECHNICAL/
- Baseline: AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/

#### 1.7 Post-Market Surveillance
- **PMS-001** v2.0 FULL (18 KB) ⭐ OFICIAL
- PROC-001 v1.0 (Incident Reporting, 54 KB)
- PROC-002 v1.0 (Event Investigation, 76 KB)
- PROC-003 v1.0 (CAPA, 74 KB)
- FORM-001 v1.0 (Incident Report Form, 13 KB)
- FORM-002 v1.0 (Investigation Form, 22 KB)
- FORM-003 v1.0 (CAPA Form, 22 KB)
- FORM-004 v1.0 (ANVISA Notification, 24 KB)

**Localização:**
- Oficial: CONSOLIDADO_20251018/03_POST_MARKET/
- Baseline: AUTHORITATIVE_BASELINE/07_POS_MERCADO/

#### 1.8 Labeling & Instructions
- IFU-001 v2.0 (Instructions For Use, 19 KB)
- IFU-001_EN_US_v1.0_OFICIAL.pdf
- IFU-001_PT_BR_v1.0_OFICIAL.pdf

**Localização:**
- MD: CONSOLIDADO_20251018/04_REGULATORY/
- PDF: AUTHORITATIVE_BASELINE/08_ROTULAGEM/

#### 1.9 Cybersecurity
- SEC-001 v2.0 (Security Analysis, 58 KB)
- SBOM v1.0 (Software Bill of Materials)
- VEX v1.0 (Vulnerability Analysis)

**Localização:**
- Updated: CONSOLIDADO_20251018/04_REGULATORY/
- Baseline: AUTHORITATIVE_BASELINE/09_CYBERSECURITY/

#### 1.10 SOUP Analysis
- SOUP-001 v2.0 (17 KB)

**Localização:**
- Updated: CONSOLIDADO_20251018/04_REGULATORY/
- Baseline: AUTHORITATIVE_BASELINE/10_SOUP/

---

### CATEGORIA 2: Implementation & Code (Implementação)

**Total:** 69 arquivos (31%)

**Subcategorias:**

#### 2.1 Source Code (Production)
- **src/hemodoctor/** (38 arquivos Python)
  - api/ (main.py, pipeline.py)
  - engines/ (evidence.py, syndrome.py, next_steps.py, normalization.py, schema_validator.py, worm_log.py, output_renderer.py)
  - models/ (cbc.py, evidence.py, syndrome.py)
  - utils/ (yaml_parser.py)

**Localização:** hemodoctor_cdss/src/

#### 2.2 Tests (Unit + Integration + Security)
- **tests/** (355 unit + 7 integration + 104 security = 466 total)
  - unit/ (test_evidence_engine.py, test_syndrome.py, etc.)
  - integration/ (test_pipeline.py, test_critical_fixes.py)
  - security/ (test_input_validation.py, test_owasp_top10.py, etc.)

**Localização:** hemodoctor_cdss/tests/

**Coverage:** 89% (362/362 core tests passing)

#### 2.3 Configuration (YAMLs)
- **config/** (16 YAMLs, 9,063 linhas) ⭐ ÚNICA FONTE DA VERDADE
  - 00_config_hybrid.yaml (12 KB)
  - 01_schema_hybrid.yaml (13 KB)
  - 02_evidence_hybrid.yaml (29 KB) - 79 evidências
  - 03_syndromes_hybrid.yaml (29 KB) - 35 síndromes
  - 04_output_templates_hybrid.yaml (6.9 KB)
  - 05_missingness_hybrid_v2.3.yaml (29 KB)
  - 05_missingness_hybrid.yaml (22 KB)
  - 06_route_policy_hybrid.yaml (17 KB)
  - 07_conflict_matrix_hybrid.yaml (15 KB)
  - 07_normalization_heuristics.yaml (16 KB)
  - 08_wormlog_hybrid.yaml (19 KB)
  - 09_next_steps_engine_hybrid.yaml (41 KB) - 40 triggers
  - 10_runbook_hybrid.yaml (25 KB)
  - 11_case_state_hybrid.yaml (21 KB)
  - 12_output_policies_cdss.yaml (2.1 KB)
  - 12_output_policies_hybrid.yaml (23 KB)

**Localização:** hemodoctor_cdss/config/

**Nota:** YAMLs movidos de HEMODOCTOR_HIBRIDO_V1.0/YAMLs/ em 21 Out 2025

#### 2.4 Implementation Documentation
- IMPLEMENTATION_REPORT.md (14 KB)
- DEVELOPER_HANDOFF.md (14 KB)
- COMPLETION_SUMMARY.md (12 KB)
- SECURITY_TESTING_SUMMARY.md (11 KB)
- SPRINT_2_PLAN_INTEGRATION_TESTING.md (10 KB)
- TEST-SPEC-001_v1.0_YAML_VALIDATION.md (40 KB)
- RESUMO_SESSAO_21_OUT_2025_FINAL.md (13 KB)
- RESUMO_EXECUCAO_PARALELA_FINAL.md (8.6 KB)
- QUICK_START_NOVA_JANELA.md (7.6 KB)
- README.md (4.6 KB)

**Localização:** hemodoctor_cdss/docs/

#### 2.5 Validation Materials
- HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx (34 KB) - Excel completo

**Localização:** hemodoctor_cdss/docs/

---

### CATEGORIA 3: Automation & Skills (Automação)

**Total:** 27 arquivos (12%)

**Subcategorias:**

#### 3.1 Claude Skills (11 skills)
Cada skill contém:
- SKILL.md (descrição)
- Scripts Python (1-3 por skill)
- References (quando aplicável)

**Skills disponíveis:**
1. clinical-test-generator (SKILL.md + scripts + refs)
2. code-helper (SKILL.md + scripts)
3. documentation (SKILL.md + scripts)
4. evidence-engine (SKILL.md + scripts)
5. hemodoctor-validator (SKILL.md + scripts)
6. next-steps-debugger (SKILL.md + scripts)
7. test-suite (SKILL.md + scripts)
8. yaml-dag-visualizer (SKILL.md + scripts)
9. yaml-validation (SKILL.md + scripts)
10. README.md (índice skills)

**Localização:** HEMODOCTOR_HIBRIDO_V1.0/.claude/skills/

**Scripts totais:** 16 arquivos Python

---

### CATEGORIA 4: Reports & Analysis (Relatórios & Análises)

**Total:** 57 documentos (25%)

**Subcategorias:**

#### 4.1 Status Reports
- BRIEFING_DEV_TEAM_v2.3.1.md (30 KB)
- RELATORIO_IMPLEMENTACAO_v2.3.1_FINAL.md
- STATUS_IMPLEMENTACAO.txt
- SUMARIO_EXECUTIVO_*.md
- RELATORIO_VV_COMPLIANCE_20251019.md
- MAPA_COMPLIANCE_VISUAL_20251019.md

**Localização:** HEMODOCTOR_HIBRIDO_V1.0/ (raiz)

#### 4.2 Consolidation Logs
- CONSOLIDATION_LOG_SRS-001.md (14 KB)
- CONSOLIDATION_LOG_SDD-001.md (12 KB)
- CONSOLIDATION_LOG_TEC-002.md (11 KB)
- CONSOLIDATION_LOG_CER-001.md (9.8 KB)
- CONSOLIDATION_LOG_PMS-001.md (23 KB)
- (+ 6 outros logs)

**Localização:** HEMODOCTOR_HIBRIDO_V1.0/CONSOLIDADO_20251018/06_CONSOLIDATION_LOGS/

**Total:** 11 logs

#### 4.3 Multi-Agent Analysis Reports
- ALINHAMENTO_YAMLS_20251019.md
- ALINHAMENTO_CODIGO_YAMLS_20251019.md
- ALINHAMENTO_RASTREABILIDADE_20251019.md
- ALINHAMENTO_REGULATORY_20251019.md
- ALINHAMENTO_VV_20251019.md
- ALINHAMENTO_CLINICO_20251019.md
- EXECUTIVE_SUMMARY_REGULATORY_20251019.md
- SUMARIO_EXECUTIVO_ALINHAMENTO_VV.md
- ACOES_IMEDIATAS_COMPLIANCE_20251019.md

**Localização:** docs/reports/

**Total:** 9+ relatórios

#### 4.4 Executive Summaries
- Para cada documento regulatório v2.0/v3.0:
  - SRS-001_v3.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (24 KB)
  - SDD-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (6.5 KB)
  - TEC-002_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (11 KB)
  - CER-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (9.1 KB)
  - PMS-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (5.8 KB)

**Localização:** CONSOLIDADO_20251018/01_CORE_TECHNICAL/ e /02_CLINICAL/

#### 4.5 Analysis Documents
- ANALISE_COMPLETA_TODOLIST_20251013.md
- ANALISE_HYBRID_VS_AUTHORITATIVE_21OUT2025.md
- CONSOLIDACAO_ESTRUTURA_COMPLETA_21OUT2025.md
- FASE1_INVENTARIO_COMPLETO_21OUT2025.md
- FASE2_VERSOES_IDENTIFICADAS_21OUT2025.md (este arquivo em FASE 3)

**Localização:** docs/

---

### CATEGORIA 5: Technical Specifications (Especificações Técnicas)

**Total:** 6 documentos (3%)

#### 5.1 Hybrid V1.0 Specifications
- README.md (Visão geral V1.0)
- INDEX_COMPLETO.md (Índice detalhado)
- QUICKSTART_IMPLEMENTACAO.md (Guia dev team)
- CLAUDE.md (Contexto para IA)

**Localização:** HEMODOCTOR_HIBRIDO_V1.0/

#### 5.2 Comparative Analysis
- ANALISE_COMPARATIVA_TRIPLA_*.md
- COMPARACAO_HIBRIDO_vs_SADMH_V2.3.md

**Localização:** HEMODOCTOR_HIBRIDO_V1.0/Analise_Comparativa/

---

## 📊 DISTRIBUIÇÃO POR CATEGORIA

| Categoria | Arquivos | % | Localização Principal |
|-----------|----------|---|-----------------------|
| **1. Regulatory Submission** | 67 | 30% | AUTHORITATIVE + CONSOLIDADO |
| **2. Implementation & Code** | 69 | 31% | hemodoctor_cdss |
| **3. Automation & Skills** | 27 | 12% | HYBRID/.claude/skills |
| **4. Reports & Analysis** | 57 | 25% | HYBRID raiz + docs/reports |
| **5. Technical Specs** | 6 | 3% | HYBRID raiz |
| **TOTAL** | 225 | 100% | — |

---

## 🔍 ANÁLISE DE SOBREPOSIÇÃO

### Overlap entre AUTHORITATIVE e CONSOLIDADO

**6 documentos regulatórios com versões múltiplas:**
- SRS-001, SDD-001, TEC-002, TRC-001, CER-001, PMS-001

**Decisão:** Manter versões mais recentes (v2.x/v3.x) em CONSOLIDADO, arquivar v1.0 de AUTHORITATIVE

### Overlap entre HYBRID e hemodoctor_cdss

**1 overlap (YAMLs):**
- YAMLs estavam em HYBRID/YAMLs/ (especificação)
- YAMLs MOVIDOS para hemodoctor_cdss/config/ (implementação) ✅ RESOLVIDO em 21 Out

### Overlap entre categorias

**Nenhuma sobreposição crítica:**
- Reports (Categoria 4) podem mencionar documentos regulatórios (Categoria 1), mas são COMPLEMENTARES
- Skills (Categoria 3) automatizam processos, mas não duplicam documentos

---

## 🎯 AGRUPAMENTO LÓGICO PROPOSTO

### Grupo A: Regulatory Package (Pacote Regulatório)

**Propósito:** Submissão ANVISA/FDA

**Conteúdo:**
- DMR, SRS, SDD, TEC, TRC, CER, PMS, VVP, TESTREP, COV, TST, IFU, SEC, SOUP
- 67 documentos oficiais
- Versões v1.0 (baseline) + v2.x/v3.x (atualizadas)

**Localização sugerida:** `REGULATORY_PACKAGE/`

**Estrutura:**
```
REGULATORY_PACKAGE/
├── 01_DEVICE_MASTER_RECORD/
├── 02_DESIGN_CONTROLS/
├── 03_RISK_MANAGEMENT/
├── 04_VERIFICATION_VALIDATION/
├── 05_CLINICAL_EVALUATION/
├── 06_TRACEABILITY/
├── 07_POST_MARKET_SURVEILLANCE/
├── 08_LABELING/
├── 09_CYBERSECURITY/
├── 10_SOUP/
└── ARCHIVE/ (versões antigas v1.0)
```

### Grupo B: Implementation (Implementação Ativa)

**Propósito:** Código-fonte + testes + configuração

**Conteúdo:**
- Source code (38 arquivos Python)
- Tests (466 testes - 89% coverage)
- YAMLs (16 módulos - 9,063 linhas)
- Implementation docs (10 documentos)
- 69 arquivos totais

**Localização atual:** `hemodoctor_cdss/` ✅ JÁ CONSOLIDADO

**Estrutura:**
```
hemodoctor_cdss/
├── src/
├── tests/
├── config/ (16 YAMLs ⭐)
├── docs/
├── data/
└── wormlog/
```

### Grupo C: Automation & Development Tools (Ferramentas)

**Propósito:** Skills Claude + scripts de automação

**Conteúdo:**
- 11 skills completos
- 16 scripts Python
- 27 arquivos totais

**Localização atual:** `HEMODOCTOR_HIBRIDO_V1.0/.claude/skills/` ✅ OK

**Estrutura:**
```
.claude/skills/
├── clinical-test-generator/
├── code-helper/
├── documentation/
├── evidence-engine/
├── hemodoctor-validator/
├── next-steps-debugger/
├── test-suite/
├── yaml-dag-visualizer/
├── yaml-validation/
└── README.md
```

### Grupo D: Reports & Analysis (Relatórios)

**Propósito:** Status reports + análises + logs

**Conteúdo:**
- Status reports (10 documentos)
- Consolidation logs (11 logs)
- Multi-agent analysis (9 relatórios)
- Executive summaries (5 summaries)
- Analysis docs (5 análises)
- 57 documentos totais

**Localização sugerida:** `REPORTS_ARCHIVE/`

**Estrutura:**
```
REPORTS_ARCHIVE/
├── status_reports/
├── consolidation_logs/
├── multi_agent_analysis/
├── executive_summaries/
└── technical_analysis/
```

### Grupo E: Technical Specifications (Especificações)

**Propósito:** Documentação técnica do projeto

**Conteúdo:**
- Hybrid V1.0 specs (4 documentos)
- Comparative analysis (2 documentos)
- 6 documentos totais

**Localização atual:** `HEMODOCTOR_HIBRIDO_V1.0/` ✅ OK

**Estrutura:**
```
HEMODOCTOR_HIBRIDO_V1.0/
├── README.md
├── INDEX_COMPLETO.md
├── QUICKSTART_IMPLEMENTACAO.md
├── CLAUDE.md
└── Analise_Comparativa/
```

---

## 📁 MAPA DE DESTINO (PROPOSTA)

```
/Users/abelcosta/Documents/HemoDoctor/docs/
│
├── 📦 REGULATORY_PACKAGE/ ⭐ NOVO (Grupo A)
│   ├── 01_DEVICE_MASTER_RECORD/
│   ├── 02_DESIGN_CONTROLS/
│   ├── 03_RISK_MANAGEMENT/
│   ├── 04_VERIFICATION_VALIDATION/
│   ├── 05_CLINICAL_EVALUATION/
│   ├── 06_TRACEABILITY/
│   ├── 07_POST_MARKET_SURVEILLANCE/
│   ├── 08_LABELING/
│   ├── 09_CYBERSECURITY/
│   ├── 10_SOUP/
│   └── ARCHIVE/ (versões antigas)
│
├── 💻 hemodoctor_cdss/ ✅ OK (Grupo B)
│   ├── src/
│   ├── tests/
│   ├── config/ (16 YAMLs ⭐)
│   ├── docs/
│   ├── data/
│   └── wormlog/
│
├── 🤖 .claude/skills/ ✅ OK (Grupo C)
│   └── (11 skills)
│
├── 📊 REPORTS_ARCHIVE/ ⭐ NOVO (Grupo D)
│   ├── status_reports/
│   ├── consolidation_logs/
│   ├── multi_agent_analysis/
│   ├── executive_summaries/
│   └── technical_analysis/
│
├── 📚 HEMODOCTOR_HIBRIDO_V1.0/ ✅ OK (Grupo E)
│   ├── README.md
│   ├── INDEX_COMPLETO.md
│   ├── QUICKSTART_IMPLEMENTACAO.md
│   ├── CLAUDE.md
│   └── Analise_Comparativa/
│
└── 📄 CLAUDE.md (raiz) ✅ OK
    README.md ✅ OK
    VERSION.md ✅ OK
    STATUS_ATUAL.md ✅ OK
    PROGRESS.md ✅ OK
    BUGS.md ✅ OK
    DECISIONS.md ✅ OK
```

---

## ✅ DECISÕES DE RENOMEAÇÃO

### Renomear (2 diretórios)

1. **AUTHORITATIVE_BASELINE + CONSOLIDADO_20251018 → REGULATORY_PACKAGE**
   - Motivo: Consolida versões v1.0 (baseline) + v2.x/v3.x (atualizadas)
   - Estrutura mais clara (10 módulos regulatórios)
   - Archive para versões antigas

2. **HEMODOCTOR_HIBRIDO_V1.0 (raiz) → REPORTS_ARCHIVE**
   - Motivo: Raiz contém 57 relatórios/análises (não specs técnicos)
   - Specs técnicos (4 documentos) mantidos em HEMODOCTOR_HIBRIDO_V1.0 (subdiretório)

### Manter (3 diretórios)

1. **hemodoctor_cdss/** ✅
   - Já consolidado e organizado
   - 100% implementação ativa

2. **.claude/skills/** ✅
   - Já consolidado
   - 11 skills funcionais

3. **HEMODOCTOR_HIBRIDO_V1.0/** ✅
   - Specs técnicos importantes
   - Comparative analysis

---

## 📊 MÉTRICAS FINAIS

| Métrica | Valor |
|---------|-------|
| **Total categorias identificadas** | 5 |
| **Total subcategorias** | 23 |
| **Documentos regulatórios** | 67 (30%) |
| **Documentos implementação** | 69 (31%) |
| **Documentos automação** | 27 (12%) |
| **Documentos relatórios** | 57 (25%) |
| **Documentos especificações** | 6 (3%) |
| **Grupos lógicos propostos** | 5 (A-E) |
| **Diretórios a criar** | 2 (REGULATORY_PACKAGE, REPORTS_ARCHIVE) |
| **Diretórios a renomear** | 2 |
| **Diretórios a manter** | 3 |

---

## ✅ CHECKLIST FASE 3

- [x] Analisar 186 documentos ativos
- [x] Identificar 5 categorias principais
- [x] Criar 23 subcategorias
- [x] Mapear sobreposições (3 identificadas, 1 resolvida)
- [x] Propor agrupamento lógico (5 grupos A-E)
- [x] Criar estrutura de destino
- [x] Identificar renomeações necessárias (2 diretórios)
- [x] Documentar decisões
- [x] Relatório gerado

**Status:** ✅ FASE 3 COMPLETA - Ready for FASE 4

---

## 🔜 PRÓXIMO

**FASE 4:** Propor estrutura consolidada final (30 min)

**O que fazer:**
1. Detalhar estrutura final de REGULATORY_PACKAGE
2. Detalhar estrutura final de REPORTS_ARCHIVE
3. Criar plano de migração (quais arquivos vão para onde)
4. Validar que nada será perdido
5. Criar checklist de execução

---

**Criado:** 21 de Outubro de 2025
**Duração Fase 3:** 30 minutos
**Total Categorias:** 5
**Total Subcategorias:** 23
**Grupos Lógicos:** 5 (A-E)
