# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Não Lançado]

### Em Desenvolvimento
- Melhorias no sistema de agentes
- Atualizações de conformidade regulatória

---

## [2.0.0] - 2025-10-11

### 🎉 Release Inicial do Repositório GitHub

#### Adicionado
- **Estrutura Completa**: AUTHORITATIVE_BASELINE com 10 módulos regulatórios
- **Sistema de Agentes**: 13 agentes especializados em HEMODOCTOR_AGENTES/
- **Metodologia BMAD**: Framework completo de documentação automatizada
- **Documentação Profissional**: README.md, CONTRIBUTING.md, SECURITY.md, LICENSE
- **Templates de Issues**: Bug reports e feature requests padronizados
- **Scripts de Automação**: Migração, validação e análise

#### Documentos Regulatórios Incluídos

**Módulo 01 - REGULATORIO**
- DMR v2.0 - Device Master Record completo
- Manifestos e checksums de validação

**Módulo 02 - CONTROLES_DESIGN**
- SRS v2.2 - Software Requirements Specification (5 versões evolutivas)
- SDD v2.0 - Software Design Document (3 versões)
- TEC v1.0 - Technical File / Software Development Plan
- API_SPECS - 10 especificações OpenAPI/AsyncAPI

**Módulo 03 - GESTAO_RISCO**
- RMP v1.0 - Risk Management Plan ISO 14971
- TEC-002 v2.0 - Risk Management File

**Módulo 04 - VERIFICACAO_VALIDACAO**
- TST v1.0 - Test Specification
- Relatórios de cobertura e validação

**Módulo 05 - AVALIACAO_CLINICA**
- CER v1.2 - Clinical Evaluation Report (validado)
- Evidências científicas
- Revisão de literatura

**Módulo 06 - RASTREABILIDADE**
- TRC v2.1 - Traceability Matrix com 100% coverage
- Rastreamento Requisitos → Design → Testes → Riscos

**Módulo 07 - POS_MERCADO**
- PMS v1.1 - Post-Market Surveillance Plan

**Módulo 08 - ROTULAGEM**
- IFU v1.0 PT-BR - Instruções de Uso em Português
- IFU v1.0 EN-US - Instructions For Use em Inglês

**Módulo 09 - CYBERSECURITY**
- SEC v1.0 - Cybersecurity Analysis
- SBOM v1.0 - Software Bill of Materials
- VEX v1.0 - Vulnerability Exploitability eXchange

**Módulo 10 - SOUP**
- SOUP-001 v1.0 - Análise de Software of Unknown Provenance

#### Sistema de Agentes

**Agentes Regulatórios**:
- anvisa-regulatory-specialist
- external-regulatory-consultant
- regulatory-review-specialist

**Agentes Técnicos**:
- software-architecture-specialist
- risk-management-specialist
- hematology-technical-specialist

**Agentes de Qualidade**:
- quality-systems-specialist
- traceability-specialist
- documentation-finalization-specialist

**Agentes Clínicos**:
- clinical-evidence-specialist
- cep-protocol-specialist
- biostatistics-specialist

**Orquestração**:
- hemodoctor-orchestrator

#### Scripts e Ferramentas
- `analyze_hemodoctor_agents.js` - Análise do sistema de agentes
- `analyze_project_knowledge.js` - Análise de conhecimento
- `migrate_p0_files.sh` / `migrate_p1_files.sh` - Scripts de migração
- `validate_p0.sh` / `validate_p1.sh` - Scripts de validação
- `reorganize_repository_v2.0.sh` - Reorganização do repositório

#### Relatórios Incluídos
- ✅ RELATORIO_ANALISE_AGENTES_HEMODOCTOR.md
- ✅ RELATORIO_AUDITORIA_SISTEMA_AGENTES.md
- ✅ RELATORIO_COMPARACAO_MIGRACAO_20251010.md
- ✅ RELATORIO_ORGANIZACAO_FINAL_20251011.md
- ✅ REPOSITORY_ANALYSIS_DETAILED_20251011.md
- ✅ DASHBOARD_AGENTES_HEMODOCTOR.html

#### Configurações do Repositório
- Configurado como repositório público
- Topics adicionados: healthcare, medical-device, regulatory, anvisa, fda, hematology, oncology, samd, documentation, iso-13485
- Issues habilitados
- Wiki habilitado
- `.gitignore` configurado para projetos Node.js e Python

### Fixado
- README.md focado exclusivamente no HemoDoctor (removidas referências ao Scout Clinical Trials)
- Correção na descrição do projeto para focar em documentação regulatória

---

## [1.2.0] - 2025-10-08

### Adicionado
- CER v1.2 - Clinical Evaluation Report atualizado
- PMS v1.1 - Post-Market Surveillance Plan atualizado

### Atualizado
- TRC v2.1 - Matriz de rastreabilidade com 100% de cobertura
- Validações consolidadas completas

---

## [1.1.0] - 2025-10-08

### Adicionado
- SRS v1.1 - Software Requirements Specification atualizado
- SDD v1.1 - Software Design Document atualizado

### Fixado
- Análise de cobertura de requisitos
- Correções em rastreabilidade

---

## [1.0.0] - 2025-10-08

### 🎉 Release Inicial - SUBMISSION READY

#### Adicionado
- **Baseline Autoritativa Completa**: Todos os 10 módulos regulatórios
- **Conformidade Total**: ANVISA RDC 185/2001, RDC 657/2022
- **Normas ISO**: 13485, 14971, 62304, 27001
- **Documentação Técnica**: SRS, SDD, TEC, API Specs
- **Avaliação Clínica**: CER v1.0 completo
- **Gestão de Riscos**: RMP v1.0 conforme ISO 14971
- **Rastreabilidade**: TRC v1.0 inicial
- **Cybersecurity**: SEC, SBOM, VEX
- **SOUP Analysis**: Componentes de terceiros analisados
- **IFU**: Instruções em PT-BR e EN-US

#### Status
- ✅ **SUBMISSION READY**: Pronto para submissão ANVISA
- ✅ Todos os documentos obrigatórios completos
- ✅ Rastreabilidade estabelecida
- ✅ Validações executadas
- ✅ Conformidade regulatória verificada

---

## Tipos de Mudanças

- **Adicionado**: Para novas funcionalidades
- **Alterado**: Para mudanças em funcionalidades existentes
- **Descontinuado**: Para funcionalidades que serão removidas
- **Removido**: Para funcionalidades removidas
- **Fixado**: Para correções de bugs
- **Segurança**: Para vulnerabilidades corrigidas

---

## Controle de Versões

### Versionamento de Documentos
- **Major (X.0.0)**: Mudanças estruturais significativas
- **Minor (X.Y.0)**: Atualizações de conteúdo, novos documentos
- **Patch (X.Y.Z)**: Correções, typos, ajustes menores

### Status de Documentos
- **DRAFT**: Em elaboração
- **REVIEW**: Em revisão
- **OFICIAL**: Aprovado e oficial
- **DEPRECATED**: Obsoleto

---

## Notas de Conformidade

Todas as mudanças em documentos regulatórios são:
- ✅ Rastreadas na matriz TRC
- ✅ Revisadas por especialistas
- ✅ Validadas quanto à conformidade
- ✅ Versionadas adequadamente
- ✅ Documentadas em manifestos

---

**Mantido por**: Equipe HemoDoctor IDOR-SP  
**Última Atualização**: 2025-10-11

