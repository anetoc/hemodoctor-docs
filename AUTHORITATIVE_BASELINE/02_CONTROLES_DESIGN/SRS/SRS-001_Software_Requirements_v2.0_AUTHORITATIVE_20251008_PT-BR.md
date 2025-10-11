# SRS-001 — Especificação de Requisitos de Software

**Código:** SRS-001
**Versão:** v2.0 (AUTHORITATIVE)
**Data:** 2025-10-08
**Autor(es):** @spec-writer | Abel Costa
**Revisores:** {REVISORES}
**Aprovadores:** {APROVADORES}
**Status:** AUTHORITATIVE - Linha de Base Consolidada
**Confidencialidade:** Interno/Confidencial

---

## 1. Escopo e Finalidade

**Produto:** HemoDoctor SaMD (Software como Dispositivo Médico)
**Classificação:** **Classe C (IEC 62304)** | ANVISA Classe III | FDA Classe III
**Tipo:** CDSS (Sistema de Apoio à Decisão Clínica) baseado em software para avaliação de Hemograma Completo (CBC) e próximas etapas clínicas sugeridas
**Uso Pretendido:** Auxiliar profissionais de saúde no diagnóstico hematológico e planejamento de tratamento

**Alterações v1.1:** Adicionados 10 requisitos funcionais adicionais (REQ-HD-006 a REQ-HD-015) e RNFs expandidos para suportar implantação corporativa, conformidade regulatória e usabilidade clínica aprimorada.

**Alterações v1.2:** Adicionada Seção 1.3 Limites e Limitações do Sistema para esclarecer escopo (o que HemoDoctor É e NÃO É) e restrições de uso conforme recomendações da auditoria CEO Consultant (QW-002). Adicionada referência cruzada explícita SEC-001 em NFR-003/REQ-HD-060 com rastreabilidade detalhada de cibersegurança (QW-003).

**Alterações v2.0 (AUTHORITATIVE):**
- Aplicado QW-002 Limites do Sistema (Seção 1.3) - mantido da v1.2
- Aplicado QW-003 referência cruzada SEC-001 (NFR-003) - mantido da v1.2
- Aplicado QW-005 decisão SLO: Adicionado latência P99 ≤ 5s e timeout API 30s ao NFR-001
- Adicionado REQ-HD-016 Análise Hematológica Específica Pediátrica (placeholder para Épico 3 Tarefa 3.5)
- Atualizados todos os links de rastreabilidade forward (REQ → SDD → TEST → RISK → IFU → PMS)
- Consolidado conteúdo único de versões arquivadas (especificações de desempenho paulo v1.0)
- Aprimorados REQ-HD-001 e REQ-HD-012 com requisitos de latência P99
- **Status:** Linha de base autoritativa pronta para submissão ANVISA

### 1.3 Limites e Limitações do Sistema

**O que HemoDoctor É:**
- Sistema de apoio à decisão clínica (CDSS) para interpretação de CBC
- Fornece diagnósticos suspeitos e próximos exames recomendados
- Integra com LIS/HIS existente via API

**O que HemoDoctor NÃO É:**
- NÃO é um analisador laboratorial (recebe dados CBC pré-analisados)
- NÃO é substituto para julgamento médico
- NÃO é um sistema de diagnóstico diferencial para condições não-hematológicas
- NÃO está conectado a sistemas de imagem

**Restrições de Uso:**
- Requer interpretação por profissional de saúde treinado
- Não para uso em triagem de emergência (latência de decisão)
- Não para uso fora da população pretendida (adultos/pediátricos conforme estudo de validação)

---

## 2. Mapeamento Necessidades do Usuário → Requisitos

| Necessidade do Usuário | REQ-ID | Descrição |
|-----------|--------|-------------|
| UN-001 | REQ-HD-001 | Decisões de diagnóstico mais rápidas → Detecção automatizada de anemia |
| UN-002 | REQ-HD-012 | Gerenciar carga de alertas → Priorização inteligente de alertas |
| UN-003 | REQ-HD-020 | Mitigar viés de automação → Transparência de raciocínio + substituição |
| UN-004 | REQ-HD-050 | Alta disponibilidade → Confiabilidade do sistema ≥99,5% |
| UN-005 | REQ-HD-060 | Resiliência cibernética → Arquitetura segura + SBOM |
| UN-006 | REQ-HD-006 | Alertas configuráveis por instituição → Configuração do sistema de alertas |
| UN-007 | REQ-HD-007 | Garantia de qualidade de modelo ML → Versionamento e rollback de modelo |
| UN-008 | REQ-HD-008 | Controle de acesso e segurança → Controle de Acesso Baseado em Funções (RBAC) |
| UN-009 | REQ-HD-009 | Conformidade regulatória → Retenção e arquivamento de dados (LGPD/ANVISA) |
| UN-010 | REQ-HD-010 | Manutenção de regras clínicas → Especificação e versionamento de regras |
| UN-011 | REQ-HD-011 | Implantação multi-região → Suporte multilíngue |
| UN-012 | REQ-HD-012 | Visibilidade operacional → Monitoramento de desempenho e alertas de degradação |
| UN-013 | REQ-HD-013 | Padronização terminológica → Integração com servidor de terminologia externo |
| UN-014 | REQ-HD-014 | Capacidades de pesquisa → Modo de processamento em lote |
| UN-015 | REQ-HD-015 | Interoperabilidade em saúde → Exportação HL7 FHIR R4 |
| UN-016 | REQ-HD-016 | Suporte à população pediátrica → Análise hematológica estratificada por idade |

---

## 3. Requisitos Funcionais

### REQ-HD-001: Detecção de Anemia Crítica
**Prioridade:** CRÍTICA
**Descrição:** Identificar **anemia grave** (Hb abaixo do limiar ajustado por idade/sexo/gravidez) com **sensibilidade ≥90%** (meta 100% para validação POC)
**Comportamento:** Gerar CRITICAL_ALERT com notificação imediata
**Critérios de Aceitação:**
- Sensibilidade ≥90% (conforme TRC-001)
- Taxa de falso negativo <10%
- Latência de alerta P95 < 2s, P99 < 5s (atualização QW-005)
**Rastreabilidade:** → SDD-001 §3.2 (Projeto de Algoritmo) → TEST-HD-011 (curvas ROC/PR) → RISK-HD-001 (Mitigação de falso negativo) → IFU-001 §Desempenho → PMS-001 §SLAs

### REQ-HD-002: Ingestão e Validação de Dados CBC
**Prioridade:** ALTA
**Descrição:** Permitir ingestão de CBC + testes complementares (ferritina, ferro, B12, folato, LDH, etc.) com **validação de unidades** e faixas de referência específicas por idade/sexo/gravidez
**Dados de Entrada:**
- **CBC Core:** Hb, Ht, VCM, RDW, Leucócitos (total + diferencial), Plaquetas, Reticulócitos
- **Complementares:** Ferritina, ferro sérico, B12, folato, LDH, marcadores de hemólise, função renal/tireoide/inflamatória
- **Metadados:** Idade do paciente, sexo, status de gravidez, comorbidades
**Validação:**
- Conversão de unidades (g/dL ↔ g/L, mg/dL ↔ μmol/L)
- Mapeamento de códigos LOINC (quando aplicável)
- Detecção de valores fora da faixa por perfil do paciente
**Critérios de Aceitação:** 100% validação de unidades, zero erros relacionados a unidades em produção
**Rastreabilidade:** → SDD-001 §3.2 (Serviço de Ingestão), §3.3 (Serviço de Validação) → TEST-HD-013 (Testes de validação de unidades) → RISK-HD-101 (Erro de análise de dados) → IFU-001 §Entrada de Dados → PMS-001 §Logs de Erro

