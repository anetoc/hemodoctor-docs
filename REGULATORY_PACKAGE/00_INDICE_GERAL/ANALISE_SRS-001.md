# Análise Comparativa: SRS-001 (Software Requirements Specification)

**Data:** 2025-10-07
**Objetivo:** Identificar versão canônica ou necessidade de merge

---

## 📊 VERSÕES IDENTIFICADAS

### 1. SRS-001 v0.0 (20250916) - MD
**Path:** `hemodoctor_docs_compilados/SRS-001_Software_Requirements_v0.0_20250916.md`
**Tamanho:** 39 linhas
**Formato:** Markdown

**Pontos Fortes:**
- ✅ **CRÍTICO:** Declaração explícita "Class C (IEC 62304)" no §1 Scope
- ✅ Estrutura regulatória completa (9 seções)
- ✅ Mapeamento User Needs → Requirements (UN-001 a UN-005)
- ✅ Linkagem com outros docs (SDD-001, TST-001, IFU-001, PMS-001, RISK-002)
- ✅ Seção Safety & Risk Controls (ISO 14971)
- ✅ Seção Cybersecurity (FDA §524B)
- ✅ Seção Traceability (REQ ↔ Design ↔ Tests ↔ Label ↔ PMS)

**Pontos Fracos:**
- ⚠️ Requisitos menos detalhados (FR-001 a FR-004 genéricos)
- ⚠️ Falta detalhes técnicos de CBC (variáveis, unidades, LOINC)
- ⚠️ Versão v0.0 (draft inicial)

**Requisitos:**
- FR-001: Compute risk score and Top-N suggestions
- FR-002: Display rationale/uncertainty and clinician override
- FR-003: Record decisions and feedback (audit trail)
- FR-004: Export reports and API access (FHIR/REST)
- NFR-001 a NFR-004: Performance, uptime, audit, privacy

---

### 2. SRS-001 v1.0 (20250919) - MD
**Path:** `ROOT/SRS-001_v1.0_20250919.md`
**Tamanho:** 45 linhas
**Formato:** Markdown

**Pontos Fortes:**
- ✅ Versão v1.0 (mais recente)
- ✅ Requisitos técnicos MUITO mais detalhados (REQ-HD-001 a REQ-HD-005)
- ✅ Detalhes de CBC: Hb, Ht, VCM, RDW, leucócitos, plaquetas, reticulócitos
- ✅ Complementares: ferritina, ferro, B12, folato, LDH, marcadores hemólise
- ✅ Padronização LOINC mencionada
- ✅ Dicionário de dados completo
- ✅ Tabela de Normas/Guias aplicáveis
- ✅ REQ-HD-001: "anemia grave (Hb abaixo de limiar) com **sensibilidade 100%**" - Meta crítica!

**Pontos Fracos:**
- ❌ **CRÍTICO:** FALTA declaração "Class C (IEC 62304)" no início
- ⚠️ Menos estruturado para regulatório (falta seções Safety, Cyber detalhadas)
- ⚠️ Não mapeia User Needs explicitamente
- ⚠️ Falta linkagem com outros documentos (SDD, TST, IFU, PMS)

**Requisitos:**
- REQ-HD-001: Identificar anemia grave (Hb < limiar) com sensibilidade 100%
- REQ-HD-002: Ingestão CBC + complementares com validação de unidades
- REQ-HD-003: Exibir racional clínico (regras e fontes)
- REQ-HD-004: Exportar logs auditáveis (WORM)
- REQ-HD-005: API REST para integração LIS/HIS (OIDC/OAuth2)

---

### 3. SRS-001 v1.0 - DOCX (Hemodoctor_SaMD_gpt_v1.2)
**Path:** `Hemodoctor_SaMD_gpt_v1.2/SRS-001_v1.0.docx`
**Formato:** DOCX (binário)
**Status:** ⏳ Pendente conversão

**Ação:** Converter para MD com pandoc para comparar

---

### 4. SRS-001 v1.0 - DOCX (Projeto)
**Path:** `Projeto/SRS-001_ Especificação de Requisitos de Software v1.0.docx`
**Formato:** DOCX (binário)
**Status:** ⏳ Pendente conversão

**Ação:** Converter para MD com pandoc para comparar

---

## 🎯 DECISÃO PRELIMINAR: **MERGE NECESSÁRIO**

### Justificativa:

Nenhuma versão MD isolada é suficiente:

1. **v0.0 tem estrutura regulatória essencial:**
   - Declaração Class C (BLOQUEADOR se faltar)
   - Seções de Safety, Cyber, Traceability
   - Linkagem entre documentos

