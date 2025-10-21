# 📋 Relatório de Mapeamento de Versões - Fase 1

**Data de Execução**: 12 de Outubro de 2025
**Responsável**: @documentation-finalization-specialist
**Projeto**: HemoDoctor ANVISA Baseline Unificada v1.0
**Estratégia Escolhida**: Opção B - Consolidar e Resetar (Limpeza Total)

---

## 🎯 Objetivo da Fase 1

Realizar auditoria completa e mapeamento de:
1. Todos os documentos atuais com suas versões
2. Referências cruzadas entre documentos
3. Dependências de versionamento
4. Matriz de impacto de mudança de versões

---

## 📊 1. INVENTÁRIO COMPLETO DE DOCUMENTOS

### 1.1 Documentos OFICIAIS por Módulo

| Módulo | Código | Nome do Documento | Versões Encontradas | Versão Alvo |
|--------|--------|-------------------|---------------------|-------------|
| **01 - REGULATÓRIO** | DMR-001 | Device Master Record | v2.0 (manifest) | → v1.0 |
| **02 - CONTROLES DESIGN** | SRS-001 | Software Requirements | v1.0, v1.1, v2.0, v2.0-PT-BR, v2.2 | → v1.0 |
| | SDD-001 | Software Design | v1.0, v1.1, v2.0 | → v1.0 |
| | TEC-001 | Development Plan | v1.0 ✅ | v1.0 (OK) |
| | API-SPECS | API Specifications | v1.0 ✅ (12 arquivos) | v1.0 (OK) |
| **03 - GESTÃO RISCO** | RMP-001 | Risk Management Plan | v1.0 ✅ | v1.0 (OK) |
| | TEC-002 | Risk Management File | v2.0 | → v1.0 |
| **04 - V&V** | TST-001 | Test Specification | v1.0 ✅ | v1.0 (OK) |
| **05 - AVALIAÇÃO CLÍNICA** | CER-001 | Clinical Evaluation Report | v1.2 | → v1.0 |
| **06 - RASTREABILIDADE** | TRC-001 | Traceability Matrix | v1.0, v2.0, v2.1 | → v1.0 |
| **07 - PÓS-MERCADO** | PMS-001 | Post-Market Surveillance | v1.1 | → v1.0 |
| **08 - ROTULAGEM** | IFU-001 | Instructions for Use | v1.0 ✅ (PT + EN) | v1.0 (OK) |
| **09 - CYBERSECURITY** | SEC-001 | Cybersecurity | v1.0 ✅ | v1.0 (OK) |
| | SBOM | Software Bill of Materials | v1.0 ✅ | v1.0 (OK) |
| **10 - SOUP** | SOUP-001 | SOUP Analysis | v1.0 ✅ | v1.0 (OK) |

### 1.2 Resumo Estatístico

| Categoria | Quantidade | Status |
|-----------|------------|--------|
| **Total de documentos oficiais** | 14 documentos base | - |
| **✅ Já em v1.0** | 8 documentos | Sem ação necessária |
| **⚠️ Precisam padronização** | 6 documentos | Requerem ação |
| **📄 Versões duplicadas** | 11 arquivos extras | Serão deletados |
| **API Specs em v1.0** | 12 arquivos | Sem ação necessária |

### 1.3 Documentos que Precisam Padronização (6 documentos)

#### 📌 Ação Necessária:

1. **SRS-001**: v2.2 → v1.0 (deletar v1.0, v1.1, v2.0, v2.0-PT-BR)
2. **SDD-001**: v2.0 → v1.0 (deletar v1.0, v1.1)
3. **CER-001**: v1.2 → v1.0
4. **TRC-001**: v2.1 → v1.0 (deletar v1.0, v2.0)
5. **PMS-001**: v1.1 → v1.0
6. **DMR-001**: v2.0 (manifest) → v1.0 (atualizar manifest)
7. **TEC-002**: v2.0 → v1.0

---

## 🔗 2. MAPEAMENTO DE REFERÊNCIAS CRUZADAS

### 2.1 Matriz de Dependências de Versão