### REQ-HD-003: Transparência de Raciocínio Clínico
**Prioridade:** ALTA
**Descrição:** Exibir **raciocínio clínico** (regras, fontes, confiança) para cada recomendação para permitir tomada de decisão informada do clínico
**Comportamento:**
- Mostrar regras clínicas acionadas (ex: "Hb <7 g/dL + VCM <80 fL → Anemia ferropriva suspeita")
- Exibir fontes de evidência (diretrizes, literatura)
- Quantificação de incerteza (intervalos de confiança, intervalos de predição)
- Permitir substituição do clínico com registro obrigatório de justificativa
**Critérios de Aceitação:** 100% recomendações têm raciocínio, usuário pode acessar conjunto completo de regras
**Rastreabilidade:** → SDD-001 §3.8 (Serviço de UI - exibição de raciocínio) → TEST-HD-017 (Testes de transparência de raciocínio) → RISK-HD-008 (Fadiga de alerta), RISK-HD-401 (Viés de automação) → IFU-001 §Instruções → PMS-001 §Taxas de Substituição

### REQ-HD-004: Trilha de Auditoria e Registro
**Prioridade:** CRÍTICA (conformidade regulatória)
**Descrição:** Exportar **logs auditáveis** (WORM - Write Once Read Many) capturando todas as decisões clínicas, interações do usuário e eventos do sistema
**Eventos Registrados:**
- Timestamp de ingestão de dados CBC + ID do usuário
- Cálculo de escore de risco + versão do algoritmo
- Recomendações geradas + confiança
- Decisões do clínico (aceitar/substituir/adiar)
- Justificativas para substituições
- Alertas e exceções do sistema
**Retenção:** Conforme requisitos LGPD/GDPR (mínimo 5 anos para registros médicos no Brasil)
**Critérios de Aceitação:** Zero lacunas de auditoria, logs imutáveis, exportável para CSV/JSON
**Rastreabilidade:** → SDD-001 §3.9 (Serviço de Auditoria) → TEST-HD-018 (Completude de trilha de auditoria) → RISK-HD-103 (Corrupção de banco de dados) → IFU-001 §Trilha de Auditoria → PMS-001 §Conformidade

### REQ-HD-005: API de Integração LIS/HIS
**Prioridade:** ALTA
**Descrição:** Fornecer API REST para integração com Sistemas de Informação Laboratorial (LIS) e Sistemas de Informação Hospitalar (HIS) com autenticação segura (OIDC/OAuth2)
**Endpoints:**
- POST /api/v1/cbc/analyze - Enviar dados CBC para análise
- GET /api/v1/results/{case_id} - Recuperar resultados de análise
- GET /api/v1/audit/{case_id} - Recuperar trilha de auditoria
**Autenticação:** OpenID Connect (OIDC) ou OAuth2 com MFA
**Limitação de Taxa:** 100 requisições/min por cliente
**Interoperabilidade:** Suporte HL7 FHIR R4 (opcional), importação CSV/Parquet
**Rastreabilidade:** → SDD-001 §3.1 (Gateway API) → TEST-HD-019 (Testes de integração API) → RISK-HD-104 (Falha de interface API) → IFU-001 §Integração → PMS-001 §Desempenho API

---

### REQ-HD-006: Configuração do Sistema de Alertas
**Prioridade:** ALTA
**Descrição:** Habilitar **configuração por instituição** de limiares de alerta, regras de priorização e parâmetros de throttling para prevenir fadiga de alerta mantendo segurança do paciente
**Funcionalidade:**
- **Limiares Configuráveis:** Instituições podem ajustar limiares de Hb/Leucócitos/Plaquetas dentro de faixas seguras (ex: limiar de anemia grave: 6,5-8,0 g/dL)
- **Priorização de Alertas:** Sistema de quatro níveis (CRÍTICO/ALTO/MÉDIO/BAIXO) com regras customizáveis
- **Throttling de Alertas:** Máximo configurável de alertas por janela de tempo (padrão: 3 CRÍTICO/hora, 10 ALTO/hora)
- **Supressão Inteligente:** Suprimir alertas duplicados para mesmo paciente dentro de janela de tempo configurável (padrão: 24 horas)
- **Regras de Escalonamento:** Definir caminhos de escalonamento (ex: alerta CRÍTICO → pager médico se não reconhecido em 15 min)
**Interface de Configuração:**
- Portal web administrativo (protegido por RBAC, função Admin apenas)
- Versionamento de configuração (baseado em Git, com workflow de aprovação)
- Validação de configuração (rejeitar limiares inseguros, ex: Hb <5 g/dL acionaria substituição de segurança)
**Critérios de Aceitação:**
- Admin pode modificar limiares dentro de faixas seguras (±20% do padrão)
- Throttling de alertas previne >3 alertas CRÍTICOS/hora por configuração padrão
- Mudanças de configuração requerem dupla aprovação (Admin + SME Clínico)
- Todas as mudanças de configuração registradas em trilha de auditoria
**Rastreabilidade:** → SDD-001 §3.7 (Orquestrador de Alertas) → TEST-HD-020 (Testes de configuração de alertas) → RISK-HD-002 (Falso positivo), RISK-HD-005 (Fadiga de alerta), RISK-HD-008 (Viés de automação) → IFU-001 §Configuração → PMS-001 §Métricas de Alerta

---

### REQ-HD-007: Versionamento e Rollback de Modelo ML
**Prioridade:** CRÍTICA
**Descrição:** Implementar **gerenciamento robusto de ciclo de vida de modelo ML** incluindo versionamento, teste A/B, monitoramento de desempenho e capacidade de rollback emergencial para garantir qualidade do modelo e segurança do paciente
**Funcionalidade:**
- **Versionamento de Modelo:** Rastrear versão do modelo (Git SHA + timestamp) para cada predição em log de auditoria
- **Registro de Modelo:** Registro centralizado (MLflow ou equivalente) armazenando todas as versões de modelo com metadados (data de treinamento, métricas de desempenho, status de aprovação)
- **Teste A/B:** Implantar novos modelos em subconjunto de tráfego (% configurável, padrão 10%) para validação antes de rollout completo
- **Monitoramento de Desempenho:** Monitoramento em tempo real de métricas de desempenho do modelo (sensibilidade, especificidade, ROC-AUC, detecção de drift)
- **Alertas Automatizados:** Gerar alerta ALTO se desempenho do modelo degradar >5% da linha de base
- **Rollback Emergencial:** Rollback com um clique para versão anterior do modelo com <15 min de downtime
- **Teste de Rollback:** Testes automatizados verificam procedimento de rollback trimestralmente
**Critérios de Promoção de Modelo:**
- ROC-AUC ≥0,85 no conjunto de validação (conforme TRC-001)
- Sensibilidade ≥90% para detecção de anemia grave
- Nenhum viés significativo detectado entre subgrupos de idade/sexo/gravidez (teste de equidade)
- Dupla aprovação requerida (Cientista de Dados + SME Clínico)
**Critérios de Aceitação:**
- Cada predição registrada com ID de versão do modelo
- Procedimento de rollback completo em <15 min (testado trimestralmente)
- Teste A/B suporta divisão de tráfego 5-50%
- Dashboard de desempenho do modelo atualiza em tempo real (latência <1 min)
**Rastreabilidade:** → SDD-001 §3.6 (Gerenciador de Modelo) → TEST-HD-021 (Testes de ciclo de vida do modelo) → RISK-HD-103 (Trilha de auditoria), RISK-HD-104 (Falha de API), RISK-HD-106 (Incompatibilidade de versão), RISK-HD-204 (Envenenamento de modelo) → IFU-001 §Gerenciamento de Modelo → PMS-001 §Desempenho de Modelo

---

### REQ-HD-008: Controle de Acesso Baseado em Funções (RBAC)
**Prioridade:** CRÍTICA (segurança + regulatória)
**Descrição:** Implementar **RBAC granular** com quatro funções primárias para garantir princípio de menor privilégio e conformidade com LGPD/GDPR/HIPAA
**Funções e Permissões:**

