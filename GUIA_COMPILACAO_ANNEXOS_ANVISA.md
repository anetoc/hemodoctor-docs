# 📄 Guia de Compilação - Annexos ANVISA (CER-001)

**Data:** 12 de Outubro de 2025  
**Objetivo:** Compilar Annexos B, D, E para submissão ANVISA  
**Status:** 🟡 EM PREPARAÇÃO  
**Deadline:** 20 de Outubro de 2025 (8 dias)

---

## 🎯 RESUMO EXECUTIVO

### Annexos Necessários

| Annex | Título | Páginas | Status | Ação |
|-------|--------|---------|--------|------|
| **B** | Lista Completa de 43 Estudos | ~15 | ⏳ | Compilar tabela |
| **D** | IRB Approval Letters (CEP) | ~32 | ⏳ | Obter PDFs assinados |
| **E** | Study Protocols (Retro + Prosp) | ~80 | ⏳ | Consolidar protocolos |
| **TOTAL** | | **~127 págs** | | |

---

## 📋 ANNEX B - Lista de 43 Estudos

### Objetivo

Fornecer lista completa e detalhada dos 43 estudos científicos utilizados como evidência clínica no CER-001.

### Formato Requerido

**Tabela estruturada contendo:**
1. Número sequencial (1-43)
2. Autores (et al. para >3 autores)
3. Título do estudo
4. Revista/Journal (nome + volume + páginas)
5. Ano de publicação
6. Tipo de estudo (RCT, observacional, revisão sistemática, etc.)
7. Tamanho amostral (n)
8. Nível de evidência (Oxford CEBM: I, II, III, IV, V)
9. Métricas-chave (sensibilidade/especificidade se disponível)
10. DOI ou URL

### Estrutura do Documento

```markdown
# ANNEX B - Complete List of 43 Included Studies

## Table B.1: Diagnostic Accuracy Studies (n=18)

| # | Author (Year) | Title | Journal | n | Sens (%) | Spec (%) | Evidence Level | DOI |
|---|--------------|-------|---------|---|----------|----------|----------------|-----|
| 1 | Smith et al. (2022) | AI-based CBC analysis for anemia detection | J Clin Pathol 2022;75(3):234-241 | 1,234 | 92.3 | 87.1 | II | 10.1136/jcp.2022.123456 |
| 2 | ... | ... | ... | ... | ... | ... | ... | ... |

## Table B.2: Safety and Adverse Event Studies (n=10)

[Similar structure]

## Table B.3: Usability and Workflow Studies (n=8)

[Similar structure]

## Table B.4: Economic/Cost-Effectiveness Studies (n=4)

[Similar structure]

## Table B.5: Systematic Reviews/Meta-Analyses (n=3)

[Similar structure]
```

### Ação Necessária

**Opção 1: Buscar estudos reais (Recomendado para submissão real)**
```bash
# Bases de dados a consultar:
- PubMed: https://pubmed.ncbi.nlm.nih.gov/
- SciELO: https://scielo.org/
- IEEE Xplore: https://ieeexplore.ieee.org/
- Cochrane Library: https://www.cochranelibrary.com/

# Termos de busca (MeSH):
"hematology" OR "complete blood count" OR "CBC" OR "anemia diagnosis"
AND "artificial intelligence" OR "machine learning" OR "clinical decision support"
AND "sensitivity" OR "specificity" OR "diagnostic accuracy"
Filters: 2018-2024, English/Portuguese
```

**Opção 2: Utilizar estudos de referência do HemoDoctor**
```bash
# Verificar se existem estudos já catalogados em:
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_REFERENCIAS/artigos_cientificos
ls -lh

# Se existir lista de referências, compilar em formato ANVISA
```

**Opção 3: Template com estudos representativos (Para draft/revisão)**
- Criar template com estudos genéricos de IA em hematologia
- Marcar claramente como "DRAFT - PENDING FINAL REFERENCES"
- Completar antes de submissão oficial

### Timeline

- **13 Out:** Buscar 43 estudos (6-8 horas)
- **14 Out:** Compilar tabela (3-4 horas)
- **15 Out:** Revisão de qualidade (2 horas)
- **16 Out:** PDF final Annex B (1 hora)

**Responsável:** @clinical-evidence-specialist

---

## 📋 ANNEX D - IRB Approval Letters (CEP)

### Objetivo

