---
document_id: "FORM-002"
title: "Formulário de Investigação de Evento Adverso"
version: "1.0"
status: "OFICIAL"
date: "2025-10-12"
usage: "Usado em PROC-002 (Procedimento de Investigação de Eventos Adversos)"
---

# FORM-002: Formulário de Investigação de Evento Adverso

**HemoDoctor - Dispositivo Médico Classe II (SaMD)**

---

## INSTRUÇÕES DE USO

**Quando usar:**
- Após receber FORM-001 (Relato de Incidente)
- Para investigar causa raiz de incidentes, reclamações, near misses
- Conforme PROC-002 (Procedimento de Investigação)

**Como preencher:**
- Coletar evidências técnicas e clínicas (Fase 1 - 0 a 7 dias)
- Reconstruir timeline do incidente (Fase 2 - 7 a 14 dias)
- Aplicar metodologias RCA (Fase 3 - 14 a 30 dias)
- Ser baseado em fatos e evidências (não especulações)

**Prazo de preenchimento:**
- **Incidentes GRAVES**: Investigação completa em 30 dias
- **Incidentes NÃO GRAVES**: Investigação completa em 90 dias

**Para onde enviar/arquivar:**
- Email: qualidade@hemodoctor.com com cópia para rt@hemodoctor.com
- Arquivo original: Pasta `Incidentes/YYYY/INC-YYYY-XXX/Investigacao/`
- Retenção: Mínimo 5 anos

---

## SEÇÃO 1: IDENTIFICAÇÃO

### 1.1. Número do Incidente Vinculado

**Incidente origem:**
**INC-________-______** (ver FORM-001)

**Data do incidente:**
___/___/______

**Classificação:**
☐ GRAVE ☐ NÃO GRAVE

### 1.2. Equipe de Investigação

**Investigador responsável:**
_____________________________________________________________________________
Função: _______________________________________________________________________

**Membros da equipe:**

1. ____________________________________________ Função: _____________________
2. ____________________________________________ Função: _____________________
3. ____________________________________________ Função: _____________________
4. ____________________________________________ Função: _____________________

**Especialidades representadas:**
☐ Responsável Técnico (RT)
☐ Desenvolvedor de software
☐ QA Engineer
☐ Hematologista (clinical expert)
☐ Data Scientist (ML)
☐ Usuário final (médico/enfermeiro)
☐ Gerente de Qualidade
☐ Outro: _____________________________________________________________________

### 1.3. Prazos

**Data de início da investigação:**
___/___/______

**Prazo de conclusão:**
___/___/______

**Data de conclusão real:**
___/___/______

---

## SEÇÃO 2: CRONOLOGIA DETALHADA (Timeline com 5W2H)

### 2.1. Timeline do Incidente

Reconstruir sequência de eventos com timestamps precisos:

| Timestamp | Evento | Ator | Sistema/Módulo | Observações |
|-----------|--------|------|----------------|-------------|
| ___:___ | _________________________ | __________ | _____________ | ______________ |
| ___:___ | _________________________ | __________ | _____________ | ______________ |
| ___:___ | _________________________ | __________ | _____________ | ______________ |
| ___:___ | _________________________ | __________ | _____________ | ______________ |
| ___:___ | _________________________ | __________ | _____________ | ______________ |
| ___:___ | _________________________ | __________ | _____________ | ______________ |
| ___:___ | _________________________ | __________ | _____________ | ______________ |
| ___:___ | _________________________ | __________ | _____________ | ______________ |

*(Adicionar linhas conforme necessário)*

### 2.2. Análise 5W2H

**What (O que)**: O que aconteceu exatamente?
_____________________________________________________________________________
_____________________________________________________________________________

**When (Quando)**: Timestamp preciso? Há padrão de horário/data?
_____________________________________________________________________________

**Where (Onde)**: Em qual módulo/tela do sistema? Qual ambiente (produção/staging)?
_____________________________________________________________________________

**Who (Quem)**: Usuário, paciente, versão do software, configuração?
_____________________________________________________________________________
_____________________________________________________________________________

**Why (Por quê)**: Por que o incidente ocorreu? (análise detalhada na Seção 4)
_____________________________________________________________________________

**How (Como)**: Como o problema foi detectado? Como se manifestou?
_____________________________________________________________________________
_____________________________________________________________________________

**How much (Quanto)**: Qual o impacto? Gravidade? Extensão?
_____________________________________________________________________________

---

## SEÇÃO 3: EVIDÊNCIAS COLETADAS

### 3.1. Evidências Técnicas

☐ **Logs de sistema completos**
   - Arquivo: _________________________________________________________________
   - Período: De ___/___/______ ___:___ até ___/___/______ ___:___
   - Observações: _____________________________________________________________