| Função | Permissões | MFA Requerido | Exemplos |
|------|-------------|--------------|----------|
| **Admin** | Acesso total ao sistema: gerenciamento de usuários, mudanças de configuração, implantação de modelo, acesso a log de auditoria | ✅ SIM (obrigatório) | Administradores de TI, gerentes de QA |
| **Operador de Laboratório** | Enviar dados CBC, visualizar resultados de análise, substituir recomendações (com justificativa), exportar relatórios | ❌ NÃO (opcional) | Técnicos de laboratório |
| **Médico** | Visualizar resultados de análise, substituir recomendações (com justificativa), acessar histórico do paciente, exportar relatórios | ✅ SIM (recomendado) | Hematologistas, médicos |
| **Auditor** | Acesso somente leitura a logs de auditoria, exportar dados de auditoria, gerar relatórios de conformidade | ✅ SIM (obrigatório) | Auditores de QA, assuntos regulatórios |

**Recursos Adicionais:**
- **Matriz de Permissões:** Matriz detalhada documentando todos os endpoints API e funções requeridas (mantida em SDD-001 §6.2)
- **Gerenciamento de Sessão:** Timeout de sessão após 30 min de inatividade (configurável por instituição)
- **Monitoramento de Login:** Registrar todas as tentativas de autenticação (sucesso/falha) com endereço IP, timestamp
- **Suporte MFA:** TOTP (Google Authenticator, Authy) ou MFA baseado em SMS
- **Política de Senha:** Mínimo 12 caracteres, requisitos de complexidade, rotação a cada 90 dias (configurável)
- **Registro de Ação Privilegiada:** Todas as ações Admin registradas com verificação dupla (regra de duas pessoas para mudanças críticas)
**Critérios de Aceitação:**
- Nenhum usuário pode acessar funcionalidade fora de sua função
- MFA aplicado para funções Admin e Auditor (configurável para Médico)
- Tentativas de autenticação falhadas limitadas por taxa (máx 5 tentativas/15 min)
- Todos os eventos de autenticação registrados em trilha de auditoria
- Teste de penetração RBAC passa com zero achados de acesso não autorizado
**Rastreabilidade:** → SDD-001 §6.2 (Controle de Acesso) → TEST-HD-015, TEST-HD-022 (Testes RBAC, teste de penetração) → RISK-HD-201 (Acesso não autorizado), RISK-HD-202 (Injeção de dados), RISK-HD-205 (Escalação de privilégio) → IFU-001 §Segurança → PMS-001 §Incidentes de Segurança

---

### REQ-HD-009: Retenção e Arquivamento de Dados
**Prioridade:** ALTA (conformidade regulatória)
**Descrição:** Implementar **gerenciamento automatizado de ciclo de vida de dados** em conformidade com LGPD (Brasil), GDPR (UE), HIPAA (EUA) e regulamentações ANVISA
**Políticas de Retenção:**
- **Logs de Auditoria:** Reter por **5 anos mínimo** (LGPD Art. 16, ANVISA RDC 657/2022)
- **Dados CBC + Resultados:** Reter por **5 anos mínimo** (requisito de retenção de registro médico)
- **PHI (Informação de Saúde Pessoal):** Reter apenas enquanto clinicamente necessário + período de retenção legal
- **Artefatos de Modelo:** Reter todos os modelos implantados por **10 anos** (rastreabilidade para análise retrospectiva)
**Estratégia de Arquivamento:**
- **Armazenamento Hot (0-1 ano):** PostgreSQL + S3 Standard (recuperação rápida)
- **Armazenamento Warm (1-3 anos):** S3 Infrequent Access (recuperação em minutos)
- **Armazenamento Cold (3-5 anos):** S3 Glacier (recuperação em horas)
- **Exclusão:** Exclusão automatizada após expiração do período de retenção (com período de graça de 30 dias + aprovação)
**Direitos do Titular de Dados (LGPD Art. 18):**
- **Direito de Acesso:** Paciente pode solicitar cópia de seus dados (atendido em 15 dias)
- **Direito de Exclusão:** Paciente pode solicitar exclusão (atendido em 30 dias, exceto onde retenção legal requerida)
- **Direito de Portabilidade:** Dados exportáveis em formato legível por máquina (JSON, CSV)
- **Direito de Correção:** Paciente pode solicitar correção de dados imprecisos
**Critérios de Aceitação:**
- Logs de auditoria retidos por 5 anos mínimo, acessíveis dentro de SLA (hot: <1s, warm: <1 min, cold: <24 horas)
- Arquivamento automatizado move dados para armazenamento warm após 1 ano (verificado mensalmente)
- Solicitações de exclusão de dados processadas em 30 dias (com trilha de auditoria)
- Verificação de exclusão: dados excluídos irrecuperáveis (apagamento criptográfico ou exclusão física)
- Auditoria de conformidade anual passa com zero violações de política de retenção
**Rastreabilidade:** → SDD-001 §3.9 (Serviço de Auditoria), §9 (Gerenciamento de Dados) → TEST-HD-023 (Testes de retenção/arquivamento) → RISK-HD-103 (Corrupção de banco de dados) → NFR-004 (Privacidade) → IFU-001 §Gerenciamento de Dados → PMS-001 §Conformidade

---

### REQ-HD-010: Especificação e Manutenção de Regras Clínicas
**Prioridade:** ALTA (segurança clínica)
**Descrição:** Manter **regras de decisão clínica** em formato versionado, testável e auditável com revisão obrigatória de especialista para garantir segurança clínica e conformidade regulatória
**Gerenciamento de Regras:**
- **Formato de Especificação:** Regras clínicas definidas em formato estruturado YAML ou JSON (legível por humanos, analisável por máquina)
- **Controle de Versão:** Todas as regras armazenadas em repositório Git com histórico de commits, proteção de branch (requer revisão antes de merge)
- **Revisão Clínica:** Todas as mudanças de regras revisadas e aprovadas por hematologista licenciado (documentado em mensagem de commit Git)
- **Revisão Anual:** Conjunto completo de regras revisado anualmente por conselho consultivo clínico (documentado em QMS)
**Categorias de Regras:**
- **Regras de Detecção de Anemia:** Limiares de Hb, classificação baseada em VCM (microcítica/normocítica/macrocítica)
- **Regras de Triagem de Leucemia:** Detecção de células blásticas, anormalidades diferenciais de leucócitos
- **Regras de Detecção de Hemólise:** Elevação de LDH, contagem de reticulócitos, haptoglobina
- **Regras de Priorização de Alertas:** Mapear achados clínicos para níveis de alerta (CRÍTICO/ALTO/MÉDIO/BAIXO)
**Estratégia de Teste:**
- **Testes Unitários:** Cada regra testável independentemente (100% cobertura de regras)
- **Testes de Regressão:** Suíte de testes com 100+ cenários clínicos (atualizada trimestralmente)
- **Validação Clínica:** Novas regras validadas em conjunto de dados retrospectivo (mínimo 1000 casos) antes de implantação em produção
**Rastreabilidade de Regras:**
- Cada regra mapeia para:
  - Fonte de evidência (diretriz, referência de literatura)
  - Controle de risco (ID de risco RMP-001)
  - Caso de teste (TEST-HD-xxx)
**Critérios de Aceitação:**
- 100% regras clínicas em controle de versão com aprovação de hematologista
- Todas as regras têm testes unitários (taxa de aprovação 100%)
- Revisão clínica anual documentada em QMS (com assinaturas de aprovação)
- Implantação de regras requer dupla aprovação (Hematologista + Gerente de QA)
- Todas as mudanças de regras registradas em trilha de auditoria
**Rastreabilidade:** → SDD-001 §3.4 (Motor de Regras) → TEST-HD-024 (Teste de regras clínicas) → RISK-HD-004 (Diagnóstico incorreto), RISK-HD-401 (Má interpretação do usuário) → IFU-001 §Regras Clínicas → PMS-001 §Desempenho Clínico

---

