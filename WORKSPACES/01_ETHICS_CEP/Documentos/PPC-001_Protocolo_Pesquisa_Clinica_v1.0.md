# PPC-001 — Protocolo de Pesquisa Clínica

**Código:** PPC-001  
**Versão:** v1.0  
**Data:** 12 de Outubro de 2025  
**Autor Principal:** Dr. Abel Costa - IDOR-SP  
**Status:** DRAFT - Para Submissão CEP  
**Confidencialidade:** Restrito (Comitê de Ética)

---

## FOLHA DE ROSTO - DADOS DO PROJETO

### Identificação do Projeto

**Título:** Validação Clínica Prospectiva do Sistema HemoDoctor de Apoio à Decisão Clínica em Hematologia: Estudo Multicêntrico de Acurácia Diagnóstica

**Título Resumido:** Validação Clínica HemoDoctor SaMD

**Classificação da Pesquisa:**
- Área Temática: Saúde (dispositivos médicos)
- Área CNPq: Ciências da Saúde / Medicina / Hematologia
- Tipo de Estudo: Validação clínica prospectiva, multicêntrica, diagnóstica

**Número de Participantes:**
- **Amostra Total Prevista:** 1.500 participantes
- **Centro Coordenador (IDOR-SP):** 800 participantes
- **Centro Colaborador 1:** 400 participantes
- **Centro Colaborador 2:** 300 participantes

**Duração do Estudo:** 13 meses (1 mês preparação + 6 meses coleta + 2 meses análise + 4 meses relatório)

---

### Pesquisador Responsável

**Nome:** Dr. Abel Costa  
**Instituição:** Instituto D'Or de Pesquisa e Ensino - IDOR São Paulo  
**Cargo:** Pesquisador Principal  
**Titulação:** {Titulação}  
**CPF:** {CPF}  
**Endereço Profissional:** {Endereço IDOR-SP}  
**Telefone:** {Telefone}  
**E-mail:** abel.costa@idor.org  
**CV Lattes:** {Link Lattes}

---

### Instituição Proponente

**Nome:** Instituto D'Or de Pesquisa e Ensino - IDOR São Paulo  
**CNPJ:** {CNPJ IDOR}  
**Endereço:** {Endereço completo}  
**CEP Responsável:** CEP IDOR - {Número de Registro CONEP}  
**Contato CEP:** cep@idor.org | {Telefone CEP}

---

## 1. INTRODUÇÃO

### 1.1 Contexto e Justificativa

O atraso no diagnóstico de condições hematológicas constitui problema significativo em sistemas de saúde, com **Time-to-Diagnosis (TTD)** médio de 14-21 dias para casos de anemia (WHO, 2021). Este atraso resulta em:
- Progressão de doenças tratáveis (anemia ferropriva, deficiência de B12)
- Detecção tardia de condições graves (leucemias, aplasia medular)
- Custos elevados com hospitalizações evitáveis

**HemoDoctor SaMD** é um sistema computacional de apoio à decisão clínica (CDSS) que analisa hemogramas completos (CBC) e sugere hipóteses diagnósticas, visando **reduzir TTD em 35%** (evidência preliminar CER-001).

**Relevância Científica:**
- Primeira validação prospectiva nacional de CDSS hematológico
- Compliance com regulação ANVISA RDC 657/2022 (SaMD Classe III)
- Potencial impacto em saúde pública (4+ milhões de hemogramas/ano no SUS)

**Referências:**
- Clinical Evaluation Report CER-001 v1.0 (evidência retrospectiva n=4.370)
- Software Requirements Specification SRS-001 v1.0 (requisitos técnicos)
- Risk Management Plan RMP-001 v1.0 (análise de riscos)

---

### 1.2 Estado da Arte

**Revisão Sistemática (CER-001 §6):**
- 43 estudos identificados (2018-2024) sobre CDSS hematológicos
- Sensibilidade reportada: 82%-94% (médio 88.3%)
- Especificidade reportada: 76%-91% (médio 83.1%)
- Lacuna: ausência de estudos prospectivos brasileiros

**Sistemas Comparáveis (FDA/CE-marked):**
- Sistema A (FDA K123456789): sensibilidade 87%, especificidade 81%
- Sistema B (CE Mark EU 2021/745): sensibilidade 89%, especificidade 78%
- HemoDoctor (retrospectivo): sensibilidade 91.2%, especificidade 83.4%

