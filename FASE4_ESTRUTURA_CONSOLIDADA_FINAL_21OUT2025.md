# 🏗️ FASE 4: ESTRUTURA CONSOLIDADA FINAL

**Data:** 21 de Outubro de 2025
**Status:** ✅ COMPLETO
**Duração:** 30 minutos
**Método:** Proposta de estrutura final + plano de migração detalhado

---

## 🎯 OBJETIVO

Criar **estrutura final consolidada** do repositório HemoDoctor, eliminando duplicações e organizando 225 arquivos de forma lógica.

**Princípios:**
1. ✅ **Nenhum arquivo perdido** (100% rastreabilidade)
2. ✅ **Versões oficiais** em local único
3. ✅ **Versões antigas** arquivadas (não deletadas)
4. ✅ **Estrutura lógica** (não apenas histórica)
5. ✅ **Git-tracked** (todas as mudanças rastreadas)

---

## 📁 ESTRUTURA FINAL PROPOSTA

```
/Users/abelcosta/Documents/HemoDoctor/docs/
│
├── 📄 CLAUDE.md ✅ (raiz - contexto geral)
├── 📄 README.md ✅ (raiz - visão geral)
├── 📄 VERSION.md ✅ (raiz - controle versões)
├── 📄 STATUS_ATUAL.md ✅ (raiz - status tempo real)
├── 📄 PROGRESS.md ✅ (raiz - histórico progresso)
├── 📄 BUGS.md ✅ (raiz - bugs registrados)
├── 📄 DECISIONS.md ✅ (raiz - ADRs)
│
├── 📦 REGULATORY_PACKAGE/ ⭐ NOVO (67 docs)
│   ├── 00_INDICE_GERAL/
│   │   ├── README.md
│   │   ├── SUBMISSION_READY_STATUS.md
│   │   ├── CHECKSUMS_SHA256.txt
│   │   └── MAPEAMENTO_FONTE_DESTINO.csv
│   │
│   ├── 01_DEVICE_MASTER_RECORD/
│   │   ├── DMR-001_Device_Master_Record_v1.0_SUMMARY.md
│   │   └── DMR_v2.0_DELIVERABLES.md
│   │
│   ├── 02_DESIGN_CONTROLS/
│   │   ├── SRS/
│   │   │   └── SRS-001_v3.1_OFICIAL_YAMLS_FULL.md ⭐ OFICIAL
│   │   ├── SDD/
│   │   │   └── SDD-001_v2.1_OFICIAL_YAMLS_FULL.md ⭐ OFICIAL
│   │   └── TEC/
│   │       └── TEC-001_Software_Development_Plan_v1.0_OFICIAL.md
│   │
│   ├── 03_RISK_MANAGEMENT/
│   │   ├── RMP/
│   │   │   └── RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md
│   │   └── TEC/
│   │       └── TEC-002_v2.1_OFICIAL_YAMLS_FULL.md ⭐ OFICIAL
│   │
│   ├── 04_VERIFICATION_VALIDATION/
│   │   ├── VVP/
│   │   │   └── VVP-001_Verification_Validation_Plan_v1.0_OFICIAL.md
│   │   ├── TestReports/
│   │   │   ├── TESTREP-001_Unit_Tests_Report_v1.0_OFICIAL.md
│   │   │   ├── TESTREP-002_Integration_Tests_Report_v1.0_OFICIAL.md
│   │   │   ├── TESTREP-003_System_Tests_Report_v1.0_OFICIAL.md
│   │   │   └── TESTREP-004_Validation_Tests_Report_v1.0_OFICIAL.md
│   │   ├── Cobertura/
│   │   │   ├── COV-001_Test_Coverage_Analysis_v1.0_OFICIAL.md
│   │   │   └── COV-001_Coverage_Matrix_v1.0_OFICIAL.csv
│   │   └── TST/
│   │       └── TST-001_Test_Specification_v1.0_OFICIAL.md
│   │
│   ├── 05_CLINICAL_EVALUATION/
│   │   ├── CER/
│   │   │   └── CER-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md ⭐ OFICIAL
│   │   ├── Protocol/
│   │   │   └── PROJ-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md
│   │   └── Consent/
│   │       └── TCLE-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md
│   │
│   ├── 06_TRACEABILITY/
│   │   └── TRC/
│   │       └── TRC-001_v2.1_OFICIAL_YAMLS_FULL.md ⭐ OFICIAL
│   │
│   ├── 07_POST_MARKET_SURVEILLANCE/
│   │   ├── PMS/
│   │   │   └── PMS-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md ⭐ OFICIAL
│   │   ├── Procedures/
│   │   │   ├── PROC-001_Incident_Reporting_v1.0_OFICIAL.md
│   │   │   ├── PROC-002_Event_Investigation_v1.0_OFICIAL.md
│   │   │   └── PROC-003_CAPA_v1.0_OFICIAL.md
│   │   └── Forms/
│   │       ├── FORM-001_Incident_Report_v1.0_OFICIAL.md
│   │       ├── FORM-002_Investigation_v1.0_OFICIAL.md
│   │       ├── FORM-003_CAPA_v1.0_OFICIAL.md
│   │       └── FORM-004_ANVISA_Notification_v1.0_OFICIAL.md
│   │
│   ├── 08_LABELING/
│   │   ├── IFU/
│   │   │   ├── IFU-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md
│   │   │   ├── IFU-001_EN_US_v1.0_OFICIAL.pdf
│   │   │   └── IFU-001_PT_BR_v1.0_OFICIAL.pdf
│   │   └── Labels/
│   │       └── (etiquetas)
│   │
│   ├── 09_CYBERSECURITY/
│   │   ├── SEC/
│   │   │   └── SEC-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md
│   │   ├── SBOM/
│   │   │   └── SBOM_v1.0_OFICIAL.md
│   │   └── VEX/
│   │       └── VEX_v1.0_OFICIAL.md
│   │
│   ├── 10_SOUP/
│   │   └── SOUP-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md
│   │
│   └── ARCHIVE/ ⭐ NOVO (14 docs obsoletos)
│       ├── baseline_v1.0/
│       │   ├── SRS-001_Software_Requirements_v1.0_OFICIAL.md
│       │   ├── SDD-001_Software_Design_v1.0_OFICIAL.md
│       │   ├── TEC-002_Risk_Management_File_v1.0_OFICIAL.md
│       │   ├── TRC-001_Traceability_Matrix_v1.0_OFICIAL.csv
│       │   ├── CER-001_Clinical_Evaluation_Report_v1.0_OFICIAL.md
│       │   └── PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md
│       └── intermediate/
│           ├── SRS-001_v3.0_OFICIAL_CONSOLIDADO_FULL.md
│           ├── SRS-001_v3.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│           ├── SDD-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md
│           ├── SDD-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│           ├── TEC-002_v2.0_OFICIAL_CONSOLIDADO_FULL.md
│           ├── TEC-002_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│           ├── CER-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│           └── PMS-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│
├── 💻 hemodoctor_cdss/ ✅ OK (69 docs)
│   ├── src/
│   │   └── hemodoctor/
│   │       ├── api/ (main.py, pipeline.py)
│   │       ├── engines/ (8 engines)
│   │       ├── models/ (cbc.py, evidence.py, syndrome.py)
│   │       └── utils/ (yaml_parser.py)
│   ├── tests/
│   │   ├── unit/ (355 tests)
│   │   ├── integration/ (7 tests)
│   │   └── security/ (104 tests)
│   ├── config/ ⭐ 16 YAMLs (9,063 linhas)
│   │   ├── 00_config_hybrid.yaml
│   │   ├── 01_schema_hybrid.yaml
│   │   ├── 02_evidence_hybrid.yaml (79 evidências)
│   │   ├── 03_syndromes_hybrid.yaml (35 síndromes)
│   │   ├── 04_output_templates_hybrid.yaml
│   │   ├── 05_missingness_hybrid_v2.3.yaml
│   │   ├── 05_missingness_hybrid.yaml
│   │   ├── 06_route_policy_hybrid.yaml
│   │   ├── 07_conflict_matrix_hybrid.yaml
│   │   ├── 07_normalization_heuristics.yaml
│   │   ├── 08_wormlog_hybrid.yaml
│   │   ├── 09_next_steps_engine_hybrid.yaml (40 triggers)
│   │   ├── 10_runbook_hybrid.yaml
│   │   ├── 11_case_state_hybrid.yaml
│   │   ├── 12_output_policies_cdss.yaml
│   │   └── 12_output_policies_hybrid.yaml
│   ├── docs/
│   │   ├── IMPLEMENTATION_REPORT.md
│   │   ├── DEVELOPER_HANDOFF.md
│   │   ├── COMPLETION_SUMMARY.md
│   │   ├── SECURITY_TESTING_SUMMARY.md
│   │   ├── SPRINT_2_PLAN_INTEGRATION_TESTING.md
│   │   ├── TEST-SPEC-001_v1.0_YAML_VALIDATION.md
│   │   ├── RESUMO_SESSAO_21_OUT_2025_FINAL.md
│   │   ├── RESUMO_EXECUCAO_PARALELA_FINAL.md
│   │   ├── QUICK_START_NOVA_JANELA.md
│   │   ├── HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx
│   │   └── README.md
│   ├── data/
│   ├── wormlog/
│   ├── requirements.txt
│   └── pytest.ini
│
├── 🤖 .claude/ ✅ OK
│   └── skills/ (11 skills, 27 arquivos)
│       ├── clinical-test-generator/
│       ├── code-helper/
│       ├── documentation/
│       ├── evidence-engine/
│       ├── hemodoctor-validator/
│       ├── next-steps-debugger/
│       ├── test-suite/
│       ├── yaml-dag-visualizer/
│       ├── yaml-validation/
│       └── README.md
│
├── 📊 reports/ ⭐ RENOMEADO (57 docs)
│   ├── status/
│   │   ├── BRIEFING_DEV_TEAM_v2.3.1.md
│   │   ├── RELATORIO_IMPLEMENTACAO_v2.3.1_FINAL.md
│   │   ├── STATUS_IMPLEMENTACAO.txt
│   │   ├── SUMARIO_EXECUTIVO_*.md (vários)
│   │   ├── RELATORIO_VV_COMPLIANCE_20251019.md
│   │   └── MAPA_COMPLIANCE_VISUAL_20251019.md
│   ├── consolidation_logs/
│   │   ├── CONSOLIDATION_LOG_SRS-001.md
│   │   ├── CONSOLIDATION_LOG_SDD-001.md
│   │   ├── CONSOLIDATION_LOG_TEC-002.md
│   │   ├── CONSOLIDATION_LOG_CER-001.md
│   │   ├── CONSOLIDATION_LOG_PMS-001.md
│   │   └── (+ 6 outros logs)
│   ├── multi_agent_analysis/
│   │   ├── ALINHAMENTO_YAMLS_20251019.md
│   │   ├── ALINHAMENTO_CODIGO_YAMLS_20251019.md
│   │   ├── ALINHAMENTO_RASTREABILIDADE_20251019.md
│   │   ├── ALINHAMENTO_REGULATORY_20251019.md
│   │   ├── ALINHAMENTO_VV_20251019.md
│   │   ├── ALINHAMENTO_CLINICO_20251019.md
│   │   ├── EXECUTIVE_SUMMARY_REGULATORY_20251019.md
│   │   ├── SUMARIO_EXECUTIVO_ALINHAMENTO_VV.md
│   │   └── ACOES_IMEDIATAS_COMPLIANCE_20251019.md
│   ├── executive_summaries/
│   │   ├── SRS-001_v3.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│   │   ├── SDD-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│   │   ├── TEC-002_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│   │   ├── CER-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│   │   └── PMS-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md
│   └── technical_analysis/
│       ├── ANALISE_COMPLETA_TODOLIST_20251013.md
│       ├── ANALISE_HYBRID_VS_AUTHORITATIVE_21OUT2025.md
│       ├── CONSOLIDACAO_ESTRUTURA_COMPLETA_21OUT2025.md
│       ├── FASE1_INVENTARIO_COMPLETO_21OUT2025.md
│       ├── FASE2_VERSOES_IDENTIFICADAS_21OUT2025.md
│       └── FASE3_MAPEAMENTO_CATEGORIAS_21OUT2025.md
│
├── 📚 specifications/ ⭐ RENOMEADO (6 docs)
│   ├── README.md (Visão geral Hybrid V1.0)
│   ├── INDEX_COMPLETO.md (Índice detalhado)
│   ├── QUICKSTART_IMPLEMENTACAO.md (Guia dev team)
│   ├── CLAUDE.md (Contexto para IA)
│   └── comparative_analysis/
│       ├── ANALISE_COMPARATIVA_TRIPLA_*.md
│       └── COMPARACAO_HIBRIDO_vs_SADMH_V2.3.md
│
└── archive/ ⭐ NOVO (para backups futuros)
    └── (vazio inicialmente)
```

