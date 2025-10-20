# HemoDoctor Hybrid v2.4.0
## Documento de Validacao Clinica para Hematologista

**Data:** 20/10/2025
**Versao:** v2.4.0

---

## SUMARIO EXECUTIVO

Sistema de apoio a decisao clinica (SaMD Class III) para analise de hemogramas.
**35 sindromes hematologicas** usando **79 evidencias clinicas**.

---

## COMPONENTES DO SISTEMA

| Componente | Quantidade |
|------------|------------|
| Informação | Valor |
| Versão | v2.4.0 |
| Data | 19 Out 2025 |
| Total Evidências | 79 |
| Total Síndromes | 35 |
| Total Triggers | 40 |
| Total Campos CBC | 35 |

---

## EVIDENCIAS CLINICAS


### 1. E-ANC-VCRIT

**Categoria:** Critical

**Regra:** `anc < 0.2`

**Forca:** strong

**Descricao:** ANC < 0.2×10⁹/L (neutropenia muito grave)

**Significancia Clinica:** Risco infeccioso extremo

**Fonte:** Dev Team + HemoDoctor SRS-001

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 2. E-ANC-CRIT

**Categoria:** Critical

**Regra:** `anc < 0.5`

**Forca:** strong

**Descricao:** ANC < 0.5×10⁹/L (neutropenia grave)

**Significancia Clinica:** Risco infeccioso alto

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 3. E-WBC-VERY-HIGH

**Categoria:** Critical

**Regra:** `wbc > 100`

**Forca:** strong

**Descricao:** WBC > 100×10⁹/L (leucocitose extrema)

**Significancia Clinica:** Suspeita blástica/leucostase

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 4. E-PLT-CRIT-LOW

**Categoria:** Critical

**Regra:** `plt < 10`

**Forca:** strong

**Descricao:** PLT < 10×10⁹/L (plaquetopenia crítica)

**Significancia Clinica:** Risco hemorrágico grave

**Fonte:** Dev Team + HemoDoctor SRS-001

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 5. E-SCHISTOCYTES-GE1PCT

**Categoria:** Critical

**Regra:** `morphology.esquistocitos == true`

**Forca:** strong

**Descricao:** Esquistócitos presentes (≥1%)

**Significancia Clinica:** TMA/MAT concern

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 6. E-HEMOLYSIS-PATTERN

**Categoria:** Critical

**Regra:** `(reticulocytes > 100) or (haptoglobin < 40) or (ldh > 500) or (bt_indireta > 1.0)`

**Forca:** strong

**Descricao:** Padrão de hemólise (qualquer marcador positivo)

**Significancia Clinica:** Hemólise ativa

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 7. E-HB-CRIT-LOW

**Categoria:** Red Blood Cell

**Regra:** `hb < config.cutoffs.hb_critical_low[age_sex_group]`

**Forca:** strong

**Descricao:** Hemoglobina crítica (ajustada por idade/sexo)

**Significancia Clinica:** Anemia grave - risco de hipóxia

**Fonte:** HemoDoctor SRS-001 v3.0 + Ajustes Dr. Abel

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 8. E-HB-HIGH

**Categoria:** Red Blood Cell

**Regra:** `hb > config.cutoffs.hb_high[age_sex_group]`

**Forca:** strong

**Descricao:** Hemoglobina alta por idade/sexo

**Significancia Clinica:** Policitemia vera ou eritrocitose secundária

**Fonte:** Validação Externa v2.3.1 + WHO 2016 PV criteria

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 9. E-HCT-HIGH

**Categoria:** Red Blood Cell

**Regra:** `ht > config.cutoffs.hct_high[age_sex_group]`

**Forca:** strong

**Descricao:** Hematócrito alto por idade/sexo

**Significancia Clinica:** Policitemia vera ou eritrocitose secundária

**Fonte:** Validação Externa v2.3.1

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 10. E-MICROCYTOSIS

**Categoria:** Red Blood Cell

**Regra:** `mcv < config.cutoffs.mcv_low_adult`

**Forca:** moderate

**Descricao:** Microcitose (MCV < 80 fL adulto ou < 75 fL criança)

**Significancia Clinica:** IDA, talassemia, anemia inflamatória

**Fonte:** Dev Team + HemoDoctor

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 11. E-MACROCYTOSIS

**Categoria:** Red Blood Cell

**Regra:** `mcv > config.cutoffs.mcv_high_adult`

**Forca:** moderate

**Descricao:** Macrocitose (MCV > 100 fL)

**Significancia Clinica:** B12/folato, álcool, hipotireoidismo, MDS

**Fonte:** Dev Team + HemoDoctor

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 12. E-RDW-HIGH

**Categoria:** Red Blood Cell

**Regra:** `rdw > 14`

**Forca:** moderate

**Descricao:** RDW elevado (> 14%)

**Significancia Clinica:** Anisocitose - IDA, hemoglobinopatias

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 13. E-IDA-LABS

**Categoria:** Red Blood Cell

**Regra:** `(ferritin < 30) or (tsat < 20)`

**Forca:** moderate

**Descricao:** Ferritina < 30 ng/mL ou TSat < 20%

**Significancia Clinica:** Deficiência de ferro

**Fonte:** Dev Team + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 14. E-IDA-INFLAM

**Categoria:** Red Blood Cell

**Regra:** `(ferritin >= 30 and ferritin <= 100) and (tsat < 20) and (crp > 10)`

**Forca:** moderate

**Descricao:** Ferritina 30-100 + TSat baixo + CRP elevado

**Significancia Clinica:** Anemia ferropriva + inflamatória

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 15. E-INFLAM-HIGH