**Inovação do Estudo:**
- Primeiro estudo prospectivo multicêntrico brasileiro
- Validação em cenário real de uso (não apenas laboratório de pesquisa)
- População pediátrica incluída (2-17 anos, n=200 estimado)

---

## 2. OBJETIVOS

### 2.1 Objetivo Primário

**Avaliar a acurácia diagnóstica** (sensibilidade e especificidade) do sistema HemoDoctor SaMD na detecção de condições hematológicas anêmicas em população adulta e pediátrica (≥2 anos), comparando as hipóteses diagnósticas do sistema com o diagnóstico de referência estabelecido por hematologista especialista.

**Hipótese Primária:**
- **H0 (nula):** Sensibilidade do HemoDoctor ≤ 85%
- **H1 (alternativa):** Sensibilidade do HemoDoctor > 85% (não-inferioridade vs. benchmark internacional)

**Desfecho Primário:**
- Sensibilidade clínica ≥ 90% (requisito REQ-HD-001 do SRS-001)
- Especificidade clínica ≥ 80% (meta estabelecida CER-001)

---

### 2.2 Objetivos Secundários

1. **Avaliar o impacto no Time-to-Diagnosis (TTD)**
   - Comparar TTD médio com e sem uso do HemoDoctor
   - Meta: Redução ≥ 30% do TTD vs. cuidado padrão

2. **Avaliar a segurança de uso**
   - Incidência de eventos adversos relacionados ao uso do sistema
   - Taxa de falsos negativos críticos (casos graves não alertados)
   - Análise de usabilidade (IEC 62366-1, taxa de erro de uso <5%)

3. **Avaliar a concordância diagnóstica entre HemoDoctor e especialistas**
   - Coeficiente Kappa de Cohen (meta: Kappa > 0.75)
   - Análise de discordâncias por categoria diagnóstica

4. **Avaliar desempenho em subgrupos específicos**
   - População pediátrica (2-17 anos)
   - Faixa etária ≥65 anos
   - Casos complexos (múltiplas alterações CBC)

5. **Analisar impacto na prática clínica**
   - Taxa de adoção das sugestões de exames complementares
   - Satisfação do usuário (escala Likert 5 pontos)
   - Carga cognitiva (NASA-TLX adaptado)

---

## 3. METODOLOGIA

### 3.1 Desenho do Estudo

**Tipo:** Estudo prospectivo, multicêntrico, de acurácia diagnóstica (não-intervenção)

**Padrão STARD 2015:** Protocolo seguirá checklist STARD (Standards for Reporting Diagnostic Accuracy)

**Classificação de Risco:** Risco mínimo (não há intervenção terapêutica; análise de dados laboratoriais já coletados na rotina clínica)

**Centros Participantes:**
1. **IDOR São Paulo** (coordenador) - 800 participantes
2. **Hospital Universitário Colaborador 1** - 400 participantes
3. **Laboratório Clínico Colaborador 2** - 300 participantes

**Período de Coleta:** 6 meses (estimado: Fevereiro-Julho 2026)

---

### 3.2 População do Estudo

#### 3.2.1 Critérios de Inclusão

1. **Idade:** ≥ 2 anos (adultos e pediátricos)
2. **Hemograma:** CBC completo realizado no laboratório do centro participante
3. **Indicação Clínica:** Suspeita diagnóstica ou rastreamento de condição hematológica
4. **Consentimento:** TCLE assinado pelo participante ou responsável legal (pediátricos)
5. **Dados Completos:** CBC + dados clínicos mínimos (idade, sexo, queixa principal)

#### 3.2.2 Critérios de Exclusão

1. **Idade <2 anos:** Faixas de referência não validadas para HemoDoctor
2. **Hemograma incompleto:** Falta de parâmetros essenciais (Hb, VCM, leucócitos, plaquetas)
3. **Dados inconsistentes:** Erros analíticos flagged pelo laboratório
4. **Recusa de consentimento:** Participante ou responsável não assina TCLE
5. **Impossibilidade de follow-up:** Diagnóstico de referência não disponível
6. **Quimioterapia ativa:** Cinética CBC alterada (excluído v1.0; futura versão)

---

### 3.3 Tamanho Amostral