☐ **Dados de entrada (CBC completo)**
   - Arquivo: _________________________________________________________________
   - Valores: _________________________________________________________________

☐ **Output do sistema (sugestão diagnóstica)**
   - Sugestão: ________________________________________________________________
   - Confidence score: _________
   - Alertas: _________________________________________________________________

☐ **Screenshots/prints de tela**
   - Arquivo: _________________________________________________________________

☐ **Histórico de versões de software**
   - Versão em uso no momento do incidente: _________________________________
   - Última atualização: ___/___/______
   - Changelog relevante: _____________________________________________________

☐ **Ambiente técnico**
   - Browser: ____________________ Versão: ___________
   - Sistema Operacional: ________________________________________
   - Rede: ☐ Estável ☐ Instável (latência: _______ ms)
   - GPU/CPU: ☐ Normal ☐ Sobrecarga

☐ **Código-fonte relevante**
   - Módulo: __________________________________________________________________
   - Commit: __________________________________________________________________
   - Branch: __________________________________________________________________

### 3.2. Evidências Clínicas

☐ **Entrevista estruturada com usuário (médico/enfermeiro)**
   - Data da entrevista: ___/___/______
   - Duração: _______ minutos
   - Resumo: __________________________________________________________________
   ___________________________________________________________________________
   ___________________________________________________________________________

☐ **Entrevista com paciente** (se aplicável e com consentimento)
   - Data: ___/___/______ Consentimento obtido: ☐ Sim ☐ Não
   - Resumo: __________________________________________________________________
   ___________________________________________________________________________

☐ **Prontuário médico relevante**
   - Diagnóstico final: ________________________________________________________
   - Exames complementares: ____________________________________________________
   - Tratamento instituído: ____________________________________________________

☐ **Contexto clínico**
   - Urgência: ☐ Rotina ☐ Urgência ☐ Emergência
   - Comorbidades do paciente: ________________________________________________
   - Tratamento prévio: ________________________________________________________

### 3.3. Lista Completa de Evidências (Numerada)

1. _____________________________________________________________________________
2. _____________________________________________________________________________
3. _____________________________________________________________________________
4. _____________________________________________________________________________
5. _____________________________________________________________________________
6. _____________________________________________________________________________
7. _____________________________________________________________________________
8. _____________________________________________________________________________
9. _____________________________________________________________________________
10. ____________________________________________________________________________

**Pasta de armazenamento:**
_____________________________________________________________________________

---

## SEÇÃO 4: ANÁLISE DE CAUSA RAIZ

### 4.1. Metodologia Aplicada

Metodologias utilizadas (aplicar pelo menos 2):
☐ 5 Whys (Método Toyota)
☐ Ishikawa (Espinha de Peixe - 6M)
☐ Análise de Modo de Falha

---

### 4.2. Metodologia 1: 5 Whys

**Pergunta inicial:** Por que o incidente ocorreu?

**Why 1:** ____________________________________________________________________
**Resposta:** _________________________________________________________________
_____________________________________________________________________________

**Why 2:** ____________________________________________________________________
**Resposta:** _________________________________________________________________
_____________________________________________________________________________

**Why 3:** ____________________________________________________________________
**Resposta:** _________________________________________________________________
_____________________________________________________________________________

**Why 4:** ____________________________________________________________________
**Resposta:** _________________________________________________________________
_____________________________________________________________________________

**Why 5:** ____________________________________________________________________
**Resposta (CAUSA RAIZ):** ____________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

---

### 4.3. Metodologia 2: Ishikawa (Espinha de Peixe - 6M)

**Categorizar causas potenciais:**

**1. Método (processo, algoritmo):**
_____________________________________________________________________________
_____________________________________________________________________________

**2. Máquina (hardware, infraestrutura):**
_____________________________________________________________________________
_____________________________________________________________________________

**3. Material (dados, entrada):**
_____________________________________________________________________________
_____________________________________________________________________________

**4. Mão de obra (treinamento, erro humano):**
_____________________________________________________________________________
_____________________________________________________________________________

**5. Medida (métricas, monitoramento):**
_____________________________________________________________________________
_____________________________________________________________________________

**6. Meio ambiente (contexto clínico, condições externas):**
_____________________________________________________________________________
_____________________________________________________________________________

**Análise:** Qual categoria contribuiu mais para o incidente?
_____________________________________________________________________________
_____________________________________________________________________________

---

### 4.4. Metodologia 3: Análise de Modo de Falha

**Identificar tipo de falha:**

☐ **Bug de Software** (erro de código, lógica incorreta)
   - Descrição: ________________________________________________________________
   - Módulo/função afetada: ____________________________________________________
   - Severidade: ☐ Crítico ☐ Alto ☐ Médio ☐ Baixo