**Categoria:** Red Blood Cell

**Regra:** `crp > 10`

**Forca:** weak

**Descricao:** CRP > 10 mg/L

**Significancia Clinica:** Inflamação ativa

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 16. E-B12-FOLATE-LOW

**Categoria:** Red Blood Cell

**Regra:** `(b12 < 300) or (folate < 3.1)`

**Forca:** moderate

**Descricao:** B12 < 300 pg/mL ou Folato < 3.1 ng/mL

**Significancia Clinica:** Deficiência vitamínica - anemia megaloblástica

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 17. E-BETA-THAL-TRAIT

**Categoria:** Red Blood Cell

**Regra:** `hba2 >= 3.5`

**Forca:** strong

**Descricao:** HbA2 ≥ 3.5%

**Significancia Clinica:** Traço beta-talassêmico

**Fonte:** SADMH + Ajustes Dr. Abel

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 18. E-ALFA-THAL-PATTERN

**Categoria:** Red Blood Cell

**Regra:** `(mcv < 80) and (rdw < 14) and (ferritin > 30)`

**Forca:** moderate

**Descricao:** Microcitose + RDW normal + ferritina normal

**Significancia Clinica:** Padrão sugestivo de alfa-talassemia

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 19. E-HB-SICKLE-MORPH

**Categoria:** Red Blood Cell

**Regra:** `morphology.drepanocitos == true`

**Forca:** strong

**Descricao:** Drepanócitos presentes

**Significancia Clinica:** Doença falciforme

**Fonte:** SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 20. E-ESFEROCITOS-PRESENT

**Categoria:** Red Blood Cell

**Regra:** `morphology.esferocitos == true`

**Forca:** moderate

**Descricao:** Esferócitos presentes

**Significancia Clinica:** Esferocitose hereditária ou hemólise autoimune

**Fonte:** HemoDoctor + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 21. E-ROULEAUX-PRESENT

**Categoria:** Red Blood Cell

**Regra:** `morphology.rouleaux == true`

**Forca:** moderate

**Descricao:** Rouleaux (hemácias empilhadas)

**Significancia Clinica:** Mieloma múltiplo, inflamação

**Fonte:** SADMH + Ajustes Dr. Abel

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 22. E-DACRIOCITOS-PRESENT

**Categoria:** Red Blood Cell

**Regra:** `morphology.dacriocitos == true`

**Forca:** moderate

**Descricao:** Dacrócitos (tear drops)

**Significancia Clinica:** Mielofibrose, talassemia

**Fonte:** SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 23. E-APLASIA-RETIC-LOW

**Categoria:** Red Blood Cell

**Regra:** `(hb < config.cutoffs.hb_critical_low[age_sex_group]) and (reticulocytes < 50)`

**Forca:** strong

**Descricao:** Anemia grave + reticulócitos < 50×10⁹/L

**Significancia Clinica:** Aplasia/crise aplástica (Parvovírus B19)

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 24. E-IRON-LOW

**Categoria:** Red Blood Cell

**Regra:** `iron < 50`

**Forca:** high

**Descricao:** Serum iron <50 μg/dL

**Significancia Clinica:** Iron deficiency anemia (IDA)

**Fonte:** WHO 2011 IDA criteria

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 25. E-TIBC-HIGH

**Categoria:** Red Blood Cell

**Regra:** `tibc > 450`

**Forca:** moderate

**Descricao:** TIBC >450 μg/dL (increased iron-binding capacity)

**Significancia Clinica:** Iron deficiency anemia (IDA)

**Fonte:** WHO 2011 IDA criteria

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 26. E-TSAT-LOW

**Categoria:** Red Blood Cell

**Regra:** `transferrin_saturation < 20`

**Forca:** high

**Descricao:** Transferrin saturation <20%

**Significancia Clinica:** Iron deficiency anemia (IDA)

**Fonte:** WHO 2011 IDA criteria

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 27. E-SOLUBLE-TRANSFERRIN-RECEPTOR-HIGH

**Categoria:** Red Blood Cell

**Regra:** `soluble_transferrin_receptor > 8.5`

**Forca:** moderate

**Descricao:** Soluble transferrin receptor >8.5 mg/L

**Significancia Clinica:** Iron deficiency, active erythropoiesis

**Fonte:** WHO 2011 micronutrient guidelines

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 28. E-HEPCIDIN-HIGH

**Categoria:** Red Blood Cell

**Regra:** `hepcidin > 100`

**Forca:** moderate

**Descricao:** Hepcidin >100 ng/mL (iron absorption blockade)

**Significancia Clinica:** Anemia of chronic disease (ACD)

**Fonte:** Nature Reviews Hematology 2023

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 29. E-WBC-HIGH

**Categoria:** White Blood Cell

**Regra:** `wbc > 11`

**Forca:** moderate

**Descricao:** WBC > 11×10⁹/L

**Significancia Clinica:** Leucocitose

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 30. E-WBC-LOW

**Categoria:** White Blood Cell

**Regra:** `wbc < config.cutoffs.wbc_low[age_group]`

**Forca:** strong

**Descricao:** Leucopenia por faixa etária

**Significancia Clinica:** Pancitopenia, aplasia, MDS, quimioterapia

**Fonte:** Validação Externa v2.3.1

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 31. E-LEFT-SHIFT

**Categoria:** White Blood Cell

**Regra:** `morphology.bastoes == true or morphology.mielocitos == true or morphology.metamielocitos == true`

**Forca:** moderate

**Descricao:** Desvio à esquerda (bastões/mielócitos/metamielócitos)