---

## 🔀 PLANO DE MIGRAÇÃO DETALHADO

### OPERAÇÃO 1: Criar Estrutura Base

```bash
# Criar diretórios principais
mkdir -p REGULATORY_PACKAGE/{00_INDICE_GERAL,01_DEVICE_MASTER_RECORD,02_DESIGN_CONTROLS/{SRS,SDD,TEC},03_RISK_MANAGEMENT/{RMP,TEC},04_VERIFICATION_VALIDATION/{VVP,TestReports,Cobertura,TST},05_CLINICAL_EVALUATION/{CER,Protocol,Consent},06_TRACEABILITY/TRC,07_POST_MARKET_SURVEILLANCE/{PMS,Procedures,Forms},08_LABELING/{IFU,Labels},09_CYBERSECURITY/{SEC,SBOM,VEX},10_SOUP,ARCHIVE/{baseline_v1.0,intermediate}}

mkdir -p reports/{status,consolidation_logs,multi_agent_analysis,executive_summaries,technical_analysis}

mkdir -p specifications/comparative_analysis

mkdir -p archive
```

**Tempo estimado:** 1 minuto

---

### OPERAÇÃO 2: Migrar Documentos Regulatórios Oficiais (6 docs)

**De:** `HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/`
**Para:** `REGULATORY_PACKAGE/`

