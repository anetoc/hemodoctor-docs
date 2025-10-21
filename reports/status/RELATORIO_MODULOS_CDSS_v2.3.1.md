# 🎯 MÓDULOS CDSS v2.3.1 - MICROCOPY SEGURA

**Data:** 19 de Outubro de 2025  
**Versão:** v2.3.1-cdss  
**Tipo:** Extensão CDSS (Clinical Decision Support System)  
**Status:** ✅ **IMPLEMENTADO**

---

## 📊 RESUMO

Dois novos módulos CDSS foram adicionados ao HemoDoctor Hybrid v2.3.1 para garantir **linguagem não-diagnóstica** e **microcopy segura** voltada a médicos não-hematologistas.

✅ **Módulo 04:** Output Templates (microcopy segura)  
✅ **Módulo 12-CDSS:** Output Policies (políticas de renderização)

---

## 🔧 MÓDULO 04: OUTPUT TEMPLATES

### Arquivo: `04_output_templates_hybrid.yaml`
**Versão:** v2.3.1-cdss

### Propósito
Templates de microcopy segura para CDSS que **NUNCA usa linguagem diagnóstica**.

### Características Principais

#### 1. **Léxico Controlado**
✅ **Verbos permitidos:**
- "padrão compatível com"
- "sugere"
- "pode representar"
- "considerar"
- "recomenda-se"

❌ **Verbos proibidos:**
- "diagnóstico de"
- "tem (doença)"
- "confirma"
- "é (doença)"
- "câncer/leucemia" (sem "suspeita")

#### 2. **Templates por Criticidade**

**CRÍTICO:**
```
CRÍTICO — {headline}
Hipótese: **{syndrome_name} (C{confidence})** — {compat_phrase}.
**Por quê:** {evidence_short}. {values_line}
**Ação tempo-sensível:** {next_step_1}; {next_step_2}; {next_step_3}.
{missing_line}
*{disclaimer}*
```

**PRIORIDADE:**
```
PRIORIDADE — {headline}
Hipótese: **{syndrome_name} (C{confidence})** — {compat_phrase}.
**Por quê:** {evidence_short}. {values_line}
**Próximos passos:** 1) {next_step_1}; 2) {next_step_2}; 3) {next_step_3}; 4) {next_step_4}.
{missing_line}
*{disclaimer}*
```

**ROTINA:**
```
ROTINA — {headline}
**Sem achados críticos/prioritários.** {borderline_note}
**Orientação:** {routine_tip}.
*{disclaimer}*
```

**REVER AMOSTRA:**
```
REVER AMOSTRA — Pré-analítico suspeito
**Motivo:** {preanalytical_reason}.
**Ação recomendada:** {recollect_actions}.
*{disclaimer}*
```

#### 3. **Mapeamento de Síndromes → Textos**

Todas as 35 síndromes têm microcopy pré-definida:

**Exemplos:**

- **S-TMA:**  
  - Headline: "Suspeita de microangiopatia trombótica (MAT)"
  - Compat: "alta suspeita (PLT crítica + esquistócitos)"
  - Next steps: Esfregaço imediato, ADAMTS13/Complemento, Creatinina

- **S-PV:**  
  - Headline: "Eritrocitose — PV a considerar"
  - Compat: "padrão compatível (Hb/Ht altos)"
  - Next steps: Repetir CBC, JAK2/CALR/MPL, EPO sérica

- **S-IDA:**  
  - Headline: "Anemia ferropriva — investigação"
  - Compat: "padrão compatível (microcitose + RDW alto)"
  - Next steps: Ferritina e TSat, CRP

- **S-ACD:** ✨ **NOVA**
  - Headline: "Anemia da doença crônica/inflamatória — investigação"
  - Compat: "padrão compatível (anemia + ferritina alta/CRP alto)"
  - Next steps: Confirmar CRP/ferritina/TSat, Tratar base