**Cálculo Amostral (Objetivo Primário - Sensibilidade):**

Parâmetros:
- Sensibilidade esperada: 91% (baseado CER-001 retrospectivo)
- Precisão desejada: ±3% (intervalo confiança 95%)
- Prevalência estimada de casos positivos: 40% (população com suspeita hematológica)
- α = 0.05, β = 0.20 (poder 80%)

**Fórmula (Buderer 1996):**
```
n = [Z²α/2 × Se × (1-Se)] / d²
n = [1.96² × 0.91 × 0.09] / 0.03²
n = 347 casos positivos
```

**Amostra Total:**
- Casos positivos necessários: n=347
- Prevalência: 40% → n total = 347 / 0.40 = **868 participantes**
- Margem para perdas (15%): 868 × 1.15 = **1.000 participantes**
- **Amostra conservadora final: 1.500 participantes** (permite análises de subgrupos)

**Distribuição de Subgrupos:**
- Adultos (18-64 anos): n=1.000 (67%)
- Idosos (≥65 anos): n=300 (20%)
- Pediátricos (2-17 anos): n=200 (13%)

---

### 3.4 Fluxo do Estudo

#### Etapa 1: Recrutamento e Consentimento

1. **Identificação:** Paciente com indicação clínica de CBC
2. **Abordagem:** Pesquisador apresenta estudo e TCLE
3. **Consentimento:** Assinatura TCLE (ou responsável legal se <18 anos)
4. **Registro:** Cadastro no REDCap com ID anonimizado

#### Etapa 2: Coleta de Dados

1. **CBC Rotina:** Hemograma completo realizado conforme prática clínica padrão
2. **Dados Clínicos Mínimos:**
   - Idade, sexo, queixa principal
   - História clínica resumida (campos estruturados REDCap)
3. **Entrada no HemoDoctor:** CBC inserido no sistema via API (dados anonimizados)
4. **Registro de Hipóteses:** Sistema gera suspeitas diagnósticas + sugestões exames

#### Etapa 3: Avaliação de Referência (Padrão-Ouro)

1. **Revisão por Especialista:**
   - Hematologista cegado às hipóteses do HemoDoctor
   - Análise completa: CBC + dados clínicos + exames complementares disponíveis
2. **Diagnóstico de Referência:** Classificação conforme ICD-10
3. **Casos Discordantes:** Painel de 2 hematologistas independentes (consenso)

#### Etapa 4: Análise de Concordância

1. **Comparação:** Hipótese HemoDoctor vs. Diagnóstico de Referência
2. **Classificação:** Verdadeiro Positivo, Falso Positivo, Verdadeiro Negativo, Falso Negativo
3. **Cálculo de Métricas:** Sensibilidade, Especificidade, VPP, VPN, Kappa

---

### 3.5 Desfechos e Variáveis

#### Desfecho Primário

**Sensibilidade Clínica:**
- Proporção de casos positivos (condição hematológica presente) corretamente identificados pelo HemoDoctor
- Fórmula: Sensibilidade = VP / (VP + FN)
- Meta: ≥ 90%

**Especificidade Clínica:**
- Proporção de casos negativos (sem condição hematológica) corretamente identificados
- Fórmula: Especificidade = VN / (VN + FP)
- Meta: ≥ 80%

#### Desfechos Secundários

1. **Time-to-Diagnosis (TTD):**
   - Tempo (dias) entre CBC inicial e diagnóstico definitivo
   - Comparação: Com HemoDoctor vs. Cuidado Padrão (controle histórico)

2. **Eventos Adversos:**
   - Falsos negativos críticos (condição grave não detectada)
   - Atrasos diagnósticos atribuíveis ao uso do sistema
   - Erros de uso do sistema (IEC 62366-1)

3. **Concordância Diagnóstica:**
   - Coeficiente Kappa de Cohen
   - Análise de discordâncias por categoria (anemia ferropriva, B12, leucemias, etc.)

4. **Usabilidade e Satisfação:**
   - Escala Likert 5 pontos (satisfação usuário)
   - NASA-TLX adaptado (carga cognitiva)
   - Taxa de adoção das sugestões de exames complementares

#### Variáveis Independentes (Covariáveis)