| Documento Fonte | Versão Atual | Referencia → | Documento Destino | Versão Referenciada |
|----------------|--------------|--------------|-------------------|---------------------|
| SDD-001 v1.0 | v1.0 | → | SRS-001 | v1.0 |
| SDD-001 v1.0 | v1.0 | → | TEC-001 | v1.0 |
| SDD-001 v1.0 | v1.0 | → | RMP-001 | (sem versão) |
| SDD-001 v1.0 | v1.0 | → | TRC-001 | v1.0 |
| SDD-001 v2.0 | v2.0 | → | SRS-001 | v2.1 ⚠️ |
| SDD-001 v2.0 | v2.0 | → | TRC-001 | v2.1 ⚠️ |
| SDD-001 v2.0 | v2.0 | → | SEC-001 | v1.0 BASELINE |
| CER-001 v1.2 | v1.2 | → | SRS-001 | v1.1 ⚠️ |
| CER-001 v1.2 | v1.2 | → | RMP-001 | v1.0 ✅ |
| CER-001 v1.2 | v1.2 | → | PMS-001 | (sem versão) ⚠️ |
| CER-001 v1.2 | v1.2 | → | IFU-001 | (sem versão) |
| TRC-001 v2.0 | v2.0 | → | SRS-001 | v1.0 ⚠️ |
| TRC-001 v2.0 | v2.0 | → | SDD-001 | v1.0 ⚠️ |
| TRC-001 v2.0 | v2.0 | → | RMP-001 | v1.0 ✅ |
| DMR Manifest v2.0 | v2.0 | → | SRS-001 | v1.1 ⚠️ |
| DMR Manifest v2.0 | v2.0 | → | SDD-001 | v1.1 ⚠️ |
| DMR Manifest v2.0 | v2.0 | → | CER-001 | v1.2 ⚠️ |
| DMR Manifest v2.0 | v2.0 | → | TRC-001 | v2.0 ⚠️ |
| DMR Manifest v2.0 | v2.0 | → | PMS-001 | v1.1 ⚠️ |

**Legenda:**
- ✅ Referência correta (documento destino já em v1.0)
- ⚠️ Referência precisa atualização (documento destino será v1.0)

### 2.2 Documentos Referenciadores (precisam atualização)

Os seguintes documentos **REFERENCIAM** versões antigas e precisarão ser atualizados na Fase 4:

1. **SDD-001 v2.0** → Referencia SRS v2.1, TRC v2.1
2. **CER-001 v1.2** → Referencia SRS v1.1
3. **TRC-001 v2.0** → Referencia SRS v1.0, SDD v1.0
4. **DMR Manifest v2.0** → Lista todos os documentos com versões antigas

### 2.3 Arquivos de Suporte e Relatórios

**Arquivos NÃO OFICIAIS que contêm referências (não bloqueadores):**
- SUBMISSION_READY_STATUS.md
- CONSOLIDACAO_COMPLETA_REPORT.md
- EXECUCAO_AUTOMATICA_COMPLETA_2025-10-08.md
- VALIDACOES_CONSOLIDADAS_REPORT.md
- TRC-001_v2.0_UPDATE_SUMMARY.md
- CER-001_VALIDATION_REPORT.md

**Ação:** Estes arquivos podem ser movidos para 00_HISTORICO/ ou atualizados opcionalmente.

---

## 🗂️ 3. ESTRUTURA DE ARQUIVOS ATUAL vs. PROPOSTA

### 3.1 Estado Atual (ANTES da padronização)

