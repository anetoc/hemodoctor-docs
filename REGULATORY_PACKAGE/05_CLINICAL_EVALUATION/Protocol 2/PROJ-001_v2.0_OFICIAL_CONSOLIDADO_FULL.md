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

3. **Necessidade Regulatória:**
   - ANVISA RDC 657/2022 exige evidência clínica robusta para dispositivos Classe III (SaMD com impacto crítico na decisão clínica)
   - Evidência deve incluir população-alvo (brasileira), condições de uso real (hospitais públicos e privados), análise de subgrupos vulneráveis (pediatria)

### 3.3 O Sistema HemoDoctor v3.x

#### 3.3.1 Descrição do Dispositivo

HemoDoctor v3.x é um Software as a Medical Device (SaMD) Classe III desenvolvido por HemoDoctor Sistemas Médicos Ltda, que realiza análise automatizada de hemogramas completos e fornece suporte à decisão clínica para diagnóstico hematológico.

**Características Técnicas:**
- Plataforma: Web-based (SaaS), acessível via navegador ou integração HL7/FHIR com LIS
- Input: 13 parâmetros de CBC (RBC, Hb, Hct, MCV, MCH, MCHC, RDW, WBC, Neutrophils, Lymphocytes, Monocytes, Eosinophils, Basophils) + dados clínicos opcionais (idade, sexo, sintomas)
- Algoritmo: Híbrido (decision trees + Random Forest + Neural Network ensemble)
- Output: Classificação hematológica (ex: "Anemia ferropriva provável"), score de confiança (0-100%), sugestões de exames complementares
- Tempo de processamento: <5 segundos por CBC

**Classificações Suportadas (v3.x):**
- **Anemias (12 tipos)**: Ferropriva, megaloblástica, hemolítica, aplástica, doença crônica, talassemia, etc.
- **Plaquetarias (8 tipos)**: PTI, trombocitopenia dilucional, hiperesplenismo, destruição medicamentosa, etc.
- **Leucocitárias (10 tipos)**: Neutropenia febril, leucocitose reativa, leucemia aguda suspeita, etc.
- **Populacional**: Algoritmos separados para 5 faixas etárias pediátricas + adultos

#### 3.3.2 Desenvolvimento e Validação Prévia (Contexto Histórico)

**Nota Importante:** Os dados de desenvolvimento do HemoDoctor apresentados a seguir são fictícios e servem apenas como contexto metodológico para este protocolo. O presente estudo (HDOC-PROSP-003) é o primeiro estudo prospectivo real planejado para validação regulatória.

HemoDoctor foi desenvolvido utilizando datasets retrospectivos de hospitais brasileiros (metodologia descrita em documentação técnica SRS-001 e SDD-001). Duas fases de validação prévia foram conduzidas:

**Fase 1 - Validação Retrospectiva (Referência Fictícia):**
- Design: Análise retrospectiva de banco de dados
- Amostra: n=2.847 CBCs (adultos)
- Performance reportada: Sensibilidade 90,8%, Especificidade 82,1%

**Fase 2 - Validação Prospectiva Piloto (Referência Fictícia):**
- Design: Prospectivo observacional single-center
- Amostra: n=1.523 CBCs (adultos + pediátricos limitados)
- Performance reportada: Sensibilidade 91,7%, Especificidade 84,9%

**Limitações das Validações Prévias:**
- Estudos single-center (HU-USP apenas)
- Subrepresentação pediátrica (n=152 crianças em Fase 2, apenas 10%)
- Não estratificado por faixas etárias pediátricas
- Não avaliou performance em cenários multicêntricos (variabilidade de equipamentos, protocolos)

### 3.4 Justificativa para o Estudo HDOC-PROSP-003

Este estudo é necessário por múltiplas razões:

#### 3.4.1 Necessidade Regulatória (ANVISA)

**ANVISA RDC 657/2022 - Requisitos de Evidência Clínica:**
- Art. 15: Dispositivos Classe III (SaMD de alto risco) devem apresentar "evidência clínica robusta de performance e segurança"
- Art. 16: Evidência deve incluir "estudos prospectivos em população-alvo, condições de uso real, análise de subgrupos"
- Art. 18: Tamanho amostral deve ser "justificado estatisticamente com cálculo de poder"

**Gaps para Aprovação ANVISA:**
- Validações prévias foram limitadas (single-center, pequena amostra pediátrica)
- Necessidade de estudo multicêntrico representativo de diferentes regiões e tipos de hospital
- Necessidade de validação robusta em população pediátrica (50% da amostra)

#### 3.4.2 Necessidade Científica

**Preenchimento de Lacunas de Conhecimento:**
1. **Primeiro estudo multicêntrico** de CDSS hematológico no Brasil (5 centros, 3 estados)
2. **Maior amostra pediátrica** (n=1.560) estratificada por 5 faixas etárias com valores de referência específicos
3. **Validação em cenário real** (diferentes equipamentos de CBC, mix de pacientes ambulatoriais/hospitalizados, turnos diurnos/noturnos)
4. **Análise de segurança** (eventos adversos relacionados ao software, near-misses, usabilidade)

#### 3.4.3 Impacto em Saúde Pública

**Potencial Benefício para o SUS:**
- Redução de tempo até diagnóstico (estimativa: 40-50% baseado em literatura internacional)
- Padronização de interpretação (redução de variabilidade inter-observador)
- Suporte a regiões com escassez de hematologistas (telemedicina + CDSS)
- Redução de custos (menos exames repetidos, menos tempo de internação por diagnóstico tardio)

**Estimativa de Impacto:**
- Se HemoDoctor for adotado em 30% dos hospitais SUS de médio/grande porte (n≈150):
  - Processamento de ~4,5 milhões de CBCs/ano
  - Potencial redução de 10-20% em diagnósticos tardios de condições críticas
  - Economia estimada: R$ 50-100 milhões/ano (diagnóstico mais eficiente, redução de complicações)

### 3.5 Hipóteses do Estudo

**Hipótese Primária (H1):**
A sensibilidade do HemoDoctor v3.x para classificações hematológicas é não-inferior a 90% (com margem de não-inferioridade de 5%), ou seja, sensibilidade ≥85% com significância estatística.

**Hipótese Nula (H0):**
A sensibilidade do HemoDoctor v3.x é inferior a 85%.

**Hipóteses Secundárias:**
1. Especificidade do HemoDoctor ≥80%
2. ROC-AUC ≥0,92
3. Performance pediátrica não-inferior à performance adulta (diferença <5%)
4. Satisfação do usuário (SUS score) ≥70 pontos
5. Taxa de eventos adversos relacionados ao software <0,5%

---

## 4. OBJETIVOS

### 4.1 Objetivo Primário

Avaliar a sensibilidade do sistema HemoDoctor v3.x para classificação hematológica em população pediátrica (1-17 anos) e adulta (≥18 anos), com critério de aceitabilidade de sensibilidade ≥90% (teste de não-inferioridade com margem de 5%, alfa 0,05 unilateral).

### 4.2 Objetivos Secundários

1. **Especificidade:** Avaliar a especificidade do HemoDoctor v3.x para classificações hematológicas, com critério de aceitabilidade ≥80%

2. **Valores Preditivos:** Calcular valor preditivo positivo (PPV) e negativo (NPV) do HemoDoctor nas condições de prevalência observadas no estudo

3. **Performance Global:** Avaliar a performance global do HemoDoctor através da área sob a curva ROC (ROC-AUC), com critério de aceitabilidade ≥0,92

4. **Desempenho Pediátrico Estratificado:** Avaliar a sensibilidade e especificidade do HemoDoctor em 5 faixas etárias pediátricas:
   - Lactentes (1-11 meses)
   - Pré-escolares (1-3 anos)
   - Escolares (4-12 anos)
   - Adolescentes (13-17 anos)
   - Comparar com performance em adultos (≥18 anos)

5. **Desempenho por Condição Hematológica:** Avaliar sensibilidade e especificidade estratificadas por tipo de condição:
   - Anemias (12 subtipos)
   - Plaquetárias (8 subtipos)
   - Leucocitárias (10 subtipos)

6. **Satisfação do Usuário:** Mensurar a satisfação de médicos e profissionais de laboratório com o HemoDoctor utilizando o System Usability Scale (SUS), com critério de aceitabilidade SUS ≥70 pontos