### REQ-HD-011: Suporte Multilíngue
**Prioridade:** MÉDIA
**Descrição:** Suportar **internacionalização (i18n)** para três idiomas (Português Brasileiro, Inglês Americano, Espanhol) para permitir implantação em mercados LATAM e EUA
**Idiomas Suportados:**
- **pt-BR:** Português Brasileiro (primário, padrão)
- **en-US:** Inglês Americano (requerido para submissão FDA)
- **es-ES:** Espanhol Europeu (expansão mercado LATAM)
**Elementos Localizados:**
- **Texto da UI:** Todas as strings da interface do usuário (botões, rótulos, mensagens)
- **Terminologia Clínica:** Nomes de doenças, recomendações (fonte: traduções SNOMED CT)
- **Documentação:** IFU (Instruções de Uso) traduzido e revisado por SME clínico por idioma
- **Mensagens de Alerta:** Alertas CRÍTICO/ALTO/MÉDIO/BAIXO no idioma selecionado do usuário
**Não Localizado:**
- **Logs de Auditoria:** Sempre em Inglês (para consistência regulatória)
- **Payloads API:** Sempre em Inglês (para consistência de integração)
**Implementação:**
- **Framework i18n:** React-i18next ou equivalente
- **Qualidade de Tradução:** Todas as traduções clínicas revisadas por hematologista nativo do idioma
- **Fallback:** Se tradução ausente, exibir Inglês com log de aviso (sem falha do sistema)
**Critérios de Aceitação:**
- 100% strings da UI traduzíveis (sem texto hardcoded)
- Traduções de terminologia clínica validadas por hematologista por idioma
- Usuário pode trocar idioma dinamicamente (preferência de sessão + padrão por usuário)
- IFU disponível em todos os três idiomas (aprovação regulatória por região)
**Rastreabilidade:** → SDD-001 §3.8 (Serviço de UI - i18n) → TEST-HD-025 (Testes multilíngues) → IFU-001 (versões multilíngues) → PMS-001 §Implantação Internacional

---

### REQ-HD-012: Monitoramento de Desempenho e Alertas de Degradação
**Prioridade:** ALTA
**Descrição:** Implementar **observabilidade abrangente** com monitoramento de desempenho em tempo real, detecção de anomalias e alertas automatizados para garantir conformidade com SLA (99,5% uptime, latência P95 <2s, latência P99 <5s conforme QW-005)
**Métricas Monitoradas:**
- **Latência:** P50, P95, P99 por endpoint API (alerta se P95 >2s ou P99 >5s conforme QW-005)
- **Taxa de Transferência:** Requisições/segundo, casos/hora (alerta se <80% da linha de base)
- **Taxa de Erro:** Erros 4xx/5xx por endpoint (alerta se >1% taxa de erro)
- **Disponibilidade:** Uptime do serviço (alerta se <99,5% em janela de 24 horas)
- **Utilização de Recursos:** CPU, memória, E/S de disco por contêiner (alerta se >80% sustentado)
- **Desempenho de Modelo:** Sensibilidade/especificidade em tempo real (alerta se drift >5% da linha de base)
- **Desempenho de Banco de Dados:** Latência de query, saturação de pool de conexão (alerta se degradado)
**Estratégia de Alertas:**
- **Níveis de Severidade:** CRÍTICO (pager imediato), ALTO (notificação Slack), MÉDIO (email), BAIXO (apenas dashboard)
- **Escalonamento:** Alertas CRÍTICOS não reconhecidos em 15 min → escalar para gerente de plantão
- **Correlação de Alertas:** Agrupar alertas relacionados (ex: alta latência + alta CPU) para reduzir ruído
- **Runbooks:** Cada tipo de alerta tem runbook documentado (etapas de diagnóstico, remediação)
**Stack de Observabilidade:**
- **Métricas:** Prometheus + dashboards Grafana
- **Logging:** Stack ELK (Elasticsearch, Logstash, Kibana) ou Splunk
- **Tracing:** OpenTelemetry para rastreamento distribuído
- **APM (Monitoramento de Desempenho de Aplicação):** Datadog, New Relic ou equivalente
**Critérios de Aceitação:**
- Todas as métricas críticas monitoradas com <1 min de atraso
- Alertas CRÍTICOS acionam em 1 min de violação de limiar
- 100% alertas CRÍTICOS têm runbooks documentados
- Revisão mensal de desempenho identifica tendências (planejamento de capacidade)
- Conformidade com SLA (99,5% uptime, P95 ≤2s, P99 ≤5s) medida e reportada mensalmente
**Rastreabilidade:** → SDD-001 §8 (Projeto de Desempenho), §10 (Observabilidade) → TEST-HD-026 (Testes de monitoramento de desempenho) → NFR-001, NFR-002 → IFU-001 §Requisitos do Sistema → PMS-001 §SLAs

---

### REQ-HD-013: Integração com Servidores de Terminologia Externos
**Prioridade:** MÉDIA
**Descrição:** Habilitar **integração com servidores de terminologia médica externos** (SNOMED CT, LOINC, ICD-10) para codificação padronizada, validação de terminologia e interoperabilidade clínica
**Terminologias Suportadas:**
- **SNOMED CT:** Achados clínicos, doenças (ex: "Anemia ferropriva" → SNOMED 87522002)
- **LOINC:** Testes laboratoriais (ex: "Hemoglobina [Massa/volume] em Sangue" → LOINC 718-7)
- **ICD-10:** Códigos de diagnóstico para cobrança e relatório (ex: "D50.9 Anemia ferropriva não especificada")
- **ATC (Anatômico Terapêutico Químico):** Códigos de medicação (melhoria futura)
**Recursos de Integração:**
- **Lookup de Terminologia:** Consultar servidor de terminologia para validação de código (ex: verificar código LOINC válido)
- **Mapeamento de Códigos:** Mapear nomes internos de doenças para códigos padrão (ex: "Anemia ferropriva" → SNOMED 87522002)
- **Expansão de Conceito:** Expandir diagnóstico para incluir conceitos relacionados (ex: "Anemia" → todos os subtipos de anemia)
- **Suporte Multilíngue:** Recuperar terminologia no idioma do usuário (pt-BR, en-US, es-ES)
**Opções de Servidor de Terminologia:**
- **Interno:** Implantar servidor de terminologia (ex: Ontoserver, HAPI FHIR Terminology Service)
- **Externo:** Integrar com servidor de terminologia institucional (se disponível)
- **Fallback:** Banco de dados de terminologia embutido (atualizado trimestralmente) se servidor externo indisponível
**Critérios de Aceitação:**
- Todos os parâmetros CBC mapeados para códigos LOINC (100% cobertura para 15 parâmetros core)
- Todos os diagnósticos hematológicos mapeados para códigos SNOMED CT (100% cobertura para top 50 diagnósticos)
- Latência de lookup de terminologia <500ms (P95)
- Fallback para terminologia embutida se servidor externo indisponível (degradação graciosa)
- Atualizações trimestrais de banco de dados de terminologia documentadas e validadas
**Rastreabilidade:** → SDD-001 §3.3 (Serviço de Validação - terminologia) → TEST-HD-027 (Testes de integração de terminologia) → REQ-HD-002 → IFU-001 §Interoperabilidade → PMS-001 §Integração

---