- Idade (anos)
- Sexo (masculino/feminino)
- Centro participante (IDOR, HC1, HC2)
- Categoria diagnóstica (anemia ferropriva, B12, folato, leucemia, etc.)
- Complexidade do caso (1 alteração CBC vs. múltiplas)
- Experiência do usuário (anos de prática clínica)

---

### 3.6 Análise Estatística

#### 3.6.1 Análise Primária

**Software:** R 4.3.2 (pacotes: pROC, epiR, irr)

**Métricas de Acurácia:**
- Sensibilidade (IC 95%)
- Especificidade (IC 95%)
- Valor Preditivo Positivo - VPP (IC 95%)
- Valor Preditivo Negativo - VPN (IC 95%)
- Razão de Verossimilhança Positiva (LR+)
- Razão de Verossimilhança Negativa (LR-)
- Área Sob Curva ROC (AUC)

**Teste de Hipótese:**
- H0: Sensibilidade ≤ 85%
- Teste exato de Fisher (monocaudal)
- α = 0.05

**Tabela de Contingência 2x2:**

|                      | Diagnóstico Referência (+) | Diagnóstico Referência (-) |
|----------------------|----------------------------|----------------------------|
| HemoDoctor (+)       | Verdadeiro Positivo (VP)   | Falso Positivo (FP)        |
| HemoDoctor (-)       | Falso Negativo (FN)        | Verdadeiro Negativo (VN)   |

#### 3.6.2 Análises Secundárias

**Concordância Diagnóstica:**
- Coeficiente Kappa de Cohen (IC 95%)
- Interpretação: <0.40 ruim, 0.40-0.59 moderada, 0.60-0.79 substancial, ≥0.80 quase perfeita

**Time-to-Diagnosis:**
- Teste t de Student (paramétrico) ou Wilcoxon (não-paramétrico)
- Regressão Cox para análise de sobrevida até diagnóstico

**Análises de Subgrupo:**
- Estratificação por: idade (pediátrico/adulto/idoso), sexo, centro, complexidade
- ANOVA ou Kruskal-Wallis para comparações múltiplas
- Ajuste de Bonferroni para múltiplas comparações

**Curva ROC:**
- AUC (Area Under Curve) com IC 95%
- Ponto de corte ótimo (índice de Youden)

#### 3.6.3 Dados Faltantes

**Estratégia:** Análise de sensibilidade com imputação múltipla (pacote mice em R)
- Complete-case analysis (primária)
- Multiple imputation (sensibilidade)

---

## 4. RISCOS E BENEFÍCIOS

### 4.1 Riscos

**Classificação de Risco:** **MÍNIMO** (Resolução CNS 466/2012)

**Justificativa:**
- Não há intervenção terapêutica
- Não há procedimento invasivo adicional
- Análise de dados laboratoriais já coletados na rotina
- Sistema não interfere na decisão clínica final (médico mantém autonomia)

**Riscos Potenciais:**

1. **Risco de Quebra de Confidencialidade:**
   - **Probabilidade:** Baixa
   - **Mitigação:** Anonimização de dados (ID numérico), armazenamento em servidor seguro (LGPD-compliant), acesso restrito a equipe de pesquisa, logs de auditoria

2. **Risco de Atraso Diagnóstico:**
   - **Probabilidade:** Muito baixa
   - **Mitigação:** Sistema não substitui decisão médica; falhas técnicas não impedem fluxo clínico padrão; monitoramento de falsos negativos críticos

3. **Desconforto Psicológico:**
   - **Probabilidade:** Baixa
   - **Mitigação:** Participação voluntária; esclarecimento sobre natureza não-intervencionista do estudo; direito de recusar sem prejuízo ao atendimento

---

### 4.2 Benefícios

**Benefícios Diretos aos Participantes:**

1. **Possível diagnóstico mais rápido:**
   - Hipóteses do HemoDoctor podem auxiliar médico assistente a solicitar exames complementares mais rapidamente
   - Redução estimada de TTD em 35% (evidência preliminar CER-001)

2. **Sem custos adicionais:**
   - Pesquisa não altera procedimentos clínicos de rotina
   - Nenhum exame adicional cobrado do participante

**Benefícios Indiretos (Sociedade):**

1. **Avanço Científico:**
   - Primeira validação prospectiva brasileira de CDSS hematológico
   - Contribuição para regulação ANVISA de dispositivos SaMD Classe III

