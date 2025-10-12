# HemoDoctor - Sistema de Documentação Regulatória para Dispositivos Médicos

## 📋 Visão Geral

HemoDoctor é um sistema completo de documentação técnica e regulatória para dispositivos médicos SaMD (Software as a Medical Device) na área de oncologia hematológica, desenvolvido em conformidade com normas ANVISA, FDA e IMDRF.

## 🎯 Objetivo

Prover documentação técnica completa e rastreável para submissão regulatória de dispositivos médicos de Classe III focados em suporte à decisão clínica em neoplasias hematológicas.

## 🏗️ Estrutura do Projeto

### AUTHORITATIVE_BASELINE/
Base autoritativa de documentação regulatória organizada em 10 módulos conforme requisitos ANVISA/FDA:

#### **00_INDICE_GERAL**
- Índices mestres
- Checksums de validação
- Relatórios de consolidação
- Estratégia de consolidação

#### **01_REGULATORIO**
- **Certificados**: Certificações ISO 13485, ISO 27001
- **Declarações**: DoC (Declaration of Conformity)
- **DMR** (Device Master Record): Manifesto completo do dispositivo
- **QMS**: Sistema de Gestão da Qualidade

#### **02_CONTROLES_DESIGN**
- **API_SPECS**: 10 especificações OpenAPI/AsyncAPI
  - API Gateway, Ingestion Service, Validation Service
  - Rules Engine, HemoAI Inference, Alert Orchestrator
  - Audit Service, Model Manager, UI Backend
  - Async Events (mensageria)
- **Arquitetura**: Diagramas de arquitetura do sistema
- **SDD** (Software Design Document): 3 versões (v1.0, v1.1, v2.0)
- **SRS** (Software Requirements Specification): 5 versões até v2.2
- **TEC** (Technical File): Plano de desenvolvimento de software

#### **03_GESTAO_RISCO**
- **Análises**: Análises de risco detalhadas
- **Matrizes**: Matrizes de risco
- **RMP** (Risk Management Plan): Plano de gestão de riscos ISO 14971

#### **04_VERIFICACAO_VALIDACAO**
- **Cobertura**: Relatórios de cobertura de testes
- **TestReports**: Relatórios de testes executados
- **TST** (Test Specification): Especificações de teste
- **VVP** (Verification & Validation Plan): Planos V&V

#### **05_AVALIACAO_CLINICA**
- **CER** (Clinical Evaluation Report): Avaliação clínica v1.2
- **Evidências**: Evidências clínicas coletadas
- **Literatura**: Revisão sistemática de literatura

#### **06_RASTREABILIDADE**
- **Matrizes**: Matrizes de rastreabilidade
- **TRC**: Matriz de rastreabilidade completa (v1.0, v2.0, v2.1)
  - Requisitos → Design → Testes → Riscos

#### **07_POS_MERCADO**
- **PMS** (Post-Market Surveillance): Vigilância pós-mercado
- **Vigilância**: Planos de vigilância

#### **08_ROTULAGEM**
- **IFU** (Instructions For Use): 
  - IFU-001_EN_US_v1.0_OFICIAL.pdf (Inglês)
  - IFU-001_PT_BR_v1.0_OFICIAL.pdf (Português)
- **Labels**: Rótulos do produto

#### **09_CYBERSECURITY**
- **SBOM** (Software Bill of Materials): Lista completa de componentes
- **SEC**: Análise de segurança cibernética
- **VEX** (Vulnerability Exploitability eXchange): Análise de vulnerabilidades

#### **10_SOUP**
- **SOUP-001**: Análise de Software of Unknown Provenance
  - Componentes de terceiros
  - Análise de riscos de SOUP

## 🤖 Sistema de Agentes Especializados

### HEMODOCTOR_AGENTES/

Sistema multi-agente para automação de processos regulatórios:

#### **Agentes Regulatórios**
- **anvisa-regulatory-specialist**: Especialista em regulamentação ANVISA RDC 185/2001, RDC 657/2022
- **external-regulatory-consultant**: Consultoria FDA, MDR europeu, IMDRF
- **regulatory-review-specialist**: Revisão de submissões regulatórias

#### **Agentes Técnicos**
- **software-architecture-specialist**: Arquitetura de software IEC 62304
- **risk-management-specialist**: Gestão de riscos ISO 14971
- **hematology-technical-specialist**: Especialista técnico em hematologia

#### **Agentes de Qualidade**
- **quality-systems-specialist**: Sistemas de qualidade ISO 13485
- **traceability-specialist**: Rastreabilidade de requisitos
- **documentation-finalization-specialist**: Finalização de documentação

#### **Agentes Clínicos**
- **clinical-evidence-specialist**: Avaliação de evidências clínicas
- **cep-protocol-specialist**: Protocolos para Comitê de Ética
- **biostatistics-specialist**: Análises bioestatísticas

#### **Orquestração**
- **hemodoctor-orchestrator**: Coordenador central do sistema

Cada agente possui:
- `CLAUDE.md`: Instruções específicas do agente
- `commands.json`: Comandos disponíveis
- Scripts Python quando aplicável

