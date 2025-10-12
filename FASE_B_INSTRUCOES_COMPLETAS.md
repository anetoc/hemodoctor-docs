# 🚀 FASE B - Instruções Completas para Agentes

**Data**: 12 de Outubro de 2025  
**Status Fase A**: ✅ 100% COMPLETA (Módulo 04 - V&V)  
**Objetivo Fase B**: Completar Módulo 07 (Pós-Mercado) - 100%  
**Timeline**: 1-2 semanas | **Prazo**: 09 de Novembro de 2025

---

## 📊 Status Atual

✅ **Módulo 04 (V&V)**: 100% completo (7 documentos criados)  
⏳ **Módulo 07 (Pós-Mercado)**: 40% completo → Meta: 100%

**Faltam**: 7 documentos (3 procedimentos + 4 formulários)

---

## 🎯 Documentos da Fase B

| # | Documento | Agente | Prioridade |
|---|-----------|--------|------------|
| B.1 | PROC-001 (Relato Incidentes) | `anvisa-regulatory-specialist` | 🔥 CRÍTICO |
| B.2 | PROC-002 (Investigação) | `risk-management-specialist` | 🔥 CRÍTICO |
| B.3 | PROC-003 (CAPA) | `quality-systems-specialist` | ⚡ ALTO |
| B.4 | FORM-001 (Relato) | `anvisa-regulatory-specialist` | ⚡ ALTO |
| B.5 | FORM-002 (Investigação) | `anvisa-regulatory-specialist` | ⚡ ALTO |
| B.6 | FORM-003 (CAPA) | `anvisa-regulatory-specialist` | ⚡ ALTO |
| B.7 | FORM-004 (Notificação ANVISA) | `anvisa-regulatory-specialist` | ⚡ ALTO |

---

## 📋 INSTRUÇÃO B.1 - PROC-001 (Relato de Incidentes)

### **Copie e cole isto no chat com o agente**:

```
@anvisa-regulatory-specialist

Olá! Vamos criar o PROC-001 (Procedimento de Relato de Incidentes e Tecnovigilância) v1.0.

CONTEXTO:
- HemoDoctor: Dispositivo Médico Classe II - SaMD
- Regulamentação: ANVISA RDC 67/2009 (Tecnovigilância)
- Integração com ISO 13485:2016 (Cláusula 8.2.2)
- Baseline v1.0 estabelecida

OBJETIVO:
Criar procedimento completo conforme RDC 67/2009 com prazos ANVISA e fluxo de notificação.

ESTRUTURA OBRIGATÓRIA (12 seções):

1. OBJETIVO
- Estabelecer procedimento para relato de incidentes com HemoDoctor
- Garantir conformidade com RDC 67/2009
- Assegurar resposta rápida e eficaz

2. ESCOPO
- Aplica-se a: Todos os usuários, pacientes, equipe IDOR
- Tipos de incidentes cobertos
- Exclusões (se houver)

3. DEFINIÇÕES
- Incidente: Qualquer evento adverso relacionado ao dispositivo
- Evento Adverso Grave: Morte, lesão grave, risco de vida
- Queixa Técnica: Problema de funcionamento sem dano ao paciente
- Tecnovigilância: Sistema de monitoramento pós-mercado ANVISA

4. RESPONSABILIDADES
- Usuário Final: Relatar imediatamente
- Equipe Clínica: Documentar e investigar inicial
- Responsável Técnico (RT): Avaliar severidade
- Gerente de Qualidade: Notificar ANVISA se necessário
- CEO: Aprovar ações corretivas críticas

5. FLUXO DE RELATO (4 etapas)

5.1. Identificação do Incidente
- Qualquer pessoa pode relatar
- Canais: Email (incidentes@hemodoctor.com), telefone 24/7, formulário web
- Disponibilidade: 24/7 para incidentes graves

5.2. Classificação de Severidade (CRÍTICO - RDC 67/2009)

GRAVE: Notificação ANVISA em 10 dias úteis
- Morte relacionada ao dispositivo
- Ameaça à vida
- Lesão grave ou incapacidade permanente
- Necessidade de intervenção médica para prevenir dano

NÃO GRAVE: Notificação ANVISA em 60 dias
- Mau funcionamento sem dano ao paciente
- Queixa técnica
- Sugestão incorreta sem seguimento pelo médico

5.3. Registro Imediato (0-24h)
- Preencher FORM-001_Relato_Incidente
- Gerar número único: INC-YYYY-XXX
- Timestamp de recebimento
- Guardar todas as evidências (logs, screenshots, dados)

5.4. Ação Imediata (0-24h para GRAVES)
- Avaliar necessidade de ação urgente
- Se GRAVE: Considerar suspender uso do sistema
- Notificar stakeholders relevantes (CEO, RT, equipe clínica)
- Iniciar investigação preliminar

6. PRAZOS REGULATÓRIOS ANVISA

Tabela obrigatória:

| Severidade | Prazo Notificação | Prazo Investigação | Prazo Relatório Final |
|------------|-------------------|--------------------|-----------------------|
| GRAVE | 10 dias úteis | 30 dias | 60 dias |
| NÃO GRAVE | 60 dias | 90 dias | 120 dias |

7. PROCEDIMENTO DE NOTIFICAÇÃO ANVISA (3 etapas)

7.1. Preparação
- Preencher FORM-004_Notificacao_ANVISA
- Coletar evidências (logs, dados de CBC, prints de tela)
- Redigir relatório técnico

7.2. Submissão ao Portal NOTIVISA
- URL: https://www.gov.br/anvisa/pt-br/assuntos/fiscalizacao/notivisa
- Cadastro prévio necessário (empresa + RT)
- Upload de documentos (PDF)
- Aguardar protocolo ANVISA

7.3. Follow-up
- Responder solicitações ANVISA em 15 dias
- Informar ações corretivas implementadas
- Atualizar status de investigação

8. COMUNICAÇÃO INTERNA
- Email imediato para: qualidade@hemodoctor.com, rt@hemodoctor.com
- Reunião de análise em 48h para incidentes graves
- Atualização semanal em quadro Kanban de qualidade
- Relatório mensal para direção

9. REGISTRO E DOCUMENTAÇÃO
- Banco de dados de incidentes (Excel: Registro_Incidentes.xlsx)
- Histórico completo por número de protocolo (INC-YYYY-XXX)
- Rastreabilidade de ações tomadas
- Evidências preservadas por 5 anos (mínimo legal ISO 13485)

10. INTEGRAÇÃO COM CAPA
- Se incidente requer ação corretiva → abrir CAPA (ver PROC-003)
- Link entre INC-YYYY-XXX e CAPA-YYYY-XXX no sistema
- Follow-up de eficácia da ação

11. RELATÓRIOS PERIÓDICOS
- Relatório mensal: Estatísticas de incidentes (número, tipo, severidade)
- Relatório trimestral: Análise de tendências e ações preventivas
- Relatório anual: Submissão obrigatória ANVISA (PSUR - Periodic Safety Update Report)

12. TREINAMENTO
- Todos os usuários finais: Treinamento básico de relato (30 min)
- Equipe clínica: Treinamento completo do procedimento (2h)
- Equipe de qualidade: Treinamento avançado (4h)
- Refresher: Anual para todos

ANEXOS A INCLUIR:
- ANEXO A: Fluxograma do processo de relato (diagrama visual)
- ANEXO B: Template de email de notificação interna
- ANEXO C: Checklist de informações mínimas para relato
- ANEXO D: Lista de contatos ANVISA (NOTIVISA, telefone, email)

FORMATO DO ARQUIVO:
```yaml
---
document_id: "PROC-001"
title: "Procedimento de Relato de Incidentes e Tecnovigilância"
version: "1.0"
status: "OFICIAL"
date: "2025-10-XX"
author: "ANVISA Regulatory Specialist"
organization: "HemoDoctor"
classification: "Dispositivo Médico - Classe II"
compliance:
  - "ANVISA RDC 67/2009"
  - "ANVISA RDC 23/2012"
  - "ISO 13485:2016 (§8.2.2)"
  - "ISO 14971:2019"