☐ **Dados Incorretos** (entrada inválida não tratada)
   - Tipo de dado: _____________________________________________________________
   - Validação faltante: _______________________________________________________

☐ **Uso Inadequado** (erro do usuário, má interpretação)
   - Tipo de erro: _____________________________________________________________
   - Gap de treinamento: _______________________________________________________

☐ **Limitação de Design** (sistema funciona como projetado, mas insuficiente)
   - Edge case não coberto: ____________________________________________________
   - Requisito faltante: _______________________________________________________

☐ **Infraestrutura** (problema de ambiente técnico)
   - Componente: _______________________________________________________________
   - Falha: ____________________________________________________________________

☐ **Outro:**
_____________________________________________________________________________

---

## SEÇÃO 5: CAUSA RAIZ IDENTIFICADA

### 5.1. Causa Raiz (Específica e Verificável)

**Causa Raiz Fundamental:**
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

### 5.2. Categoria da Causa Raiz

☐ Bug Crítico
☐ Bug Alto
☐ Dados Inválidos
☐ Uso Inadequado
☐ Limitação de Design
☐ Infraestrutura
☐ Outro: _____________________________________________________________________

### 5.3. Evidências que Suportam a Causa Raiz

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

### 5.4. Causas Secundárias (Fatores Contribuintes)

1. _____________________________________________________________________________
2. _____________________________________________________________________________
3. _____________________________________________________________________________

### 5.5. Verificação da Causa Raiz

**A causa raiz é:**
- ☐ **Específica** (não vaga como "falha humana" ou "erro de processo")
- ☐ **Verificável** (pode ser testada/comprovada com evidências)
- ☐ **Explica 100% do problema** (se eliminada, problema não recorre)
- ☐ **Eliminável** (é viável eliminar esta causa raiz)

---

## SEÇÃO 6: AVALIAÇÃO DE IMPACTO

### 6.1. Impacto no Paciente

**Houve dano real ao paciente?**
☐ Sim ☐ Não ☐ Potencial (near miss)

**Gravidade do dano:**
☐ Sem dano
☐ Leve (desconforto temporário)
☐ Moderado (dano temporário com necessidade de intervenção)
☐ Grave (dano permanente ou ameaça à vida)
☐ Fatal (morte)

**Necessidade de follow-up médico:**
☐ Sim ☐ Não
Descrição: ____________________________________________________________________

**Dano é reversível?**
☐ Sim ☐ Não ☐ Parcialmente

---

### 6.2. Impacto no Sistema

**Quantos usuários potencialmente afetados?**
☐ 1 (caso isolado)
☐ 2-10 (pequeno grupo)
☐ 11-100 (múltiplos usuários)
☐ > 100 (sistemático)

**Frequência do problema:**
☐ Isolado (ocorreu uma vez)
☐ Raro (< 1% de uso)
☐ Recorrente (1-10% de uso)
☐ Sistemático (> 10% de uso)

**Risco de recorrência sem ação:**
☐ Baixo (improvável acontecer novamente)
☐ Médio (pode acontecer novamente)
☐ Alto (provavelmente vai acontecer novamente)
☐ Crítico (vai acontecer novamente com certeza)

**Módulos do HemoDoctor afetados:**
_____________________________________________________________________________
_____________________________________________________________________________

---

### 6.3. Impacto Regulatório

**Requer notificação ANVISA?**
☐ Sim (conforme PROC-001) ☐ Não

**Impacto em certificações:**
☐ ISO 13485
☐ ISO 27001 (Segurança da Informação)
☐ Nenhum impacto

**Risco de recall?**
☐ Sim ☐ Não
Justificativa: _________________________________________________________________

**Risco de processo legal?**
☐ Baixo ☐ Médio ☐ Alto
Justificativa: _________________________________________________________________

---

## SEÇÃO 7: RECOMENDAÇÕES

### 7.1. Ação Corretiva Imediata (0-7 dias)

**O que fazer AGORA para mitigar:**
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

**Responsável:**
_____________________________________________________________________________

**Prazo:**
___/___/______

---

### 7.2. Ação Corretiva Longo Prazo (7-60 dias)

**O que fazer para resolver definitivamente:**
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

**Responsável:**
_____________________________________________________________________________

**Prazo:**
___/___/______

---

### 7.3. Ação Preventiva

**O que fazer para prevenir casos similares:**
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

**Responsável:**
_____________________________________________________________________________

**Prazo:**
___/___/______

---

## SEÇÃO 8: DECISÕES

### 8.1. Necessidade de CAPA

**Abrir CAPA (PROC-003)?**
☐ **SIM** (justificar abaixo)
☐ **NÃO** (justificar abaixo)

**Justificativa:**
_____________________________________________________________________________
_____________________________________________________________________________

**Se SIM, número do CAPA:**
**CAPA-________-______**

