---
document_id: "PROC-002"
title: "Procedimento de Investigação de Eventos Adversos"
version: "1.0"
status: "OFICIAL"
date: "2025-10-12"
author: "Risk Management Specialist"
organization: "HemoDoctor"
classification: "Dispositivo Médico - Classe II"
compliance:
  - "ISO 13485:2016 (§8.5)"
  - "ISO 14971:2019"
  - "ANVISA RDC 67/2009"
history:
  - version: "1.0"
    date: "2025-10-12"
    changes: "Versão inicial do procedimento de investigação RCA"
    author: "Risk Management Specialist"
---

# PROC-002: Procedimento de Investigação de Eventos Adversos

## 1. OBJETIVO

Este procedimento estabelece um processo sistemático para:

- **Investigar causa raiz** de incidentes relatados via PROC-001 (Procedimento de Relato de Incidentes e Tecnovigilância)
- **Prevenir recorrência** através de ações baseadas em evidências e análise técnico-científica
- **Cumprir requisitos regulatórios** estabelecidos pela ANVISA (RDC 67/2009) e normas internacionais ISO 13485:2016 e ISO 14971:2019
- **Garantir segurança do paciente** por meio de investigação rigorosa e ações eficazes

## 2. ESCOPO

### 2.1. Aplicabilidade

Este procedimento aplica-se a:

- **Todos os incidentes** relatados via PROC-001 envolvendo o dispositivo médico HemoDoctor
- **Queixas técnicas** reportadas por usuários finais (médicos, enfermeiros, técnicos de laboratório)
- **Near misses** com potencial de dano ao paciente
- **Não-conformidades** identificadas em auditorias internas ou externas relacionadas ao desempenho clínico do sistema

### 2.2. Priorização por Severidade

A investigação será iniciada conforme cronograma baseado na classificação de severidade:

| Severidade | Prazo de Início | Prazo de Conclusão | Responsável |
|------------|-----------------|-----------------------|-------------|
| **GRAVE** | 24 horas | 30 dias | Risk Manager + RT |
| **NÃO GRAVE** | 7 dias úteis | 60 dias | Risk Manager |

**Definições** (conforme PROC-001):
- **GRAVE**: Morte, ameaça à vida, lesão grave/incapacidade permanente, necessidade de intervenção médica para prevenir dano
- **NÃO GRAVE**: Mau funcionamento sem dano ao paciente, queixa técnica, sugestão incorreta sem seguimento pelo médico

---

## 3. METODOLOGIA DE INVESTIGAÇÃO

A investigação seguirá uma abordagem estruturada em **3 fases**, com duração típica de **30 dias** (incidentes GRAVES) ou **60 dias** (NÃO GRAVES).

### 3.1. FASE 1: Coleta de Evidências (0-7 dias)

#### 3.1.1. Evidências Técnicas

Coletar **todas** as seguintes informações do sistema HemoDoctor:

**Logs de Sistema:**
- Timestamp completo (data, hora, timezone) de cada evento
- User ID e sessão (identificador único do usuário)
- Ações executadas (login, input de CBC, visualização de resultado, logout)
- Dados de entrada (CBC completo: WBC, RBC, Hgb, Hct, MCV, MCH, MCHC, RDW, Plaquetas, diferencial leucocitário)
- Output do sistema (sugestão diagnóstica, nível de confiança/confidence score, alertas gerados)
- Erros ou warnings registrados
- Tempo de resposta do sistema (latência)

**Ambiente Técnico:**
- Versão do software HemoDoctor (ex: v1.2.3)
- Versão do modelo HemoAI (ex: model_v4.5_20250901)
- Browser/Aplicativo (tipo, versão, sistema operacional)
- Dispositivo (desktop, tablet, mobile)
- Rede (velocidade, latência, tipo de conexão)
- Integração com LIS (Laboratory Information System), se aplicável

**Dados Completos:**
- Screenshot ou print da tela no momento do incidente
- Histórico de versões de software (confirmar versão exata usada)
- Comparação com versões anteriores (se bug reportado, quando foi introduzido?)

#### 3.1.2. Evidências Clínicas

Coletar **com consentimento apropriado** e seguindo **LGPD/regulamentação ética**:

**Entrevista Estruturada com Usuário:**
- Médico ou profissional de saúde que utilizou o sistema
- Questionário padronizado (ver Anexo A):
  - O que você esperava que o sistema fizesse?
  - O que o sistema realmente fez?
  - Qual ação você tomou com base na sugestão do sistema?
  - Você percebeu algum problema no momento do uso?
  - Qual foi o desfecho clínico final?

**Entrevista com Paciente (se aplicável):**
- Somente se consentimento informado obtido
- Foco em: sintomas apresentados, evolução clínica, impacto percebido

**Prontuário Médico Relevante:**
- Diagnóstico final confirmado (padrão-ouro: biópsia, citometria de fluxo, etc.)
- Exames complementares realizados (mielograma, imunofenotipagem, citogenética, molecular)
- Tratamento instituído
- Evolução clínica (melhora, piora, óbito)

**Contexto Clínico:**
- Urgência do caso (emergência, eletivo)
- Comorbidades do paciente
- Tratamento prévio (quimioterapia, radioterapia, uso de medicamentos que alteram CBC)
- Idade, sexo, etnia (podem influenciar ranges de normalidade)

#### 3.1.3. Preservação de Evidências

- **Backup imediato** de todos os logs e dados (antes que sejam sobrescritos)
- **Cadeia de custódia**: Registrar quem coletou, quando, e onde está armazenado
- **Cópia forense** do banco de dados (se necessário)
- **Armazenamento seguro**: Pasta dedicada ao incidente (estrutura: `INC-YYYY-XXX/Evidencias/`)

### 3.2. FASE 2: Reconstrução do Incidente (7-14 dias)

#### 3.2.1. Criar Timeline Detalhado

Reconstruir a sequência exata de eventos usando uma tabela estruturada:

| Timestamp | Evento | Ator | Sistema/Módulo | Dados Associados | Observações |
|-----------|--------|------|----------------|------------------|-------------|
| 2025-03-15 10:15:32 | Login no sistema | Dr. Maria Silva | HemoDoctor Web | User ID: 1234 | Sucesso |
| 2025-03-15 10:16:05 | CBC inserido | Dr. Maria Silva | Ingestion Service | Paciente: Pediátrico, 2 anos, sexo M | WBC: 45.000, Blastos: 60% |
| 2025-03-15 10:16:08 | Validação de entrada | Sistema | Validation Service | CBC válido (ranges adultos) | ⚠️ Idade NÃO validada |
| 2025-03-15 10:16:12 | Início de inferência | Sistema | HemoAI Engine | Processando com model_v4.5 | - |
| 2025-03-15 10:16:15 | Resultado gerado | Sistema | HemoAI Engine | Sugestão: LMA (Leucemia Mieloide Aguda) | Confidence: 78% |
| 2025-03-15 10:16:20 | Visualização de resultado | Dr. Maria Silva | UI Frontend | Tela de resultado exibida | Usuário visualizou sugestão |
| 2025-03-15 10:17:00 | Decisão clínica | Dr. Maria Silva | - | Médico seguiu sugestão: LMA | Iniciou investigação para LMA |
| 2025-03-15 12:30:00 | Diagnóstico final | Laboratório | - | Biópsia + Citometria | **Diagnóstico real: LLA (Leucemia Linfoide Aguda)** |
| 2025-03-15 14:00:00 | Correção de conduta | Dr. Maria Silva | - | Tratamento alterado para LLA | Atraso de 2h na conduta correta |

**Análise do Timeline:**
- **Ponto crítico identificado**: 10:16:08 - Validação NÃO detectou que paciente era pediátrico (2 anos)
- **Consequência**: Modelo treinado com dados adultos classificou incorretamente
- **Impacto**: Sugestão de LMA ao invés de LLA (leucemias com protocolos de tratamento diferentes)

#### 3.2.2. Perguntas 5W2H

Aplicar metodologia jornalística para garantir completude da investigação:

**1. What (O que aconteceu?)**
- Descrição objetiva: Sistema sugeriu diagnóstico de LMA, mas diagnóstico correto era LLA

**2. When (Quando ocorreu?)**
- Data/hora precisa: 15/03/2025 às 10:16:15
- Contexto temporal: Durante expediente normal, não era emergência

**3. Where (Onde ocorreu?)**
- Módulo específico: HemoAI Engine → Inferência do modelo de Machine Learning
- Tela: Tela de resultado diagnóstico (UI Frontend)
- Local físico: Hospital Infantil X, Unidade de Hematologia Pediátrica

**4. Who (Quem esteve envolvido?)**
- Usuário: Dr. Maria Silva (Hematologista Pediátrica, 10 anos de experiência)
- Paciente: Criança de 2 anos (iniciais: R.S.)
- Software: HemoDoctor v1.2.3 com modelo HemoAI v4.5
- Equipe técnica: Time de desenvolvimento HemoDoctor

**5. Why (Por que ocorreu?)**
- Causa imediata: Modelo classificou incorretamente LLA como LMA
- Causa raiz: **A ser determinada na Fase 3** (análise de causa raiz)

**6. How (Como foi detectado?)**
- Detecção: Exames complementares (biópsia + citometria de fluxo) revelaram diagnóstico correto
- Relato: Dr. Maria Silva reportou discrepância via FORM-001

**7. How much (Qual foi o impacto?)**
- Gravidade: **GRAVE** (atraso de 2h na conduta, mas sem dano permanente ao paciente)
- Extensão: 1 paciente afetado (incidente isolado ou recorrente? → investigar)
- Custo: Exames adicionais, tempo de equipe, risco de dano maior

### 3.3. FASE 3: Análise de Causa Raiz (14-30 dias)

Esta é a fase **mais crítica** da investigação. A identificação correta da causa raiz determina a eficácia das ações corretivas.

#### 3.3.1. Metodologia A: 5 Whys (Método Toyota)

Aplicar **5 perguntas sucessivas** "Por quê?" até chegar à causa raiz:

**Pergunta Inicial**: Por que o incidente ocorreu?

**Exemplo prático (caso LMA vs LLA pediátrico):**

- **Why 1**: Por que a sugestão foi incorreta?
  - **Resposta**: Porque o modelo HemoAI classificou erroneamente LLA como LMA