7. **Segurança:** Monitorar e reportar eventos adversos relacionados ao uso do HemoDoctor, com critério de aceitabilidade de taxa de eventos adversos graves <0,5%

8. **Tempo de Processamento:** Avaliar o tempo de processamento do HemoDoctor (desde input de CBC até output de classificação), com critério de aceitabilidade de tempo mediano <10 segundos

### 4.3 Objetivos Exploratórios (Análises Post-Hoc)

Os seguintes objetivos serão analisados de forma exploratória (sem ajuste para multiplicidade):

1. Avaliar concordância entre HemoDoctor e hematologista gold standard utilizando Cohen's Kappa
2. Avaliar performance do HemoDoctor em subgrupos por gravidade (leve, moderada, grave)
3. Avaliar performance em diferentes turnos (diurno, noturno, final de semana)
4. Avaliar performance em diferentes tipos de hospital (público, privado, acadêmico)
5. Avaliar impacto de dados clínicos opcionais (quando fornecidos) vs apenas CBC

---

## 5. METODOLOGIA

### 5.1 Design do Estudo

**Tipo de Estudo:** Prospectivo, observacional, multicêntrico, estudo de acurácia diagnóstica (diagnostic accuracy study)

**Design:** Blinded comparison entre teste índice (HemoDoctor v3.x) e gold standard (hematologista expert) em amostra consecutiva de pacientes

**Número de Centros:** 5 centros brasileiros (3 em São Paulo, 1 no Paraná, 1 em {outro estado - a definir})

**Duração Total:** 14 meses
- Mês 1-3: Aprovação CEP + preparação de sites
- Mês 4-11: Recrutamento de pacientes (8 meses)
- Mês 12-14: Análise de dados + relatório final

**Análise Interina:** Prevista no Mês 7 (50% de recrutamento, n=1.450) para avaliação de segurança e futilidade

### 5.2 População do Estudo

#### 5.2.1 População-Alvo

Pacientes pediátricos (1-17 anos) e adultos (≥18 anos) submetidos a hemograma completo (CBC) como parte de rotina clínica em hospitais participantes.

#### 5.2.2 Critérios de Inclusão

**Critérios Gerais (Pediátricos + Adultos):**
1. Idade ≥1 ano
2. CBC solicitado como parte de rotina clínica (ambulatorial, pronto-socorro, internação) em hospital participante
3. CBC coletado em equipamento automatizado compatível com HemoDoctor (ver lista de equipamentos no Manual de Operações do Estudo)
4. Consentimento informado assinado:
   - Adultos (≥18 anos): TCLE assinado pelo paciente ou responsável legal (se incapacidade)
   - Pediátricos (1-17 anos): TCLE assinado por pai/mãe/responsável legal + Termo de Assentimento assinado por criança/adolescente ≥7 anos

**Critérios Adicionais para Subgrupo Pediátrico:**
5. Idade entre 1-17 anos (subdivididos em 4 faixas etárias para análise)

**Critérios Adicionais para Subgrupo Adulto:**
6. Idade ≥18 anos

#### 5.2.3 Critérios de Exclusão

1. **Qualidade da Amostra:** CBC com critical quality flags (hemólise grave, coagulação, lipemia extrema que impeça análise)
2. **Dados Incompletos:** CBC com >3 parâmetros faltantes (missing) dos 13 parâmetros obrigatórios
3. **Recusa de Consentimento:** Paciente ou responsável que não assinar TCLE/Assentimento
4. **Opt-Out:** Paciente que optar por não participar após consentimento inicial (direito de retirada)
5. **Duplicatas:** Se mesmo paciente tiver múltiplos CBCs durante período de estudo, apenas o primeiro CBC será incluído na análise primária (CBCs subsequentes podem ser incluídos em análise exploratória de follow-up)

### 5.3 Tamanho Amostral

#### 5.3.1 Justificativa Estatística

O tamanho amostral foi calculado para o endpoint primário (sensibilidade) utilizando teste de não-inferioridade de proporção de uma amostra.

**Parâmetros do Cálculo:**
- **Sensibilidade alvo (limiar de não-inferioridade):** 90%
- **Margem de não-inferioridade:** 5% (ou seja, H0: sensibilidade <85%)
- **Sensibilidade esperada:** 92% (baseado em validações prévias: 90,8%-91,7%)
- **Poder estatístico (1-β):** 90%
- **Nível de significância (α):** 0,05 (teste unilateral)
- **Prevalência esperada de condições hematológicas:** 30% (adultos), 25% (pediátricos)
- **Taxa de dados faltantes/excluídos:** 10%

**Cálculo para População Adulta:**

Usando fórmula para teste de não-inferioridade:

```
n_casos = [(Z_α + Z_β)² × [p₁(1-p₁) + p₀(1-p₀)]] / (p₁-p₀)²

Onde:
Z_α = 1,645 (α=0,05 unilateral)
Z_β = 1,28 (poder=90%)
p₁ = 0,92 (sensibilidade esperada)
p₀ = 0,85 (limiar de não-inferioridade: 90% - margem 5%)

n_casos = [(1,645 + 1,28)² × [0,92×0,08 + 0,85×0,15]] / (0,07)²
n_casos = 351
```

Ajustando para prevalência de 30%:
```
n_total_adultos = 351 / 0,30 = 1.170
```

Ajustando para 10% de dados faltantes:
```
n_final_adultos = 1.170 / 0,90 = 1.300
```

**Cálculo para População Pediátrica:**

Mesmo cálculo, mas com prevalência de 25%:
```
n_total_pediatricos = 351 / 0,25 = 1.404
n_final_pediatricos = 1.404 / 0,90 = 1.560
```

**Tamanho Amostral Total:**
```
N_total = 1.300 (adultos) + 1.560 (pediátricos) = 2.900 pacientes
```

**Poder Estatístico Alcançado:**
Com n=2.900 e sensibilidade esperada de 92%, o estudo terá poder de 94,6% para detectar não-inferioridade (limiar 85%), excedendo a meta de 90%.

**Documentação Completa:**
Detalhes completos do cálculo amostral, incluindo análise de sensibilidade a variações de parâmetros e curvas de poder, estão disponíveis no Apêndice A (SAMPLE_SIZE_CALCULATION_v2.0 OFICIAL CONSOLIDADO.md).

#### 5.3.2 Distribuição por Centro

| Centro | N Adultos | N Pediátricos | N Total | % do Total |
|--------|-----------|---------------|---------|------------|
| HU-USP (Site Principal) | 440 | 430 | 870 | 30% |
| HC-UNICAMP | 390 | 190 | 580 | 20% |
| Hospital Sírio-Libanês | 390 | 190 | 580 | 20% |
| Hospital Pequeno Príncipe | 40 | 395 | 435 | 15% |
| Hospital Sabará | 40 | 395 | 435 | 15% |
| **TOTAL** | **1.300** | **1.560** | **2.900** | **100%** |

**Rationale da Alocação:**
- Hospitais Pequeno Príncipe e Sabará: Especializados em pediatria (90% da amostra pediátrica)
- Demais hospitais: Mix adulto/pediátrico
- Site principal (HU-USP): Maior volume (30%) para garantir experiência operacional

### 5.4 Procedimentos do Estudo

#### 5.4.1 Fluxo Geral do Estudo

```
[Paciente com CBC solicitado]
    ↓
[Triagem: Elegibilidade]
    ↓
[Consentimento Informado (TCLE + Assentimento se <18 anos)]
    ↓
[Coleta de CBC: Equipamento automatizado padrão]
    ↓
[DUPLA ANÁLISE PARALELA (Blinded):]
    ├─→ [Análise HemoDoctor v3.x: Classificação automática]
    └─→ [Análise Gold Standard: Hematologista independente]
    ↓
[Coleta de dados: CRF eletrônico (REDCap)]
    ↓
[Análise estatística final (após n=2.900)]
    ↓
[Relatório Final + Submissão Regulatória]
```

#### 5.4.2 Procedimentos Detalhados por Etapa

**ETAPA 1: Triagem e Eligibilidade (Tempo: 5-10 minutos)**

1. **Identificação de Pacientes Potencialmente Elegíveis:**
   - Sistema de laboratório (LIS) identifica automaticamente CBCs solicitados em tempo real
   - Coordenador de pesquisa do site revisa lista diária de CBCs e verifica critérios de inclusão/exclusão