**Significancia Clinica:** Infecção, LMC, reação leucemoide

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 32. E-ANC-HIGH

**Categoria:** White Blood Cell

**Regra:** `anc > 10`

**Forca:** moderate

**Descricao:** ANC > 10×10⁹/L

**Significancia Clinica:** Neutrofilia grave

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 33. E-BLASTS-PRESENT

**Categoria:** White Blood Cell

**Regra:** `morphology.blastos == true`

**Forca:** strong

**Descricao:** Blastos presentes

**Significancia Clinica:** Leucemia aguda, SMD high-grade

**Fonte:** Dev Team + HemoDoctor

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 34. E-PROMIELOCITOS-PRESENT

**Categoria:** White Blood Cell

**Regra:** `morphology.promielocitos == true`

**Forca:** strong

**Descricao:** Promielócitos presentes

**Significancia Clinica:** LPA (M3), reação leucemoide

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 35. E-LYMPHOCYTOSIS

**Categoria:** White Blood Cell

**Regra:** `lymphocytes_abs > 5`

**Forca:** moderate

**Descricao:** Linfócitos > 5×10⁹/L

**Significancia Clinica:** LLC, linfoma, viral

**Fonte:** Dev Team + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 36. E-LYMPH-ATYPICAL

**Categoria:** White Blood Cell

**Regra:** `morphology.linfocitos_atipicos == true`

**Forca:** moderate

**Descricao:** Linfócitos atípicos presentes

**Significancia Clinica:** Infecção viral (EBV, CMV)

**Fonte:** HemoDoctor + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 37. E-EOS-HIGH

**Categoria:** White Blood Cell

**Regra:** `eosinophils_abs >= 1.5`

**Forca:** moderate

**Descricao:** Eosinófilos ≥ 1.5×10⁹/L

**Significancia Clinica:** Parasitas, alergia, NMP

**Fonte:** Dev Team + Ajustes Dr. Abel

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 38. E-BASO-HIGH

**Categoria:** White Blood Cell

**Regra:** `basophils_abs >= 0.2`

**Forca:** weak

**Descricao:** Basófilos ≥ 0.2×10⁹/L

**Significancia Clinica:** NMP (LMC), alergia

**Fonte:** Dev Team + Ajustes Dr. Abel

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 39. E-MONOCYTOSIS

**Categoria:** White Blood Cell

**Regra:** `monocytes_abs > 1.0`

**Forca:** moderate

**Descricao:** Monócitos > 1.0×10⁹/L

**Significancia Clinica:** LMMC, infecção crônica

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 40. E-LEUCOERITROBLASTOSE

**Categoria:** White Blood Cell

**Regra:** `(morphology.mielocitos == true or morphology.metamielocitos == true) and (morphology.policromasia == true)`

**Forca:** moderate

**Descricao:** Leucoeritroblastose (imaturos + policromasia)

**Significancia Clinica:** Mielofibrose, infiltração medular, sepse

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 41. E-CRP-HIGH

**Categoria:** White Blood Cell

**Regra:** `crp > 10`

**Forca:** weak

**Descricao:** CRP > 10 mg/L

**Significancia Clinica:** Inflamação/infecção

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 42. E-PLT-HIGH

**Categoria:** Platelet

**Regra:** `plt > 450`

**Forca:** moderate

**Descricao:** PLT > 450×10⁹/L

**Significancia Clinica:** Trombocitose (reativa vs clonal)

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 43. E-PLT-VERY-HIGH

**Categoria:** Platelet

**Regra:** `plt >= 650`

**Forca:** strong

**Descricao:** PLT ≥ 650×10⁹/L

**Significancia Clinica:** Trombocitose clonal provável (NMP)

**Fonte:** Dev Team + Ajustes Dr. Abel

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 44. E-PSEUDO-THROMBO

**Categoria:** Platelet

**Regra:** `morphology.aglomerados_plaquetarios == true or mpv > 12`

**Forca:** strong

**Descricao:** Aglomerados plaquetários ou MPV > 12 fL

**Significancia Clinica:** Pseudo-trombocitopenia (EDTA)

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 45. E-THROMBOCYTOSIS-PERSIST

**Categoria:** Platelet

**Regra:** `metadata.persistent_thrombocytosis == true`

**Forca:** moderate

**Descricao:** Trombocitose persistente (>2 CBCs em 2-6 sem)

**Significancia Clinica:** Aumenta suspeita clonal

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 46. E-CLONAL-PROFILE

**Categoria:** Platelet

**Regra:** `(crp <= 10 or crp unknown) and (ferritin <= 30 or ferritin unknown) and (tsat <= 20 or tsat unknown)`

**Forca:** moderate

**Descricao:** Perfil não reativo (CRP/ferritina/TSat normais ou ausentes)

**Significancia Clinica:** Exclusão de causas reativas

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 47. E-PLT-GIGANTES

**Categoria:** Platelet

**Regra:** `morphology.plaquetas_gigantes == true`

**Forca:** moderate

**Descricao:** Plaquetas gigantes presentes

**Significancia Clinica:** NMP, Bernard-Soulier

**Fonte:** SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 48. E-PLT-LOW

**Categoria:** Platelet

**Regra:** `plt < 150`

**Forca:** moderate

**Descricao:** PLT < 150×10⁹/L

**Significancia Clinica:** Trombocitopenia

**Fonte:** HemoDoctor SRS-001

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 49. E-MPV-HIGH

**Categoria:** Platelet

**Regra:** `mpv > 12`

**Forca:** weak

**Descricao:** MPV > 12 fL

**Significancia Clinica:** Plaquetas jovens ou pseudo-trombocitopenia

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 50. E-D-DIMER-HIGH