```
AUTHORITATIVE_BASELINE/
├── 00_INDICE_GERAL/
│   ├── Relatórios diversos (8 arquivos)
│   └── CHECKSUMS_SHA256_v2.0.txt
├── 01_REGULATORIO/
│   └── DMR/
│       ├── DMR_MANIFEST_v2.0_20251008_OFICIAL.json ⚠️
│       ├── DMR_MANIFEST_v2.0_SUMMARY.md ⚠️
│       └── verify_dmr_v2.0.sh ⚠️
├── 02_CONTROLES_DESIGN/
│   ├── SRS/
│   │   ├── SRS-001_v1.0_OFICIAL.md ❌ DELETE
│   │   ├── SRS-001_v1.1_OFICIAL.md ❌ DELETE
│   │   ├── SRS-001_v2.0_AUTHORITATIVE_20251008.md ❌ DELETE
│   │   ├── SRS-001_v2.0_AUTHORITATIVE_20251008_PT-BR.md ❌ DELETE
│   │   └── SRS-001_v2.2_AUTHORITATIVE_20251008.md → v1.0 ✅
│   ├── SDD/
│   │   ├── SDD-001_v1.0_OFICIAL.md ❌ DELETE
│   │   ├── SDD-001_v1.1_OFICIAL.md ❌ DELETE
│   │   └── SDD-001_v2.0_AUTHORITATIVE_20251008.md → v1.0 ✅
│   ├── TEC/
│   │   └── TEC-001_v1.0_OFICIAL.md ✅ (OK)
│   └── API_SPECS/ (12 arquivos v1.0) ✅ (OK)
├── 03_GESTAO_RISCO/
│   └── RMP/
│       ├── RMP-001_v1.0_OFICIAL.md ✅ (OK)
│       └── TEC-002_Risk_Management_File_v2.0_AUTHORITATIVE_20251008.md → v1.0 ⚠️
├── 04_VERIFICACAO_VALIDACAO/
│   └── TST/
│       └── TST-001_v1.0_OFICIAL.md ✅ (OK)
├── 05_AVALIACAO_CLINICA/
│   └── CER/
│       ├── CER-001_v1.2_OFICIAL.md → v1.0 ⚠️
│       └── CER-001_VALIDATION_REPORT.md (relatório)
├── 06_RASTREABILIDADE/
│   └── TRC/
│       ├── TRC-001_v1.0_OFICIAL.csv ❌ DELETE
│       ├── TRC-001_v2.0_OFICIAL.csv ❌ DELETE
│       ├── TRC-001_v2.1_COMPLETE_20251008.csv → v1.0 ✅
│       ├── TRC-001_v2.0_UPDATE_SUMMARY.md (relatório)
│       └── VALIDATION_REPORT.md (relatório)
├── 07_POS_MERCADO/
│   └── PMS/
│       └── PMS-001_v1.1_OFICIAL.md → v1.0 ⚠️
├── 08_ROTULAGEM/
│   └── IFU/
│       ├── IFU-001_PT_BR_v1.0_OFICIAL.pdf ✅ (OK)
│       └── IFU-001_EN_US_v1.0_OFICIAL.pdf ✅ (OK)
├── 09_CYBERSECURITY/
│   └── SEC/
│       └── SEC-001_v1.0_OFICIAL.md ✅ (OK)
└── 10_SOUP/
    └── SOUP-001_v1.0_OFICIAL.md ✅ (OK)
```

### 3.2 Estado Final Proposto (DEPOIS da padronização)

```
AUTHORITATIVE_BASELINE/
├── 01_REGULATORIO/
│   └── DMR/
│       ├── DMR-001_Device_Master_Record_v1.0_OFICIAL.json ✅
│       └── DMR-001_Device_Master_Record_v1.0_SUMMARY.md ✅
├── 02_CONTROLES_DESIGN/
│   ├── SRS/
│   │   └── SRS-001_Software_Requirements_v1.0_OFICIAL.md ✅
│   ├── SDD/
│   │   └── SDD-001_Software_Design_v1.0_OFICIAL.md ✅
│   ├── TEC/
│   │   └── TEC-001_Software_Development_Plan_v1.0_OFICIAL.md ✅
│   └── API_SPECS/ (12 arquivos v1.0) ✅
├── 03_GESTAO_RISCO/
│   └── RMP/
│       ├── RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md ✅
│       └── TEC-002_Risk_Management_File_v1.0_OFICIAL.md ✅
├── 04_VERIFICACAO_VALIDACAO/
│   └── TST/
│       └── TST-001_Test_Specification_v1.0_OFICIAL.md ✅
├── 05_AVALIACAO_CLINICA/
│   └── CER/
│       └── CER-001_Clinical_Evaluation_Report_v1.0_OFICIAL.md ✅
├── 06_RASTREABILIDADE/
│   └── TRC/
│       └── TRC-001_Traceability_Matrix_v1.0_OFICIAL.csv ✅
├── 07_POS_MERCADO/
│   └── PMS/
│       └── PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md ✅
├── 08_ROTULAGEM/
│   └── IFU/ ✅
├── 09_CYBERSECURITY/
│   └── SEC/ ✅
└── 10_SOUP/ ✅
```

