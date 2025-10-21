# 📊 FASE 2: IDENTIFICAÇÃO DE VERSÕES MAIS RECENTES

**Data:** 21 de Outubro de 2025
**Status:** ✅ COMPLETO
**Duração:** 45 minutos
**Método:** Análise sistemática dos 225 arquivos inventariados

---

## 🎯 OBJETIVO

Identificar versões mais recentes de cada documento no repositório, comparando:
- HEMODOCTOR_HIBRIDO_V1.0/ (106 arquivos)
- AUTHORITATIVE_BASELINE/ (50 arquivos)
- hemodoctor_cdss/ (69 arquivos)

---

## 📋 RESULTADO PRINCIPAL

**Total de duplicações críticas:** 6 documentos regulatórios com múltiplas versões

| Documento | Versões | Localização Mais Recente |
|-----------|---------|-------------------------|
| SRS-001 | 4 versões (v1.0 → v3.1) | CONSOLIDADO_20251018 |
| SDD-001 | 4 versões (v1.0 → v2.1) | CONSOLIDADO_20251018 |
| TEC-002 | 4 versões (v1.0 → v2.1) | CONSOLIDADO_20251018 |
| TRC-001 | 4 versões (v1.0 → v2.1) | CONSOLIDADO_20251018 |
| CER-001 | 4 versões (v1.0 → v2.0) | CONSOLIDADO_20251018 |
| PMS-001 | 3 versões (v1.0 → v2.0) | CONSOLIDADO_20251018 |

**Duplicações não-críticas:**
- __init__.py (9 cópias) - ✅ Normal (módulos Python diferentes)
- README.md (7 cópias) - ✅ Normal (um por diretório)
- SKILL.md (9 cópias) - ✅ Normal (um por skill)
- evidence.py, syndrome.py (2 cópias cada) - ✅ Contextos diferentes (engines vs models)
- validate_yaml.py (2 cópias) - ✅ Skills diferentes

---

## 📊 ANÁLISE DETALHADA POR DOCUMENTO

### 1. SRS-001 (Software Requirements Specification)

**Versão Mais Recente:** v3.1 OFICIAL YAMLS FULL (59 KB) ⭐

**Todas as Versões:**

| Versão | Tamanho | Localização | Status |
|--------|---------|-------------|--------|
| v1.0 OFICIAL | 81 KB | AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/ | 🟡 Baseline original |
| v3.0 FULL | 73 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | 🟡 Atualizado |
| v3.0 EXECUTIVE SUMMARY | 24 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | 🟡 Resumo executivo |
| v3.1 YAMLS FULL | 59 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | ✅ **MAIS RECENTE** |

**Arquivos Relacionados:**
- CONSOLIDATION_LOG_SRS-001.md (14 KB) - Log de consolidação
- ANALISE_SRS-001.md (6.4 KB) - Análise técnica

**Decisão:** Manter v3.1 YAMLS FULL como oficial

---

### 2. SDD-001 (Software Design Document)

**Versão Mais Recente:** v2.1 OFICIAL YAMLS FULL (69 KB) ⭐

**Todas as Versões:**

| Versão | Tamanho | Localização | Status |
|--------|---------|-------------|--------|
| v1.0 OFICIAL | 60 KB | AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD/ | 🟡 Baseline original |
| v2.0 FULL | 34 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | 🟡 Atualizado |
| v2.0 EXECUTIVE SUMMARY | 6.5 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | 🟡 Resumo executivo |
| v2.1 YAMLS FULL | 69 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | ✅ **MAIS RECENTE** |

**Arquivos Relacionados:**
- CONSOLIDATION_LOG_SDD-001.md (12 KB) - Log de consolidação

**Decisão:** Manter v2.1 YAMLS FULL como oficial

---

### 3. TEC-002 (Technical File - Risk Management)

**Versão Mais Recente:** v2.1 OFICIAL YAMLS FULL (48 KB) ⭐

**Todas as Versões:**

