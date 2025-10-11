# HemoDoctor - Sistema de Documentação Regulatória para Oncologia Hematológica

## 📋 Visão Geral

HemoDoctor é um sistema completo de documentação técnica e regulatória para dispositivos médicos na área de oncologia hematológica, especificamente focado em neoplasias hematológicas.

## 🎯 Características Principais

- **Scout Clinical Trials**: Sistema integrado para busca e análise de ensaios clínicos
- **Validação Automática**: Validação inteligente de dados de NCTs com ClinicalTrials.gov
- **Processamento de PDFs**: Análise local e segura de protocolos (Olympia-4)
- **Integração N8N**: Workflows automatizados no N8N IDOR.org
- **Sistema de Agentes**: Múltiplos agentes especializados para diferentes aspectos regulatórios

## 🏗️ Estrutura do Projeto

### AUTHORITATIVE_BASELINE/
Base autoritativa de documentação regulatória organizada em 10 módulos:

1. **00_INDICE_GERAL**: Índices e documentação geral
2. **01_REGULATORIO**: Certificações, declarações, DMR, QMS
3. **02_CONTROLES_DESIGN**: Arquitetura, API specs, SDD, SRS, TEC
4. **03_GESTAO_RISCO**: Análises de risco, matrizes, RMP
5. **04_VERIFICACAO_VALIDACAO**: Testes, cobertura, relatórios
6. **05_AVALIACAO_CLINICA**: CER, evidências clínicas, literatura
7. **06_RASTREABILIDADE**: Matrizes de rastreabilidade
8. **07_POS_MERCADO**: PMS, vigilância pós-mercado
9. **08_ROTULAGEM**: IFU, labels
10. **09_CYBERSECURITY**: SBOM, análises de segurança
11. **10_SOUP**: Análise de Software of Unknown Provenance

### HEMODOCTOR_AGENTES/
Sistema de agentes especializados:

- **anvisa-regulatory-specialist**: Especialista em regulamentação ANVISA
- **biostatistics-specialist**: Análises bioestatísticas
- **cep-protocol-specialist**: Protocolos CEP
- **clinical-evidence-specialist**: Evidências clínicas
- **documentation-finalization-specialist**: Finalização de documentação
- **external-regulatory-consultant**: Consultoria regulatória externa
- **hematology-technical-specialist**: Especialista técnico em hematologia
- **hemodoctor-orchestrator**: Orquestrador do sistema
- **quality-systems-specialist**: Sistemas de qualidade
- **regulatory-review-specialist**: Revisão regulatória
- **risk-management-specialist**: Gestão de riscos
- **software-architecture-specialist**: Arquitetura de software
- **traceability-specialist**: Rastreabilidade

### BMAD-METHOD/
Metodologia BMAD (Biomedical Automated Documentation) com ferramentas e templates.

## 🚀 Sistema Scout Clinical Trials

### Funcionalidades
- ✅ Chat AI com reconhecimento de linguagem natural
- ✅ Extração automática de entidades (idade, diagnóstico)
- ✅ Análise de compatibilidade paciente-estudo
- ✅ Processamento seguro de PDFs localmente
- ✅ Validação automática com ClinicalTrials.gov API
- ✅ Score de qualidade (0-100) com bloqueio automático < 30
- ✅ 0% chance de NCTs inválidos no workflow

### Endpoints Ativos (N8N IDOR.org)
- `ask-ai`: Chat inteligente em português
- `analyze-pdf`: Análise de protocolos
- `scout-clinical-trials`: Busca de ensaios clínicos

### Status de Validação
71% dos estudos confirmados via API ClinicalTrials.gov:

**Confirmados:**
- NCT06500884 (Talquetamab MonumenTAL)
- NCT05083169 (Teclistamab MajesTEC)
- NCT05317416 (Elranatamab MagnetisMM)
- NCT02303821 (Carfilzomib ALL)

## 📊 Relatórios e Análises

O projeto inclui diversos relatórios de análise:
- Análise de agentes do sistema
- Comparação de migração
- Auditoria do sistema
- Análise de conhecimento do projeto
- Dashboard de agentes

## 🔒 Segurança e Privacidade

- Processamento local de documentos sensíveis
- Análise segura de PDFs
- Sem exposição de dados de pacientes
- Conformidade com regulamentações ANVISA

## 🏥 Contexto Clínico

Desenvolvido no IDOR-SP (Instituto D'Or de Pesquisa e Ensino) com foco em:
- Mieloma Múltiplo
- Linfomas
- Leucemias
- Outras neoplasias hematológicas

## 👥 Principais Investigadores

- Dr. Abel Costa (IDOR-SP)
- Dr. Eduardo Rego

## 📝 Licença

Este é um projeto de documentação técnica e regulatória médica. Todos os direitos reservados.

## 🔗 Links Importantes

- N8N IDOR: https://n8n.idor.org
- Workflow ID: dXlTWy6FOjwUC6R4

---

**Status**: Sistema 100% funcional e deployado
**Última Atualização**: Outubro 2025

