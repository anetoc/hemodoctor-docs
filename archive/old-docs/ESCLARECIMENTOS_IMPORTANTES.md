# 📋 ESCLARECIMENTOS IMPORTANTES - HemoDoctor Project

**Data:** 19 de Outubro de 2025 - 21:00 BRT
**Fonte:** Dr. Abel Costa
**Contexto:** Análise documentos consolidados

---

## 🎯 ESCLARECIMENTO 1: Dados Fictícios (MODELO/TEMPLATE)

### Status Atual dos Dados

**IMPORTANTE:** Todos os dados de estudos clínicos mencionados nos documentos são **FICTÍCIOS** e servem APENAS como **MODELO/TEMPLATE**.

**Documentos Afetados:**
- CER-001 (Clinical Evaluation Report): N=4,370 casos → **FICTÍCIO**
- PROJ-001 (Clinical Protocol): N=2,900 casos → **FICTÍCIO**
- CLIN-VAL-001 (Clinical Validation): 7 casos validados → **FICTÍCIO**
- Test cases: 95 test cases, 72% pass rate → **FICTÍCIO**

### Propósito dos Dados Fictícios

✅ **Servem como:**
- Template de estrutura documental (formato, seções, métricas)
- Referência de compliance regulatório (ANVISA/FDA/ISO)
- Modelo de rastreabilidade (REQ → Design → Code → Test)
- Exemplo de métricas esperadas (pass rate, coverage, sensitivity)

❌ **NÃO devem ser usados para:**
- Submissão regulatória real
- Validação clínica real
- Claims de performance (sensibilidade, especificidade)
- Treinamento de modelos ML

---

## 🎯 ESCLARECIMENTO 2: Base de Dados Real do MVP (FUTURO)

### Dados Reais Pendentes

**Dr. Abel tem uma base de dados REAL do MVP** que será fornecida posteriormente para:

1. **Testes com dados reais** (substituir dados fictícios)
2. **Validação clínica real** (Red List FN=0, sensibilidade ≥90%)
3. **Calibração do modelo** (Platt scaling, confidence scores)
4. **Performance real** (pass rate, coverage, métricas reais)

### Workflow Planejado

```
┌─────────────────────────────────────────────────────────┐
│ FASE ATUAL: Especificação + Mock Data (FICTÍCIO)       │
├─────────────────────────────────────────────────────────┤
│ ✅ YAMLs 15 módulos (7,350 linhas) - ESPECIFICAÇÃO     │
│ ✅ Documentação completa (baseline + consolidados)      │
│ ✅ Estrutura de testes (template)                       │
│ ⚠️ Dados fictícios (MODELO apenas)                      │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│ PRÓXIMA FASE: Testes com Dados Reais do MVP            │
├─────────────────────────────────────────────────────────┤
│ 1. Dr. Abel fornece base real do MVP                   │
│ 2. Executar pipeline com dados reais                   │
│ 3. Validar Red List FN=0 (8 síndromes críticas)        │
│ 4. Medir performance real (sens, spec, pass rate)      │
│ 5. Calibrar modelo (Platt scaling)                     │
│ 6. Gerar relatórios reais (CLIN-VAL-002, TESTREP)      │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 ESCLARECIMENTO 3: YAMLs como Fonte de Verdade ⭐

### Modelo HÍBRIDO = Análise Completa de TODOS os Documentos

**CRÍTICO:** Os **15 módulos YAML do HEMODOCTOR_HIBRIDO_V1.0** foram construídos **COM ANÁLISE DE TODOS OS DOCUMENTOS EXISTENTES**.

**Isso significa:**

✅ **YAMLs já incorporam:**
- Análise de 67+ documentos do AUTHORITATIVE_BASELINE
- Análise de documentos consolidados (18 Out)
- Análise de múltiplas versões de cada documento
- Conhecimento clínico hematológico consolidado
- Requirements regulatórios (ANVISA/FDA/ISO)
- Estrutura de decisão clínica otimizada

✅ **YAMLs são a ESPECIFICAÇÃO MASTER:**
```
DOCUMENTOS (67 baseline + 10 consolidados)
           ↓
    ANÁLISE COMPLETA
           ↓
  📁 15 YAMLs (7,350 linhas) ⭐ FONTE DE VERDADE
           ↓
     IMPLEMENTAÇÃO