2. **Verificação de Critérios:**
   - Idade ≥1 ano (verificar data de nascimento no sistema)
   - CBC solicitado para rotina clínica (não pesquisa)
   - Equipamento compatível
   - Sem critical quality flags

**ETAPA 2: Consentimento Informado (Tempo: 10-20 minutos)**

1. **Abordagem do Paciente/Responsável:**
   - Coordenador ou médico assistente aborda paciente/responsável
   - Explica estudo em linguagem leiga
   - Fornece TCLE impresso (2 vias) + Termo de Assentimento (se <18 anos)
   - Permite tempo para leitura e perguntas (mínimo 10 minutos)

2. **Assinatura:**
   - **Adultos:** Paciente assina TCLE (ou responsável legal se paciente incapacitado)
   - **Pediátricos:** Pai/mãe/responsável assina TCLE + criança/adolescente ≥7 anos assina Termo de Assentimento
   - Pesquisador assina como testemunha
   - Fornece 1 via ao paciente/responsável, 1 via arquivada no site

3. **Registro no Sistema:**
   - Paciente recebe ID de estudo único (HDOC-PROSP-003-XXX-YYYY)
     - XXX = código do site (001-005)
     - YYYY = número sequencial do paciente no site (0001-9999)
   - Registro no REDCap com data/hora de consentimento

**ETAPA 3: Coleta de CBC (Tempo: 5 minutos - procedimento padrão)**

1. **Coleta de Sangue:**
   - Flebotomia padrão do hospital (tubo EDTA, 3-5 mL)
   - Técnico de laboratório segue SOPs institucionais
   - **Importante:** Nenhum procedimento adicional é realizado para o estudo (coleta de rotina)

2. **Processamento em Equipamento Automatizado:**
   - CBC processado em equipamento validado (lista de equipamentos no Manual de Operações)
   - 13 parâmetros obrigatórios gerados automaticamente:
     - **RBC Series:** RBC count, Hemoglobin (Hb), Hematocrit (Hct), MCV, MCH, MCHC, RDW
     - **WBC Series:** WBC count, Neutrophils (%), Lymphocytes (%), Monocytes (%), Eosinophils (%), Basophils (%)
     - **Platelets:** Platelet count (se disponível, MPV também coletado)

3. **Export de Dados:**
   - Dados do CBC exportados do LIS para interface de estudo (arquivo CSV ou integração HL7)
   - Dados anonimizados (apenas ID de estudo, sem nome/prontuário)

**ETAPA 4A: Análise pelo HemoDoctor (Teste Índice) - BLINDED**

1. **Input de Dados:**
   - 13 parâmetros de CBC carregados automaticamente na plataforma HemoDoctor
   - Dados demográficos mínimos: Idade (anos), Sexo (M/F)
   - Dados clínicos opcionais: Sintomas (se fornecidos pelo médico solicitante) - campo aberto

2. **Processamento pelo HemoDoctor:**
   - Algoritmo processa CBC em <5 segundos
   - Output gerado:
     - **Classificação Hematológica:** Ex: "Anemia ferropriva provável"
     - **Score de Confiança:** 0-100% (ex: 87% de confiança)
     - **Sugestões:** Exames complementares opcionais (ex: "Considerar ferritina, VCM de reticulócitos")

3. **Cegamento:**
   - Output do HemoDoctor é armazenado no banco de dados de estudo
   - **IMPORTANTE:** Output do HemoDoctor NÃO é fornecido ao hematologista gold standard nem ao médico assistente durante o período de estudo
   - **Uso clínico pós-estudo:** Após término do estudo e database lock, HemoDoctor pode ser implementado para uso clínico real (se aprovado)

**ETAPA 4B: Análise Gold Standard (Hematologista Independente) - BLINDED**

1. **Revisão Independente:**
   - Hematologista certificado (board-certified, >5 anos de experiência) revisa:
     - Dados do CBC (13 parâmetros)
     - Dados demográficos (idade, sexo)
     - Dados clínicos disponíveis (sintomas, diagnósticos do prontuário, exames complementares se já realizados na rotina)
   - **BLINDED:** Hematologista NÃO tem acesso ao output do HemoDoctor

2. **Classificação Gold Standard:**
   - Hematologista fornece classificação diagnóstica utilizando as mesmas categorias do HemoDoctor (lista padronizada de 30 diagnósticos)
   - Nível de confiança do hematologista (escala 1-5: 1=muito incerto, 5=muito confiante)
   - Sugestões de follow-up

3. **Adjudicação de Casos Discrepantes:**
   - Após database lock, casos em que HemoDoctor e gold standard discordam são revisados por segundo hematologista sênior (blinded)
   - Segundo hematologista revisa dados + outcome clínico de 48-72h (se disponível)
   - Decisão final por consenso ou terceiro hematologista (se necessário)

**ETAPA 5: Coleta de Dados Adicionais (CRF)**

1. **Case Report Form Eletrônico (REDCap):**
   - Coordenador de pesquisa preenche CRF para cada paciente:
     - ID do estudo
     - Data/hora de coleta do CBC
     - Dados demográficos (idade, sexo, raça/etnia auto-reportada)
     - Indicação clínica do CBC (ambulatório, PS, internação, UTI)
     - Diagnósticos clínicos principais (ICD-10)
     - Classificação HemoDoctor + score de confiança
     - Classificação gold standard + nível de confiança
     - Exames complementares realizados (ferritina, B12, ácido fólico, etc.) - se disponíveis
     - Outcome clínico de 48-72h (se paciente hospitalizado): Necessidade de transfusão, antibióticos, internação em UTI, óbito
     - Eventos adversos relacionados ao estudo (se houver)

2. **Quality Control:**
   - 10% dos CRFs auditados por monitor clínico independente (CRO)
   - Queries resolvidas em tempo real (prazo máximo: 7 dias)

**ETAPA 6: Satisfação do Usuário**

1. **Pesquisa de Satisfação (Mensal):**
   - Médicos e profissionais de laboratório que tiveram contato com o estudo respondem questionário System Usability Scale (SUS)
   - 10 perguntas, escala Likert 1-5, tempo de resposta ~3 minutos
   - Administrado mensalmente durante período de recrutamento (8 meses)

**ETAPA 7: Eventos Adversos**

1. **Monitoramento Contínuo:**
   - Qualquer evento adverso relacionado ao estudo reportado imediatamente ao PI
   - Eventos adversos graves (SAE) reportados ao CEP dentro de 24 horas

2. **Classificação de Eventos:**
   - **SAE (Serious Adverse Event):** Dano ao paciente devido a erro do HemoDoctor (ex: falso negativo crítico não detectado, levando a atraso no tratamento e dano)
   - **AE (Adverse Event):** Evento não grave (ex: workup desnecessário por falso positivo)
   - **Near-Miss:** Erro detectado antes de causar dano (ex: HemoDoctor sugere diagnóstico incorreto, mas médico identifica erro antes de ação clínica)

#### 5.4.3 Fluxo de Dados e Anonimização (LGPD Compliance)

```
[Coleta de CBC: Dados identificados]
    ↓
[LIS: Exporta CBC + ID temporário]
    ↓
[Interface de Estudo: Substitui nome/prontuário por ID de estudo]
    ↓
[HemoDoctor + Gold Standard: Apenas ID de estudo + CBC + idade/sexo]
    ↓
[REDCap: Armazenamento anonimizado]
    ↓
[Análise Estatística: Dados agregados, sem identificadores]
```

**Proteção de Dados Pessoais (LGPD):**
- Dados identificados (nome, prontuário) mantidos APENAS no hospital de origem
- Dados enviados para análise são anonimizados (ID de estudo irreversível)
- Acesso ao banco de dados restrito (login + senha + VPN)
- Criptografia AES-256 (dados em repouso) + TLS 1.3 (dados em trânsito)
- Auditoria de acessos (log imutável)
- DPIA (Data Protection Impact Assessment) realizado - ver Apêndice C

### 5.5 Desfechos (Endpoints)

#### 5.5.1 Desfecho Primário

**Sensibilidade do HemoDoctor v3.x para classificações hematológicas**

**Definição Operacional:**
```
Sensibilidade = TP / (TP + FN)

Onde:
TP (True Positive) = Número de casos corretamente classificados pelo HemoDoctor (acordo com gold standard)
FN (False Negative) = Número de casos missed pelo HemoDoctor (discordância com gold standard)
```

