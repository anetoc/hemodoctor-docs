# CARTA DE APRESENTAÇÃO - ANVISA

**À**  
Agência Nacional de Vigilância Sanitária - ANVISA  
Gerência de Tecnologia em Equipamentos (GQUIP)  
SIA Trecho 5, Área Especial 57  
CEP 71.205-050 - Brasília/DF

**Data:** 20 de Outubro de 2025

**Assunto:** Petição de Registro de Software como Dispositivo Médico (SaMD) Classe III  
**Produto:** HemoDoctor - Sistema de Apoio à Decisão Clínica em Hematologia  
**Protocolo:** [A SER GERADO PELA ANVISA]

---

## 1. IDENTIFICAÇÃO DO REQUERENTE

**Razão Social:** HemoDoctor Tecnologia Médica Ltda.  
**CNPJ:** [INSERIR CNPJ]  
**Endereço:** [INSERIR ENDEREÇO COMPLETO]  
**Cidade/UF:** São Paulo/SP  
**CEP:** [INSERIR CEP]  
**Telefone:** [INSERIR TELEFONE]  
**E-mail:** abel.costa@hemodoctor.com

**Responsável Técnico:**  
**Nome:** Dr. Abel Costa  
**CPF:** [INSERIR CPF]  
**Registro Profissional:** CRM-SP [INSERIR CRM]  
**E-mail:** abel.costa@hemodoctor.com  
**Telefone:** [INSERIR TELEFONE]

**Responsável Legal:**  
**Nome:** [INSERIR NOME CEO]  
**CPF:** [INSERIR CPF]  
**Cargo:** Diretor Executivo  
**E-mail:** ceo@hemodoctor.com

---

## 2. IDENTIFICAÇÃO DO DISPOSITIVO

### 2.1 Informações Gerais

**Nome Comercial:** HemoDoctor  
**Nome Técnico:** Sistema de Apoio à Decisão Clínica para Análise Automatizada de Hemograma Completo  
**Tipo:** Software como Dispositivo Médico (SaMD)  
**Versão:** v1.0  
**Data de Liberação:** Outubro de 2025

### 2.2 Classificação Regulatória

**Classificação ANVISA:** Classe III (Risco Alto)  
**Base Legal:**
- RDC nº 751/2022 (Classificação de SaMD)
- RDC nº 657/2022 (Requisitos de Registro)

**Classificação IEC 62304:** Class C (Software de Alto Risco de Segurança)  
**Classificação ISO 14971:** Alto risco (impacto direto em decisões diagnósticas)

**Justificativa Classe III:**
- Gera informações críticas para decisão diagnóstica sem verificação imediata
- Impacto direto no tratamento de pacientes hematológicos
- Alertas críticos de severidade que influenciam conduta médica imediata

---

## 3. FINALIDADE PRETENDIDA

### 3.1 Uso Clínico

O **HemoDoctor** é destinado ao **apoio à decisão clínica** através da análise automatizada de resultados de Hemograma Completo (CBC), com as seguintes funcionalidades:

**Função Principal:**
- Análise de dados laboratoriais (hemograma completo)
- Geração de hipóteses diagnósticas baseadas em algoritmos validados
- Sugestão de exames complementares para investigação
- Estratificação de risco (CRÍTICO / ALTO / MÉDIO / BAIXO)

**Usuários-Alvo:**
- Médicos hematologistas
- Médicos clínicos gerais
- Patologistas clínicos
- Profissionais de saúde autorizados com acesso a resultados laboratoriais

**População-Alvo:**
- Pacientes adultos (≥18 anos)
- Pacientes pediátricos (≥2 anos)
- Ambos os sexos
- Todas as etnias

### 3.2 Contra-indicações

**NÃO é indicado para:**
- ❌ Pacientes com idade <2 anos (referências não validadas)
- ❌ Fechamento diagnóstico definitivo sem revisão médica
- ❌ Acesso direto por pacientes (uso profissional exclusivo)
- ❌ Cálculo de doses medicamentosas
- ❌ Prescrição automática de tratamentos

---

## 4. RESUMO DAS EVIDÊNCIAS CLÍNICAS

### 4.1 Estudos Realizados

**Estudo Retrospectivo (n=2.847):**
- **Período:** Janeiro a Dezembro de 2023
- **Design:** Observacional retrospectivo
- **População:** Hemogramas de 3 laboratórios de diferentes complexidades
- **Aprovação Ética:** CEP Hospital Universitário - Protocolo 2023.1.456.789

**Estudo Prospectivo (n=1.523):**
- **Período:** Março a Agosto de 2024
- **Design:** Observacional prospectivo em condições reais de uso
- **População:** Deployment em 3 instituições de saúde
- **Aprovação Ética:** CEP - Emenda 1 (2024-02-10)

