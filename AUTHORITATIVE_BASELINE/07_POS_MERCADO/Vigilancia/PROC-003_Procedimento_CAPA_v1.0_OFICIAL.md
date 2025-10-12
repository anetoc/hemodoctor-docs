---
document_id: "PROC-003"
title: "Procedimento CAPA - Corrective and Preventive Actions"
version: "1.0"
status: "OFICIAL"
date: "2025-10-12"
author: "Quality Systems Specialist"
organization: "IDOR-SP"
classification: "Dispositivo Médico - Classe II"
compliance:
  - "ISO 13485:2016 (§8.5.2 e §8.5.3)"
  - "21 CFR Part 820.100 (FDA CAPA)"
  - "ISO 14971:2019"
  - "ANVISA RDC 16/2013"
history:
  - version: "1.0"
    date: "2025-10-12"
    changes: "Versão inicial do procedimento CAPA"
    author: "Quality Systems Specialist"
---

# PROC-003: Procedimento CAPA - Corrective and Preventive Actions

**HemoDoctor - Dispositivo Médico Classe II (SaMD)**

---

## 1. OBJETIVO

Este procedimento estabelece um processo sistemático e estruturado para:

- **Eliminar causas de não-conformidades detectadas** através de ações corretivas
- **Prevenir ocorrência de não-conformidades potenciais** através de ações preventivas
- **Melhorar continuamente o sistema de qualidade** do HemoDoctor
- **Cumprir requisitos regulatórios** ISO 13485:2016, 21 CFR Part 820.100 (FDA) e ANVISA RDC 16/2013

### Escopo

Este procedimento aplica-se a:
- Todas as não-conformidades identificadas no desenvolvimento, produção e vigilância pós-mercado do HemoDoctor
- Incidentes, reclamações, auditorias, desvios de processo e análises de tendências
- Todas as áreas organizacionais: Desenvolvimento, Qualidade, Operações, Suporte Clínico

---

## 2. DEFINIÇÕES

### 2.1. Termos Críticos

- **Ação Corretiva**: Ação para eliminar a causa de uma não-conformidade **DETECTADA** e prevenir sua recorrência.
  - Exemplo: Bug crítico causou crash → corrigir o bug + teste de regressão

- **Ação Preventiva**: Ação para eliminar a causa de uma não-conformidade **POTENCIAL** identificada através de análise de tendências, auditorias ou near misses.
  - Exemplo: Análise de logs mostra padrão de lentidão → otimizar código antes de afetar usuários

- **Não-conformidade**: Não cumprimento de um requisito especificado em normas, regulamentações, especificações ou procedimentos internos.
  - Exemplo: Requisito REQ-FUNC-015 (validação de idade pediátrica) não foi implementado

- **Causa raiz**: Razão fundamental identificável e verificável de um problema, cuja eliminação previne a recorrência.
  - Exemplo: Falta de validação de input → permite entrada de dados inválidos → sugestão incorreta

- **CAPA**: Sistema integrado de ações **C**orretivas e **A**ções **P**reventivas (do inglês *Corrective and Preventive Actions*)

- **Eficácia**: Grau de realização do resultado planejado. Uma ação é eficaz se eliminou a causa raiz e preveniu recorrência.
  - Medida objetiva: 0% de recorrência após implementação + período de monitoramento

### 2.2. Acrônimos

- **RCA**: Root Cause Analysis (Análise de Causa Raiz)
- **NC**: Não-conformidade
- **QA**: Quality Assurance (Garantia de Qualidade)
- **RT**: Responsável Técnico
- **SLA**: Service Level Agreement (Acordo de Nível de Serviço)
- **KPI**: Key Performance Indicator (Indicador Chave de Performance)

---

## 3. QUANDO ABRIR CAPA

### 3.1. Gatilhos Obrigatórios (CAPA DEVE ser aberta)

1. **Incidente GRAVE com paciente** (conforme PROC-001)
   - Morte, lesão grave, ameaça à vida relacionada ao HemoDoctor
   - Exemplo: Sugestão diagnóstica incorreta seguida pelo médico causou dano ao paciente

2. **Bug CRÍTICO de software**
   - Crash, perda de dados, indisponibilidade do sistema
   - Exemplo: Falha no módulo de inferência causa crash em 10% das requisições

3. **Reclamação recorrente de usuário** (≥ 3x mesmo problema)
   - Múltiplos relatos do mesmo tipo de problema indicam causa sistêmica
   - Exemplo: 3 médicos diferentes relatam timeout na tela de resultados

4. **Auditoria interna: Não-conformidade MAIOR**
   - NC classificada como MAIOR (impacto significativo na qualidade/segurança)
   - Exemplo: Auditoria encontra 15 testes de validação não executados (TST-001)

5. **Auditoria externa: Qualquer NC**
   - Auditorias de certificadora ISO 13485, ANVISA, FDA → toda NC requer CAPA
   - Exemplo: Auditoria ISO encontra procedimento de calibração não seguido

6. **Falha em teste de sistema** (requisito crítico não atendido)
   - Teste de validação falha para requisito de segurança ou eficácia
   - Exemplo: Teste de precisão diagnóstica: Especificado 85%, medido 78%

7. **Desvio de processo de qualidade**
   - Processo documentado não foi seguido e impactou qualidade
   - Exemplo: Release deployado em produção sem aprovação do RT

8. **Near miss GRAVE** (quase-acidente com potencial de dano)
   - Problema detectado antes de causar dano, mas com potencial grave
   - Exemplo: Validação de input falhou, mas médico notou erro antes de seguir sugestão

9. **Análise de tendências: Padrão negativo identificado**
   - Dashboards de monitoramento mostram degradação de métricas
   - Exemplo: Taxa de erro do modelo HemoAI subiu de 5% para 15% em 3 meses

10. **Recall ou Field Safety Corrective Action (FSCA)**
    - Necessidade de retirar produto do mercado ou notificar usuários
    - Exemplo: Versão 2.3.1 tem bug crítico → recall + hotfix urgente

### 3.2. Gatilhos Opcionais (decisão do Gerente de Qualidade)

- **Reclamação única de usuário** (severidade média)
  - Avaliação: É caso isolado ou potencial sistêmico?

- **Sugestão de melhoria de processo**
  - Oportunidade identificada por colaborador
  - Exemplo: "Poderíamos automatizar validação de CBC para reduzir erros"

- **Oportunidade de otimização**
  - Não é problema, mas há espaço para melhoria
  - Exemplo: Tempo de resposta do sistema é aceitável (3s), mas poderia ser 1s

### 3.3. Quando NÃO abrir CAPA

- Problemas pontuais resolvidos sem risco de recorrência
- Questões de suporte técnico já resolvidas (ex: erro de senha do usuário)
- Bugs triviais de baixo impacto (ex: erro de digitação em label de UI)

Para esses casos: Registrar no sistema de tickets, resolver, e documentar. Não requer CAPA formal.

---

## 4. PROCESSO CAPA (8 ETAPAS - 100 dias típico)

### 4.1. ETAPA 1: ABERTURA (Dia 0)

#### 4.1.1. Informações Obrigatórias

Ao abrir um CAPA, coletar:

**A) Identificação do Problema**
- Descrição clara e objetiva: **Quem, o que, quando, onde**
- Evitar linguagem vaga: ❌ "Sistema está lento" → ✅ "Tempo de resposta do HemoAI aumentou de 2s para 15s em 40% das requisições desde 01/10/2025"

**B) Evidências Iniciais**
- Fatos, dados, documentos que comprovam o problema
- Anexos: Logs, screenshots, relatórios de incidente, reclamações de usuários
- Referência: Link para INC-YYYY-XXX se originado de incidente

**C) Classificação**

Tipo:
- □ **Corretiva** (problema já ocorreu, vamos eliminar causa e prevenir recorrência)
- □ **Preventiva** (problema ainda não ocorreu, mas identificamos risco potencial)

Fonte:
- □ Incidente (referência: INC-YYYY-XXX)
- □ Auditoria (interna/externa)
- □ Reclamação de usuário
- □ Near Miss (quase-acidente)
- □ Análise de tendências
- □ Outro: _____________

**D) Responsável Designado**
- Nome completo + Função
- Esta pessoa será o "dono" do CAPA e coordenará todas as etapas
- Critério de escolha: Expertise na área do problema

**E) Prazo Inicial**
- Estimado conforme prioridade (ver seção 6 - Tabela de Priorização)
- CRÍTICA: 30 dias | ALTA: 60 dias | MÉDIA: 90 dias | BAIXA: 120 dias

**F) Número CAPA Gerado**
- Formato: **CAPA-YYYY-XXX** (ano-sequencial)
- Exemplo: CAPA-2025-012
- Sistema gera automaticamente (ou manual se planilha Excel)

#### 4.1.2. Aprovação Inicial

1. **Gerente de Qualidade** revisa e aprova abertura
   - Verifica: Informações estão completas?
   - Verifica: Classificação de prioridade está correta?
   - Verifica: Responsável tem competência?
   - Decisão: Aprovar abertura ✅ ou solicitar mais informações ⚠️

2. **Notificação imediata** (se impacto alto)
   - Notificar: CEO, RT, Gerente de Desenvolvimento
   - Método: Email + reunião emergencial (se CRÍTICO)

#### 4.1.3. Registro

- Registrar no **CAPA Register** (Excel/Jira/QMS)
- Campos mínimos: Número, Data, Tipo, Fonte, Responsável, Status ("Aberto"), Prazo
- Status inicial: **"Aberto - Aguardando Análise"**

---

### 4.2. ETAPA 2: ANÁLISE DE CAUSA RAIZ (Dias 0-15)

#### 4.2.1. Objetivos

- Identificar a **causa fundamental** do problema (não apenas sintomas)
- Causa raiz deve ser **específica, verificável, e eliminável**
- Análise deve ser **baseada em evidências** (não suposições)

#### 4.2.2. Metodologias de RCA

Aplicar pelo menos **2 das 3 metodologias** abaixo:

**A) 5 Whys (Método Toyota)**

Perguntar "por quê" repetidamente até chegar à causa fundamental.

**Exemplo Prático - Incidente Real em Healthcare AI:**

**Problema inicial**: Sistema HemoDoctor sugeriu diagnóstico incorreto para paciente pediátrico (2 anos).

- **Why 1**: Por que a sugestão foi incorreta?
  - **Resposta**: Porque o modelo HemoAI classificou erroneamente os valores de CBC.

- **Why 2**: Por que o modelo classificou erroneamente?
  - **Resposta**: Porque os valores de CBC do paciente estavam fora do range usado no treinamento do modelo.