**Categoria:** Coagulation

**Regra:** `d_dimer > 500`

**Forca:** moderate

**Descricao:** D-dímero > 500 ng/mL

**Significancia Clinica:** CIVD, TEV

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 51. E-FIBRINOGEN-LOW

**Categoria:** Coagulation

**Regra:** `fibrinogenio < 150`

**Forca:** strong

**Descricao:** Fibrinogênio < 150 mg/dL

**Significancia Clinica:** CIVD, hipofibrinogenemia

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 52. E-PT-APTT-PROLONGED

**Categoria:** Coagulation

**Regra:** `(pt > normal_high) or (aptt > normal_high)`

**Forca:** moderate

**Descricao:** PT ou APTT prolongado

**Significancia Clinica:** CIVD, deficiência fatores, anticoagulação

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 53. E-COAG-PANEL-ABNORMAL

**Categoria:** Coagulation

**Regra:** `E-D-DIMER-HIGH and (E-FIBRINOGEN-LOW or E-PT-APTT-PROLONGED)`

**Forca:** strong

**Descricao:** Painel de coagulação anormal (≥2 marcadores)

**Significancia Clinica:** CIVD provável

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 54. E-DIC-SCORE-HIGH

**Categoria:** Coagulation

**Regra:** `dic_isth_score >= 5`

**Forca:** strong

**Descricao:** Score ISTH CIVD ≥ 5

**Significancia Clinica:** CIVD confirmada

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 55. E-JAK2-CALR-MPL-POS

**Categoria:** Molecular

**Regra:** `jak2_pos == true or calr_pos == true or mpl_pos == true`

**Forca:** strong

**Descricao:** JAK2/CALR/MPL positivo

**Significancia Clinica:** NMP (PV, TE, MFP)

**Fonte:** Dev Team + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 56. E-BCR-ABL-POS

**Categoria:** Molecular

**Regra:** `bcr_abl_pos == true`

**Forca:** strong

**Descricao:** BCR-ABL positivo

**Significancia Clinica:** LMC

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 57. E-COOMBS-POS

**Categoria:** Molecular

**Regra:** `coombs_pos == true`

**Forca:** moderate

**Descricao:** Coombs Direto positivo

**Significancia Clinica:** Hemólise autoimune

**Fonte:** Dev Team + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 58. E-G6PD-DEFICIENT

**Categoria:** Molecular

**Regra:** `g6pd_deficient == true`

**Forca:** moderate

**Descricao:** G6PD deficiente

**Significancia Clinica:** Hemólise oxidativa

**Fonte:** Dev Team + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 59. E-PK-DEFICIENT

**Categoria:** Molecular

**Regra:** `pk_deficient == true`

**Forca:** moderate

**Descricao:** Piruvato Quinase deficiente

**Significancia Clinica:** Anemia hemolítica congênita

**Fonte:** Dev Team

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 60. E-HPN-POS

**Categoria:** Molecular

**Regra:** `hpn_pos == true`

**Forca:** strong

**Descricao:** HPN (PNH) - CD55/CD59 deficientes

**Significancia Clinica:** Hemoglobinúria Paroxística Noturna

**Fonte:** Dev Team + SADMH

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 61. E-FLC-RATIO-ABNORMAL

**Categoria:** Molecular

**Regra:** `flc_ratio_abnormal == true`

**Forca:** moderate

**Descricao:** Free Light Chains ratio anormal

**Significancia Clinica:** Mieloma múltiplo, MGUS

**Fonte:** Dev Team + Ajustes Dr. Abel

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 62. E-PMLRARA-POS

**Categoria:** Molecular

**Regra:** `pmlrara_pos == true`

**Forca:** strong

**Descricao:** PML-RARA positivo

**Significancia Clinica:** Leucemia Promielocítica Aguda (LPA/M3)

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 63. E-EPO-HIGH

**Categoria:** Molecular

**Regra:** `epo > normal_high`

**Forca:** moderate

**Descricao:** Eritropoetina elevada

**Significancia Clinica:** Eritrocitose secundária (hipóxia, rim)

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 64. E-EPO-LOW

**Categoria:** Molecular

**Regra:** `epo < normal_low`

**Forca:** moderate

**Descricao:** Eritropoetina baixa

**Significancia Clinica:** Policitemia Vera

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 65. E-TSH-ABNORMAL

**Categoria:** Supplementary Lab

**Regra:** `tsh < 0.5 or tsh > 5.0`

**Forca:** low

**Descricao:** TSH anormal (hypothyroidism or hyperthyroidism)

**Significancia Clinica:** Secondary anemia due to thyroid dysfunction

**Fonte:** Endocrine Society 2023 guidelines

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 66. E-VIT-B12-LOW

**Categoria:** Supplementary Lab

**Regra:** `vitamin_b12 < 200`

**Forca:** moderate

**Descricao:** Vitamin B12 <200 pg/mL

**Significancia Clinica:** Megaloblastic anemia, neuropathy

**Fonte:** WHO 2016 micronutrient guidelines

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 67. E-FOLATO-LOW

**Categoria:** Supplementary Lab

**Regra:** `folate < 3.0`

**Forca:** moderate

**Descricao:** Folate <3.0 ng/mL

**Significancia Clinica:** Megaloblastic anemia

**Fonte:** WHO 2016 micronutrient guidelines

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 68. E-RETICULOCYTES-LOW

**Categoria:** Supplementary Lab

**Regra:** `reticulocytes < 0.5`

**Forca:** high

**Descricao:** Reticulocytes <0.5% (inadequate marrow response)