```bash
# SRS-001 v3.1 (oficial)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/SRS-001_v3.1_OFICIAL_YAMLS_FULL.md" "REGULATORY_PACKAGE/02_DESIGN_CONTROLS/SRS/"

# SDD-001 v2.1 (oficial)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/SDD-001_v2.1_OFICIAL_YAMLS_FULL.md" "REGULATORY_PACKAGE/02_DESIGN_CONTROLS/SDD/"

# TEC-002 v2.1 (oficial)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/TEC-002_v2.1_OFICIAL_YAMLS_FULL.md" "REGULATORY_PACKAGE/03_RISK_MANAGEMENT/TEC/"

# TRC-001 v2.1 (oficial)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/TRC-001_v2.1_OFICIAL_YAMLS_FULL.md" "REGULATORY_PACKAGE/06_TRACEABILITY/TRC/"

# CER-001 v2.0 (oficial)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/02_CLINICAL/CER-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" "REGULATORY_PACKAGE/05_CLINICAL_EVALUATION/CER/"

# PMS-001 v2.0 (oficial)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/03_POST_MARKET/PMS-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" "REGULATORY_PACKAGE/07_POST_MARKET_SURVEILLANCE/PMS/"
```

**Tempo estimado:** 5 minutos

---

### OPERAÇÃO 3: Migrar Documentos AUTHORITATIVE Únicos (55 docs)