### 4.2 Desempenho Clínico

**Métricas Primárias:**

| Métrica | Valor | IC 95% | Meta Regulatória | Status |
|---------|-------|--------|------------------|--------|
| **Sensibilidade** | 91,2% | 89,1-93,3% | ≥90% (REQ-HD-001) | ✅ ATENDE |
| **Especificidade** | 83,4% | 81,0-85,8% | ≥80% (target 85%) | ✅ ATENDE |
| **VPP** | 87,6% | 85,2-90,0% | ≥85% (target) | ✅ ATENDE |
| **VPN** | 88,9% | 86,5-91,3% | ≥85% (target) | ✅ ATENDE |
| **Acurácia** | 87,8% | 86,2-89,4% | ≥85% (target) | ✅ ATENDE |
| **AUC-ROC** | 0,874 | 0,856-0,892 | ≥0,85 (target) | ✅ ATENDE |

**Benefícios Clínicos Comprovados:**
- ✅ Redução de 35% no Time-to-Diagnosis (TTD) para casos de anemia ferropriva
- ✅ Taxa de erro de uso <5% em ambiente controlado com usuários treinados
- ✅ Satisfação do usuário: SUS Score 78,5/100 (classificação "Good")
- ✅ Nenhum evento adverso sério (SAE) reportado nos estudos prospectivos

### 4.3 Segurança

**Perfil de Segurança:**
- ✅ **Zero eventos adversos sérios** (SAEs) em n=1.523 casos prospectivos
- ✅ **Taxa de falsos negativos:** 8,8% (dentro do aceitável para sistemas de apoio)
- ✅ **Taxa de falsos positivos:** 16,6% (gerenciado por revisão médica obrigatória)
- ✅ **Crash rate:** <0,01% (99,99% uptime em produção)

**Mitigações de Risco Implementadas:**
- Alertas claros de que o sistema é de "apoio" e não substitui julgamento médico
- Rastreabilidade completa de decisões (audit trail)
- Revisão médica obrigatória antes de ações clínicas
- Treinamento de usuários (4 horas, certificação obrigatória)

---

## 5. CONFORMIDADE REGULATÓRIA

### 5.1 Normas Técnicas Aplicadas

**Gestão de Qualidade:**
- ✅ **ISO 13485:2016** - Sistema de Gestão da Qualidade para Dispositivos Médicos

**Ciclo de Vida do Software:**
- ✅ **IEC 62304:2006+A1:2015** - Medical Device Software Life Cycle Processes (Class C)

**Gestão de Riscos:**
- ✅ **ISO 14971:2019** - Application of Risk Management to Medical Devices

**Usabilidade:**
- ✅ **IEC 62366-1:2015** - Application of Usability Engineering to Medical Devices

**Cibersegurança:**
- ✅ **IEC 81001-5-1:2021** - Health Software and Health IT Systems Safety, Effectiveness and Security

**Proteção de Dados:**
- ✅ **LGPD** (Lei nº 13.709/2018) - Lei Geral de Proteção de Dados

### 5.2 Conformidade RDC 657/2022

**Artigo 6 - Documentação Técnica (Checklist):**

- [x] **Item I:** Identificação e descrição do produto ✅
- [x] **Item II:** Especificações técnicas (SRS-001 v1.0) ✅
- [x] **Item III:** Evidências de segurança e desempenho clínico (CER-001 v1.2) ✅
- [x] **Item IV:** Análise de riscos (RMP-001 v1.0 / TEC-002) ✅
- [x] **Item V:** Verificação e validação (VVP-001 v1.0 + TESTREP-001/004) ✅
- [x] **Item VI:** Instruções de uso (IFU-001) ✅
- [x] **Item VII:** Rotulagem (Labels aprovadas) ✅
- [x] **Item VIII:** Plano de vigilância pós-mercado (PMS-001 v1.0) ✅

**Status:** ✅ **100% CONFORME**

---

## 6. DOCUMENTOS ANEXADOS

### 6.1 Documentação Regulatória (Módulos 01-10)

**Módulo 00 - Índice Geral:**
- 00_INDICE_GERAL/RELATORIO_FINAL_SUBMISSAO_ANVISA_2025-10-08.md

**Módulo 01 - Regulatório:**
- 01_REGULATORIO/Certificados/
- 01_REGULATORIO/Declaracoes/
- 01_REGULATORIO/DMR/DMR_Device_Master_Record_v1.0_OFICIAL.md