**Significancia Clinica:** Aplastic anemia, marrow failure, nutritional deficiency

**Fonte:** NCCN 2023 hematology guidelines

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 69. E-RETICULOCYTES-HIGH

**Categoria:** Supplementary Lab

**Regra:** `reticulocytes > 2.0`

**Forca:** moderate

**Descricao:** Reticulocytes >2.0% (appropriate marrow response)

**Significancia Clinica:** Hemolysis, bleeding, or EPO therapy

**Fonte:** NCCN 2023 hematology guidelines

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 70. E-PRE-MCHC-IMPLAUS

**Categoria:** Pre Analytical

**Regra:** `mchc > 37 or mchc < 25`

**Forca:** strong

**Descricao:** MCHC > 37 ou < 25 g/dL (impossível fisiologicamente)

**Significancia Clinica:** Erro pré-analítico (aglutinação, lipemia)

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 71. E-PRE-CLUMPS-SUSPECT

**Categoria:** Pre Analytical

**Regra:** `(plt < 100) and (mpv > 12)`

**Forca:** moderate

**Descricao:** PLT < 100 + MPV > 12 (sem morfologia confirmatória)

**Significancia Clinica:** Suspeita pseudo-trombocitopenia

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 72. E-PRE-HB-HT-INCONSIST

**Categoria:** Pre Analytical

**Regra:** `abs((hb/ht)*100 - mchc) > 2`

**Forca:** moderate

**Descricao:** Inconsistência entre Hb, Ht e MCHC (>2 g/dL)

**Significancia Clinica:** Erro pré-analítico

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 73. E-PRE-COLD-AGGLUTININ

**Categoria:** Pre Analytical

**Regra:** `(mchc > 37) and (mcv < 80) and (hb < config.cutoffs.hb_critical_low[age_sex_group])`

**Forca:** moderate

**Descricao:** MCHC > 37 + microcitose + anemia

**Significancia Clinica:** Suspeita aglutinina fria

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 74. E-PRE-LIPEMIA-SUSPECT

**Categoria:** Pre Analytical

**Regra:** `metadata.sample_lipemic == true`

**Forca:** weak

**Descricao:** Amostra lipêmica (metadata flag)

**Significancia Clinica:** Interferência Hb por lipemia

**Fonte:** Ajustes Dr. Abel Costa

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 75. E-ANEMIA

**Categoria:** Complementary

**Regra:** `hb < config.cutoffs.hb_low[age_sex_group]`

**Forca:** moderate

**Descricao:** Anemia por idade/sexo

**Significancia Clinica:** Múltiplas causas (IDA, ACD, hemólise, aplasia, etc.)

**Fonte:** WHO 2011 anemia criteria

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 76. E-FERRITIN-HIGH-100

**Categoria:** Complementary

**Regra:** `ferritin > 100`

**Forca:** moderate

**Descricao:** Ferritina >100 ng/mL

**Significancia Clinica:** ACD, iron overload, inflammation, malignancy

**Fonte:** NCCN 2023 anemia guidelines

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 77. E-LDH-HIGH

**Categoria:** Complementary

**Regra:** `ldh > config.cutoffs.ldh_high`

**Forca:** high

**Descricao:** LDH elevado

**Significancia Clinica:** Hemolysis, TMA, tissue damage, malignancy

**Fonte:** ISTH 2023 hemolysis criteria

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 78. E-BT-IND-HIGH

**Categoria:** Complementary

**Regra:** `bilirubin_indirect > 1.2`

**Forca:** high

**Descricao:** Bilirrubina indireta >1.2 mg/dL

**Significancia Clinica:** Hemolysis, Gilbert syndrome

**Fonte:** Clinical chemistry reference ranges

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 79. E-CREATININA-HIGH

**Categoria:** Complementary

**Regra:** `creatinine > config.cutoffs.creatinine_high[age_sex_group]`

**Forca:** moderate

**Descricao:** Creatinina elevada (kidney injury)

**Significancia Clinica:** TMA (renal involvement), AKI, CKD

**Fonte:** KDIGO 2023 AKI criteria

**Validacao:**
- [ ] Criterio clinicamente adequado?
- [ ] Cutoff correto para populacao alvo?
- [ ] Faixas pediatricas necessarias?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


## SINDROMES HEMATOLOGICAS


### 1. S-NEUTROPENIA-GRAVE

**Criticidade:** critical

**Logica:** {'any': ['E-ANC-VCRIT', 'E-ANC-CRIT']}

**Evidencias Requeridas:** None

**Evidencias Opcionais:** E-ANC-VCRIT, E-ANC-CRIT

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 2. S-BLASTIC-SYNDROME

**Criticidade:** critical

**Logica:** {'any': ['E-WBC-VERY-HIGH', {'all': ['E-WBC-VERY-HIGH', 'E-PLT-CRIT-LOW']}, {'all': ['E-WBC-VERY-HIGH', 'E-HEMOLYSIS-PATTERN']}, 'E-BLASTS-PRESENT']}

**Evidencias Requeridas:** None

**Evidencias Opcionais:** E-WBC-VERY-HIGH, {'all': ['E-WBC-VERY-HIGH', 'E-PLT-CRIT-LOW']}, {'all': ['E-WBC-VERY-HIGH', 'E-HEMOLYSIS-PATTERN']}, E-BLASTS-PRESENT

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 3. S-TMA

**Criticidade:** critical

**Logica:** {'all': ['E-PLT-CRIT-LOW', 'E-SCHISTOCYTES-GE1PCT'], 'any': ['E-LDH-HIGH', 'E-BT-IND-HIGH', 'E-CREATININA-HIGH']}