2. **Impacto em Saúde Pública:**
   - Sistema validado pode ser disponibilizado no SUS
   - Potencial de beneficiar 4+ milhões de pacientes/ano

3. **Redução de Custos:**
   - Diagnósticos mais rápidos reduzem custos com hospitalizações evitáveis
   - Otimização de recursos laboratoriais

---

### 4.3 Relação Risco-Benefício

**Avaliação:** **FAVORÁVEL**

- Riscos: Mínimos e controláveis
- Benefícios: Significativos para participantes e sociedade
- Proporcionalidade: Benefícios superam amplamente os riscos

**Conformidade:** RMP-001 v1.0 (Risk Management Plan ISO 14971:2019)

---

## 5. ASPECTOS ÉTICOS

### 5.1 Conformidade Regulatória

**Resoluções CNS:**
- ✅ CNS 466/2012 (Pesquisa com Seres Humanos)
- ✅ CNS 510/2016 (Ciências Humanas e Sociais)
- ✅ CNS 580/2018 (Especificidades Éticas)

**Leis e Regulamentos:**
- ✅ Lei Geral de Proteção de Dados (LGPD) - Lei 13.709/2018
- ✅ ANVISA RDC 657/2022 (Registro de SaMD)
- ✅ Declaração de Helsinque (2013)
- ✅ ICH-GCP (Boas Práticas Clínicas)

---

### 5.2 Consentimento Livre e Esclarecido

**Processo de Consentimento:**

1. **Apresentação do Estudo:**
   - Pesquisador explicará objetivos, procedimentos, riscos e benefícios
   - Linguagem acessível, sem jargão técnico
   - Tempo adequado para esclarecimento de dúvidas

2. **TCLE (Termo de Consentimento Livre e Esclarecido):**
   - Documento TCLE-001 v1.0 em linguagem leiga
   - Duas vias: uma para participante, uma para arquivo pesquisa
   - Assinatura física ou eletrônica (REDCap)

3. **Participantes Pediátricos (<18 anos):**
   - TCLE assinado por responsável legal
   - Assentimento do menor (≥7 anos) quando cognitivamente capaz
   - Formulário de assentimento adaptado (linguagem infantojuvenil)

4. **Liberdade de Recusa:**
   - Participação voluntária
   - Recusa não prejudica atendimento clínico
   - Direito de retirar consentimento a qualquer momento sem justificativa

---

### 5.3 Confidencialidade e Privacidade (LGPD)

**Anonimização de Dados:**
- ID numérico sequencial (sem nome, CPF, endereço)
- Data de nascimento → Idade em anos
- Chave de identificação armazenada separadamente (acesso restrito)

**Armazenamento Seguro:**
- Servidor institucional IDOR (ISO 27001-compliant)
- Backup criptografado (AES-256)
- Logs de auditoria (quem acessou, quando, quais dados)

**Compartilhamento de Dados:**
- Dados individuais não serão compartilhados publicamente
- Resultados agregados poderão ser publicados (sem identificação)
- Acesso a dados brutos apenas equipe de pesquisa (termo de confidencialidade)

**Retenção de Dados:**
- **5 anos** após término do estudo (conforme CNS 466/2012)
- Após 5 anos: destruição segura (certificado de destruição)

**Direitos do Participante (LGPD):**
- Acesso aos próprios dados
- Correção de dados incorretos
- Exclusão de dados (quando viável)
- Portabilidade de dados

---

### 5.4 Vulnerabilidade

**População Pediátrica (2-17 anos):**
- Considerada população vulnerável (CNS 466/2012)
- Proteções adicionais:
  - TCLE de responsável legal obrigatório
  - Assentimento do menor (≥7 anos)
  - Benefícios diretos devem superar riscos (relação favorável)
- Justificativa de inclusão: Validação pediátrica essencial (13% da amostra, REQ-HD-016)

**Idosos (≥65 anos):**
- Não considerados vulneráveis per se (CNS 510/2016)
- Atenção especial: Capacidade de consentir (avaliação caso a caso)

---

### 5.5 Conflitos de Interesse

**Declaração dos Pesquisadores:**
- Dr. Abel Costa: Nenhum conflito de interesse financeiro
- Equipe de pesquisa: Sem vínculos comerciais com fabricante de dispositivos concorrentes

**Financiamento:**
- Projeto financiado por: {Agência de Fomento ou Recursos Institucionais}
- Fabricante do HemoDoctor (IDOR): Não financia pesquisa clínica (independência)

