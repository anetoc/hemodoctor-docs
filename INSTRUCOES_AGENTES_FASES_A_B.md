# 🤖 Instruções para Agentes - Fases A e B

**Data**: 12 de Outubro de 2025  
**Responsável**: Dr. Abel Costa - IDOR-SP  
**Status**: Pronto para execução

---

## 📋 Índice Rápido

- [Fase A: Completar Módulo 04 (V&V)](#fase-a-completar-módulo-04-vv)
- [Fase B: Completar Módulo 07 (Pós-Mercado)](#fase-b-completar-módulo-07-pós-mercado)

---

## 🎯 FASE A: Completar Módulo 04 (V&V)

**Timeline**: 2-3 semanas  
**Prazo**: 02 de Novembro de 2025 (v2.2.0)  
**Prioridade**: ALTA (executar em paralelo com aguardo do CEP)

---

### 📌 A.1. VVP - Verification & Validation Plan (CRÍTICO)

#### **Agente**: `quality-systems-specialist`

#### **Instrução Completa**:

```
@quality-systems-specialist 

Olá! Preciso criar o VVP-001 (Verification & Validation Plan) v1.0 para o HemoDoctor.

CONTEXTO:
- Dispositivo Médico Classe II - SaMD
- Software de suporte à decisão clínica em hematologia
- Conforme IEC 62304 (Software de Dispositivo Médico)
- Baseline v1.0 já estabelecida

DOCUMENTOS BASE (para referência):
1. SRS-001 v1.0: AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/
   - Contém todos os requisitos funcionais e não-funcionais
2. SDD-001 v1.0: AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SDD/
   - Arquitetura e design do sistema
3. TST-001 v1.0: AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TST/
   - Especificação de testes já existente
4. TRC-001 v1.0: AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/
   - Matriz de rastreabilidade

ESTRUTURA OBRIGATÓRIA DO VVP-001:

1. INTRODUÇÃO
   - Propósito do documento
   - Escopo da verificação e validação
   - Referências (SRS, SDD, TST, IEC 62304, ISO 13485)
   - Definições e abreviações

2. ESTRATÉGIA GERAL DE V&V
   - Abordagem de V&V (baseada em risco - ISO 14971)
   - Classificação de segurança (Classe B conforme IEC 62304)
   - Critérios de aceitação gerais
   - Responsabilidades (equipe de QA, dev, clinical)

3. NÍVEIS DE TESTE
   3.1. Testes Unitários
       - Escopo e objetivos
       - Ferramentas (pytest, unittest)
       - Cobertura mínima: 80% de código
       - Responsável: Desenvolvedores
   
   3.2. Testes de Integração
       - Escopo: APIs, módulos, interfaces
       - Casos de teste de integração
       - Ambiente de teste
       - Responsável: QA
   
   3.3. Testes de Sistema
       - Escopo: Requisitos funcionais do SRS
       - End-to-end testing
       - Performance, segurança, usabilidade
       - Responsável: QA + Clinical
   
   3.4. Testes de Validação
       - Escopo: Ambiente clínico simulado
       - Dados reais anonimizados
       - Validação com usuários finais
       - Responsável: Clinical Team

4. AMBIENTE DE TESTE
   - Hardware necessário
   - Software (versões)
   - Dados de teste (fontes, anonimização)
   - Configurações de ambiente

5. CRITÉRIOS DE ACEITAÇÃO
   - Critérios de Pass/Fail por nível
   - Defeitos críticos: 0 tolerância
   - Defeitos altos: correção obrigatória
   - Cobertura de requisitos: > 95%

6. RECURSOS E CRONOGRAMA
   - Equipe de V&V (funções)
   - Ferramentas de teste
   - Timeline (alinhado com projeto)
   - Marcos de entrega

7. RASTREABILIDADE
   - Como usar TRC-001 para rastreamento
   - Requisitos → Testes → Resultados
   - Gestão de gaps de cobertura

8. GESTÃO DE DEFEITOS
   - Processo de reporte
   - Classificação (crítico/alto/médio/baixo)
   - Workflow de correção
   - Re-teste

9. DOCUMENTAÇÃO E EVIDÊNCIAS
   - Tipos de evidências requeridas
   - Armazenamento de resultados
   - Test Reports a serem gerados

10. APROVAÇÕES E ASSINATURAS
    - Matriz de aprovação
    - Assinaturas necessárias

FORMATO DO ARQUIVO:
```yaml
---
document_id: "VVP-001"
title: "Verification & Validation Plan - HemoDoctor"
version: "1.0"
status: "OFICIAL"
date: "2025-10-XX"
author: "Quality Systems Specialist"
organization: "IDOR-SP"
classification: "Dispositivo Médico - Classe II"
compliance:
  - "IEC 62304:2006"
  - "ISO 13485:2016"
  - "ISO 14971:2019"
history:
  - version: "1.0"
    date: "2025-10-XX"
    changes: "Versão inicial do plano de V&V"
    author: "Quality Systems"
---
```

SALVAR EM:
AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/VVP/VVP-001_Verification_Validation_Plan_v1.0_OFICIAL.md

CHECKLIST DE VALIDAÇÃO:
- [ ] Todas as 10 seções presentes
- [ ] Alinhado com IEC 62304
- [ ] Referencia TST-001, SRS-001, SDD-001
- [ ] Estratégia baseada em risco documentada
- [ ] 4 níveis de teste claramente definidos
- [ ] Critérios de aceitação específicos
- [ ] Timeline realista
- [ ] Header YAML completo

Pode começar?
```

---

### 📌 A.2. Test Reports (4 documentos - CRÍTICO)

#### **Agente**: `quality-systems-specialist` + `software-architecture-specialist`

#### **Instrução Completa para Cada Report**:

##### **A.2.1. Unit Tests Report**

```
@quality-systems-specialist

Crie o relatório de testes unitários:

TESTREP-001_Unit_Tests_Report_v1.0_OFICIAL.md

BASEADO EM:
- TST-001 v1.0 (casos de teste unitários)
- Código do HemoDoctor (assumir acesso ao código)

ESTRUTURA:

1. SUMÁRIO EXECUTIVO
   - Total de testes executados
   - Taxa de sucesso (pass rate)
   - Cobertura de código
   - Resumo de issues

2. AMBIENTE DE TESTE
   - Python 3.10+
   - Pytest framework
   - Coverage.py
   - Data de execução

3. CASOS DE TESTE EXECUTADOS
   Para cada módulo principal:
   - Nome do módulo
   - Casos de teste (com IDs do TST-001)
   - Resultado (Pass/Fail)
   - Tempo de execução
   
   Módulos:
   - Ingestion Service
   - Validation Service
   - Rules Engine
   - HemoAI Inference
   - Alert Orchestrator
   - Audit Service

4. COBERTURA DE CÓDIGO
   - Statement coverage: X%
   - Branch coverage: X%
   - Function coverage: X%
   - Por módulo (tabela)
   
   Objetivo: > 80% coverage

5. DEFEITOS IDENTIFICADOS
   | ID | Módulo | Severidade | Descrição | Status |
   |-----|---------|------------|-----------|--------|
   | UT-001 | ... | Alto | ... | Corrigido |

6. ANÁLISE DE RESULTADOS
   - Estatísticas gerais
   - Áreas de maior risco
   - Recomendações

7. CONCLUSÃO
   - Status geral: APROVADO/REPROVADO
   - Próximos passos

8. EVIDÊNCIAS ANEXAS
   - Log de execução pytest
   - Relatório coverage HTML
   - Screenshots (se aplicável)

SALVAR EM:
AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-001_Unit_Tests_v1.0_OFICIAL.md

Pode criar baseado em casos de teste típicos para sistemas de ML em healthcare?
```

##### **A.2.2. Integration Tests Report**

```
@quality-systems-specialist

Crie o relatório de testes de integração:

TESTREP-002_Integration_Tests_Report_v1.0_OFICIAL.md

FOCO: Integração entre microserviços e APIs

ESTRUTURA SIMILAR A TESTREP-001, MAS COM:

3. CASOS DE TESTE DE INTEGRAÇÃO
   - API Gateway ↔ Ingestion Service
   - Ingestion ↔ Validation Service
   - Validation ↔ Rules Engine
   - Rules Engine ↔ HemoAI Inference
   - HemoAI ↔ Alert Orchestrator
   - Todos ↔ Audit Service (logging)
   - UI Backend ↔ todos os serviços

4. TESTES DE API (baseado em API_SPECS v1.0)
   - Endpoints testados
   - Payloads de exemplo
   - Respostas esperadas vs obtidas
   - Status codes validados

5. TESTES DE MENSAGERIA
   - Kafka/RabbitMQ events
   - Async communication
   - Error handling

SALVAR EM:
AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-002_Integration_Tests_v1.0_OFICIAL.md
```

##### **A.2.3. System Tests Report**

```
@quality-systems-specialist

Crie o relatório de testes de sistema (end-to-end):

TESTREP-003_System_Tests_Report_v1.0_OFICIAL.md

FOCO: Validar requisitos funcionais do SRS-001 v1.0

ESTRUTURA:

3. CASOS DE TESTE DE SISTEMA
   Para cada requisito do SRS-001:
   - REQ-ID (do SRS)
   - Cenário de teste
   - Passos de execução
   - Resultado esperado
   - Resultado obtido
   - Status (Pass/Fail)

   Exemplos de cenários:
   - Ingestão completa de hemograma → sugestão diagnóstica
   - Paciente pediátrico com dados específicos → ajuste de ranges
   - Alerta crítico → notificação em tempo real
   - Auditoria completa de decisão

4. TESTES DE PERFORMANCE
   - Tempo de resposta < 3 segundos (requisito)
   - Throughput: X requisições/segundo
   - Load testing com 100 usuários simultâneos
   - Stress testing

5. TESTES DE SEGURANÇA
   - Autenticação e autorização
   - Criptografia de dados
   - LGPD compliance
   - Penetration testing básico

6. TESTES DE USABILIDADE
   - Navegação intuitiva
   - Tempo para completar tarefa
   - Taxa de erro do usuário
   - Feedback de médicos (se disponível)

SALVAR EM:
AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-003_System_Tests_v1.0_OFICIAL.md
```

##### **A.2.4. Validation Tests Report**

```
@quality-systems-specialist

Crie o relatório de testes de validação (ambiente clínico):

TESTREP-004_Validation_Tests_Report_v1.0_OFICIAL.md

FOCO: Validação com dados reais em ambiente de produção simulado

ESTRUTURA:

1. SUMÁRIO EXECUTIVO
   - Objetivo: Validar desempenho clínico do HemoDoctor
   - Ambiente: Produção simulada
   - Dados: 500 casos reais anonimizados
   - Resultado geral

2. AMBIENTE DE VALIDAÇÃO
   - Infraestrutura (igual a produção)
   - Dados de teste (fontes, anonimização)
   - Usuários finais envolvidos (X médicos)

3. CASOS DE VALIDAÇÃO CLÍNICA
   - Acurácia diagnóstica
   - Sensibilidade e especificidade
   - Valores preditivos
   - Comparação com gold standard

4. CENÁRIOS CLÍNICOS REAIS
   Caso 1: Leucemia Mieloide Aguda
   - Dados de entrada
   - Sugestão do sistema
   - Diagnóstico confirmado
   - Resultado: CORRETO/INCORRETO

   [Repetir para múltiplos casos]

5. ACEITAÇÃO DO USUÁRIO
   - Feedback dos médicos
   - Facilidade de uso
   - Confiança nas sugestões
   - Tempo economizado

6. ANÁLISE ESTATÍSTICA
   - Curva ROC
   - AUC (Area Under Curve)
   - Intervalos de confiança
   - Comparação com baseline

7. CONCLUSÃO
   - Sistema VALIDADO clinicamente
   - Pronto para uso clínico
   - Limitações identificadas

SALVAR EM:
AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-004_Validation_Tests_v1.0_OFICIAL.md
```

---

### 📌 A.3. Coverage Analysis (IMPORTANTE)

#### **Agente**: `traceability-specialist`

#### **Instrução Completa**:

```
@traceability-specialist

Crie a análise de cobertura de testes:

COV-001_Test_Coverage_Analysis_v1.0_OFICIAL.md

OBJETIVO: Mapear 100% dos requisitos do SRS-001 para testes do TST-001

DOCUMENTOS BASE:
1. SRS-001 v1.0: Todos os requisitos (funcionais e não-funcionais)
2. TST-001 v1.0: Todos os casos de teste
3. TRC-001 v1.0: Matriz de rastreabilidade atual

ESTRUTURA:

1. SUMÁRIO EXECUTIVO
   - Total de requisitos no SRS: X
   - Total de requisitos testados: Y
   - Cobertura geral: Y/X = Z%
   - Gaps identificados: X-Y
   - Status: APROVADO (se > 95%)

2. METODOLOGIA
   - Como a análise foi feita
   - Critérios de "coberto" vs "não coberto"
   - Exceções justificadas

3. MATRIZ DE COBERTURA DETALHADA

| REQ-ID | Descrição | Prioridade | Test-ID | Tipo Teste | Status | Notas |
|--------|-----------|------------|---------|------------|--------|-------|
| REQ-FUNC-001 | Ingestão HL7 | Crítica | TST-001, TST-045 | Unit, System | ✅ Coberto | - |
| REQ-FUNC-002 | Validação CBC | Crítica | TST-002, TST-046 | Unit, System | ✅ Coberto | - |
| ... | ... | ... | ... | ... | ... | ... |

4. ANÁLISE POR CATEGORIA

4.1. Requisitos Funcionais
   - Total: X
   - Cobertos: Y (Z%)
   - Não cobertos: W

4.2. Requisitos Não-Funcionais
   - Performance: 100% coberto
   - Segurança: 100% coberto
   - Usabilidade: 90% coberto
   - Disponibilidade: 100% coberto

4.3. Por Prioridade
   - Críticos: 100% cobertos (obrigatório)
   - Altos: 98% cobertos
   - Médios: 95% cobertos
   - Baixos: 85% cobertos

5. GAPS DE COBERTURA IDENTIFICADOS

| REQ-ID | Descrição | Motivo Não Testado | Ação Recomendada |
|--------|-----------|--------------------| -----------------|
| REQ-FUNC-XXX | ... | Requisito postponed | Criar TST-XXX em v1.1 |

6. JUSTIFICATIVAS PARA REQUISITOS NÃO TESTADOS
   - Requisitos postponed para v1.1
   - Requisitos de documentação apenas
   - Requisitos de treinamento (fora de escopo técnico)

7. RECOMENDAÇÕES
   - Criar testes para gaps críticos
   - Aumentar cobertura de não-funcionais
   - Priorizar testes de performance

8. CONCLUSÃO
   - Cobertura atual: Z%
   - Meta: > 95% para requisitos críticos: ATINGIDA/NÃO ATINGIDA
   - Status: APROVADO para submissão

SALVAR EM:
AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/Cobertura/COV-001_Test_Coverage_Analysis_v1.0_OFICIAL.md

TAMBÉM CRIAR:
COV-001_Coverage_Matrix_v1.0_OFICIAL.csv
(Exportar tabela do item 3 em CSV para análise em Excel)

Pode criar baseando-se nos requisitos típicos do SRS-001?
```

---

### 📊 Checklist Final Fase A

Após criar todos os documentos, validar:

- [ ] VVP-001 criado e aprovado
- [ ] TESTREP-001 (Unit) criado
- [ ] TESTREP-002 (Integration) criado
- [ ] TESTREP-003 (System) criado
- [ ] TESTREP-004 (Validation) criado
- [ ] COV-001 análise criada
- [ ] COV-001 matriz CSV criada
- [ ] Todos os documentos com header YAML v1.0
- [ ] Referências cruzadas atualizadas
- [ ] Módulo 04 status: 100% completo

---

## 🎯 FASE B: Completar Módulo 07 (Pós-Mercado)

**Timeline**: 1-2 semanas  
**Prazo**: 09 de Novembro de 2025 (v2.3.0)  
**Prioridade**: MÉDIA (após Fase A ou em paralelo)

---

### 📌 B.1. Procedimento de Relato de Incidentes (CRÍTICO - ANVISA)

#### **Agente**: `anvisa-regulatory-specialist`

#### **Instrução Completa**:

```
@anvisa-regulatory-specialist

Crie o procedimento de relato de incidentes conforme ANVISA:

PROC-001_Procedimento_Relato_Incidentes_v1.0_OFICIAL.md

REGULAMENTAÇÃO BASE:
- ANVISA RDC 67/2009 (Tecnovigilância)
- ANVISA RDC 23/2012 (Notificação de eventos adversos)
- ISO 13485:2016 (Cláusula 8.2.2 - Reclamações)

ESTRUTURA OBRIGATÓRIA:

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
   - Tecnovigilância: Sistema de monitoramento pós-mercado

4. RESPONSABILIDADES
   - Usuário Final: Relatar imediatamente
   - Equipe Clínica: Documentar e investigar inicial
   - Responsável Técnico: Avaliar severidade
   - Gerente de Qualidade: Notificar ANVISA se necessário
   - CEO: Aprovar ações corretivas críticas

5. FLUXO DE RELATO

5.1. Identificação do Incidente
   - Qualquer pessoa pode relatar
   - Canais: Email, telefone, formulário web, presencial
   - Disponibilidade: 24/7 para incidentes graves

5.2. Classificação de Severidade
   [CRÍTICO - Seguir RDC 67/2009]
   
   GRAVE: Notificação ANVISA em 10 dias úteis
   - Morte relacionada ao dispositivo
   - Ameaça à vida
   - Lesão grave ou incapacidade permanente
   - Necessidade de intervenção médica para prevenir dano
   
   NÃO GRAVE: Notificação ANVISA em 60 dias
   - Mau funcionamento sem dano ao paciente
   - Queixa técnica
   - Sugestão incorreta sem seguimento pelo médico

5.3. Registro Imediato
   - Preencher FORM-001_Relato_Incidente (ver Fase B.4)
   - Gerar número único de protocolo
   - Timestamp de recebimento
   - Guardar todas as evidências

5.4. Ação Imediata (0-24h)
   - Avaliar necessidade de ação urgente
   - Se GRAVE: Considerar suspender uso do sistema
   - Notificar stakeholders relevantes
   - Iniciar investigação preliminar

6. PRAZOS REGULATÓRIOS ANVISA

| Severidade | Prazo Notificação | Prazo Investigação | Prazo Relatório Final |
|------------|-------------------|--------------------|-----------------------|
| GRAVE | 10 dias úteis | 30 dias | 60 dias |
| NÃO GRAVE | 60 dias | 90 dias | 120 dias |

7. PROCEDIMENTO DE NOTIFICAÇÃO ANVISA

7.1. Preparação
   - Preencher FORM-004_Notificacao_ANVISA
   - Coletar evidências (logs, dados, prints)
   - Redigir relatório técnico

7.2. Submissão
   - Portal NOTIVISA: https://www.gov.br/anvisa/pt-br/assuntos/fiscalizacao/notivisa
   - Cadastro prévio necessário
   - Upload de documentos
   - Aguardar protocolo

7.3. Follow-up
   - Responder solicitações ANVISA em 15 dias
   - Informar ações corretivas implementadas
   - Atualizar status de investigação

8. COMUNICAÇÃO INTERNA
   - Email imediato para equipe de qualidade
   - Reunião de análise em 48h para incidentes graves
   - Atualização semanal em quadro Kanban

9. REGISTRO E DOCUMENTAÇÃO
   - Banco de dados de incidentes (Excel ou sistema)
   - Histórico completo por número de protocolo
   - Rastreabilidade de ações tomadas
   - Evidências preservadas por 5 anos (mínimo legal)

10. INTEGRAÇÃO COM CAPA
    - Se incidente requer ação corretiva → abrir CAPA (ver PROC-003)
    - Link entre incidente e CAPA no sistema
    - Follow-up de eficácia da ação

11. RELATÓRIO PERIÓDICO
    - Relatório mensal: Estatísticas de incidentes
    - Relatório trimestral: Análise de tendências
    - Relatório anual: Submissão obrigatória ANVISA (PSUR)

12. TREINAMENTO
    - Todos os usuários: Treinamento básico de relato
    - Equipe clínica: Treinamento completo do procedimento
    - Refresher: Anual

FORMATO DO ARQUIVO:
```yaml
---
document_id: "PROC-001"
title: "Procedimento de Relato de Incidentes e Tecnovigilância"
version: "1.0"
status: "OFICIAL"
date: "2025-10-XX"
compliance:
  - "ANVISA RDC 67/2009"
  - "ANVISA RDC 23/2012"
  - "ISO 13485:2016"
---
```

ANEXOS A INCLUIR:
- Fluxograma do processo de relato
- Template de email de notificação interna
- Checklist de informações mínimas para relato

SALVAR EM:
AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/PROC-001_Procedimento_Relato_Incidentes_v1.0_OFICIAL.md

Pode criar este procedimento crítico para ANVISA?
```

---

### 📌 B.2. Procedimento de Investigação de Eventos (CRÍTICO)

#### **Agente**: `risk-management-specialist`

#### **Instrução Completa**:

```
@risk-management-specialist

Crie o procedimento de investigação de eventos adversos:

PROC-002_Procedimento_Investigacao_Eventos_v1.0_OFICIAL.md

BASE:
- ISO 13485:2016 (Cláusula 8.5 - Melhoria)
- ISO 14971:2019 (Análise de riscos pós-mercado)
- RCA (Root Cause Analysis) metodologia

ESTRUTURA:

1. OBJETIVO
   - Investigar causa raiz de incidentes
   - Prevenir recorrência
   - Cumprir requisitos regulatórios

2. ESCOPO
   - Todos os incidentes relatados via PROC-001
   - Priorização por severidade

3. METODOLOGIA DE INVESTIGAÇÃO

3.1. Coleta de Evidências (0-7 dias)
   - Logs de sistema (timestamp, user, ação)
   - Dados de entrada (CBC, paciente)
   - Output do sistema (sugestão diagnóstica)
   - Screenshots/prints
   - Entrevista com usuário
   - Entrevista com paciente (se aplicável)
   - Histórico médico relevante
   - Ambiente técnico (browser, OS, rede)

3.2. Reconstrução do Incidente (7-14 dias)
   - Timeline detalhado do evento
   - O que aconteceu?
   - Quando aconteceu?
   - Onde (módulo do sistema)?
   - Quem estava envolvido?
   - Como foi detectado?

3.3. Análise de Causa Raiz (14-30 dias)
   
   Ferramentas:
   
   A) **5 Whys**
   Pergunta inicial: Por que o incidente ocorreu?
   - Why 1: ...
   - Why 2: ...
   - Why 3: ...
   - Why 4: ...
   - Why 5: ... → CAUSA RAIZ
   
   B) **Ishikawa (Espinha de Peixe)**
   Categorias:
   - Método (processo, algoritmo)
   - Máquina (hardware, infraestrutura)
   - Material (dados, entrada)
   - Mão de obra (treinamento, erro humano)
   - Medida (métricas, monitoramento)
   - Meio ambiente (contexto clínico)
   
   C) **Análise de Falha**
   - Falha de software? (bug)
   - Falha de dados? (entrada incorreta)
   - Falha de processo? (uso inadequado)
   - Falha de design? (limitação do sistema)

4. AVALIAÇÃO DE IMPACTO

4.1. Impacto no Paciente
   - Houve dano? (sim/não)
   - Gravidade do dano
   - Necessidade de follow-up médico

4.2. Impacto no Sistema
   - Quantos usuários afetados?
   - Frequência do problema?
   - Risco de recorrência?

4.3. Impacto Regulatório
   - Requer notificação ANVISA?
   - Impacto em certificações?
   - Risco de recall?

5. CATEGORIZAÇÃO DA CAUSA RAIZ

| Categoria | Descrição | Exemplo |
|-----------|-----------|---------|
| Bug de Software | Erro de código | Loop infinito, null pointer |
| Dados Incorretos | Entrada inválida | CBC fora do range normal |
| Uso Inadequado | Erro do usuário | Má interpretação da sugestão |
| Limitação de Design | Sistema funcionou como esperado mas resultado inadequado | Caso edge não coberto |
| Infraestrutura | Problema de ambiente | Timeout de rede |

6. RELATÓRIO DE INVESTIGAÇÃO

Template:
- Número do incidente
- Data de ocorrência
- Data da investigação
- Investigador responsável
- Sumário executivo (1 parágrafo)
- Evidências coletadas (lista)
- Timeline do incidente (tabela)
- Análise de causa raiz (5 Whys + Ishikawa)
- Causa raiz identificada
- Categorização
- Impacto avaliado
- Recomendações:
  - Ação corretiva imediata
  - Ação corretiva longo prazo
  - Ação preventiva
- Necessidade de CAPA: SIM/NÃO
- Necessidade de atualização de risco (RMP): SIM/NÃO
- Necessidade de notificação ANVISA: SIM/NÃO
- Conclusão
- Assinaturas

7. DECISÃO SOBRE AÇÕES

7.1. Se BUG identificado:
   - Abrir ticket de desenvolvimento
   - Prioridade: Crítica/Alta/Média/Baixa
   - Target fix version
   - Regressão testing obrigatório

7.2. Se DADO incorreto:
   - Melhorar validação de entrada
   - Adicionar alertas para usuário
   - Documentar range válido

7.3. Se USO inadequado:
   - Atualizar IFU (Instructions for Use)
   - Treinamento adicional para usuários
   - Melhorar UX (se aplicável)

7.4. Se LIMITAÇÃO de design:
   - Avaliar se é crítico corrigir
   - Se sim: Abrir CAPA e planejar redesign
   - Se não: Documentar limitação conhecida no IFU

8. INTEGRAÇÃO COM CAPA (PROC-003)
   - Se ação corretiva necessária → Abrir CAPA-XXX
   - Link no relatório de investigação
   - Usar mesma causa raiz identificada

9. ATUALIZAÇÃO DE GESTÃO DE RISCO
   - Se novo risco identificado → Atualizar RMP-001
   - Se risco existente subestimado → Revisar avaliação
   - Atualizar controles de mitigação

10. FOLLOW-UP E FECHAMENTO
    - Verificar implementação de ações
    - Re-teste se bug corrigido
    - Validar eficácia da ação
    - Comunicar aos stakeholders
    - Fechar incidente no sistema
    - Arquivar documentação

11. RELATÓRIO PARA ANVISA
    - Se incidente grave: Usar FORM-004
    - Incluir: Causa raiz, ações tomadas, status
    - Prazo: Conforme RDC 67/2009

SALVAR EM:
AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/PROC-002_Procedimento_Investigacao_Eventos_v1.0_OFICIAL.md

Pode criar com exemplos de casos reais em healthcare software?
```

---

### 📌 B.3. Procedimento CAPA (IMPORTANTE)

#### **Agente**: `quality-systems-specialist`

#### **Instrução Completa**:

```
@quality-systems-specialist

Crie o procedimento CAPA (Corrective and Preventive Actions):

PROC-003_Procedimento_CAPA_v1.0_OFICIAL.md

BASE:
- ISO 13485:2016 (Cláusula 8.5.2 e 8.5.3)
- 21 CFR Part 820.100 (FDA CAPA)
- Integração com gestão de riscos (ISO 14971)

ESTRUTURA:

1. OBJETIVO
   - Eliminar causas de não-conformidades
   - Prevenir recorrência
   - Melhorar continuamente o sistema de qualidade

2. DEFINIÇÕES
   - Ação Corretiva: Eliminar causa de não-conformidade detectada
   - Ação Preventiva: Eliminar causa de não-conformidade potencial
   - Não-conformidade: Não cumprimento de requisito
   - Causa raiz: Razão fundamental do problema

3. QUANDO ABRIR CAPA

Gatilhos:
- Incidente grave com paciente
- Bug crítico de software
- Reclamação recorrente de usuário
- Auditoria interna: Não-conformidade
- Auditoria externa: Não-conformidade
- Falha em teste de sistema
- Desvio de processo
- Near miss (quase acidente)

4. PROCESSO CAPA (8 ETAPAS)

4.1. ABERTURA (Dia 0)
- Identificação do problema
- Descrição clara e objetiva
- Evidências iniciais
- Classificação: Corretiva ou Preventiva
- Responsável designado
- Prazo inicial estimado
- Número CAPA gerado: CAPA-YYYY-XXX

4.2. ANÁLISE DE CAUSA RAIZ (0-15 dias)
- Usar metodologias (5 Whys, Ishikawa)
- Envolver equipe multidisciplinar
- Coletar dados e evidências
- Documentar análise completa
- Identificar causa raiz verificável

4.3. PLANEJAMENTO DA AÇÃO (15-20 dias)
- Definir ação corretiva/preventiva específica
- Estabelecer objetivos SMART
- Identificar recursos necessários
- Definir responsáveis
- Estabelecer prazo realista
- Avaliar impacto em outros processos

4.4. APROVAÇÃO (20-22 dias)
- Revisão por Gerente de Qualidade
- Aprovação por Responsável Técnico
- Se impacto alto: Aprovação CEO
- Registro de aprovação com assinatura

4.5. IMPLEMENTAÇÃO (22-60 dias)
- Executar ação conforme plano
- Documentar todas as etapas
- Comunicar à equipe afetada
- Treinar pessoal (se aplicável)
- Atualizar documentação (SOPs, IFU, etc)
- Registrar evidências de implementação

4.6. VERIFICAÇÃO DE EFICÁCIA (60-90 dias)
- Definir critérios de eficácia (ANTES da implementação)
- Monitorar indicadores
- Coletar dados pós-implementação
- Comparar situação antes vs depois
- Verificação objetiva e mensurável

Exemplos de critérios:
- Bug: 0 ocorrências em 30 dias
- Processo: 100% conformidade em auditoria
- Treinamento: 100% equipe aprovada em teste

4.7. REVISÃO DA GESTÃO DE RISCO (90-95 dias)
- Avaliar se novo risco foi introduzido
- Atualizar RMP-001 se necessário
- Revisar controles de mitigação
- Documentar no histórico de riscos

4.8. FECHAMENTO (95-100 dias)
- Confirmar eficácia da ação
- Arquivar documentação completa
- Atualizar registros de qualidade
- Comunicar fechamento aos stakeholders
- Lessons learned para equipe

5. FORMULÁRIO CAPA (FORM-003)

Campos obrigatórios:
- Número CAPA
- Data de abertura
- Tipo: Corretiva / Preventiva
- Fonte: Incidente / Auditoria / Reclamação / Outro
- Descrição do problema
- Evidências
- Análise de causa raiz
- Causa raiz identificada
- Ação proposta
- Responsável
- Prazo
- Recursos necessários
- Critérios de eficácia
- Status: Aberta / Em análise / Implementação / Verificação / Fechada / Cancelada
- Data de fechamento
- Verificação de eficácia: Sim / Não
- Assinaturas (Responsável, QA, RT)

6. PRIORIZAÇÃO DE CAPA

| Prioridade | Critério | Prazo |
|------------|----------|-------|
| Crítica | Risco à segurança do paciente | 30 dias |
| Alta | Não-conformidade regulatória | 60 dias |
| Média | Reclamação recorrente | 90 dias |
| Baixa | Melhoria de processo | 120 dias |

7. INDICADORES DE DESEMPENHO

- Número de CAPAs abertas/mês
- Número de CAPAs fechadas/mês
- Tempo médio de fechamento
- Taxa de eficácia (CAPAs eficazes / CAPAs verificadas)
- Taxa de recorrência (mesmo problema reabre CAPA?)
- Backlog de CAPAs em aberto

Metas:
- Tempo médio < 90 dias
- Taxa de eficácia > 95%
- Taxa de recorrência < 5%

8. INTEGRAÇÃO COM OUTROS PROCESSOS

8.1. Com Gestão de Incidentes (PROC-001)
- Incidente grave → Investigação (PROC-002) → CAPA
- Link bidirecional nos sistemas

8.2. Com Gestão de Riscos (RMP-001)
- CAPA pode gerar novo risco
- Atualizar análise de risco se aplicável

8.3. Com Auditoria Interna
- Não-conformidade de auditoria → CAPA obrigatória
- Follow-up em auditoria subsequente

8.4. Com Treinamento
- CAPA pode resultar em necessidade de treinamento
- Registrar treinamento como parte da ação

9. DOCUMENTAÇÃO E RASTREABILIDADE

- Sistema de gestão de CAPAs (Excel ou software)
- Pasta física/digital por CAPA
- Retenção: 5 anos mínimo (requisito regulatório)
- Rastreabilidade de todas as ações
- Histórico de revisões

10. REVISÃO GERENCIAL

- Revisão mensal: CAPAs críticas
- Revisão trimestral: Análise de tendências
- Revisão anual: Apresentação para direção
- Dashboards de indicadores

SALVAR EM:
AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/PROC-003_Procedimento_CAPA_v1.0_OFICIAL.md

Pode criar este procedimento crítico de qualidade?
```

---

### 📌 B.4. Formulários e Templates (IMPORTANTE)

#### **Agente**: `anvisa-regulatory-specialist`

#### **Instrução Completa**:

```
@anvisa-regulatory-specialist

Crie 4 formulários padronizados para vigilância pós-mercado:

LOCALIZAÇÃO: AUTHORITATIVE_BASELINE/07_POS_MERCADO/Vigilancia/Formularios/

---

FORM-001_Relato_Incidente_v1.0.md

Formulário para relato inicial de incidentes (usado em PROC-001).

ESTRUTURA:

# Formulário de Relato de Incidente - HemoDoctor

**Número de Protocolo**: [Gerado automaticamente]  
**Data de Recebimento**: ___/___/______  
**Recebido por**: _______________________

## 1. IDENTIFICAÇÃO DO RELATOR

- Nome: _____________________________________
- Função: ___________________________________
- Hospital/Instituição: _____________________
- Telefone: __________________________________
- Email: _____________________________________
- Relação com o incidente: □ Usuário □ Paciente □ Testemunha □ Outro: _______

## 2. INFORMAÇÕES DO DISPOSITIVO

- Nome do Produto: HemoDoctor
- Versão do Software: v______
- Número de Série/Licença: _________________
- Local de uso: _____________________________

## 3. DESCRIÇÃO DO INCIDENTE

- Data do incidente: ___/___/______
- Hora: ___:___
- Local: _____________________________________

**Descrição detalhada** (O que aconteceu?):
__________________________________________________
__________________________________________________
__________________________________________________

**Dados de entrada** (CBC, parâmetros):
__________________________________________________

**Output do sistema** (Sugestão diagnóstica):
__________________________________________________

**Resultado esperado**:
__________________________________________________

## 4. IMPACTO NO PACIENTE

□ Não houve envolvimento de paciente  
□ Houve envolvimento de paciente

Se houve:
- Iniciais do paciente: ___________
- Idade: ______ Sexo: □ M □ F
- Número do prontuário: ___________________

**Houve dano ao paciente?**
□ Não
□ Sim - Descrever:
__________________________________________________

**Gravidade do dano** (se houve):
□ Sem dano físico
□ Dano temporário reversível
□ Dano permanente
□ Ameaça à vida
□ Morte

## 5. CLASSIFICAÇÃO PRELIMINAR DE SEVERIDADE

□ **GRAVE** (morte, ameaça à vida, lesão grave)  
  → Notificação ANVISA: 10 dias úteis

□ **NÃO GRAVE** (mau funcionamento sem dano)  
  → Notificação ANVISA: 60 dias

## 6. AÇÃO IMEDIATA TOMADA

□ Nenhuma
□ Sistema desligado
□ Paciente monitorado
□ Intervenção médica realizada
□ Outro: ___________________________________

## 7. EVIDÊNCIAS ANEXAS

□ Screenshots
□ Logs de sistema
□ Relatório médico
□ Exames complementares
□ Outro: ___________________________________

## 8. ASSINATURAS

**Relator**:
Nome: _____________________ Assinatura: __________ Data: ___/___/___

**Responsável Técnico (RT)**:
Nome: _____________________ Assinatura: __________ Data: ___/___/___

**Gerente de Qualidade**:
Nome: _____________________ Assinatura: __________ Data: ___/___/___

---

**PARA USO INTERNO**

**Próximas Ações**:
□ Iniciar investigação (PROC-002)
□ Abrir CAPA
□ Notificar ANVISA
□ Atualizar gestão de risco

**Investigador Designado**: ___________________  
**Prazo Investigação**: ___/___/______

---

FORM-002_Investigacao_Evento_v1.0.md

Formulário para investigação completa (usado em PROC-002).

[Similar estrutura com:]
- Número CAPA vinculado
- Cronologia detalhada
- Análise de causa raiz (5 Whys + Ishikawa)
- Evidências coletadas
- Conclusões
- Recomendações

---

FORM-003_CAPA_v1.0.md

Formulário CAPA (usado em PROC-003).

[Estrutura com 8 seções do processo CAPA]

---

FORM-004_Notificacao_ANVISA_v1.0.md

Template para notificação oficial ANVISA conforme RDC 67/2009.

[Estrutura conforme portal NOTIVISA]

---

Pode criar todos os 4 formulários com estrutura completa e profissional?
```

---

### 📊 Checklist Final Fase B

Após criar todos os documentos, validar:

- [ ] PROC-001 (Relato Incidentes) criado e aprovado
- [ ] PROC-002 (Investigação) criado e aprovado
- [ ] PROC-003 (CAPA) criado e aprovado
- [ ] FORM-001 (Relato) criado
- [ ] FORM-002 (Investigação) criado
- [ ] FORM-003 (CAPA) criado
- [ ] FORM-004 (Notificação ANVISA) criado
- [ ] Todos conformes com ANVISA RDC 67/2009
- [ ] Integração entre procedimentos documentada
- [ ] Módulo 07 status: 100% completo

---

## 🎯 VALIDAÇÃO FINAL - Ambas as Fases

Após completar Fases A e B, executar:

### Com `documentation-finalization-specialist`:

```
@documentation-finalization-specialist

Execute validação final dos módulos 04 e 07:

/document-quality-assurance all-PKGs ANVISA-standards

Verifique:
1. Módulo 04 (V&V): 100% completo?
2. Módulo 07 (Pós-Mercado): 100% completo?
3. Todos os documentos v1.0?
4. Headers padronizados?
5. Referências cruzadas corretas?

Gere relatório:
RELATORIO_VALIDACAO_MODULOS_04_07_v1.0.md
```

---

## 📋 Timeline Sugerido

### Semana 1 (21-25 Out)
- [ ] VVP-001 (Fase A)
- [ ] PROC-001 (Fase B)
- [ ] PROC-002 (Fase B)

### Semana 2 (28 Oct - 01 Nov)
- [ ] TESTREP-001, 002 (Fase A)
- [ ] PROC-003 (Fase B)
- [ ] Formulários (Fase B)

### Semana 3 (04-08 Nov)
- [ ] TESTREP-003, 004 (Fase A)
- [ ] COV-001 (Fase A)
- [ ] Validação final

---

## 📞 Suporte

**Dúvidas técnicas**: dev-hemodoctor@idor.org  
**Dúvidas regulatórias**: regulatory-hemodoctor@idor.org  
**Dúvidas QA**: quality-hemodoctor@idor.org

---

**Status**: ✅ Instruções prontas para uso  
**Última Atualização**: 12 de Outubro de 2025  
**Versão**: 1.0