**Evidencias Requeridas:** E-PLT-CRIT-LOW, E-SCHISTOCYTES-GE1PCT

**Evidencias Opcionais:** E-LDH-HIGH, E-BT-IND-HIGH, E-CREATININA-HIGH

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 4. S-PLT-CRITICA

**Criticidade:** critical

**Logica:** {'all': ['E-PLT-CRIT-LOW']}

**Evidencias Requeridas:** E-PLT-CRIT-LOW

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 5. S-ANEMIA-GRAVE

**Criticidade:** critical

**Logica:** {'all': ['E-HB-CRIT-LOW']}

**Evidencias Requeridas:** E-HB-CRIT-LOW

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 6. S-NEUTROFILIA-LEFTSHIFT-CRIT

**Criticidade:** critical

**Logica:** {'all': ['E-WBC-HIGH'], 'any': ['E-ANC-HIGH', 'E-LEFT-SHIFT']}

**Evidencias Requeridas:** E-WBC-HIGH

**Evidencias Opcionais:** E-ANC-HIGH, E-LEFT-SHIFT

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 7. S-THROMBOCITOSE-CRIT

**Criticidade:** critical

**Logica:** {'all': ['E-PLT-VERY-HIGH']}

**Evidencias Requeridas:** E-PLT-VERY-HIGH

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 8. S-CIVD

**Criticidade:** critical

**Logica:** {'all': ['E-D-DIMER-HIGH'], 'any': ['E-FIBRINOGEN-LOW', 'E-PT-APTT-PROLONGED']}

**Evidencias Requeridas:** E-D-DIMER-HIGH

**Evidencias Opcionais:** E-FIBRINOGEN-LOW, E-PT-APTT-PROLONGED

**Threshold:** 0.85

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 9. S-APL-SUSPEITA

**Criticidade:** critical

**Logica:** {'all': ['E-PROMIELOCITOS-PRESENT'], 'any': ['E-COAG-PANEL-ABNORMAL', 'E-D-DIMER-HIGH']}

**Evidencias Requeridas:** E-PROMIELOCITOS-PRESENT

**Evidencias Opcionais:** E-COAG-PANEL-ABNORMAL, E-D-DIMER-HIGH

**Threshold:** 0.85

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 10. S-IDA

**Criticidade:** priority

**Logica:** {'all': ['E-MICROCYTOSIS', 'E-RDW-HIGH'], 'any': ['E-IDA-LABS'], 'negative': ['E-INFLAM-HIGH']}

**Evidencias Requeridas:** E-MICROCYTOSIS, E-RDW-HIGH

**Evidencias Opcionais:** E-IDA-LABS

**Exclusoes:** E-INFLAM-HIGH

**Threshold:** 0.8

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 11. S-IDA-INFLAM

**Criticidade:** priority

**Logica:** {'all': ['E-MICROCYTOSIS', 'E-IDA-INFLAM']}

**Evidencias Requeridas:** E-MICROCYTOSIS, E-IDA-INFLAM

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 12. S-ACD

**Criticidade:** priority

**Logica:** {'all': ['E-ANEMIA'], 'any': ['E-FERRITIN-HIGH-100', 'E-CRP-HIGH']}

**Evidencias Requeridas:** E-ANEMIA

**Evidencias Opcionais:** E-FERRITIN-HIGH-100, E-CRP-HIGH

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 13. S-BETA-THAL

**Criticidade:** priority

**Logica:** {'all': ['E-BETA-THAL-TRAIT']}

**Evidencias Requeridas:** E-BETA-THAL-TRAIT

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 14. S-ALFA-THAL

**Criticidade:** priority

**Logica:** {'all': ['E-ALFA-THAL-PATTERN']}

**Evidencias Requeridas:** E-ALFA-THAL-PATTERN

**Threshold:** 0.8

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 15. S-MACRO-B12-FOLATE

**Criticidade:** priority

**Logica:** {'all': ['E-MACROCYTOSIS'], 'any': ['E-B12-FOLATE-LOW']}

**Evidencias Requeridas:** E-MACROCYTOSIS

**Evidencias Opcionais:** E-B12-FOLATE-LOW

**Threshold:** 0.6

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 16. S-HEMOLYSIS

**Criticidade:** priority

**Logica:** {'all': ['E-HEMOLYSIS-PATTERN'], 'any': ['E-ESFEROCITOS-PRESENT', 'E-SCHISTOCYTES-GE1PCT', 'E-HB-SICKLE-MORPH']}

**Evidencias Requeridas:** E-HEMOLYSIS-PATTERN

**Evidencias Opcionais:** E-ESFEROCITOS-PRESENT, E-SCHISTOCYTES-GE1PCT, E-HB-SICKLE-MORPH

**Threshold:** 0.8

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 17. S-APLASIA-RETIC-LOW

**Criticidade:** priority

**Logica:** {'all': ['E-APLASIA-RETIC-LOW']}

**Evidencias Requeridas:** E-APLASIA-RETIC-LOW

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 18. S-LEUCOERITROBLASTOSE

**Criticidade:** priority

**Logica:** {'all': ['E-LEUCOERITROBLASTOSE']}

**Evidencias Requeridas:** E-LEUCOERITROBLASTOSE

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 19. S-HB-SICKLE

**Criticidade:** priority

**Logica:** {'all': ['E-HB-SICKLE-MORPH']}

**Evidencias Requeridas:** E-HB-SICKLE-MORPH

**Threshold:** 0.9

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 20. S-PSEUDO-THROMBO

**Criticidade:** priority

**Logica:** {'any': ['E-PSEUDO-THROMBO', 'E-PRE-CLUMPS-SUSPECT']}