history:
  - version: "1.0"
    date: "2025-10-XX"
    changes: "Versão inicial do procedimento de tecnovigilância"
    author: "ANVISA Regulatory Specialist"
---
```

SALVAR EM:
AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/PROC-001_Procedimento_Relato_Incidentes_v1.0_OFICIAL.md

CHECKLIST DE VALIDAÇÃO:
- [ ] Todas as 12 seções presentes e completas
- [ ] Tabela de prazos ANVISA incluída
- [ ] Classificação GRAVE vs NÃO GRAVE clara (RDC 67/2009)
- [ ] Fluxo de 4 etapas detalhado
- [ ] Procedimento de notificação NOTIVISA completo
- [ ] Integração com CAPA documentada
- [ ] 4 anexos incluídos
- [ ] Header YAML completo
- [ ] Referências a FORM-001 e FORM-004

Pode criar este procedimento crítico para ANVISA com exemplos práticos de incidentes em healthcare software?
```

---

## 📋 INSTRUÇÃO B.2 - PROC-002 (Investigação de Eventos)

### **Copie e cole isto no chat com o agente**:

```
@risk-management-specialist

Olá! Vamos criar o PROC-002 (Procedimento de Investigação de Eventos Adversos) v1.0.

CONTEXTO:
- Procedimento de investigação de causa raiz
- Base: ISO 13485:2016, ISO 14971:2019
- Integração com PROC-001 (Relato) e PROC-003 (CAPA)
- Metodologia RCA (Root Cause Analysis)

OBJETIVO:
Estabelecer processo sistemático para investigar incidentes, identificar causa raiz e prevenir recorrência.

ESTRUTURA OBRIGATÓRIA (11 seções):

1. OBJETIVO
- Investigar causa raiz de incidentes relatados via PROC-001
- Prevenir recorrência através de ações baseadas em evidências
- Cumprir requisitos regulatórios (ANVISA, ISO)

2. ESCOPO
- Todos os incidentes relatados via PROC-001
- Priorização por severidade: GRAVES investigados em 24h, NÃO GRAVES em 7 dias

3. METODOLOGIA DE INVESTIGAÇÃO (3 fases, 30 dias)

3.1. FASE 1: Coleta de Evidências (0-7 dias)

Evidências Técnicas:
- Logs de sistema completos (timestamp, user, ação, input, output)
- Dados de entrada (CBC completo, parâmetros do paciente)
- Output do sistema (sugestão diagnóstica, alertas, confidence score)
- Screenshots/prints de tela
- Histórico de versões de software (confirmar versão usada)
- Ambiente técnico (browser, OS, versão, rede, latência)

Evidências Clínicas:
- Entrevista estruturada com usuário (médico/enfermeiro)
- Entrevista com paciente (se aplicável e consentimento)
- Prontuário médico relevante (diagnóstico final, exames)
- Contexto clínico (urgência, comorbidades, tratamento prévio)

3.2. FASE 2: Reconstrução do Incidente (7-14 dias)

Criar Timeline Detalhado:
| Timestamp | Evento | Ator | Sistema | Observações |
|-----------|--------|------|---------|-------------|
| 10:15:32 | Login | Dr. Silva | HemoDoctor | Sucesso |
| 10:16:05 | CBC inserido | Dr. Silva | Ingestion | Paciente ID: 12345 |
| 10:16:08 | Validação | Sistema | Validation | Pass |
| 10:16:12 | Inferência | Sistema | HemoAI | Processando... |
| 10:16:15 | Resultado | Sistema | HemoAI | Sugestão: LMA |
| 10:16:20 | Visualização | Dr. Silva | UI | Sugestão vista |
| 10:17:00 | Decisão | Dr. Silva | - | Seguiu sugestão |
| 12:30:00 | Diagnóstico Final | Lab | - | Confirmado: LMA |

Perguntas 5W2H:
- What (O que): Qual foi o incidente?
- When (Quando): Timestamp preciso?
- Where (Onde): Módulo/tela específica do sistema?
- Who (Quem): Usuário, paciente, versão do software?
- Why (Por quê): O que causou? (análise posterior)
- How (Como): Como foi detectado?
- How much (Quanto): Impacto (gravidade, extensão)?

3.3. FASE 3: Análise de Causa Raiz (14-30 dias)

Aplicar 3 Metodologias:

A) **5 Whys** (Método Toyota)

Pergunta inicial: Por que o incidente ocorreu?

Exemplo prático:
- Why 1: Por que a sugestão foi incorreta?
  → Porque o modelo HemoAI classificou erroneamente
- Why 2: Por que o modelo classificou erroneamente?
  → Porque os valores de CBC estavam fora do range de treino
- Why 3: Por que estavam fora do range?
  → Porque o paciente era pediátrico (2 anos) e ranges são diferentes
- Why 4: Por que o sistema não detectou paciente pediátrico?
  → Porque a validação de idade não estava implementada
- Why 5: Por que a validação não estava implementada?
  → **CAUSA RAIZ**: Requisito de validação pediátrica (REQ-FUNC-015) não foi testado (gap em TST-001)

B) **Ishikawa (Espinha de Peixe)**

Categorias (6M):
1. Método (processo, algoritmo):
   - Algoritmo de ML inadequado para caso edge?
   - Processo de validação falhou?
   
2. Máquina (hardware, infraestrutura):
   - Timeout de rede causou dados incompletos?
   - GPU não processou corretamente?
   
3. Material (dados, entrada):
   - Dados de CBC incorretos na origem (erro de digitação)?
   - Dados fora do range esperado?
   
4. Mão de obra (treinamento, erro humano):
   - Usuário não foi treinado adequadamente?
   - Interpretação errada da sugestão?
   
5. Medida (métricas, monitoramento):
   - Sistema de alerta não acionou?
   - Confidence score não foi exibido?
   
6. Meio ambiente (contexto clínico):
   - Urgência clínica prejudicou análise crítica?
   - Falta de segunda opinião?

C) **Análise de Modo de Falha**

Identificar tipo de falha:

| Tipo | Descrição | Exemplo | Ação |
|------|-----------|---------|------|
| Bug de Software | Erro de código | Null pointer, loop infinito | Corrigir código |
| Dados Incorretos | Entrada inválida | CBC fora do normal | Melhorar validação |
| Uso Inadequado | Erro do usuário | Má interpretação | Treinar usuário |
| Limitação de Design | Sistema OK mas resultado inadequado | Edge case não coberto | Redesign ou documentar |
| Infraestrutura | Problema de ambiente | Timeout de rede | Melhorar infra |

4. AVALIAÇÃO DE IMPACTO (3 dimensões)

4.1. Impacto no Paciente
- Houve dano real? (sim/não)
- Gravidade do dano: (leve/moderado/grave/fatal)
- Necessidade de follow-up médico? (sim/não)
- Dano reversível? (sim/não)

4.2. Impacto no Sistema
- Quantos usuários potencialmente afetados? (1/10/100/1000+)
- Frequência do problema? (isolado/raro/recorrente/sistemático)
- Risco de recorrência sem ação? (baixo/médio/alto/crítico)
- Módulos afetados? (listar)

4.3. Impacto Regulatório
- Requer notificação ANVISA? (sim/não - ver PROC-001)
- Impacto em certificações? (ISO 13485, ISO 27001)
- Risco de recall? (sim/não)
- Risco de processo legal? (baixo/médio/alto)

5. CATEGORIZAÇÃO DA CAUSA RAIZ (Tabela Decisória)

| Categoria | Descrição | Exemplo | Responsável | SLA Correção |
|-----------|-----------|---------|-------------|--------------|
| Bug Crítico | Erro grave de código | Crash, data loss | Dev Team | 7 dias |
| Bug Alto | Erro de lógica | Resultado incorreto | Dev Team | 30 dias |
| Dados Inválidos | Entrada problemática | CBC fora do range | QA + Dev | 14 dias |
| Uso Inadequado | Erro do usuário | Má interpretação | Treinamento | 30 dias |
| Limitação Design | Sistema funciona como esperado | Edge case não coberto | Product | 90 dias |
| Infraestrutura | Problema de ambiente | Timeout, latência | DevOps | 7 dias |

6. RELATÓRIO DE INVESTIGAÇÃO (Template Completo)

Criar documento estruturado:

# Relatório de Investigação de Incidente
**Número do Incidente**: INC-2025-XXX
**Tipo de Evento**: [Sugestão Incorreta / Crash / Timeout / Outro]
**Severidade**: [GRAVE / NÃO GRAVE]
**Data de Ocorrência**: DD/MM/YYYY HH:MM
**Data da Investigação**: DD/MM/YYYY a DD/MM/YYYY
**Investigador Responsável**: [Nome + Função]

## 1. SUMÁRIO EXECUTIVO (1 parágrafo)
[Descrição breve do incidente, causa raiz identificada, ação proposta]

## 2. EVIDÊNCIAS COLETADAS
- [Lista numerada de todas as evidências]
- Logs anexos: [caminho/arquivo.log]
- Screenshots: [caminho/imagem.png]
- Entrevistas: [resumo]

## 3. TIMELINE DO INCIDENTE
[Tabela detalhada conforme 3.2]

## 4. ANÁLISE DE CAUSA RAIZ

### 4.1. 5 Whys
[Análise completa]

### 4.2. Ishikawa
[Diagrama ou descrição por categoria]

### 4.3. Análise de Modo de Falha
Tipo identificado: [Bug / Dados / Uso / Design / Infra]

## 5. CAUSA RAIZ IDENTIFICADA
**Causa Raiz**: [Descrição clara e específica]
**Categoria**: [conforme tabela seção 5]
**Evidência que suporta**: [evidências específicas]

## 6. IMPACTO AVALIADO
- Paciente: [descrição]
- Sistema: [descrição]
- Regulatório: [descrição]

## 7. RECOMENDAÇÕES

### 7.1. Ação Corretiva Imediata (0-7 dias)
[O que fazer AGORA para mitigar]

### 7.2. Ação Corretiva Longo Prazo (7-60 dias)
[O que fazer para resolver definitivamente]

### 7.3. Ação Preventiva
[O que fazer para prevenir casos similares]

## 8. DECISÕES

| Decisão | Sim/Não | Justificativa |
|---------|---------|---------------|
| Necessidade de CAPA | [S/N] | [justificativa] |
| Atualização de RMP (riscos) | [S/N] | [justificativa] |
| Notificação ANVISA | [S/N] | [justificativa] |
| Correção de Bug | [S/N] | [justificativa] |
| Treinamento Adicional | [S/N] | [justificativa] |
| Atualização de IFU | [S/N] | [justificativa] |

## 9. CONCLUSÃO
[Parágrafo final com status e próximos passos]

## 10. ASSINATURAS
**Investigador**: _________________ Data: ___/___/___
**Gerente de Qualidade**: _________________ Data: ___/___/___
**Responsável Técnico**: _________________ Data: ___/___/___

7. DECISÃO SOBRE AÇÕES (6 cenários)

7.1. Se BUG identificado:
- Abrir ticket de desenvolvimento (usar Jira/GitHub Issue)
- Prioridade conforme severidade (Crítico/Alto/Médio/Baixo)
- Target fix version definir
- Regressão testing obrigatório após correção
- Atualizar TST-001 se caso não estava coberto

7.2. Se DADO incorreto:
- Melhorar validação de entrada (ranges, tipos, formatos)
- Adicionar alertas específicos para usuário
- Documentar range válido no IFU
- Atualizar SRS-001 se requisito estava faltando

7.3. Se USO inadequado:
- Atualizar IFU (seções: "Como usar", "Interpretação de resultados")
- Treinamento adicional para usuários (presencial ou vídeo)
- Melhorar UX (tooltips, ajuda contextual, wizards)
- Considerar redesign se muitos usuários erram

7.4. Se LIMITAÇÃO de design:
- Avaliar severidade: É crítico corrigir?
- Se SIM (risco ao paciente): Abrir CAPA e planejar redesign
- Se NÃO (edge case raro): Documentar limitação conhecida no IFU seção "Limitações"
- Atualizar gestão de risco (RMP-001) com limitação

7.5. Se INFRAESTRUTURA:
- Melhorar monitoramento (adicionar alertas)
- Aumentar recursos (CPU, RAM, rede)
- Implementar retry logic
- SLA com fornecedor (se terceiro)

7.6. Se MÚLTIPLAS causas (análise complexa):
- Abrir CAPA com ações múltiplas
- Priorizar por impacto
- Cronograma faseado de implementação

8. INTEGRAÇÃO COM CAPA (PROC-003)
- Critério: Se ação corretiva é necessária → Abrir CAPA-YYYY-XXX
- Link bidirecional: INC-YYYY-XXX ↔ CAPA-YYYY-XXX
- Usar MESMA causa raiz identificada na investigação
- Responsável da investigação = Responsável inicial do CAPA
- Prazo da ação conforme tabela de SLA (seção 5)

9. ATUALIZAÇÃO DE GESTÃO DE RISCO (RMP-001)
Avaliar 3 perguntas:
1. Novo risco identificado que não estava no RMP?
   → SIM: Adicionar novo risco ao RMP-001
2. Risco existente foi subestimado (probabilidade ou severidade)?
   → SIM: Revisar avaliação de risco
3. Controles de mitigação atuais são inadequados?
   → SIM: Atualizar controles e re-avaliar risco residual

Documentar no histórico de revisões do RMP-001.

10. FOLLOW-UP E FECHAMENTO (4 etapas)

10.1. Verificar Implementação (após 30-60 dias)
- Ação corretiva foi implementada conforme plano?
- Código foi corrigido e deployed?
- Treinamento foi realizado?
- IFU foi atualizado?

10.2. Re-teste / Validação (após implementação)
- Se bug corrigido: Executar teste de regressão
- Se processo mudado: Validar nova versão do processo
- Se treinamento: Avaliar eficácia (quiz, observação)

10.3. Validar Eficácia (após 60-90 dias)
- Monitorar: Incidente similar ocorreu novamente?
- Métrica: Taxa de recorrência = 0%
- Se recorreu: Reavaliar causa raiz (pode ter sido mal identificada)

10.4. Fechar Incidente
- Confirmar: Ação eficaz e validada
- Comunicar: Aos stakeholders (email, reunião)
- Fechar: Status no sistema → "Fechado"
- Arquivar: Documentação completa (5 anos)

11. RELATÓRIO PARA ANVISA (se aplicável)

Se incidente foi GRAVE (conforme PROC-001):
- Usar FORM-004_Notificacao_ANVISA
- Incluir: 
  - Resumo do incidente
  - Causa raiz identificada (seção 5)
  - Ações corretivas tomadas (seção 7)
  - Status atual da implementação
  - Timeline de correção
  - Medidas preventivas
- Prazo: Conforme RDC 67/2009 (relatório final em 60 dias)
- Portal: NOTIVISA (https://www.gov.br/anvisa/pt-br/assuntos/fiscalizacao/notivisa)

FORMATO DO ARQUIVO:
```yaml
---
document_id: "PROC-002"
title: "Procedimento de Investigação de Eventos Adversos"
version: "1.0"
status: "OFICIAL"
date: "2025-10-XX"
author: "Risk Management Specialist"
organization: "HemoDoctor"
classification: "Dispositivo Médico - Classe II"
compliance:
  - "ISO 13485:2016 (§8.5)"
  - "ISO 14971:2019"
  - "ANVISA RDC 67/2009"