## 📊 Metodologia BMAD

### BMAD-METHOD/
Biomedical Automated Documentation Method - Framework para documentação automatizada:

- Templates de documentos regulatórios
- Ferramentas de validação
- Padrões de rastreabilidade
- Guias de conformidade

## 📈 Status do Projeto

### ✅ Documentos Completos (Status: SUBMISSION READY)

- [x] DMR v2.0 - Device Master Record
- [x] SRS v2.2 - Software Requirements Specification
- [x] SDD v2.0 - Software Design Document
- [x] TRC v2.1 - Traceability Matrix (100% coverage)
- [x] RMP v1.0 - Risk Management Plan
- [x] CER v1.2 - Clinical Evaluation Report (validado)
- [x] TST v1.0 - Test Specification
- [x] PMS v1.1 - Post-Market Surveillance
- [x] SOUP v1.0 - Software of Unknown Provenance Analysis
- [x] SEC v1.0 - Cybersecurity Analysis
- [x] SBOM v1.0 - Software Bill of Materials
- [x] IFU v1.0 - Instructions For Use (PT-BR e EN-US)

### 📝 Relatórios Disponíveis

- Análise completa de agentes
- Comparação de migrações
- Auditoria do sistema
- Dashboard de agentes (HTML)
- Análise de conhecimento do projeto
- Relatórios de consolidação

## 📂 Documentação Adicional

### docs/
Documentação adicional organizada:
- **reports/**: Relatórios de análise, auditorias e avaliações
- **archive/**: Documentos históricos e propostas implementadas
- **ceo-consultant/**: Documentação do CEO Consultant Agent

### scripts/
Scripts de utilidade consolidados:
- **Migração**: `migrate_p0_files.sh`, `migrate_p1_files.sh`
- **Validação**: `validate_p0.sh`, `validate_p1.sh`
- **Análise**: `analyze_hemodoctor_agents.js`, `analyze_project_knowledge.js`
- **Organização**: `reorganize_repository_v2.0.sh`

## 📋 Controle de Versão

Para informações detalhadas sobre versionamento, histórico de mudanças e roadmap, consulte:

📖 **[VERSION.md](VERSION.md)** - Controle completo de versões

**Versão Atual**: `v2.0.0` (12 de Outubro de 2025)

### Próximos Milestones
- **v2.1.0** (19 Out): Submissão ao Comitê de Ética (CEP)
- **v2.2.0** (26 Out): Completar Verificação e Validação
- **v2.3.0** (2 Nov): Procedimentos de Pós-Mercado
- **v3.0.0** (16 Nov): Submissão ANVISA Completa

## 🏥 Contexto Clínico

### Área de Aplicação
- **Especialidade**: Hematologia e Oncologia Hematológica
- **Indicações Clínicas**:
  - Mieloma Múltiplo
  - Linfomas (Hodgkin e Não-Hodgkin)
  - Leucemias (Agudas e Crônicas)
  - Síndromes Mielodisplásicas
  - Outras neoplasias hematológicas

### Classe do Dispositivo
- **Classificação**: Classe III (Alto Risco)
- **Tipo**: SaMD - Software as a Medical Device
- **Função**: Suporte à decisão clínica

## 📚 Referências Científicas

### HEMODOCTOR_REFERENCIAS/

#### Artigos Científicos
- POC JAMIA 5.1 - Proof of Concept publicado
- Dados de coorte
- Métricas primárias e secundárias
- Relatórios de validação

#### Apresentações
- HemoDoctor.pptx - Apresentação principal
- Pacote de Auditoria e Prontidão para Submissão

## 🔒 Conformidade Regulatória

### Normas Aplicadas
- ✅ **ANVISA**: RDC 185/2001, RDC 657/2022
- ✅ **ISO 13485**: Sistema de Gestão da Qualidade
- ✅ **ISO 14971**: Gestão de Riscos
- ✅ **IEC 62304**: Software de Dispositivo Médico
- ✅ **ISO 27001**: Segurança da Informação
- ✅ **IMDRF**: SaMD Guidelines

### Segurança e Privacidade
- Conformidade LGPD
- Análise de cybersecurity completa
- SBOM e VEX atualizados
- Auditoria de componentes SOUP

## 👥 Instituição

**IDOR-SP** (Instituto D'Or de Pesquisa e Ensino)
- Desenvolvimento institucional
- Validação clínica em ambiente real
- Conformidade ética (CEP)

## 📦 Versão Consolidada

Disponível versão empacotada:
- `HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip`
- `HEMODOCTOR_CONSOLIDADO_v2.0_20251010/` (descompactado)

## 📄 Licença

Este é um projeto de documentação técnica e regulatória de dispositivo médico. Todos os direitos reservados.

## 📞 Contato

Para questões sobre o projeto ou submissões regulatórias, entre em contato através dos canais oficiais do IDOR-SP.

---

**Status Atual**: ✅ SUBMISSION READY - Pronto para submissão ANVISA  
**Última Atualização**: 12 de Outubro de 2025  
**Versão da Documentação**: v2.0.0  
**Completude Geral**: 75% (8/10 módulos completos)