- **Why 2**: Por que o modelo classificou erroneamente?
  - **Resposta**: Porque os valores de CBC estavam fora do range de treinamento do modelo

- **Why 3**: Por que os valores estavam fora do range de treinamento?
  - **Resposta**: Porque o paciente era pediátrico (2 anos) e os ranges pediátricos são significativamente diferentes dos adultos (ex: leucócitos normais em criança podem ser 5.000-15.000, vs 4.000-10.000 em adultos)

- **Why 4**: Por que o sistema não detectou que o paciente era pediátrico?
  - **Resposta**: Porque a validação de idade não estava implementada no Validation Service

- **Why 5**: Por que a validação de idade não estava implementada?
  - **Resposta**: **CAUSA RAIZ IDENTIFICADA**:
    - O requisito de validação de idade pediátrica (REQ-FUNC-015) estava documentado no SRS-001
    - Porém, **não foi adequadamente coberto nos testes de sistema** (gap no plano de testes TST-001)
    - A funcionalidade foi desenvolvida parcialmente mas não validada em casos edge (pacientes < 5 anos)
    - Nenhum teste de aceitação verificou especificamente esta condição

**Critério de Parada**:
- A causa raiz é ESPECÍFICA (não vaga como "erro humano" ou "falha de software")
- A causa raiz é ACIONÁVEL (pode ser corrigida com ação concreta)
- A causa raiz é VERIFICÁVEL (pode ser testada após correção)

#### 3.3.2. Metodologia B: Ishikawa (Espinha de Peixe / Diagrama de Causa e Efeito)

Analisar o problema sob **6 categorias (6M)**:

```
                                    PROBLEMA
                                       │
                     ┌─────────────────┼─────────────────┐
                     │                 │                 │
                 MÉTODO            MÁQUINA         MATERIAL
              (Processo)         (Hardware)         (Dados)
                     │                 │                 │
        ┌────────────┼─────────┬──────┼──────┬──────────┼────────┐
        │            │         │      │      │          │        │
    Algoritmo    Validação  GPU?  Timeout?  CBC    Range    Idade
      ML         falhou              rede   correto? válido? detectada?
```

**Análise detalhada por categoria:**

**1. MÉTODO (Processo, Algoritmo)**
- Algoritmo de ML inadequado para casos edge (população pediátrica)?
  - ✓ **SIM**: Modelo treinado majoritariamente com dados adultos
- Processo de validação de entrada falhou?
  - ✓ **SIM**: Validação não verificou idade do paciente

**2. MÁQUINA (Hardware, Infraestrutura)**
- Timeout de rede causou dados incompletos?
  - ✗ NÃO: Logs mostram latência normal (120ms)
- GPU não processou corretamente?
  - ✗ NÃO: Inferência completou com sucesso (tempo: 3.2s)
- Problema de memória?
  - ✗ NÃO: Uso de RAM e GPU dentro do normal

**3. MATERIAL (Dados, Entrada)**
- Dados de CBC incorretos na origem (erro de digitação)?
  - ✗ NÃO: Valores conferidos, CBC correto para LLA pediátrica
- Dados fora do range esperado pelo modelo?
  - ✓ **SIM**: WBC 45.000 com 60% blastos é valor extremo, comum em LLA pediátrica mas raro em adultos
- Dados de idade do paciente foram fornecidos?
  - ✓ **SIM**: Campo idade preenchido corretamente (2 anos)

**4. MÃO DE OBRA (Treinamento, Erro Humano)**
- Usuário não foi treinado adequadamente?
  - ✗ NÃO: Dr. Maria Silva é hematologista experiente, com treinamento certificado em HemoDoctor
- Interpretação errada da sugestão?
  - ✗ NÃO: Médica entendeu corretamente a sugestão, mas confiou no sistema
- Falta de análise crítica do resultado?
  - ⚠️ PARCIAL: Médica poderia ter questionado mais, mas sistema não alertou sobre limitação para pediatria

**5. MEDIDA (Métricas, Monitoramento)**
- Sistema de alerta não acionou?
  - ✓ **SIM**: Não existe alerta automático para "paciente pediátrico com modelo treinado para adultos"
- Confidence score foi exibido?
  - ✓ SIM (78%), mas usuário não foi treinado sobre interpretação de scores baixos vs altos
- Métricas de performance do modelo para pediatria?
  - ✓ **NÃO EXISTEM**: Modelo nunca foi validado especificamente em população pediátrica

**6. MEIO AMBIENTE (Contexto Clínico, Organizacional)**
- Urgência clínica prejudicou análise crítica?
  - ✗ NÃO: Caso eletivo, sem pressão de tempo
- Falta de segunda opinião?
  - ✗ NÃO APLICÁVEL: Hospital tem protocolo de discussão de casos, mas apenas após resultado do sistema
- Cultura organizacional de "confiar no sistema"?
  - ⚠️ POSSÍVEL: Pode ter contribuído, mas não é causa raiz

**Consolidação Ishikawa:**
- **Causas principais identificadas**: Método (validação falhou) + Material (dados fora do range) + Medida (alertas ausentes)
- **Causa raiz convergente**: Ausência de validação de idade pediátrica + Modelo não validado para população pediátrica

#### 3.3.3. Metodologia C: Análise de Modo de Falha

Identificar o **tipo de falha** e a **ação apropriada**:

| Tipo de Falha | Descrição | Este caso? | Ação Apropriada |
|---------------|-----------|------------|-----------------|
| **Bug de Software** | Erro de código (crash, null pointer, loop infinito) | ❌ NÃO | Corrigir código |
| **Dados Incorretos** | Entrada inválida ou fora do esperado | ✅ **PARCIAL** | Melhorar validação de entrada |
| **Uso Inadequado** | Erro do usuário, má interpretação | ❌ NÃO | Treinar usuário, melhorar UX |
| **Limitação de Design** | Sistema funciona como projetado, mas resultado inadequado | ✅ **SIM** | Redesign ou documentar limitação |
| **Infraestrutura** | Problema de ambiente (rede, servidor) | ❌ NÃO | Melhorar infraestrutura |

**Conclusão da Análise de Modo de Falha:**
- **Tipo identificado**: **Limitação de Design** + **Dados Fora do Range**
- O sistema funcionou "como projetado" (processou os dados e gerou uma sugestão)
- Porém, o design **não contemplava** casos pediátricos adequadamente
- A validação de entrada **não cobria** verificação de adequação do modelo para a população

---

## 4. AVALIAÇÃO DE IMPACTO

A avaliação de impacto deve considerar **3 dimensões**:

### 4.1. Impacto no Paciente

**Perguntas obrigatórias:**

1. **Houve dano real ao paciente?**
   - ☐ Não (near miss)
   - ☑ Sim (especificar abaixo)

2. **Gravidade do dano:**
   - ☐ Leve (desconforto temporário, exames adicionais)
   - ☑ Moderado (atraso no tratamento correto, mas sem sequela permanente)
   - ☐ Grave (sequela permanente, internação prolongada)
   - ☐ Fatal (óbito relacionado)

3. **Necessidade de follow-up médico adicional?**
   - ☑ Sim: Exames complementares urgentes (biópsia, citometria)
   - Atraso de 2h na conduta correta (tempo perdido investigando LMA ao invés de LLA)

4. **Dano é reversível?**
   - ☑ Sim: Conduta foi corrigida a tempo, paciente iniciou protocolo adequado de LLA
   - Prognóstico não foi significativamente afetado (detectado precocemente)

**Classificação Final de Impacto no Paciente:** MODERADO

### 4.2. Impacto no Sistema

**Perguntas obrigatórias:**

1. **Quantos usuários/pacientes potencialmente afetados?**
   - Análise de banco de dados (últimos 6 meses):
     - Total de pacientes pediátricos (< 18 anos) processados: **87 pacientes**
     - Total de pacientes < 5 anos: **12 pacientes**
     - Casos similares (LLA vs LMA pediátrico): **3 casos identificados** (requer investigação retroativa!)
   - **Estimativa**: 10-100 usuários potencialmente afetados (MÉDIO)

2. **Frequência do problema:**
   - ☐ Isolado (caso único)
   - ☑ Raro (< 5% dos casos similares)
   - ☐ Recorrente (5-20% dos casos)
   - ☐ Sistemático (> 20% dos casos)

3. **Risco de recorrência sem ação corretiva:**
   - ☐ Baixo (improvável repetir)
   - ☐ Médio (pode repetir em condições específicas)
   - ☑ Alto (provavelmente repetirá em casos similares)
   - ☐ Crítico (certamente repetirá)

4. **Módulos/funcionalidades afetados:**
   - Validation Service (validação de entrada)
   - HemoAI Engine (modelo de inferência)
   - UI Frontend (exibição de alertas)
   - IFU (Instruções de Uso - seção "Limitações" incompleta)

**Classificação Final de Impacto no Sistema:** ALTO

### 4.3. Impacto Regulatório

**Perguntas obrigatórias:**

1. **Requer notificação ANVISA? (conforme PROC-001)**
   - ☑ Sim: Evento classificado como GRAVE (atraso no tratamento, risco de dano)
   - Prazo: 10 dias úteis (conforme RDC 67/2009)
   - Usar FORM-004 (Notificação ANVISA)

2. **Impacto em certificações?**
   - ISO 13485: ☑ SIM (não-conformidade em validação de design e controle de processos)
   - ISO 14971: ☑ SIM (risco não adequadamente controlado)
   - ISO 27001: ☐ NÃO (não há impacto em segurança da informação)

3. **Risco de recall ou Field Safety Corrective Action (FSCA)?**
   - ☑ Possível: Se ANVISA determinar que risco é inaceitável
   - Ação proativa recomendada:
     - Emitir Field Safety Notice (FSN) aos usuários
     - Limitar uso a pacientes adultos até correção
     - Atualização de software urgente

4. **Risco de processo legal ou responsabilidade civil?**
   - ☐ Baixo (improvável)
   - ☑ Médio (paciente/hospital pode questionar)
   - ☐ Alto (já há processo em andamento)
   - Recomendação: Acionar seguro de responsabilidade civil, documentar ação proativa

**Classificação Final de Impacto Regulatório:** ALTO

---

## 5. CATEGORIZAÇÃO DA CAUSA RAIZ

Com base na análise das 3 metodologias (5 Whys + Ishikawa + Modo de Falha), categorizar a causa raiz e definir responsável e SLA:

| Categoria | Descrição | Exemplo | Responsável | SLA Correção |
|-----------|-----------|---------|-------------|--------------|
| **Bug Crítico** | Erro grave de código (crash, data loss, cálculo incorreto) | Crash ao inserir CBC, perda de dados | Dev Team + QA | 7 dias |
| **Bug Alto** | Erro de lógica sem crash (resultado incorreto) | Cálculo errado de índice hematimétrico | Dev Team | 30 dias |
| **Dados Inválidos** | Entrada problemática não detectada | CBC fora do range, unidades incorretas | QA + Dev | 14 dias |
| **Uso Inadequado** | Erro do usuário, má interpretação | Usuário não entendeu sugestão | Treinamento + UX | 30 dias |
| **Limitação Design** | Sistema funciona como esperado, mas inadequado | Edge case não coberto (pediatria) | Product + Dev | 90 dias |
| **Infraestrutura** | Problema de ambiente (rede, servidor, latência) | Timeout, lentidão, indisponibilidade | DevOps | 7 dias |

**Categorização do Caso Exemplo (LMA vs LLA pediátrico):**
- **Categoria**: Limitação de Design + Dados Inválidos (categoria combinada)
- **Descrição**: Sistema não foi projetado/validado para população pediátrica + Validação não detectou paciente fora do range de treinamento do modelo
- **Responsável**: Product Manager + Dev Team + Risk Manager
- **SLA**: 60 dias (intermediário entre Bug Alto e Limitação Design devido à gravidade ALTA)

---

## 6. RELATÓRIO DE INVESTIGAÇÃO

Ao final da investigação, elaborar **relatório estruturado** usando o template abaixo.

### Template Completo de Relatório de Investigação

---

# Relatório de Investigação de Incidente

**Número do Incidente**: INC-2025-XXX
**Tipo de Evento**: ☐ Sugestão Incorreta ☐ Crash ☐ Timeout ☐ Perda de Dados ☐ Outro: __________
**Severidade**: ☐ GRAVE ☐ NÃO GRAVE
**Data de Ocorrência**: DD/MM/YYYY HH:MM
**Data da Investigação**: DD/MM/YYYY a DD/MM/YYYY (Duração: ___ dias)
**Investigador Responsável**: [Nome Completo] - [Função: Risk Manager / QA Engineer / Clinical Expert]

---

## 1. SUMÁRIO EXECUTIVO

[Parágrafo único, máximo 200 palavras, respondendo:]
- **O que aconteceu?** (descrição do incidente em linguagem não-técnica)
- **Por que aconteceu?** (causa raiz em 1 frase)
- **O que será feito?** (ação corretiva proposta em 1 frase)

**Exemplo:**
> Em 15/03/2025, o sistema HemoDoctor sugeriu diagnóstico de Leucemia Mieloide Aguda (LMA) para paciente pediátrico de 2 anos, quando o diagnóstico correto era Leucemia Linfoide Aguda (LLA). A investigação identificou que o modelo de Machine Learning não foi validado para população pediátrica e a validação de entrada não verifica adequação do paciente ao escopo do modelo. Como ação corretiva, será implementada validação obrigatória de idade com alerta quando paciente estiver fora do range de treinamento (18-80 anos), e será conduzida validação clínica específica para população pediátrica antes de liberar uso neste grupo.

---

## 2. EVIDÊNCIAS COLETADAS

Listar **todas** as evidências, numeradas sequencialmente:

1. **Logs de Sistema** (caminho: `/logs/2025-03-15/hemodoctor_app.log`, linhas 1234-1567)
   - Timestamp de cada evento
   - User ID: 1234 (Dr. Maria Silva)
   - Input CBC: WBC=45.000, Hgb=8.5, Blastos=60%, etc.
   - Output: Sugestão LMA, confidence 78%

2. **Screenshots** (anexos: `INC-2025-XXX/screenshots/`)
   - `tela_resultado.png`: Tela de resultado exibida ao usuário
   - `input_cbc.png`: Dados de CBC inseridos

3. **Entrevista com Usuário** (arquivo: `entrevista_DrMariaSilva_20250316.pdf`)
   - Data: 16/03/2025
   - Duração: 45 minutos
   - Principais pontos:
     - Usuária confiou na sugestão do sistema
     - Não recebeu alerta sobre limitação para pediatria
     - Percebeu discrepância ao receber resultado de citometria

4. **Prontuário Médico** (cópia anonimizada: `prontuario_paciente_RS.pdf`)
   - Diagnóstico final: LLA (Leucemia Linfoide Aguda) confirmada por biópsia + citometria de fluxo
   - Evolução: Tratamento instituído, paciente em remissão

5. **Análise de Banco de Dados** (relatório: `analise_casos_pediatricos_202501-202506.xlsx`)
   - Total de pacientes pediátricos: 87
   - Casos similares encontrados: 3 (requerem follow-up)

6. **Versão de Software** (confirmado via GitLab)
   - HemoDoctor: v1.2.3 (commit hash: `abc123def456`)
   - Modelo HemoAI: v4.5 (treinado em 01/09/2024 com dataset adulto)

7. **Documentação de Requisitos** (revisada)
   - SRS-001 v1.0: REQ-FUNC-015 especifica validação de idade, mas **não foi testado adequadamente**
   - TST-001 v1.0: Plano de testes **não inclui casos pediátricos** (gap identificado)

---

## 3. TIMELINE DO INCIDENTE

[Inserir tabela detalhada conforme Seção 3.2.1]

---

## 4. ANÁLISE DE CAUSA RAIZ

### 4.1. Metodologia: 5 Whys

[Inserir análise completa conforme Seção 3.3.1]

**Causa Raiz Identificada (5 Whys):**
Requisito de validação de idade pediátrica (REQ-FUNC-015) não foi adequadamente testado durante validação de sistema (gap no plano de testes TST-001).

### 4.2. Metodologia: Ishikawa (6M)

[Inserir análise completa conforme Seção 3.3.2]

**Causas Principais (Ishikawa):**
- Método: Validação de entrada falhou (idade não verificada)
- Material: Dados fora do range de treinamento do modelo
- Medida: Alertas automáticos ausentes para população não validada

### 4.3. Análise de Modo de Falha

**Tipo de Falha**: Limitação de Design + Dados Inválidos (categoria combinada)

**Evidência que Suporta:**
- Modelo HemoAI v4.5 foi treinado exclusivamente com dados de adultos (18-80 anos)
- Nenhum caso pediátrico foi incluído no dataset de treinamento ou validação
- Validation Service não implementa verificação de adequação do paciente ao escopo do modelo
- IFU (Instruções de Uso) não documenta claramente esta limitação

---

## 5. CAUSA RAIZ CONSOLIDADA

**Causa Raiz Primária:**
Ausência de validação clínica do sistema HemoDoctor para população pediátrica, resultando em uso fora do escopo validado.

**Causas Secundárias (contribuintes):**
1. Gap no plano de testes: TST-001 não incluiu casos pediátricos
2. IFU incompleta: Seção "Limitações" não especifica restrição de idade
3. Alertas ausentes: Sistema não detecta automaticamente pacientes fora do range validado

**Categoria:** Limitação de Design + Dados Inválidos
**Evidências que Suportam:**
- Dataset de treinamento do modelo (adultos apenas)
- Plano de testes TST-001 (ausência de casos pediátricos)
- Código do Validation Service (sem verificação de idade)
- Relatório de validação clínica (não inclui pediatria)

---

## 6. IMPACTO AVALIADO

### 6.1. Impacto no Paciente
**Classificação:** MODERADO
- Atraso de 2h na conduta correta
- Sem sequela permanente (tratamento corrigido a tempo)
- Exames adicionais necessários

### 6.2. Impacto no Sistema
**Classificação:** ALTO
- 87 pacientes pediátricos potencialmente afetados (últimos 6 meses)
- 3 casos similares identificados (requerem investigação retroativa)
- Múltiplos módulos afetados (Validation, HemoAI, UI, IFU)

### 6.3. Impacto Regulatório
**Classificação:** ALTO
- Notificação ANVISA obrigatória (evento GRAVE)
- Não-conformidade ISO 13485 (validação inadequada)
- Risco de FSCA (Field Safety Corrective Action)

---

## 7. RECOMENDAÇÕES

### 7.1. Ação Corretiva Imediata (0-7 dias)

**Objetivo:** Mitigar risco imediato enquanto ação definitiva é implementada

**Ações:**
1. **Emitir Field Safety Notice (FSN) URGENTE** para todos os usuários do HemoDoctor:
   - Título: "Importante: Limitação de Uso para Pacientes Pediátricos"
   - Conteúdo: "O sistema HemoDoctor foi validado exclusivamente para pacientes adultos (idade 18-80 anos). **NÃO UTILIZE** para pacientes pediátricos (< 18 anos) até nova comunicação."
   - Canal: Email + notificação in-app + ligação telefônica para hospitais pediátricos

2. **Implementar alerta temporário na UI** (hotfix v1.2.4):
   - Ao inserir idade < 18 anos: Exibir alerta **CRÍTICO** (vermelho, blocking):
     - "⚠️ ATENÇÃO: Este sistema não foi validado para pacientes pediátricos. A sugestão diagnóstica pode estar incorreta. Recomenda-se fortemente não utilizar o resultado."
   - Usuário deve confirmar ciência do risco (checkbox + assinatura digital) para prosseguir

3. **Atualizar IFU imediatamente** (v1.1):
   - Seção "Indicações de Uso": Adicionar "Pacientes adultos (18-80 anos)"
   - Seção "Contraindicações": Adicionar "Pacientes pediátricos (< 18 anos) - sistema não validado para esta população"
   - Seção "Limitações": Adicionar descrição detalhada da limitação

4. **Investigação retroativa dos 3 casos similares identificados:**
   - Revisão dos prontuários
   - Contato com médicos responsáveis
   - Avaliar se houve dano e necessidade de notificação

**Responsável:** Gerente de Qualidade + RT
**Prazo:** 7 dias corridos
**Status:** ☐ Planejado ☐ Em andamento ☐ Concluído

### 7.2. Ação Corretiva de Longo Prazo (7-60 dias)

**Objetivo:** Corrigir definitivamente o problema, permitindo uso seguro em população pediátrica (se viável) ou garantir controles adequados

**Ações:**

**Opção A (Preferencial): Validar Sistema para Uso Pediátrico**