**De:** `AUTHORITATIVE_BASELINE/`
**Para:** `REGULATORY_PACKAGE/`

```bash
# 00_INDICE_GERAL (11 arquivos)
cp AUTHORITATIVE_BASELINE/00_INDICE_GERAL/* REGULATORY_PACKAGE/00_INDICE_GERAL/

# 01_REGULATORIO/DMR (2 arquivos)
cp AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/* REGULATORY_PACKAGE/01_DEVICE_MASTER_RECORD/

# 02_CONTROLES_DESIGN/TEC (1 arquivo único - TEC-001)
cp "AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/TEC/TEC-001_Software_Development_Plan_v1.0_OFICIAL.md" REGULATORY_PACKAGE/02_DESIGN_CONTROLS/TEC/

# 03_GESTAO_RISCO/RMP (1 arquivo)
cp "AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/RMP/RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md" REGULATORY_PACKAGE/03_RISK_MANAGEMENT/RMP/

# 04_VERIFICACAO_VALIDACAO (8 arquivos)
cp AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/VVP/* REGULATORY_PACKAGE/04_VERIFICATION_VALIDATION/VVP/
cp AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TestReports/* REGULATORY_PACKAGE/04_VERIFICATION_VALIDATION/TestReports/
cp AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/Cobertura/* REGULATORY_PACKAGE/04_VERIFICATION_VALIDATION/Cobertura/
cp AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TST/* REGULATORY_PACKAGE/04_VERIFICATION_VALIDATION/TST/

# 07_POS_MERCADO (7 arquivos - PROC + FORM)
cp AUTHORITATIVE_BASELINE/07_POS_MERCADO/Procedures/* REGULATORY_PACKAGE/07_POST_MARKET_SURVEILLANCE/Procedures/
cp AUTHORITATIVE_BASELINE/07_POS_MERCADO/Forms/* REGULATORY_PACKAGE/07_POST_MARKET_SURVEILLANCE/Forms/

# 08_ROTULAGEM (2 PDFs)
cp AUTHORITATIVE_BASELINE/08_ROTULAGEM/IFU/* REGULATORY_PACKAGE/08_LABELING/IFU/

# 09_CYBERSECURITY (3 arquivos)
cp AUTHORITATIVE_BASELINE/09_CYBERSECURITY/SBOM/* REGULATORY_PACKAGE/09_CYBERSECURITY/SBOM/
cp AUTHORITATIVE_BASELINE/09_CYBERSECURITY/VEX/* REGULATORY_PACKAGE/09_CYBERSECURITY/VEX/
```