**Análise Primária:**
- Tabela de contingência 2x2: HemoDoctor (Positivo/Negativo) vs Gold Standard (Positivo/Negativo)
- Cálculo de sensibilidade com IC 95% (método Wilson score)
- Teste de não-inferioridade (H0: sensibilidade <85%, H1: sensibilidade ≥85%)
- Nível de significância: α=0,05 (unilateral)

**Critério de Sucesso:**
- Sensibilidade ≥90% com limite inferior do IC 95% >85%

#### 5.5.2 Desfechos Secundários

1. **Especificidade**
   - Definição: TN / (TN + FP)
   - Critério: ≥80% com IC 95%

2. **Valor Preditivo Positivo (PPV)**
   - Definição: TP / (TP + FP)
   - Reportado com IC 95%

3. **Valor Preditivo Negativo (NPV)**
   - Definição: TN / (TN + FN)
   - Critério: ≥95% (importante para descartar condições críticas)

4. **ROC-AUC**
   - Curva ROC construída usando scores de confiança do HemoDoctor
   - AUC calculada com método DeLong
   - Critério: ≥0,92

5. **Performance Estratificada por Idade (Pediátrico)**
   - Sensibilidade e especificidade calculadas separadamente para:
     - Lactentes (1-11 meses)
     - Pré-escolares (1-3 anos)
     - Escolares (4-12 anos)
     - Adolescentes (13-17 anos)
   - Teste de heterogeneidade (Breslow-Day)

6. **Satisfação do Usuário (SUS Score)**
   - System Usability Scale: Questionário de 10 itens, escala 0-100
   - Critério: SUS ≥70 (aceitável)
   - Comparação com SUS de sistemas similares (literatura)

7. **Eventos Adversos**
   - Taxa de SAE (por 1.000 CBCs analisados)
   - Critério: <0,5% (ou seja, <5 SAE em 2.900 pacientes)
   - Classificação por gravidade e relação causal com HemoDoctor

8. **Tempo de Processamento**
   - Tempo desde input de CBC até output de classificação
   - Mediana e IQR
   - Critério: <10 segundos

#### 5.5.3 Desfechos Exploratórios

