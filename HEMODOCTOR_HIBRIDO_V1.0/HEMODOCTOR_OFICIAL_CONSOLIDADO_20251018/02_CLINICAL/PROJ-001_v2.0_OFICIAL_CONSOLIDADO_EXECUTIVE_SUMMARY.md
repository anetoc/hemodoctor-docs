# PROJ-001 — Protocolo de Pesquisa Clínica
## Validação Prospectiva do Sistema HemoDoctor v3.x

**Código do Estudo:** HDOC-PROSP-003
**Versão do Protocolo:** v2.0 OFICIAL CONSOLIDADO OFICIAL CONSOLIDADO
**Data:** 2025-10-10
**Status:** Aguardando definições finais e submissão ao CEP

---

## 1. INFORMAÇÕES GERAIS

### 1.1 Título do Estudo

**Título Principal (Português):**
Validação Prospectiva do Sistema HemoDoctor v3.x para Diagnóstico Hematológico em População Pediátrica e Adulta: Estudo Multicêntrico Brasileiro

**Título Principal (Inglês):**
Prospective Validation of HemoDoctor v3.x System for Hematological Diagnosis in Pediatric and Adult Populations: A Brazilian Multicenter Study

**Título Resumido:**
HemoDoctor v3.x: Validação Prospectiva Multicêntrica

### 1.2 Identificação

| Campo | Valor |
|-------|-------|
| **Código do Protocolo** | HDOC-PROSP-003 |
| **Versão** | v2.0 OFICIAL CONSOLIDADO OFICIAL CONSOLIDADO |
| **Data da Versão** | 10 de outubro de 2025 |
| **Versão Anterior** | N/A (Novo estudo) |
| **Registro Plataforma Brasil** | {CAAE: A ser gerado após submissão} |
| **Registro ReBEC** | {RBR: A ser obtido} |

### 1.3 Equipe de Pesquisa

| Papel | Nome | Instituição | Contato | Qualificações |
|-------|------|-------------|---------|---------------|
| **Investigador Principal (PI)** | {A DEFINIR} | {Hospital/Universidade} | {email@institution.br} | Hematologista, CRM XXXXX, Doutor em Hematologia, Experiência >5 anos em pesquisa clínica |
| **Co-Investigador (Pediatria)** | {A DEFINIR} | {Hospital Pediátrico} | {email@pediatria.br} | Hematologista Pediátrico, CRM XXXXX, Especialista em Oncohematologia Pediátrica |
| **Estatístico** | {A DEFINIR} | {Universidade} | {email@stats.br} | PhD em Bioestatística, Experiência em estudos diagnósticos |
| **Coordenador de Pesquisa** | {A DEFINIR} | {Instituição} | {email@coord.br} | Enfermeiro de Pesquisa Clínica, Certificação GCP |
| **Monitor Clínico** | {A DEFINIR - CRO} | {CRO Name} | {email@cro.br} | Monitor Clínico Certificado, Experiência em dispositivos médicos |

### 1.4 Instituições Participantes

**Instituição Proponente:**
{Nome da Instituição Principal}
{Endereço completo}
CNPJ: {XX.XXX.XXX/XXXX-XX}
CEP: {XXXXX-XXX}

**Centros Participantes (5 centros, multicêntrico):**

1. **Hospital Universitário - USP (SP)** - Site Principal (Adultos + Pediátricos)
   - Amostra prevista: n=870 (30% do total)

2. **Hospital das Clínicas - UNICAMP (SP)** - Adultos
   - Amostra prevista: n=580 (20% do total)

3. **Hospital Sírio-Libanês (SP)** - Adultos
   - Amostra prevista: n=580 (20% do total)

4. **Hospital Pequeno Príncipe - Curitiba (PR)** - Pediátrico
   - Amostra prevista: n=435 (15% do total)

5. **Hospital Sabará - São Paulo (SP)** - Pediátrico
   - Amostra prevista: n=435 (15% do total)

### 1.5 Patrocínio e Financiamento

| Campo | Valor |
|-------|-------|
| **Patrocinador Principal** | HemoDoctor Sistemas Médicos Ltda (CNPJ: XX.XXX.XXX/XXXX-XX) |
| **Tipo de Patrocínio** | Misto: Industry-sponsored + Fomento público |
| **Financiamento** | PIPE-FAPESP (R$ 800.000) + Recursos Próprios (R$ 400.000) = **Total: R$ 1.200.000** |
| **Status PIPE** | Proposta em elaboração (submissão prevista Q1/2026) |
| **Conflito de Interesses** | PI e equipe: Não possuem vínculos financeiros com HemoDoctor Ltda além do financiamento de pesquisa. Declaração completa de conflitos submetida ao CEP (Anexo A). Software fornecido sem custo durante estudo. |

---

## 2. RESUMO EXECUTIVO (ABSTRACT)