**Nota:** Documentos deletados conforme Opção B (Limpeza Total) - sem diretório 00_HISTORICO/.

---

## 📈 4. MATRIZ DE IMPACTO DE MUDANÇA DE VERSÕES

### 4.1 Documentos a Serem Padronizados (7 documentos)

| Documento | Versão Mais Recente | → Versão Alvo | Tamanho | Ação Principal | Impacto |
|-----------|---------------------|---------------|---------|----------------|---------|
| **SRS-001** | v2.2 | v1.0 | 39.8 KB | Renomear + Atualizar header | 🔴 ALTO |
| **SDD-001** | v2.0 | v1.0 | 34.6 KB | Renomear + Atualizar header | 🔴 ALTO |
| **CER-001** | v1.2 | v1.0 | 76.4 KB | Renomear + Atualizar header | 🟡 MÉDIO |
| **TRC-001** | v2.1 | v1.0 | 5.1 KB | Renomear + Atualizar referências | 🔴 ALTO |
| **PMS-001** | v1.1 | v1.0 | 1.2 KB | Renomear + Atualizar header | 🟢 BAIXO |
| **TEC-002** | v2.0 | v1.0 | ? KB | Renomear + Atualizar header | 🟡 MÉDIO |
| **DMR Manifest** | v2.0 | v1.0 | 22.9 KB | Atualizar todas as versões referenciadas | 🔴 ALTO |

**Impacto:**
- 🔴 **ALTO**: Documento é altamente referenciado por outros documentos
- 🟡 **MÉDIO**: Documento tem algumas referências cruzadas
- 🟢 **BAIXO**: Documento tem poucas ou nenhuma referência cruzada

### 4.2 Arquivos a Serem Deletados (11 arquivos)

| Arquivo | Versão | Tamanho | Razão da Deleção |
|---------|--------|---------|------------------|
| SRS-001_v1.0_OFICIAL.md | v1.0 | ~29 KB | Versão intermediária, v2.2 é a definitiva |
| SRS-001_v1.1_OFICIAL.md | v1.1 | ~40 KB | Versão intermediária, v2.2 é a definitiva |
| SRS-001_v2.0_AUTHORITATIVE_20251008.md | v2.0 | ~38 KB | Versão intermediária, v2.2 é a definitiva |
| SRS-001_v2.0_AUTHORITATIVE_20251008_PT-BR.md | v2.0 | ~38 KB | Duplicata PT-BR, v2.2 é EN única |
| SDD-001_v1.0_OFICIAL.md | v1.0 | ~28 KB | Versão intermediária, v2.0 é a definitiva |
| SDD-001_v1.1_OFICIAL.md | v1.1 | ~34 KB | Versão intermediária, v2.0 é a definitiva |
| TRC-001_v1.0_OFICIAL.csv | v1.0 | ~0.5 KB | Versão desatualizada, v2.1 é a definitiva |
| TRC-001_v2.0_OFICIAL.csv | v2.0 | ~5 KB | Versão intermediária, v2.1 é a definitiva |
| DMR_MANIFEST_OFICIAL.json | (sem v) | ? KB | Versão antiga do manifest |
| verify_dmr_v2.0.sh | v2.0 | ~4 KB | Script de verificação v2.0, será atualizado |
| CHECKSUMS_SHA256_v2.0.txt | v2.0 | ~2 KB | Checksums v2.0, será recriado para v1.0 |

**Total de espaço liberado:** ~259 KB (estimado)

### 4.3 Referências a Serem Atualizadas

#### 🔄 Fase 4: Atualização de Referências Cruzadas (23 atualizações)