---

### 8.2. Atualização de Gestão de Risco (RMP-001)

**Atualizar RMP-001?**
☐ **SIM** (descrever mudanças)
☐ **NÃO**

**Mudanças necessárias:**
_____________________________________________________________________________
_____________________________________________________________________________

---

### 8.3. Notificação ANVISA

**Notificar ANVISA via NOTIVISA?**
☐ **SIM** (preencher FORM-004)
☐ **NÃO**

**Prazo:**
☐ 10 dias úteis (GRAVE)
☐ 60 dias (NÃO GRAVE)

---

### 8.4. Correção de Bug

**Correção de bug necessária?**
☐ **SIM**
☐ **NÃO**

**Se SIM, criar ticket:**
- Sistema: ☐ Jira ☐ GitHub Issues ☐ Outro: _________________________________
- Prioridade: ☐ Crítica ☐ Alta ☐ Média ☐ Baixa
- Target fix version: ________________________________________________________

---

### 8.5. Treinamento Adicional

**Treinamento necessário?**
☐ **SIM**
☐ **NÃO**

**Se SIM, público-alvo:**
_____________________________________________________________________________

**Conteúdo:**
_____________________________________________________________________________

---

### 8.6. Atualização de IFU

**Atualizar IFU (Instructions for Use)?**
☐ **SIM** (especificar seção)
☐ **NÃO**

**Seção a atualizar:**
_____________________________________________________________________________

**Mudança necessária:**
_____________________________________________________________________________

---

## SEÇÃO 9: ASSINATURAS

### 9.1. Investigador Responsável

Declaro que a investigação foi conduzida de forma imparcial, baseada em evidências, e que a análise de causa raiz está completa e verificável.

**Nome completo:**
_____________________________________________________________________________

**Assinatura:**
_______________________________________ **Data:** ___/___/______

---

### 9.2. Gerente de Qualidade

Declaro que revisei a investigação e aprovo as conclusões e recomendações.

**Nome completo:**
_____________________________________________________________________________

**Assinatura:**
_______________________________________ **Data:** ___/___/______

---

### 9.3. Responsável Técnico (RT)

Declaro que revisei os aspectos técnicos da investigação e aprovo as ações propostas.

**Nome completo:**
_____________________________________________________________________________

**Assinatura:**
_______________________________________ **Data:** ___/___/______

---

## EXEMPLO DE PREENCHIMENTO

**Cenário:** Investigação do INC-2025-008 (paciente pediátrico)

### Exemplo - Seção 4.2 (5 Whys)

- **Why 1:** Por que a sugestão foi incorreta?
  - **Resposta:** Porque o modelo HemoAI classificou erroneamente os valores de CBC.

- **Why 2:** Por que o modelo classificou erroneamente?
  - **Resposta:** Porque os valores de CBC estavam fora do range de treino do modelo.

- **Why 3:** Por que estavam fora do range?
  - **Resposta:** Porque o paciente era pediátrico (2 anos) e ranges são diferentes de adultos. Modelo treinado apenas com dados de adultos.

- **Why 4:** Por que o sistema não detectou paciente pediátrico?
  - **Resposta:** Porque não há validação de idade no módulo de validação de input.

- **Why 5:** Por que a validação não estava implementada?
  - **Resposta (CAUSA RAIZ):** Requisito REQ-FUNC-015 (validação de idade) estava especificado no SRS-001, mas não foi incluído no plano de testes TST-001. Gap de rastreabilidade entre requisitos e testes.

### Exemplo - Seção 5.1

**Causa Raiz:** "Gap de implementação do requisito REQ-FUNC-015 (validação de idade pediátrica) devido a falha de rastreabilidade entre SRS-001 e TST-001. Desenvolvedor não implementou o requisito e QA não detectou a omissão durante validação."

### Exemplo - Seção 8 (Decisões)

- Necessidade de CAPA: **SIM** - "Problema afeta segurança do paciente e requer ação corretiva estruturada."
- CAPA aberto: **CAPA-2025-012**
- Atualizar RMP-001: **SIM** - "Risco R12 (uso em população não validada) precisa ter probabilidade reduzida após implementação da validação."
- Notificar ANVISA: **NÃO** - "Classificado como NÃO GRAVE (near miss, médico não seguiu sugestão)."
- Correção de bug: **SIM** - "Implementar validação de idade conforme REQ-FUNC-015."
- Atualizar IFU: **SIM** - "Seção 'Limitações' deve documentar claramente que sistema é validado apenas para adultos 18-80 anos."

---

**FIM DO FORM-002**

---

*Documento controlado. Versão digital é a oficial. Cópias impressas devem ser verificadas antes do uso.*

*Retenção: 5 anos mínimo (ISO 13485:2016)*