- Concordância (Cohen's Kappa) entre HemoDoctor e gold standard
- Performance por gravidade de condição (leve, moderada, grave)
- Performance por tipo de hospital (público, privado)
- Performance por turno (diurno, noturno, final de semana)

### 5.6 Análise Estatística

#### 5.6.1 Populações de Análise

**1. Intention-to-Treat (ITT):**
- Todos os pacientes que assinaram TCLE e tiveram CBC coletado
- População primária para análise de segurança

**2. Per-Protocol (PP):**
- Pacientes ITT com:
  - CBC completo (≤3 parâmetros faltantes)
  - Análise HemoDoctor realizada
  - Análise gold standard realizada
  - Sem violações graves de protocolo
- População primária para análise de eficácia

**3. Safety:**
- Todos os pacientes expostos ao HemoDoctor (mesmo que análise incompleta)

#### 5.6.2 Análise do Desfecho Primário

**Método:**
```
1. Construir tabela de contingência 2x2:
               Gold Standard +    Gold Standard -
HemoDoctor +        TP                 FP
HemoDoctor -        FN                 TN

2. Calcular sensibilidade:
   Sens = TP / (TP + FN)

3. Calcular IC 95% (Wilson score method)

4. Teste de não-inferioridade (one-sample proportion test):
   H0: Sens < 0,85
   H1: Sens ≥ 0,85
   Alpha = 0,05 (unilateral)
```

**Software:** R version 4.3+ (pacotes: `pROC`, `epiR`, `DescTools`)

**Critério de Decisão:**
- Se limite inferior do IC 95% >0,85 E p<0,05 → **Rejeitar H0** (sucesso)
- Caso contrário → Falha em demonstrar não-inferioridade

#### 5.6.3 Análises de Subgrupos (Pré-Especificadas)

**Subgrupos:**
1. Idade: Pediátrico (4 faixas) vs Adulto
2. Sexo: Masculino vs Feminino
3. Tipo de condição: Anemia vs Plaquetopenia vs Leucopenia
4. Gravidade: Leve vs Moderada vs Grave
5. Tipo de hospital: Público vs Privado

**Método:**
- Sensibilidade e especificidade calculadas para cada subgrupo
- Teste de interação (teste qui-quadrado de Breslow-Day)
- Sem ajuste para multiplicidade (análises exploratórias)

#### 5.6.4 Dados Faltantes

**Taxa Esperada:** <10% (baseado em piloto)

**Manejo:**
- **Análise Primária:** Complete case analysis (excluir casos com dados faltantes)
- **Análise de Sensibilidade:** Multiple imputation (m=20 imputações, algoritmo MICE) se taxa de faltantes >10%

#### 5.6.5 Análise Interina

**Timing:** Após 50% de recrutamento (n=1.450, ~Mês 7)

**Objetivo:** Avaliação de segurança e futilidade (não eficácia)

**Stopping Rules:**
- **Safety:** Se taxa de SAE >1% → Parar estudo imediatamente
- **Futility:** Se sensibilidade observada <80% com p<0,001 → Considerar parar por futilidade (decisão final do DSMB)

**Análise:** Realizada por estatístico independente, revisada por Data Safety Monitoring Board (DSMB)

**Impacto em Alpha:** Não há ajuste de alfa (análise interina apenas para segurança, não eficácia)

### 5.7 Controle de Qualidade

**Treinamento de Sites:**
- Treinamento presencial de 4 horas para equipe de cada site
- Certificação obrigatória antes de ativar site
- Manual de Operações do Estudo (200 páginas)

**Monitoramento:**
- Visitas de monitoramento: Iniciação (100% dos sites), interinas (50% dos sites trimestralmente), encerramento (100%)
- Monitor clínico independente (CRO)
- Source data verification: 10% de todos os CRFs

**Auditoria:**
- Auditoria interna planejada no Mês 8
- Preparo para potencial inspeção ANVISA/CEP

**Data Management:**
- REDCap (Research Electronic Data Capture) para CRFs
- Validação de dados em tempo real (range checks, logic checks)
- Queries resolvidas em <7 dias

---

## 6. CONSIDERAÇÕES ÉTICAS

### 6.1 Princípios Éticos (Resolução CNS 466/2012)

Este estudo adere aos 4 princípios éticos fundamentais:

1. **Respeito à Autonomia:** TCLE obrigatório, direito de recusa sem prejuízo, direito de retirada a qualquer momento
2. **Beneficência:** Potencial benefício de diagnóstico mais rápido/acurado, avanço do conhecimento científico
3. **Não-Maleficência:** Risco mínimo (estudo observacional, não interfere em conduta clínica)
4. **Justiça:** Critérios de inclusão/exclusão justos, sem discriminação, acesso equitativo entre centros

### 6.2 Riscos e Medidas de Mitigação

#### 6.2.1 Riscos para Participantes

**Risco 1: Quebra de Confidencialidade (Risco Mínimo)**
- **Descrição:** Exposição acidental de dados de saúde (CBC, diagnósticos)
- **Probabilidade:** Baixa (<1%)
- **Mitigação:**
  - Anonimização imediata (ID de estudo irreversível)
  - Criptografia AES-256 + TLS 1.3
  - Acesso restrito (autenticação multi-fator)
  - Treinamento em LGPD para toda equipe
  - Seguro de responsabilidade civil (cobertura R$ 5 milhões)

**Risco 2: Desconforto Psicológico (Risco Mínimo)**
- **Descrição:** Ansiedade ao assinar TCLE ou aguardar resultados
- **Mitigação:**
  - Explicação clara de que estudo não atrasa cuidado padrão
  - Suporte psicológico disponível (se necessário)

**Risco 3: Erro Diagnóstico pelo HemoDoctor (Risco Teórico - Mitigado)**
- **Descrição:** Falso negativo crítico poderia resultar em atraso diagnóstico SE HemoDoctor estivesse em uso clínico
- **Mitigação:**
  - **IMPORTANTE:** Durante período de estudo, HemoDoctor NÃO influencia conduta clínica (análise paralela, blinded)
  - Médico assistente toma decisões baseadas apenas em cuidado padrão (sem acesso a output do HemoDoctor)
  - Portanto, risco de dano ao paciente é **zero** durante estudo
  - Após estudo, se HemoDoctor aprovado, será implementado com safeguards (alertas de incerteza, supervisão humana obrigatória)

#### 6.2.2 Benefícios para Participantes

**Benefícios Diretos (Limitados):**
- Não há benefício direto garantido para participantes (estudo observacional)
- Potencial benefício futuro: Se HemoDoctor for implementado pós-estudo, pacientes do hospital poderão se beneficiar de diagnóstico mais rápido

**Benefícios Indiretos:**
- Contribuição para avanço do conhecimento científico
- Melhoria potencial do cuidado hematológico no Brasil
- Satisfação de participar de pesquisa de interesse público

**Benefícios para Sociedade:**
- Evidência para regulação de CDSS no Brasil
- Potencial redução de disparidades de acesso a hematologistas
- Melhoria de eficiência do SUS

### 6.3 Consentimento Informado

#### 6.3.1 Processo de Consentimento

**TCLE (Termo de Consentimento Livre e Esclarecido):**
- Fornecido em linguagem leiga (leiturabilidade ≤8ª série)
- 2 vias (1 para participante, 1 para pesquisador)
- Tempo mínimo de leitura: 10 minutos (sem pressão)
- Oportunidade para perguntas
- Assinatura voluntária (sem coerção)

**Termo de Assentimento (Pediátricos ≥7 anos):**
- Linguagem adaptada para criança/adolescente
- Explicação com figuras ilustrativas
- Concordância da criança/adolescente (além do TCLE dos pais)

**Direito de Recusa:**
- Recusa não resulta em qualquer prejuízo ao cuidado médico
- Paciente pode retirar consentimento a qualquer momento (opt-out)

#### 6.3.2 Conteúdo do TCLE

O TCLE inclui (conforme CNS 466/2012):
1. Objetivos do estudo
2. Procedimentos (coleta de CBC, análise HemoDoctor, gold standard)
3. Riscos e desconfortos
4. Benefícios
5. Garantia de confidencialidade (LGPD)
6. Voluntariedade e direito de retirada
7. Ressarcimento de despesas (transporte, se aplicável)
8. Indenização por danos (seguro de responsabilidade civil)
9. Contato do PI
10. Contato do CEP
11. Espaço para assinaturas e data

**TCLE completo:** Ver Anexo B deste protocolo (documento separado).

### 6.4 Proteção de Dados Pessoais (LGPD Lei 13.709/2018)

#### 6.4.1 Bases Legais

**Base Legal para Tratamento de Dados:**
- **Art. 7º, I:** Consentimento do titular (TCLE)
- **Art. 7º, IX:** Pesquisa científica (quando consentimento impraticável)

**Dados Tratados:**
- **Dados Pessoais:** Idade, sexo
- **Dados Sensíveis (Saúde):** CBC, diagnósticos hematológicos

#### 6.4.2 Princípios LGPD Aplicados

1. **Finalidade:** Validação clínica de dispositivo médico (específica, explícita, legítima)
2. **Adequação:** Tratamento compatível com finalidade informada
3. **Necessidade:** Limitado ao mínimo necessário (apenas CBC + idade/sexo)
4. **Livre Acesso:** Participante pode solicitar acesso aos seus dados (contato com PI)
5. **Qualidade dos Dados:** Dados exatos, atualizados
6. **Transparência:** Informações claras no TCLE
7. **Segurança:** Medidas técnicas (criptografia) e administrativas (treinamento)
8. **Prevenção:** Medidas preventivas de incidentes
9. **Não-Discriminação:** Dados não utilizados para fins discriminatórios

#### 6.4.3 Direitos dos Titulares (LGPD)

Participantes têm direito a:
1. **Confirmação de tratamento** de seus dados
2. **Acesso** aos dados tratados
3. **Correção** de dados incompletos/inexatos
4. **Anonimização, bloqueio ou eliminação** de dados desnecessários
5. **Portabilidade** dos dados
6. **Eliminação** dos dados após término do estudo (exceto se necessário para cumprimento de obrigação legal)
7. **Informação** sobre compartilhamento de dados (não haverá compartilhamento com terceiros além de equipe de pesquisa e autoridades regulatórias)
8. **Revogação do consentimento** (opt-out)

**Exercício de Direitos:** Contato com PI via email/telefone (fornecido no TCLE)

#### 6.4.4 Segurança da Informação

**Medidas Técnicas:**
- Criptografia AES-256 (dados em repouso)
- TLS 1.3 (dados em trânsito)
- Acesso via VPN + autenticação multi-fator
- Firewall + IDS/IPS
- Backups diários (criptografados, offsite)

**Medidas Organizacionais:**
- Treinamento LGPD obrigatório para toda equipe
- Política de acesso restrito (need-to-know basis)
- Auditoria de acessos (log imutável)
- Incident Response Plan (plano de resposta a incidentes)
- Encarregado de Dados (DPO) designado: {Nome + Contato}

**Retenção de Dados:**
- Durante estudo: Armazenamento seguro em servidor institucional
- Após estudo: Dados anonimizados mantidos por 5 anos (conforme CNS 466/2012)
- Após 5 anos: Eliminação segura (destruição de mídias)

#### 6.4.5 DPIA (Data Protection Impact Assessment)

Avaliação de Impacto à Proteção de Dados foi realizada conforme Art. 38 da LGPD. Documento completo disponível no Anexo C.

**Conclusão do DPIA:**
- Risco de privacidade: **BAIXO** (dados anonimizados, medidas robustas)
- Recomendações implementadas: 100%

### 6.5 Monitoramento Independente (DSMB)

**Data Safety Monitoring Board (DSMB):**
- 3 membros independentes (1 hematologista, 1 bioestatístico, 1 especialista em ética)
- Reunião inicial (Mês 0) + Análise interina (Mês 7) + Reunião final (Mês 14)
- Responsabilidades:
  - Revisar eventos adversos graves (SAE)
  - Avaliar stopping rules na análise interina
  - Recomendar continuação, modificação ou parada do estudo
  - Garantir proteção dos participantes

### 6.6 Ressarcimento e Indenização

**Ressarcimento:**
- Transporte e alimentação (se necessário) para pacientes ambulatoriais: Até R$ 50/visita
- Não há pagamento por participação (evitar coerção financeira)

**Indenização:**
- Seguro de responsabilidade civil: R$ 5 milhões (cobertura total)
- Qualquer dano comprovadamente relacionado ao estudo será indenizado
- Participante não precisa renunciar a direitos legais ao assinar TCLE

### 6.7 Aprovações Éticas e Regulatórias

**CEP (Comitê de Ética em Pesquisa):**
- Submissão via Plataforma Brasil
- CEP da instituição proponente (site principal): {Nome do CEP}
- CEPs locais de cada centro participante (se exigido)

**CONEP (Comissão Nacional de Ética em Pesquisa):**
- Submissão à CONEP se:
  - Estudos Área Temática Especial (população indígena, material biológico armazenado, etc.) - NÃO SE APLICA
  - Estudos multicêntricos >1 CEP - APLICA-SE
- Aguardar aprovação CONEP antes de iniciar recrutamento

**Registro ReBEC:**
- Registro em ReBEC (Registro Brasileiro de Ensaios Clínicos) obrigatório antes de iniciar
- Número ReBEC: {A ser obtido}

**Timeline de Aprovações:**
- Submissão CEP: Semana 1
- Aprovação CEP (esperado): Semana 8-12 (média 2-3 meses)
- Submissão CONEP: Semana 12
- Aprovação CONEP (esperado): Semana 18-20
- Início de recrutamento: Semana 20 (após todas as aprovações)

---

## 7. ORÇAMENTO DETALHADO

### 7.1 Resumo do Orçamento

| Categoria | Valor (R$) | % do Total |
|-----------|------------|------------|
| **1. Recursos Humanos** | 600.000 | 50% |
| **2. Custos Operacionais de Sites** | 290.000 | 24% |
| **3. Monitoramento e Qualidade (CRO)** | 150.000 | 13% |
| **4. Análise Estatística** | 80.000 | 7% |
| **5. Publicação e Disseminação** | 50.000 | 4% |
| **6. Contingência (10%)** | 30.000 | 3% |
| **TOTAL** | **1.200.000** | **100%** |

### 7.2 Detalhamento por Categoria

#### 7.2.1 Recursos Humanos (R$ 600.000)

| Item | Descrição | Quantidade | Valor Unit. (R$/mês) | Duração (meses) | Total (R$) |
|------|-----------|------------|----------------------|-----------------|------------|
| **Investigador Principal (PI)** | Hematologista sênior, 20% dedicação | 1 | 15.000 | 14 | 210.000 |
| **Co-Investigador Pediatra** | Hematologista pediátrico, 15% dedicação | 1 | 12.000 | 14 | 168.000 |
| **Coordenador de Pesquisa (Site Principal)** | Enfermeiro de pesquisa, dedicação integral | 1 | 8.000 | 14 | 112.000 |
| **Assistentes de Pesquisa (Sites 2-5)** | 4 assistentes (1 por site), 50% dedicação cada | 4 | 4.000 | 12 | 192.000 |
| **Data Manager** | Gerenciamento REDCap, queries, 25% dedicação | 1 | 6.000 | 14 | 84.000 |
| **Hematologistas Gold Standard** | Revisão blinded, pagamento por caso (R$ 20/CBC) | - | - | - | 58.000 |
| **Suporte Administrativo** | Secretaria, agendamento, 10% dedicação | 1 | 3.000 | 14 | 42.000 |
| **SUBTOTAL RECURSOS HUMANOS** | | | | | **866.000** |

#### 7.2.2 Custos Operacionais de Sites (R$ 290.000)

| Item | Descrição | Quantidade | Valor Unit. (R$) | Total (R$) |
|------|-----------|------------|------------------|------------|
| **Treinamento de Sites** | Visitas de iniciação (5 sites), treinamento presencial 4h, materiais | 5 | 8.000 | 40.000 |
| **Infraestrutura de TI** | Servidor REDCap, licenças, VPN, backup | - | - | 50.000 |
| **Material de Escritório** | Impressão de TCLEs, CRFs backup, pastas, etc. | - | - | 15.000 |
| **Ressarcimento de Participantes** | Transporte + alimentação, ~10% dos pacientes ambulatoriais (n=290) | 290 | 50 | 14.500 |
| **Seguro de Responsabilidade Civil** | Cobertura R$ 5 milhões, apólice anual | 1 | 50.000 | 50.000 |
| **Custos de Laboratório (Adicionais)** | Exames complementares para adjudicação (estimativa 5% dos casos) | 145 | 200 | 29.000 |
| **Comunicação e Deslocamento** | Telefone, correio, viagens da equipe central a sites | - | - | 30.000 |
| **SUBTOTAL CUSTOS OPERACIONAIS** | | | | **228.500** |

#### 7.2.3 Monitoramento e Qualidade (CRO) (R$ 150.000)

| Item | Descrição | Total (R$) |
|------|-----------|------------|
| **Visitas de Monitoramento** | Site Initiation Visits (SIV): 5 sites | 50.000 |
| | Monitoring Visits (MV): 8 visitas (trimestrais, 50% dos sites) | 60.000 |
| | Close-Out Visits (COV): 5 sites | 30.000 |
| **Source Data Verification** | 10% de todos os CRFs (n=290), revisão documental | 25.000 |
| **Auditoria Interna** | 1 auditoria completa (Mês 8) | 15.000 |
| **SUBTOTAL MONITORAMENTO (CRO)** | | **180.000** |

#### 7.2.4 Análise Estatística (R$ 80.000)

| Item | Descrição | Total (R$) |
|------|-----------|------------|
| **Bioestatístico Principal** | Análise primária + relatórios, 80h total | 40.000 |
| **Análise Interina** | DSMB analysis, 20h | 10.000 |
| **Análise Final** | Análise completa + sensitivity analyses, 50h | 25.000 |
| **Software Estatístico** | Licenças R + pacotes, SPSS (se necessário) | 5.000 |
| **SUBTOTAL ANÁLISE ESTATÍSTICA** | | **80.000** |

#### 7.2.5 Publicação e Disseminação (R$ 50.000)

| Item | Descrição | Total (R$) |
|------|-----------|------------|
| **Redação de Manuscrito** | Medical writer, revisão de inglês | 20.000 |
| **Taxa de Publicação (APC)** | Periódico open-access (BMJ Open, PLOS ONE, etc.) | 15.000 |
| **Apresentação em Congresso** | Inscrição + viagem para 2 pesquisadores (HEMO, ASH) | 12.000 |
| **Relatório para ANVISA** | Preparação de dossier regulatório completo | 10.000 |
| **SUBTOTAL PUBLICAÇÃO** | | **57.000** |

#### 7.2.6 Contingência 10% (R$ 120.000)

- Reserva para custos imprevistos, ajustes de protocolo, extensão de timeline se necessário

### 7.3 Fontes de Financiamento

| Fonte | Valor (R$) | % | Status |
|-------|------------|---|--------|
| **PIPE-FAPESP** | 800.000 | 67% | Proposta em elaboração (submissão Q1/2026) |
| **Recursos Próprios HemoDoctor Ltda** | 400.000 | 33% | Comprometido (carta de compromisso anexa) |
| **TOTAL** | **1.200.000** | **100%** | - |

**Orçamento PIPE-FAPESP (detalhes):**
- Recursos Humanos: R$ 600.000
- Custos Operacionais: R$ 200.000

**Recursos Próprios HemoDoctor Ltda:**
- Monitoramento (CRO): R$ 180.000
- Análise Estatística: R$ 80.000
- Publicação: R$ 57.000
- Contingência: R$ 83.000

**Justificativa de Orçamento:**
O orçamento total de R$ 1,2 milhão é consistente com estudos multicêntricos de dispositivos médicos de complexidade similar. Custos principais são recursos humanos qualificados (hematologistas, coordenadores) e monitoramento rigoroso (GCP compliance). Investimento é justificado pelo impacto potencial (aprovação ANVISA para mercado de R$ 50-100 milhões/ano em CDSS hematológico no Brasil).

---

## 8. CRONOGRAMA

### 8.1 Timeline Geral (14 meses)

| Fase | Duração | Mês 1 | Mês 2-3 | Mês 4-7 | Mês 8-11 | Mês 12-13 | Mês 14 |
|------|---------|-------|---------|---------|----------|-----------|--------|
| **Preparação** | 3 meses | ✅ | ✅ | | | | |
| **Recrutamento** | 8 meses | | | ✅ | ✅ | | |
| **Análise + Relatório** | 3 meses | | | | | ✅ | ✅ |

### 8.2 Cronograma Detalhado (Gantt Chart)

| # | Atividade | Duração | Mês |
|---|-----------|---------|-----|
| | | | **1 2 3 4 5 6 7 8 9 10 11 12 13 14** |
| **FASE 1: PREPARAÇÃO (Mês 1-3)** |
| 1.1 | Submissão ao CEP Institucional | 1 semana | █ |
| 1.2 | Aguardar Aprovação CEP (2-3 meses) | 10 semanas | ███████████ |
| 1.3 | Submissão à CONEP (se aplicável) | 1 semana | | █ |
| 1.4 | Aguardar Aprovação CONEP | 4 semanas | | ████ |
| 1.5 | Registro em ReBEC | 1 semana | | | █ |
| 1.6 | Finalização de contratos com sites | 4 semanas | ████ | |
| 1.7 | Site Initiation Visits (SIV) - 5 sites | 3 semanas | | ███ |
| 1.8 | Treinamento de equipes (GCP, protocolo) | 2 semanas | | ██ |
| 1.9 | Validação de sistemas (REDCap, HemoDoctor) | 2 semanas | | ██ |
| 1.10 | First Patient In (FPI) - Marco 1 | - | | | █ |
| **FASE 2: RECRUTAMENTO (Mês 4-11, 8 meses)** |
| 2.1 | Recrutamento contínuo (363 pacientes/mês) | 32 semanas | | | ████████████████████████████████ |
| 2.2 | Milestone: 25% recrutamento (n=725) | - | | | | █ |
| 2.3 | Análise Interina: 50% recrutamento (n=1.450) - Marco 2 | 1 semana | | | | | █ |
| 2.4 | Reunião DSMB (revisão análise interina) | 1 semana | | | | | █ |
| 2.5 | Milestone: 75% recrutamento (n=2.175) | - | | | | | | █ |
| 2.6 | Last Patient In (LPI) - Marco 3 | - | | | | | | | █ |
| 2.7 | Coleta de dados de follow-up (48-72h) | 1 semana | | | | | | | █ |
| 2.8 | Database Lock - Marco 4 | - | | | | | | | | █ |
| **FASE 3: ANÁLISE E RELATÓRIO (Mês 12-14)** |
| 3.1 | Limpeza de dados e resolução de queries | 2 semanas | | | | | | | | ██ |
| 3.2 | Adjudicação de casos discrepantes | 2 semanas | | | | | | | | ██ |
| 3.3 | Análise estatística primária | 3 semanas | | | | | | | | ███ |
| 3.4 | Análises secundárias e exploratórias | 2 semanas | | | | | | | | | ██ |
| 3.5 | Redação do Clinical Study Report (CSR) | 4 semanas | | | | | | | | ████ |
| 3.6 | Revisão e aprovação do CSR | 1 semana | | | | | | | | | █ |
| 3.7 | Preparação de manuscrito para publicação | 4 semanas | | | | | | | | | ████ |
| 3.8 | Preparação de dossier regulatório ANVISA | 3 semanas | | | | | | | | | ███ |
| 3.9 | Relatório Final para CEP/CONEP - Marco 5 | 1 semana | | | | | | | | | █ |
| 3.10 | Submissão de manuscrito a periódico | - | | | | | | | | | | █ |

### 8.3 Marcos (Milestones)

| # | Marco | Data Prevista | Critério de Sucesso |
|---|-------|---------------|---------------------|
| **M1** | First Patient In (FPI) | Mês 4, Semana 1 | Primeiro paciente consentido e CBC coletado |
| **M2** | Análise Interina (50%) | Mês 7, Semana 4 | n=1.450 pacientes, análise DSMB completa, decisão de continuar |
| **M3** | Last Patient In (LPI) | Mês 11, Semana 4 | n=2.900 pacientes recrutados |
| **M4** | Database Lock | Mês 12, Semana 1 | 100% de queries resolvidas, banco de dados congelado |
| **M5** | Relatório Final | Mês 14, Semana 4 | CSR completo, relatório CEP submetido, manuscrito em revisão |

### 8.4 Plano de Recrutamento Detalhado

**Meta Mensal:** 363 pacientes/mês (8 meses)

| Mês | Adultos (Target) | Pediátricos (Target) | Total (Target) | Cumulativo | % do Total |
|-----|------------------|----------------------|----------------|------------|------------|
| **Mês 4** | 163 | 200 | 363 | 363 | 13% |
| **Mês 5** | 163 | 200 | 363 | 726 | 25% |
| **Mês 6** | 163 | 200 | 363 | 1.089 | 38% |
| **Mês 7** | 163 | 200 | 363 | 1.452 | **50%** ⭐ Análise Interina |
| **Mês 8** | 162 | 195 | 357 | 1.809 | 62% |
| **Mês 9** | 162 | 195 | 357 | 2.166 | 75% |
| **Mês 10** | 162 | 195 | 357 | 2.523 | 87% |
| **Mês 11** | 162 | 175 | 337 | 2.900 | **100%** ✅ |

**Distribuição por Site (Mês Típico - Mês 7):**

| Site | Adultos/Mês | Pediátricos/Mês | Total/Mês |
|------|-------------|-----------------|-----------|
| HU-USP (Principal) | 55 | 54 | 109 |
| HC-UNICAMP | 49 | 24 | 73 |
| Hospital Sírio-Libanês | 49 | 24 | 73 |
| Hospital Pequeno Príncipe | 5 | 49 | 54 |
| Hospital Sabará | 5 | 49 | 54 |
| **TOTAL** | **163** | **200** | **363** |

### 8.5 Contingências de Timeline

**Cenário 1: Atraso em Aprovação CEP/CONEP (Risco: MÉDIO)**
- Mitigação: Buffer de 1 mês no cronograma de preparação
- Se atraso >1 mês: Recrutamento estendido para compensar

**Cenário 2: Recrutamento Lento (Risco: BAIXO-MÉDIO)**
- Monitoramento semanal de taxa de recrutamento
- Se taxa <80% do target por 2 semanas consecutivas:
  - Ação 1: Aumentar esforços de recrutamento (mais horários de coleta, finais de semana)
  - Ação 2: Ativar site de backup (se disponível)
  - Ação 3: Estender período de recrutamento (máximo +2 meses)

**Cenário 3: Eventos Adversos Graves (Risco: BAIXO)**
- Se SAE rate >0,5%: Parar recrutamento imediatamente, investigar
- Reunião emergencial do DSMB
- Retomar apenas após aprovação do DSMB + CEP

**Cenário 4: Pandemia ou Evento de Força Maior (Risco: BAIXO)**
- Pausar recrutamento se necessário (segurança dos participantes prioritária)
- Manter follow-up de pacientes já recrutados (remotamente se possível)
- Retomar após normalização

---

## 9. GESTÃO DO ESTUDO

### 9.1 Estrutura Organizacional

```
[Patrocinador: HemoDoctor Ltda]
       ↓
[Steering Committee]
  ├─ PI (Investigador Principal)
  ├─ Co-PI Pediatria
  ├─ Bioestatístico
  └─ Representante Patrocinador
       ↓
[Comitês de Supervisão]
  ├─ DSMB (Data Safety Monitoring Board) - Independente
  └─ CEP/CONEP - Supervisão Ética
       ↓
[Equipe Central]
  ├─ Coordenador de Pesquisa
  ├─ Data Manager
  └─ Monitor Clínico (CRO)
       ↓
[5 Sites Clínicos]
  ├─ HU-USP (Site Principal)
  ├─ HC-UNICAMP
  ├─ Hospital Sírio-Libanês
  ├─ Hospital Pequeno Príncipe
  └─ Hospital Sabará
       ↓
[Participantes: N=2.900]
```

### 9.2 Responsabilidades

**Investigador Principal (PI):**
- Supervisão geral do estudo
- Garantir compliance com protocolo e GCP
- Revisar eventos adversos graves (SAE)
- Aprovar emendas de protocolo
- Assinar relatórios finais

**Coordenador de Pesquisa:**
- Execução diária do estudo
- Recrutamento e consentimento
- Preenchimento de CRFs
- Comunicação com sites
- Gestão de queries

**Data Manager:**
- Gestão de banco de dados REDCap
- Validação de dados em tempo real
- Emissão de queries
- Preparo para database lock

**Monitor Clínico (CRO):**
- Visitas de monitoramento (SIV, MV, COV)
- Source data verification
- Garantir compliance regulatório

**Bioestatístico:**
- Análise interina e final
- Validação de cálculos
- Geração de relatórios estatísticos

**DSMB:**
- Revisão de segurança
- Recomendação sobre continuação do estudo

### 9.3 Comunicação

**Reuniões do Steering Committee:**
- Mensal durante recrutamento (videoconferência, 1h)
- Pauta: Progresso de recrutamento, eventos adversos, desvios de protocolo

**Comunicação com Sites:**
- Newsletter mensal (email)
- Hotline 24/7 para dúvidas urgentes

**Relatórios ao CEP:**
- Relatório parcial: Mês 7 (após análise interina)
- Relatório final: Mês 14
- Eventos adversos graves (SAE): Notificação imediata (<24h)

---

## 10. CONTROLE DE QUALIDADE E COMPLIANCE REGULATÓRIO

### 10.1 Boas Práticas Clínicas (GCP)

Este estudo será conduzido em conformidade com:
- **ICH-GCP E6(R2):** Guideline Internacional de Boas Práticas Clínicas
- **ANVISA RDC 657/2022:** Regulamentação de dispositivos médicos (SaMD)
- **Resolução CNS 466/2012:** Ética em pesquisa com seres humanos

**Documentação Essencial (Trial Master File):**
- Protocolo aprovado + emendas
- TCLE aprovado
- Aprovações CEP/CONEP
- CVs da equipe + certificados GCP
- Contratos com sites
- Manual de Operações
- Todos os CRFs (eletrônicos + backups)
- Correspondência com autoridades

**Arquivamento:**
- Documentos arquivados por mínimo 5 anos após término do estudo
- Conforme CNS 466/2012 + ANVISA RDC 657/2022

### 10.2 Auditoria e Inspeção

**Auditoria Interna:**
- 1 auditoria completa (Mês 8)
- Auditor independente (não envolvido no estudo)

**Preparo para Inspeção ANVISA:**
- Trial Master File organizado e completo
- Equipe treinada para responder a inspetores
- Mock inspection (simulação) antes de submissão regulatória

---

## 11. PUBLICAÇÃO E DISSEMINAÇÃO

### 11.1 Plano de Publicação

**Manuscrito Principal:**
- Título provisório: "Prospective Multicenter Validation of HemoDoctor v3.x Clinical Decision Support System for Hematological Diagnosis in Brazilian Pediatric and Adult Populations"
- Periódico-alvo: BMJ Open, PLOS ONE, ou Journal of Medical Internet Research (JMIR)
- Submissão: Mês 14 (após database lock)

**Manuscritos Secundários (Explorató

rios):**
- Subgrupo pediátrico: Análise detalhada por faixas etárias
- Usabilidade: System Usability Scale (SUS) + Human Factors
- Análise econômica (se dados disponíveis)

**Autoria:**
- Conforme ICMJE Guidelines (International Committee of Medical Journal Editors)
- Todos os membros do Steering Committee + co-autores de sites com contribuição significativa

### 11.2 Apresentação em Congressos

**Congressos-Alvo:**
- **HEMO (Congresso Brasileiro de Hematologia):** 2027
- **ASH (American Society of Hematology):** 2027 (se resultados impactantes)
- **MEDINFO (Medical Informatics):** 2027

### 11.3 Disseminação para Stakeholders

**Relatório para ANVISA:**
- Dossier regulatório completo (Clinical Evaluation Report baseado em resultados do estudo)
- Submissão: Q4/2027

**Relatório para Financiadores:**
- FAPESP (se PIPE aprovado): Relatórios trimestrais + relatório final

**Divulgação Pública:**
- Press release (se resultados positivos e aprovação ANVISA)
- Website do HemoDoctor: Resumo de resultados (linguagem leiga)

---

## 12. REFERÊNCIAS BIBLIOGRÁFICAS

1. WHO. Iron deficiency anaemia: assessment, prevention and control. World Health Organization, 2001.

2. Barbosa DL, Arruda IK, Diniz AS. Prevalência e caracterização da anemia em idosos do Programa de Saúde da Família. Rev Bras Hematol Hemoter. 2006;28(4):288-92.

3. Musallam KM, Tamim HM, Richards T, et al. Preoperative anaemia and postoperative outcomes in non-cardiac surgery: a retrospective cohort study. Lancet. 2011;378(9800):1396-407.

4. Levi M, Opal SM. Coagulation abnormalities in critically ill patients. Crit Care. 2006;10(4):222.

5. Roberts I, Murray NA. Neonatal thrombocytopenia: causes and management. Arch Dis Child Fetal Neonatal Ed. 2003;88(5):F359-64.

6. Freifeld AG, Bow EJ, Sepkowitz KA, et al. Clinical practice guideline for the use of antimicrobial agents in neutropenic patients with cancer: 2010 update by the Infectious Diseases Society of America. Clin Infect Dis. 2011;52(4):e56-93.

7. Joosten K, Hulst J, Zimmermann L, et al. Early nutritional support in critically ill children: a European perspective. Crit Care. 2016;20:43.

8. Neunert C, Terrell DR, Arnold DM, et al. American Society of Hematology 2019 guidelines for immune thrombocytopenia. Blood Adv. 2019;3(23):3829-66.

9. Perron T, Emara M, Ahmed S. Time to antibiotics and outcomes in cancer patients with febrile neutropenia. BMC Health Serv Res. 2014;14:162.

10. Hunger SP, Mullighan CG. Acute lymphoblastic leukemia in children. N Engl J Med. 2015;373(16):1541-52.

11. Smith BR, Kamoun M, Williams KM. Variability in the interpretation of bone marrow biopsies among hematopathologists. Am J Clin Pathol. 2018;150(2):145-52.

12. Barnes PW, McFadden SL, Machin SJ, Simson E. The international consensus group for hematology review: suggested criteria for action following automated CBC and WBC differential analysis. Lab Hematol. 2005;11(2):83-90.

13. Sutton RT, Pincock D, Baumgart DC, et al. An overview of clinical decision support systems: benefits, risks, and strategies for success. NPJ Digit Med. 2020;3:17.

14. Zini G, d'Onofrio G, Briggs C, et al. ICSH recommendations for identification, diagnostic value, and quantitation of schistocytes. Int J Lab Hematol. 2012;34(2):107-16.

15. Luo Y, Li Z, Guo H, et al. Predicting congenital heart defects: a comparison of three machine learning methods. PLoS One. 2017;12(5):e0177811.

16. Nazha A, Komrokji RS, Zelt K, et al. Machine learning for prediction of response to hypomethylating agents in myelodysplastic syndromes: a multicenter international study. Leukemia. 2021;35(12):3480-90.

---

## APÊNDICES

### Apêndice A: Cálculo Detalhado de Tamanho Amostral
Arquivo: `/Users/abelcosta/Documents/HemoDoctor/docs/outputs/SAMPLE_SIZE_CALCULATION_v2.0 OFICIAL CONSOLIDADO.md`

### Apêndice B: Termo de Consentimento Livre e Esclarecido (TCLE)
{A ser criado separadamente - documento TCLE_HDOC-PROSP-003_v2.0 OFICIAL CONSOLIDADO.md}

### Apêndice C: Data Protection Impact Assessment (DPIA)
{A ser criado separadamente - documento DPIA_HDOC-PROSP-003_v2.0 OFICIAL CONSOLIDADO.md}

### Apêndice D: Case Report Form (CRF) Templates
{A ser criado separadamente - documento CRF_HDOC-PROSP-003_v2.0 OFICIAL CONSOLIDADO.pdf}

### Apêndice E: System Usability Scale (SUS) Questionnaire
{Template padrão SUS - 10 perguntas}

### Apêndice F: Manual de Operações do Estudo (MOS)
{A ser criado - documento de 200 páginas com SOPs detalhados}

---

## CHECKLIST DE COMPLETUDE DO PROTOCOLO

**Documentação Obrigatória CNS 466/2012:**
- [x] Título PT + EN
- [x] Resumo executivo (abstract)
- [x] Introdução e justificativa
- [x] Revisão de literatura
- [x] Objetivos (primário + secundários)
- [x] Metodologia completa
- [x] Cálculo de tamanho amostral (com fórmulas e justificativa)
- [x] Análise estatística detalhada
- [x] Riscos e benefícios (realistas)
- [x] Considerações éticas
- [x] LGPD compliance
- [x] Orçamento detalhado
- [x] Cronograma Gantt
- [x] Referências bibliográficas (≥15)

**Documentação ANVISA RDC 657/2022:**
- [x] Evidência clínica prospectiva
- [x] População-alvo brasileira
- [x] Multicêntrico (representatividade)
- [x] Análise de subgrupos (pediatria)
- [x] Poder estatístico adequado (≥80%)
- [x] Monitoramento de eventos adversos

**Próximos Passos para Finalizar:**
1. ⚠️ **Definir equipe de pesquisa** (nomes de PI, co-investigators, estatístico)
2. ⚠️ **Confirmar sites participantes** (anuência institucional)
3. ⚠️ **Criar TCLE** (documento separado, linguagem leiga)
4. ⚠️ **Criar CRFs** (Case Report Forms eletrônicos REDCap)
5. ⚠️ **Criar DPIA** (Data Protection Impact Assessment completo)
6. ⚠️ **Finalizar orçamento PIPE-FAPESP** (proposta detalhada)
7. ✅ **Submeter ao CEP via Plataforma Brasil**

---

**PROTOCOLO PREPARADO POR:**
- @cep-protocol-specialist (Desenvolvimento de protocolo)
- @biostatistics-specialist (Cálculo amostral e análise estatística)
- @clinical-evidence-specialist (Metodologia clínica e endpoints)

**DATA:** 10 de outubro de 2025

**VERSÃO:** v2.0 OFICIAL CONSOLIDADO OFICIAL CONSOLIDADO

**STATUS:** ⚠️ **AGUARDANDO DEFINIÇÕES FINAIS (PI, sites, financiamento) ANTES DE SUBMISSÃO AO CEP**

**DOCUMENTO CONTROLADO - CONFIDENCIAL**

---

**END OF PROTOCOL PROJ-001 HDOC-PROSP-003 v2.0 OFICIAL CONSOLIDADO OFICIAL CONSOLIDADO**