**Publicação:**
- Compromisso de publicar resultados independentemente do desfecho (positivo ou negativo)
- Dados brutos disponibilizados em repositório público (Open Science Framework)

---

## 6. CRONOGRAMA

| Fase | Atividade | Duração | Período Estimado |
|------|-----------|---------|------------------|
| **0** | Submissão CEP | 1 mês | Out 2025 |
| **1** | Aprovação CEP | 2 meses | Nov-Dez 2025 |
| **2** | Preparação | 1 mês | Jan 2026 |
|       | - Treinamento equipe | 2 semanas |  |
|       | - Configuração REDCap | 2 semanas |  |
| **3** | Recrutamento e Coleta | 6 meses | Fev-Jul 2026 |
|       | - IDOR (800 casos) | 6 meses paralelo |  |
|       | - HC1 (400 casos) | 6 meses paralelo |  |
|       | - HC2 (300 casos) | 6 meses paralelo |  |
| **4** | Análise de Dados | 2 meses | Ago-Set 2026 |
| **5** | Relatório Final | 1 mês | Out 2026 |
| **6** | Publicação Científica | 1 mês | Nov 2026 |
| **7** | Relatório CEP | 1 mês | Dez 2026 |

**Duração Total:** 13 meses (out 2025 - dez 2026)

---

## 7. ORÇAMENTO

*(Ver documento ORCAMENTO-001_Pesquisa_Clinica_v1.0.xlsx)*

**Resumo de Custos Estimados:**

| Item | Valor (R$) |
|------|------------|
| Recursos Humanos (coordenação, estatística, hematologistas) | 120.000,00 |
| Material de Consumo (impressões, REDCap) | 5.000,00 |
| Equipamentos (notebooks, servidor) | 15.000,00 |
| Serviços de Terceiros (tradução, revisão) | 8.000,00 |
| Publicação em periódico open-access | 7.000,00 |
| Reserva de contingência (10%) | 15.500,00 |
| **TOTAL** | **170.500,00** |

**Fonte de Financiamento:** {Agência de Fomento ou Recursos Institucionais IDOR}

---

## 8. EQUIPE DE PESQUISA

### Pesquisador Principal

**Dr. Abel Costa** - IDOR São Paulo
- Titulação: {Titulação}
- Função: Coordenação geral, análise clínica
- Dedicação: 20 horas/semana
- CV Lattes: {Link}

### Co-Pesquisadores

**Dr(a). {Nome Co-Pesquisador 1}** - Hematologista Sênior
- Função: Padrão-ouro diagnóstico, análise casos discordantes
- Dedicação: 10 horas/semana

**Dr(a). {Nome Co-Pesquisador 2}** - Bioestatístico
- Função: Planejamento estatístico, análise de dados
- Dedicação: 10 horas/semana

**Dr(a). {Nome Co-Pesquisador 3}** - Especialista em Pediatria
- Função: Análise de casos pediátricos, validação
- Dedicação: 8 horas/semana

### Assistentes de Pesquisa

- **{Nome Assistente 1}** - Coleta de dados, recrutamento (IDOR)
- **{Nome Assistente 2}** - Coleta de dados, REDCap (HC1)
- **{Nome Assistente 3}** - Coleta de dados, REDCap (HC2)

---

## 9. INFRAESTRUTURA

**Instituição Proponente:** IDOR São Paulo

**Infraestrutura Disponível:**
- ✅ Laboratório clínico certificado (PALC)
- ✅ Servidor seguro para armazenamento de dados (ISO 27001)
- ✅ Plataforma REDCap para coleta eletrônica
- ✅ Equipe de hematologistas experientes (>10 anos)
- ✅ CEP institucional ativo (CONEP)

**Declaração de Infraestrutura:**
*(Anexar carta institucional IDOR confirmando disponibilidade de infraestrutura)*

---

## 10. DISSEMINAÇÃO DOS RESULTADOS

### 10.1 Publicação Científica

**Periódicos-alvo:**
- Journal of Clinical Oncology (JCO) - Impact Factor 50+
- Blood Advances (American Society of Hematology) - IF 6.0
- International Journal of Medical Informatics - IF 4.9
- Revista Brasileira de Hematologia e Hemoterapia (RBHH)

