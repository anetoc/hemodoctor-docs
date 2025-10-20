# 📋 FORMULÁRIO DE VALIDAÇÃO CLÍNICA
# HemoDoctor Hybrid V1.0 - Dr. Abel Costa
# Data: 19 de Outubro de 2025
# Status: FASE 1.1 - Revisão de Síndromes

---

## 🎯 INSTRUÇÕES

Este formulário guia você pelas 4 componentes clínicas críticas:

1. **34 Síndromes** (3-4h) - Critérios clínicos, actions, next_steps
2. **Cutoffs** (2-3h) - Thresholds para cada síndrome
3. **Next Steps** (2-3h) - Exames sugeridos por síndrome  
4. **Proxy Logic** (2h) - Inferência de dados ausentes

**Formato:** ✅ APROVADO | ⚠️ REVISAR | ❌ REJEITAR + comentário

---

## ✅ FASE 1.1: REVISAR 34 SÍNDROMES

### **Distribuição das 34 Síndromes:**

- **9 CRÍTICAS** (short-circuit, ≥1 evidência = diagnóstico)
- **23 PRIORIDADE** (análise completa, need ALL/ANY logic)
- **1 REVIEW SAMPLE** (qualidade, pré-analíticos)
- **1 ROTINA** (normal ou borderline)

---

### **GRUPO A: SÍNDROMES CRÍTICAS (9 síndromes)**

#### A.1: S-NEUTROPENIA-GRAVE
- **ID:** S-NEUTROPENIA-GRAVE
- **Trigger:** ANC < 0.5 ×10⁹/L OR ANC < 0.2 ×10⁹/L (very critical)
- **Evidence:** E-ANC-CRIT | E-ANC-VCRIT
- **Actions:**
  - Repetir CBC urgente ✅
  - Esfregaço manual ✅
  - Precauções infecção ✅
  - CRP e hemoculturas se febre ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.2: S-BLASTIC-SYNDROME
- **ID:** S-BLASTIC-SYNDROME
- **Trigger:** WBC muito alto + blastos OR padrão específico
- **Evidence:** E-WBC-VERY-HIGH | E-BLASTS-PRESENT
- **Actions:**
  - Esfregaço urgente ✅
  - Imunofenotipagem STAT ✅
  - Avaliar leucostase ✅
  - BCR-ABL se left shift ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.3: S-TMA (Microangiopatia Trombótica)
- **ID:** S-TMA
- **Trigger:** Esquistócitos ≥1% + Plaquetopenia crítica + Hemólise
- **Evidence:** E-SCHISTOCYTES-GE1PCT | E-PLT-CRIT-LOW | E-HEMOLYSIS-PATTERN
- **Actions:**
  - Esfregaço urgente ✅
  - LDH, bilirrubina, haptoglobina ✅
  - PLASMIC score ✅
  - ADAMTS13 atividade ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.4: S-PLT-CRITICA (Plaquetopenia Crítica)
- **ID:** S-PLT-CRITICA
- **Trigger:** PLT < 10 ×10⁹/L
- **Evidence:** E-PLT-CRIT-LOW
- **Actions:**
  - Esfregaço urgente (excluir pseudo) ✅
  - Repetir CBC ✅
  - Coagulação (TP/APTT/Fib/D-dímero) ✅
  - Avaliar risco hemorrágico ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.5: S-ANEMIA-GRAVE
- **ID:** S-ANEMIA-GRAVE
- **Trigger:** Hb crítica (varies por idade/sexo/gravidez)
- **Evidence:** E-HB-CRIT-LOW-M | E-HB-CRIT-LOW-F | E-HB-CRIT-LOW-PED
- **Actions:**
  - Transfusão se indicação ✅
  - Avaliar sangramento ativo ✅
  - Hemólise workup ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.6: S-WBC-VERY-HIGH (Hiperleucócitose)
- **ID:** S-WBC-VERY-HIGH
- **Trigger:** WBC > 100 ×10⁹/L
- **Evidence:** E-WBC-VERY-HIGH
- **Actions:**
  - Avaliar leucostase (hipóxia?) ✅
  - Preps citorredutor urgente ✅
  - Hidratação agressiva ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.7: S-CIVD (Disseminação Intravascular)
- **ID:** S-CIVD
- **Trigger:** Coagulograma alterado + evidências
- **Evidence:** (coagulação, plaquetas, D-dímero)
- **Actions:**
  - Coagulograma completo ✅
  - Fibrinogênio, D-dímero ✅
  - ISTH scoring ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.8: S-LISE-CELULAR (Síndrome de Lise)