1. **Coletar dataset pediátrico** (30 dias):
   - Mínimo 500 casos de CBC pediátricos (0-18 anos) com diagnóstico confirmado
   - Incluir distribuição etária (0-2 anos, 3-5, 6-12, 13-18)
   - Incluir casos normais + principais patologias pediátricas (LLA, anemia ferropriva, infecções)
   - Parceria com hospitais pediátricos de referência

2. **Retreinar ou ajustar modelo HemoAI** (20 dias):
   - Opção 1: Retreinar modelo v5.0 com dataset adulto + pediátrico
   - Opção 2: Criar modelo específico para pediatria (HemoAI-Ped)
   - Validar performance separadamente (adultos vs pediatria)

3. **Validação clínica específica** (30 dias):
   - Estudo prospectivo com 100 casos pediátricos
   - Avaliar sensibilidade, especificidade, VPP, VPN
   - Comparar com especialista em hematologia pediátrica
   - Protocolo aprovado por CEP (Comitê de Ética em Pesquisa)

4. **Atualizar documentação técnica** (10 dias):
   - SRS-001 v2.0: Especificar requisitos pediátricos
   - TST-001 v2.0: Adicionar casos de teste pediátricos
   - RMP-001 v2.0: Atualizar gestão de risco (novo escopo)
   - IFU v2.0: Remover contraindicação se validação for bem-sucedida

**OU**

**Opção B (Alternativa): Manter Restrição Pediátrica com Controles Rigorosos**

1. **Implementar validação técnica obrigatória** (14 dias):
   - Validation Service: Verificação automática de idade
   - Se idade < 18 anos → **BLOQUEAR** uso do sistema (não apenas alertar)
   - Mensagem: "Sistema não disponível para pacientes pediátricos. Contate suporte para mais informações."

2. **Controles administrativos** (7 dias):
   - Contrato de licença: Adicionar cláusula de restrição de uso
   - Treinamento obrigatório: Enfatizar limitação pediátrica
   - Auditoria periódica: Verificar se hospitais pediátricos estão usando indevidamente

**Decisão entre Opção A ou B:**
- Reunião da Direção em 7 dias
- Avaliar viabilidade técnica, regulatória e comercial
- Considerar demanda de mercado (hospitais pediátricos representam X% da receita?)

**Responsável:** Product Manager + Dev Team + Clinical Affairs
**Prazo:** 60 dias
**Status:** ☐ Planejado ☐ Em andamento ☐ Concluído

### 7.3. Ação Preventiva

**Objetivo:** Prevenir problemas similares (uso fora do escopo validado) em futuros desenvolvimentos

**Ações:**

1. **Atualizar processo de desenvolvimento** (14 dias):
   - Checklist obrigatório em Design Review: "População-alvo está claramente definida? Controles para uso fora do escopo estão implementados?"
   - Gate de aprovação: Não passar para desenvolvimento sem definição clara de escopo e limitações

2. **Melhorar plano de testes** (14 dias):
   - Template de TST atualizado: Incluir seção "Casos Fora do Escopo" (boundary testing)
   - Teste obrigatório: Verificar comportamento do sistema quando usado fora do escopo validado

3. **Implementar sistema de alertas dinâmicos** (30 dias):
   - Metadados do modelo: Incluir "range_idade_valido: [18, 80]", "population: adult"
   - Validation Service: Comparar dados do paciente com metadados do modelo automaticamente
   - Gerar alerta automático se fora do escopo

4. **Treinamento da equipe** (30 dias):
   - Workshop: "Gestão de Riscos em IA/ML para Healthcare"
   - Tópicos: Edge cases, população não validada, bias algorítmico, limitações de modelos
   - Público: Dev Team, QA, Product, Clinical Affairs

**Responsável:** Quality Manager + Training Coordinator
**Prazo:** 30 dias
**Status:** ☐ Planejado ☐ Em andamento ☐ Concluído

---

## 8. DECISÕES

Marcar "S" (Sim) ou "N" (Não) e justificar:

| Decisão | S/N | Justificativa |
|---------|-----|---------------|
| **Necessidade de CAPA** | **S** | Causa raiz identificada requer ação corretiva sistemática (implementar validação, atualizar IFU, retreinar modelo ou restringir uso). Abrir CAPA-2025-XXX vinculado a INC-2025-XXX. |
| **Atualização de RMP (Gestão de Riscos)** | **S** | Risco não adequadamente controlado foi identificado: "Uso do sistema em população não validada". Atualizar RMP-001 com novo risco (ou revisar probabilidade de risco existente) e controles de mitigação. |
| **Notificação ANVISA** | **S** | Evento classificado como GRAVE (atraso no tratamento, risco de dano ao paciente). Notificação obrigatória em 10 dias úteis via NOTIVISA. Usar FORM-004. |
| **Correção de Bug** | **N** | Não é bug de software (sistema funcionou como projetado). É limitação de design. Porém, validação de entrada deve ser melhorada (ver ação corretiva). |
| **Treinamento Adicional** | **S** | Usuários devem ser retreinados sobre: (1) Limitações do sistema (população validada); (2) Interpretação de confidence scores; (3) Importância de análise crítica do resultado. |
| **Atualização de IFU** | **S** | IFU atual não documenta adequadamente a limitação para população pediátrica. Atualizar seções: Indicações, Contraindicações, Limitações. |
| **Field Safety Notice (FSN)** | **S** | Comunicação urgente aos usuários sobre limitação crítica de segurança. Prevenir novos casos enquanto ação corretiva não é implementada. |
| **Investigação Retroativa** | **S** | 3 casos similares foram identificados no banco de dados. Necessário investigar se houve dano e tomar ações apropriadas (notificações adicionais, follow-up clínico). |

---

## 9. CONCLUSÃO

[Parágrafo final resumindo status e próximos passos]

**Exemplo:**
> A investigação concluiu que o incidente INC-2025-XXX resultou de uso do sistema HemoDoctor em população pediátrica, para a qual o sistema não foi validado. A causa raiz foi identificada como ausência de validação clínica para este grupo etário e falha na implementação de controles para prevenir uso fora do escopo validado. Ações corretivas imediatas (Field Safety Notice + alerta temporário na UI) serão implementadas em 7 dias. Ações de longo prazo (validação pediátrica ou restrição técnica de uso) serão definidas pela Direção e implementadas em 60 dias. CAPA-2025-XXX foi aberto para acompanhar implementação e verificação de eficácia. Notificação ANVISA será submetida em 10 dias úteis conforme RDC 67/2009.

---

## 10. ASSINATURAS

**Investigador:**
- Nome: ___________________________________
- Função: Risk Manager
- Assinatura: _____________________ Data: ___/___/_____

**Gerente de Qualidade:**
- Nome: ___________________________________
- Função: Quality Manager
- Assinatura: _____________________ Data: ___/___/_____
- **Aprovação da Investigação**: ☐ Aprovado ☐ Revisar

**Responsável Técnico (RT):**
- Nome: ___________________________________
- Função: RT (Responsável Técnico ANVISA)
- Registro Profissional: CRM __________
- Assinatura: _____________________ Data: ___/___/_____
- **Aprovação para Ações Corretivas**: ☐ Aprovado ☐ Revisar

---

[FIM DO RELATÓRIO]

---

## 7. DECISÃO SOBRE AÇÕES (6 Cenários)

Baseado na **categorização da causa raiz** (Seção 5), aplicar o fluxo de decisão apropriado:

### 7.1. Se BUG Identificado

**Cenário:** Erro de código (crash, cálculo incorreto, null pointer, loop infinito, perda de dados)

**Ações Obrigatórias:**

1. **Abrir ticket de desenvolvimento** (usar Jira, GitHub Issue, ou sistema de tracking)
   - Título: "[BUG] [CRÍTICO/ALTO/MÉDIO/BAIXO] Descrição curta"
   - Descrição: Link para relatório de investigação, passos para reproduzir, evidências (logs, screenshots)
   - Labels: `bug`, `security` (se aplicável), `patient-safety` (se crítico)

2. **Prioridade conforme severidade:**
   - **Crítico**: Impacto na segurança do paciente, data loss, crash sistemático → P0 (hotfix imediato)
   - **Alto**: Resultado incorreto, impacto clínico moderado → P1 (próximo sprint)
   - **Médio**: Bug funcional sem impacto clínico → P2 (backlog priorizado)
   - **Baixo**: Bug estético, usabilidade → P3 (backlog)

3. **Definir target fix version:**
   - P0: Hotfix (v1.2.4) em 7 dias
   - P1: Próxima release minor (v1.3.0) em 30 dias
   - P2: Próxima release major (v2.0.0) em 90 dias

4. **Regressão testing obrigatório após correção:**
   - Executar suite completa de testes (automated + manual)
   - Verificar que bug foi corrigido **E** que correção não introduziu novos bugs
   - Teste específico: Criar test case que reproduz o bug original (deve passar após correção)

5. **Atualizar TST-001 (Plano de Testes):**
   - Se bug não estava coberto por testes existentes → Adicionar novo test case
   - Objetivo: Garantir que bug não retorne em futuras versões (regression prevention)

**Responsável:** Dev Team + QA Team
**Prazo:** Conforme prioridade (7-90 dias)

### 7.2. Se DADO Incorreto

**Cenário:** Entrada problemática (CBC fora do range, unidades incorretas, formato inválido, valores impossíveis)

**Ações Obrigatórias:**

1. **Melhorar validação de entrada no Validation Service:**
   - Implementar checks adicionais:
     - Range checks (min/max para cada parâmetro de CBC)
     - Consistência interna (ex: Hematócrito deve ser ~3x Hemoglobina)
     - Unidades (converter automaticamente ou exigir unidade padrão)
     - Valores impossíveis (ex: WBC > 500.000 é extremamente raro, requer confirmação)

2. **Adicionar alertas específicos para usuário:**
   - Se valor fora do normal mas tecnicamente possível:
     - Alerta amarelo (warning): "Valor de WBC (150.000) está muito acima do normal. Favor confirmar."
   - Se valor impossível:
     - Alerta vermelho (erro): "Valor de Hematócrito (150%) é impossível. Favor revisar."

3. **Documentar range válido no IFU:**
   - Seção "Especificações Técnicas":
     - Tabela com ranges aceitos para cada parâmetro de CBC
     - Unidades padrão (ex: WBC em células/µL, Hgb em g/dL)
   - Seção "Solução de Problemas":
     - "O que fazer se o sistema rejeitar um valor de CBC?"