Fornecer cartas de aprovação do Comitê de Ética em Pesquisa (CEP) para estudos retrospectivo e prospectivo.

### Documentos Necessários

#### D.1 - CEP Hospital Universitário - Protocol 2023.1.456.789

**Cartas requeridas:**
1. **Aprovação Inicial** (2023-01-15)
   - Protocolo do estudo retrospectivo
   - Waiver de TCLE (dados anonimizados)
   - Aprovação LGPD Article 11

2. **Emenda 1** (2024-02-10)
   - Protocolo do estudo prospectivo
   - Modelo de consentimento opt-out
   - Justificativa de mudança de metodologia

3. **Emenda 2** (2025-08-20)
   - Extensão PMCF (Post-Market Clinical Follow-up)
   - Plano de monitoramento de 24 meses
   - Data Safety Monitoring Board (DSMB) charter

#### D.2 - Informed Consent Documents

4. **TCLE Waiver** (estudo retrospectivo)
   - Justificativa LGPD Article 11
   - Parecer favorável CEP

5. **Opt-Out Consent Model** (estudo prospectivo)
   - Termo de informação ao paciente
   - Modelo de opt-out
   - Aprovação CEP

### Formato Requerido

**PDFs autênticos:**
- Logo da instituição (CEP)
- Assinatura do presidente do CEP
- Carimbo oficial da instituição
- Número CAAE (Plataforma Brasil)
- Data de emissão

### Ação Necessária

**CRÍTICO:** Documentos devem ser REAIS e ASSINADOS

**Se já existem:**
```bash
# Buscar aprovações CEP existentes
cd /Users/abelcosta/Documents/HemoDoctor/docs/WORKSPACES/01_ETHICS_CEP/Documentos
find . -name "*CEP*" -o -name "*CAAE*" -o -name "*IRB*"

# Se encontrado, copiar para annexo D
```

**Se NÃO existem:**
1. **Opção A (Recomendado):** Submeter protocolo real ao CEP
   - Usar documentos em `01_ETHICS_CEP/`
   - Submeter Plataforma Brasil
   - Aguardar aprovação (60-90 dias)
   - ⚠️ IMPACTA TIMELINE!

2. **Opção B:** Criar draft com template CEP
   - Usar template CEP padrão
   - Marcar como "PENDING CEP SUBMISSION"
   - Bloqueia submissão ANVISA até obter real

3. **Opção C:** Usar dados de estudo multicêntrico existente
   - Se HemoDoctor tem parceria com instituição já aprovada
   - Obter cópia da aprovação CEP

### Timeline

**Cenário 1 (Aprovação já existe):**
- **13 Out:** Localizar PDFs (2 horas)
- **14 Out:** Compilar Annex D (1 hora)

**Cenário 2 (Precisa submeter CEP):**
- **13-20 Out:** Preparar e submeter Plataforma Brasil (5 dias)
- **Nov-Dez:** Aguardar parecer CEP (60 dias)
- **Jan 2026:** Receber aprovação e compilar Annex D
- ⚠️ **ANVISA submission adiada para Q1 2026**

**Recomendação:** Verificar IMEDIATAMENTE se aprovação CEP já existe!

**Responsável:** Dr. Abel Costa + @cep-protocol-specialist

---

## 📋 ANNEX E - Study Protocols

### Objetivo

Fornecer protocolos completos dos estudos retrospectivo e prospectivo, incluindo metodologia, análise estatística e resultados.

### Documentos Necessários

#### E.1 - Retrospective Study Protocol (v1.0, 2023-01-01)

**Conteúdo (25 páginas):**
1. **Study Title**
   - "Retrospective Validation of HemoDoctor SaMD for Automated CBC Analysis"

2. **Objectives**
   - Primary: Validate sensitivity ≥90% for severe anemia detection
   - Secondary: Assess specificity, PPV, NPV, diagnostic accuracy

3. **Methodology**
   - Design: Retrospective observational study
   - Population: n=2,847 CBC cases (Jan-Dec 2023)
   - Inclusion/exclusion criteria
   - Data source: 3 laboratories (different complexity levels)

4. **Statistical Analysis Plan**
   - Sample size justification (power analysis)
   - Primary outcome: Sensitivity with 95% CI
   - Secondary outcomes: Specificity, PPV, NPV, AUC-ROC
   - Subgroup analyses: Age groups, anemia types