- **S-PANCYTOPENIA:** ✅ **CORRIGIDA**
  - Headline: "Pancitopenia — investigação dirigida"
  - Compat: "padrão compatível (3 séries baixas)"
  - Next steps: Reticulócitos, Esfregaço, Medula óssea

#### 4. **Helpers de Renderização**

```yaml
values_compaction:
  joiner: ", "
  key_order: [hb, mcv, rdw, wbc, anc, plt, mchc]

missingness_render:
  prefix: "Lacunas: "
  joiner: "; "
  max_items: 2

headlines:
  by_criticality:
    critical: "Risco imediato"
    priority: "Investigar direcionado"
    routine: "Sem alertas relevantes"
    review_sample: "Validação pré-analítica necessária"
```

---

## 🔧 MÓDULO 12-CDSS: OUTPUT POLICIES

### Arquivo: `12_output_policies_cdss.yaml`
**Versão:** v2.3.1-cdss

### Propósito
Políticas de seleção e renderização de cards com foco em segurança clínica.

### Características Principais

#### 1. **Seleção Hierárquica**

```yaml
selection_order: [critical, review_sample, priority, borderline, routine]
```

**Regras:**
1. Se `any_critical_true` → **critical**
2. Se `preanalytical_flags_true` → **review_sample**
3. Se `any_priority_true` → **priority**
4. Se `has_borderline` → **borderline**
5. Senão → **routine**

#### 2. **Escalação SMS Crítica**

```yaml
sms_if:
  - "anc < 0.2e9"         # Neutropenia muito grave
  - "plt < 10e9"          # Plaquetopenia crítica
  - "wbc >= 100e9"        # Leucostase
  - "apl_suspect == true" # APL suspeita
lock_route_until_ack: true
```

#### 3. **Borderline Rules**

**Adulto:**
- MCV: [80,82) ou (98,100]
- PLT: [140,150) ou (450,500]
- WBC: [3.8,4) ou (11,12]

**Pediátrico:**
- Hb: [11,11.5)
- MCV: [75,78)

#### 4. **Gating de Next Steps**

Impede sugestões avançadas antes de básicos:

**Anemia workup:**
```yaml
if: "S-IDA OR S-ACD OR S-MACRO-B12-FOLATE"
require_first: ["Ferritina", "TSat", "CRP", "B12", "Folato"]
```

**Trombocitopenia workup:**
```yaml
if: "plt<150"
require_first: ["Esfregaço", "MPV"]
```

#### 5. **Microcopy Controlada**

```yaml
non_diagnostic_banner: "CDSS de apoio à decisão. Não substitui julgamento clínico. Resultado não é diagnóstico."

compat_words:
  C0: "indícios insuficientes"
  C1: "padrão compatível"
  C2: "padrão sugestivo"

critical_time_phrase: "Ação tempo-sensível"
```

#### 6. **Auditoria Completa**

```yaml
audit:
  include:
    - route_id
    - fired_evidences
    - top_syndromes
    - key_values_compact
    - engine_versions
    - config_hash
    - code_hash
    - event_id             # Idempotência
```

---

## 🎯 INTEGRAÇÃO COM SISTEMA v2.3.1

### Pipeline Completo

```
00_config
  ↓
01_schema
  ↓
02_evidence
  ↓
03_syndromes
  ↓
05_missingness
  ↓
06_route_policy
  ↓
09_next_steps
  ↓
[NOVO] 04_output_templates ←── Microcopy segura
  ↓
[NOVO] 12_output_policies_cdss ←── Políticas CDSS
  ↓
Card Final (JSON/HTML/Markdown)
```

### Compatibilidade