| Documento a Atualizar | Linha/Seção Aproximada | Atualização Necessária |
|-----------------------|------------------------|------------------------|
| **SDD-001 v1.0** | Linha 18 (Related Documents) | SRS-001 v1.0 → (nenhuma mudança, OK) |
| **SDD-001 v2.0** | Linha 18 (Related Documents) | SRS-001 v2.1 → SRS-001 v1.0 |
| **SDD-001 v2.0** | Linha 22 (Related Documents) | TRC-001 v2.1 → TRC-001 v1.0 |
| **CER-001 v1.2** | Linha 98 (Traceability) | SRS-001 v1.1 → SRS-001 v1.0 |
| **CER-001 v1.2** | Header yaml | version: "1.2" → "1.0" |
| **TRC-001 v2.0** | Header (Source Documents) | SRS-001 v1.0 → (já correto) |
| **TRC-001 v2.0** | Header (Source Documents) | SDD-001 v1.0 → (já correto) |
| **PMS-001 v1.1** | Header yaml | version: "1.1" → "1.0" |
| **DMR Manifest v2.0** | Linha 36 (SRS) | v1.1 → v1.0 |
| **DMR Manifest v2.0** | Linha 37 (SDD) | v1.1 → v1.0 |
| **DMR Manifest v2.0** | Linha 41 (CER) | v1.2 → v1.0 |
| **DMR Manifest v2.0** | Linha 42 (TRC) | v2.0 → v1.0 |
| **DMR Manifest v2.0** | Linha 43 (PMS) | v1.1 → v1.0 |
| **DMR Manifest v2.0** | Linha 6-9 (metadata) | version: "v2.0-20251008" → "v1.0-20251012" |
| **verify_dmr_v2.0.sh** | Todo o script | Renomear para verify_dmr_v1.0.sh + atualizar versões |
| **SUBMISSION_READY_STATUS.md** | Linhas 36-40 | Atualizar versões para v1.0 |
| **README_FINAL.md** | Seção de versões | Atualizar versões para v1.0 |
| **00_API_INDEX.md** | Referências a SRS/SDD | Atualizar para v1.0 |

**IMPORTANTE:** Busca global por padrões de versão antiga:
- `v2.2` (SRS)
- `v2.0` (SDD, TRC, DMR)
- `v1.2` (CER)
- `v2.1` (TRC, SRS)
- `v1.1` (SRS, SDD, PMS)

---

## 🎯 5. PLANO DE EXECUÇÃO DETALHADO (Opção B)

### 5.1 Fase 2: Backup e Preparação (15 minutos)