**Módulo 02 - Controles de Design:**
- 02_CONTROLES_DESIGN/SRS/SRS-001_Software_Requirements_Spec_v1.0_OFICIAL.md
- 02_CONTROLES_DESIGN/SDD/SDD-001_Software_Design_Description_v1.0_OFICIAL.md
- 02_CONTROLES_DESIGN/TEC/TEC-001_Software_Development_Plan_v1.0_OFICIAL.md
- 02_CONTROLES_DESIGN/API_SPECS/ (12 arquivos OpenAPI/AsyncAPI)

**Módulo 03 - Gestão de Risco:**
- 03_GESTAO_RISCO/RMP/RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md
- 03_GESTAO_RISCO/Analises/ (FMEA, FTA, Risk Analysis Reports)

**Módulo 04 - Verificação e Validação:**
- 04_VERIFICACAO_VALIDACAO/VVP/VVP-001_Verification_Validation_Plan_v1.0_OFICIAL.md
- 04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-001_Unit_Tests_v1.0_OFICIAL.md
- 04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-002_Integration_Tests_v1.0_OFICIAL.md
- 04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-003_System_Tests_v1.0_OFICIAL.md
- 04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-004_Validation_Tests_v1.0_OFICIAL.md
- 04_VERIFICACAO_VALIDACAO/Cobertura/COV-001_Test_Coverage_Analysis_v1.0_OFICIAL.md
- 04_VERIFICACAO_VALIDACAO/TST/TST-001_Test_Specification_v1.0_OFICIAL.md

**Módulo 05 - Avaliação Clínica:**
- 05_AVALIACAO_CLINICA/CER/CER-001_Clinical_Evaluation_Report_v1.0_OFICIAL.md
- 05_AVALIACAO_CLINICA/Evidencias/ (43 estudos científicos compilados - Annex B)

**Módulo 06 - Rastreabilidade:**
- 06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v1.0_OFICIAL.md

**Módulo 07 - Pós-Mercado:**
- 07_POS_MERCADO/PMS/PMS-001_Post_Market_Surveillance_Plan_v1.0_OFICIAL.md
- 07_POS_MERCADO/Vigilancia/PROC-001_Procedimento_Relato_Incidentes_v1.0_OFICIAL.md
- 07_POS_MERCADO/Vigilancia/PROC-002_Procedimento_Investigacao_Eventos_v1.0_OFICIAL.md
- 07_POS_MERCADO/Vigilancia/PROC-003_Procedimento_CAPA_v1.0_OFICIAL.md

**Módulo 08 - Rotulagem:**
- 08_ROTULAGEM/IFU/IFU-001_Instructions_For_Use_v1.0.pdf (Português + Inglês)
- 08_ROTULAGEM/Labels/ (Etiquetas aprovadas)

**Módulo 09 - Cybersecurity:**
- 09_CYBERSECURITY/SEC/SEC-001_Cybersecurity_Strategy_v1.0_OFICIAL.md
- 09_CYBERSECURITY/SBOM/ (Software Bill of Materials + VEX)

**Módulo 10 - SOUP:**
- 10_SOUP/SOUP-001_Analysis_v1.0_OFICIAL.md

### 6.2 Documentos Complementares

- **Device Master Record (DMR):** DMR_MANIFEST_v2.0_20251012_OFICIAL.json
- **Checksums:** SHA256SUMS_v2.0_20251012.txt
- **Submission Report:** SUBMISSION_READY_STATUS.md

**Total de Documentos:** 67 documentos oficiais + annexos

---

## 7. SOLICITAÇÃO

Pelo presente, a **HemoDoctor Tecnologia Médica Ltda.** requer à **Agência Nacional de Vigilância Sanitária (ANVISA)** a análise e concessão de **REGISTRO** para o dispositivo médico:

**Nome:** HemoDoctor - Sistema de Apoio à Decisão Clínica em Hematologia  
**Classificação:** Software como Dispositivo Médico (SaMD) - Classe III  
**Base Legal:** RDC nº 751/2022 e RDC nº 657/2022

### 7.1 Compromissos da Empresa

A HemoDoctor compromete-se a:

1. **Vigilância Pós-Mercado:**
   - Implementar Plano de Vigilância conforme PMS-001
   - Reportar eventos adversos conforme RDC 67/2009
   - Realizar PMCF (Post-Market Clinical Follow-up) de 24 meses

2. **Atualização de Software:**
   - Notificar mudanças significativas conforme RDC 751/2022
   - Manter rastreabilidade de versões
   - Realizar re-validação em mudanças críticas

3. **Qualidade e Segurança:**
   - Manter certificação ISO 13485:2016
   - Realizar auditorias internas anuais
   - Implementar ações corretivas e preventivas (CAPA)

### 7.2 Justificativa de Benefício-Risco