**Evidencias Requeridas:** None

**Evidencias Opcionais:** E-PSEUDO-THROMBO, E-PRE-CLUMPS-SUSPECT

**Threshold:** 1

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 21. S-PTI

**Criticidade:** priority

**Logica:** {'all': ['E-PLT-LOW'], 'negative': ['E-PSEUDO-THROMBO', 'E-COAG-PANEL-ABNORMAL', 'E-HEMOLYSIS-PATTERN']}

**Evidencias Requeridas:** E-PLT-LOW

**Exclusoes:** E-PSEUDO-THROMBO, E-COAG-PANEL-ABNORMAL, E-HEMOLYSIS-PATTERN

**Threshold:** 0.75

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 22. S-THROMBOCITOSE

**Criticidade:** priority

**Logica:** {'all': ['E-PLT-HIGH']}

**Evidencias Requeridas:** E-PLT-HIGH

**Threshold:** 0.6

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 23. S-LYMPHOPROLIFERATIVE

**Criticidade:** priority

**Logica:** {'all': ['E-LYMPHOCYTOSIS']}

**Evidencias Requeridas:** E-LYMPHOCYTOSIS

**Threshold:** 0.6

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 24. S-EOSINOFILIA

**Criticidade:** priority

**Logica:** {'all': ['E-EOS-HIGH']}

**Evidencias Requeridas:** E-EOS-HIGH

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 25. S-MONOCITOSE-CRONICA

**Criticidade:** priority

**Logica:** {'all': ['E-MONOCYTOSIS']}

**Evidencias Requeridas:** E-MONOCYTOSIS

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 26. S-BASOFILIA

**Criticidade:** priority

**Logica:** {'all': ['E-BASO-HIGH']}

**Evidencias Requeridas:** E-BASO-HIGH

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 27. S-CML

**Criticidade:** priority

**Logica:** {'all': ['E-BCR-ABL-POS'], 'any': ['E-LEFT-SHIFT', 'E-WBC-HIGH', 'E-BASO-HIGH']}

**Evidencias Requeridas:** E-BCR-ABL-POS

**Evidencias Opcionais:** E-LEFT-SHIFT, E-WBC-HIGH, E-BASO-HIGH

**Threshold:** 0.8

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 28. S-MPN-POSSIBLE

**Criticidade:** priority

**Logica:** {'any': ['E-PLT-HIGH', 'E-WBC-HIGH'], 'all': ['E-JAK2-CALR-MPL-POS'], 'negative': ['E-BCR-ABL-POS']}

**Evidencias Requeridas:** E-JAK2-CALR-MPL-POS

**Evidencias Opcionais:** E-PLT-HIGH, E-WBC-HIGH

**Exclusoes:** E-BCR-ABL-POS

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 29. S-PV

**Criticidade:** priority

**Logica:** {'any': ['E-HB-HIGH', 'E-HCT-HIGH']}

**Evidencias Requeridas:** None

**Evidencias Opcionais:** E-HB-HIGH, E-HCT-HIGH

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 30. S-ERITROCITOSE-SECUNDARIA

**Criticidade:** priority

**Logica:** {'any': ['E-HB-HIGH', 'E-HCT-HIGH']}

**Evidencias Requeridas:** None

**Evidencias Opcionais:** E-HB-HIGH, E-HCT-HIGH

**Threshold:** 0.6

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 31. S-EVANS

**Criticidade:** priority

**Logica:** {'all': ['E-HB-CRIT-LOW', 'E-PLT-LOW'], 'any': ['E-COOMBS-POS']}

**Evidencias Requeridas:** E-HB-CRIT-LOW, E-PLT-LOW

**Evidencias Opcionais:** E-COOMBS-POS

**Threshold:** 0.6

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 32. S-PANCYTOPENIA

**Criticidade:** priority

**Logica:** {'all': ['E-ANEMIA', 'E-PLT-LOW', 'E-WBC-LOW']}

**Evidencias Requeridas:** E-ANEMIA, E-PLT-LOW, E-WBC-LOW

**Threshold:** 0.7

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 33. S-MM-MGUS

**Criticidade:** priority

**Logica:** {'all': ['E-ROULEAUX-PRESENT'], 'any': ['E-HB-CRIT-LOW', 'E-FLC-RATIO-ABNORMAL']}

**Evidencias Requeridas:** E-ROULEAUX-PRESENT

**Evidencias Opcionais:** E-HB-CRIT-LOW, E-FLC-RATIO-ABNORMAL

**Threshold:** 0.6

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 34. S-PRE-ANALITICO

**Criticidade:** review_sample

**Logica:** {'any': ['E-PRE-MCHC-IMPLAUS', 'E-PRE-HB-HT-INCONSIST', 'E-PRE-COLD-AGGLUTININ', 'E-PRE-LIPEMIA-SUSPECT']}

**Evidencias Requeridas:** None

**Evidencias Opcionais:** E-PRE-MCHC-IMPLAUS, E-PRE-HB-HT-INCONSIST, E-PRE-COLD-AGGLUTININ, E-PRE-LIPEMIA-SUSPECT

**Threshold:** 0.8

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


### 35. S-INCONCLUSIVO

**Criticidade:** routine

**Logica:** {'all': []}

**Evidencias Requeridas:** None

**Threshold:** 0

**Validacao:**
- [ ] Logica ALL/ANY correta?
- [ ] Evidencias suficientes?
- [ ] Threshold adequado?

**Comentarios do Hematologista:**
```
_________________________________________________________________
```

---


## PROXIMOS PASSOS CLINICOS (Amostra)