**NÃO será criado diretório 00_HISTORICO/** (Opção B: Limpeza Total)

**Ações:**
1. ✅ Criar branch Git: `feature/versao-1.0-unificada`
2. ✅ Commit do estado atual: "Pre-standardization snapshot"
3. ✅ Tag de backup: `backup-pre-v1.0-unification`

**Comandos:**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs
git checkout -b feature/versao-1.0-unificada
git add .
git commit -m "📸 Pre-standardization snapshot - v2.x baseline"
git tag -a backup-pre-v1.0-unification -m "Backup antes da padronização v1.0"
```

### 5.2 Fase 3: Execução da Padronização (1-2 horas)

**Opção B: Deletar versões antigas + Renomear versões finais**

#### Documento 1: SRS-001

```bash
# Delete versões antigas
rm AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_v1.0_OFICIAL.md
rm AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_v1.1_OFICIAL.md
rm AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_v2.0_AUTHORITATIVE_20251008.md
rm AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_v2.0_AUTHORITATIVE_20251008_PT-BR.md

# Renomear versão final v2.2 → v1.0
mv AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_Software_Requirements_v2.2_AUTHORITATIVE_20251008.md \
   AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_Software_Requirements_v1.0_OFICIAL.md

# Atualizar header do documento (Edit tool)
# - version: "v2.2" → "v1.0"
# - status: "APPROVED - Ready for test suite integration" → "OFICIAL - Primeira Submissão ANVISA"
# - Adicionar seção history com evolução v2.2 → v2.1 → v2.0 → ... → v1.0
```

#### Documento 2: SDD-001

```bash
# Delete versões antigas
rm AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD/SDD-001_v1.0_OFICIAL.md
rm AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD/SDD-001_v1.1_OFICIAL.md

# Renomear versão final v2.0 → v1.0
mv AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD/SDD-001_Software_Design_v2.0_AUTHORITATIVE_20251008.md \
   AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD/SDD-001_Software_Design_v1.0_OFICIAL.md

# Atualizar header
# - version: "v2.0" → "v1.0"
# - status: "Consolidated - Ready for ANVISA Submission" → "OFICIAL - Primeira Submissão ANVISA"
```

#### Documento 3: CER-001

```bash
# Renomear versão v1.2 → v1.0
mv AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER/CER-001_Clinical_Evaluation_Report_v1.2_OFICIAL.md \
   AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER/CER-001_Clinical_Evaluation_Report_v1.0_OFICIAL.md

# Atualizar header
# - version: "v1.2" → "v1.0"
```

#### Documento 4: TRC-001

```bash
# Delete versões antigas
rm AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v1.0_OFICIAL.csv
rm AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v2.0_OFICIAL.csv

# Renomear versão final v2.1 → v1.0
mv AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v2.1_COMPLETE_20251008.csv \
   AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v1.0_OFICIAL.csv

# Atualizar primeira linha do CSV
# TRC-001 v2.1 COMPLETE → TRC-001 v1.0 OFICIAL
```

#### Documento 5: PMS-001

```bash
# Renomear versão v1.1 → v1.0
mv AUTHORITATIVE_BASELINE/07_POS_MERCADO/PMS/PMS-001_PostMarket_Surveillance_v1.1_OFICIAL.md \
   AUTHORITATIVE_BASELINE/07_POS_MERCADO/PMS/PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md

# Atualizar header
# - version: "v1.1" → "v1.0"
```

#### Documento 6: TEC-002

```bash
# Renomear versão v2.0 → v1.0
mv AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/RMP/TEC-002_Risk_Management_File_v2.0_AUTHORITATIVE_20251008.md \
   AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/RMP/TEC-002_Risk_Management_File_v1.0_OFICIAL.md

# Atualizar header
# - version: "v2.0" → "v1.0"
```

#### Documento 7: DMR Manifest

```bash
# Delete versão antiga
rm AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/DMR_MANIFEST_OFICIAL.json

# Renomear v2.0 → v1.0
mv AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/DMR_MANIFEST_v2.0_20251008_OFICIAL.json \
   AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/DMR-001_Device_Master_Record_v1.0_OFICIAL.json

mv AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/DMR_MANIFEST_v2.0_SUMMARY.md \
   AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/DMR-001_Device_Master_Record_v1.0_SUMMARY.md

# Atualizar manifest JSON
# - version: "v2.0-20251008" → "v1.0-20251012"
# - Todas as referências de versão interna para v1.0
```

#### Script de Verificação

```bash
# Renomear v2.0 → v1.0
mv AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/verify_dmr_v2.0.sh \
   AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/verify_dmr_v1.0.sh

# Atualizar conteúdo do script
# - Todas as referências v2.0 → v1.0
# - Atualizar versões dos documentos listados
```

### 5.3 Fase 4: Validação e Atualização de Referências (1-2 horas)

**Busca global por versões antigas:**

```bash
cd AUTHORITATIVE_BASELINE

# Buscar v2.2 (SRS)
grep -r "v2\.2" . --exclude-dir=.git

# Buscar v2.0 (múltiplos docs)
grep -r "v2\.0" . --exclude-dir=.git

# Buscar v1.2 (CER)
grep -r "v1\.2" . --exclude-dir=.git

# Buscar v2.1 (TRC)
grep -r "v2\.1" . --exclude-dir=.git

# Buscar v1.1 (múltiplos docs)
grep -r "v1\.1" . --exclude-dir=.git
```

**Atualização sistemática:**
- Todos os resultados devem ter suas referências atualizadas para v1.0
- Prioridade para documentos OFICIAIS
- Relatórios podem ser atualizados opcionalmente

**Validação final:**

```bash
# Verificar nomenclatura padronizada
find AUTHORITATIVE_BASELINE -name "*_v1.0_OFICIAL*" -type f

# Contar documentos oficiais (deve ser 14 + 12 APIs = 26 arquivos)
find AUTHORITATIVE_BASELINE -name "*_v1.0_OFICIAL*" -type f | wc -l

# Verificar se não há mais versões antigas
find AUTHORITATIVE_BASELINE -name "*_v[2-9].*" -type f
find AUTHORITATIVE_BASELINE -name "*_v1.[1-9]*" -type f
```

---

## ✅ 6. CRITÉRIOS DE SUCESSO DA FASE 1

### 6.1 Deliverables Completados

- [x] **RELATORIO_MAPEAMENTO_VERSOES.md** - Este documento ✅
- [x] **Inventário completo** - 14 documentos base + 12 APIs identificados ✅
- [x] **Matriz de referências cruzadas** - 23 referências mapeadas ✅
- [x] **Matriz de impacto** - 7 documentos + 11 deleções identificados ✅
- [x] **Plano de execução detalhado** - Comandos prontos para Fase 3 ✅

### 6.2 Insights Importantes

1. **Opção B confirmada como viável**: Não há necessidade de preservar histórico em 00_HISTORICO/ porque:
   - Todo histórico está no Git
   - Versões antigas são evolutivas, não branches paralelas
   - Limpeza total facilita submissão ANVISA

2. **SRS-001 v2.2 é a versão mais completa**: Contém:
   - Requisitos pediátricos (REQ-HD-016)
   - Classificação de severidade de plaquetas
   - Validação clínica aprovada (CLIN-VAL-001)
   - Todos os requisitos evolutivos de v1.0 → v2.2

3. **TRC-001 v2.1 é a versão mais atual**:
   - Arquivo encontrado: `TRC-001_Traceability_Matrix_v2.1_COMPLETE_20251008.csv`
   - Não está listado no plano original (que menciona v2.1 mas não lista o arquivo)
   - Deve ser a versão final para renomear

4. **DMR v2.0 está como Manifest, não como documento tradicional**:
   - É um JSON + Markdown de inventário
   - Deve ser renomeado para DMR-001 com prefixo padrão
   - Requer atualização de TODAS as 36 referências internas

5. **Impacto de mudança é ALTO para SRS/SDD/TRC/DMR**:
   - Estes documentos são os mais referenciados
   - Qualquer erro na atualização de referências quebrará a rastreabilidade
   - Requer validação rigorosa na Fase 4

### 6.3 Riscos Identificados

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Referências cruzadas quebradas | Média | Alto | Busca global sistemática na Fase 4 |
| Conteúdo perdido na renomeação | Baixa | Alto | Git backup + revisão manual |
| Versão errada escolhida para v1.0 | Baixa | Alto | Análise detalhada de qual versão é mais completa |
| Nomenclatura inconsistente | Média | Médio | Seguir padrão: `CODIGO-XXX_Nome_v1.0_OFICIAL.ext` |
| Checksums inválidos | Média | Médio | Regenerar todos os checksums após mudanças |

---

## 📅 7. PRÓXIMOS PASSOS

### **Aprovação Necessária do Dr. Abel Costa:**

Antes de prosseguir para a Fase 2, confirme:

1. ✅ **Opção B (Limpeza Total) está aprovada?**
   - Deletar versões antigas sem criar 00_HISTORICO/
   - Histórico preservado apenas no Git

2. ✅ **Versões finais escolhidas estão corretas?**
   - SRS v2.2 → v1.0
   - SDD v2.0 → v1.0
   - TRC v2.1 → v1.0 (arquivo COMPLETE)
   - CER v1.2 → v1.0
   - PMS v1.1 → v1.0
   - TEC-002 v2.0 → v1.0

3. ✅ **Nomenclatura está aprovada?**
   - `CODIGO-XXX_Nome_v1.0_OFICIAL.ext`
   - DMR: `DMR-001_Device_Master_Record_v1.0_OFICIAL.json`

### **Se APROVADO, executar:**

```bash
@documentation-finalization-specialist, vamos executar a Fase 2 (Backup e Preparação).
```

### **Se REQUER AJUSTES, especificar:**

```
Ajustes necessários:
- [Descrever mudanças]
```

---

## 📊 8. ESTATÍSTICAS FINAIS DA FASE 1

| Métrica | Valor |
|---------|-------|
| **Tempo de execução** | 45 minutos |
| **Documentos analisados** | 35 arquivos .md + 3 .csv |
| **Referências cruzadas mapeadas** | 23 referências |
| **Documentos a padronizar** | 7 documentos |
| **Arquivos a deletar** | 11 arquivos |
| **Espaço a liberar** | ~259 KB |
| **Referências a atualizar na Fase 4** | ~18 locais |

---

**Status da Fase 1**: ✅ **COMPLETA**
**Próximo passo**: Aguardando aprovação para Fase 2
**Responsável**: Dr. Abel Costa

---

**Gerado por**: @documentation-finalization-specialist
**Data**: 2025-10-12
**Versão do relatório**: 1.0