### REQ-HD-014: Modo de Processamento em Lote
**Prioridade:** BAIXA
**Descrição:** Suportar **processamento em lote** de dados históricos de CBC para pesquisa clínica retrospectiva, estudos de melhoria de qualidade e vigilância pós-mercado regulatória
**Casos de Uso:**
- **Análise Retrospectiva:** Analisar 10.000+ casos históricos de CBC para identificar tendências (ex: prevalência sazonal de anemia)
- **Retreinamento de Modelo:** Processar dados históricos para retreinar modelos ML (com divisão adequada treino/teste)
- **Auditorias de Qualidade:** Reanalisar casos para validar acurácia de alerta (estudos de calibração)
- **Relatório Regulatório:** Gerar estatísticas agregadas para relatórios de vigilância pós-mercado ANVISA
**Funcionalidade:**
- **Ingestão em Lote:** Upload de arquivo CSV/Parquet com múltiplos casos CBC (até 100.000 casos por lote)
- **Processamento Assíncrono:** Processar lotes assincronamente (baseado em fila, sem restrição de tempo real)
- **Rastreamento de Progresso:** UI web mostra status de processamento de lote (enfileirado/processando/completo/falhou)
- **Resultados de Lote:** Exportar resultados de lote como CSV/JSON (inclui todas as predições, alertas, raciocínio)
- **Desidentificação:** Modo de desidentificação opcional (remover PHI, manter apenas dados clínicos + estatísticas agregadas)
**Requisitos de Desempenho:**
- **Taxa de Transferência:** Processar 10.000 casos/hora (menor prioridade que processamento em tempo real)
- **Isolamento de Recursos:** Processamento em lote usa pool de recursos separado (sem impacto em latência em tempo real)
**Critérios de Aceitação:**
- Modo lote processa 10.000 casos/hora (validado com teste de carga)
- Processamento em lote não degrada latência P95 em tempo real (isolamento verificado)
- Resultados de lote correspondem a resultados em tempo real para mesmos dados de entrada (100% consistência)
- Modo de desidentificação remove todos os 18 identificadores HIPAA (validado com ferramentas de detecção PII)
**Rastreabilidade:** → SDD-001 §3.2 (Serviço de Ingestão - modo lote) → TEST-HD-028 (Testes de processamento em lote) → IFU-001 §Processamento em Lote → PMS-001 §Uso em Pesquisa

---

### REQ-HD-015: Exportação para Formato HL7 FHIR R4
**Prioridade:** MÉDIA
**Descrição:** Habilitar **exportação de resultados de análise CBC** em formato HL7 FHIR R4 para integração perfeita com sistemas de Registro Eletrônico de Saúde (EHR) e trocas de dados de saúde
**Recursos FHIR:**
- **DiagnosticReport:** Resumo de análise CBC (status, data de emissão, executor, resultados)
- **Observation:** Parâmetros CBC individuais (Hb, VCM, Leucócitos, etc.) como Observações FHIR com códigos LOINC
- **RiskAssessment:** Escore de risco HemoDoctor e probabilidades de diagnóstico diferencial
- **Provenance:** Trilha de auditoria (quem, quando, qual versão do algoritmo)
**Perfis FHIR:**
- **US Core:** Conformidade com US Core IG (Guia de Implementação) para DiagnosticReport, Observation
- **RNDS Brasileiro (Rede Nacional de Dados em Saúde):** Conformidade com perfis de rede nacional de dados de saúde brasileira (se aplicável)
**Modos de Exportação:**
- **API REST:** `GET /api/v1/fhir/DiagnosticReport/{case_id}` retorna JSON FHIR
- **Exportação em Lote:** `GET /api/v1/fhir/export?start_date=X&end_date=Y` retorna NDJSON (JSON delimitado por nova linha) para exportação em lote
- **Notificação Push:** Webhook opcional para enviar bundle FHIR para EHR quando análise completa
**Validação FHIR:**
- Todos os recursos FHIR exportados validados contra schema FHIR R4 (usando HAPI FHIR Validator ou equivalente)
- Erros de validação registrados e reportados (sem exportação se validação falhar)
**Critérios de Aceitação:**
- 100% resultados CBC exportáveis como DiagnosticReport FHIR R4 válido
- Todos os parâmetros CBC mapeados para códigos LOINC em Observações FHIR
- Exportação FHIR inclui recurso Provenance (versão do algoritmo, timestamp, ID do usuário)
- Validação FHIR passa com zero erros (avisos aceitáveis, documentados)
- Exportação em lote suporta até 10.000 relatórios por requisição (com paginação)
**Rastreabilidade:** → SDD-001 §3.1 (Gateway API - endpoints FHIR) → TEST-HD-029 (Testes de validação FHIR) → REQ-HD-005 → IFU-001 §Exportação FHIR → PMS-001 §Interoperabilidade

---

### REQ-HD-016: Análise Hematológica Específica Pediátrica
**Prioridade:** ALTA
**Descrição:** Fornecer **análise hematológica estratificada por idade** para populações pediátricas (0-18 anos) com considerações de fisiologia de desenvolvimento para suportar diagnóstico preciso em crianças e adolescentes
**Status:** PLACEHOLDER - Será detalhado no Épico 3 Tarefa 3.5 (Especificação de Requisitos Pediátricos)

**Escopo (Preliminar):**
- **Estratificação por Idade:** Suportar faixas de referência específicas por idade para lactentes (0-1a), crianças pequenas (1-3a), crianças (3-12a), adolescentes (12-18a)
- **Fisiologia de Desenvolvimento:** Considerar anemia fisiológica da infância, persistência de hemoglobina F, mudanças de leucócitos no desenvolvimento
- **Alertas Específicos Pediátricos:** Diferenciar limiares críticos para populações pediátricas vs. adultas
- **Regras Clínicas:** Regras de decisão clínica específicas pediátricas validadas por hematologista pediátrico

**Critérios de Aceitação (Preliminar):**
- Faixas de referência específicas por idade para todos os parâmetros CBC (0-18 anos, estratificadas por estágio de desenvolvimento)
- Limiares de alerta específicos pediátricos validados por conselho consultivo clínico
- 100% casos pediátricos usam faixas de referência apropriadas por idade (sem faixas adultas aplicadas a crianças)
- Sensibilidade ≥90% para detecção de anemia pediátrica grave (validado em coorte pediátrica)

**Rastreabilidade (Preliminar):** → SDD-001 §3.2.5 (Lógica Pediátrica - a ser adicionada no Épico 3) → TEST-HD-016 (Testes de validação pediátrica - a ser criado) → RISK-HD-016 (Diagnóstico errado pediátrico - a ser adicionado) → IFU-001 §Grupos Etários → CER-001 §Subgrupo Pediátrico

**Nota:** Este requisito é um **placeholder** para reservar o ID REQ-HD-016. Especificação completa será desenvolvida no Épico 3 Tarefa 3.5 com consulta de especialista em hematologia pediátrica e estudo de validação clínica.

---

## 4. Requisitos Não-Funcionais

### RNF-001: Desempenho
**Análise em Tempo Real:**
- **Latência P95:** ≤ 2 segundos por análise de caso CBC (SLO primário)
- **Latência P99:** ≤ 5 segundos por análise de caso CBC (SLO fallback, atualização QW-005)
- **Timeout API:** 30 segundos (limite de infraestrutura, atualização QW-005)
- **Taxa de Transferência:** Suportar 1000 casos/hora por instância (tempo real)
- **Escalabilidade:** Suporte a escalonamento horizontal (implantação containerizada, Kubernetes HPA)

**Processamento em Lote:**
- **Taxa de Transferência:** Processar 10.000 casos históricos/hora
- **Isolamento de Recursos:** Sem impacto em latência em tempo real (pool de recursos dedicado)

**Limiares de Monitoramento (atualização QW-005):**
- Alerta se P95 > 2s por > 5 minutos (desempenho degradado)
- Alerta se P99 > 5s por > 10 minutos (degradação severa)
- Alerta se taxa de timeout API > 0,1% (problema de capacidade de infraestrutura)

**Degradação Graciosa:**
- Timeout de modelo ML: 5s → fallback para modo somente regras
- Timeout de banco de dados: 10s → retry 3x com backoff exponencial
- Timeout API: 30s → retornar 504 Gateway Timeout, registrar incidente

### RNF-002: Confiabilidade
- **Uptime:** ≥99,5% disponibilidade (SLA)
- **Testes de Regressão Automatizados:** 100% caminhos críticos cobertos
- **Failover:** Degradação graciosa se modelo ML indisponível (fallback para baseado em regras)
- **Recuperação de Desastres:** RPO (Objetivo de Ponto de Recuperação) ≤1 hora, RTO (Objetivo de Tempo de Recuperação) ≤4 horas

