# SUMÁRIO EXECUTIVO: Bugs YAMLs v2.3.1

**Data:** 19 de Outubro de 2025
**Status:** 🔴 7 BUGS IDENTIFICADOS (5 P0, 2 P1)
**Tempo Total de Correção:** 67 minutos (~1 hora)

---

## BUGS CRÍTICOS (P0) - 45 MINUTOS

### 🔴 BUG-007: 5 Evidências Faltantes (15 min)

**Problema:** Síndromes S-ACD e S-PANCYTOPENIA não disparam (evidências não definidas)

**Evidências a adicionar:**
- E-ANEMIA
- E-FERRITIN-HIGH-100
- E-LDH-HIGH
- E-BT-IND-HIGH
- E-CREATININA-HIGH

**Arquivo:** `02_evidence_hybrid.yaml`
**Solução:** Ver ANEXO C do relatório completo

---

### 🔴 BUG-008: Metadata Evidências Incorreta (5 min)

**Problema:** Declara 75, mas apenas 64 definidas

**Atual:** `total_evidences: 75`
**Correto:** `total_evidences: 64` (ou 69 após BUG-007)

**Arquivo:** `02_evidence_hybrid.yaml` linha 562

---

### 🔴 BUG-009: Metadata Síndromes Incorreta (2 min)

**Problema:** Declara 34, mas 35 definidas

**Atual:** `total_syndromes: 34`
**Correto:** `total_syndromes: 35`

**Arquivo:** `03_syndromes_hybrid.yaml` linha 712

---

### 🔴 BUG-010: Campo monocytes_abs Faltante (10 min)

**Problema:** E-MONOCYTOSIS usa campo não definido no schema

**Solução:** Adicionar ao `01_schema_hybrid.yaml`

```yaml
  - name: monocytes_abs
    type: float
    unit: 1e9/L
    required: false
    loinc: "742-7"
    description: "Monócitos absolutos"
    physiological_range: [0, 5]
```

---

### ✅ BUG-011 (BUG-005): WORM Retention JÁ CORRIGIDO (0 min)

**Status:** ✅ Linha 129 confirmada com `days: 1825` (5 anos)

**Nenhuma ação necessária.**

---

## BUGS MÉDIOS (P1) - 22 MINUTOS

### 🟡 BUG-012: Versão Inconsistente (2 min)

**Arquivo:** `09_next_steps_engine_hybrid.yaml` linha 6

**Atual:** `version: hybrid_v2.3.1`
**Correto:** `version: next_steps_engine_hybrid_v2.3.1`

---

### 🟡 BUG-013: Sintaxe Triggers Inválida (20 min)

**Problema:** 4 triggers usam pseudo-código (`AND`/`OR` maiúsculas, `missing`, `high`/`low`)

**Triggers a corrigir:**
- trigger-pv-erythrocytosis (linha 1029)
- trigger-pv-erythrocytosis-negative (linha 1046)
- trigger-pti-exclude-pseudo (linha 1058)
- trigger-apl-suspect (linha 1088)

**Exemplo de correção:**

```yaml
# ❌ ERRADO
when: "(E-HB-HIGH OR E-HCT-HIGH) AND (jak2_pos missing)"

# ✅ CORRETO
when: "(hb > config.cutoffs.hb_high[age_sex_group] or ht > config.cutoffs.hct_high[age_sex_group]) and (jak2_pos is None)"
```

---

## PLANO DE EXECUÇÃO (67 MIN)

```
1. BUG-007 (15 min) → Adicionar 5 evidências
2. BUG-008 (5 min)  → Metadata evidências
3. BUG-009 (2 min)  → Metadata síndromes
4. BUG-010 (10 min) → Campo monocytes_abs
5. BUG-012 (2 min)  → Versão 09_next_steps
6. BUG-013 (20 min) → Sintaxe triggers
-------------------------------------------
TOTAL: 54 min      → Código
       13 min      → Testes + validação
       67 min      → TOTAL
```

---

## IMPACTO CLÍNICO

| Bug | Impacto | Síndromes Afetadas |
|-----|---------|-------------------|
| BUG-007 | 🔴 ALTO | S-ACD, S-PANCYTOPENIA não disparam |
| BUG-008 | 🟡 MÉDIO | Rastreabilidade regulatória |
| BUG-009 | 🟡 MÉDIO | Rastreabilidade regulatória |
| BUG-010 | 🔴 ALTO | S-MONOCITOSE-CRONICA não dispara |
| BUG-011 | ✅ OK | Nenhum (já corrigido) |
| BUG-012 | 🟢 BAIXO | Rastreabilidade de versão |
| BUG-013 | 🔴 ALTO | 4 triggers não disparam (syntax error) |

---

## RECOMENDAÇÃO

**Timeline:** 26 Out vs 30 Nov

- ❌ **26 Out (7 dias):** INVIÁVEL - 67 min de bugs + testes críticos pendentes
- ✅ **30 Nov (6 semanas):** VIÁVEL - tempo suficiente para corrigir + testar + validar Red List

**Ver relatório completo:** `RELATORIO_ANALISE_TECNICA_YAMLS_v2.3.1.md`

---

**Próximo Passo:** Executar patches → Rodar test suite → Commit v2.3.2