- **Why 3**: Por que os valores estavam fora do range de treinamento?
  - **Resposta**: Porque o paciente era pediátrico (2 anos) e os ranges hematológicos normais são diferentes de adultos. O modelo foi treinado apenas com dados de adultos.

- **Why 4**: Por que o sistema não detectou que o paciente era pediátrico?
  - **Resposta**: Porque não há validação de idade no módulo de validação de input. O campo "idade" é aceito mas não processado.

- **Why 5**: Por que a validação de idade não estava implementada?
  - **Resposta**: **CAUSA RAIZ**: O requisito REQ-FUNC-015 ("Sistema deve validar idade do paciente e alertar se fora do range 18-80 anos") estava especificado no SRS-001, mas não foi incluído no plano de testes TST-001. Gap de rastreabilidade entre requisitos e testes.

**Ação derivada**: Implementar REQ-FUNC-015 + adicionar teste específico TST-015 + retreinar modelo com dados pediátricos ou documentar limitação no IFU.

---

**B) Ishikawa (Espinha de Peixe - 6M)**

Categorizar causas potenciais em 6 dimensões:

```
                     ┌─── Método (processo, algoritmo)
                     │
                     ├─── Máquina (hardware, infraestrutura)
                     │
 Causa do Problema ──┼─── Material (dados, entrada)
                     │
                     ├─── Mão de obra (treinamento, erro humano)
                     │
                     ├─── Medida (métricas, monitoramento)
                     │
                     └─── Meio ambiente (contexto clínico)
```

**Exemplo para caso do paciente pediátrico:**

1. **Método** (processo, algoritmo):
   - Algoritmo de ML treinado apenas com dados de adultos
   - Processo de validação de input não inclui verificação de idade

2. **Máquina** (hardware, infraestrutura):
   - Não aplicável neste caso (infraestrutura funcionou corretamente)

3. **Material** (dados, entrada):
   - Dados de treino não incluem range pediátrico
   - Input do usuário (idade = 2 anos) foi aceito sem validação

4. **Mão de obra** (treinamento, erro humano):
   - Desenvolvedor não implementou validação de idade (REQ-FUNC-015)
   - QA não detectou gap de teste durante revisão de TST-001
   - Médico usuário não percebeu que sistema não é validado para pediátricos (IFU não documenta claramente)

5. **Medida** (métricas, monitoramento):
   - Dashboard de monitoramento não alerta quando paciente pediátrico é processado
   - Não há métrica de "% pacientes fora do range de idade validado"

6. **Meio ambiente** (contexto clínico):
   - Hospital pediátrico usando sistema validado apenas para adultos
   - Urgência clínica pode ter prejudicado análise crítica do médico

**Análise**: Múltiplas causas contribuintes, mas causa raiz primária é **gap de implementação de requisito + gap de teste**.

---

**C) Análise de Modo de Falha**

Identificar tipo de falha para direcionar ação:

| Tipo de Falha | Descrição | Exemplo | Ação Típica |
|---------------|-----------|---------|-------------|
| **Bug de Software** | Erro de código, lógica incorreta | Null pointer exception, loop infinito, crash | Corrigir código + teste de regressão |
| **Dados Incorretos** | Input inválido não tratado | CBC fora do range normal, formato incorreto | Melhorar validação de entrada + alertas |
| **Uso Inadequado** | Erro do usuário, má interpretação | Médico interpretou sugestão incorretamente | Treinamento + melhorar UX + IFU |
| **Limitação de Design** | Sistema funciona como projetado, mas insuficiente | Edge case não coberto (ex: pediatria) | Redesign ou documentar limitação conhecida |
| **Infraestrutura** | Problema de ambiente técnico | Timeout de rede, latência, GPU não responde | Melhorar infra + monitoramento + retry logic |

**Classificação do exemplo pediátrico**: **Limitação de Design** + **Bug de Software** (validação faltando)

---

#### 4.2.3. Equipe Multidisciplinar

Envolver especialistas conforme tipo de problema:

- **Responsável Técnico (RT)**: Sempre
- **Desenvolvedor**: Se bug ou requisito técnico
- **QA Engineer**: Se falha de teste ou validação
- **Usuário final** (médico/enfermeiro): Se problema de uso ou interpretação
- **Gerente de Qualidade**: Sempre
- **Clinical Expert (hematologista)**: Se impacto clínico ou requisito médico
- **Data Scientist**: Se problema relacionado ao modelo de ML

**Reunião de RCA**: Agendar em até 7 dias após abertura do CAPA. Duração: 2-4h.

#### 4.2.4. Documentar Análise

Criar documento de análise contendo:

1. **Todas as metodologias aplicadas** (5 Whys + Ishikawa + Análise de Falha)
2. **Causa raiz VERIFICÁVEL identificada**
   - Específica (não vaga)
   - Baseada em evidências
   - Explica 100% do problema
3. **Evidências que suportam a causa raiz**
   - Logs, dados, testes, entrevistas
4. **Causas secundárias** (se houver)
   - Fatores contribuintes

#### 4.2.5. Critérios de Aprovação da Etapa 2

Gerente de Qualidade aprova RCA se:

- ✅ Causa raiz é **específica** (não "falha humana" ou "erro de processo")
- ✅ Causa raiz é **verificável** (pode ser testada/comprovada)
- ✅ Causa raiz **explica 100%** do problema
- ✅ Eliminação da causa raiz é **viável** (tecnicamente e financeiramente)

Se não aprovado: Reavaliar análise, coletar mais evidências, refazer RCA.

---

### 4.3. ETAPA 3: PLANEJAMENTO DA AÇÃO (Dias 15-20)

#### 4.3.1. Definir Ação (Critérios SMART)

Toda ação deve ser:

- **S**pecific (Específica): Descrição clara e detalhada
  - ❌ "Melhorar validação"
  - ✅ "Implementar validação de idade pediátrica no módulo Validation Service: rejeitar input se idade < 18 anos com mensagem 'HemoDoctor validado apenas para adultos 18-80 anos'"

- **M**easurable (Mensurável): Critério objetivo de sucesso
  - ✅ "100% dos pacientes com idade < 18 anos serão identificados e rejeitados pelo sistema"

- **A**chievable (Alcançável): Recursos disponíveis, tecnicamente viável
  - Avaliar: Temos desenvolvedores? Budget? Tecnologia existe?

- **R**elevant (Relevante): Ação ataca a causa raiz diretamente
  - ✅ Se causa raiz é "falta de validação", ação é "implementar validação"
  - ❌ Se causa raiz é "falta de validação", ação é "treinar usuários" (não resolve)

- **T**ime-bound (Prazo): Data específica
  - ✅ "Implementação até 30/11/2025"

#### 4.3.2. Plano Detalhado

O plano deve incluir:

**1. Descrição da Ação (detalhada)**

"Implementar validação de idade pediátrica no HemoDoctor conforme REQ-FUNC-015:
- Adicionar validação no módulo `Validation Service` (arquivo `validation.py`)
- Se idade < 18 anos: Rejeitar input com erro HTTP 400 e mensagem: 'HemoDoctor é validado apenas para pacientes adultos (18-80 anos). Para pacientes pediátricos, consulte hematologista.'
- Se idade > 80 anos: Alerta warning (não bloqueia) informando que dados de validação clínica são limitados para idosos
- Atualizar IFU seção 'Limitações' com: 'Sistema não validado para pacientes pediátricos (< 18 anos)'
- Adicionar teste automatizado TST-015 validando rejeição de pacientes < 18 anos"

**2. Objetivos**

- Prevenir 100% de uso do HemoDoctor em pacientes pediátricos
- Cumprir requisito REQ-FUNC-015 (especificado mas não implementado)
- Reduzir risco RMP-001-R12 (uso em população não validada)

**3. Recursos Necessários**

- **Humanos**:
  - 1 Desenvolvedor Backend (8 horas de implementação)
  - 1 QA Engineer (4 horas de teste)
  - 1 Technical Writer (2 horas para atualizar IFU)
  - Total: 14 horas-pessoa

- **Financeiros**:
  - Custo de desenvolvimento: R$ 1.400 (14h × R$100/h)
  - Custo de re-release: R$ 500 (CI/CD, deploy)
  - **Total: R$ 1.900**

- **Técnicos**:
  - Ambiente de desenvolvimento (já disponível)
  - Pipeline CI/CD (já configurado)
  - Servidor de staging para testes (já disponível)

**4. Responsáveis**

- **Primário** (implementa): João Silva (Desenvolvedor Backend)
- **Secundário** (apoia/revisa): Maria Santos (Tech Lead)
- **Revisor QA**: Pedro Costa (QA Engineer)
- **Aprovador**: Dr. Ana Rocha (Responsável Técnico)

**5. Prazo**

- Data de início: 25/10/2025
- Data de conclusão: 15/11/2025
- Duração: 21 dias (incluindo testes e revisões)

**6. Impacto em Outros Processos**

Documentos a atualizar:
- ✅ **SRS-001**: Confirmar que REQ-FUNC-015 já está documentado (sim)
- ✅ **TST-001**: Adicionar novo caso de teste TST-015
- ✅ **IFU-001**: Seção "Limitações" - adicionar nota sobre pediatria
- ✅ **RMP-001**: Atualizar risco R12 (probabilidade reduz de "3" para "1")

Sistemas afetados:
- Validation Service (backend)
- Interface de input de CBC (frontend - mensagem de erro)

Necessidade de retreinamento:
- ❌ Não necessário (validação é explícita no sistema)
- ✅ Comunicar aos usuários via email e nota de release

**7. Critérios de Eficácia** (DEFINIR AGORA)

**Critério 1 - Funcional:**
- **Métrica**: 100% dos inputs com idade < 18 anos são rejeitados pelo sistema
- **Método**: Executar TST-015 com 20 casos de teste (10 pediátricos, 10 adultos)
- **Meta**: 100% pass rate

**Critério 2 - Operacional:**
- **Métrica**: 0 incidentes relacionados a pacientes pediátricos em 60 dias pós-implementação
- **Método**: Monitorar banco de dados de incidentes (query: `SELECT * FROM incidents WHERE tag = 'pediatric' AND date > '2025-11-15'`)
- **Meta**: 0 incidentes

**Critério 3 - Risco:**
- **Métrica**: Risco RMP-001-R12 reavaliado e reduzido
- **Método**: Revisar avaliação de risco (probabilidade cai de 3→1, RPN cai)
- **Meta**: RPN < 50 (aceitável)

**Período de monitoramento**: 60 dias

---

