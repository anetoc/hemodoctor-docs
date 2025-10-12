# Reunião: Decisão Banco de Dados - 2025-10-05

## Participantes
- Dr. Abel Costa (Product Owner)
- João Silva (Tech Lead)
- Maria Santos (Backend Dev)
- Pedro Oliveira (Frontend Dev)
- Ana Ribeiro (DBA)

## Contexto

Reunião de follow-up da discussão iniciada em 01/10/2025 sobre escolha de banco de dados para microservices.

## Apresentações

### POC PostgreSQL (Maria)
- ✅ Transações ACID funcionando
- ✅ Suporte nativo para JSON
- ✅ Performance adequada para volume esperado
- ⚠️ Requer mais setup inicial

### POC MongoDB (Pedro)
- ✅ Setup rápido e fácil
- ✅ Flexibilidade de schema
- ❌ Transações multi-documento complexas
- ❌ Menor garantia de consistência

### Análise de Conformidade (Abel)
- 🔴 **Requisito crítico**: IEC 62304 exige rastreabilidade de dados
- 🔴 **Requisito ANVISA**: Integridade de dados médicos (ACID)
- 🟢 PostgreSQL atende completamente
- 🟡 MongoDB requer work-arounds

## Decisão

**✅ DECISÃO APROVADA POR UNANIMIDADE: PostgreSQL**

**Justificativa**:
1. Conformidade regulatória (IEC 62304, ANVISA)
2. Transações ACID garantem integridade
3. Rastreabilidade de dados médicos
4. Suporte a JSON para flexibilidade quando necessário
5. Maturidade e confiabilidade comprovadas

**Exceções**:
- MongoDB será usado APENAS para:
  - Logs de aplicação (não-críticos)
  - Cache de sessões
  - Dados analíticos (não regulados)

## Próximos Passos

- [ ] [@João] Criar ADR-001 formalizando esta decisão - Prazo: 2025-10-07
- [ ] [@Maria] Setup de PostgreSQL em dev/staging - Prazo: 2025-10-10
- [ ] [@Ana] Definir schema inicial e migrations - Prazo: 2025-10-12
- [ ] [@Pedro] Atualizar documentação de arquitetura - Prazo: 2025-10-10

## Referências

- POC PostgreSQL: `POCs/postgresql_tests/`
- POC MongoDB: `POCs/mongodb_tests/`
- Requisitos regulatórios: Ver SRS v2.2, Seção 4.2.3
- Análise de conformidade: Ver RMP v1.0, Seção sobre integridade de dados

---

**Data da Decisão**: 2025-10-05  
**Status**: ✅ APROVADA  
**Impacto**: Alto - afeta toda arquitetura de dados

