# HemoDoctor Regras Completas v2.4.0 - Excel Exportado

**Data:** 20 de Outubro de 2025  
**Arquivo:** `HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx`  
**Tamanho:** 34 KB  
**Versão HemoDoctor:** v2.4.0

---

## 📊 Resumo do Conteúdo

| Categoria | Quantidade |
|-----------|------------|
| **Evidências** | 79 |
| **Síndromes** | 35 |
| **Triggers (Next Steps)** | 40 |
| **Campos CBC** | 35 |
| **Cutoffs** | ~150 valores |

---

## 📑 Abas do Excel

### 1. **Resumo**
- Informações gerais do HemoDoctor v2.4.0
- Estatísticas de evidências (critical, strong, moderate, weak)
- Distribuição de síndromes (critical, priority, review, routine)

### 2. **Evidências** (79 linhas)
**Colunas:**
- ID (ex: E-ANC-CRIT)
- Categoria (critical, red_cell, white_cell, platelet, etc)
- Rule (fórmula/condição)
- Strength (strong/moderate/weak)
- Description
- Clinical Significance
- Requires (campos necessários)
- Source (referência)
- Differential (diagnósticos diferenciais)
- Next Steps (próximos passos)

**Categorias de Evidências:**
- Critical: 6
- Red Blood Cell: 15
- White Blood Cell: 13
- Platelet: 8
- Coagulation: 5
- Molecular: 10
- Supplementary Lab: 5
- Pre-Analytical: 5
- Complementary: 5

**Total: 79 evidências**

### 3. **Síndromes** (35 linhas)
**Colunas:**
- ID (ex: S-TMA)
- Criticality (critical/priority/routine)
- Combine Logic (estrutura lógica)
- Required Evidences (ALL)
- Optional Evidences (ANY)
- Negative Evidences (exclusões)
- Threshold
- Description
- Actions (ações clínicas)
- Next Steps (próximos passos)
- Short Circuit (YES/NO)

**Distribuição:**
- Critical: 9 síndromes (short-circuit enabled)
- Priority: 24 síndromes
- Review Sample: 1 síndrome
- Routine: 1 síndrome

**Total: 35 síndromes**

### 4. **Next Steps** (40 linhas)
**Colunas:**
- Trigger ID
- Syndrome Target
- When Condition (lógica Python)
- Priority Level (critical/priority/routine)
- Test Recommendations
- Rationale
- Cost Band (low/mid/high)
- Turnaround

**Total: 40 triggers**

### 5. **Cutoffs**
Valores de corte por idade/sexo para parâmetros:
- hb_low, hb_critical_low, hb_high, hb_critical_high
- wbc_low, wbc_high
- plt_low, plt_critical_low, plt_high
- anc_critical, anc_low
- mcv_low, mcv_high
- ldh_high
- creatinine_high
- E muitos outros...

**Grupos de Idade:**
- neonatal_0_7d
- neonatal_8_28d
- infant_1_12m
- toddler_1_2y
- preschool_2_5y
- school_6_12y
- adolescent_13_18y
- adult_male
- adult_female

### 6. **Schema CBC** (35 campos)
**Colunas:**
- Field Name
- Type (float/int/str/bool)
- Unit
- Required (YES/NO)
- Range (min-max)
- Description

**Campos incluem:**
- hb, ht, rbc, mcv, mch, mchc, rdw
- wbc, anc, lymphocytes_abs, monocytes_abs, eosinophils_abs, basophils_abs
- plt, mpv
- reticulocytes
- ferritin, tsat, tibc, iron
- b12, folate, ldh, crp
- morphology (nested object)
- metadata (nested object)

### 7. **Metadados**
Informações sobre os arquivos YAML fonte:
- Nome do arquivo
- Versão
- Última modificação
- Tamanho (linhas)
- Número de elementos

---

## 🎯 Uso Recomendado

### Para Médicos/Clínicos:
- **Aba Síndromes**: Consultar critérios diagnósticos e ações clínicas
- **Aba Evidências**: Ver detalhes de cada regra clínica
- **Aba Next Steps**: Guia de exames complementares