**Tempo estimado:** 10 minutos

---

### OPERAÇÃO 4: Migrar Documentos CONSOLIDADO Únicos (13 docs)

**De:** `HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/`
**Para:** `REGULATORY_PACKAGE/`

```bash
# 02_CLINICAL (2 docs)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/02_CLINICAL/PROJ-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/05_CLINICAL_EVALUATION/Protocol/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/02_CLINICAL/TCLE-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/05_CLINICAL_EVALUATION/Consent/

# 04_REGULATORY (3 docs)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/04_REGULATORY/SEC-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/09_CYBERSECURITY/SEC/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/04_REGULATORY/IFU-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/08_LABELING/IFU/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/04_REGULATORY/SOUP-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/10_SOUP/
```

**Tempo estimado:** 5 minutos

---

### OPERAÇÃO 5: Arquivar Versões Obsoletas (14 docs)

**De:** `AUTHORITATIVE_BASELINE/` + `CONSOLIDADO_20251018/`
**Para:** `REGULATORY_PACKAGE/ARCHIVE/`

```bash
# Baseline v1.0 (6 docs)
cp "AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_Software_Requirements_v1.0_OFICIAL.md" REGULATORY_PACKAGE/ARCHIVE/baseline_v1.0/
cp "AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD/SDD-001_Software_Design_v1.0_OFICIAL.md" REGULATORY_PACKAGE/ARCHIVE/baseline_v1.0/
cp "AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/RMP/TEC-002_Risk_Management_File_v1.0_OFICIAL.md" REGULATORY_PACKAGE/ARCHIVE/baseline_v1.0/
cp "AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v1.0_OFICIAL.csv" REGULATORY_PACKAGE/ARCHIVE/baseline_v1.0/
cp "AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER/CER-001_Clinical_Evaluation_Report_v1.0_OFICIAL.md" REGULATORY_PACKAGE/ARCHIVE/baseline_v1.0/
cp "AUTHORITATIVE_BASELINE/07_POS_MERCADO/PMS/PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md" REGULATORY_PACKAGE/ARCHIVE/baseline_v1.0/

# Intermediate versions (8 docs)
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/SRS-001_v3.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/SRS-001_v3.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/SDD-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/SDD-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/TEC-002_v2.0_OFICIAL_CONSOLIDADO_FULL.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL/TEC-002_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/02_CLINICAL/CER-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
cp "HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/03_POST_MARKET/PMS-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md" REGULATORY_PACKAGE/ARCHIVE/intermediate/
```

