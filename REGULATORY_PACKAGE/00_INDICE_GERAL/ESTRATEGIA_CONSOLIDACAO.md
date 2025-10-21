# Estratégia de Consolidação - Dossiê ANVISA Unificado

**Data:** 2025-10-07
**Status:** FASE 1.2 - Mapeamento em andamento
**Objetivo:** Consolidar 3 dossiês fragmentados em 1 oficial para submissão ANVISA

---

## 📊 SITUAÇÃO ATUAL

### Dossiês Identificados:

1. **ROOT** (`/Users/abelcosta/Documents/HemoDoctor/hemodoctor_PJ/`)
   - Arquivos MD v1.0 datados 2025-09-19
   - SRS-001, SDD-001, SEC-001
   - **Características:** Formato markdown, fácil diff, provável versão de trabalho mais recente

2. **Hemodoctor_SaMD_gpt_v1.2**
   - Arquivos DOCX v1.0
   - SRS-001, SDD-001, TEC-001, SEC-001, PMS-001
   - **Características:** Formato binário, precisa conversão, versão GPT-gerada

3. **Projeto/**
   - Arquivos DOCX v1.0 com nomes longos descritivos
   - Inclui CER-001 v1.1 (crítico para RDC 657)
   - **Características:** Nomes detalhados, inclui documentos não encontrados em outros dossiês

4. **HemoDoctor_ANVISA_Submission_Package_20251009**
   - Estrutura organizada por RDC (07_post_market, 08_labeling)
   - Múltiplas versões de PMS-001 (v1.1 provável canônica)
   - IFU-001 v1.0 EN/PT-BR PDFs A4 (versões oficiais)
   - **Características:** Mais recente (2025-10-09), estruturado para submissão

5. **hemodoctor_docs_compilados/**
   - DMR_MANIFEST_final_20250916.json (25 arquivos, SHA256)
   - TRC-001_v1.0_20250917.csv (18 requisitos 100% rastreados)
   - SRS-001 v0.0 (contém declaração Classe C crítica)
   - **Características:** Documentos compilados, checksums, traceability

---

## 🎯 CRITÉRIOS PARA VERSÃO CANÔNICA

### Prioridade de Seleção:

1. **Data mais recente** (desde que completa)
2. **Formato MD > PDF > DOCX** (facilita manutenção e diff)
3. **Conteúdo mais completo** (checksum, diagramas, tabelas)
4. **Conformidade regulatória** (RDC 751/657, IEC 62304 Classe C)
5. **Rastreabilidade** (referências consistentes com TRC-001)

### Decisões Iniciais:

| Documento | Versão Canônica | Justificativa |
|-----------|-----------------|---------------|
| **DMR_MANIFEST** | `final_20250916.json` | 25 arquivos + SHA256, mais completo que v6 |
| **TRC-001** | `v1.0_20250917.csv` | 100% rastreabilidade, única versão encontrada |
| **IFU-001 EN** | `v1.0_A4_20250917.pdf` | PDF oficial, v1.0 final |
| **IFU-001 PT-BR** | `v1.0_A4_20250917.pdf` | PDF oficial, v1.0 final |
| **PMS-001** | `v1.1.md` (Submission Package) | Versão mais recente encontrada |
| **CER-001** | `v1.1.docx` (Projeto/) | ⚠️ Precisa validação @clinical-evidence |
| **SRS-001** | ⚠️ **PENDENTE** | 4 versões - comparar v0.0 vs v1.0 |
| **SDD-001** | ⚠️ **PENDENTE** | 3 versões - validar diagramas Classe C |
| **TEC-001** | ⚠️ **PENDENTE** | 2 versões DOCX - validar build procedures |
| **SEC-001** | ⚠️ **PENDENTE** | 3 versões - validar SBOM e §524B |

---

## 📋 PRÓXIMAS AÇÕES

### FASE 1.2 - Comparação de Versões:

#### 1. **SRS-001 (Software Requirements Specification)**

**Versões encontradas:**
- `ROOT/SRS-001_v1.0_20250919.md` (data: 19/09)
- `Hemodoctor_SaMD_gpt_v1.2/SRS-001_v1.0.docx`
- `Projeto/SRS-001_v1.0.docx`
- `hemodoctor_docs_compilados/SRS-001_v0.0_20250916.md` (contém declaração Classe C)

**Ações:**
1. Ler e comparar conteúdo de todas as 4 versões
2. Verificar se v1.0 inclui declaração Classe C (presente em v0.0)
3. Contar requisitos em cada versão (comparar com 18 em TRC-001)
4. Validar referências cruzadas com SDD-001 e TRC-001
5. **Decisão:** Escolher canônica ou MERGE se necessário

#### 2. **SDD-001 (Software Design Document)**

**Versões encontradas:**
- `ROOT/SDD-001_v1.0_20250919.md`
- `Hemodoctor_SaMD_gpt_v1.2/SDD-001_v1.0.docx`
- `Projeto/SDD-001_v1.0.docx`

**Ações:**
1. Comparar diagramas de arquitetura entre versões
2. Validar segregação de componentes Classe C (IEC 62304 §5.3.1)
3. Verificar se há "TEC-001_Diagram_Global_Architecture_20250916.png"
4. Contar componentes e interfaces
5. Validar referências com SRS-001 (FR-001 a FR-004)

#### 3. **TEC-001 (Software Development Plan)**

**Versões encontradas:**
- `Hemodoctor_SaMD_gpt_v1.2/TEC-001_v1.0.docx`
- `Projeto/TEC-001_v1.0.docx`

**Ações:**
1. Converter DOCX para MD (ambas versões)
2. Comparar build procedures e release procedures
3. Verificar Configuration Management Plan
4. Validar Maintenance Plan (gap identificado por @traceability)
5. Escolher mais completo ou MERGE

#### 4. **SEC-001 (Cybersecurity)**

**Versões encontradas:**
- `ROOT/SEC-001_v1.0_20250919.md`
- `Hemodoctor_SaMD_gpt_v1.2/SEC-001_v1.0.docx`
- `Projeto/SEC-001_v1.0.docx` (inclui DPIA/LGPD)

**Ações:**
1. Comparar SBOM entre versões
2. Validar §524B compliance (FDA cybersecurity)
3. Verificar se DPIA/LGPD está em versão Projeto
4. Validar threat model e incident response plan
5. **IMPORTANTE:** Versão Projeto pode ter conteúdo único (LGPD)

---

## 🚨 GAPS CRÍTICOS IDENTIFICADOS

### 1. **SOUP Analysis** ❌ AUSENTE
- **Status:** NÃO ENCONTRADO em nenhum dossiê
- **Requisito:** IEC 62304 §5.3.4 (obrigatório Classe C)
- **Ação:** CRIAR do zero (2-3 horas)
- **Prioridade:** BLOQUEADOR

### 2. **Architecture Diagrams** ⚠️ PENDENTE VALIDAÇÃO
- **Status:** TEC-001_Diagram_Global_Architecture_20250916.png encontrado
- **Requisito:** IEC 62304 §5.3.1 (segregação Classe C)
- **Ação:** Validar com @software-architecture-specialist
- **Prioridade:** ALTA

### 3. **CER-001 Clinical Evidence** ⚠️ PENDENTE VALIDAÇÃO
- **Status:** v1.1 encontrado
- **Requisito:** RDC 657/2022 (obrigatório Classe III)
- **Ação:** Validar com @clinical-evidence-specialist
- **Prioridade:** CRÍTICA

---

## 🔄 WORKFLOW DE CONSOLIDAÇÃO

### Passo a Passo:

1. **Leitura e Comparação**
   - Ler todas as versões de cada documento
   - Gerar tabela comparativa (tamanho, data, seções, referências)

2. **Análise de Completude**
   - Contar requisitos, riscos, testes, componentes
   - Verificar checklist IEC 62304/RDC 751
   - Identificar seções únicas em cada versão

3. **Decisão de Versão Canônica**
   - Aplicar critérios de prioridade
   - Se necessário, MERGE de seções de múltiplas versões
   - Documentar decisão com justificativa

4. **Conversão e Normalização**
   - Converter DOCX → Markdown (pandoc)
   - Normalizar formato (cabeçalhos, tabelas, referências)
   - Atualizar referências cruzadas

5. **Validação Cruzada**
   - Verificar consistência com TRC-001
   - Validar referências SRS → SDD → Test Reports
   - Executar checklist de completude

6. **Empacotamento Final**
   - Copiar para estrutura unificada
   - Gerar checksums SHA256
   - Atualizar DMR_MANIFEST

---

## 📅 CRONOGRAMA

### FASE 1.2 - Mapeamento e Comparação (1 dia)
- ✅ Criar estrutura dossiê unificado
- ✅ Criar MAPEAMENTO_FONTE_DESTINO.csv
- ⏳ **AGORA:** Comparar SRS-001 (4 versões)
- ⏳ Comparar SDD-001 (3 versões)
- ⏳ Comparar TEC-001 (2 versões)
- ⏳ Comparar SEC-001 (3 versões)
- ⏳ Definir versões canônicas finais

### FASE 2.1 - Consolidação Core (2 dias)
- Executar merge de documentos
- Converter DOCX → MD
- Validar referências cruzadas
- Criar SOUP Analysis

### FASE 2.2 - Validação Especializada (2 dias)
- @software-architecture-specialist (SDD-001)
- @clinical-evidence-specialist (CER-001)
- @risk-management-specialist (RMP-001)

### FASE 3 - Empacotamento (1 dia)
- Copiar para estrutura final
- Gerar checksums
- Atualizar DMR_MANIFEST
- Review final com @anvisa-regulatory-specialist

---

## 💡 RECOMENDAÇÕES

### Automatização:
- Script Python para comparação de MD files (diff, word count, section count)
- Pandoc batch conversion DOCX → MD
- SHA256 checksum generator
- Cross-reference validator (REQ-ID, RISK-ID, TEST-ID)

### Validação Manual Necessária:
- ❗ Diagramas de arquitetura (formato visual)
- ❗ Conteúdo clínico (CER-001)
- ❗ SBOM e análise de ameaças (SEC-001)
- ❗ Procedures de build/release (TEC-001)

### Pontos de Atenção:
- ⚠️ SRS-001 v0.0 tem declaração Classe C crítica - verificar se v1.0 mantém
- ⚠️ Projeto/SEC-001 pode ter DPIA/LGPD único - não perder
- ⚠️ IFU-001 v1.2 MD existe mas v1.0 PDF é oficial - verificar qual usar
- ⚠️ 169 grupos de duplicados ainda pendentes - priorizar após core docs

---

**Próximo passo:** Comparar SRS-001 (4 versões) e escolher/merge versão canônica