5. **Results**
   - Sensitivity: 91.2% (95% CI: 89.1%-93.3%) ✅
   - Specificity: 83.4% (95% CI: 81.0%-85.8%) ✅
   - Tables and figures (ROC curves, confusion matrix)

6. **Ethics and Regulatory**
   - CEP approval Protocol 2023.1.456.789
   - LGPD compliance (anonymized data)

#### E.2 - Prospective Study Protocol (v2.0, 2024-02-01)

**Conteúdo (30 páginas):**
1. **Study Title**
   - "Prospective Real-World Validation of HemoDoctor SaMD in Clinical Practice"

2. **Objectives**
   - Primary: Confirm sensitivity ≥90% in real-world settings
   - Secondary: Assess TTD reduction, user satisfaction, safety

3. **Methodology**
   - Design: Prospective observational study
   - Population: n=1,523 CBC cases (Mar-Aug 2024)
   - Real-world deployment in 3 sites
   - Healthcare professional training (4 hours)

4. **Statistical Analysis Plan**
   - Primary outcome: Sensitivity with 95% CI
   - Secondary outcomes: TTD, SUS score, adverse events
   - Interim analysis at n=750

5. **Results**
   - Confirmed sensitivity ≥90% ✅
   - TTD reduction: 35% (2.3 min vs 8.7 min, p<0.001) ✅
   - User satisfaction: SUS score 78.5/100 (Good) ✅
   - No serious adverse events (SAE) ✅

6. **Ethics and Regulatory**
   - CEP approval Amendment 1 (2024-02-10)
   - Opt-out consent model
   - LGPD compliance

### Formato Requerido

**Estrutura por protocolo:**
```markdown
# STUDY PROTOCOL E.[1|2]

## 1. PROTOCOL SUMMARY
- Title
- Protocol version & date
- Principal Investigator
- Study sites
- Study period
- Ethics approval (CAAE number)

## 2. BACKGROUND AND RATIONALE
- Clinical need
- HemoDoctor SaMD description
- Study justification

## 3. OBJECTIVES
- Primary objective
- Secondary objectives
- Exploratory objectives

## 4. STUDY DESIGN
- Type (retrospective/prospective, observational)
- Study population
- Inclusion/exclusion criteria
- Sample size calculation

## 5. STUDY PROCEDURES
- Data collection methods
- HemoDoctor SaMD workflow
- Reference standard (gold standard)

## 6. DATA MANAGEMENT
- Case report forms (CRFs)
- Data entry and validation
- Database management

## 7. STATISTICAL ANALYSIS PLAN
- Primary endpoint analysis
- Secondary endpoint analysis
- Subgroup analyses
- Missing data handling

## 8. ETHICS AND REGULATORY
- CEP approval
- Informed consent (or waiver)
- LGPD compliance
- Adverse event reporting

## 9. STUDY TIMELINE
- Milestones
- Interim analyses
- Final report

## 10. REFERENCES
- Guidelines (ISO 14155, ICH-GCP)
- Literature

## APPENDICES
- Sample size calculation
- Statistical code (R/Python)
- CRFs
- Consent forms
```

### Ação Necessária

**Opção 1: Usar protocolos do CONSOLIDADO v2.0**
```bash
# Verificar se protocolos já existem
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/01_SUBMISSAO_CEP/PROTOCOLO
ls -lh

# Se PROJ-001 e PROJ-002 existem, adaptar para Annex E
```

**Opção 2: Criar protocolos baseados no CER-001**
- Extrair metodologia do CER-001 (já documentada)
- Expandir para formato completo de protocolo
- Adicionar statistical analysis plan detalhado
- Incluir resultados completos

**Opção 3: Template para draft**
- Criar template genérico
- Marcar seções "TO BE COMPLETED"
- Usar para revisão interna
- Completar antes de submissão oficial

### Timeline

- **14 Out:** Criar E.1 (Retrospective Protocol) - 6 horas
- **15 Out:** Criar E.2 (Prospective Protocol) - 6 horas
- **16 Out:** Revisão de qualidade ambos - 3 horas
- **17 Out:** PDF final Annex E - 2 horas

**Responsável:** @clinical-evidence-specialist + @biostatistics-specialist

---

## 📊 CRONOGRAMA CONSOLIDADO

### Semana 1 (14-18 Out)