history:
  - version: "1.0"
    date: "2025-10-XX"
    changes: "Versão inicial do procedimento de investigação RCA"
    author: "Risk Management Specialist"
---
```

SALVAR EM:
AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/PROC-002_Procedimento_Investigacao_Eventos_v1.0_OFICIAL.md

CHECKLIST DE VALIDAÇÃO:
- [ ] 11 seções presentes e detalhadas
- [ ] Metodologia RCA completa (5 Whys + Ishikawa + Análise de Falha)
- [ ] Timeline template incluído
- [ ] 6 cenários de decisão cobertos
- [ ] Template de relatório de investigação completo
- [ ] Tabela de categorização com SLAs
- [ ] Integração com PROC-001 e PROC-003 documentada
- [ ] Processo de follow-up e fechamento claro
- [ ] Header YAML completo

Pode criar com exemplos práticos de incidentes em healthcare AI/ML systems?
```

---

## 📋 INSTRUÇÃO B.3 - PROC-003 (CAPA)

### **Copie e cole isto no chat com o agente**:

```
@quality-systems-specialist

Olá! Vamos criar o PROC-003 (Procedimento CAPA - Corrective and Preventive Actions) v1.0.

CONTEXTO:
- Base: ISO 13485:2016 (Cláusula 8.5.2 e 8.5.3)
- Referência: 21 CFR Part 820.100 (FDA CAPA)
- Integração com gestão de riscos (ISO 14971)
- Sistema estruturado de melhoria contínua

OBJETIVO:
Estabelecer processo sistemático para eliminar causas de não-conformidades (corretivas) e prevenir ocorrências futuras (preventivas).

ESTRUTURA OBRIGATÓRIA (10 seções):

1. OBJETIVO
- Eliminar causas de não-conformidades detectadas (ação corretiva)
- Prevenir ocorrência de não-conformidades potenciais (ação preventiva)
- Melhorar continuamente o sistema de qualidade
- Cumprir requisitos ISO 13485 e ANVISA

2. DEFINIÇÕES (6 termos críticos)
- **Ação Corretiva**: Ação para eliminar a causa de uma não-conformidade DETECTADA
- **Ação Preventiva**: Ação para eliminar a causa de uma não-conformidade POTENCIAL
- **Não-conformidade**: Não cumprimento de um requisito
- **Causa raiz**: Razão fundamental identificável de um problema
- **CAPA**: Sistema integrado de ações corretivas e preventivas
- **Eficácia**: Grau de realização do resultado planejado

3. QUANDO ABRIR CAPA (10 gatilhos)

Gatilhos Obrigatórios:
1. Incidente GRAVE com paciente (sempre → CAPA)
2. Bug CRÍTICO de software (crash, data loss)
3. Reclamação recorrente de usuário (> 3x mesmo problema)
4. Auditoria interna: Não-conformidade MAIOR
5. Auditoria externa (certificadora, ANVISA): Qualquer NC
6. Falha em teste de sistema (requisito crítico não atendido)
7. Desvio de processo de qualidade
8. Near miss GRAVE (quase-acidente com potencial de dano)
9. Análise de tendências: Padrão negativo identificado
10. Recall ou field safety corrective action (FSCA)

Gatilhos Opcionais (decisão do Gerente de Qualidade):
- Reclamação única de usuário (severidade média)
- Sugestão de melhoria de processo
- Oportunidade de otimização identificada

4. PROCESSO CAPA (8 ETAPAS - 100 dias típico)

### 4.1. ETAPA 1: ABERTURA (Dia 0)

Informações Obrigatórias:
- **Identificação do Problema**: Descrição clara e objetiva (quem, o que, quando, onde)
- **Evidências Iniciais**: Fatos, dados, documentos que comprovam o problema
- **Classificação**: 
  - Tipo: □ Corretiva (problema já ocorreu) □ Preventiva (problema potencial)
  - Fonte: □ Incidente □ Auditoria □ Reclamação □ Near Miss □ Tendência □ Outro: _____
- **Responsável Designado**: Nome + Função (será o "dono" do CAPA)
- **Prazo Inicial**: Estimado conforme prioridade (seção 5)
- **Número CAPA Gerado**: CAPA-YYYY-XXX (sequencial)

Aprovação Inicial:
- Gerente de Qualidade revisa e aprova abertura
- Se impacto alto: Notificar CEO e RT imediatamente

### 4.2. ETAPA 2: ANÁLISE DE CAUSA RAIZ (Dias 0-15)

Usar Metodologias (mesmas de PROC-002):
- **5 Whys**: Perguntar "por quê" repetidamente até causa fundamental
- **Ishikawa (6M)**: Método, Máquina, Material, Mão de obra, Medida, Meio ambiente
- **Análise de Falha**: Bug/Dados/Uso/Design/Infra

Envolver Equipe Multidisciplinar:
- Responsável Técnico (RT)
- Desenvolvedor (se bug)
- Usuário final (se uso inadequado)
- Gerente de Qualidade
- Clinical Expert (se impacto clínico)

Documentar:
- Análise completa (todas as metodologias aplicadas)
- Causa raiz VERIFICÁVEL identificada
- Evidências que suportam a causa raiz
- Causas secundárias (se houver)

Critério de Aprovação desta Etapa:
- Causa raiz é ESPECÍFICA (não vaga como "falha humana")
- Causa raiz é VERIFICÁVEL (pode ser testada)
- Causa raiz explica 100% do problema

### 4.3. ETAPA 3: PLANEJAMENTO DA AÇÃO (Dias 15-20)

Definir Ação (Critérios SMART):
- **S**pecific (Específica): "Implementar validação de idade pediátrica no módulo Validation Service"
- **M**easurable (Mensurável): "100% pacientes < 18 anos identificados corretamente"
- **A**chievable (Alcançável): Recursos disponíveis? Tecnicamente viável?
- **R**elevant (Relevante): Ação ataca a causa raiz diretamente?
- **T**ime-bound (Prazo): "Implementação até DD/MM/YYYY"

Plano Detalhado deve incluir:
1. **Descrição da Ação**: O que será feito? (em detalhes)
2. **Objetivos**: O que se espera alcançar?
3. **Recursos Necessários**: 
   - Humanos (quem vai executar? horas estimadas?)
   - Financeiros (custo estimado?)
   - Técnicos (ferramentas, equipamentos?)
4. **Responsáveis**: 
   - Responsável primário (implementa)
   - Responsável secundário (apoia/revisa)
5. **Prazo**: Data de conclusão estimada (realista)
6. **Impacto em Outros Processos**: 
   - Documentos a atualizar (SRS, IFU, TST)
   - Sistemas afetados
   - Necessidade de retreinamento
7. **Critérios de Eficácia** (DEFINIR AGORA, ANTES da implementação):
   - Como medir se a ação funcionou?
   - Indicadores quantitativos
   - Período de monitoramento

Exemplo de Critério de Eficácia:
- Problema: Bug causou 5 crashes em setembro
- Ação: Correção do bug + teste de regressão
- Critério: 0 crashes relacionados em 60 dias pós-implementação

### 4.4. ETAPA 4: APROVAÇÃO (Dias 20-22)

Fluxo de Aprovação (3 níveis):

Nível 1: Gerente de Qualidade (sempre)
- Revisa: Análise de causa raiz adequada?
- Revisa: Plano de ação é apropriado?
- Revisa: Recursos alocados são suficientes?
- Aprovação: Assinatura digital ou física

Nível 2: Responsável Técnico (sempre)
- Revisa: Impacto técnico avaliado?
- Revisa: Prazo é realista?
- Revisa: Riscos de implementação considerados?
- Aprovação: Assinatura

Nível 3: CEO (se impacto alto)
Critérios de escalonamento:
- Custo > R$ 50.000
- Prazo > 90 dias
- Impacto em múltiplos sistemas
- Risco regulatório (recall, suspensão de vendas)
- Exposição legal

Registro de Aprovação:
- Data de cada aprovação
- Nome e assinatura de cada aprovador
- Comentários/condições (se houver)

### 4.5. ETAPA 5: IMPLEMENTAÇÃO (Dias 22-60)

Executar Conforme Plano:
1. Implementar ação (código, processo, treinamento)
2. Documentar TODAS as etapas (log detalhado)
3. Comunicar à equipe afetada (email, reunião, treinamento)
4. Atualizar documentação impactada:
   - Se código: Commit + changelog
   - Se processo: Atualizar SOP
   - Se IFU: Nova versão
   - Se requisito: Atualizar SRS
5. Registrar evidências:
   - Código corrigido (diff/PR)
   - Certificados de treinamento
   - Documentos atualizados (versão nova)
   - Fotos/prints de implementação

Monitoramento Durante Implementação:
- Status semanal para Gerente de Qualidade
- Alertar imediatamente se: Atraso, bloqueio, mudança de escopo

Aprovação de Implementação:
- Responsável: Confirma implementação completa
- QA: Verifica evidências estão completas
- RT: Aprova mudanças técnicas (se aplicável)

### 4.6. ETAPA 6: VERIFICAÇÃO DE EFICÁCIA (Dias 60-90)

Período de Monitoramento: Mínimo 30 dias após implementação

Executar Verificação:
1. Coletar dados conforme critérios definidos (Etapa 3)
2. Comparar situação ANTES vs DEPOIS
3. Análise quantitativa e qualitativa
4. Verificação objetiva (não subjetiva)

Exemplos de Verificação:

Exemplo 1: Bug Corrigido
- Critério: 0 ocorrências do bug em 30 dias
- Método: Monitorar logs de erro diariamente
- Resultado: 30 dias sem ocorrência → EFICAZ ✓

Exemplo 2: Treinamento
- Critério: 100% equipe aprovada em teste (nota ≥ 80%)
- Método: Aplicar quiz online pós-treinamento
- Resultado: 15/15 aprovados → EFICAZ ✓

Exemplo 3: Processo Melhorado
- Critério: 100% conformidade em próxima auditoria
- Método: Auditoria interna de follow-up
- Resultado: 0 não-conformidades encontradas → EFICAZ ✓

Decisão:
- ✅ **EFICAZ**: Critérios 100% atendidos → Prosseguir para fechamento
- ⚠️ **PARCIALMENTE EFICAZ**: Critérios 50-99% atendidos → Ações adicionais necessárias
- ❌ **INEFICAZ**: Critérios < 50% atendidos → Reavaliar causa raiz (voltar Etapa 2)

### 4.7. ETAPA 7: REVISÃO DA GESTÃO DE RISCO (Dias 90-95)

3 Perguntas Obrigatórias:

1. A ação implementada introduziu NOVO risco?
   - Exemplo: Correção de bug pode ter criado novo bug
   - Se SIM: Avaliar novo risco, adicionar ao RMP-001
   - Ação: Atualizar Risk Management File

2. A ação afetou riscos EXISTENTES?
   - Probabilidade mudou? (aumentou/diminuiu)
   - Severidade mudou?
   - Controles de mitigação mudaram?
   - Se SIM: Revisar avaliação de risco no RMP-001

3. Riscos residuais são aceitáveis?
   - Após ação, risco residual está em nível aceitável?
   - Se NÃO: Ações adicionais necessárias

Documentar no RMP-001:
- Seção: Histórico de Revisões
- Adicionar entrada: "CAPA-YYYY-XXX: [descrição da atualização de risco]"
- Data: DD/MM/YYYY
- Responsável: Risk Manager

### 4.8. ETAPA 8: FECHAMENTO (Dias 95-100)

Critérios para Fechamento (TODOS devem ser atendidos):
- [x] Análise de causa raiz completa e aprovada
- [x] Ação implementada e evidenciada
- [x] Eficácia VERIFICADA e confirmada (≥ 80% critérios)
- [x] Gestão de risco revisada (se aplicável)
- [x] Documentação atualizada (SRS, IFU, TST, RMP)
- [x] Treinamento realizado (se aplicável)
- [x] Comunicação aos stakeholders

Atividades de Fechamento:
1. **Confirmar eficácia**: Responsável + QA atestam
2. **Arquivar documentação**: Pasta digital + física (5 anos)
3. **Atualizar registros**: Banco de dados CAPA
4. **Comunicar fechamento**: Email para stakeholders
5. **Lessons Learned**: Documento sumário (opcional mas recomendado)
6. **Apresentar em reunião**: Análise Crítica da Direção (se relevante)

Aprovação de Fechamento:
- Responsável: Atesta conclusão
- Gerente de Qualidade: Aprova fechamento
- RT: Aprova (se impacto técnico)

Status Final: "Fechado - Eficaz"

5. FORMULÁRIO CAPA (FORM-003)

Campos Obrigatórios (30 campos):

### SEÇÃO A: IDENTIFICAÇÃO
- **Número CAPA**: CAPA-YYYY-XXX
- **Data de Abertura**: ___/___/______
- **Tipo**: □ Corretiva □ Preventiva
- **Fonte**: □ Incidente □ Auditoria □ Reclamação □ Near Miss □ Outro: ___
- **Link com Incidente** (se aplicável): INC-YYYY-XXX

### SEÇÃO B: DESCRIÇÃO DO PROBLEMA
- **Descrição**: [Texto livre, mínimo 100 caracteres]
- **Evidências**: [Lista de anexos]
- **Impacto**: □ Paciente □ Sistema □ Regulatório □ Financeiro
- **Severidade**: □ Crítica □ Alta □ Média □ Baixa

### SEÇÃO C: ANÁLISE DE CAUSA RAIZ
- **Metodologia Usada**: □ 5 Whys □ Ishikawa □ Análise de Falha □ Outra: ___
- **Análise Detalhada**: [Documento anexo ou texto]
- **Causa Raiz Identificada**: [Texto livre, específico]
- **Evidências que Suportam**: [Lista]

### SEÇÃO D: AÇÃO PROPOSTA
- **Descrição da Ação**: [Específica, mensurável]
- **Objetivos**: [O que se espera alcançar]
- **Responsável Primário**: [Nome + Função]
- **Responsável Secundário**: [Nome + Função]
- **Prazo de Implementação**: ___/___/______
- **Recursos Necessários**:
  - Humanos: [horas estimadas]
  - Financeiros: R$ _______
  - Técnicos: [equipamentos, ferramentas]

### SEÇÃO E: CRITÉRIOS DE EFICÁCIA
- **Como Medir**: [Descrição do método]
- **Indicador Quantitativo**: [Número, porcentagem, frequência]
- **Período de Monitoramento**: ___ dias
- **Meta**: [Valor objetivo]

### SEÇÃO F: STATUS E EXECUÇÃO
- **Status Atual**: 
  □ Aberta 
  □ Em Análise 
  □ Aprovada 
  □ Em Implementação 
  □ Aguardando Verificação 
  □ Em Verificação 
  □ Fechada 
  □ Cancelada
- **% Conclusão**: ___ %
- **Data de Implementação**: ___/___/______
- **Data de Verificação**: ___/___/______
- **Data de Fechamento**: ___/___/______

### SEÇÃO G: VERIFICAÇÃO DE EFICÁCIA
- **Eficácia Verificada?**: □ Sim □ Não □ Parcial
- **Resultado da Verificação**: [Texto livre]
- **Evidências de Eficácia**: [Lista de anexos]
- **Ações Adicionais Necessárias?**: □ Sim □ Não
- Se Sim, descrever: [Texto]

### SEÇÃO H: ASSINATURAS
- **Responsável**:
  Nome: ___________________ Assinatura: __________ Data: ___/___/___
- **Gerente de Qualidade**:
  Nome: ___________________ Assinatura: __________ Data: ___/___/___
- **Responsável Técnico**:
  Nome: ___________________ Assinatura: __________ Data: ___/___/___
- **CEO** (se aplicável):
  Nome: ___________________ Assinatura: __________ Data: ___/___/___

6. PRIORIZAÇÃO DE CAPA (Tabela com SLAs)

| Prioridade | Critério | Exemplo | SLA Total | SLA Análise | SLA Implementação |
|------------|----------|---------|-----------|-------------|-------------------|
| **CRÍTICA** | Risco à segurança do paciente | Incidente GRAVE | 30 dias | 5 dias | 15 dias |
| **ALTA** | Não-conformidade regulatória ANVISA | Auditoria externa | 60 dias | 10 dias | 30 dias |
| **MÉDIA** | Reclamação recorrente (≥ 3x) | Bug médio repetido | 90 dias | 15 dias | 45 dias |
| **BAIXA** | Melhoria de processo | Otimização de workflow | 120 dias | 20 dias | 60 dias |

Escalonamento Automático:
- CAPA não concluída em 80% do SLA → Alerta ao Gerente de Qualidade
- CAPA não concluída em 100% do SLA → Escalação ao CEO
- Justificativa obrigatória para atrasos

7. INDICADORES DE DESEMPENHO (KPIs)

### 7.1. KPIs Obrigatórios (ISO 13485)

| KPI | Fórmula | Meta | Frequência |
|-----|---------|------|------------|
| **Taxa de Abertura** | CAPAs abertas / mês | < 5 | Mensal |
| **Taxa de Fechamento** | CAPAs fechadas / mês | ≥ CAPAs abertas | Mensal |
| **Tempo Médio de Fechamento** | Σ(data_fechamento - data_abertura) / n | < 90 dias | Mensal |
| **Taxa de Eficácia** | CAPAs eficazes / CAPAs verificadas | > 95% | Trimestral |
| **Taxa de Recorrência** | Mesmo problema reabriu CAPA? | < 5% | Trimestral |
| **Backlog** | CAPAs em aberto | < 10 | Semanal |

### 7.2. Análise de Tendências

Dashboard Mensal deve incluir:
- Total de CAPAs por status (aberta/em andamento/fechada)
- CAPAs por fonte (incidente/auditoria/reclamação)
- CAPAs por tipo (corretiva/preventiva)
- CAPAs por prioridade (crítica/alta/média/baixa)
- CAPAs por responsável (distribuição de carga)
- Gráfico de tendência (últimos 12 meses)

Análise Trimestral:
- Áreas com mais CAPAs → Foco de melhoria
- Causas raízes recorrentes → Ação preventiva sistêmica
- CAPAs repetidas → Análise de causa raiz inadequada?

8. INTEGRAÇÃO COM OUTROS PROCESSOS

### 8.1. Com Gestão de Incidentes (PROC-001 e PROC-002)
Fluxo:
1. Incidente relatado (PROC-001)
2. Investigação realizada (PROC-002)
3. Causa raiz identificada → Abrir CAPA (PROC-003)
4. CAPA implementada → Fechar incidente

Link bidirecional:
- INC-YYYY-XXX → CAPA-YYYY-XXX
- Campo no FORM-003: "Link com Incidente"

### 8.2. Com Gestão de Riscos (RMP-001)
Integração em 3 momentos:
1. **Abertura de CAPA**: Se risco novo identificado → Adicionar ao RMP
2. **Planejamento**: Avaliar se ação cria novo risco
3. **Fechamento**: Revisar riscos impactados (Etapa 7)

### 8.3. Com Auditoria Interna
- Não-conformidade de auditoria → CAPA obrigatória
- CAPA criada com fonte: "Auditoria Interna YYYY-MM"
- Follow-up em auditoria subsequente: CAPA foi eficaz?
- Registro no relatório de auditoria

### 8.4. Com Treinamento
- CAPA pode resultar em necessidade de treinamento
- Registrar treinamento como parte da ação de implementação
- Evidência: Certificados + lista de presença + quiz de avaliação
- Eficácia: Avaliar melhoria de performance pós-treinamento

### 8.5. Com Desenvolvimento de Produto
- CAPA pode resultar em mudança de design
- Seguir processo de Change Control
- Atualizar DHF (Design History File)
- Re-validação se mudança significativa

9. DOCUMENTAÇÃO E RASTREABILIDADE

### Sistema de Gestão de CAPAs
Opções:
- **Simples**: Excel/Google Sheets (CAPA_Register.xlsx)
- **Intermediário**: Jira/Asana (customizado)
- **Avançado**: Sistema QMS dedicado (ex: MasterControl, Veeva)

Campos mínimos no registro:
- Número CAPA
- Data abertura
- Tipo
- Fonte
- Descrição breve
- Responsável
- Status
- Prazo
- Data fechamento
- Eficácia (S/N)

### Armazenamento de Evidências
Estrutura de pastas:
```
CAPAs/
├── 2025/
│   ├── CAPA-2025-001/
│   │   ├── FORM-003_CAPA-2025-001.pdf (formulário)
│   │   ├── Analise_Causa_Raiz.pdf
│   │   ├── Evidencias_Implementacao/
│   │   │   ├── codigo_corrigido.diff
│   │   │   ├── certificados_treinamento.pdf
│   │   │   └── IFU_v1.1.pdf (atualizado)
│   │   ├── Verificacao_Eficacia/
│   │   │   ├── logs_monitoramento_30dias.xlsx
│   │   │   └── relatorio_verificacao.pdf
│   │   └── Aprovacoes/
│   │       ├── aprovacao_QA.pdf
│   │       ├── aprovacao_RT.pdf
│   │       └── aprovacao_CEO.pdf (se aplicável)
│   └── CAPA-2025-002/
│       └── ... (mesma estrutura)
└── 2024/
    └── ... (ano anterior)