#### 4.3.3. Exemplo de Critério de Eficácia (Geral)

Para qualquer CAPA, critérios de eficácia devem ser:

| Problema Resolvido | Critério de Eficácia | Como Medir | Período |
|--------------------|----------------------|------------|---------|
| Bug causou 5 crashes em setembro | 0 crashes relacionados | Monitorar logs de erro diariamente | 60 dias |
| 3 reclamações de timeout (15s) | Tempo de resposta < 5s em 99% das requisições | Monitorar dashboard APM (Application Performance Monitoring) | 30 dias |
| Auditoria: 15 testes não executados | 100% testes executados e documentados | Re-auditoria interna em TST-001 | 30 dias |
| Near miss: Dados não-validados processados | 100% inputs validados, 0 bypass de validação | Code review + teste de penetração | 30 dias |
| Reclamação: IFU confuso | 0 reclamações sobre mesma seção do IFU | Monitorar tickets de suporte | 90 dias |

---

### 4.4. ETAPA 4: APROVAÇÃO (Dias 20-22)

#### 4.4.1. Fluxo de Aprovação (3 níveis)

**Nível 1: Gerente de Qualidade (SEMPRE obrigatório)**

Revisão:
- ✅ Análise de causa raiz está adequada?
- ✅ Plano de ação é apropriado e ataca a causa raiz?
- ✅ Recursos alocados são suficientes?
- ✅ Critérios de eficácia estão bem definidos?
- ✅ Impacto em outros processos foi avaliado?

Decisão:
- ✅ **Aprovado**: Prosseguir para implementação
- ⚠️ **Aprovado com ressalvas**: Implementar com ajustes menores
- ❌ **Não aprovado**: Refazer plano

**Registro**: Assinatura digital ou física, data de aprovação

---

**Nível 2: Responsável Técnico (SEMPRE obrigatório)**

Revisão:
- ✅ Impacto técnico está corretamente avaliado?
- ✅ Prazo é realista considerando complexidade técnica?
- ✅ Riscos de implementação foram considerados?
- ✅ Mudança está alinhada com arquitetura do sistema?

Decisão: Aprovar ou solicitar ajustes

**Registro**: Assinatura, data

---

**Nível 3: CEO (SE impacto alto)**

Critérios de escalonamento ao CEO:

- ✅ Custo > R$ 50.000
- ✅ Prazo > 90 dias
- ✅ Impacto em múltiplos sistemas ou processos críticos
- ✅ Risco regulatório (recall, suspensão de vendas, perda de certificação)
- ✅ Exposição legal significativa (risco de processo judicial)
- ✅ Necessidade de mudança organizacional (ex: contratar especialista)

Se qualquer critério acima: CEO deve aprovar.

Revisão do CEO:
- ✅ Investimento justifica benefício?
- ✅ Riscos são aceitáveis?
- ✅ Impacto no negócio foi considerado?

**Registro**: Assinatura do CEO, data, comentários

---

#### 4.4.2. Documentação de Aprovação

Registrar no FORM-003 (CAPA Form) seção H:

- Data de cada aprovação
- Nome completo de cada aprovador
- Assinatura (digital ou manuscrita)
- Comentários ou condições (se houver)
  - Exemplo: "Aprovado condicionado a: Re-teste completo antes de deploy em produção"

Após todas as aprovações: Status do CAPA muda para **"Aprovado - Pronto para Implementação"**

---

### 4.5. ETAPA 5: IMPLEMENTAÇÃO (Dias 22-60)

#### 4.5.1. Executar Conforme Plano

1. **Implementar ação técnica** (código, processo, treinamento, documentação)
   - Seguir plano aprovado na Etapa 3
   - Se desvios necessários: Re-aprovar com QA e RT

2. **Documentar TODAS as etapas** (log detalhado)
   - Changelog de código (commits Git com referência ao CAPA)
   - Atas de reuniões de treinamento
   - Evidências de atualização de documentos (diff de versões)

3. **Comunicar à equipe afetada**
   - Email para todos os stakeholders
   - Reunião de kick-off se ação complexa
   - Treinamento formal se mudança de processo

4. **Atualizar documentação impactada**

| Se ação envolve... | Atualizar documento... | Evidência |
|--------------------|------------------------|-----------|
| Correção de código | Changelog, Git commit, Pull Request | Link do PR aprovado |
| Mudança de processo | SOP (Standard Operating Procedure) | SOP v2.0 aprovado |
| Atualização de IFU | IFU (Instructions for Use) | IFU v1.1 assinado pelo RT |
| Novo requisito | SRS (Software Requirements Spec) | SRS v1.2 + rastreabilidade |
| Novo teste | TST (Test Specification) | TST-XXX executado + relatório |
| Mudança de risco | RMP (Risk Management Plan) | RMP-001 revisado |

5. **Registrar evidências**

Coletar e arquivar:
- ✅ Código corrigido (diff antes/depois, Pull Request aprovado)
- ✅ Certificados de treinamento (lista de presença + quiz de avaliação)
- ✅ Documentos atualizados (versão antiga vs nova, changelog)
- ✅ Fotos/prints de implementação (se aplicável)
- ✅ Email de comunicação enviado aos stakeholders

Armazenar em: `CAPAs/2025/CAPA-2025-XXX/Evidencias_Implementacao/`

---

#### 4.5.2. Monitoramento Durante Implementação

**Status semanal para Gerente de Qualidade:**
- Email semanal com progresso (% conclusão, bloqueios, próximos passos)
- Template:
  ```
  CAPA-2025-XXX - Status Semanal
  Responsável: [Nome]
  Período: [Data início] a [Data fim]

  Progresso: 60% concluído
  Realizações esta semana:
  - Código implementado e testado em staging
  - IFU atualizado e revisado por Tech Writer

  Bloqueios:
  - Aguardando aprovação final do RT para deploy em produção

  Próximos passos:
  - Deploy em produção (previsto 10/11)
  - Execução de testes de regressão pós-deploy

  Status do prazo: ✅ No prazo (conclusão prevista 15/11)
  ```

**Alertar imediatamente se:**
- ⚠️ **Atraso**: Prazo não será cumprido (escalar para QA e CEO)
- ⚠️ **Bloqueio**: Impedimento técnico ou organizacional (ex: falta de recurso)
- ⚠️ **Mudança de escopo**: Ação planejada precisa ser alterada (re-aprovar)

---

#### 4.5.3. Aprovação de Implementação

Após implementação completa:

**1. Responsável confirma:**
- ✅ Ação foi implementada conforme plano
- ✅ Todas as evidências estão coletadas e armazenadas
- ✅ Documentação foi atualizada
- ✅ Comunicação foi realizada

**2. QA verifica:**
- ✅ Evidências estão completas (checklist)
- ✅ Documentos atualizados têm versão e aprovação corretas
- ✅ Mudanças estão rastreáveis (Git, registro de mudanças)

**3. RT aprova** (se mudança técnica):
- ✅ Código foi revisado (code review)
- ✅ Testes foram executados e passaram
- ✅ Deploy foi realizado com sucesso
- ✅ Rollback plan está disponível (se necessário)

**Registro**: Assinaturas no FORM-003 seção F (Status e Execução)

Status do CAPA: **"Implementado - Aguardando Verificação de Eficácia"**

---

### 4.6. ETAPA 6: VERIFICAÇÃO DE EFICÁCIA (Dias 60-90)

#### 4.6.1. Período de Monitoramento

**Mínimo**: 30 dias após implementação completa
**Típico**: 60 dias
**Estendido**: 90 dias (para ações complexas ou críticas)

#### 4.6.2. Executar Verificação

1. **Coletar dados** conforme critérios definidos na Etapa 3
   - Usar fontes objetivas: Logs, dashboard, banco de dados, relatórios automatizados
   - Evitar avaliações subjetivas ("parece melhor") → usar dados quantitativos

2. **Comparar situação ANTES vs DEPOIS**

| Métrica | Antes da Ação | Depois da Ação | Meta | Status |
|---------|---------------|----------------|------|--------|
| Crashes/mês | 5 | 0 | 0 | ✅ Atingida |
| Tempo de resposta (p99) | 15s | 3s | < 5s | ✅ Atingida |
| Reclamações/mês | 3 | 0 | 0 | ✅ Atingida |
| Taxa de aprovação em auditoria | 85% | 100% | 100% | ✅ Atingida |

3. **Análise quantitativa e qualitativa**
   - Quantitativa: Números, métricas, percentuais
   - Qualitativa: Feedback de usuários, observações de campo

4. **Verificação objetiva** (não subjetiva)
   - ✅ "0 ocorrências do bug em 60 dias" (objetivo)
   - ❌ "Bug parece resolvido" (subjetivo)

---

#### 4.6.3. Exemplos de Verificação

**Exemplo 1: Bug Corrigido**

- **Problema**: Crash no módulo de inferência (5 ocorrências em setembro)
- **Ação**: Correção do bug + teste de regressão
- **Critério de eficácia**: 0 ocorrências do bug em 30 dias
- **Método de verificação**: Monitorar logs de erro diariamente com query: `SELECT * FROM error_logs WHERE error_type = 'InferenceModuleCrash' AND date > '2025-11-15'`
- **Resultado**: 30 dias completos (15/11 a 15/12) → 0 ocorrências detectadas
- **Conclusão**: ✅ **EFICAZ**

---

**Exemplo 2: Treinamento Realizado**

- **Problema**: 3 médicos interpretaram sugestão diagnóstica incorretamente
- **Ação**: Treinamento completo sobre uso do HemoDoctor (4 horas) + atualização do IFU
- **Critério de eficácia**: 100% da equipe aprovada em teste de conhecimento (nota ≥ 80%)
- **Método de verificação**: Aplicar quiz online pós-treinamento (20 questões)
- **Resultado**:
  - 15 participantes treinados
  - Notas: 14 aprovados (≥ 80%), 1 reprovado (75%)
  - Ação: Retreinamento individual para o 1 reprovado → nota final 85%
  - **Resultado final**: 15/15 aprovados (100%)
- **Conclusão**: ✅ **EFICAZ**

---

**Exemplo 3: Processo Melhorado**

- **Problema**: Auditoria interna encontrou 15 testes não executados (não-conformidade MAIOR)
- **Ação**: Executar todos os 15 testes + atualizar TST-001 + implementar checklist de QA antes de release
- **Critério de eficácia**: 100% conformidade em próxima auditoria interna de follow-up
- **Método de verificação**: Auditoria interna realizada em 30 dias
- **Resultado**:
  - Auditoria de follow-up executada em 15/12/2025
  - Verificação: 15/15 testes executados e documentados
  - 0 não-conformidades encontradas no processo de teste