```

### Hierarquia de Prioridade

| Nível | Artefato | Status | Uso |
|-------|----------|--------|-----|
| **1** | **15 YAMLs Hybrid V1.0** ⭐ | MASTER | **Especificação autoritativa** |
| 2 | AUTHORITATIVE_BASELINE | Referência | Rastreabilidade + Compliance |
| 3 | Documentos Consolidados | Referência | Melhorias pontuais |
| 4 | Código implementado | Derivado | Implementa YAMLs |
| 5 | Testes | Derivado | Valida YAMLs |

**Regra de Ouro:**
> **Em caso de conflito, YAMLs prevalecem sobre documentos.**

---

## 🎯 ESCLARECIMENTO 4: Estrutura de Decisão e Modelo

### Modelo a Seguir

**IMPORTANTE:** A estrutura de decisão e modelo **DEVEM SEGUIR** o que foi feito **POR ÚLTIMO** = **15 YAMLs Hybrid V1.0**

**Módulos YAML (estrutura master):**

```yaml
00_config_hybrid.yaml           # Cutoffs, unidades, normalização
01_schema_hybrid.yaml           # Schema canônico INPUT/OUTPUT
02_evidence_hybrid.yaml         # 75 evidências atômicas (E-XXX)
03_syndromes_hybrid.yaml        # 34 síndromes (S-XXX) + DAG fusion
04_output_templates_hybrid.yaml # Templates markdown/HTML/JSON/FHIR
05_missingness_hybrid_v2.3.yaml # Proxy logic + always-output
06_route_policy_hybrid.yaml     # Deterministic routing + SHA256
07_conflict_matrix_hybrid.yaml  # Resolução de conflitos
07_normalization_heuristics.yaml # Site-specific normalization
08_wormlog_hybrid.yaml          # WORM audit log (HMAC-SHA256)
09_next_steps_engine_hybrid.yaml # 34 triggers clinical next steps
10_runbook_hybrid.yaml          # Implementation roadmap (8-14 weeks)
11_case_state_hybrid.yaml       # State machine (5 states)
12_output_policies_hybrid.yaml  # Output orchestration
```

### Pipeline de Decisão (Master)

```
CBC Input (CSV/HL7/JSON)
  ↓
[00_config] Normalization (site-specific heuristics)
  ↓
[01_schema] Validation (canonical schema)
  ↓
[02_evidence] Evidence evaluation (75 rules → E-XXX)
  ↓
[03_syndromes] DAG fusion (34 syndromes → S-XXX)
  ↓
[05_missingness] Proxy logic + guaranteed output
  ↓
[06_route_policy] Precedence + route_id (SHA256)
  ↓
[09_next_steps] Prioritized clinical recommendations
  ↓
[12_output] Card rendering (markdown/HTML/JSON/FHIR)
  ↓
[08_wormlog] Immutable audit log (HMAC)
```

**Esta é a estrutura DEFINITIVA** que deve ser implementada.

---

## 🎯 ESCLARECIMENTO 5: Correções nos YAMLs SÃO PERMITIDAS

### YAMLs São "Living Documents"

**IMPORTANTE:** Embora YAMLs sejam a fonte de verdade, **CORREÇÕES SÃO PERMITIDAS** quando:

✅ **Correções Permitidas:**
1. **Bugs técnicos** (ex: BUG-005 - WORM retention 90d → 1825d)
2. **Bugs clínicos** (ex: BUG-006 - E-HB-HIGH, E-WBC-LOW ausentes)
3. **Bugs lógicos** (ex: BUG-002 - age boundaries `<` → `<=`)
4. **Melhorias de especificação** (ex: adicionar evidências/síndromes)
5. **Ajustes regulatórios** (ex: compliance ANVISA/FDA)

❌ **Mudanças NÃO Permitidas:**
1. Alterar arquitetura fundamental (15 módulos)
2. Mudar pipeline de decisão (normalization → evidence → syndrome → output)
3. Remover funcionalidades críticas (WORM log, audit trail, always-output)
4. Violar standards regulatórios (IEC 62304, ANVISA RDC 657/751)

### Workflow de Correção de YAMLs

```
1. Identificar bug/gap no YAML
   ↓