| Dia | Annex B | Annex D | Annex E | Responsável |
|-----|---------|---------|---------|-------------|
| **13 Out (Dom)** | Buscar 43 estudos | Verificar se CEP existe | - | @clinical-evidence-specialist |
| **14 Out (Seg)** | Compilar tabela | Localizar PDFs ou preparar templates | Criar Protocol E.1 | @clinical-evidence-specialist |
| **15 Out (Ter)** | Revisão qualidade | Compilar Annex D | Criar Protocol E.2 | @clinical-evidence-specialist + @biostatistics-specialist |
| **16 Out (Qua)** | PDF final | PDF final (se PDFs existem) | Revisão qualidade | QA Review |
| **17 Out (Qui)** | - | - | PDF final | Final approval |
| **18 Out (Sex)** | - | Submeter CEP (se necessário) | - | @cep-protocol-specialist |

### Entrega Final

**17 Out 2025 - 23:59 BRT:**
- ✅ Annex B (PDF, ~15 páginas)
- ✅ Annex D (PDF, ~32 páginas) ou PENDING se aguarda CEP
- ✅ Annex E (PDF, ~80 páginas)

**Total:** 127 páginas de annexos compilados

---

## ⚠️ RISCOS E MITIGAÇÕES

### Risco 1: Aprovação CEP não existe

**Probabilidade:** ALTA (60%)  
**Impacto:** CRÍTICO (bloqueia ANVISA)

**Mitigação:**
1. Verificar IMEDIATAMENTE status CEP (13 Out)
2. Se não existe: Submeter urgência Plataforma Brasil
3. Negociar com ANVISA: Submission conditional (pending CEP)
4. Usar dados de estudo multicêntrico já aprovado

### Risco 2: Estudos científicos (Annex B) não disponíveis

**Probabilidade:** MÉDIA (30%)  
**Impacto:** MÉDIO (reduz qualidade CER)

**Mitigação:**
1. Usar estudos open-access (PubMed Central, SciELO)
2. Solicitar papers via ResearchGate
3. Substituir estudos inacessíveis por similares
4. Priorizar systematic reviews/meta-analyses (maior impacto)

### Risco 3: Protocolos incompletos (Annex E)

**Probabilidade:** BAIXA (20%)  
**Impacto:** MÉDIO (requer retrabalho)

**Mitigação:**
1. Usar templates ISO 14155:2020
2. Expandir metodologia já descrita em CER-001
3. Revisar com @biostatistics-specialist
4. Validar contra checklist ANVISA RDC 657/2022

---

## 📞 PRÓXIMA AÇÃO IMEDIATA

### Segunda-feira, 14 de Outubro - 09:00

**CRÍTICO - P0:**
1. [ ] Verificar se aprovação CEP existe
2. [ ] Se SIM: Localizar PDFs e copiar
3. [ ] Se NÃO: Preparar submissão urgente Plataforma Brasil

**ALTA PRIORIDADE:**
4. [ ] Iniciar busca 43 estudos (Annex B)
5. [ ] Verificar protocolos em CONSOLIDADO v2.0

**Agentes:**
- @clinical-evidence-specialist (Annexos B e E)
- @cep-protocol-specialist (Annex D - CEP)
- @biostatistics-specialist (Annex E - Statistical plans)

---

## ✅ CHECKLIST DE QUALIDADE

### Annex B
- [ ] 43 estudos listados
- [ ] Todos com DOI válido
- [ ] Níveis de evidência classificados
- [ ] Métricas de desempenho extraídas
- [ ] Tabelas formatadas (ANVISA style)

### Annex D
- [ ] Aprovação CEP inicial (2023)
- [ ] Emenda 1 (2024)
- [ ] Emenda 2 (2025)
- [ ] Todos com assinatura e carimbo
- [ ] Número CAAE visível
- [ ] Logos institucionais claras

### Annex E
- [ ] Protocolo retrospectivo completo (25 pág)
- [ ] Protocolo prospectivo completo (30 pág)
- [ ] Statistical analysis plans detalhados
- [ ] Resultados completos incluídos
- [ ] Aprovação CEP referenciada
- [ ] Figuras e tabelas numeradas

---

**Status:** 🟡 AGUARDANDO INÍCIO  
**Deadline:** 17 Out 2025 (5 dias)  
**Criticidade:** 🔴 P0 (bloqueia ANVISA submission)

---

**Última Atualização:** 12 de Outubro de 2025 - 23:55 BRT  
**Próxima Revisão:** 14 de Outubro de 2025 (início compilação)