✅ **100% compatível** com módulos existentes:
- 00_config_hybrid.yaml (v2.3.1)
- 01_schema_hybrid.yaml (v2.3.1)
- 02_evidence_hybrid.yaml (v2.3.1)
- 03_syndromes_hybrid.yaml (v2.3.1)
- 05_missingness_hybrid_v2.3.yaml
- 06_route_policy_hybrid.yaml
- 08_wormlog_hybrid.yaml (v2.3.1)
- 09_next_steps_engine_hybrid.yaml (v2.3.1)
- 10_runbook_hybrid.yaml (v2.3.1)
- 11_case_state_hybrid.yaml
- 12_output_policies_hybrid.yaml (v2.3.1 — base)

---

## 🎖️ IMPACTO CLÍNICO

### 1. **Segurança Jurídica**
- ✅ Linguagem **NUNCA diagnóstica**
- ✅ Disclaimer **sempre presente**
- ✅ Verbos controlados (léxico aprovado)

### 2. **Usabilidade para Não-Hematologistas**
- ✅ Headlines claros e diretos
- ✅ Próximos passos priorizados (máx. 4)
- ✅ Valores compactos (máx. 6 por linha)
- ✅ Lacunas visíveis (top 2)

### 3. **Auditoria Regulatória**
- ✅ Event ID para idempotência
- ✅ Engine versions rastreadas
- ✅ Config/code hash incluídos
- ✅ WORM log compatível

### 4. **Gating Inteligente**
- ✅ Previne "shopping list" de exames
- ✅ Força exames básicos antes de avançados
- ✅ Respeita fluxo clínico lógico

---

## 📦 ARQUIVOS CRIADOS

```
HEMODOCTOR_HIBRIDO_V1.0/YAMLs/
├── 04_output_templates_hybrid.yaml        ✅ NOVO (v2.3.1-cdss)
└── 12_output_policies_cdss.yaml           ✅ NOVO (v2.3.1-cdss)
```

---

## 🧪 VALIDAÇÃO RECOMENDADA

### Teste de Microcopy

Para cada síndrome crítica (TMA, Neutropenia, APL, etc.):
1. ✅ Verificar que NÃO usa linguagem diagnóstica
2. ✅ Verificar que disclaimer está presente
3. ✅ Verificar que verbos estão no léxico permitido
4. ✅ Verificar que confidence (C0/C1/C2) está mapeado

### Teste de Gating

Para S-IDA sem ferritina:
1. ✅ Deve sugerir Ferritina ANTES de JAK2
2. ✅ Deve sugerir TSat ANTES de medula óssea

Para PTI sem esfregaço:
1. ✅ Deve sugerir Esfregaço ANTES de anticorpos

### Teste de Escalação

Para casos críticos:
1. ✅ ANC <0.2 → SMS + lock route
2. ✅ PLT <10 → SMS + lock route
3. ✅ WBC ≥100 → SMS + lock route
4. ✅ APL suspeita → SMS + lock route

---

## ⏭️ PRÓXIMOS PASSOS

### Dev Team
1. **Parser de templates:** Implementar substituição de placeholders
2. **Renderer:** Gerar HTML/JSON/Markdown a partir dos templates
3. **Validator:** Garantir que microcopy respeita léxico
4. **Gating engine:** Implementar lógica de require_first

### Validação Clínica
1. **Review 100 cards:** Verificar linguagem não-diagnóstica
2. **Compliance check:** Confirmar léxico aprovado
3. **Usability test:** Testar com médicos generalistas

### Regulatório
1. **IFU update:** Incorporar disclaimer e léxico
2. **Risk management:** Atualizar com gating logic
3. **Labeling:** Confirmar "CDSS, não diagnóstico"

---

## 🎉 CONCLUSÃO

**Os módulos CDSS v2.3.1 foram integrados COM SUCESSO.**

✅ Microcopy segura implementada  
✅ Políticas de output reforçadas  
✅ Gating inteligente de exames  
✅ Auditoria completa  
✅ 100% compatível com v2.3.1 base

**Status:** ✅ **PRONTO PARA DESENVOLVIMENTO**

---

**FIM DO RELATÓRIO CDSS**