- **Conclusão**: ✅ **EFICAZ**

---

**Exemplo 4: Ação Preventiva (Análise de Tendências)**

- **Problema**: Dashboard mostra aumento gradual de tempo de resposta (de 2s para 5s em 3 meses)
- **Ação Preventiva**: Otimização de código + aumento de recursos de servidor (antes de afetar usuários)
- **Critério de eficácia**: Tempo de resposta p99 < 3s mantido por 60 dias
- **Método de verificação**: Monitorar dashboard APM diariamente
- **Resultado**:
  - 60 dias de monitoramento (15/11 a 15/01)
  - Tempo de resposta p99: Média 2.1s (range 1.8s-2.5s)
  - 0 reclamações de lentidão
- **Conclusão**: ✅ **EFICAZ**

---

#### 4.6.4. Decisão de Eficácia

Classificar resultado conforme % de critérios atingidos:

| Status | Critérios Atingidos | Ação Necessária |
|--------|---------------------|-----------------|
| ✅ **EFICAZ** | 100% | Prosseguir para fechamento do CAPA |
| ⚠️ **PARCIALMENTE EFICAZ** | 50-99% | Ações adicionais necessárias (mini-CAPA ou extensão) |
| ❌ **INEFICAZ** | < 50% | Reavaliar causa raiz (voltar para Etapa 2) |

**Se EFICAZ**: Documentar resultado positivo, prosseguir para Etapa 7.

**Se PARCIALMENTE EFICAZ**:
- Identificar quais critérios não foram atingidos
- Definir ações adicionais (corretivas)
- Estender prazo de monitoramento
- Exemplo: Meta era 0 reclamações, mas houve 1 reclamação → Investigar se é caso relacionado ou novo problema

**Se INEFICAZ**:
- **Causa raiz foi mal identificada** → Refazer RCA (Etapa 2)
- **Ação foi inadequada** → Replanejar ação (Etapa 3)
- **Implementação foi falha** → Verificar evidências de implementação
- **Novos fatores surgiram** → Ampliar escopo da análise

Gerente de Qualidade deve aprovar decisão de eficácia.

---

### 4.7. ETAPA 7: REVISÃO DA GESTÃO DE RISCO (Dias 90-95)

#### 4.7.1. Objetivo

Avaliar se a ação implementada:
1. Introduziu **novo risco**
2. Afetou **riscos existentes**
3. Resultou em **riscos residuais aceitáveis**

#### 4.7.2. Três Perguntas Obrigatórias

**Pergunta 1: A ação implementada introduziu NOVO risco?**

Exemplo:
- **Ação**: Correção de bug no módulo de inferência (refatoração de código)
- **Novo risco potencial**: Refatoração pode ter introduzido novos bugs em outras partes do código
- **Avaliação**: Risco identificado → Adicionar ao RMP-001 como R25 ("Risco de regressão após correção de bug")
- **Mitigação**: Teste de regressão completo executado + code review por 2 desenvolvedores

**Se SIM**:
- Adicionar novo risco ao **RMP-001** (Risk Management Plan)
- Avaliar severidade e probabilidade
- Definir controles de mitigação
- Atualizar Risk Management File

---

**Pergunta 2: A ação afetou riscos EXISTENTES?**

Mudanças a avaliar:
- **Probabilidade** mudou? (aumentou ou diminuiu)
- **Severidade** mudou? (impacto maior ou menor)
- **Controles de mitigação** mudaram? (novos controles adicionados)

Exemplo:
- **Risco RMP-001-R12**: "Uso do HemoDoctor em população não validada (pediátricos)"
  - **Antes da ação**:
    - Probabilidade: 3 (Provável - não há validação de idade)
    - Severidade: 4 (Grave - risco de diagnóstico incorreto)
    - RPN (Risk Priority Number): 3 × 4 = 12 (Alto)
  - **Ação implementada**: Validação de idade pediátrica (rejeita input se < 18 anos)
  - **Depois da ação**:
    - Probabilidade: 1 (Remoto - sistema bloqueia automaticamente)
    - Severidade: 4 (Grave - mas probabilidade reduzida)
    - RPN: 1 × 4 = 4 (Baixo - aceitável)

**Se SIM**:
- Revisar avaliação de risco no **RMP-001**
- Atualizar tabela de riscos
- Re-calcular RPN (Risk Priority Number)
- Documentar mudança de controles de mitigação

---

**Pergunta 3: Riscos residuais são aceitáveis?**

Após ação implementada:
- Avaliar risco residual (risco que permanece após mitigações)
- Comparar com critérios de aceitabilidade (definidos em RMP-001)
- Exemplo de critério: RPN < 50 = aceitável, RPN ≥ 50 = não aceitável

**Se riscos residuais NÃO são aceitáveis**:
- Ações adicionais são necessárias (abrir novo CAPA ou estender o atual)
- Exemplo: RPN = 60 ainda é alto → Adicionar controle extra (ex: alerta ao usuário + documentar limitação no IFU)

**Se riscos residuais SÃO aceitáveis**:
- Documentar aceitação formal
- Assinatura do RT e Gerente de Qualidade

---

#### 4.7.3. Documentar no RMP-001

**Seção**: Histórico de Revisões (no final do documento RMP-001)

Adicionar entrada:

```markdown
### Revisão 2025-12-15: CAPA-2025-012 - Validação de Idade Pediátrica

**Mudanças**:
- **Risco R12** ("Uso em população não validada - pediátricos"):
  - Probabilidade reduzida de 3 → 1 (controle de validação de idade implementado)
  - RPN reduzido de 12 → 4 (aceitável)
  - Novo controle de mitigação: "Sistema bloqueia input se idade < 18 anos (REQ-FUNC-015)"

**Risco residual**: RPN = 4 (Baixo) - aceitável conforme critérios do RMP.

**Responsável pela revisão**: Dr. Ana Rocha (RT)
**Data**: 15/12/2025
**Referência**: CAPA-2025-012
```

**Versionamento do RMP**:
- Se mudança é significativa (novo risco ou mudança de categoria): Atualizar versão do RMP (ex: v1.0 → v1.1)
- Se mudança é menor (ajuste de RPN): Manter versão, apenas adicionar no histórico

---

### 4.8. ETAPA 8: FECHAMENTO (Dias 95-100)

#### 4.8.1. Critérios para Fechamento

**TODOS os critérios abaixo devem ser atendidos**:

- [x] **Análise de causa raiz** completa e aprovada (Etapa 2)
- [x] **Ação implementada** e evidenciada (Etapa 5)
- [x] **Eficácia VERIFICADA** e confirmada ≥ 80% dos critérios (Etapa 6)
- [x] **Gestão de risco revisada** se aplicável (Etapa 7)
- [x] **Documentação atualizada**: SRS, IFU, TST, RMP conforme necessário
- [x] **Treinamento realizado** se aplicável (e eficácia validada)
- [x] **Comunicação aos stakeholders** realizada (email, reunião, release notes)

Se qualquer critério não for atendido: CAPA não pode ser fechado.

---

#### 4.8.2. Atividades de Fechamento

**1. Confirmar eficácia**
- Responsável do CAPA atesta: "Ação foi eficaz conforme critérios definidos"
- QA revisa e confirma: "Evidências de eficácia estão documentadas e verificadas"

**2. Arquivar documentação**
- Pasta digital: `CAPAs/2025/CAPA-2025-XXX/` (todos os documentos, evidências, aprovações)
- Backup físico (se exigido): Impressão de FORM-003 assinado + sumário executivo
- Retenção: Mínimo **5 anos** (requisito ISO 13485)

**3. Atualizar registros**
- Banco de dados CAPA (Excel/Jira/QMS):
  - Status: "Fechado - Eficaz"
  - Data de fechamento: DD/MM/YYYY
  - Eficácia verificada: ✅ Sim
- Dashboard de CAPA atualizado (backlog -1)

**4. Comunicar fechamento**
- Email para stakeholders:
  ```
  Assunto: [FECHAMENTO] CAPA-2025-012 - Validação de Idade Pediátrica

  Prezados,

  Informamos o fechamento do CAPA-2025-012 após verificação de eficácia.

  Problema resolvido: Sistema HemoDoctor aceitava pacientes pediátricos sem validação.
  Ação implementada: Validação de idade pediátrica (bloqueia input se < 18 anos).
  Eficácia verificada: 100% dos critérios atingidos (0 incidentes em 60 dias, 100% testes passaram).

  Documentos atualizados:
  - IFU-001 v1.1 (seção Limitações)
  - TST-001 v1.2 (novo teste TST-015)
  - RMP-001 v1.1 (risco R12 reduzido)

  Obrigado pela colaboração.

  [Nome do Responsável pelo CAPA]
  ```

**5. Lessons Learned** (opcional, mas recomendado)
- Criar documento sumário (1-2 páginas):
  - O que aprendemos com este CAPA?
  - O que funcionou bem?
  - O que poderia ter sido melhor?
  - Recomendações para CAPAs futuros
- Apresentar em reunião de qualidade mensal

**6. Apresentar em reunião** (se relevante)
- Análise Crítica da Direção (Management Review) trimestral ou anual
- Resumo: Problema → Causa raiz → Ação → Resultado
- KPIs de impacto (ex: "Redução de 100% em incidentes deste tipo")

---

#### 4.8.3. Aprovação de Fechamento

**Assinaturas obrigatórias no FORM-003 seção H:**

1. **Responsável do CAPA**: Atesta conclusão e eficácia
   - Nome: __________________
   - Assinatura: __________________
   - Data: ___/___/______

2. **Gerente de Qualidade**: Aprova fechamento
   - Nome: __________________
   - Assinatura: __________________
   - Data: ___/___/______

3. **Responsável Técnico**: Aprova (se impacto técnico)
   - Nome: __________________
   - Assinatura: __________________
   - Data: ___/___/______

**Status final no sistema**: **"Fechado - Eficaz"**

**Celebrar**: CAPA concluído com sucesso! 🎉 Sistema de qualidade funcionou.

---

## 5. FORMULÁRIO CAPA (FORM-003)

Ver documento separado: **FORM-003_CAPA_v1.0.md**

O formulário contém **30 campos obrigatórios** organizados em **8 seções**:

- **Seção A**: Identificação (número CAPA, data, tipo, fonte)
- **Seção B**: Descrição do Problema (texto livre + evidências)
- **Seção C**: Análise de Causa Raiz (metodologia + causa identificada)
- **Seção D**: Ação Proposta (SMART + responsável + prazo + recursos)
- **Seção E**: Critérios de Eficácia (como medir + indicador + meta)
- **Seção F**: Status e Execução (status atual + % conclusão + datas)
- **Seção G**: Verificação de Eficácia (resultado + evidências)
- **Seção H**: Assinaturas (responsável, QA, RT, CEO se aplicável)

---

## 6. PRIORIZAÇÃO DE CAPA (Tabela com SLAs)

Toda CAPA deve ser priorizada na abertura conforme critérios abaixo:

| Prioridade | Critério | Exemplo | SLA Total | SLA Análise (Etapa 2) | SLA Implementação (Etapa 5) | SLA Verificação (Etapa 6) |
|------------|----------|---------|-----------|------------------------|-----------------------------|---------------------------|
| **CRÍTICA** 🔴 | Risco à segurança do paciente | Incidente GRAVE com dano ao paciente | **30 dias** | 5 dias | 15 dias | 10 dias |
| **ALTA** 🟠 | Não-conformidade regulatória ANVISA/FDA | Auditoria externa, recall | **60 dias** | 10 dias | 30 dias | 20 dias |
| **MÉDIA** 🟡 | Reclamação recorrente (≥ 3x) ou bug médio | Bug repetido, processo falho | **90 dias** | 15 dias | 45 dias | 30 dias |
| **BAIXA** 🟢 | Melhoria de processo | Otimização de workflow, sugestão de usuário | **120 dias** | 20 dias | 60 dias | 40 dias |

### 6.1. Escalonamento Automático

Sistema de alertas:

- ⚠️ **80% do SLA atingido**: Alerta automático ao Gerente de Qualidade
  - Exemplo: CAPA CRÍTICA (SLA 30 dias) → Alerta em 24 dias se ainda não fechado
  - Ação: QA verifica bloqueios, oferece suporte

- 🚨 **100% do SLA atingido** (prazo vencido): Escalação ao CEO
  - Email automático: "CAPA-YYYY-XXX venceu prazo. Ação imediata necessária."
  - Reunião de emergência: QA + RT + Responsável do CAPA + CEO
  - **Justificativa obrigatória**: Por que o prazo não foi cumprido?
  - Possíveis causas legítimas: Bloqueio técnico externo, mudança de escopo aprovada, recurso indisponível
  - Ação: Re-planejar com novo prazo realista + alocar recursos adicionais

### 6.2. Reclassificação de Prioridade

Prioridade pode mudar durante o ciclo de vida do CAPA:

- **Upgrade** (aumentar prioridade):
  - Se análise de RCA revela impacto maior que o inicialmente estimado
  - Se problema se agrava (ex: recorrência aumenta)
  - Aprovação: QA + RT

- **Downgrade** (reduzir prioridade):
  - Se análise de RCA revela impacto menor
  - Se ação de contenção imediata reduziu urgência
  - Aprovação: QA + RT + justificativa documentada

---

## 7. INDICADORES DE DESEMPENHO (KPIs)

### 7.1. KPIs Obrigatórios (ISO 13485:2016 Cláusula 8.5)

| KPI | Fórmula | Meta | Frequência de Medição |
|-----|---------|------|-----------------------|
| **Taxa de Abertura** | CAPAs abertas / mês | < 5 | Mensal |
| **Taxa de Fechamento** | CAPAs fechadas / mês | ≥ CAPAs abertas | Mensal |
| **Tempo Médio de Fechamento** | Σ(data_fechamento - data_abertura) / n | < 90 dias | Mensal |
| **Taxa de Eficácia** | (CAPAs eficazes / CAPAs verificadas) × 100% | > 95% | Trimestral |
| **Taxa de Recorrência** | (CAPAs com mesmo problema reaberto / CAPAs fechadas) × 100% | < 5% | Trimestral |
| **Backlog** | CAPAs em aberto (status ≠ "Fechado") | < 10 | Semanal |

### 7.2. Interpretação dos KPIs

**Taxa de Abertura**:
- **< 5 CAPAs/mês**: Excelente. Sistema de qualidade está estável.
- **5-10 CAPAs/mês**: Aceitável. Monitorar tendências.
- **> 10 CAPAs/mês**: Preocupante. Investigar causas sistêmicas (problemas de design? falta de treinamento? processo inadequado?).

**Taxa de Fechamento**:
- **≥ CAPAs abertas**: Backlog está estável ou diminuindo. ✅
- **< CAPAs abertas**: Backlog está crescendo. Ação necessária: Alocar mais recursos, priorizar CAPAs críticas.

**Tempo Médio de Fechamento**:
- **< 60 dias**: Excelente.
- **60-90 dias**: Aceitável.
- **> 90 dias**: Ações estão demorando demais. Investigar: Falta de recursos? Análise de causa raiz inadequada? Processos lentos?

**Taxa de Eficácia**:
- **> 95%**: Excelente. Ações estão resolvendo problemas.
- **80-95%**: Aceitável, mas há espaço para melhoria.
- **< 80%**: Preocupante. Causas raízes estão sendo mal identificadas ou ações são inadequadas. Revisar processo de RCA.

**Taxa de Recorrência**:
- **< 5%**: Excelente. Problemas não estão voltando.
- **5-10%**: Aceitável.
- **> 10%**: Crítico. Causas raízes não estão sendo eliminadas. Reavaliar metodologia de RCA.

**Backlog**:
- **< 10 CAPAs**: Saudável.
- **10-20 CAPAs**: Atenção. Aumentar recursos de QA.
- **> 20 CAPAs**: Crítico. Sistema de CAPA sobrecarregado. Revisar priorização e alocar time dedicado.

---

### 7.3. Dashboard Mensal de CAPA

**Visualizações obrigatórias:**

1. **Total de CAPAs por status** (gráfico de barras)
   - Aberta | Em Análise | Aprovada | Em Implementação | Em Verificação | Fechada

2. **CAPAs por fonte** (gráfico de pizza)
   - Incidente | Auditoria | Reclamação | Near Miss | Tendência | Outro

3. **CAPAs por tipo** (gráfico de pizza)
   - Corretiva | Preventiva

4. **CAPAs por prioridade** (gráfico de barras)
   - CRÍTICA | ALTA | MÉDIA | BAIXA

5. **CAPAs por responsável** (gráfico de barras - distribuição de carga)
   - Listar top 5 responsáveis com mais CAPAs atribuídas

6. **Tendência de CAPAs** (gráfico de linha - últimos 12 meses)
   - Eixo X: Meses (ex: Jan, Fev, Mar, ..., Dez)
   - Eixo Y: Número de CAPAs abertas
   - Linhas: Abertas (azul), Fechadas (verde), Backlog (vermelho)

---

### 7.4. Análise Trimestral

Gerente de Qualidade deve realizar análise aprofundada a cada 3 meses:

**Perguntas a responder:**

1. **Áreas com mais CAPAs** → Onde estão os problemas recorrentes?
   - Exemplo: 60% dos CAPAs são relacionados ao módulo de inferência → Foco de melhoria
   - Ação: Investigar design do módulo, retreinamento do modelo, revisão de requisitos

2. **Causas raízes recorrentes** → Há padrões?
   - Exemplo: 40% dos CAPAs têm causa raiz "gap de teste" → Ação preventiva sistêmica: Melhorar processo de QA, contratar QA adicional
   - Exemplo: 30% dos CAPAs têm causa raiz "falta de validação de input" → Ação: Criar biblioteca de validação padrão

3. **CAPAs repetidas** → Mesma causa raiz reapareceu?
   - Se SIM: Análise de causa raiz foi inadequada na primeira vez
   - Ação: Revisar metodologia de RCA, envolver especialista externo

4. **Eficácia das ações** → Taxa de eficácia está > 95%?
   - Se NÃO: Por que ações não estão funcionando?
   - Possíveis causas: Ações atacam sintomas e não causa raiz, falta de follow-up, critérios de eficácia mal definidos

5. **Tendência de backlog** → Está crescendo ou diminuindo?
   - Crescendo: Alocar mais recursos
   - Diminuindo: Sistema está funcionando bem

**Relatório trimestral** (template):
```markdown
# Relatório Trimestral de CAPA - Q4 2025

**Período**: Outubro a Dezembro 2025
**Data do Relatório**: 10/01/2026
**Autor**: [Nome do Gerente de Qualidade]

## 1. Resumo Executivo
- Total de CAPAs abertos no trimestre: 12
- Total de CAPAs fechados no trimestre: 10
- Backlog final: 8 (vs 6 no trimestre anterior)
- Taxa de eficácia: 95% (19/20 CAPAs verificados foram eficazes)

## 2. KPIs vs Meta
| KPI | Meta | Resultado | Status |
|-----|------|-----------|--------|
| Taxa de Abertura | < 5/mês | 4/mês | ✅ |
| Tempo Médio de Fechamento | < 90 dias | 72 dias | ✅ |
| Taxa de Eficácia | > 95% | 95% | ✅ |
| Backlog | < 10 | 8 | ✅ |

## 3. Análise de Tendências
- **Área com mais CAPAs**: Módulo de Inferência (5/12 CAPAs = 42%)
- **Causa raiz recorrente**: "Falta de teste de edge cases" (4/12 CAPAs)
- **Ação preventiva proposta**: Criar biblioteca de edge cases para testes automatizados

## 4. CAPAs Críticos Fechados
- CAPA-2025-012: Validação de idade pediátrica (eficaz)
- CAPA-2025-015: Bug de crash no módulo de inferência (eficaz)

## 5. Recomendações
- Investir em QA automation para reduzir gap de testes
- Treinamento de equipe de desenvolvimento em "edge case thinking"
- Considerar contratar QA Engineer adicional se backlog ultrapassar 15

## 6. Conclusão
Sistema de CAPA está funcionando adequadamente. KPIs dentro da meta. Ações preventivas recomendadas para reduzir CAPAs futuros.
```

---

## 8. INTEGRAÇÃO COM OUTROS PROCESSOS

### 8.1. Com Gestão de Incidentes (PROC-001 e PROC-002)

**Fluxo típico:**

```
1. Incidente ocorre
   ↓
2. Relatado via PROC-001 (Relato de Incidentes)
   Gera: INC-2025-XXX
   ↓
3. Investigação via PROC-002 (Investigação RCA)
   Causa raiz identificada
   ↓
4. Decisão: Necessidade de CAPA?
   → SIM: Abrir CAPA-2025-XXX (PROC-003)
   → NÃO: Fechar incidente com ação pontual
   ↓
5. CAPA implementado e eficácia verificada
   ↓
6. Fechar CAPA
   ↓
7. Fechar incidente original (INC-2025-XXX)
```