### Para Desenvolvedores:
- **Aba Evidências**: Implementar lógica de avaliação de evidências
- **Aba Síndromes**: Implementar DAG de fusão de síndromes
- **Aba Schema CBC**: Validação de entrada
- **Aba Cutoffs**: Normalização por idade/sexo

### Para Regulatório/QA:
- **Aba Resumo**: Visão geral do sistema
- **Aba Metadados**: Rastreabilidade dos arquivos fonte
- **Todas as abas**: Documentação completa para auditorias

---

## 🔍 Exemplos de Dados

### Evidência (E-ANC-CRIT)
```
ID: E-ANC-CRIT
Categoria: Critical
Rule: anc < 0.5
Strength: strong
Description: ANC < 0.5×10⁹/L (neutropenia grave)
Clinical Significance: Risco infeccioso alto
Source: Dev Team
```

### Síndrome (S-TMA)
```
ID: S-TMA
Criticality: critical
Required Evidences: E-PLT-CRIT-LOW, E-SCHISTOCYTES-GE1PCT
Optional Evidences: E-LDH-HIGH, E-BT-IND-HIGH, E-CREATININA-HIGH
Threshold: 1.0
Short Circuit: YES
Actions: Esfregaço IMEDIATO; LDH urgente; ADAMTS13/Complemento
```

### Trigger (trigger_tma)
```
ID: trigger_tma
Syndrome: S-TMA
When: 'S-TMA' in syndromes and syndromes['S-TMA'].criticality == 'critical'
Level: urgent
Test: Blood smear + LDH + indirect bilirubin + creatinine
Cost: low
Turnaround: <2h
```

---

## 📝 Notas Importantes

1. **Formatação:**
   - Headers em negrito + fundo cinza
   - Regras/condições em fonte Courier (monospace)
   - Colunas auto-ajustadas (10-80 caracteres)
   - Bordas em todas as células

2. **Dados:**
   - Todos os valores são estáticos (sem fórmulas Excel)
   - Listas separadas por "; " (ponto-vírgula + espaço)
   - Campos aninhados (morphology, metadata) representados como strings

3. **Fonte de Dados:**
   - `02_evidence_hybrid.yaml` (79 evidências)
   - `03_syndromes_hybrid.yaml` (35 síndromes)
   - `09_next_steps_engine_hybrid.yaml` (40 triggers)
   - `00_config_hybrid.yaml` (cutoffs)
   - `01_schema_hybrid.yaml` (schema CBC)

4. **Completude:**
   - ✅ TODAS as 79 evidências incluídas
   - ✅ TODAS as 35 síndromes incluídas
   - ✅ TODOS os 40 triggers incluídos
   - ✅ TODOS os cutoffs incluídos
   - ✅ TODOS os campos CBC incluídos

---

## 🚀 Próximos Passos

### Para Utilização:
1. Abrir arquivo em Excel/LibreOffice/Google Sheets
2. Usar filtros nas abas para busca rápida
3. Consultar aba Resumo para overview

### Para Desenvolvimento:
1. Usar como referência de implementação
2. Validar contra os YAMLs originais
3. Gerar testes unitários a partir das regras

### Para Documentação:
1. Anexar ao dossiê regulatório
2. Usar em apresentações clínicas
3. Material de treinamento para equipe médica

---

**Gerado em:** 20 de Outubro de 2025  
**Script:** `generate_excel_complete.py`  
**Responsável:** HemoDoctor Development Team  
**Versão:** v2.4.0

---

## 📞 Suporte

Para dúvidas sobre o conteúdo:
- **Clínico:** Dr. Abel Costa
- **Técnico:** HemoDoctor Dev Team
- **Regulatório:** Regulatory Affairs Team

**IMPORTANTE:** Este arquivo é uma EXPORTAÇÃO dos YAMLs oficiais. Os YAMLs são a fonte de verdade (single source of truth) para implementação.