| Versão | Tamanho | Localização | Status |
|--------|---------|-------------|--------|
| v1.0 OFICIAL | 52 KB | AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/RMP/ | 🟡 Baseline original |
| v2.0 FULL | 52 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | 🟡 Atualizado |
| v2.0 EXECUTIVE SUMMARY | 11 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | 🟡 Resumo executivo |
| v2.1 YAMLS FULL | 48 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | ✅ **MAIS RECENTE** |

**Arquivos Relacionados:**
- CONSOLIDATION_LOG_TEC-002.md (11 KB) - Log de consolidação

**Decisão:** Manter v2.1 YAMLS FULL como oficial

---

### 4. TRC-001 (Traceability Matrix)

**Versão Mais Recente:** v2.1 OFICIAL YAMLS FULL (31 KB) ⭐

**Todas as Versões:**

| Versão | Tamanho | Localização | Status |
|--------|---------|-------------|--------|
| v1.0 OFICIAL (CSV) | 7.1 KB | AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/ | 🟡 Baseline original |
| v2.0 UPDATE SUMMARY | 6.5 KB | AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/ | 🟡 Resumo atualização |
| v2.1 YAMLS FULL | 31 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | ✅ **MAIS RECENTE** |
| v2.1 UPDATE SUMMARY | 12 KB | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ | 🟡 Resumo atualização |

**Decisão:** Manter v2.1 YAMLS FULL como oficial

---

### 5. CER-001 (Clinical Evaluation Report)

**Versão Mais Recente:** v2.0 OFICIAL CONSOLIDADO FULL (75 KB) ⭐

**Todas as Versões:**

| Versão | Tamanho | Localização | Status |
|--------|---------|-------------|--------|
| v1.0 OFICIAL | 75 KB | AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER/ | 🟡 Baseline original |
| VALIDATION REPORT | 27 KB | AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER/ | 🟡 Relatório validação |
| v2.0 FULL | 75 KB | CONSOLIDADO_20251018/02_CLINICAL/ | ✅ **MAIS RECENTE** |
| v2.0 EXECUTIVE SUMMARY | 9.1 KB | CONSOLIDADO_20251018/02_CLINICAL/ | 🟡 Resumo executivo |

**Arquivos Relacionados:**
- CONSOLIDATION_LOG_CER-001.md (9.8 KB) - Log de consolidação

**Decisão:** Manter v2.0 FULL como oficial

---

### 6. PMS-001 (Post-Market Surveillance)

**Versão Mais Recente:** v2.0 OFICIAL CONSOLIDADO FULL (18 KB) ⭐

**Todas as Versões:**

| Versão | Tamanho | Localização | Status |
|--------|---------|-------------|--------|
| v1.0 OFICIAL | 1.2 KB | AUTHORITATIVE_BASELINE/07_POS_MERCADO/PMS/ | 🟡 Baseline original (stub) |
| v2.0 FULL | 18 KB | CONSOLIDADO_20251018/03_POST_MARKET/ | ✅ **MAIS RECENTE** |
| v2.0 EXECUTIVE SUMMARY | 5.8 KB | CONSOLIDADO_20251018/03_POST_MARKET/ | 🟡 Resumo executivo |

**Arquivos Relacionados:**
- CONSOLIDATION_LOG_PMS-001.md (23 KB) - Log de consolidação

**Decisão:** Manter v2.0 FULL como oficial

---

### 7. VVP-001 (Verification & Validation Plan)

**Versão Única:** v1.0 OFICIAL (35 KB) ✅

**Localização:** AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/VVP/

**Decisão:** Manter v1.0 como oficial (versão única)

---

## 🔍 PADRÃO IDENTIFICADO

### Estrutura de Versionamento

```
AUTHORITATIVE_BASELINE/
├── Versões v1.0 (baseline original)
└── Algumas v2.0 UPDATE_SUMMARY

HEMODOCTOR_HIBRIDO_V1.0/CONSOLIDADO_20251018/
├── Versões v2.0 FULL (atualização consolidada)
├── Versões v2.1 YAMLS FULL (baseado em YAMLs v2.4.0) ⭐ MAIS RECENTE
└── EXECUTIVE_SUMMARY para cada versão
```