2. Documentar em BUGS.md (BUG-XXX)
   ↓
3. Propor correção (manter estrutura YAML)
   ↓
4. Validar correção (testes + revisão clínica)
   ↓
5. Atualizar YAML (versão minor bump)
   ↓
6. Atualizar rastreabilidade (TRC-001)
   ↓
7. Regenerar testes (se aplicável)
```

---

## 📊 IMPACTO NOS TRABALHOS EM ANDAMENTO

### Análise Multi-Agente (19 Out 2025)

**Resultado da análise permanece VÁLIDO**, mas com **nova interpretação:**

| Achado Original | Nova Interpretação |
|-----------------|-------------------|
| SRS-001 v3.0 superior ao baseline | ✅ Útil para rastreabilidade, mas YAMLs prevalecem |
| Rastreabilidade 98.5% | ✅ Importante para compliance regulatório |
| Compliance 91% | ✅ Crítico para submissão ANVISA |
| V&V 65% (dados fictícios) | ⚠️ Será refeito com dados reais do MVP |
| Pass rate 72% | ⚠️ FICTÍCIO - aguardar dados reais |
| Red List não validado | ⚠️ Será validado com dados reais do MVP |

### Prioridades Ajustadas

**P0 - HOJE (45 min) - MANTÉM:**
1. ✅ Extrair código ZIP (10 min) - BUG-001
2. ✅ Implementar Bug #2 (30 min) - BUG-002
3. ✅ Corrigir WORM retention (5 min) - BUG-005

**P1 - Esta Semana - AJUSTA:**
4. ✅ Integrar SRS-001 v3.0 (rastreabilidade)
5. ⚠️ Verificar TEC-002 v2.0 (RMP-001) - **MENOS URGENTE** (YAMLs têm risk logic)
6. ✅ Corrigir BUG-006 (E-HB-HIGH, E-WBC-LOW) nos YAMLs

**P2 - Aguardar Dados Reais do MVP:**
7. ⏳ Executar pipeline com dados reais
8. ⏳ Validar Red List FN=0 (dados reais)
9. ⏳ Medir performance real (sens, spec)
10. ⏳ Gerar CLIN-VAL-002 com dados reais

---

## 🎯 DECISÕES ATUALIZADAS

### ADR-003: YAMLs como Fonte de Verdade ⭐

**Status:** ✅ APROVADO (Dr. Abel)

**Decisão:**
> Os **15 módulos YAML do HEMODOCTOR_HIBRIDO_V1.0** são a **especificação master autoritativa** do sistema, pois foram construídos COM ANÁLISE DE TODOS OS DOCUMENTOS.

**Consequências:**
1. Em caso de conflito: YAMLs prevalecem sobre documentos
2. Documentos (baseline + consolidados) são para rastreabilidade/compliance
3. Implementação DEVE seguir YAMLs fielmente
4. Correções nos YAMLs são permitidas (bugs, gaps, melhorias)

**Aprovador:** Dr. Abel Costa
**Data:** 19 Out 2025

---

### ADR-004: Dados Fictícios vs Reais

**Status:** ✅ APROVADO (Dr. Abel)

**Decisão:**
> Todos os dados de estudos clínicos atuais são **FICTÍCIOS** e servem como **MODELO/TEMPLATE**. Testes reais serão executados com **base de dados real do MVP** fornecida posteriormente.

**Consequências:**
1. CER-001, PROJ-001, CLIN-VAL-001: métricas são TEMPLATE
2. Pass rate, coverage, sensitivity: FICTÍCIOS
3. Red List validation: será refeita com dados reais
4. Submissão ANVISA: aguarda validação com dados reais

**Aprovador:** Dr. Abel Costa
**Data:** 19 Out 2025

---

## 📋 AÇÕES IMEDIATAS ATUALIZADAS

### HOJE (19 Out - 45 min) - P0

```bash
# 1. Extrair código ZIP (10 min) - BUG-001
cd /Users/abelcosta/Documents/HemoDoctor/docs/
unzip /Users/abelcosta/Documents/HemoDoctor/HemoDoctor_BACKUP_20251016/HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip -d HEMODOCTOR_CONSOLIDADO_v2.0_20251010/