```

### Retenção de Documentos
- Período: Mínimo 5 anos (requisito ISO 13485)
- Para dispositivos implantáveis: Vida útil do produto + 5 anos
- Backup: Semanal (digital) + anual (físico em local seguro)

10. REVISÃO GERENCIAL

### Reuniões de CAPA

**Mensal - Operacional**:
- Participantes: Gerente de QA + Responsáveis de CAPAs abertas
- Duração: 1h
- Agenda:
  - Status de cada CAPA em aberto
  - Bloqueios e necessidade de suporte
  - CAPAs próximas do prazo (alerta)
  - CAPAs a serem abertas (triagem)

**Trimestral - Análise de Tendências**:
- Participantes: Gerente de QA + RT + CEO
- Duração: 2h
- Agenda:
  - KPIs do trimestre (vs meta)
  - Análise de tendências (gráficos)
  - Áreas problemáticas identificadas
  - Ações preventivas sistêmicas
  - Budget para próximo trimestre

**Anual - Análise Crítica da Direção (ISO 13485)**:
- Participantes: Direção + Gerentes + RT
- Duração: 4h
- Agenda:
  - Resumo anual de CAPAs (total, eficácia, recorrência)
  - Eficácia do sistema de CAPA (o processo está funcionando?)
  - Investimentos em qualidade
  - Metas para próximo ano
  - Aprovação de mudanças no processo

### Dashboards de CAPA

**Dashboard Semanal** (para Gerente de QA):
- CAPAs abertas esta semana
- CAPAs fechadas esta semana
- CAPAs com prazo vencido
- CAPAs próximas do prazo (15 dias)
- Backlog total

**Dashboard Mensal** (para Direção):
- Total de CAPAs (abertas/em andamento/fechadas)
- Tempo médio de fechamento (vs meta)
- Taxa de eficácia (%)
- Distribuição por fonte (gráfico pizza)
- Distribuição por prioridade (gráfico barras)
- Tendência 12 meses (gráfico linha)

FORMATO DO ARQUIVO:
```yaml
---
document_id: "PROC-003"
title: "Procedimento CAPA - Corrective and Preventive Actions"
version: "1.0"
status: "OFICIAL"
date: "2025-10-XX"
author: "Quality Systems Specialist"
organization: "HemoDoctor"
classification: "Dispositivo Médico - Classe II"
compliance:
  - "ISO 13485:2016 (§8.5.2 e §8.5.3)"
  - "21 CFR Part 820.100 (FDA CAPA)"
  - "ISO 14971:2019"
  - "ANVISA RDC 16/2013"