### Cronologia de Versionamento

1. **v1.0 OFICIAL** (AUTHORITATIVE_BASELINE) - Baseline original
2. **v2.0 CONSOLIDADO FULL** (CONSOLIDADO_20251018) - Primeira consolidação
3. **v2.1 YAMLS FULL** (CONSOLIDADO_20251018) - Baseado em YAMLs v2.4.0 ⭐
4. **v3.0/v3.1** (SRS-001 apenas) - Versão avançada

### Nomenclatura

- **OFICIAL** = Documento oficial submetido
- **FULL** = Versão completa
- **EXECUTIVE_SUMMARY** = Resumo executivo
- **UPDATE_SUMMARY** = Resumo de atualizações
- **YAMLS** = Baseado em YAMLs v2.4.0 (evidências + síndromes)
- **CONSOLIDADO** = Versão consolidada de múltiplas fontes

---

## 📁 OUTROS DOCUMENTOS (SEM DUPLICAÇÃO)

### Documentos Únicos em AUTHORITATIVE_BASELINE

**01_REGULATORIO:**
- DMR_v2.0_DELIVERABLES.md
- DMR-001_Device_Master_Record_v1.0_SUMMARY.md

**02_CONTROLES_DESIGN:**
- TEC-001_Software_Development_Plan_v1.0_OFICIAL.md (28 KB)

**04_VERIFICACAO_VALIDACAO:**
- VVP-001_Verification_Validation_Plan_v1.0_OFICIAL.md (35 KB)
- TESTREP-001_Unit_Tests_Report_v1.0_OFICIAL.md (20 KB)
- TESTREP-002_Integration_Tests_Report_v1.0_OFICIAL.md (2.9 KB)
- TESTREP-003_System_Tests_Report_v1.0_OFICIAL.md (3.7 KB)
- TESTREP-004_Validation_Tests_Report_v1.0_OFICIAL.md (6.6 KB)
- COV-001_Test_Coverage_Analysis_v1.0_OFICIAL.md (18 KB)
- COV-001_Coverage_Matrix_v1.0_OFICIAL.csv (4 KB)
- TST-001_Test_Specification_v1.0_OFICIAL.md (68 KB)

**Total:** 8 documentos (100% únicos - mantidos como estão)

### Documentos Únicos em CONSOLIDADO_20251018

**02_CLINICAL:**
- PROJ-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md (78 KB)
- TCLE-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md (13 KB)

**04_REGULATORY:**
- SEC-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md (58 KB)
- IFU-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md (19 KB)
- SOUP-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md (17 KB)

**06_CONSOLIDATION_LOGS:**
- 11 logs de consolidação (.md)

**Total:** 18 documentos (100% únicos - mantidos como estão)

### Documentos Únicos em hemodoctor_cdss

**docs/:**
- IMPLEMENTATION_REPORT.md (14 KB)
- DEVELOPER_HANDOFF.md (14 KB)
- COMPLETION_SUMMARY.md (12 KB)
- SECURITY_TESTING_SUMMARY.md (11 KB)
- SPRINT_2_PLAN_INTEGRATION_TESTING.md (10 KB)
- TEST-SPEC-001_v1.0_YAML_VALIDATION.md (40 KB)
- RESUMO_SESSAO_21_OUT_2025_FINAL.md (13 KB)
- RESUMO_EXECUCAO_PARALELA_FINAL.md (8.6 KB)
- QUICK_START_NOVA_JANELA.md (7.6 KB)
- HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx (34 KB)

**Total:** 10+ documentos (100% únicos - mantidos como estão)

---

## 🎯 DECISÕES DE CONSOLIDAÇÃO

### Versões Oficiais (Mais Recentes)

