# HemoDoctor - Dossiê ANVISA Unificado

**Produto:** HemoDoctor SaMD
**Classe:** ANVISA Classe III / FDA Classe III
**Fabricante:** [Nome da empresa]
**Versão do Software:** 1.0.0
**Data de Criação do Dossiê:** 2025-10-07
**Status:** Em Consolidação

---

## 📋 ÍNDICE GERAL

### 00. ÍNDICE GERAL
- Este documento (README.md)
- Histórico de Versões
- Guia de Navegação

### 01. REGULATÓRIO
**Objetivo:** Documentação regulatória e declarações de conformidade

- `DMR_MANIFEST.json` - Device Master Record oficial
- Declarações de conformidade (IEC 62304, ISO 14971, ISO 13485)
- Certificados de qualidade
- Correspondências regulatórias

**Documentos Chave:**
- DMR_MANIFEST_final_20250916.json (25 arquivos, SHA256 checksums)

### 02. CONTROLES DE DESIGN
**Objetivo:** Ciclo de vida de desenvolvimento IEC 62304 Classe C

#### SRS - Software Requirements Specification
- `SRS-001_Software_Requirements_v0.0_20250916.md`
- Requisitos funcionais (FR-001 a FR-004)
- Requisitos não-funcionais (latência, uptime, auditoria)
- Cybersecurity §524B compliance

#### SDD - Software Design Document
- `SDD-001_Software_Design_v1.0.md`
- Arquitetura de componentes (Classe C segregation)
- Diagramas de fluxo de dados
- Especificações de interfaces

#### TEC - Software Development Plan
- `TEC-001_Software_Development_Plan_v1.0.md`
- Processo de desenvolvimento
- Ferramentas e ambiente
- Controle de versão e configuração
- Procedimentos de build/release

#### Arquitetura
- Diagramas de arquitetura global
- Diagramas de componentes
- Diagramas de deployment

**Status Atual:** Documentos existem mas fragmentados em 3 dossiês

### 03. GESTÃO DE RISCO
**Objetivo:** ISO 14971 Risk Management

- `RMP-001` - Risk Management Plan
- `RISK-ANALYSIS` - Análise de riscos (FMEA)
- Matrizes de risco
- Plano de mitigação

**Rastreabilidade:** Linkado a TRC-001 (100% dos requisitos têm riscos mapeados)

### 04. VERIFICAÇÃO E VALIDAÇÃO
**Objetivo:** IEC 62304 §5.5-5.8, evidências de testes

- `VVP-001` - Verification & Validation Plan
- Test Reports (TEST-HD-004 a TEST-HD-016)
- Cobertura de testes (unit, integration, system)
- ROC/PR curves, confusion matrix

**Status:** 100% cobertura em TRC-001

### 05. AVALIAÇÃO CLÍNICA
**Objetivo:** RDC 657/2022 Clinical Evidence

- `CER-001` - Clinical Evaluation Report (v1.0, v1.1, v1.2 encontrados)
- Literatura científica de suporte
- Evidências clínicas de performance
- Estudos de validação clínica

**Requisito ANVISA:** Obrigatório para Classe III

### 06. RASTREABILIDADE
**Objetivo:** Demonstrar completude end-to-end

- `TRC-001_Traceability_Matrix_v1.0_20250917.csv`
  - 18 requisitos mapeados
  - 100% cobertura: User_Need → REQ → Design → Test → Risk → Label → PMS
  - Exemplo: REQ-HD-001 (Sensibilidade ≥0.90) → SDD-001 §3.2 → TEST-HD-011 → RISK-HD-001 → IFU-001 §Performance → PMS-001 §SLAs

**Status:** 100% dos requisitos rastreados, mas SRS-001 contém requisitos adicionais não em TRC-001

### 07. PÓS-MERCADO
**Objetivo:** Vigilância e monitoramento contínuo

- `PMS-001` - Post-Market Surveillance Plan
- Procedimentos de vigilância
- Mecanismos de feedback
- SLAs e KPIs de monitoramento

### 08. ROTULAGEM
**Objetivo:** IFU, labels, instruções de uso

- `IFU-001` - Instructions for Use
- Labels e advertências
- Manual do usuário
- Informações de segurança

### 09. CYBERSECURITY
**Objetivo:** FDA §524B Cybersecurity compliance

- `SEC-001` - Cybersecurity documentation
- `SBOM` - Software Bill of Materials
- Análise de vulnerabilidades
- Plano de resposta a incidentes