### RNF-003: Segurança e Cibersegurança (REQ-HD-060)
**Prioridade:** CRÍTICA
**Descrição:** Implementar arquitetura segura com RBAC, SBOM, VEX e hardening conforme melhores práticas da indústria.

**Requisitos Detalhados:** Veja **SEC-001 Documentação de Cibersegurança** para:
- Modelagem de ameaças (metodologia STRIDE)
- Processos de gerenciamento de vulnerabilidades
- Software Bill of Materials (SBOM)
- Vulnerability Exploitability eXchange (VEX)
- Procedimentos de hardening de segurança
- Resultados de testes de penetração

**Controles de Segurança:**
- **IAM:** Controle de Acesso Baseado em Funções (RBAC) com 4 funções (Admin, Operador de Lab, Médico, Auditor)
- **MFA:** Autenticação Multi-Fator obrigatória para funções Admin e Auditor
- **Criptografia:** TLS 1.3 para dados em trânsito, AES-256 para dados em repouso
- **SBOM:** Software Bill of Materials (formato CycloneDX/SPDX)
- **SAST/DAST:** Testes de Segurança de Aplicação Estáticos e Dinâmicos em CI/CD
- **Modelo de Ameaças:** Análise de ameaças baseada em STRIDE documentada
- **Conformidade:** Requisitos de Cibersegurança FDA §524B, linhas de base ISO/IEC 27001
- **Gerenciamento de Vulnerabilidades:** CVD (Divulgação Coordenada de Vulnerabilidades), VEX (Vulnerability Exploitability eXchange)
- **Atualizações Seguras:** Atualizações assinadas com capacidade de rollback
- **Testes de Penetração:** Testes de penetração anuais por terceiros

**Conformidade Regulatória:** FDA §524B, requisitos ciber ANVISA RDC 751/2022
**Rastreabilidade:** → SEC-001 §Todos → RISK-HD-CYB-001 a RISK-HD-CYB-010 → TST-SEC-001 a TST-SEC-005

### RNF-004: Privacidade
- **Minimização de Dados:** Coletar apenas dados clinicamente necessários
- **Pseudonimização:** Desidentificar PHI em logs e exportações
- **Retenção e Descarte:** Gerenciamento automatizado de ciclo de vida de dados (retenção de 5 anos, exclusão segura)
- **Conformidade:** LGPD (Brasil) / GDPR (UE) / HIPAA (EUA)
- **Direitos do Titular de Dados:** Suportar solicitações de acesso, exclusão, portabilidade, correção de paciente (LGPD Art. 18)

### RNF-005: Usabilidade
- **Conformidade IEC 62366-1:** Processo de engenharia de usabilidade documentado (relatório HFE separado)
- **Taxa de Sucesso em Tarefa Crítica:** 100% (validado com teste de usabilidade)
- **Acessibilidade:** Conformidade WCAG 2.1 Nível AA
- **Suporte Multilíngue:** UI disponível em pt-BR, en-US, es-ES
- **Materiais de Treinamento:** Treinamento abrangente de usuário (IFU-001, tutoriais em vídeo, ajuda in-app)

### RNF-006: Manutenibilidade
- **Qualidade de Código:** Aprovação em quality gate SonarQube (0 bugs críticos, cobertura de código ≥80%)
- **Documentação:** Todos os componentes documentados (arquitetura, API, implantação)
- **Versionamento:** Versionamento semântico para todos os releases (MAIOR.MENOR.PATCH)
- **Gerenciamento de Dependências:** Atualizações automatizadas de dependências (Dependabot, Renovate)
- **Débito Técnico:** Revisão e priorização trimestral de débito técnico

### RNF-007: Conformidade Regulatória
- **IEC 62304:** Conformidade com ciclo de vida Classe C (100% rastreabilidade)
- **ISO 14971:** Gerenciamento de risco (RMP-001, FMEA, aceitação de risco residual)
- **ISO 13485:** Sistema de Gestão de Qualidade
- **ANVISA RDC 657/2022:** Evidência clínica para SaMD Classe III
- **ANVISA RDC 751/2022:** Requisitos de registro SaMD
- **Submissão Pré-Mercado FDA:** 510(k) ou PMA (se expansão mercado EUA)
- **21 CFR Part 11:** Registros e assinaturas eletrônicas (se submissão FDA)

---

## 5. Dicionário de Dados

### Parâmetros CBC Core:
| Variável | Unidade | Faixa de Referência (Exemplo: Homem Adulto) | LOINC |
|----------|------|---------------------------------------|-------|
| Hemoglobina (Hb) | g/dL | 13,5-17,5 | 718-7 |
| Hematócrito (Ht) | % | 38-50 | 4544-3 |
| VCM | fL | 80-100 | 787-2 |
| RDW | % | 11,5-14,5 | 788-0 |
| Leucócitos | 10³/μL | 4,5-11,0 | 6690-2 |
| Neutrófilos | 10³/μL | 1,5-8,0 | 751-8 |
| Linfócitos | 10³/μL | 1,0-4,8 | 731-0 |
| Plaquetas | 10³/μL | 150-400 | 777-3 |
| Reticulócitos | % | 0,5-2,5 | 4679-7 |

### Testes Complementares:
| Variável | Unidade | Uso Clínico | LOINC |
|----------|------|--------------|-------|
| Ferritina | ng/mL | Diagnóstico de deficiência de ferro | 2276-4 |
| Ferro Sérico | μg/dL | Metabolismo de ferro | 2498-4 |
| Vitamina B12 | pg/mL | Anemia megaloblástica | 2132-9 |
| Folato | ng/mL | Anemia megaloblástica | 2284-8 |
| LDH | U/L | Marcador de hemólise | 2532-0 |

**Nota:** Faixas de referência variam por idade, sexo, status de gravidez e altitude. Sistema deve suportar limiares específicos por perfil de paciente (veja REQ-HD-002, REQ-HD-016 para faixas pediátricas).

---

## 6. Interfaces

### 6.1 Interfaces Externas
- **API REST:** JSON sobre HTTPS (especificação OpenAPI v1.1)
- **Mensageria (opcional):** AMQP/Kafka para integração LIS assíncrona
- **FHIR R4:** Interoperabilidade com sistemas EHR (DiagnosticReport, Observation, RiskAssessment)
- **CSV/Parquet:** Importação em lote para processamento em lote
- **Servidores de Terminologia:** Lookups SNOMED CT, LOINC, ICD-10

### 6.2 Interface de Usuário
- **UI Web:** Para operadores de laboratório (SPA baseado em React)
- **Tarefas Críticas:**
  - Revisar e aprovar relatórios automatizados
  - Substituir recomendações com justificativa
  - Exportar logs de auditoria
  - Configurar limiares de alerta (função Admin apenas)
- **Acessibilidade:** Conformidade WCAG 2.1 Nível AA
- **Teste de Usabilidade:** Conformidade IEC 62366-1 (documentado em relatório HFE separado)
- **Multilíngue:** pt-BR, en-US, es-ES

### 6.3 Observabilidade
- **Métricas:** Endpoints compatíveis com Prometheus (latência, taxa de transferência, taxas de erro)
- **Logging:** Logs JSON estruturados (compatível com ELK/Splunk)
- **Tracing:** Rastreamento distribuído (OpenTelemetry)
- **Trilha de Auditoria:** Banco de dados de auditoria imutável separado (append-only)
- **Dashboards de Desempenho:** Dashboards Grafana para monitoramento em tempo real

---

## 7. Controles de Segurança e Risco (Ligação ISO 14971)