| Documento | Versão Oficial | Localização |
|-----------|----------------|-------------|
| **SRS-001** | v3.1 YAMLS FULL (59 KB) | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ |
| **SDD-001** | v2.1 YAMLS FULL (69 KB) | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ |
| **TEC-002** | v2.1 YAMLS FULL (48 KB) | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ |
| **TRC-001** | v2.1 YAMLS FULL (31 KB) | CONSOLIDADO_20251018/01_CORE_TECHNICAL/ |
| **CER-001** | v2.0 FULL (75 KB) | CONSOLIDADO_20251018/02_CLINICAL/ |
| **PMS-001** | v2.0 FULL (18 KB) | CONSOLIDADO_20251018/03_POST_MARKET/ |
| **VVP-001** | v1.0 OFICIAL (35 KB) | AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/VVP/ |

### Versões a Arquivar

**AUTHORITATIVE_BASELINE (versões v1.0):**
- SRS-001_Software_Requirements_v1.0_OFICIAL.md (81 KB)
- SDD-001_Software_Design_v1.0_OFICIAL.md (60 KB)
- TEC-002_Risk_Management_File_v1.0_OFICIAL.md (52 KB)
- TRC-001_Traceability_Matrix_v1.0_OFICIAL.csv (7.1 KB)
- CER-001_Clinical_Evaluation_Report_v1.0_OFICIAL.md (75 KB)
- PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md (1.2 KB)

**Total:** 6 documentos a arquivar

**CONSOLIDADO_20251018 (versões intermediárias v2.0/v3.0):**
- SRS-001_v3.0_OFICIAL_CONSOLIDADO_FULL.md (73 KB)
- SRS-001_v3.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (24 KB)
- SDD-001_v2.0_OFICIAL_CONSOLIDADO_FULL.md (34 KB)
- SDD-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (6.5 KB)
- TEC-002_v2.0_OFICIAL_CONSOLIDADO_FULL.md (52 KB)
- TEC-002_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (11 KB)
- CER-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (9.1 KB)
- PMS-001_v2.0_OFICIAL_CONSOLIDADO_EXECUTIVE_SUMMARY.md (5.8 KB)

**Total:** 8 documentos a arquivar

### Versões a Manter (Mais Recentes + Únicos)

**Total:** 6 versões oficiais + ~180 documentos únicos = **186 documentos ativos**

---

## 📊 MÉTRICAS FINAIS

| Métrica | Valor |
|---------|-------|
| **Total arquivos inventariados** | 225 |
| **Documentos únicos** | ~180 (80%) |
| **Documentos com múltiplas versões** | 6 (3%) |
| **Versões totais** | 26 (11%) |
| **Duplicações Python** | 6 arquivos (contextos diferentes) |
| **Versões a arquivar** | 14 (6%) |
| **Versões oficiais identificadas** | 6 (100% dos docs com múltiplas versões) |

---

## ✅ CHECKLIST FASE 2

- [x] Analisar 225 arquivos
- [x] Identificar duplicações (6 arquivos Python - contextos diferentes)
- [x] Identificar documentos com múltiplas versões (6 docs regulatórios)
- [x] Comparar versões (v1.0 vs v2.0 vs v2.1 vs v3.0/v3.1)
- [x] Identificar versão mais recente de cada documento
- [x] Documentar padrão de versionamento
- [x] Criar lista de versões a arquivar (14 documentos)
- [x] Criar lista de versões oficiais (6 documentos)
- [x] Relatório gerado

**Status:** ✅ FASE 2 COMPLETA - Ready for FASE 3

---

## 🔜 PRÓXIMO

**FASE 3:** Mapear categorias reais de documentos (30 min)

**O que fazer:**
1. Analisar conteúdo dos 186 documentos ativos
2. Identificar categorias temáticas (não só estrutura de pastas)
3. Propor agrupamento lógico
4. Verificar se estrutura atual reflete conteúdo real

---

**Criado:** 21 de Outubro de 2025
**Duração Fase 2:** 45 minutos
**Total Arquivos Analisados:** 225
**Versões Oficiais Identificadas:** 6/6 (100%)