- **ID:** S-LISE-CELULAR
- **Trigger:** LDH muito alto + potássio elevado (se disponível)
- **Evidence:** E-LDH-VERY-HIGH
- **Actions:**
  - K, creatinina, ácido úrico ✅
  - Fosfato, cálcio ✅
  - Hidratação IV ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

#### A.9: S-PSEUDOTROMBOCITOPENIA
- **ID:** S-PSEUDOTROMBOCITOPENIA
- **Trigger:** PLT baixa no EDTA mas normal ou alta em citrato
- **Evidence:** E-PSEUDOPLAQUETOPENIA (aglutinina fria/crioaglutininas)
- **Actions:**
  - Repetir em tubo citrato ✅
  - Aquecer amostra ✅
  - Esfregaço ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

### **GRUPO B: SÍNDROMES DE PRIORIDADE (23 síndromes)**

#### B.1-B.23: Avaliação Rápida

**Listar aqui seu feedback sobre as 23 síndromes de prioridade:**

```
[ ] B.1:  IDA (Anemia por Deficiência de Ferro)         ✅ | ⚠️ | ❌
[ ] B.2:  Anemia Megaloblástica                          ✅ | ⚠️ | ❌
[ ] B.3:  Beta-Talassemia                                ✅ | ⚠️ | ❌
[ ] B.4:  Doença Falciforme                              ✅ | ⚠️ | ❌
[ ] B.5:  Hemólise Crônica                               ✅ | ⚠️ | ❌
[ ] B.6:  Hemólise Aguda                                 ✅ | ⚠️ | ❌
[ ] B.7:  Esferocitose Hereditária                       ✅ | ⚠️ | ❌
[ ] B.8:  Deficiência G6PD                               ✅ | ⚠️ | ❌
[ ] B.9:  Trombocitose Reativa                           ✅ | ⚠️ | ❌
[ ] B.10: Trombocitopenia Periférica (PTI)               ✅ | ⚠️ | ❌
[ ] B.11: SHU (Síndrome Hemolítica Urêmica)              ✅ | ⚠️ | ❌
[ ] B.12: PTT (Púrpura Trombótica Trombocitopênica)      ✅ | ⚠️ | ❌
[ ] B.13: Eosinofilia                                     ✅ | ⚠️ | ❌
[ ] B.14: Linfocitose                                     ✅ | ⚠️ | ❌
[ ] B.15: Linfopenia                                      ✅ | ⚠️ | ❌
[ ] B.16: Basofilia/Eosinofilia Patológica                ✅ | ⚠️ | ❌
[ ] B.17: Monócitose                                      ✅ | ⚠️ | ❌
[ ] B.18: Neutrofilia                                     ✅ | ⚠️ | ❌
[ ] B.19: Desvio à Esquerda                               ✅ | ⚠️ | ❌
[ ] B.20: Hipersegmentação Neutrofílica                   ✅ | ⚠️ | ❌
[ ] B.21: Anemia Inflamatória                             ✅ | ⚠️ | ❌
[ ] B.22: Anemia com RDW Elevado                          ✅ | ⚠️ | ❌
[ ] B.23: Eritrocitose                                    ✅ | ⚠️ | ❌
```

**Comentários gerais sobre Prioridade:**
___________________________________________________________________

---

### **GRUPO C: SÍNDROMES ESPECIAIS (2 síndromes)**

#### C.1: S-REVIEW-SAMPLE (Controle de Qualidade)
- **Trigger:** Erro pré-analítico detectado
- **Actions:** Repetir coleta ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

#### C.2: S-NORMAL-BORDERLINE
- **Trigger:** Valores normais ou borderline
- **Actions:** Nenhuma ação urgente ✅
- **Seu feedback:** [ ] ✅ OK | [ ] ⚠️ Revisar | [ ] ❌ Rejeitar
- **Comentários:** _______________________________________________

---

## 📊 RESUMO FASE 1.1

- **Total Síndromes:** 34
- **Aprovadas (✅):** _____ / 34
- **Revisar (⚠️):** _____ / 34
- **Rejeitar (❌):** _____ / 34
- **Status:** [ ] PRONTO PARA FASE 1.2 | [ ] NECESSITA AJUSTES

**Data Conclusão:** ______________  
**Tempo Gasto:** ______ horas

---

**Próximo Passo:** Avançar para FASE 1.2 - Revisar Cutoffs