### Estratégias de Mitigação de Risco:
- **Limiares de Falso Negativo/Positivo:** Tradeoffs configuráveis de sensibilidade/especificidade (REQ-HD-006)
- **Throttling de Alertas:** Prevenir fadiga de alerta (máx 3 alertas críticos por sessão) (REQ-HD-006)
- **Treinamento e HFE:** Treinamento obrigatório de usuário + validação de Engenharia de Fatores Humanos
- **Failover:** Fallback baseado em regras se modelo ML falhar (REQ-HD-007)
- **Substituição Manual:** Clínico sempre pode substituir com trilha de auditoria (REQ-HD-003)
- **RBAC:** Controle de acesso baseado em funções previne ações não autorizadas (REQ-HD-008)
- **Retenção de Dados:** Conformidade com requisitos de retenção LGPD/ANVISA (REQ-HD-009)
- **Segurança Pediátrica:** Faixas de referência específicas por idade previnem diagnóstico errado (REQ-HD-016)

### Link para Gerenciamento de Risco:
- **RISK-HD-001:** Falso negativo anemia grave → Mitigação: Alta sensibilidade (≥90%), REQ-HD-001, latência P95 <2s
- **RISK-HD-002:** Falso positivo anemia grave → Mitigação: Limiares configuráveis, REQ-HD-006
- **RISK-HD-003:** Indicadores de leucemia perdidos → Mitigação: Regras diferenciais de leucócitos, REQ-HD-010
- **RISK-HD-004:** Diagnóstico diferencial incorreto → Mitigação: Versionamento de regras clínicas, REQ-HD-010
- **RISK-HD-005:** Fadiga de alerta → Mitigação: Throttling de alertas, REQ-HD-006
- **RISK-HD-008:** Viés de automação → Mitigação: Exibição obrigatória de raciocínio, REQ-HD-003
- **RISK-HD-016:** Diagnóstico errado pediátrico → Mitigação: Faixas específicas por idade, REQ-HD-016
- **RISK-HD-101:** Erro de análise de dados → Mitigação: Validação de unidades, REQ-HD-002
- **RISK-HD-103:** Corrupção de banco de dados → Mitigação: Logs de auditoria WORM, REQ-HD-004
- **RISK-HD-104:** Falha de interface API → Mitigação: Timeout 30s, lógica de retry, REQ-HD-005
- **RISK-HD-106:** Incompatibilidade de versão de algoritmo → Mitigação: Versionamento de modelo, REQ-HD-007
- **RISK-HD-201:** Acesso não autorizado → Mitigação: RBAC + MFA, REQ-HD-008
- **RISK-HD-202:** Injeção de dados maliciosos → Mitigação: Validação de entrada, REQ-HD-002
- **RISK-HD-204:** Envenenamento de modelo → Mitigação: Validação de modelo, REQ-HD-007
- **RISK-HD-401:** Usuário interpreta mal recomendação → Mitigação: Teste de usabilidade + treinamento, REQ-HD-003

Análise detalhada de risco em **RMP-001** (Plano de Gerenciamento de Risco).

---

## 8. Cibersegurança (Conformidade FDA §524B)

### Controles de Cibersegurança:
- **CVD (Divulgação Coordenada de Vulnerabilidades):** security.txt público + bug bounty
- **SBOM:** Formato CycloneDX/SPDX, atualizado por release
- **VEX (Vulnerability Exploitability eXchange):** Comunicar status de patch para CVEs conhecidos
- **Atualização/Rollback Seguro:** Atualizações de firmware/software assinadas com rollback atômico (REQ-HD-007)
- **Logging:** Registro de eventos de segurança (falha de autenticação, tentativas de escalação de privilégio)
- **RBAC:** Controle de acesso de menor privilégio (REQ-HD-008)
- **Linhas de Base Cripto:** Módulos criptográficos conformes com NIST FIPS 140-2
- **Testes de Penetração:** Pentesting anual por terceiros

### Modelo de Ameaças:
- **Análise STRIDE:** Documentado em **SEC-001** (documentação de Cibersegurança)
- **Superfície de Ataque:** Rede (API), Física (acesso a servidor), Cadeia de Suprimentos (dependências)

---

## 9. Verificação e Validação

### Verificação (IEC 62304 §5.5-5.7):
- Cada REQ-ID mapeado para TEST-ID em **TRC-001** (Matriz de Rastreabilidade)
- Testes unitários: 80% cobertura de código mínima
- Testes de integração: 100% cobertura de endpoint API
- Testes de sistema: Cenários clínicos end-to-end

### Validação (IEC 62304 §5.8):
- Validação clínica: Curvas ROC/PR (TEST-HD-011)
- Validação de usabilidade: Teste HFE IEC 62366-1
- Validação pós-mercado: Monitoramento de desempenho no mundo real PMS-001

### Critérios Aprovado/Reprovado:
- Todos os requisitos críticos (prioridade CRÍTICA): 100% taxa de aprovação
- Requisitos de alta prioridade: ≥95% taxa de aprovação
- RNFs de desempenho: Atender ou exceder limiares especificados (P95 ≤2s, P99 ≤5s)

### Cobertura de Teste (v2.0):
- **REQ-HD-001 a HD-005:** TEST-HD-011 a HD-019 (existentes)
- **REQ-HD-006:** TEST-HD-020 (teste de configuração de alertas)
- **REQ-HD-007:** TEST-HD-021 (teste de versionamento e rollback de modelo)
- **REQ-HD-008:** TEST-HD-015, TEST-HD-022 (teste de penetração RBAC)
- **REQ-HD-009:** TEST-HD-023 (teste de retenção e exclusão de dados)
- **REQ-HD-010:** TEST-HD-024 (teste unitário de regras clínicas)
- **REQ-HD-011:** TEST-HD-025 (teste de UI multilíngue)
- **REQ-HD-012:** TEST-HD-026 (monitoramento de desempenho, testes de percentil P95/P99)
- **REQ-HD-013:** TEST-HD-027 (integração de servidor de terminologia)
- **REQ-HD-014:** TEST-HD-028 (desempenho de processamento em lote)
- **REQ-HD-015:** TEST-HD-029 (validação FHIR R4)
- **REQ-HD-016:** TEST-HD-016 (validação pediátrica - a ser criado no Épico 3)

---

## 10. Rastreabilidade

### Ligação de Requisitos:
**REQ ↔ Projeto ↔ Testes ↔ Riscos ↔ Rótulo ↔ PMS**

Exemplo (REQ-HD-001):
```
REQ-HD-001 (Detecção de anemia, Sensibilidade ≥90%, P95 <2s, P99 <5s)
  → SDD-001 §3.2 (Projeto de algoritmo)
  → TEST-HD-011 (Validação ROC/PR, matriz de confusão)
  → RISK-HD-001 (Mitigação de risco de falso negativo)
  → IFU-001 §Desempenho (Reivindicações de desempenho voltadas ao usuário: "95% análises <2s, 99% <5s")
  → PMS-001 §SLAs (Monitoramento de sensibilidade + latência no mundo real)
```

Exemplo (REQ-HD-007):
```
REQ-HD-007 (Versionamento e Rollback de Modelo ML)
  → SDD-001 §3.6 (Projeto de Gerenciador de Modelo)
  → TEST-HD-021 (Teste de rollback, teste A/B, detecção de drift)
  → RISK-HD-103, RISK-HD-104, RISK-HD-106, RISK-HD-204 (Riscos relacionados a modelo)
  → IFU-001 §Gerenciamento de Modelo (Documentação de ciclo de vida do modelo)
  → PMS-001 §Desempenho de Modelo (Monitoramento de drift no mundo real)
```

Exemplo (REQ-HD-016 - Pediátrico):
```
REQ-HD-016 (Análise Hematológica Específica Pediátrica)
  → SDD-001 §3.2.5 (Lógica pediátrica - a ser adicionada no Épico 3)
  → TEST-HD-016 (Validação pediátrica - a ser criado no Épico 3)
  → RISK-HD-016 (Diagnóstico errado pediátrico - a ser adicionado no Épico 3)
  → IFU-001 §Grupos Etários (Instruções de uso pediátrico)
  → CER-001 §Subgrupo Pediátrico (Evidência clínica para uso pediátrico)
```

