# Reunião: Planning Sprint 14 - 2025-10-01

## Participantes
- Dr. Abel Costa (Product Owner)
- João Silva (Tech Lead)
- Maria Santos (Backend Dev)
- Pedro Oliveira (Frontend Dev)

## Pauta
1. Review do Sprint 13
2. Definição de tarefas Sprint 14
3. Discussão sobre arquitetura de microservices

## Discussões

### 1. Review Sprint 13
- ✅ Concluídas 8 de 10 histórias
- ⚠️ 2 histórias com impedimentos técnicos (banco de dados)
- 📊 Velocity: 32 pontos

### 2. Sprint 14 - Tarefas Planejadas
- Implementação de API Gateway
- Refatoração do serviço de validação
- Testes de integração dos microservices
- Documentação de APIs

### 3. Arquitetura de Microservices

**Discussão**: Qual banco de dados usar para cada serviço?

**Opções Consideradas**:
- MongoDB (NoSQL, flexível)
- PostgreSQL (SQL, ACID, relacional)

**Pontos Levantados**:
- João: "PostgreSQL oferece melhor conformidade ACID para dados médicos"
- Maria: "MongoDB seria mais rápido para logs e eventos"
- Pedro: "Precisamos de transações para garantir integridade"

**Decisão Pendente**: Agendar reunião específica sobre escolha de BD

## Decisões

- ✅ Sprint 14 aprovado com 10 histórias (40 pontos)
- ✅ Priorizar API Gateway esta semana
- 🕐 **PENDENTE**: Decisão sobre banco de dados → Reunião dia 05/10

## Action Items

- [ ] [@João] Criar ADR sobre opções de banco de dados - Prazo: 2025-10-03
- [ ] [@Maria] Preparar POC com PostgreSQL - Prazo: 2025-10-04
- [ ] [@Pedro] Preparar POC com MongoDB - Prazo: 2025-10-04
- [ ] [@Abel] Validar requisitos de conformidade regulatória - Prazo: 2025-10-03

## Próxima Reunião

**Data**: 2025-10-05 (sexta-feira)  
**Horário**: 14:00  
**Objetivo**: Decisão final sobre banco de dados