**Link bidirecional:**
- No FORM-001 (Relato de Incidente): Campo "CAPA Relacionado" → CAPA-2025-XXX
- No FORM-003 (CAPA): Campo "Link com Incidente" → INC-2025-XXX

**Rastreabilidade:**
- Banco de dados deve permitir query: "Listar todos os CAPAs originados de incidentes GRAVES"
- Dashboard: "Taxa de CAPAs originados de incidentes" (meta: < 30% - maioria deveria ser preventiva)

---

### 8.2. Com Gestão de Riscos (RMP-001)

**Integração em 3 momentos:**

**1. Abertura de CAPA (Etapa 1)**
- Pergunta: O problema revelou um **novo risco** não identificado no RMP-001?
- Se SIM: Adicionar ao RMP-001 como novo risco (ex: R26)
- Exemplo: Incidente revela que "Sistema não detecta dados de CBC adulterados intencionalmente" → Novo risco de segurança cibernética

**2. Planejamento da Ação (Etapa 3)**
- Pergunta: A ação proposta pode **criar novo risco**?
- Exemplo: Correção de bug via refatoração massiva de código → Risco de regressão
- Se SIM: Avaliar risco, adicionar controles de mitigação (ex: teste de regressão extensivo)

**3. Fechamento (Etapa 7)**
- Obrigatório: Revisar riscos impactados pela ação
- Atualizar probabilidade, severidade, RPN
- Documentar no histórico de revisões do RMP-001

**Documento RMP-001** deve ter seção:
```markdown
## Revisões por CAPA

| Data | CAPA | Mudança de Risco | Responsável |
|------|------|------------------|-------------|
| 15/12/2025 | CAPA-2025-012 | R12: Probabilidade 3→1, RPN 12→4 | Dr. Ana Rocha |
| 20/12/2025 | CAPA-2025-015 | R08: Adicionado controle de teste de regressão | Dr. Ana Rocha |
```

---

### 8.3. Com Auditoria Interna

**Fluxo:**

1. **Auditoria interna** realizada conforme cronograma (ex: trimestral)
2. **Não-conformidade (NC)** encontrada:
   - NC MAIOR → CAPA obrigatório
   - NC MENOR → CAPA opcional (decisão do QA)
3. **Abrir CAPA** com fonte: "Auditoria Interna [Data]"
4. **Implementar ação** conforme PROC-003
5. **Auditoria de follow-up** (30-90 dias após): Verificar se NC foi resolvida
   - Se resolvida: Fechar CAPA + fechar NC
   - Se não resolvida: Reavaliar causa raiz, estender CAPA

**Registro no relatório de auditoria:**
```markdown
## Não-conformidades Encontradas

| NC | Descrição | Classificação | CAPA Aberto | Status |
|----|-----------|---------------|-------------|--------|
| NC-2025-A01 | 15 testes não executados (TST-001) | MAIOR | CAPA-2025-018 | Fechado (verificado em 15/12) |
| NC-2025-A02 | IFU não menciona limitação pediátrica | MENOR | CAPA-2025-019 | Em andamento |
```

---

### 8.4. Com Treinamento

**Quando CAPA resulta em treinamento:**

Exemplo de causa raiz: "Usuários interpretam sugestão diagnóstica incorretamente"

**Ação de treinamento deve incluir:**

1. **Plano de treinamento**:
   - Conteúdo: O que será ensinado?
   - Duração: Quantas horas?
   - Método: Presencial, online, vídeo, manual?
   - Instrutor: Quem conduzirá?

2. **Execução**:
   - Lista de presença (todos assinaram?)
   - Material distribuído (slides, manual, certificado)
   - Data e local

3. **Avaliação de eficácia do treinamento**:
   - **Imediata**: Quiz pós-treinamento (mínimo 80% para aprovação)
   - **Follow-up**: Observação de campo (usuários estão aplicando o aprendizado?) após 30 dias
   - **Resultado**: Taxa de aprovação, feedback dos participantes

4. **Evidências**:
   - Certificados de conclusão (PDF assinado)
   - Lista de presença escaneada
   - Resultados de quiz (planilha)
   - Fotos da sessão de treinamento

5. **Retreinamento** (se necessário):
   - Se usuário reprova: Treinamento individual adicional
   - Se taxa de reprovação > 20%: Revisar conteúdo do treinamento (pode estar inadequado)

---

### 8.5. Com Desenvolvimento de Produto

**Quando CAPA resulta em mudança de design:**

Exemplo de causa raiz: "Algoritmo de ML não cobre edge case (pacientes pediátricos)"

**Ação requer mudança de design:**

1. **Seguir processo de Change Control** (se existir procedimento formal):
   - Solicitar mudança (Change Request)
   - Avaliar impacto (técnico, regulatório, cronograma, custo)
   - Aprovar mudança (comitê de mudanças)
   - Implementar mudança
   - Validar mudança

2. **Atualizar DHF (Design History File)**:
   - DHF é o conjunto de documentos que descreve o histórico de design do dispositivo
   - Adicionar: CAPA-2025-XXX como justificativa da mudança de design
   - Atualizar: Arquitetura de sistema, especificação de requisitos, documentos de verificação e validação

3. **Re-validação** (se mudança significativa):
   - Perguntas:
     - A mudança afeta segurança ou eficácia? → Re-validação clínica pode ser necessária
     - A mudança afeta requisitos críticos? → Re-executar testes de validação (TST-001)
     - A mudança requer submissão à ANVISA? → Avaliar conforme RDC 185/2001 (mudança significativa)

4. **Documentação atualizada**:
   - SRS (Software Requirements Specification)
   - SDD (Software Design Description)
   - TST (Test Specification)
   - Validação de Software (conforme IEC 62304)

---

## 9. DOCUMENTAÇÃO E RASTREABILIDADE

### 9.1. Sistema de Gestão de CAPAs

**Opções de sistema:**

**Opção 1: Simples (Excel/Google Sheets)** ✅ Recomendado para startups
- **Ferramenta**: Excel ou Google Sheets
- **Arquivo**: `CAPA_Register.xlsx`
- **Vantagens**: Baixo custo, fácil de usar, portável
- **Desvantagens**: Sem workflow automatizado, rastreabilidade manual

**Opção 2: Intermediário (Jira/Asana customizado)** ✅ Recomendado para empresas médias
- **Ferramenta**: Jira, Asana, Monday.com
- **Customização**: Criar projeto "CAPA" com campos personalizados
- **Vantagens**: Workflow automatizado, notificações, rastreabilidade automática, integração com desenvolvimento
- **Desvantagens**: Custo médio, necessidade de configuração inicial

**Opção 3: Avançado (Sistema QMS dedicado)** ✅ Recomendado para empresas estabelecidas
- **Ferramenta**: MasterControl, Veeva Vault QMS, Arena PLM, Greenlight Guru
- **Vantagens**: Compliant by design (ISO 13485, FDA 21 CFR Part 11), auditoria trail, assinatura eletrônica, integrações, relatórios automatizados
- **Desvantagens**: Custo alto (milhares de dólares/ano), curva de aprendizado

---

### 9.2. Campos Mínimos no CAPA Register

| Campo | Tipo | Obrigatório | Exemplo |
|-------|------|-------------|---------|
| **Número CAPA** | Texto | Sim | CAPA-2025-012 |
| **Data de Abertura** | Data | Sim | 15/10/2025 |
| **Tipo** | Lista (Corretiva/Preventiva) | Sim | Corretiva |
| **Fonte** | Lista | Sim | Incidente |
| **Link com Incidente** | Texto | Condicional | INC-2025-008 |
| **Descrição Breve** | Texto (50-100 chars) | Sim | Sistema aceita pacientes pediátricos sem validação |
| **Responsável** | Texto | Sim | João Silva (Dev Backend) |
| **Prioridade** | Lista (Crítica/Alta/Média/Baixa) | Sim | ALTA |
| **Status** | Lista | Sim | Em Implementação |
| **Prazo** | Data | Sim | 15/11/2025 |
| **Data de Fechamento** | Data | Condicional | 20/12/2025 |
| **Eficácia Verificada** | Sim/Não/Parcial | Condicional | Sim |
| **% Conclusão** | Número (0-100) | Sim | 80% |

**Exemplo de linha no CAPA Register (Excel):**

| CAPA | Data Abertura | Tipo | Fonte | Link INC | Descrição | Responsável | Prioridade | Status | Prazo | % Concl. | Eficácia |
|------|---------------|------|-------|----------|-----------|-------------|------------|--------|-------|----------|----------|
| CAPA-2025-012 | 15/10/2025 | Corretiva | Incidente | INC-2025-008 | Validação de idade pediátrica | João Silva | ALTA | Fechado | 15/11/2025 | 100% | Sim |
| CAPA-2025-013 | 20/10/2025 | Preventiva | Tendência | - | Otimização tempo de resposta | Maria Santos | MÉDIA | Em Verificação | 20/12/2025 | 90% | - |

---

### 9.3. Armazenamento de Evidências

**Estrutura de pastas recomendada:**

```
CAPAs/
├── 2025/
│   ├── CAPA-2025-001/
│   │   ├── 01_Abertura/
│   │   │   ├── FORM-003_CAPA-2025-001_v1.0.pdf (formulário inicial)
│   │   │   ├── Evidencia_Incidente_INC-2025-XXX.pdf
│   │   │   └── Aprovacao_Abertura_QA.pdf
│   │   ├── 02_Analise_Causa_Raiz/
│   │   │   ├── RCA_5_Whys.pdf
│   │   │   ├── RCA_Ishikawa.pdf
│   │   │   └── Aprovacao_RCA_QA.pdf
│   │   ├── 03_Planejamento/
│   │   │   ├── Plano_Acao_Detalhado.pdf
│   │   │   └── Aprovacoes/
│   │   │       ├── Aprovacao_QA.pdf
│   │   │       ├── Aprovacao_RT.pdf
│   │   │       └── Aprovacao_CEO.pdf (se aplicável)
│   │   ├── 04_Implementacao/
│   │   │   ├── Codigo_Corrigido/
│   │   │   │   ├── Pull_Request_#123.pdf
│   │   │   │   └── Code_Review.pdf
│   │   │   ├── Documentacao_Atualizada/
│   │   │   │   ├── IFU_v1.1.pdf
│   │   │   │   ├── TST-001_v1.2.pdf
│   │   │   │   └── Changelog.md
│   │   │   └── Treinamento/ (se aplicável)
│   │   │       ├── Lista_Presenca.pdf
│   │   │       ├── Certificados.pdf
│   │   │       └── Resultados_Quiz.xlsx
│   │   ├── 05_Verificacao_Eficacia/
│   │   │   ├── Logs_Monitoramento_60_dias.xlsx
│   │   │   ├── Relatorio_Verificacao_Eficacia.pdf
│   │   │   └── Aprovacao_Eficacia_QA.pdf
│   │   ├── 06_Revisao_Risco/
│   │   │   ├── RMP-001_v1.1.pdf (atualizado)
│   │   │   └── Analise_Impacto_Risco.pdf
│   │   ├── 07_Fechamento/
│   │   │   ├── FORM-003_CAPA-2025-001_FINAL.pdf (formulário completo com todas as assinaturas)
│   │   │   ├── Email_Comunicacao_Fechamento.pdf
│   │   │   └── Lessons_Learned.pdf (opcional)
│   │   └── README.md (sumário do CAPA: problema, causa raiz, ação, resultado)
│   │
│   ├── CAPA-2025-002/
│   │   └── ... (mesma estrutura)
│   │
│   └── ... (outros CAPAs de 2025)
│
└── 2024/
    └── ... (CAPAs do ano anterior)
```