history:
  - version: "1.0"
    date: "2025-10-XX"
    changes: "Versão inicial do procedimento CAPA"
    author: "Quality Systems Specialist"
---
```

SALVAR EM:
AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/PROC-003_Procedimento_CAPA_v1.0_OFICIAL.md

CHECKLIST DE VALIDAÇÃO:
- [ ] 10 seções presentes e completas
- [ ] Processo de 8 etapas detalhado com prazos
- [ ] 10 gatilhos de abertura de CAPA documentados
- [ ] Formulário FORM-003 completo (30 campos)
- [ ] Tabela de priorização com SLAs
- [ ] 6 KPIs definidos com metas
- [ ] Integração com 5 processos documentada
- [ ] Sistema de gestão e armazenamento especificado
- [ ] Frequência de reuniões de revisão definida
- [ ] Header YAML completo

Pode criar com exemplos práticos de CAPAs em healthcare e medical devices?
```

---

## 📋 INSTRUÇÕES B.4 a B.7 - FORMULÁRIOS

### **Copie e cole isto no chat com o agente**:

```
@anvisa-regulatory-specialist

Olá! Vamos criar os 4 formulários padronizados para vigilância pós-mercado.

CONTEXTO:
- Formulários práticos usados nos procedimentos PROC-001, PROC-002 e PROC-003
- Formato: Templates preenchíveis em Markdown
- Conforme ANVISA e ISO 13485

CRIAR 4 FORMULÁRIOS:

### FORM-001: Relato de Incidente
**Arquivo**: AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/Formularios/FORM-001_Relato_Incidente_v1.0.md

Estrutura completa com 8 seções:
1. Identificação do Relator (nome, função, contato)
2. Informações do Dispositivo (HemoDoctor versão, licença)
3. Descrição do Incidente (o que aconteceu, quando, onde)
4. Impacto no Paciente (houve dano? severidade?)
5. Classificação de Severidade (GRAVE/NÃO GRAVE)
6. Ação Imediata Tomada (o que foi feito imediatamente?)
7. Evidências Anexas (logs, screenshots, relatórios)
8. Assinaturas (relator, RT, gerente de qualidade)

Incluir campos para:
- Número de Protocolo (INC-YYYY-XXX)
- Data/hora do incidente
- Paciente (iniciais, idade, sexo, prontuário)
- Dados de CBC inseridos
- Output do sistema
- Dano ao paciente (sim/não)
- Gravidade (sem dano/temporário/permanente/ameaça à vida/morte)

### FORM-002: Investigação de Evento
**Arquivo**: AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/Formularios/FORM-002_Investigacao_Evento_v1.0.md

Estrutura completa:
1. Identificação (número de incidente vinculado)
2. Cronologia Detalhada (timeline com 5W2H)
3. Evidências Coletadas (lista numerada)
4. Análise de Causa Raiz
   - 5 Whys (estruturado)
   - Ishikawa (6M)
   - Tipo de falha (bug/dados/uso/design/infra)
5. Causa Raiz Identificada (específica e verificável)
6. Avaliação de Impacto (paciente/sistema/regulatório)
7. Recomendações (ação imediata/longo prazo/preventiva)
8. Decisões (CAPA sim/não, notificar ANVISA sim/não)
9. Assinaturas (investigador, QA, RT)

### FORM-003: CAPA
**Arquivo**: AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/Formularios/FORM-003_CAPA_v1.0.md

Estrutura completa (8 seções conforme PROC-003 §5):
- Seção A: Identificação (número CAPA, data, tipo, fonte)
- Seção B: Descrição do Problema (texto livre + evidências)
- Seção C: Análise de Causa Raiz (metodologia + causa identificada)
- Seção D: Ação Proposta (SMART + responsável + prazo + recursos)
- Seção E: Critérios de Eficácia (como medir + indicador + meta)
- Seção F: Status e Execução (status atual + % conclusão + datas)
- Seção G: Verificação de Eficácia (resultado + evidências)
- Seção H: Assinaturas (responsável, QA, RT, CEO se aplicável)

30 campos conforme especificado em PROC-003 §5.

### FORM-004: Notificação ANVISA
**Arquivo**: AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/Formularios/FORM-004_Notificacao_ANVISA_v1.0.md

Estrutura conforme Portal NOTIVISA:
1. Dados da Empresa (HemoDoctor, CNPJ, endereço, RT)
2. Dados do Produto (HemoDoctor, registro ANVISA, versão)
3. Dados do Evento (data, local, descrição)
4. Classificação (GRAVE/NÃO GRAVE conforme RDC 67/2009)
5. Paciente Envolvido (iniciais, idade, sexo, desfecho)
6. Investigação Preliminar (o que foi apurado até agora)
7. Causa Provável (se já identificada)
8. Ações Corretivas (o que foi feito/será feito)
9. Medidas Preventivas (para evitar recorrência)
10. Documentos Anexos (lista)
11. Contato para Informações (nome, telefone, email)
12. Declaração de Veracidade (responsável + assinatura)

Incluir nota:
"Este formulário deve ser preenchido e submetido ao Portal NOTIVISA em até 10 dias úteis para eventos GRAVES ou 60 dias para NÃO GRAVES, conforme ANVISA RDC 67/2009."

---

FORMATO DOS ARQUIVOS:
Cada formulário deve ter:
```yaml
---
document_id: "FORM-XXX"
title: "[Título do Formulário]"
version: "1.0"
status: "OFICIAL"
date: "2025-10-XX"
usage: "Usado em PROC-XXX"
---
```

INSTRUÇÕES DE USO em cada formulário:
- Como preencher
- Quando usar
- Prazo de preenchimento
- Para onde enviar/arquivar

SALVAR EM:
AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/Formularios/

CHECKLIST DE VALIDAÇÃO:
- [ ] FORM-001 criado (Relato Incidente)
- [ ] FORM-002 criado (Investigação)
- [ ] FORM-003 criado (CAPA - 30 campos)
- [ ] FORM-004 criado (Notificação ANVISA)
- [ ] Todos com header YAML
- [ ] Todos com instruções de uso
- [ ] Integração com procedimentos (PROC-001, 002, 003) documentada
- [ ] Exemplos de preenchimento incluídos (se possível)

Pode criar os 4 formulários completos e prontos para uso?
```