2. **v1.0 tem conteúdo técnico crítico:**
   - Requisitos detalhados (REQ-HD-001 a 005)
   - Meta de sensibilidade 100% para anemia grave
   - Dicionário de dados CBC completo
   - LOINC padronização

### Estratégia de MERGE:

**Base:** v0.0 (estrutura regulatória)

**Incorporar de v1.0:**
1. Requisitos REQ-HD-001 a REQ-HD-005 (substituir FR-001 a FR-004)
2. Seção "Dados e Dicionário" completa (CBC + complementares)
3. Detalhes de validação de unidades e faixas por perfil
4. Tabela de Normas/Guias aplicáveis

**Manter de v0.0:**
1. **CRÍTICO:** "Class C (IEC 62304)" no Scope
2. Mapeamento User Needs (UN-001 a UN-005)
3. Seção Safety & Risk Controls
4. Seção Cybersecurity (§524B detalhada)
5. Seção Traceability

**Resultado esperado:**
- SRS-001 v1.0 OFICIAL (merged)
- ~80-90 linhas
- 100% compliance IEC 62304 Classe C + RDC 751

---

## 📋 CHECKLIST DE COMPLETUDE (IEC 62304 §5.2)

| Seção | v0.0 | v1.0 | Merged |
|-------|------|------|--------|
| **1. Scope & Class declaration** | ✅ Class C | ❌ Falta | ✅ |
| **2. User Needs → Requirements** | ✅ UN-001 a UN-005 | ⚠️ Implícito | ✅ |
| **3. Functional Requirements** | ⚠️ FR-001 a FR-004 genéricos | ✅ REQ-HD-001 a 005 detalhados | ✅ |
| **4. Non-functional Requirements** | ✅ NFR-001 a NFR-004 | ⚠️ Menos estruturado | ✅ |
| **5. Data Dictionary** | ❌ Falta | ✅ CBC completo | ✅ |
| **6. Interfaces** | ✅ FHIR/REST | ✅ REST/JSON + LIS | ✅ |
| **7. Safety & Risk Controls** | ✅ ISO 14971 linkage | ⚠️ Implícito | ✅ |
| **8. Cybersecurity** | ✅ §524B detalhado | ⚠️ Menos detalhado | ✅ |
| **9. Verification criteria** | ✅ Link to TEST-HD | ✅ Mapeado a TRC | ✅ |
| **10. Traceability** | ✅ REQ↔Design↔Test↔Label↔PMS | ⚠️ Falta | ✅ |

**Score:**
- v0.0: 8/10 (estrutura, falta detalhes técnicos)
- v1.0: 6/10 (detalhes técnicos, falta estrutura regulatória)
- **Merged: 10/10** ✅

---

## ⏭️ PRÓXIMAS AÇÕES

### 1. Converter DOCX para MD
```bash
pandoc -s "Hemodoctor_SaMD_gpt_v1.2/SRS-001_v1.0.docx" -o "temp/SRS-001_gpt_v1.0.md"
pandoc -s "Projeto/SRS-001_ Especificação de Requisitos de Software v1.0.docx" -o "temp/SRS-001_projeto_v1.0.md"
```

### 2. Comparar DOCX convertidos com MD
- Verificar se há conteúdo único em DOCX
- Identificar se há versões mais recentes escondidas

### 3. Executar MERGE
- Criar SRS-001_v1.0_MERGED.md
- Revisar com @software-architecture-specialist
- Validar referências cruzadas com TRC-001

### 4. Validar Requisitos vs TRC-001
- TRC-001 tem 18 requisitos mapeados
- SRS merged deve conter TODOS os 18 + justificar ausentes
- Verificar REQ-HD-001 a REQ-HD-005 vs REQ-HD-001 em TRC-001

---

## 🚨 BLOQUEADORES IDENTIFICADOS

### CRITICAL:
- ❌ Sem declaração "Class C" em v1.0 → **INSUBMISSÍVEL sem correção**
- ⚠️ Inconsistência de IDs: FR-001 vs REQ-HD-001 → TRC-001 usa qual?

### IMPORTANTE:
- ⚠️ TRC-001 menciona REQ-HD-001 (Sensibilidade ≥0.90) mas v1.0 MD diz "100%" → Qual é correto?
- ⚠️ User Needs não mapeados em v1.0 → RDC 751 §3.1 pode exigir

---

**Recomendação:** Executar MERGE v0.0 + v1.0, depois validar com @traceability-specialist