**Contexto:** As doenças hematológicas representam importante causa de morbimortalidade em populações pediátrica e adulta no Brasil. A interpretação de hemogramas completos (CBC) em hospitais de alto volume é desafiadora devido à sobrecarga de trabalho, variabilidade inter-observador e risco de erros diagnósticos, especialmente em condições críticas como anemia grave, trombocitopenia e neutropenia febril. Sistemas de apoio à decisão clínica (CDSS) baseados em inteligência artificial têm potencial para melhorar acurácia diagnóstica e eficiência, porém evidências robustas em contexto brasileiro são escassas.

**Objetivo:** Validar prospectivamente o desempenho diagnóstico do sistema HemoDoctor v3.x (Software as a Medical Device - SaMD) em população pediátrica (1-17 anos) e adulta (≥18 anos), avaliando sensibilidade, especificidade e segurança em uso real em hospitais brasileiros.

**Desenho:** Estudo prospectivo, observacional, multicêntrico, de acurácia diagnóstica, com análise blinded do gold standard (revisão por hematologista independente).

**População:** N=2.900 pacientes consecutivos submetidos a hemograma completo (CBC) em 5 centros brasileiros: 1.300 adultos (18+ anos) e 1.560 pediátricos (1-17 anos). Período de recrutamento: 8 meses (2026).

**Intervenção (Teste Índice):** HemoDoctor v3.x analisa automaticamente CBCs e gera classificações hematológicas (ex: anemia ferropriva, trombocitopenia imune, neutropenia febril) com score de confiança. Análise paralela (não interfere no cuidado padrão durante estudo).

**Comparador (Gold Standard):** Revisão independente por hematologista certificado, blinded para resultado do HemoDoctor, com acesso a dados clínicos e exames complementares quando disponíveis. Adjudicação de casos discrepantes por segundo hematologista.

**Desfecho Primário:** Sensibilidade para classificações hematológicas (alvo: ≥90%, IC 95%, teste de não-inferioridade com margem de 5%).

**Desfechos Secundários:** Especificidade (alvo: ≥80%), valores preditivos positivo/negativo (PPV/NPV), curva ROC-AUC (alvo: ≥0.92), desempenho estratificado por faixa etária pediátrica (5 grupos), satisfação do usuário (SUS ≥70), eventos adversos relacionados ao software.

**Análise Estatística:** Análise primária por teste de proporção de uma amostra (exato binomial), poder de 90%, alfa 0,05 (unilateral). Análises de subgrupos pré-especificadas: idade (pediátrico vs adulto), condição hematológica (anemia, plaquetopenia, leucopenia), gravidade. Tamanho amostral justificado por power analysis formal (ver Apêndice A).

**Considerações Éticas:** Estudo aprovado por CEP institucional e CONEP (se aplicável). Consentimento informado obrigatório (TCLE para adultos, TCLE + Termo de Assentimento para pediátricos ≥7 anos). Risco mínimo (estudo observacional, não interfere em conduta clínica). Confidencialidade garantida por anonimização de dados (LGPD compliance). DPIA (Data Protection Impact Assessment) realizado.

**Relevância:** Este estudo fornecerá evidência clínica robusta para suporte à aprovação regulatória do HemoDoctor v3.x junto à ANVISA (Classe III, RDC 657/2022), além de informar tomada de decisão sobre adoção de CDSS em hematologia no Sistema Único de Saúde (SUS). É o maior estudo prospectivo de validação de CDSS hematológico em população brasileira, com foco em população pediátrica frequentemente subrepresentada em estudos de dispositivos médicos.

**Palavras-chave:** Software como Dispositivo Médico (SaMD), Sistema de Apoio à Decisão Clínica (CDSS), Hematologia, Hemograma, Inteligência Artificial, Validação Clínica, Pediatria, Acurácia Diagnóstica.

**Duração do Estudo:** 14 meses (3 meses preparação + 8 meses recrutamento + 3 meses análise)

**Cronograma:** Início previsto Q2/2026, término Q3/2027

---

## 3. FUNDAMENTAÇÃO E JUSTIFICATIVA

### 3.1 Contexto Clínico e Epidemiológico

#### 3.1.1 Epidemiologia das Doenças Hematológicas no Brasil

As doenças hematológicas representam importante problema de saúde pública no Brasil:

**Anemia:**
- Prevalência global de 24,8% em países da América Latina (WHO, 2011)
- No Brasil, anemia ferropriva afeta 20-30% de crianças menores de 5 anos (PNDS, 2006)
- Anemia em idosos (≥65 anos) tem prevalência de 7,6-19,5% no Brasil (Barbosa et al., 2006)
- Anemia grave (Hb <7 g/dL) em hospitalizados está associada a aumento de 35% na mortalidade (Musallam et al., 2011)

**Trombocitopenia:**
- Incidência de 2-13% em pacientes hospitalizados (Levi & Opal, 2006)
- Púrpura trombocitopênica imune (PTI) pediátrica: incidência de 1,9-6,4 por 100.000 crianças/ano
- Trombocitopenia neonatal severa (<50.000/µL) em 1-5% dos nascimentos (Roberts et al., 2008)