4. **Atualizar SRS-001 (Requisitos de Sistema):**
   - Se requisito de validação estava faltando → Adicionar novo requisito
   - Se requisito existia mas era vago → Tornar específico (especificar ranges numéricos)

**Responsável:** QA Team + Dev Team (Validation Service)
**Prazo:** 14 dias

### 7.3. Se USO Inadequado

**Cenário:** Erro do usuário (má interpretação da sugestão, falta de análise crítica, uso fora do escopo, treinamento inadequado)

**Ações Obrigatórias:**

1. **Atualizar IFU (Instruções de Uso):**
   - **Seção "Como Usar"**: Tornar mais claro, adicionar exemplos, prints de tela, workflow passo a passo
   - **Seção "Interpretação de Resultados"**:
     - Explicar o que significa cada sugestão diagnóstica
     - Enfatizar: "A sugestão do sistema é uma FERRAMENTA DE APOIO, não substitui julgamento clínico"
     - Adicionar exemplos de casos onde médico DEVE questionar a sugestão (confidence baixo, contexto clínico discordante)
   - **Seção "Limitações"**: Listar claramente o que o sistema NÃO faz

2. **Treinamento adicional para usuários:**
   - **Formato**: Presencial (workshop 2h) ou online (vídeo 30min + quiz)
   - **Conteúdo obrigatório**:
     - Revisão das limitações do sistema
     - Interpretação de confidence scores (< 70% = baixa confiança, > 90% = alta confiança)
     - Casos de uso correto vs incorreto (case studies)
     - Quiz de avaliação (nota mínima 80% para aprovação)
   - **Público**: Todos os usuários existentes (refresher) + novos usuários (onboarding)
   - **Evidência**: Certificado de conclusão + registro no sistema de treinamento

3. **Melhorar UX (User Experience):**
   - **Tooltips contextuais**: Ao passar mouse sobre sugestão diagnóstica, exibir explicação resumida
   - **Ajuda contextual**: Botão "?" em cada tela, abrindo documentação relevante
   - **Wizards**: Para tarefas complexas, guiar usuário passo a passo
   - **Confirmações**: Para ações críticas (ex: aceitar sugestão diagnóstica), solicitar confirmação explícita

4. **Considerar redesign se muitos usuários erram:**
   - Se > 20% dos usuários cometem o mesmo erro → Problema é de design, não de treinamento
   - Conduzir teste de usabilidade (observar usuários reais usando o sistema)
   - Identificar pontos de confusão e redesenhar interface

**Responsável:** Training Team + UX Designer + Clinical Affairs
**Prazo:** 30 dias

### 7.4. Se LIMITAÇÃO de Design

**Cenário:** Sistema funciona como esperado (não é bug), mas resultado é inadequado para caso específico (edge case não coberto, população não validada, contexto clínico não suportado)

**Ações Obrigatórias:**

**Passo 1: Avaliar Severidade**

Perguntas críticas:
1. **É crítico corrigir?** (há risco significativo ao paciente?)
   - SIM → Prosseguir para ação corretiva (Passo 2A)
   - NÃO → Prosseguir para documentação de limitação conhecida (Passo 2B)

**Passo 2A: Se SIM (Risco Crítico) - Corrigir Limitação**

1. **Abrir CAPA** (PROC-003)
   - Tipo: Ação Corretiva
   - Fonte: Incidente INC-YYYY-XXX
   - Causa raiz: Limitação de design

2. **Planejar redesign ou extensão de escopo:**
   - Exemplo (caso LMA vs LLA pediátrico):
     - Opção 1: Validar sistema para população pediátrica (coletar dados, retreinar modelo, validação clínica)
     - Opção 2: Implementar controle técnico para bloquear uso fora do escopo validado
   - Envolver: Product Manager, Dev Team, Clinical Affairs, Regulatory Affairs

3. **Atualizar gestão de risco (RMP-001):**
   - Risco identificado: "Uso em população não validada resulta em sugestão incorreta"
   - Probabilidade: Alta (se não houver controles)
   - Severidade: Alta (impacto clínico)
   - Controles de mitigação: Implementar controles técnicos ou administrativos
   - Risco residual: Deve ser reduzido a nível aceitável

**Prazo:** 90 dias (redesign completo) ou 14 dias (controle técnico)

**Passo 2B: Se NÃO (Risco Baixo) - Documentar Limitação**

1. **Documentar limitação conhecida no IFU:**
   - **Seção "Limitações"** (criar ou expandir):
     - Listar claramente os cenários onde sistema pode não funcionar adequadamente
     - Exemplo: "Este sistema não foi validado para pacientes pediátricos (< 18 anos), portanto sugestões podem estar incorretas neste grupo."
   - **Seção "Indicações de Uso"**:
     - Especificar claramente população-alvo (ex: "Adultos de 18 a 80 anos")

2. **Atualizar gestão de risco (RMP-001):**
   - Risco identificado: "Limitação de design resulta em sugestão subótima para edge cases"
   - Probabilidade: Média (casos raros)
   - Severidade: Baixa (usuário pode identificar e compensar)
   - Controles de mitigação: Documentar no IFU, treinar usuários sobre limitação
   - Risco residual: Aceitável (com controles administrativos)

3. **Comunicar aos usuários:**
   - Field Safety Notice (se limitação não era conhecida previamente)
   - Email aos usuários: "Esclarecimento sobre Limitações do Sistema"
   - Treinamento: Incluir discussão sobre limitações conhecidas

**Prazo:** 14 dias

**Responsável:** Product Manager + Regulatory Affairs + Risk Manager

### 7.5. Se INFRAESTRUTURA

**Cenário:** Problema de ambiente (timeout de rede, servidor lento, latência alta, indisponibilidade, problema de integração com LIS)

**Ações Obrigatórias:**

1. **Melhorar monitoramento (observability):**
   - Adicionar alertas automáticos:
     - Latência > 10s → Alerta para equipe DevOps
     - Uptime < 99.5% em 24h → Alerta para gerência
     - Taxa de erro > 1% → Alerta imediato
   - Implementar dashboards:
     - Grafana ou similar: Métricas em tempo real (latência, throughput, erros, uptime)
     - Log aggregation: ELK stack ou similar (centralizar logs de todos os serviços)

2. **Aumentar recursos (capacity planning):**
   - Se problema foi causado por sobrecarga:
     - CPU, RAM, disco: Aumentar capacidade do servidor
     - Rede: Aumentar largura de banda, otimizar roteamento
     - Banco de dados: Adicionar índices, otimizar queries, considerar sharding
   - Realizar load testing: Simular pico de uso e verificar se infraestrutura suporta

3. **Implementar retry logic e graceful degradation:**
   - Retry automático: Se timeout de rede, tentar novamente (3x com backoff exponencial)
   - Circuit breaker: Se serviço externo está fora, não sobrecarregar com requisições (falhar rápido)
   - Fallback: Se serviço não está disponível, exibir mensagem clara ao usuário ("Sistema temporariamente indisponível. Tente novamente em 5 minutos.")
   - Queue de requisições: Se sistema está sobrecarregado, enfileirar requisições ao invés de rejeitar

4. **SLA com fornecedor (se serviço terceiro):**
   - Revisar contrato: SLA está sendo cumprido?
   - Escalação: Contatar fornecedor para resolver problema recorrente
   - Plano B: Considerar fornecedor alternativo se SLA não é cumprido consistentemente

**Responsável:** DevOps Team + Infrastructure Manager
**Prazo:** 7 dias (mitigação) + 30 dias (solução permanente)

### 7.6. Se MÚLTIPLAS Causas (Análise Complexa)

**Cenário:** Investigação identificou que incidente foi causado por **combinação de fatores** (ex: bug + uso inadequado + infraestrutura)

**Ações Obrigatórias:**

1. **Abrir CAPA com ações múltiplas:**
   - Cada causa raiz → Uma ação corretiva específica
   - Exemplo:
     - Causa 1 (Bug): Corrigir código (prazo: 14 dias)
     - Causa 2 (Treinamento): Retreinar usuários (prazo: 30 dias)
     - Causa 3 (Infraestrutura): Aumentar capacidade de servidor (prazo: 7 dias)

2. **Priorizar por impacto:**
   - Qual causa contribuiu mais para o incidente?
   - Qual ação tem maior impacto na prevenção de recorrência?
   - Matriz de priorização:
     - **Urgente + Importante** (fazer PRIMEIRO): Ação crítica de segurança
     - **Urgente + Não Importante**: Ação rápida mas baixo impacto (fazer se houver tempo)
     - **Não Urgente + Importante**: Ação estratégica (planejar bem)
     - **Não Urgente + Não Importante**: Ação opcional (baixa prioridade)

3. **Cronograma faseado de implementação:**
   - Fase 1 (0-7 dias): Ações imediatas (mitigação de risco)
   - Fase 2 (7-30 dias): Ações de curto prazo (correções principais)
   - Fase 3 (30-90 dias): Ações de longo prazo (melhorias estruturais)

4. **Coordenação entre equipes:**
   - Reunião de kickoff do CAPA: Alinhar todas as equipes envolvidas
   - Status semanal: Acompanhar progresso de cada ação
   - Identificar dependências: Ação B depende de Ação A? Planejar sequência apropriada

**Responsável:** CAPA Owner (designado) + Gerente de Qualidade (coordenação)
**Prazo:** Conforme cronograma faseado (até 90 dias)

---

## 8. INTEGRAÇÃO COM CAPA (PROC-003)

### 8.1. Critério de Abertura de CAPA

**Abrir CAPA obrigatoriamente se:**
- Ação corretiva é necessária (conforme Seção 7)
- Incidente é classificado como GRAVE
- Causa raiz requer mudança em design, processo ou documentação
- Risco de recorrência é MÉDIO ou ALTO

**Não abrir CAPA se:**
- Incidente é isolado (único caso, improvável repetir)
- Causa foi erro humano pontual sem falha de processo
- Ação já foi tomada imediatamente (ex: correção de dados) e risco de recorrência é BAIXO

### 8.2. Vinculação INC ↔ CAPA

**Link bidirecional:**
- No relatório de investigação (FORM-002): Campo "CAPA Relacionada" → CAPA-YYYY-XXX
- No formulário CAPA (FORM-003): Campo "Incidente de Origem" → INC-YYYY-XXX