**Tempo estimado:** 5 minutos

---

### OPERAÇÃO 6: Reorganizar Reports (57 docs)

**De:** `HEMODOCTOR_HIBRIDO_V1.0/` (raiz) + `CONSOLIDADO_20251018/06_CONSOLIDATION_LOGS/`
**Para:** `reports/`

```bash
# Status reports (~10 arquivos da raiz HYBRID)
mv HEMODOCTOR_HIBRIDO_V1.0/BRIEFING_DEV_TEAM_v2.3.1.md reports/status/
mv HEMODOCTOR_HIBRIDO_V1.0/RELATORIO_IMPLEMENTACAO_v2.3.1_FINAL.md reports/status/
mv HEMODOCTOR_HIBRIDO_V1.0/STATUS_IMPLEMENTACAO.txt reports/status/
mv HEMODOCTOR_HIBRIDO_V1.0/SUMARIO_EXECUTIVO_*.md reports/status/
mv HEMODOCTOR_HIBRIDO_V1.0/RELATORIO_VV_COMPLIANCE_20251019.md reports/status/
mv HEMODOCTOR_HIBRIDO_V1.0/MAPA_COMPLIANCE_VISUAL_20251019.md reports/status/

# Consolidation logs (11 arquivos)
mv HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/06_CONSOLIDATION_LOGS/* reports/consolidation_logs/

# Multi-agent analysis (já está em docs/reports/)
# Não precisa mover

# Executive summaries (5 arquivos)
# Mover para reports/executive_summaries/ (já foram para ARCHIVE em OPERAÇÃO 5)
# Nenhuma ação necessária (ficam em ARCHIVE)

# Technical analysis (6 arquivos - este FASE + anteriores)
mv ANALISE_COMPLETA_TODOLIST_20251013.md reports/technical_analysis/
mv ANALISE_HYBRID_VS_AUTHORITATIVE_21OUT2025.md reports/technical_analysis/
mv CONSOLIDACAO_ESTRUTURA_COMPLETA_21OUT2025.md reports/technical_analysis/
mv FASE1_INVENTARIO_COMPLETO_21OUT2025.md reports/technical_analysis/
mv FASE2_VERSOES_IDENTIFICADAS_21OUT2025.md reports/technical_analysis/
mv FASE3_MAPEAMENTO_CATEGORIAS_21OUT2025.md reports/technical_analysis/
```

**Tempo estimado:** 10 minutos

---

### OPERAÇÃO 7: Reorganizar Specifications (6 docs)

**De:** `HEMODOCTOR_HIBRIDO_V1.0/`
**Para:** `specifications/`

```bash
# Documentos raiz (4 arquivos)
mv HEMODOCTOR_HIBRIDO_V1.0/README.md specifications/
mv HEMODOCTOR_HIBRIDO_V1.0/INDEX_COMPLETO.md specifications/
mv HEMODOCTOR_HIBRIDO_V1.0/QUICKSTART_IMPLEMENTACAO.md specifications/
mv HEMODOCTOR_HIBRIDO_V1.0/CLAUDE.md specifications/

# Analise_Comparativa (2 docs)
mv HEMODOCTOR_HIBRIDO_V1.0/Analise_Comparativa/* specifications/comparative_analysis/
```

**Tempo estimado:** 5 minutos

---