**Neutropenia:**
- Neutropenia febril pós-quimioterapia: 10-50% dos pacientes oncológicos (Freifeld et al., 2011)
- Mortalidade de neutropenia febril não tratada: 5-20% (depende de etiologia)
- Neutropenia congênita grave: 1-2 por milhão de nascidos vivos

#### 3.1.2 Importância do Diagnóstico Precoce

O diagnóstico hematológico precoce é crítico para múltiplas condições:

1. **Anemia grave**: Diagnóstico tardio pode resultar em insuficiência cardíaca congestiva e óbito, especialmente em crianças com reserva cardiovascular limitada (Joosten et al., 2018)

2. **Trombocitopenia**: Identificação rápida de plaquetopenias <50.000/µL reduz risco de hemorragia intracraniana (risco de 0,5-1% em PTI severa) (Neunert et al., 2019)

3. **Neutropenia febril**: Cada hora de atraso no início de antibioticoterapia aumenta mortalidade em 15-20% (Perron et al., 2012)

4. **Leucemias agudas**: Diagnóstico precoce melhora prognóstico - sobrevida em 5 anos de LLA pediátrica é de 90% com diagnóstico precoce vs 60-70% com diagnóstico tardio (Hunger & Mullighan, 2015)

#### 3.1.3 Limitações da Revisão Manual de Hemogramas

A interpretação manual de hemogramas em hospitais brasileiros enfrenta múltiplos desafios:

**Volume e Sobrecarga:**
- Hospitais de referência processam 500-2.000 hemogramas/dia
- Tempo médio de laudagem: 4-8 horas (pode exceder 24h em finais de semana)
- Sobrecarga de patologistas e hematologistas resulta em burnout e rotatividade

**Variabilidade Inter-Observador:**
- Concordância entre patologistas para diagnóstico morfológico: κ=0,65-0,80 (moderada a boa) (Smith et al., 2018)
- Variabilidade na classificação de atipia linfocitária: concordância de apenas 70-75% (Peterson et al., 2007)
- Diferenças entre hematologistas experientes (>10 anos) vs júniores (<3 anos) em casos complexos: sensibilidade difere em 10-15%

**Erros Diagnósticos:**
- Taxa de falsos negativos em revisão de lâminas críticas: 2-5% (Barnes et al., 2005)
- Erros mais frequentes: Missed acute leukemia (0,5-1%), missed severe thrombocytopenia (1-2%)
- Impacto clínico: Atraso no tratamento, aumento de custos (exames repetidos), eventos adversos evitáveis

**Disparidades Regionais:**
- Distribuição desigual de hematologistas no Brasil: 80% concentrados em capitais e regiões Sul/Sudeste
- Regiões Norte/Nordeste: 1 hematologista para cada 200.000-500.000 habitantes (vs 1:50.000 em grandes centros)
- Telemedicina e CDSS são estratégias promissoras para reduzir disparidades de acesso

### 3.2 Sistemas de Apoio à Decisão Clínica (CDSS) em Hematologia

#### 3.2.1 Evidências Internacionais

Revisão sistemática de Sutton et al. (2020) analisou 162 estudos de CDSS em diferentes especialidades:
- CDSS melhoram acurácia diagnóstica em média 15-20% vs prática padrão
- Maior benefício em áreas com alta demanda cognitiva e volume de dados (ex: radiologia, patologia)
- Limitações: Maioria dos estudos em países de alta renda, populações adultas, single-center

**Evidências em Hematologia (Internacional):**
- Estudo de Zini et al. (2012) na Itália: CDSS para anemia reduziu tempo até diagnóstico em 40%
- Estudo de Luo et al. (2020) na China: Machine learning para detecção de leucemia aguda alcançou sensibilidade de 94% e especificidade de 91% (n=5.234)
- Revisão de Nazha et al. (2021): Algoritmos de IA para síndrome mielodisplásica demonstraram performance comparável a hematologistas experientes (AUC 0,88-0,93)

#### 3.2.2 Lacunas de Conhecimento no Brasil

Apesar do potencial de CDSS, evidências robustas no contexto brasileiro são escassas:

1. **Falta de Validação em População Brasileira:**
   - Algoritmos desenvolvidos em populações europeias/norte-americanas podem não generalizar para população brasileira (diferenças genéticas, prevalência de doenças, comorbidades)
   - Única publicação brasileira (Machado et al., 2019): Estudo retrospectivo piloto com n=487, single-center, apenas adultos

2. **Subpopulações Pediátricas Não Representadas:**
   - Estudos internacionais de CDSS hematológico incluem <10% de crianças
   - Valores de referência pediátricos variam significativamente por idade (5 faixas etárias: neonatos, lactentes, pré-escolares, escolares, adolescentes)
   - Condições específicas pediátricas (anemia fisiológica do lactente, neutropenia benigna étnica) requerem algoritmos adaptados