**Rastreabilidade:**
- Sistema de gestão de qualidade deve permitir navegação entre INC e CAPA
- Dashboard: Visualizar todos os CAPAs abertos a partir de incidentes

### 8.3. Causa Raiz Compartilhada

**Usar MESMA causa raiz** identificada na investigação (Seção 5):
- Copiar texto da causa raiz do relatório de investigação para FORM-003 (Seção C)
- Garantir consistência: Não criar causa raiz diferente no CAPA
- Se análise posterior revelar causa raiz diferente → Atualizar AMBOS documentos (INC e CAPA)

### 8.4. Responsável

**Responsável da investigação = Responsável inicial do CAPA:**
- Quem conduziu a investigação (Risk Manager, QA Engineer) é o responsável natural por iniciar o CAPA
- Durante planejamento do CAPA (PROC-003, Etapa 3), responsável pode ser transferido para pessoa mais adequada para implementar ação (ex: Dev Team Lead se ação é correção de código)

### 8.5. Prazo da Ação

**Prazo conforme tabela de SLA (Seção 5):**
- Usar categorização de causa raiz para determinar prazo:
  - Bug Crítico → 7 dias
  - Bug Alto → 30 dias
  - Dados Inválidos → 14 dias
  - Uso Inadequado → 30 dias
  - Limitação Design → 90 dias
  - Infraestrutura → 7 dias

### 8.6. Fechamento Coordenado

**Incidente só pode ser fechado após CAPA ser fechado:**
- Status do incidente: "Aguardando CAPA" até CAPA-YYYY-XXX ser concluído e eficácia verificada
- Quando CAPA é fechado → Atualizar incidente para "Fechado - CAPA Eficaz"
- Se CAPA falhar → Reabrir investigação (causa raiz pode ter sido identificada incorretamente)

---

## 9. ATUALIZAÇÃO DE GESTÃO DE RISCO (RMP-001)

A gestão de risco (Risk Management Plan - RMP) é um **documento vivo** que deve ser atualizado sempre que novos riscos são identificados ou riscos existentes mudam.

### 9.1. Perguntas Obrigatórias (Avaliar 3 Cenários)

**Pergunta 1: Novo risco identificado que não estava no RMP?**

- **Como identificar:** Revisar RMP-001 e buscar se risco similar já está documentado
- **Se SIM (risco novo):**
  1. Adicionar novo risco ao RMP-001
  2. Preencher análise de risco:
     - Identificação do perigo (hazard)
     - Situação perigosa (hazardous situation)
     - Dano potencial (harm)
     - Probabilidade de ocorrência (P1 a P5: improvável a frequente)
     - Severidade do dano (S1 a S5: insignificante a catastrófico)
     - Risco inicial (P x S)
     - Controles de mitigação (o que será feito para reduzir risco)
     - Risco residual (após controles)
     - Aceitabilidade (aceitável / não aceitável)

**Exemplo (caso LMA vs LLA pediátrico):**

| Campo | Valor |
|-------|-------|
| **ID do Risco** | RISK-047 (novo) |
| **Perigo (Hazard)** | Uso do sistema em população não validada (pediatria) |
| **Situação Perigosa** | Paciente pediátrico tem CBC processado por modelo treinado com dados adultos |
| **Dano Potencial** | Sugestão diagnóstica incorreta → atraso ou erro no tratamento → dano ao paciente |
| **Probabilidade (antes)** | P3 (Ocasional) - Casos pediátricos representam 5% do uso |
| **Severidade** | S4 (Grave) - Pode resultar em lesão grave ou morte |
| **Risco Inicial** | P3 x S4 = **ALTO** (inaceitável) |
| **Controles de Mitigação** | 1. Alerta blocking na UI para idade < 18 anos<br>2. Field Safety Notice aos usuários<br>3. Atualização de IFU (contraindicação)<br>4. Treinamento sobre limitação<br>5. [Futuro] Validação clínica para pediatria |
| **Probabilidade (depois)** | P1 (Raro) - Com controles, uso indevido é raro |
| **Risco Residual** | P1 x S4 = **MÉDIO** (aceitável com controles) |
| **Aceitabilidade** | ✓ Aceitável (com controles implementados) |
| **Verificação de Controle** | Auditoria trimestral: Verificar se usuários estão respeitando contraindicação |

---

**Pergunta 2: Risco existente foi subestimado (probabilidade ou severidade)?**

- **Como identificar:** Buscar no RMP-001 se risco similar já existe
- **Se SIM (risco subestimado):**
  1. Revisar avaliação de risco existente
  2. Atualizar probabilidade (se incidente ocorreu mais vezes que esperado)
  3. Atualizar severidade (se dano foi maior que previsto)
  4. Recalcular risco residual
  5. Se novo risco residual é inaceitável → Adicionar controles adicionais

**Exemplo:**
- Risco existente: RISK-012 "Modelo classifica incorretamente leucemia aguda"
- Avaliação anterior: P2 (Raro) x S3 (Moderado) = MÉDIO (aceitável)
- Após incidente: Identificou-se que probabilidade é maior em pediatria
- Nova avaliação: P3 (Ocasional) x S4 (Grave) = ALTO (inaceitável)
- Ação: Adicionar controles (conforme RISK-047 acima)

---

**Pergunta 3: Controles de mitigação atuais são inadequados?**

- **Como identificar:** Verificar se controles existentes no RMP preveniram o incidente
- **Se controles falharam:**
  1. Avaliar por que controle não funcionou:
     - Controle não foi implementado?
     - Controle foi implementado mas é ineficaz?
     - Controle foi bypassado pelo usuário?
  2. Atualizar controles:
     - Fortalecer controle existente (tornar obrigatório, automatizado)
     - Adicionar controle adicional (defesa em profundidade)
  3. Re-avaliar risco residual

**Exemplo:**
- Controle existente: "Usuários são treinados sobre limitações do sistema"
- Falha: Treinamento não enfatizava suficientemente a contraindicação pediátrica
- Ação: Fortalecer controle → Implementar controle técnico (alerta blocking na UI) em adição ao controle administrativo (treinamento)

### 9.2. Documentação no RMP-001

**Atualizar seção "Histórico de Revisões" do RMP-001:**

| Versão | Data | Descrição da Mudança | Autor | Aprovador |
|--------|------|----------------------|-------|-----------|
| 1.0 | 01/01/2025 | Versão inicial do RMP | Risk Manager | RT |
| 1.1 | 15/03/2025 | **Adicionado RISK-047** (uso em população pediátrica) após incidente INC-2025-XXX. Controles de mitigação implementados (alerta UI, FSN, IFU atualizado). Risco residual: MÉDIO (aceitável). | Risk Manager | RT |

**Atualizar seção "Análise de Risco":**
- Adicionar nova linha na tabela de riscos com RISK-047
- Ou atualizar linha existente se risco similar já estava documentado

**Atualizar seção "Controles de Mitigação":**
- Listar controles implementados (ex: CTRL-047A: Alerta UI, CTRL-047B: FSN, etc.)
- Para cada controle: Descrever, definir responsável de implementação, prazo

**Atualizar seção "Risco-Benefício":**
- Se novo risco foi identificado: Reavaliar se benefício clínico do dispositivo ainda supera riscos residuais
- Documentar justificativa de aceitabilidade do risco

### 9.3. Aprovação

**Aprovação obrigatória:**
- Risk Manager: Revisa e atualiza RMP
- Responsável Técnico (RT): Aprova atualização (assinatura)
- Gerente de Qualidade: Aprova (assinatura)

**Prazo:** Atualização do RMP deve ser concluída antes do fechamento do CAPA

---

## 10. FOLLOW-UP E FECHAMENTO (4 Etapas)

### 10.1. Verificar Implementação (após 30-60 dias)

**Objetivo:** Confirmar que ação corretiva foi **efetivamente implementada** conforme planejado

**Checklist de Verificação:**

- [ ] **Ação corretiva foi implementada conforme plano do CAPA?**
  - Revisar: Todas as tarefas do CAPA foram concluídas?
  - Evidências: Documentação de implementação (commits de código, certificados de treinamento, versão atualizada de documentos)

- [ ] **Código foi corrigido e deployed?** (se ação era correção de bug)
  - Verificar: Nova versão do software foi lançada em produção?
  - Evidências: Release notes, changelog, tag de versão no Git

- [ ] **Treinamento foi realizado?** (se ação incluía treinamento)
  - Verificar: 100% dos usuários-alvo foram treinados?
  - Evidências: Lista de presença (se presencial), certificados de conclusão (se online), quiz de avaliação (nota ≥ 80%)

- [ ] **IFU foi atualizado?** (se ação incluía atualização de documentação)
  - Verificar: Nova versão do IFU foi publicada e distribuída aos usuários?
  - Evidências: IFU v1.X com data de revisão, email de notificação aos usuários, versão no portal de documentos

- [ ] **Evidências de implementação estão completas e arquivadas?**
  - Pasta do CAPA (ver PROC-003) contém todos os documentos obrigatórios
  - Rastreabilidade: Link entre INC → Investigação → CAPA → Implementação

**Responsável:** Gerente de Qualidade (verifica) + CAPA Owner (fornece evidências)
**Prazo:** 30 dias após data de conclusão planejada (conforme CAPA)

### 10.2. Re-teste / Validação (após implementação)

**Objetivo:** Validar tecnicamente que ação corretiva **funciona como esperado**

**Cenários:**

**A) Se bug foi corrigido:**
- Executar **teste de regressão** completo:
  - Suite de testes automatizados (unit tests, integration tests, E2E tests)
  - Testes manuais exploratórios (casos edge)
- Teste específico do bug:
  - Reproduzir situação que causava o bug (deve estar corrigido)
  - Verificar que correção não introduziu novos bugs
- Evidências: Relatório de testes (TST-XXX), screenshots, logs

**B) Se processo foi mudado:**
- Validar nova versão do processo:
  - Dry-run: Simular uso do processo novo com casos reais
  - Verificar que processo novo previne problema original
- Atualizar documentação do processo (SOP)
- Evidências: Ata de validação, checklist de conformidade

**C) Se treinamento foi realizado:**
- Avaliar eficácia do treinamento:
  - Quiz de avaliação (nota ≥ 80% = aprovado)
  - Observação: Observar usuários usando o sistema após treinamento (estão aplicando o que aprenderam?)
  - Feedback: Questionário de satisfação (treinamento foi claro e útil?)