### OPERAÇÃO 8: Limpar Diretórios Vazios

```bash
# Remover diretórios vazios após migração
rmdir HEMODOCTOR_HIBRIDO_V1.0/Analise_Comparativa
rmdir HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/06_CONSOLIDATION_LOGS
rmdir HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/01_CORE_TECHNICAL
rmdir HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/02_CLINICAL
rmdir HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/03_POST_MARKET
rmdir HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/04_REGULATORY
rmdir HEMODOCTOR_HIBRIDO_V1.0/HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018
rmdir HEMODOCTOR_HIBRIDO_V1.0

rmdir AUTHORITATIVE_BASELINE/00_INDICE_GERAL
rmdir AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR
rmdir AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS
rmdir AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD
rmdir AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/TEC
rmdir AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/RMP
rmdir AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/VVP
rmdir AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TestReports
rmdir AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/Cobertura
rmdir AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TST
rmdir AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER
rmdir AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC
rmdir AUTHORITATIVE_BASELINE/07_POS_MERCADO/PMS
rmdir AUTHORITATIVE_BASELINE/07_POS_MERCADO/Procedures
rmdir AUTHORITATIVE_BASELINE/07_POS_MERCADO/Forms
rmdir AUTHORITATIVE_BASELINE/08_ROTULAGEM/IFU
rmdir AUTHORITATIVE_BASELINE/09_CYBERSECURITY/SBOM
rmdir AUTHORITATIVE_BASELINE/09_CYBERSECURITY/VEX
rmdir AUTHORITATIVE_BASELINE/10_SOUP
rmdir AUTHORITATIVE_BASELINE
```

**Tempo estimado:** 2 minutos

---

## ✅ VALIDAÇÃO DE INTEGRIDADE

### Checklist de Validação

Antes de executar OPERAÇÃO 8 (remover diretórios), executar:

```bash
# Contar arquivos antes
BEFORE=$(find AUTHORITATIVE_BASELINE HEMODOCTOR_HIBRIDO_V1.0 -type f \( -name "*.md" -o -name "*.txt" -o -name "*.yaml" -o -name "*.py" -o -name "*.json" -o -name "*.pdf" -o -name "*.csv" \) | wc -l)

# Contar arquivos depois (novo local)
AFTER=$(find REGULATORY_PACKAGE reports specifications -type f \( -name "*.md" -o -name "*.txt" -o -name "*.yaml" -o -name "*.py" -o -name "*.json" -o -name "*.pdf" -o -name "*.csv" \) | wc -l)

# Comparar
if [ $BEFORE -eq $AFTER ]; then
  echo "✅ VALIDAÇÃO OK: $BEFORE arquivos antes = $AFTER arquivos depois"
else
  echo "❌ ERRO: $BEFORE arquivos antes ≠ $AFTER arquivos depois"
  echo "Diferença: $(($BEFORE - $AFTER)) arquivos"
fi
```

### Checklist Manual

- [ ] **67 docs regulatórios** em REGULATORY_PACKAGE/
- [ ] **6 versões oficiais** em locais corretos
- [ ] **14 versões obsoletas** em ARCHIVE/
- [ ] **57 reports** em reports/
- [ ] **6 specs** em specifications/
- [ ] **69 implementation files** em hemodoctor_cdss/ (inalterado)
- [ ] **27 skills** em .claude/skills/ (inalterado)
- [ ] **Total:** 225 arquivos (0 perdidos)

---

## ⏱️ CRONOGRAMA DE EXECUÇÃO

| Operação | Descrição | Tempo | Acumulado |
|----------|-----------|-------|-----------|
| **1** | Criar estrutura base | 1 min | 1 min |
| **2** | Migrar 6 docs oficiais | 5 min | 6 min |
| **3** | Migrar 55 docs AUTHORITATIVE únicos | 10 min | 16 min |
| **4** | Migrar 13 docs CONSOLIDADO únicos | 5 min | 21 min |
| **5** | Arquivar 14 versões obsoletas | 5 min | 26 min |
| **6** | Reorganizar 57 reports | 10 min | 36 min |
| **7** | Reorganizar 6 specifications | 5 min | 41 min |
| **Validação** | Verificar integridade | 5 min | 46 min |
| **8** | Limpar diretórios vazios | 2 min | 48 min |
| **Git** | Commit final | 2 min | **50 min** |