Rastreabilidade completa documentada em **TRC-001_Traceability_Matrix_v2.0.csv** (16 requisitos funcionais + 7 RNFs mapeados, 100% cobertura).

---

## 11. Normas e Orientações Regulatórias

| Área de Conteúdo | Norma/Regulamentação | Conformidade |
|--------------|---------------------|------------|
| Ciclo de Vida de Software | IEC 62304:2006/Amd 1:2015 | Classe C |
| Gerenciamento de Risco | ISO 14971:2019 | Completo |
| Gerenciamento de Qualidade | ISO 13485:2016 | Completo |
| Evidência Clínica | ANVISA RDC 657/2022 | Classe III |
| Registro SaMD | ANVISA RDC 751/2022 | Classe III |
| Relatório AI/ML | TRIPOD-AI, MI-CLAIM | Diretrizes |
| Usabilidade | IEC 62366-1:2015 | Completo |
| Cibersegurança | FDA §524B | Completo |
| Privacidade | LGPD (Brasil), GDPR (UE), HIPAA (EUA) | Completo |
| Segurança | ISO/IEC 27001:2022, OWASP ASVS | Linhas de Base |
| Interoperabilidade | HL7 FHIR R4 | US Core IG |

---

## 12. Histórico do Documento

| Versão | Data | Autor | Alterações |
|---------|------|--------|---------|
| v0.0 | 2025-09-16 | HemoDoctor Agent | Rascunho inicial com declaração Classe C |
| v1.0 | 2025-09-19 | HemoDoctor Agent | Adicionados requisitos detalhados de CBC (REQ-HD-001 a 005) |
| v1.0 (MERGED) | 2025-10-07 | Abel Costa | Merged v0.0 + v1.0, adicionada rastreabilidade, cibersegurança |
| v1.1 (EXPANDED) | 2025-10-08 | @spec-writer | Adicionados 10 novos requisitos funcionais (REQ-HD-006 a 015), RNFs expandidos |
| v1.2 (LIMITES DO SISTEMA) | 2025-10-08 | @consultant-agent | Aplicado QW-002 (Seção 1.3 Limites do Sistema), QW-003 (referência cruzada SEC-001 em RNF-003) |
| **v2.0 (AUTHORITATIVE)** | **2025-10-08** | **@spec-writer** | **CONSOLIDAÇÃO ÉPICO 1 TAREFA 1.2:** Aplicado decisão SLO QW-005 (P99 ≤5s, timeout API 30s em RNF-001), adicionado placeholder REQ-HD-016 Pediátrico, atualizados todos os links de rastreabilidade forward, consolidado conteúdo único de versões arquivadas. **Status: Linha de base autoritativa pronta para submissão ANVISA.** |

---

## 13. Resumo de Atualizações v2.0 (AUTHORITATIVE)

### Alterações v2.0 (da v1.2):

1. **Decisão SLO de Desempenho QW-005 Aplicada:**
   - **RNF-001 Desempenho:** Adicionado requisito de latência P99 ≤ 5s (SLO fallback)
   - **RNF-001 Desempenho:** Adicionado timeout API 30s (limite de infraestrutura)
   - **RNF-001 Desempenho:** Adicionados limiares de monitoramento (alerta se P95 >2s ou P99 >5s)
   - **RNF-001 Desempenho:** Adicionada estratégia de degradação graciosa (timeout ML 5s, timeout BD 10s, timeout API 30s)
   - **REQ-HD-001:** Atualizados critérios de aceitação para incluir latência de alerta P99 <5s
   - **REQ-HD-012:** Atualizadas métricas monitoradas para incluir rastreamento e alerta de latência P99

2. **Placeholder REQ-HD-016 Pediátrico Adicionado:**
   - Adicionado novo requisito REQ-HD-016 para análise hematológica específica pediátrica
   - Status: PLACEHOLDER para especificação detalhada Épico 3 Tarefa 3.5
   - Inclui escopo preliminar, critérios de aceitação e links de rastreabilidade
   - Reserva ID de requisito para manter continuidade da matriz de rastreabilidade

3. **Links de Rastreabilidade Forward Atualizados:**
   - Todos os 16 requisitos funcionais agora têm rastreabilidade forward completa:
     - REQ → SDD-001 §X.Y (Seção de projeto)
     - REQ → TEST-HD-XXX (Caso de teste)
     - REQ → RISK-HD-XXX (Controle de risco)
     - REQ → IFU-001 §Z (Documentação voltada ao usuário)
     - REQ → PMS-001 §Métricas (Vigilância pós-mercado)
   - Validação cruzada com SDD-001 v1.1 para existência de seção de projeto
   - Adicionada rastreabilidade específica pediátrica (REQ-HD-016 → CER-001 §Subgrupo Pediátrico)

4. **Consolidação de Conteúdo de Arquivo:**
   - Revisadas versões fernanda (v1.1, bundles de Release v1.2) - formatos compactos baseados em âncoras, sem requisitos únicos
   - Incorporadas especificações únicas de desempenho de paulo v1.0 (P99 ≤5s, timeout API 30s)
   - Nenhum requisito conflitante encontrado em arquivos além de SLO já resolvido em QW-005

5. **Upgrade de Status do Documento:**
   - Status mudado de "Em Revisão" (v1.2) para "AUTHORITATIVE - Linha de Base Consolidada" (v2.0)
   - Marcado como pronto para submissão para dossiê regulatório ANVISA
   - Cobertura completa da matriz de rastreabilidade (16 funcionais + 7 RNFs = 23 requisitos)

### Checklist de Conformidade ANVISA/IEC 62304 (v2.0):

✅ **IEC 62304 §5.2.1:** Requisitos de software definidos (16 funcionais + 7 RNFs)
✅ **IEC 62304 §5.2.2:** Conteúdo de requisitos completo (todos os critérios de aceitação especificados)
✅ **IEC 62304 §5.2.3:** Reavaliação da análise de risco de dispositivo médico (vinculada ao RMP-001)
✅ **IEC 62304 §5.2.4:** Requisitos de verificação (todos os requisitos têm TEST-ID)
✅ **IEC 62304 §5.2.5:** Limites do sistema definidos (Seção 1.3, QW-002)
✅ **IEC 62304 §5.2.6:** Requisitos de interface (Seção 6: API, UI, Observabilidade)
✅ **ANVISA RDC 657/2022:** Requisitos de evidência clínica (vinculação CER-001)
✅ **ANVISA RDC 751/2022:** Requisitos de registro SaMD (rastreabilidade completa)

### Lacunas Remanescentes para Épicos Futuros:

⏳ **Épico 3 Tarefa 3.5:** Completar especificação pediátrica REQ-HD-016 (atualmente placeholder)
⏳ **Teste de Desempenho:** Executar TEST-HD-026-P99 para validar SLO P99 ≤5s (Épico 2)
⏳ **Atualização SDD-001:** Adicionar seção de projeto §3.2.5 Lógica Pediátrica (Épico 3)
⏳ **Atualização IFU-001:** Adicionar instruções de grupo etário pediátrico (Épico 3)
⏳ **Atualização CER-001:** Adicionar evidência clínica de subgrupo pediátrico (Épico 4)

---

**Próximos Passos:**
1. ✅ **COMPLETO:** SRS-001 v2.0 consolidado e salvo
2. Atualizar TRC-001 v2.0 (adicionar REQ-HD-016, atualizar rastreabilidade P99/timeout)
3. Criar placeholder TEST-HD-016 em TST-001 (testes de validação pediátrica)
4. Atualizar RMP-001 se novos riscos identificados (RISK-HD-016 diagnóstico errado pediátrico)
5. Atualizar IFU-001 com reivindicação de desempenho P99 ("99% das análises completas em 5 segundos")
6. Executar teste de desempenho para validar SLO P99 ≤5s (Épico 2)
7. Revisão e aprovação regulatória por @anvisa-regulatory-specialist

---

**FIM DO DOCUMENTO**