- Evidências: Resultados de quiz, relatório de observação

**D) Se documentação foi atualizada:**
- Validar completude e clareza da documentação:
  - Revisão técnica: Especialista revisa se informação está correta
  - Revisão de usabilidade: Usuário-alvo consegue entender?
- Evidências: Formulário de revisão assinado

**Responsável:** QA Team (testes de software), Training Team (avaliação de treinamento), Clinical Affairs (revisão de IFU)
**Prazo:** Imediatamente após implementação (antes de validar eficácia)

### 10.3. Validar Eficácia (após 60-90 dias)

**Objetivo:** Confirmar que ação corretiva **EFETIVAMENTE preveniu recorrência** do problema

**Período de Monitoramento:** Mínimo 60 dias (podendo ser 90 dias para casos complexos)

**Método de Validação:**

1. **Monitorar ocorrência de incidentes similares:**
   - Revisar banco de dados de incidentes (PROC-001)
   - Buscar: Incidentes com causa raiz similar ou sintomas similares
   - Métrica: Taxa de recorrência = (Número de incidentes similares no período / Total de oportunidades) x 100%
   - **Meta:** Taxa de recorrência = 0% (ideal) ou < 5% (aceitável)

2. **Comparar situação ANTES vs DEPOIS:**
   - **Antes da ação corretiva:** Quantos incidentes similares ocorreram em 6 meses?
   - **Depois da ação corretiva:** Quantos incidentes similares ocorreram em 2-3 meses?
   - Análise estatística (se aplicável): Diferença é significativa?

**Exemplo (caso LMA vs LLA pediátrico):**

| Métrica | ANTES (Jan-Jun 2025) | DEPOIS (Abr-Jun 2025) | Meta | Status |
|---------|----------------------|-----------------------|------|--------|
| Incidentes de sugestão incorreta em pediatria | 3 casos | 0 casos | 0 | ✅ EFICAZ |
| Uso do sistema em pacientes < 18 anos | 87 pacientes | 2 pacientes (ambos com alerta confirmado) | < 5% do total | ✅ EFICAZ |
| Compliance com IFU (contraindicação respeitada) | N/A | 98% (85/87 usuários treinados) | > 95% | ✅ EFICAZ |

3. **Análise quantitativa e qualitativa:**
   - **Quantitativa:** Métricas objetivas (números, porcentagens)
   - **Qualitativa:** Feedback de usuários ("O alerta é claro e útil?"), observação de uso real

4. **Verificação objetiva (não subjetiva):**
   - Baseada em dados concretos (logs, registros, auditorias)
   - Não baseada em opinião pessoal ("Acho que está melhor")

**Decisão de Eficácia:**

- ✅ **EFICAZ**: Critérios 100% atendidos (taxa recorrência = 0% ou < 5%, metas atingidas)
  - **Ação:** Prosseguir para fechamento do incidente (Etapa 10.4)

- ⚠️ **PARCIALMENTE EFICAZ**: Critérios 50-99% atendidos (houve melhoria, mas ainda há problemas)
  - **Ação:** Ações adicionais necessárias (abrir novo CAPA ou estender CAPA existente)
  - Exemplo: Taxa de recorrência caiu de 10% para 3% (melhoria, mas meta era < 1%)

- ❌ **INEFICAZ**: Critérios < 50% atendidos (problema persiste ou piorou)
  - **Ação:** Reavaliar causa raiz (voltar à Etapa 3.3)
  - Possibilidade: Causa raiz foi identificada incorretamente
  - Reabrir investigação com equipe ampliada ou consultor externo

**Responsável:** Risk Manager + QA Manager
**Prazo:** 60-90 dias após implementação da ação corretiva

### 10.4. Fechar Incidente

**Critérios para Fechamento (TODOS devem ser atendidos):**

- [x] Investigação completa e relatório aprovado (Seção 6)
- [x] Causa raiz identificada e documentada (Seção 5)
- [x] Ação corretiva implementada e evidenciada (Etapa 10.1)
- [x] Re-teste/validação concluído com sucesso (Etapa 10.2)
- [x] Eficácia validada: Taxa de recorrência = 0% ou < 5% (Etapa 10.3)
- [x] Gestão de risco atualizada (RMP-001) (Seção 9)
- [x] CAPA fechado (se aplicável) (Seção 8)
- [x] Notificação ANVISA concluída (se aplicável) (Seção 11)
- [x] Documentação completa arquivada (5 anos)

**Atividades de Fechamento:**

1. **Confirmar eficácia:**
   - Responsável do CAPA: Atesta que ação foi eficaz
   - QA Manager: Revisa evidências e concorda

2. **Comunicar fechamento:**
   - Email para stakeholders:
     - Assunto: "Fechamento de Incidente INC-2025-XXX"
     - Conteúdo resumido: O que aconteceu, o que foi feito, resultado da ação
     - Anexo: Sumário executivo do relatório de investigação (1 página)

3. **Atualizar registros:**
   - Banco de dados de incidentes (Excel: `Registro_Incidentes.xlsx`):
     - Status: "Fechado - Eficaz"
     - Data de fechamento: DD/MM/YYYY
     - Ação corretiva resumida: (texto breve)
   - Sistema de gestão de qualidade (QMS): Atualizar status

4. **Arquivar documentação:**
   - Pasta digital: `Incidentes/2025/INC-2025-XXX/` (estrutura completa)
   - Conteúdo:
     - FORM-001 (Relato)
     - FORM-002 (Investigação)
     - Evidências (logs, screenshots, entrevistas)
     - Relatório de investigação
     - CAPA (FORM-003) e evidências de implementação
     - Aprovações (assinaturas digitais)
     - Verificação de eficácia (relatório)
     - Notificação ANVISA (FORM-004) se aplicável
   - Backup: Cópia de segurança em servidor separado (disaster recovery)
   - Retenção: 5 anos (mínimo legal ISO 13485) + vida útil do produto

5. **Lessons Learned (opcional mas recomendado):**
   - Documento sumário (2-3 páginas):
     - O que aprendemos com este incidente?
     - O que faríamos diferente da próxima vez?
     - Boas práticas identificadas?
     - Recomendações para prevenir incidentes similares?
   - Compartilhar em reunião de equipe ou Análise Crítica da Direção

6. **Apresentar em reunião (se relevante):**
   - Análise Crítica da Direção (ISO 13485): Incluir resumo de incidentes críticos fechados
   - Reunião de Qualidade: Apresentar caso como estudo de caso
   - Treinamento: Usar como exemplo em treinamentos futuros ("Aprenda com nossos erros")

**Aprovação de Fechamento:**

- **Responsável da Investigação**: Atesta conclusão e eficácia
  - Nome: ___________________ Assinatura: __________ Data: ___/___/___

- **Gerente de Qualidade**: Aprova fechamento
  - Nome: ___________________ Assinatura: __________ Data: ___/___/___

- **Responsável Técnico (RT)**: Aprova (se impacto técnico ou regulatório)
  - Nome: ___________________ Assinatura: __________ Data: ___/___/___

**Status Final:** "Fechado - Eficaz"

**Data de Fechamento:** DD/MM/YYYY

---

## 11. RELATÓRIO PARA ANVISA (se aplicável)

Se o incidente foi classificado como **GRAVE** (conforme PROC-001 e RDC 67/2009), notificação à ANVISA é **obrigatória**.

### 11.1. Critérios para Notificação ANVISA

**Notificar ANVISA se:**
- Morte relacionada ao dispositivo médico
- Ameaça à vida do paciente
- Lesão grave ou incapacidade permanente
- Necessidade de intervenção médica para prevenir dano permanente
- Mau funcionamento que, se recorrer, pode levar a dano grave

**Prazos regulatórios (RDC 67/2009):**

| Severidade | Prazo Notificação Inicial | Prazo Relatório Final |
|------------|---------------------------|----------------------|
| **GRAVE** | 10 dias úteis | 60 dias |
| **NÃO GRAVE** | 60 dias | 120 dias |

### 11.2. Conteúdo da Notificação

Usar **FORM-004 (Notificação ANVISA)** para preparar a notificação. Incluir obrigatoriamente:

1. **Resumo do Incidente** (1 parágrafo)
   - O que aconteceu?
   - Quando e onde?
   - Quem foi afetado? (paciente: iniciais, idade, sexo - sem identificação completa por LGPD)
   - Qual foi o desfecho?

2. **Causa Raiz Identificada** (Seção 5 do relatório de investigação)
   - Descrição clara e específica da causa raiz
   - Metodologia usada (5 Whys, Ishikawa, etc.)
   - Evidências que suportam a causa raiz

3. **Ações Corretivas Tomadas** (Seção 7 do relatório de investigação)
   - Ação imediata (0-7 dias): O que foi feito para mitigar risco imediatamente?
   - Ação de longo prazo (7-60 dias): O que foi feito para resolver definitivamente?
   - Ação preventiva: O que foi feito para prevenir casos similares?

4. **Status Atual da Implementação**
   - Cada ação: Status (Concluída / Em andamento / Planejada)
   - Evidências de implementação (resumo)

5. **Timeline de Correção**
   - Data de início: Quando ação corretiva foi iniciada?
   - Data de conclusão: Quando foi concluída? (ou previsão se ainda em andamento)
   - Verificação de eficácia: Data de validação de eficácia

6. **Medidas Preventivas**
   - O que foi feito para garantir que problema não recorra?
   - Controles implementados (técnicos, administrativos)
   - Atualização de gestão de risco (RMP-001)

7. **Impacto Estimado**
   - Número de dispositivos afetados
   - Número de pacientes potencialmente afetados
   - Distribuição geográfica (onde o produto foi vendido/usado)

8. **Necessidade de Ação de Campo (Field Safety Corrective Action - FSCA)**
   - Recall (recolhimento de produto)?
   - Field Safety Notice (comunicação aos usuários)?
   - Atualização de software mandatória?

### 11.3. Submissão ao Portal NOTIVISA

**URL:** https://www.gov.br/anvisa/pt-br/assuntos/fiscalizacao/notivisa

**Requisitos:**
- Cadastro prévio da empresa (CNPJ, razão social, endereço)
- Cadastro do Responsável Técnico (RT) com registro profissional
- Login com certificado digital (e-CPF ou e-CNPJ) ou senha