# 2. Corrigir WORM retention nos YAMLs (5 min) - BUG-005
# Editar: HEMODOCTOR_HIBRIDO_V1.0/YAMLs/08_wormlog_hybrid.yaml
# Linha 118: days: 90 → days: 1825

# 3. Implementar Bug #2 no código (30 min) - BUG-002
# Seguir: GUIA_IMPLEMENTACAO_BUG002.md
# platelet_severity_classifier.py: < → <= (6 mudanças)
```

### ESTA SEMANA (20-26 Out) - P1

```bash
# 4. Corrigir BUG-006 nos YAMLs (3h)
# Adicionar em 02_evidence_hybrid.yaml:
#   - E-HB-HIGH (para S-PV Policitemia Vera)
#   - E-WBC-LOW (para S-PANCYTOPENIA)

# 5. Atualizar 03_syndromes_hybrid.yaml:
#   - S-PV: combine.all = ["E-HB-HIGH"]
#   - S-PANCYTOPENIA: combine.all = ["E-HB-LOW", "E-WBC-LOW", "E-PLT-LOW"]

# 6. Atualizar rastreabilidade (TRC-001) - 4-8h
# Adicionar mapeamento REQ-HD-001 a 015 (SRS-001 v3.0)
```

### AGUARDANDO DADOS REAIS DO MVP - P2

```
1. Receber base de dados real do Dr. Abel
2. Executar pipeline completo com dados reais
3. Validar Red List FN=0 (240 casos reais)
4. Medir performance real (sensibilidade, especificidade)
5. Calibrar modelo (Platt scaling se necessário)
6. Gerar CLIN-VAL-002 com resultados reais
7. Atualizar CER-001, PROJ-001 com dados reais
8. Preparar submissão ANVISA (com dados reais)
```

---

## 🎯 TIMELINE AJUSTADA

```
📅 19 Out (HOJE):
├─ ⚡ P0 fixes: BUG-001, BUG-002, BUG-005 (45 min)
└─ 📝 Documentar esclarecimentos (este arquivo)

📅 20-26 Out (Semana 1):
├─ 🐛 Corrigir BUG-006 nos YAMLs (3h)
├─ 📊 Atualizar rastreabilidade (4-8h)
└─ 🧪 Preparar pipeline para dados reais

📅 27 Out - 23 Nov (Semanas 2-5): ⏳ AGUARDANDO DADOS REAIS
├─ Receber base de dados real do MVP
├─ Executar testes com dados reais
├─ Validar Red List FN=0
├─ Medir performance real
└─ Calibrar modelo

📅 24-30 Nov (Semana 6):
├─ Gerar relatórios finais (dados reais)
├─ Atualizar documentação regulatória
└─ 🎯 Preparar submissão ANVISA

🎯 30 Nov 2025: SUBMISSÃO ANVISA (com dados reais)
```

---

## 📌 LEMBRETES IMPORTANTES

### Para Agentes IA

**SEMPRE LEMBRAR:**

1. ⭐ **YAMLs são a fonte de verdade** (15 módulos, 7,350 linhas)
2. 📊 **Dados atuais são FICTÍCIOS** (template apenas)
3. 🧪 **Testes reais aguardam base do MVP** (Dr. Abel fornecerá)
4. ✅ **Correções nos YAMLs são permitidas** (bugs, gaps, melhorias)
5. 📁 **Documentos são para rastreabilidade** (não especificação)

### Estrutura de Decisão Master

```
FONTE DE VERDADE: 15 YAMLs Hybrid V1.0 ⭐
           ↓
    IMPLEMENTAÇÃO (código FastAPI)
           ↓
    TESTES (com dados REAIS do MVP)
           ↓
    VALIDAÇÃO CLÍNICA (Red List FN=0)
           ↓
    SUBMISSÃO ANVISA (30 Nov 2025)
```

---

**Última Atualização:** 19 Out 2025 - 21:00 BRT
**Aprovador:** Dr. Abel Costa
**Status:** ✅ ESCLARECIMENTOS DOCUMENTADOS
**Próxima Ação:** Executar P0 (45 min) + aguardar dados reais do MVP