### 1. trigger-anemia-grave

**Sindrome Alvo:** None

**Nivel:** critical

**Recomendacoes:** Reticulócitos; Esfregaço urgente; LDH; Haptoglobina; BT indireta

**Racional:** Diferenciar regenerativa (hemólise, sangramento) vs hiporregenerativa (aplasia, infiltração); Avaliar morfologia (esquistócitos, blastos, diseritropoese); Marcador de hemólise/TMA/turnover celular; Hemólise intravascular; Hemólise (icterícia pré-hepática)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 2. trigger-ida

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Ferritina; TSat; CRP; CBC repeat (2-4 semanas)

**Racional:** Confirmar IDA (ferritina <30 ng/mL) vs ACD (ferritina 30-100 com inflamação); TSat <20% confirma deficiência de ferro funcional; Diferenciar IDA pura (CRP normal) vs ACD/IDA-inflam (CRP >10 mg/L); Avaliar resposta à reposição de ferro

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 3. trigger-beta-thal

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** HbA2 (eletroforese de hemoglobina); Ferritina

**Racional:** HbA2 >3.5% confirma β-talassemia trait; Excluir IDA concomitante (comum em mulheres)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 4. trigger-alfa-thal

**Sindrome Alvo:** None

**Nivel:** routine

**Recomendacoes:** Estudo molecular para α-talassemia; Aconselhamento genético

**Racional:** HbA2 normal com microcitose + RBC elevado sugere α-thal trait; Avaliar risco reprodutivo (hidropsia fetal se ambos pais α-thal)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 5. trigger-acd

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Ferritina; CRP; TSat; Investigar doença inflamatória/crônica de base

**Racional:** ACD: ferritina 30-100 (leve) ou >100 (moderada); Marcador de inflamação (ACD esperado se CRP >10 mg/L); TSat <20% em ACD (ferro sequestrado, não deficiente); ACD é secundária (artrite reumatoide, neoplasia, infecção crônica, DRC)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 6. trigger-macro-b12-folate

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Vitamina B12; Folato; Anticorpo anti-fator intrínseco; LDH; CBC repeat (4-8 semanas)

**Racional:** B12 <200 pg/mL = deficiência; 200-300 = limítrofe; Folato <3.1 ng/mL = deficiência; Se B12 baixa: confirmar anemia perniciosa (autoimune); Elevado em megaloblástica (destruição intramedular); Avaliar resposta à reposição (normalização MCV)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 7. trigger-hemolysis

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Reticulócitos; LDH; Haptoglobina; BT indireta; DAT (Coombs direto); G6PD; Piruvato quinase (PK)

**Racional:** Reticulócitos >100×10^9/L = hemólise regenerativa; LDH >500 U/L sugere hemólise ou TMA; Haptoglobina <40 mg/dL = hemólise intravascular; BT indireta >1.0 mg/dL = hemólise (icterícia pré-hepática); Se positivo: anemia hemolítica autoimune (AIHA); Se hemólise episódica pós-oxidante (favismo, infecção); Se hemólise crônica desde infância (enzimopenia hereditária)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 8. trigger-aplasia-retic-low

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Reticulócitos; Parvovírus B19 (IgM/IgG); Esfregaço + leucograma

**Racional:** Reticulócitos <20×10^9/L = hiporregenerativa (aplasia, infiltração); Se anemia súbita em paciente com hemólise de base (aplasia transitória); Avaliar diseritropoese, citopenias associadas (MDS, aplasia)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 9. trigger-mds

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Esfregaço detalhado; Citogenética (cariótipo medular); NGS painel mieloide; Medula óssea (aspirado + biópsia)

**Racional:** Displasia em ≥10% das células de ≥1 linhagem (hiposegmentação, pseudo-Pelger); Del(5q), trissomia 8, -7/del(7q) = MDS; Mutações SF3B1, ASXL1, TP53 = prognóstico MDS; Confirmar displasia, % blastos, celularidade, fibrose

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 10. trigger-mm-mgus

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Eletroforese de proteínas séricas + Imunofixação; Cadeias leves livres (FLC κ/λ); Cálcio sérico; Creatinina; Medula óssea + Radiografia esqueleto

**Racional:** Detectar pico monoclonal (gamopatia); Avaliar FLC ratio (κ/λ <0.26 ou >1.65 = clonal); Hipercalcemia = critério CRAB (mieloma ativo); Insuficiência renal = critério CRAB; Plasmocitose >10% + lesões líticas = mieloma múltiplo

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


### 11. trigger-pnh

**Sindrome Alvo:** None

**Nivel:** priority

**Recomendacoes:** Citometria de fluxo (CD55/CD59); LDH; D-dímero

**Racional:** Clone HPN (deficiência GPI) se ≥1% granulócitos; Marcador de hemólise intravascular (elevado em HPN); Avaliar risco trombótico (comum em HPN)

**Validacao:**
- [ ] Recomendacoes apropriadas?
- [ ] Urgencia correta?

**Comentarios:**
```
_________________________________________________________________
```

---


*Ver Excel para todos os 40 triggers*


## FORMULARIO DE VALIDACAO FINAL


### Aprovacao Geral

- [ ] Todas as 79 evidencias foram revisadas
- [ ] Todas as 35 sindromes foram revisadas
- [ ] Todos os next steps foram revisados

### Decisao Final

- [ ] APROVADO sem restricoes
- [ ] APROVADO com ressalvas (detalhar acima)
- [ ] NAO APROVADO (detalhar motivos acima)

**Nome do Hematologista:** ___________________________

**CRM:** ___________________________

**Data:** ___________________________

**Assinatura:** ___________________________