**Processo de Submissão:**

1. **Acessar portal NOTIVISA** e fazer login

2. **Preencher formulário online:**
   - Tipo de notificação: Tecnovigilância
   - Dispositivo médico: HemoDoctor (informar registro ANVISA se já tiver)
   - Dados do incidente: Conforme FORM-004

3. **Upload de documentos** (formato PDF):
   - Relatório de investigação completo (Seção 6)
   - Evidências principais (screenshots, logs - anonimizados)
   - Certificado de implementação de ações corretivas
   - Atualização do RMP (se aplicável)

4. **Aguardar protocolo ANVISA:**
   - Sistema gera número de protocolo
   - Salvar número de protocolo (ex: 25280.123456/2025-78)
   - Registrar no banco de dados de incidentes

5. **Follow-up:**
   - ANVISA pode solicitar informações adicionais (prazo: 15 dias para responder)
   - Acompanhar status da notificação no portal
   - Informar ANVISA quando ações corretivas forem concluídas e validadas

### 11.4. Comunicação com ANVISA

**Responsáveis:**
- RT (Responsável Técnico): Interlocutor principal com ANVISA
- Gerente de Qualidade: Suporte técnico
- Assuntos Regulatórios: Prepara documentação

**Registro:**
- Todas as comunicações com ANVISA devem ser registradas (emails, ofícios, ligações telefônicas)
- Arquivo: `Incidentes/2025/INC-2025-XXX/Correspondencia_ANVISA/`

**Prazos:**
- Responder solicitações ANVISA em **15 dias** (ou prazo especificado pela agência)
- Informar conclusão de ações corretivas assim que disponível
- Submeter relatório final de investigação em **60 dias** (eventos GRAVES) ou **120 dias** (NÃO GRAVES)

---

## ANEXOS

### Anexo A: Questionário Estruturado para Entrevista com Usuário

**Incidente:** INC-YYYY-XXX
**Entrevistado:** [Nome completo] - [Função]
**Data da Entrevista:** DD/MM/YYYY
**Entrevistador:** [Nome do investigador]
**Duração:** ___ minutos

---

**SEÇÃO 1: CONTEXTO DO USO**

1. Você já havia utilizado o sistema HemoDoctor antes deste incidente?
   - ☐ Sim, uso regularmente (____ vezes/mês)
   - ☐ Sim, uso ocasionalmente (____ vezes/ano)
   - ☐ Não, esta foi a primeira vez

2. Você recebeu treinamento sobre o sistema?
   - ☐ Sim, treinamento completo (data: ___/___/___)
   - ☐ Sim, treinamento básico
   - ☐ Não, aprendi sozinho(a)
   - ☐ Não lembro

3. Qual era o contexto clínico no momento do incidente?
   - ☐ Emergência (risco de vida imediato)
   - ☐ Urgência (necessário diagnóstico rápido)
   - ☐ Eletivo (rotina, sem pressão de tempo)

---

**SEÇÃO 2: DESCRIÇÃO DO INCIDENTE**

4. O que você esperava que o sistema fizesse?
   - [Resposta aberta, mínimo 50 palavras]

5. O que o sistema realmente fez? (descreva exatamente o que aconteceu)
   - [Resposta aberta, mínimo 100 palavras]

6. Houve alguma mensagem de erro ou alerta exibido?
   - ☐ Não, nenhuma mensagem
   - ☐ Sim, descreva: __________________________________

7. O que você fez imediatamente após perceber o problema?
   - [Resposta aberta]

---

**SEÇÃO 3: RESULTADO E IMPACTO**

8. Qual ação clínica você tomou com base na sugestão do sistema?
   - ☐ Segui a sugestão completamente
   - ☐ Segui a sugestão parcialmente
   - ☐ Não segui a sugestão (por quê? _________________)

9. Qual foi o diagnóstico final do paciente?
   - [Resposta: diagnóstico confirmado por exames]

10. O diagnóstico final foi:
    - ☐ Igual à sugestão do sistema (sistema acertou)
    - ☐ Diferente da sugestão do sistema (sistema errou)

11. Houve algum impacto no paciente devido ao incidente?
    - ☐ Não, nenhum impacto
    - ☐ Sim, exames adicionais necessários
    - ☐ Sim, atraso no tratamento correto
    - ☐ Sim, tratamento incorreto iniciado (especificar: ______)
    - ☐ Sim, dano ao paciente (especificar: _____________)

---

**SEÇÃO 4: PERCEPÇÃO E SUGESTÕES**

12. Você percebeu algum problema com o sistema no momento do uso?
    - ☐ Não, não percebi nada de errado
    - ☐ Sim, percebi mas continuei usando (por quê? ______)
    - ☐ Sim, percebi e parei de usar imediatamente

13. Em sua opinião, o que causou o incidente?
    - [Resposta aberta]

14. O que poderia ter prevenido este incidente?
    - [Resposta aberta - sugestões do usuário são valiosas!]

15. Você continuaria usando o sistema após este incidente?
    - ☐ Sim, sem ressalvas
    - ☐ Sim, mas com mais cautela
    - ☐ Não, perdi a confiança
    - ☐ Somente se [condição: ___________________]

---

**Assinatura do Entrevistado:**
_____________________________________ Data: ___/___/___

**Assinatura do Entrevistador:**
_____________________________________ Data: ___/___/___

---

### Anexo B: Checklist de Evidências Obrigatórias

Marcar "✓" quando evidência foi coletada:

**Evidências Técnicas:**
- [ ] Logs de sistema (completos, período relevante)
- [ ] Dados de entrada (CBC inserido pelo usuário)
- [ ] Output do sistema (sugestão, confidence score, alertas)
- [ ] Screenshots da interface (tela no momento do incidente)
- [ ] Versão de software (código fonte, commit hash, release)
- [ ] Ambiente técnico (browser, OS, dispositivo)
- [ ] Histórico de performance (sistema estava lento? timeout?)

**Evidências Clínicas:**
- [ ] Entrevista com usuário (Anexo A preenchido)
- [ ] Prontuário médico (cópia anonimizada, com consentimento)
- [ ] Diagnóstico final confirmado (exame padrão-ouro)
- [ ] Contexto clínico (comorbidades, urgência, tratamento prévio)
- [ ] Desfecho clínico (evolução do paciente)

**Evidências Documentais:**
- [ ] Relatório de incidente (FORM-001)
- [ ] Documentação de requisitos (SRS-001)
- [ ] Plano de testes (TST-001)
- [ ] Instruções de Uso (IFU)
- [ ] Gestão de Risco (RMP-001)
- [ ] Registro de treinamento (usuário foi treinado?)

**Evidências Adicionais (se aplicável):**
- [ ] Análise de banco de dados (casos similares)
- [ ] Comunicação com fornecedor (se problema de integração)
- [ ] Relatórios de auditoria (se incidente foi encontrado em auditoria)

---

### Anexo C: Glossário de Termos

**5 Whys:** Metodologia de análise de causa raiz que consiste em perguntar "por quê" cinco vezes sucessivamente até chegar à causa fundamental.

**CAPA:** Corrective and Preventive Actions (Ações Corretivas e Preventivas) - Sistema de gestão de qualidade para eliminar causas de problemas e prevenir recorrência.

**Causa Raiz:** Razão fundamental identificável que, se eliminada, previne recorrência do problema.

**Confidence Score:** Nível de confiança do modelo de Machine Learning na sugestão diagnóstica (0-100%).

**Edge Case:** Caso extremo ou atípico, fora do esperado, que pode não ser adequadamente tratado pelo sistema.

**Field Safety Corrective Action (FSCA):** Ação de campo para correção de segurança, pode incluir recall, atualização de software ou comunicação aos usuários.

**Field Safety Notice (FSN):** Comunicação urgente aos usuários sobre problema de segurança identificado.

**Incidente:** Qualquer evento adverso relacionado ao dispositivo médico.

**Ishikawa:** Diagrama de causa e efeito (espinha de peixe) que analisa problema sob 6 categorias (6M: Método, Máquina, Material, Mão de obra, Medida, Meio ambiente).

**Near Miss:** Quase-acidente, evento que poderia ter causado dano mas não causou (por sorte ou intervenção).

**NOTIVISA:** Portal da ANVISA para notificação de eventos adversos relacionados a produtos de saúde.

**RCA:** Root Cause Analysis (Análise de Causa Raiz).

**Risco Residual:** Risco que permanece após implementação de controles de mitigação.

**RMP:** Risk Management Plan (Plano de Gestão de Risco).

**RT:** Responsável Técnico (profissional registrado que responde tecnicamente pela empresa perante ANVISA).

**Severidade:** Gravidade do dano potencial ou real ao paciente.

**SLA:** Service Level Agreement (Acordo de Nível de Serviço) - Prazo comprometido para conclusão de tarefa.

---

## CONTROLE DE VERSÕES

| Versão | Data | Autor | Descrição de Mudanças | Aprovador |
|--------|------|-------|------------------------|-----------|
| 1.0 | 2025-10-12 | Risk Management Specialist | Versão inicial do procedimento de investigação de eventos adversos. Metodologia RCA completa (5 Whys + Ishikawa + Análise de Falha), 3 fases de investigação (30 dias), template de relatório, integração com PROC-001/003, exemplos práticos de healthcare AI/ML. | Gerente de Qualidade + RT |

---

## APROVAÇÕES

**Elaborado por:**
- Nome: Risk Management Specialist
- Data: 12/10/2025
- Assinatura: _____________________

**Revisado por:**
- Nome: Gerente de Qualidade
- Data: ___/___/_____
- Assinatura: _____________________

**Aprovado por:**
- Nome: Responsável Técnico (RT)
- Data: ___/___/_____
- Assinatura: _____________________

---

**NOTA IMPORTANTE:**
Este procedimento é parte integrante do Sistema de Gestão da Qualidade (SGQ) da organização e deve ser seguido por todos os envolvidos em investigação de incidentes. O não cumprimento deste procedimento pode resultar em não-conformidades regulatórias, risco à segurança do paciente e responsabilidade legal.

---

**FIM DO DOCUMENTO**

Arquivo: `PROC-002_Procedimento_Investigacao_Eventos_v1.0_OFICIAL.md`
Localização: `AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/`
Status: OFICIAL
Versão: 1.0
Data: 2025-10-12