### 10. SOUP (Software of Unknown Provenance)
**Objetivo:** IEC 62304 §5.3.4, análise de componentes third-party

- **STATUS:** ⚠️ GAP CRÍTICO IDENTIFICADO
- Análise de bibliotecas open-source
- Avaliação de riscos de dependências
- Plano de manutenção de SOUP

**Tempo Estimado:** 2-3 horas para criação

---

## 📊 STATUS DE CONSOLIDAÇÃO

### Fonte de Documentos (3 Dossiês):

1. **`@hemodoctor/dossier-anvisa-claude/`** (40+ docs, 95% completo)
2. **`HemoDoctor_ANVISA_Submission_Package_20251009/`** (mais recente)
3. **`HemoDoctor_Dossier_v0_BR/`** (estruturado por RDC)

### Inventário:
- **Total de arquivos:** 890 files
- **Documentos duplicados:** 189 grupos identificados
- **DMR versions:** 9 versões (oficial: DMR_MANIFEST_final_20250916.json)

### Avaliação Atual:
- **Status:** CONDITIONAL GO - 70% completo
- **Problema:** FRAGMENTAÇÃO (não ausência)
- **Solução:** Consolidação de 3 dossiês em 1 oficial

### Gaps Identificados:

#### 🔴 CRÍTICO (Bloqueador):
- ❌ **SOUP Analysis** (IEC 62304 §5.3.4) - 2-3 horas

#### 🟡 IMPORTANTE (Consolidação necessária):
- ⚠️ **SRS/SDD/TEC-001** - Versões múltiplas precisam consolidação
- ⚠️ **CER-001** - Precisa validação RDC 657 com @clinical-evidence-specialist
- ⚠️ **Architecture Diagrams** - Validar segregação Classe C

---

## 🎯 PLANO DE CONSOLIDAÇÃO (12 dias)

### FASE 1: Estrutura Unificada (2 dias) ✅ EM ANDAMENTO
- [x] Criar estrutura de pastas ANVISA oficial
- [x] Definir índice geral
- [ ] Mapear documentos dos 3 dossiês → estrutura unificada
- [ ] Identificar versões canônicas (latest + completo)

### FASE 2: Consolidação Core (5 dias)
- [ ] Consolidar SRS-001 (todas as versões → v1.0 oficial)
- [ ] Consolidar SDD-001 (validar diagramas Classe C)
- [ ] Consolidar TEC-001 (integrar build/release procedures)
- [ ] **CRIAR SOUP Analysis** (2-3 horas)
- [ ] Consolidar CER-001 (validação RDC 657)
- [ ] Automatizar consolidação 169 grupos duplicados

### FASE 3: Validação Final (5 dias)
- [ ] Review com @software-architecture-specialist
- [ ] Review com @risk-management-specialist
- [ ] Review com @clinical-evidence-specialist
- [ ] Review com @anvisa-regulatory-specialist
- [ ] Checklist ANVISA RDC 751/657
- [ ] Packaging final + checksums
- [ ] DMR MANIFEST oficial atualizado

---

## 🔍 PRÓXIMOS PASSOS

**AGORA (FASE 1.2):**
1. Criar documento de mapeamento `MAPEAMENTO_FONTE_DESTINO.csv`
2. Escanear 3 dossiês e mapear cada arquivo → pasta de destino
3. Identificar versões canônicas (critério: data + completude)
4. Gerar plano de consolidação por grupo de documentos

**DEPOIS (FASE 2.1):**
1. Executar consolidação de SRS/SDD/TEC/CER
2. Criar SOUP Analysis do zero
3. Validar com agentes especialistas

---

## 📚 REFERÊNCIAS REGULATÓRIAS

- **ANVISA RDC 751/2022** - Produtos para saúde de software
- **ANVISA RDC 657/2022** - Requisitos de evidências clínicas
- **IEC 62304:2006/Amd 1:2015** - Medical device software lifecycle (Classe C)
- **ISO 14971:2019** - Risk management for medical devices
- **ISO 13485:2016** - Quality management systems
- **FDA 21 CFR Part 820** - Quality System Regulation
- **FDA §524B** - Cybersecurity requirements

---

**Mantido por:** Abel Costa
**Última atualização:** 2025-10-07 22:15 BRT
**Versão do dossiê:** 1.0.0-consolidation
**Investimento regulatório:** R$ 1.5M+ em ativos