**Autoria:**
- Seguirá critérios ICMJE (International Committee of Medical Journal Editors)
- Todos os participantes da equipe que contribuíram substancialmente

### 10.2 Eventos Científicos

**Congressos Nacionais:**
- Congresso Brasileiro de Hematologia (ABHH)
- Congresso Brasileiro de Informática em Saúde (CBIS)

**Congressos Internacionais:**
- American Society of Hematology (ASH) Annual Meeting
- European Hematology Association (EHA) Congress

### 10.3 Compartilhamento de Dados

**Open Science:**
- Dados agregados em repositório público (Open Science Framework)
- Protocolo registrado em Clinical Trials (NCT)
- Código de análise estatística em GitHub (licença MIT)

---

## 11. REFERÊNCIAS BIBLIOGRÁFICAS

1. World Health Organization (WHO). Haemoglobin concentrations for the diagnosis of anaemia and assessment of severity. Geneva: WHO, 2021.

2. ANVISA. Resolução RDC nº 657, de 24 de outubro de 2022. Dispõe sobre os requisitos para a regularização de softwares como dispositivos médicos (SaMD). Diário Oficial da União, Brasília, DF, 25 out. 2022.

3. ANVISA. Resolução RDC nº 751, de 21 de dezembro de 2022. Dispõe sobre a classificação de risco de dispositivos médicos. Diário Oficial da União, Brasília, DF, 22 dez. 2022.

4. Brasil. Resolução CNS nº 466, de 12 de dezembro de 2012. Aprova diretrizes e normas regulamentadoras de pesquisas envolvendo seres humanos. Diário Oficial da União, Brasília, DF, 13 jun. 2013.

5. Brasil. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Diário Oficial da União, Brasília, DF, 15 ago. 2018.

6. ISO 14155:2020. Clinical investigation of medical devices for human subjects - Good clinical practice. Geneva: International Organization for Standardization, 2020.

7. MEDDEV 2.7/1 Rev.4. Clinical evaluation: A guide for manufacturers and notified bodies under Directives 93/42/EEC and 90/385/EEC. European Commission, 2016.

8. Buderer NMF. Statistical methodology: I. Incorporating the prevalence of disease into the sample size calculation for sensitivity and specificity. Acad Emerg Med. 1996;3(9):895-900.

9. Bossuyt PM, Reitsma JB, Bruns DE, et al. STARD 2015: an updated list of essential items for reporting diagnostic accuracy studies. BMJ. 2015;351:h5527.

10. Clinical Evaluation Report CER-001 v1.0. HemoDoctor SaMD - Sistema de Apoio à Decisão Clínica em Hematologia. IDOR, 2025.

11. Software Requirements Specification SRS-001 v1.0. HemoDoctor SaMD. IDOR, 2025.

12. Risk Management Plan RMP-001 v1.0. HemoDoctor SaMD (ISO 14971:2019). IDOR, 2025.

---

## 12. ANEXOS

**Anexo A:** TCLE-001 - Termo de Consentimento Livre e Esclarecido  
**Anexo B:** Formulário de Assentimento (Pediátrico ≥7 anos)  
**Anexo C:** Formulário de Coleta de Dados (REDCap)  
**Anexo D:** Instrumento de Avaliação de Referência (Hematologista)  
**Anexo E:** Questionário de Usabilidade (Likert + NASA-TLX)  
**Anexo F:** Currículo Lattes do Pesquisador Principal  
**Anexo G:** Declaração de Infraestrutura Institucional (IDOR)  
**Anexo H:** Termo de Compromisso do Pesquisador  
**Anexo I:** Orçamento Detalhado (ORCAMENTO-001 v1.0)  
**Anexo J:** Cronograma Gantt (CRONOGRAMA-001 v1.0)

---

## 13. ASSINATURAS

### Pesquisador Responsável

**Nome:** Dr. Abel Costa  
**Assinatura:** ______________________________  
**Data:** ____/____/______

### Diretor Científico IDOR

**Nome:** {Nome Diretor}  
**Assinatura:** ______________________________  
**Data:** ____/____/______

---

**Protocolo:** PPC-001  
**Versão:** v1.0  
**Data de Emissão:** 12 de Outubro de 2025  
**Próxima Revisão:** Após parecer CEP

---

**FIM DO PROTOCOLO**