**Benefícios desta estrutura:**
- ✅ Rastreabilidade: Todas as evidências em um único local
- ✅ Auditável: Auditores podem encontrar rapidamente todas as evidências
- ✅ Portável: Fácil de fazer backup e arquivar
- ✅ Escalável: Adicionar novos CAPAs sem bagunçar estrutura

---

### 9.4. Retenção de Documentos

**Requisitos regulatórios:**

| Regulamentação | Período de Retenção |
|----------------|---------------------|
| **ISO 13485:2016** | Mínimo **5 anos** após data de fabricação do último lote |
| **FDA 21 CFR Part 820.180** | Duração de vida útil do dispositivo + **2 anos** |
| **ANVISA RDC 16/2013** | Mínimo **5 anos** |

**Recomendação para HemoDoctor (SaMD):**
- **Período de retenção**: **5 anos** após fechamento do CAPA
- Justificativa: HemoDoctor é software (não tem lote físico), seguir mínimo regulatório de 5 anos

**Backup:**
- **Digital**: Backup semanal em servidor seguro (com controle de acesso)
- **Físico** (opcional): Backup anual em mídia física (HD externo) guardado em local seguro (cofre ignífugo)
- **Cloud**: Considerar backup em nuvem (AWS S3, Google Drive institucional com criptografia)

**Segurança:**
- ✅ Controle de acesso (apenas QA, RT, auditores têm acesso)
- ✅ Histórico de acesso (quem acessou quando?)
- ✅ Proteção contra alteração (PDFs com assinatura digital, arquivos em modo somente leitura)

---

## 10. REVISÃO GERENCIAL

### 10.1. Reuniões de CAPA

**A) Reunião Mensal - Operacional**

**Participantes:**
- Gerente de Qualidade (líder)
- Responsáveis de CAPAs abertas (cada um apresenta seu CAPA)
- RT (participa se CAPAs técnicos)

**Duração**: 1 hora

**Frequência**: Última sexta-feira de cada mês

**Agenda**:
1. **Status de cada CAPA em aberto** (10 min cada):
   - Progresso desde última reunião
   - % conclusão atual
   - Próximos passos
   - Prazo ainda é realista?

2. **Bloqueios e necessidade de suporte** (15 min):
   - Quais CAPAs estão travados?
   - O que está impedindo progresso?
   - Como QA ou RT podem ajudar?

3. **CAPAs próximas do prazo** (alerta) (10 min):
   - Quais CAPAs estão em 80% do SLA?
   - Plano de ação para evitar vencimento

4. **CAPAs a serem abertos** (triagem) (10 min):
   - Novos problemas identificados esta semana
   - Decisão: Abrir CAPA ou ação pontual?
   - Priorização

5. **KPIs do mês** (5 min):
   - Revisar dashboard de CAPA
   - Backlog, taxa de abertura, tempo médio de fechamento

**Ata da reunião**: Documentar decisões e ações (template simples):
```markdown
# Reunião Mensal de CAPA - Outubro 2025
**Data**: 27/10/2025
**Participantes**: [Lista]

## CAPAs Revisados
- **CAPA-2025-012**: 90% concluído, falta verificação de eficácia (previsto 15/11)
- **CAPA-2025-015**: 50% concluído, bloqueio: aguardando aprovação do CEO para alocação de recurso

## Decisões
- CAPA-2025-015: QA vai escalar ao CEO ainda hoje
- Novo CAPA a ser aberto: Otimização de tempo de resposta (tendência identificada)

## Ações
- [João]: Finalizar implementação CAPA-2025-012 até 05/11
- [QA]: Escalar CAPA-2025-015 ao CEO
- [Maria]: Abrir CAPA-2025-020 (otimização) até 30/10
```

---

**B) Reunião Trimestral - Análise de Tendências**

**Participantes:**
- Gerente de Qualidade (apresenta)
- RT
- CEO
- Gerentes de Desenvolvimento, Operações, Suporte Clínico

**Duração**: 2 horas

**Frequência**: Último dia útil do trimestre (Mar, Jun, Set, Dez)

**Agenda**:
1. **KPIs do trimestre vs meta** (30 min):
   - Apresentar gráficos e tabelas
   - Comparar com trimestre anterior
   - Tendências: Melhorando ou piorando?

2. **Análise de tendências** (30 min):
   - Áreas com mais CAPAs (hot spots)
   - Causas raízes recorrentes
   - Tipos de falha mais comuns (bug/dados/uso/design/infra)

3. **Ações preventivas sistêmicas** (30 min):
   - O que fazer para reduzir CAPAs futuros?
   - Exemplo: "40% dos CAPAs são gaps de teste → Ação: Contratar QA Engineer adicional"
   - Definir plano de ação preventiva com responsável e prazo

4. **Budget para próximo trimestre** (15 min):
   - Recursos necessários para fechar CAPAs em aberto
   - Investimentos em qualidade (ferramentas, treinamento, contratação)

5. **Lições aprendidas** (15 min):
   - O que aprendemos com CAPAs do trimestre?
   - Boas práticas identificadas
   - Processo de CAPA está funcionando? Precisa de ajustes?

**Relatório trimestral**: Ver seção 7.4 (template de relatório)

---

**C) Reunião Anual - Análise Crítica da Direção (ISO 13485 Cláusula 5.6)**

**Participantes:**
- Direção (CEO, CTO)
- Gerentes (Qualidade, Desenvolvimento, Operações, Comercial)
- RT
- Representante de clientes (se possível)

**Duração**: 4 horas

**Frequência**: Anual (sugerido: Janeiro, para revisar ano anterior e planejar ano seguinte)

**Agenda (conforme ISO 13485:2016 §5.6)**:

1. **Resultados de auditorias** (30 min):
   - Auditorias internas e externas do ano
   - Não-conformidades encontradas
   - Status de CAPAs relacionados

2. **Feedback de clientes** (30 min):
   - Reclamações recebidas
   - Satisfação do cliente (pesquisa NPS)
   - Sugestões de melhoria

3. **Desempenho de processos** (30 min):
   - KPIs de qualidade (incluindo CAPA)
   - Eficácia do SGQ (Sistema de Gestão da Qualidade)

4. **Conformidade do produto** (30 min):
   - HemoDoctor está atendendo requisitos?
   - Mudanças regulatórias (novas normas ANVISA, FDA, ISO)

5. **Ações de acompanhamento** (30 min):
   - Status de ações da análise crítica anterior
   - CAPAs críticos do ano

6. **Mudanças externas e internas** (20 min):
   - Mudanças de legislação
   - Mudanças de mercado
   - Mudanças organizacionais (nova equipe, nova estratégia)

7. **Resumo anual de CAPAs** (40 min):
   - Total de CAPAs (abertas/fechadas)
   - Taxa de eficácia
   - Taxa de recorrência
   - Análise: Sistema de CAPA está funcionando?
   - Investimentos necessários

8. **Metas para próximo ano** (30 min):
   - KPIs de qualidade para 2026
   - Investimentos em qualidade (budget)
   - Melhorias no processo de CAPA

9. **Aprovação de mudanças** (20 min):
   - Mudanças no processo de CAPA (se propostas)
   - Novos procedimentos de qualidade

**Ata da Análise Crítica da Direção**: Documento formal, assinado pela Direção, arquivado por 5 anos.

---

### 10.2. Dashboards de CAPA

**A) Dashboard Semanal** (para Gerente de QA)

Atualização: Segunda-feira de manhã (início da semana)

**Visualizações:**
- ✅ CAPAs **abertas esta semana** (lista)
- ✅ CAPAs **fechadas esta semana** (lista)
- 🚨 CAPAs com **prazo vencido** (lista em vermelho)
- ⚠️ CAPAs **próximas do prazo** (15 dias) (lista em amarelo)
- 📊 **Backlog total** (número)

**Exemplo**:
```
Dashboard Semanal de CAPA - Semana de 14 a 20 de Outubro de 2025

✅ Abertas esta semana: 2
- CAPA-2025-019: Atualização de IFU (Prioridade MÉDIA)
- CAPA-2025-020: Otimização de tempo de resposta (Prioridade BAIXA)

✅ Fechadas esta semana: 1
- CAPA-2025-012: Validação de idade pediátrica (Eficaz ✅)

🚨 Prazo vencido: 0

⚠️ Próximas do prazo (15 dias): 1
- CAPA-2025-015: Bug de crash (Prazo: 05/11/2025 - faltam 12 dias)

📊 Backlog total: 8 CAPAs em aberto
```

**Ação**: Se prazo vencido ou backlog > 10 → Reunião de emergência.

---

**B) Dashboard Mensal** (para Direção)

Atualização: Primeiro dia útil do mês (revisar mês anterior)

**Visualizações:**

1. **Total de CAPAs por status** (gráfico de barras horizontal):
   - Aberta | Em Análise | Aprovada | Em Implementação | Em Verificação | Fechada

2. **Tempo médio de fechamento vs meta** (gráfico de linha):
   - Meta: 90 dias (linha vermelha horizontal)
   - Real: Linha azul com valores mensais dos últimos 12 meses

3. **Taxa de eficácia** (gauge/velocímetro):
   - Meta: > 95%
   - Real: Percentual verde (se > 95%), amarelo (80-95%), vermelho (< 80%)