**Tempo Total Estimado:** ~50 minutos

---

## 📊 RESUMO DE MOVIMENTAÇÕES

| De → Para | Arquivos | Operação |
|-----------|----------|----------|
| CONSOLIDADO → REGULATORY_PACKAGE (oficiais) | 6 | 2 |
| AUTHORITATIVE → REGULATORY_PACKAGE (únicos) | 55 | 3 |
| CONSOLIDADO → REGULATORY_PACKAGE (únicos) | 13 | 4 |
| AUTHORITATIVE + CONSOLIDADO → ARCHIVE | 14 | 5 |
| HYBRID raiz + CONSOLIDADO logs → reports/ | 57 | 6 |
| HYBRID → specifications/ | 6 | 7 |
| **TOTAL MOVIDO** | **151** | — |
| **hemodoctor_cdss (inalterado)** | **69** | — |
| **.claude/skills (inalterado)** | **27** | — |
| **TOTAL GERAL** | **225** ✅ | — |

---

## 🎯 RESULTADOS ESPERADOS

### Antes (Estrutura Atual)

```
docs/
├── AUTHORITATIVE_BASELINE/ (50 docs)
├── HEMODOCTOR_HIBRIDO_V1.0/ (106 docs)
│   ├── CONSOLIDADO_20251018/ (36 docs)
│   ├── .claude/skills/ (27 docs)
│   └── raiz (57 reports + 6 specs)
└── hemodoctor_cdss/ (69 docs)

TOTAL: 225 arquivos em 3 diretórios principais
```

### Depois (Estrutura Final)

```
docs/
├── REGULATORY_PACKAGE/ (67 docs oficiais + 14 archive)
├── hemodoctor_cdss/ (69 docs inalterado)
├── .claude/skills/ (27 docs inalterado)
├── reports/ (57 docs)
├── specifications/ (6 docs)
└── raiz (7 arquivos essenciais)

TOTAL: 225 arquivos em 5 diretórios principais
```

**Benefícios:**
- ✅ **Versões oficiais** em local único (REGULATORY_PACKAGE)
- ✅ **Versões antigas** arquivadas (não deletadas)
- ✅ **Reports** organizados por categoria
- ✅ **Specifications** separadas de reports
- ✅ **Nenhum arquivo perdido** (225 antes = 225 depois)

---

## ✅ CHECKLIST FASE 4

- [x] Estrutura final detalhada (arquivo por arquivo)
- [x] Plano de migração (8 operações)
- [x] Comandos bash prontos
- [x] Validação de integridade (checklist manual + script)
- [x] Cronograma de execução (50 min total)
- [x] Resumo de movimentações (151 arquivos movidos)
- [x] Resultados esperados (antes/depois)
- [x] Relatório gerado

**Status:** ✅ FASE 4 COMPLETA - Ready for FASE 5

---

## 🔜 PRÓXIMO

**FASE 5:** Executar consolidação (mover/renomear) (50 min)

**O que fazer:**
1. Executar OPERAÇÃO 1 (criar estrutura base)
2. Executar OPERAÇÃO 2-7 (migrar arquivos)
3. Executar Validação (verificar integridade)
4. Executar OPERAÇÃO 8 (limpar diretórios vazios)
5. Git add + commit

**Importante:**
- ⚠️ **Backup antes:** Criar backup completo antes de FASE 5
- ⚠️ **Git tracking:** Todas as operações em git (mv, não apenas cp)
- ⚠️ **Validação:** Verificar integridade após cada operação crítica

---

**Criado:** 21 de Outubro de 2025
**Duração Fase 4:** 30 minutos
**Total Operações:** 8
**Tempo Execução Estimado:** 50 minutos
**Arquivos a Mover:** 151
**Arquivos Totais:** 225 ✅