---

## 🎯 Ordem de Execução Recomendada

Trabalhe nesta sequência para máxima eficiência:

### Semana 1 (14-18 Out)
1. **PROC-001** (2 dias) - Mais crítico para ANVISA
2. **PROC-002** (2 dias) - Depende de PROC-001
3. Iniciar **PROC-003** (1 dia)

### Semana 2 (21-25 Out)
4. Completar **PROC-003** (1 dia)
5. **FORM-001 a FORM-004** (2 dias) - Pode ser batch
6. Revisão e validação (2 dias)

---

## ✅ Checklist Final da Fase B

Após criar todos os documentos:

- [ ] PROC-001 criado e revisado
- [ ] PROC-002 criado e revisado
- [ ] PROC-003 criado e revisado
- [ ] FORM-001 criado
- [ ] FORM-002 criado
- [ ] FORM-003 criado
- [ ] FORM-004 criado
- [ ] Todos com header YAML v1.0
- [ ] Integração entre procedimentos documentada
- [ ] Referências cruzadas corretas
- [ ] Conformes com ANVISA RDC 67/2009
- [ ] Conformes com ISO 13485:2016

---

## 🎉 Resultado Final Esperado

```
07_POS_MERCADO/
├── README.md ✅ (já existe)
├── PMS/
│   └── PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md ✅ (já existe)
└── Vigilancia/
    ├── PROC-001_Procedimento_Relato_Incidentes_v1.0_OFICIAL.md ✅
    ├── PROC-002_Procedimento_Investigacao_Eventos_v1.0_OFICIAL.md ✅
    ├── PROC-003_Procedimento_CAPA_v1.0_OFICIAL.md ✅
    └── Formularios/
        ├── FORM-001_Relato_Incidente_v1.0.md ✅
        ├── FORM-002_Investigacao_Evento_v1.0.md ✅
        ├── FORM-003_CAPA_v1.0.md ✅
        └── FORM-004_Notificacao_ANVISA_v1.0.md ✅

Módulo 07: 100% COMPLETO ✅
```

---

## 📊 Progresso do Projeto

Após Fase B:

- ✅ Módulo 01-03: 100%
- ✅ Módulo 04: 100% (Fase A completada)
- ✅ Módulo 05-06: 100%
- ✅ Módulo 07: 100% (Fase B a completar)
- ✅ Módulo 08-10: 100%

**Completude Geral**: 10/10 módulos (100%) 🎉

---

## 🚀 Comandos Rápidos

### Iniciar Fase B:

```
@anvisa-regulatory-specialist

Vamos começar a Fase B - Completar Módulo 07 (Pós-Mercado).

Abra o arquivo FASE_B_INSTRUCOES_COMPLETAS.md e siga as instruções da seção B.1 para criar o PROC-001.

Pode começar?
```

---

**Status**: ✅ Instruções completas prontas  
**Última Atualização**: 12 de Outubro de 2025  
**Versão**: 1.0