4. **Distribuição por fonte** (gráfico de pizza):
   - Incidente (40%)
   - Auditoria (20%)
   - Reclamação (15%)
   - Near Miss (10%)
   - Tendência (10%)
   - Outro (5%)

5. **Distribuição por prioridade** (gráfico de barras vertical):
   - CRÍTICA: 2
   - ALTA: 5
   - MÉDIA: 8
   - BAIXA: 3

6. **Tendência 12 meses** (gráfico de linha dupla):
   - Linha azul: CAPAs abertas por mês
   - Linha verde: CAPAs fechadas por mês
   - Linha vermelha: Backlog no final do mês
   - Eixo X: Jan, Fev, Mar, ..., Dez
   - Eixo Y: Número de CAPAs

7. **Top 5 responsáveis** (gráfico de barras horizontal):
   - João Silva: 5 CAPAs
   - Maria Santos: 3 CAPAs
   - Pedro Costa: 2 CAPAs
   - Ana Rocha: 2 CAPAs
   - Carlos Dias: 1 CAPA

**Ferramenta**: Excel com gráficos dinâmicos, Power BI, Tableau, ou Google Data Studio.

---

## 11. EXEMPLOS PRÁTICOS DE CAPA EM HEALTHCARE E MEDICAL DEVICES

### Exemplo 1: CAPA Corretivo - Sugestão Diagnóstica Incorreta (CRÍTICO)

**Problema**:
- Incidente INC-2025-008: HemoDoctor sugeriu Leucemia Mieloide Aguda (LMA) para paciente pediátrico (2 anos). Médico seguiu sugestão, mas exames subsequentes confirmaram condição benigna (infecção viral). Paciente foi submetido a punção de medula óssea desnecessária.

**CAPA-2025-012**:
- **Tipo**: Corretiva
- **Prioridade**: CRÍTICA (risco à segurança do paciente)
- **Causa Raiz** (5 Whys): Requisito REQ-FUNC-015 (validação de idade pediátrica) não foi implementado. Gap de teste (TST-001 não cobria pediatria).
- **Ação**: Implementar validação de idade pediátrica (bloqueia input se < 18 anos) + atualizar IFU + adicionar teste TST-015
- **Prazo**: 30 dias
- **Eficácia**: 100% (0 incidentes em 60 dias, 100% testes passaram)
- **Impacto**: Risco RMP-001-R12 reduzido de RPN 12 → 4
- **Status**: Fechado - Eficaz ✅

---

### Exemplo 2: CAPA Corretivo - Bug de Crash (ALTA)

**Problema**:
- Reclamações recorrentes: 5 médicos relataram crash do sistema ao carregar pacientes com histórico extenso (> 100 exames de CBC). Sistema fica indisponível por 2-3 minutos.

**CAPA-2025-015**:
- **Tipo**: Corretiva
- **Prioridade**: ALTA (não afeta segurança diretamente, mas indisponibilidade do sistema é crítica)
- **Causa Raiz** (Ishikawa): Bug de software (memória insuficiente alocada para carregar histórico). Método inadequado (carregamento síncrono de todos os dados).
- **Ação**: Refatorar módulo de histórico (carregar dados de forma paginada, lazy loading) + aumentar heap memory de 2GB para 4GB
- **Prazo**: 60 dias
- **Eficácia**: 100% (0 crashes em 30 dias, tempo de carregamento reduzido de 120s para 5s)
- **Status**: Fechado - Eficaz ✅

---

### Exemplo 3: CAPA Preventivo - Análise de Tendências (MÉDIA)

**Problema**:
- Dashboard de monitoramento mostra aumento gradual de tempo de resposta do HemoDoctor: De 2s (média em janeiro) para 5s (média em setembro). Ainda dentro do aceitável (< 10s), mas tendência preocupante.

**CAPA-2025-020**:
- **Tipo**: Preventiva (problema ainda não causou impacto, mas tendência é negativa)
- **Prioridade**: MÉDIA
- **Causa Raiz** (Análise de Dados): Banco de dados cresceu 10x em 9 meses (de 10k para 100k registros). Queries não estão otimizadas (falta de índices).
- **Ação**: Adicionar índices no banco de dados (PostgreSQL) + otimizar queries mais lentas (identificadas via profiling) + implementar caching (Redis)
- **Prazo**: 90 dias
- **Eficácia**: 95% (tempo de resposta p99 caiu para 2.1s, mantido por 60 dias)
- **Status**: Fechado - Eficaz ✅

---

### Exemplo 4: CAPA Corretivo - Auditoria ISO (ALTA)

**Problema**:
- Auditoria externa ISO 13485: Não-conformidade MAIOR encontrada: "15 testes especificados em TST-001 não foram executados antes do release v2.3.0"

**CAPA-2025-018**:
- **Tipo**: Corretiva
- **Prioridade**: ALTA (não-conformidade regulatória)
- **Causa Raiz** (5 Whys): Processo de release não incluía checklist de QA. Testes foram especificados mas não rastreados. QA Engineer assumiu que dev team executou, mas não havia evidência.
- **Ação**:
  1. Executar os 15 testes faltantes (retroativo para v2.3.0)
  2. Criar checklist de QA obrigatório para todo release (template)
  3. Implementar gate de aprovação no CI/CD: Release só pode ser deployado se QA Engineer assinou checklist
  4. Treinamento de dev team: Importância de rastreabilidade de testes
- **Prazo**: 60 dias
- **Eficácia**: 100% (auditoria de follow-up: 0 não-conformidades, checklist está sendo usado em 100% dos releases)
- **Status**: Fechado - Eficaz ✅

---

### Exemplo 5: CAPA Corretivo - Reclamação de Uso (MÉDIA)

**Problema**:
- 3 médicos diferentes relataram: "Não entendo o que significa 'confidence score 0.73'. Devo confiar na sugestão ou não?"

**CAPA-2025-013**:
- **Tipo**: Corretiva
- **Prioridade**: MÉDIA (problema de usabilidade, não afeta segurança diretamente mas pode levar a má interpretação)
- **Causa Raiz** (Ishikawa - Mão de obra + Método): IFU não explica claramente o conceito de confidence score. Interface não fornece interpretação contextual.
- **Ação**:
  1. Atualizar IFU seção "Interpretação de Resultados": Adicionar explicação detalhada de confidence score com exemplos práticos
  2. Melhorar UX: Adicionar tooltip na interface: "Confidence score > 0.8 = alta confiança, 0.6-0.8 = confiança moderada, < 0.6 = baixa confiança (considere segunda opinião)"
  3. Adicionar alerta visual: Se confidence < 0.6 → banner amarelo: "⚠️ Sugestão com baixa confiança. Recomendamos avaliação adicional por especialista."
  4. Treinamento presencial com médicos (2h): Como interpretar resultados do HemoDoctor
- **Prazo**: 90 dias
- **Eficácia**: 100% (0 reclamações sobre interpretação em 90 dias, 100% dos médicos treinados aprovados em quiz)
- **Status**: Fechado - Eficaz ✅

---

## 12. REFERÊNCIAS REGULATÓRIAS

Este procedimento está em conformidade com:

**Normas Internacionais:**
- **ISO 13485:2016** - Medical devices - Quality management systems - Requirements for regulatory purposes
  - Cláusula 8.5.2: Ação Corretiva
  - Cláusula 8.5.3: Ação Preventiva

- **ISO 14971:2019** - Medical devices - Application of risk management to medical devices

- **21 CFR Part 820.100 (FDA)** - Quality System Regulation - Corrective and Preventive Action

**Regulamentação Nacional (Brasil):**
- **ANVISA RDC 16/2013** - Boas Práticas de Fabricação de Produtos Médicos
- **ANVISA RDC 67/2009** - Tecnovigilância
- **ANVISA RDC 185/2001** - Registro de Produtos Médicos

**Guias de Boas Práticas:**
- FDA Guidance: "Quality System Information for Certain Premarket Application Reviews" (2003)
- ISO TR 24971:2020: Guidance on the application of ISO 14971

---

## 13. GLOSSÁRIO

- **CAPA**: Corrective and Preventive Actions (Ações Corretivas e Preventivas)
- **DHF**: Design History File (Arquivo Histórico de Design)
- **FSCA**: Field Safety Corrective Action (Ação Corretiva de Segurança em Campo)
- **IFU**: Instructions for Use (Instruções de Uso)
- **KPI**: Key Performance Indicator (Indicador Chave de Performance)
- **NC**: Não-conformidade
- **QA**: Quality Assurance (Garantia de Qualidade)
- **QMS**: Quality Management System (Sistema de Gestão da Qualidade)
- **RCA**: Root Cause Analysis (Análise de Causa Raiz)
- **RMP**: Risk Management Plan (Plano de Gestão de Riscos)
- **RPN**: Risk Priority Number (Número de Prioridade de Risco) = Severidade × Probabilidade × Detectabilidade
- **RT**: Responsável Técnico
- **SLA**: Service Level Agreement (Acordo de Nível de Serviço)
- **SMART**: Specific, Measurable, Achievable, Relevant, Time-bound (critérios para definir ações)
- **SOP**: Standard Operating Procedure (Procedimento Operacional Padrão)
- **SRS**: Software Requirements Specification (Especificação de Requisitos de Software)
- **TST**: Test Specification (Especificação de Testes)

---

## 14. REVISÕES E ATUALIZAÇÕES DESTE PROCEDIMENTO

Este procedimento deve ser revisado:
- **Anualmente** (mínimo) na Análise Crítica da Direção
- Após mudanças regulatórias (novas normas ISO, ANVISA, FDA)
- Após auditoria externa (se auditor recomendar mudanças)
- Se eficácia do processo de CAPA estiver abaixo da meta (< 95%)

**Histórico de Revisões:**

| Versão | Data | Mudanças | Autor |
|--------|------|----------|-------|
| 1.0 | 12/10/2025 | Versão inicial do procedimento CAPA | Quality Systems Specialist |

---

## 15. APROVAÇÕES

Este procedimento foi revisado e aprovado por:

**Gerente de Qualidade:**
- Nome: _______________________________
- Assinatura: ___________________________
- Data: ___/___/______

**Responsável Técnico:**
- Nome: _______________________________
- Assinatura: ___________________________
- Data: ___/___/______

**CEO (aprovação final):**
- Nome: _______________________________
- Assinatura: ___________________________
- Data: ___/___/______

---

**FIM DO PROC-003**

---

*Este documento é parte integrante do Sistema de Gestão da Qualidade do HemoDoctor e está sujeito a controle de revisão conforme procedimento de Controle de Documentos.*

*Documento controlado. Cópias impressas não são controladas e devem ser verificadas antes do uso.*