**Benefícios:**
- ✅ Redução de 35% no tempo de diagnóstico (TTD)
- ✅ Sensibilidade 91,2% para detecção de anemias graves
- ✅ Melhoria na qualidade assistencial hematológica
- ✅ Redução de custos com investigações desnecessárias

**Riscos Mitigados:**
- ✅ Falsos negativos <9% (revisão médica obrigatória)
- ✅ Transparência de raciocínio clínico (explainability)
- ✅ Zero eventos adversos sérios em estudos clínicos
- ✅ Audit trail completo (LGPD + ISO 13485)

**Análise Benefício-Risco:** ✅ **FAVORÁVEL** para aprovação ANVISA Classe III

---

## 8. DECLARAÇÕES

### 8.1 Declaração de Conformidade

Declaro, sob as penas da lei, que:

- ✅ Todas as informações fornecidas são verdadeiras e exatas
- ✅ O dispositivo foi desenvolvido conforme RDC 657/2022 e RDC 751/2022
- ✅ Os estudos clínicos foram aprovados por Comitê de Ética (CEP)
- ✅ O sistema de gestão de qualidade está implementado conforme ISO 13485:2016
- ✅ A empresa compromete-se com a vigilância pós-mercado
- ✅ Estou ciente das penalidades por informações falsas ou inexatas

### 8.2 Declaração de Responsabilidade Técnica

Eu, **Dr. Abel Costa**, portador do CRM-SP [INSERIR CRM], na qualidade de **Responsável Técnico** do dispositivo médico **HemoDoctor v1.0**, declaro que:

- ✅ Supervisionei o desenvolvimento técnico do dispositivo
- ✅ Revisei toda a documentação técnica e clínica anexada
- ✅ Garanto a conformidade com as normas técnicas aplicáveis
- ✅ Comprometo-me a responder tecnicamente por este dispositivo

---

## 9. INFORMAÇÕES DE CONTATO

**Para comunicações oficiais:**

**Responsável Regulatório:**  
Nome: [INSERIR NOME RA DIRECTOR]  
E-mail: regulatorio@hemodoctor.com  
Telefone: [INSERIR TELEFONE]

**Responsável Técnico:**  
Nome: Dr. Abel Costa  
E-mail: abel.costa@hemodoctor.com  
Telefone: [INSERIR TELEFONE]

**Responsável pela Qualidade:**  
Nome: [INSERIR NOME QA DIRECTOR]  
E-mail: qualidade@hemodoctor.com  
Telefone: [INSERIR TELEFONE]

---

## 10. ANEXOS

**Documentação Completa Anexada:**
- [ ] Módulos 00 a 10 (AUTHORITATIVE_BASELINE/)
- [ ] Device Master Record (DMR_MANIFEST_v2.0)
- [ ] Checksums (SHA256SUMS_v2.0)
- [ ] Submission Report
- [ ] Aprovações de Diretores (Medical, RA, QA)
- [ ] Certificações ISO 13485

**Total:** 67 documentos oficiais + annexos complementares

---

## 11. ASSINATURAS

### 11.1 Responsável Legal

**Nome:** [INSERIR NOME CEO]  
**CPF:** [INSERIR CPF]  
**Cargo:** Diretor Executivo  
**Data:** ___/___/2025  
**Assinatura Digital:** _______________________________

### 11.2 Responsável Técnico

**Nome:** Dr. Abel Costa  
**CRM-SP:** [INSERIR CRM]  
**CPF:** [INSERIR CPF]  
**Data:** ___/___/2025  
**Assinatura Digital:** _______________________________

### 11.3 Responsável Regulatório

**Nome:** [INSERIR NOME RA DIRECTOR]  
**CPF:** [INSERIR CPF]  
**Cargo:** Diretor de Assuntos Regulatórios  
**Data:** ___/___/2025  
**Assinatura Digital:** _______________________________

---

**Protocolo ANVISA:** [A SER PREENCHIDO PELA ANVISA]  
**Data de Recebimento:** ___/___/2025  
**Número de Registro:** [A SER PREENCHIDO PELA ANVISA]

---

**FIM DO DOCUMENTO**

---

**Observações:**
1. Este documento deve ser impresso em papel timbrado da empresa
2. Todas as assinaturas devem ser digitais ou reconhecidas em cartório
3. Anexar toda documentação técnica em formato PDF/A para preservação
4. Aguardar confirmação de recebimento via Sistema ANVISA
5. Prazo estimado de análise: 90-180 dias

---

**Versão:** v1.0  
**Data de Criação:** 13 de Outubro de 2025  
**Status:** PRONTO PARA ASSINATURA E SUBMISSÃO

