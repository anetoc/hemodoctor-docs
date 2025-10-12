---
document_id: "PROC-001"
title: "Procedimento de Relato de Incidentes e Tecnovigilância"
version: "1.0"
status: "OFICIAL"
date: "2025-10-12"
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
    date: "2025-10-12"
    changes: "Versão inicial do procedimento de tecnovigilância"
    author: "ANVISA Regulatory Specialist"
---

# PROC-001: Procedimento de Relato de Incidentes e Tecnovigilância

## 1. OBJETIVO

Este procedimento estabelece diretrizes para:

- Estabelecer procedimento sistemático e padronizado para relato de incidentes com HemoDoctor
- Garantir conformidade com ANVISA RDC 67/2009 (Tecnovigilância)
- Assegurar resposta rápida e eficaz aos incidentes relatados
- Proteger a segurança dos pacientes e usuários
- Cumprir prazos regulatórios de notificação à ANVISA

## 2. ESCOPO

### 2.1. Aplicabilidade

Este procedimento aplica-se a:

- **Todos os usuários do HemoDoctor**: Médicos, enfermeiros, técnicos de laboratório, residentes
- **Pacientes**: Que direta ou indiretamente sejam afetados pelo dispositivo
- **Equipe HemoDoctor**: Desenvolvedores, equipe clínica, suporte técnico, gestão de qualidade
- **Parceiros**: Distribuidores, revendedores, implementadores

### 2.2. Tipos de Incidentes Cobertos

Este procedimento cobre:

1. **Incidentes com Dano ao Paciente**:
   - Morte relacionada ao uso do dispositivo
   - Ameaça à vida do paciente
   - Lesão grave ou incapacidade permanente
   - Necessidade de intervenção médica urgente para prevenir dano
   - Hospitalização prolongada

2. **Incidentes sem Dano ao Paciente (Queixas Técnicas)**:
   - Mau funcionamento do software (crash, freeze, erro de processamento)
   - Sugestão diagnóstica incorreta sem consequências ao paciente
   - Falha de integração com sistemas hospitalares
   - Problemas de performance (lentidão, timeout)
   - Erros de interface do usuário

3. **Near Miss (Quase-Acidentes)**:
   - Incidentes que poderiam ter causado dano mas foram evitados
   - Situações de alto risco identificadas antes de causarem consequências

### 2.3. Exclusões

Não são cobertos por este procedimento:

- Dúvidas sobre uso normal do sistema (direcionar para treinamento)
- Solicitações de melhoria de funcionalidade (direcionar para desenvolvimento de produto)
- Problemas de infraestrutura do cliente não relacionados ao HemoDoctor

## 3. DEFINIÇÕES

Para efeitos deste procedimento, aplicam-se as seguintes definições:

| Termo | Definição |
|-------|-----------|
| **Incidente** | Qualquer evento adverso, falha ou deterioração das características ou desempenho de um dispositivo médico, bem como qualquer inadequação na rotulagem ou nas instruções de uso que possa levar ou tenha levado à morte ou deterioração da saúde de pacientes, usuários ou outras pessoas (RDC 67/2009) |
| **Evento Adverso Grave** | Evento que resulte em morte, ameaça à vida, hospitalização ou prolongamento de hospitalização existente, incapacidade persistente ou significativa, anomalia congênita ou necessidade de intervenção médica para prevenir dano permanente |
| **Queixa Técnica** | Comunicação escrita, eletrônica ou oral que alegue deficiências relacionadas à identidade, qualidade, durabilidade, confiabilidade, segurança ou desempenho de um dispositivo médico após sua liberação para distribuição, mas que não tenha causado dano ao paciente |
| **Near Miss (Quase-Acidente)** | Situação ou incidente que poderia ter resultado em acidente, lesão ou dano mas foi evitado por circunstância, ação preventiva ou intervenção oportuna |
| **Tecnovigilância** | Sistema de vigilância de eventos adversos e queixas técnicas de produtos para saúde na fase de pós-comercialização, com o objetivo de recomendar a adoção de medidas que garantam a proteção e a promoção da saúde da população (RDC 67/2009) |
| **NOTIVISA** | Sistema informatizado da ANVISA para recepção de notificações de eventos adversos e queixas técnicas relacionadas ao uso de produtos sob vigilância sanitária |
| **Responsável Técnico (RT)** | Profissional legalmente habilitado e responsável perante a ANVISA pelos aspectos técnicos do dispositivo médico |
| **Recall** | Ação de retirada de um produto do mercado ou correção em campo, conduzida pelo detentor do registro após a comercialização |
| **CAPA** | Corrective and Preventive Actions - Ações Corretivas e Preventivas conforme ISO 13485 |

## 4. RESPONSABILIDADES

### 4.1. Usuário Final (Médico/Enfermeiro/Técnico)

- **Relatar imediatamente** qualquer incidente ou suspeita de mau funcionamento do HemoDoctor
- **Preservar evidências** (prints de tela, anotações, dados de entrada)
- **Documentar contexto clínico** (informações do paciente, urgência da situação, decisões tomadas)
- **Aguardar orientação** antes de continuar usando o sistema em caso de incidente grave
- **Disponibilidade** para entrevistas de investigação

### 4.2. Equipe Clínica (HemoDoctor)

- **Documentar** incidentes recebidos de forma completa e estruturada
- **Realizar avaliação preliminar** de severidade do incidente
- **Conduzir investigação inicial** (coletar evidências, entrevistar usuários)
- **Prover suporte imediato** ao usuário final
- **Comunicar** ao Responsável Técnico incidentes GRAVES em até 2 horas

### 4.3. Responsável Técnico (RT)

- **Avaliar severidade** do incidente conforme critérios da RDC 67/2009 (seção 5.2)
- **Decidir** sobre necessidade de ação imediata (suspensão de uso, comunicação a usuários)
- **Aprovar** notificações à ANVISA
- **Garantir** conformidade regulatória do processo de vigilância
- **Assinar** documentos de tecnovigilância

### 4.4. Gerente de Qualidade

- **Coordenar** o processo de relato e investigação de incidentes
- **Notificar ANVISA** via portal NOTIVISA dentro dos prazos regulatórios
- **Gerenciar** banco de dados de incidentes
- **Garantir** cumprimento de prazos de investigação e follow-up
- **Gerar relatórios periódicos** de incidentes para a direção
- **Manter registros** por mínimo de 5 anos (ISO 13485)

### 4.5. CEO / Direção

- **Aprovar** ações corretivas críticas (recall, suspensão de comercialização, mudanças de design)
- **Alocar recursos** para investigação e correção de incidentes
- **Avaliar impacto estratégico** de incidentes graves
- **Comunicar com stakeholders** externos (investidores, parceiros, mídia) se necessário
- **Revisar** relatórios mensais de tecnovigilância

## 5. FLUXO DE RELATO

### 5.1. Identificação do Incidente

#### 5.1.1. Quem Pode Relatar?

Qualquer pessoa pode relatar um incidente:
- Usuário final (médico, enfermeiro, técnico)
- Paciente ou familiar
- Equipe técnica ou de suporte
- Auditores internos ou externos
- Qualquer pessoa que tenha conhecimento de um incidente

#### 5.1.2. Canais de Relato (24/7 para Incidentes Graves)

| Canal | Disponibilidade | Uso Recomendado |
|-------|-----------------|-----------------|
| **Email**: incidentes@hemodoctor.com | 24/7 | Incidentes não urgentes, documentação detalhada |
| **Telefone**: +55 11 3456-7890 | 24/7 (plantão) | Incidentes GRAVES, situação urgente |
| **Formulário Web**: https://hemodoctor.com/relatar-incidente | 24/7 | Relato estruturado com campos obrigatórios |
| **Presencial**: Setor de Qualidade HemoDoctor | Horário comercial | Incidentes complexos, entrega de evidências físicas |

#### 5.1.3. Informações Mínimas para Relato Inicial

Ver **ANEXO C - Checklist de Informações Mínimas**:
- Data e hora do incidente
- Local (hospital, unidade)
- Versão do HemoDoctor utilizada
- Breve descrição do ocorrido
- Houve dano ao paciente? (sim/não)
- Contato do relator

### 5.2. Classificação de Severidade (CRÍTICO - RDC 67/2009)

**ATENÇÃO**: Esta classificação determina os prazos de notificação à ANVISA. A classificação deve ser realizada pelo Responsável Técnico (RT) em até 24 horas após o relato inicial.

#### 5.2.1. Incidentes GRAVES (Notificação ANVISA em 10 dias úteis)

Incidentes que se enquadram em QUALQUER um dos critérios abaixo:

**Critérios de Evento Adverso Grave (RDC 67/2009, Art. 2º):**

1. **Morte relacionada ao dispositivo**:
   - Exemplo: Paciente com leucemia aguda teve sugestão incorreta do HemoDoctor de "anemia ferropriva", atrasando tratamento oncológico urgente, resultando em óbito por progressão da doença.

2. **Ameaça à vida**:
   - Exemplo: Sistema não identificou leucocitose crítica (GB > 100.000/µL) em paciente com leucemia mieloide aguda, colocando paciente em risco iminente de leucostase cerebral.

3. **Lesão grave ou incapacidade permanente**:
   - Exemplo: Falha do sistema em detectar anemia grave (Hb < 5 g/dL) levou a atraso no tratamento, resultando em sequelas neurológicas permanentes por hipóxia cerebral.

4. **Necessidade de intervenção médica urgente para prevenir dano**:
   - Exemplo: Sistema sugeriu "anemia de doença crônica" quando paciente tinha hemorragia digestiva alta grave (Hb caindo rapidamente), necessitando intervenção cirúrgica de emergência.

5. **Hospitalização ou prolongamento de hospitalização**:
   - Exemplo: Diagnóstico incorreto do sistema atrasou tratamento adequado, prolongando internação hospitalar do paciente.

6. **Necessidade de intervenção médica para prevenir lesão ou dano permanente**:
   - Exemplo: Sistema não alertou sobre trombocitopenia grave (plaquetas < 10.000/µL), mas médico identificou manualmente e iniciou transfusão, prevenindo hemorragia cerebral.

#### 5.2.2. Incidentes NÃO GRAVES (Notificação ANVISA em 60 dias)

Incidentes que NÃO se enquadram nos critérios acima:

1. **Mau funcionamento sem dano ao paciente**:
   - Exemplo: Sistema travou (crash) ao processar CBC, mas não havia urgência clínica e médico aguardou reinicialização sem impacto ao paciente.

2. **Queixa técnica**:
   - Exemplo: Interface do usuário exibiu mensagem de erro confusa, mas funcionalidade continuou operando normalmente.

3. **Sugestão incorreta sem seguimento pelo médico**:
   - Exemplo: HemoDoctor sugeriu "anemia ferropriva" mas médico, por análise crítica e experiência clínica, solicitou exames adicionais e identificou o diagnóstico correto (talassemia), sem prejuízo ao paciente.

4. **Near miss sem dano real**:
   - Exemplo: Sistema não detectou paciente pediátrico e quase sugeriu diagnóstico inadequado, mas validação manual pelo médico identificou a idade e o erro foi evitado.

#### 5.2.3. Casos Limítrofes (Decisão do RT)

Em situações de dúvida sobre a classificação:
- **Regra de ouro**: Em caso de dúvida, **classifique como GRAVE** (princípio da precaução)
- **Consulte o RT** imediatamente
- **Documente a justificativa** da classificação no formulário FORM-001

### 5.3. Registro Imediato (0-24h)

#### 5.3.1. Preenchimento do FORM-001

- **Prazo**: Máximo 24 horas após identificação do incidente
- **Responsável**: Primeiro profissional que tomar conhecimento do incidente (pode ser usuário final, equipe de suporte, ou equipe clínica HemoDoctor)
- **Formulário**: FORM-001_Relato_Incidente (ver seção 11)
- **Campos obrigatórios**:
  - Descrição detalhada do incidente
  - Informações do paciente (iniciais, idade, sexo - sem dados identificáveis completos)
  - Dados de CBC inseridos no sistema
  - Output/resultado do HemoDoctor
  - Houve dano ao paciente?
  - Classificação preliminar de severidade

#### 5.3.2. Geração de Número de Protocolo

- **Formato**: INC-YYYY-XXX
  - INC = Incidente
  - YYYY = Ano (4 dígitos)
  - XXX = Número sequencial (começando em 001)
- **Exemplo**: INC-2025-001, INC-2025-002, etc.
- **Responsável**: Sistema automatizado ou Gerente de Qualidade (manual)

#### 5.3.3. Timestamp de Recebimento

Registrar 3 timestamps:
1. **Data/hora do incidente**: Quando o incidente ocorreu
2. **Data/hora do relato**: Quando foi relatado pela primeira vez
3. **Data/hora do registro**: Quando foi oficialmente registrado no sistema

#### 5.3.4. Preservação de Evidências

**Evidências técnicas a coletar imediatamente**:
- **Logs do sistema**: Arquivo completo do período relevante (solicitar ao DevOps)
- **Screenshots**: Todas as telas relevantes do sistema
- **Dados de entrada**: CBC completo inserido (arquivo CSV ou print)
- **Output do sistema**: Sugestão diagnóstica exibida, confidence score, alertas
- **Informações do ambiente**: Versão do HemoDoctor, browser, sistema operacional, hospital/unidade
- **Histórico de sessão**: Ações do usuário antes e depois do incidente

**Evidências clínicas a coletar**:
- Prontuário médico do paciente (cópia relevante, com consentimento)
- Resultado de exames complementares (se realizados)
- Diagnóstico final confirmado
- Tratamento instituído
- Evolução do paciente

**IMPORTANTE**: Desidentificar todas as informações do paciente (remover nome completo, CPF, endereço) conforme LGPD. Manter apenas iniciais, idade, sexo e ID interno anonimizado.

### 5.4. Ação Imediata (0-24h para Incidentes GRAVES)

#### 5.4.1. Avaliação de Urgência (Responsável Técnico)

Ao receber notificação de incidente GRAVE, o RT deve avaliar:

**Perguntas críticas:**
1. O problema pode afetar outros pacientes/usuários AGORA?
2. Existe risco iminente à segurança?
3. O sistema deve ser suspenso imediatamente?
4. Outros usuários devem ser alertados?

#### 5.4.2. Ações Imediatas Possíveis

| Situação | Ação Imediata | Responsável | Prazo |
|----------|---------------|-------------|-------|
| Bug crítico confirmado (crash, data loss) | Suspender módulo afetado | RT + DevOps | Imediato |
| Sugestão diagnóstica sistematicamente incorreta | Emitir alerta de segurança aos usuários | RT + Gerente de Qualidade | 2-4 horas |
| Incidente isolado (provavelmente uso inadequado) | Contatar usuário para esclarecimentos | Equipe Clínica | 24 horas |
| Risco regulatório (múltiplos incidentes similares) | Considerar recall ou field safety notice | CEO + RT | 24-48 horas |

#### 5.4.3. Comunicação de Ação Imediata

**Stakeholders a notificar (depende da severidade):**
- CEO: Sempre para incidentes GRAVES
- Responsável Técnico: Sempre
- Equipe de Desenvolvimento: Se bug técnico
- Usuários finais: Se risco de segurança sistêmico
- ANVISA: Se recall ou field safety corrective action (FSCA)

**Usar template de email** (ver **ANEXO B - Template de Email de Notificação Interna**).

#### 5.4.4. Investigação Preliminar

Iniciar imediatamente (mesmo antes da investigação formal completa):
- Coletar evidências adicionais
- Entrevistar usuário envolvido (se disponível)
- Revisar logs e dados técnicos
- Avaliar se é problema novo ou recorrente
- Estimar abrangência (quantos usuários podem ser afetados?)

## 6. PRAZOS REGULATÓRIOS ANVISA

A tabela abaixo resume os prazos obrigatórios da ANVISA RDC 67/2009 para notificação, investigação e relatório final:

| Severidade | Prazo Notificação ANVISA (Portal NOTIVISA) | Prazo Investigação Completa | Prazo Relatório Final à ANVISA |
|------------|--------------------------------------------|-----------------------------|--------------------------------|
| **GRAVE** | **10 dias úteis** a partir do conhecimento do evento | 30 dias | 60 dias (com causa raiz e ações corretivas) |
| **NÃO GRAVE** | 60 dias | 90 dias | 120 dias |

### 6.1. Cálculo de Prazos

**Importante**:
- **Dias úteis**: Considerar calendário de dias úteis brasileiros (excluir sábados, domingos e feriados nacionais)
- **Marco inicial**: Data em que a HemoDoctor tomou conhecimento do incidente (não a data do incidente em si)
- **Prazo fatal**: Se o último dia cair em final de semana ou feriado, o prazo se estende ao próximo dia útil

**Exemplo de cálculo:**
- Incidente GRAVE ocorreu em 15/março (sexta-feira)
- HemoDoctor tomou conhecimento em 16/março (sábado, mas relato via email)
- Marco inicial: 18/março (segunda-feira - primeiro dia útil)
- Notificação ANVISA deve ser feita até: 01/abril (10 dias úteis após 18/março, considerando feriados)

### 6.2. Documentação Obrigatória para ANVISA

A notificação ao portal NOTIVISA deve incluir:

**Notificação Inicial (Prazo: 10 ou 60 dias):**
- FORM-004_Notificacao_ANVISA preenchido
- Descrição do incidente
- Classificação de severidade (GRAVE/NÃO GRAVE)
- Impacto no paciente
- Ações imediatas tomadas
- Dados do produto (HemoDoctor, registro ANVISA, versão)
- Dados da empresa (HemoDoctor, CNPJ, RT)

**Relatório de Investigação (Prazo: 30 ou 90 dias):**
- Análise de causa raiz (ver PROC-002)
- Evidências coletadas
- Timeline detalhado do incidente
- Avaliação de impacto (quantos usuários/pacientes afetados)

**Relatório Final (Prazo: 60 ou 120 dias):**
- Causa raiz confirmada
- Ações corretivas implementadas
- Ações preventivas para evitar recorrência
- Eficácia das ações (se já verificada)
- Atualização de documentação (IFU, rotulagem, treinamento)

## 7. PROCEDIMENTO DE NOTIFICAÇÃO ANVISA (3 ETAPAS)

### 7.1. Preparação

#### 7.1.1. Documentos Necessários

- [ ] **FORM-004_Notificacao_ANVISA** preenchido completamente
- [ ] **FORM-001_Relato_Incidente** (base)
- [ ] **FORM-002_Investigacao_Evento** (se investigação preliminar já iniciada)
- [ ] **Evidências técnicas**: Logs (anonimizados), prints de tela, dados de CBC
- [ ] **Evidências clínicas**: Relatório médico (desidentificado conforme LGPD)
- [ ] **Relatório técnico**: Sumário executivo do incidente (2-3 páginas)
- [ ] **Ações imediatas**: Descrição de ações já tomadas ou planejadas

#### 7.1.2. Revisão e Aprovação Interna

**Fluxo de Aprovação:**
1. **Gerente de Qualidade**: Redige notificação e anexos
2. **Responsável Técnico**: Revisa aspectos técnicos e regulatórios
3. **CEO**: Aprova (para incidentes GRAVES ou com impacto estratégico)
4. **Advogado** (opcional): Revisa aspectos legais (se exposição significativa)

**Critérios de aprovação:**
- Informações completas e precisas?
- Tom profissional e transparente?
- Evidências suficientes anexadas?
- Ações propostas são adequadas e realistas?

#### 7.1.3. Conversão para PDF

- Todos os documentos devem ser convertidos para **PDF/A** (formato arquivo)
- Nome dos arquivos: `NOTIVISA_INC-YYYY-XXX_[Tipo_Documento]_vX.pdf`
- Exemplo: `NOTIVISA_INC-2025-001_Formulario_v1.pdf`

### 7.2. Submissão ao Portal NOTIVISA

#### 7.2.1. Acesso ao Portal

- **URL**: https://www.gov.br/anvisa/pt-br/assuntos/fiscalizacao/notivisa
- **Cadastro prévio necessário**:
  - Empresa: HemoDoctor (CNPJ, endereço, contatos)
  - Responsável Técnico: Nome, CPF, registro profissional, email, telefone
  - Produto: HemoDoctor (dados de registro ANVISA, classe de risco)

**Nota**: O cadastro é realizado UMA VEZ e reutilizado para notificações futuras.

#### 7.2.2. Preenchimento Online

O portal NOTIVISA tem formulário online estruturado. Siga os passos:

**Seção 1: Identificação da Empresa**
- CNPJ: [preencher automaticamente se cadastrado]
- Nome fantasia: HemoDoctor
- Responsável Técnico: [selecionar da lista]

**Seção 2: Identificação do Produto**
- Nome comercial: HemoDoctor
- Número de registro ANVISA: [inserir número quando disponível]
- Classe de risco: II
- Modelo/versão: [Ex: v1.5.2]

**Seção 3: Descrição do Evento**
- Tipo de evento: ☑ Evento Adverso / ☐ Queixa Técnica
- Classificação: ☑ GRAVE / ☐ NÃO GRAVE
- Data do evento: DD/MM/AAAA
- Data do conhecimento: DD/MM/AAAA
- Local: Hospital/Unidade (cidade, estado)
- Descrição (campo texto livre, máximo 2000 caracteres)

**Seção 4: Paciente Envolvido** (se aplicável)
- Iniciais: [Ex: J.S.M.]
- Idade: [Ex: 45 anos]
- Sexo: ☐ M ☑ F ☐ Não informado
- Desfecho: ☐ Recuperação completa ☑ Sequela permanente ☐ Óbito ☐ Em acompanhamento

**Seção 5: Ações Tomadas**
- Descrição das ações imediatas
- Plano de investigação
- Previsão de relatório final

**Seção 6: Anexos**
- Upload de PDFs (limite: 10MB por arquivo, máximo 10 arquivos)

**Seção 7: Declaração de Veracidade**
- Responsável pela notificação: [Nome do RT]
- CPF: [CPF do RT]
- Data: DD/MM/AAAA
- ☑ Declaro que as informações prestadas são verdadeiras

#### 7.2.3. Confirmação e Protocolo

Após submissão:
- **Número de protocolo NOTIVISA** será gerado automaticamente
- **Formato**: NOTIVISA-XXXXX-YYYY (5 dígitos + ano)
- **Comprovante em PDF**: Fazer download e arquivar
- **Email de confirmação**: ANVISA envia confirmação de recebimento em até 48h

**Registrar no sistema interno:**
- Vincular número NOTIVISA ao número de incidente interno (INC-YYYY-XXX)
- Atualizar status: "Notificado ANVISA em DD/MM/AAAA - Protocolo NOTIVISA-XXXXX"

### 7.3. Follow-up com ANVISA

#### 7.3.1. Solicitações da ANVISA

A ANVISA pode solicitar:
- Informações adicionais
- Evidências complementares
- Esclarecimentos sobre a investigação
- Atualização de status
- Relatório de eficácia de ações corretivas

**Prazo para resposta**: **15 dias corridos** a partir da solicitação da ANVISA

#### 7.3.2. Informar Ações Corretivas

**Quando informar:**
- Ação corretiva foi implementada
- Causa raiz foi confirmada
- Eficácia da ação foi verificada
- Atualização de IFU ou rotulagem foi realizada
- Recall ou field safety notice foi emitido

**Como informar:**
- Acessar portal NOTIVISA
- Localizar notificação original (número de protocolo)
- Clicar em "Adicionar Informações" ou "Atualizar Status"
- Anexar documento "Relatório de Ações Corretivas" (PDF)
- Submeter atualização

#### 7.3.3. Atualização de Status da Investigação

**Cronograma de atualizações:**

| Marco | Prazo (dias) | Informação a Prestar | Responsável |
|-------|--------------|----------------------|-------------|
| Notificação Inicial | 10 (GRAVE) ou 60 (NÃO GRAVE) | Descrição do evento, ações imediatas | Gerente de Qualidade |
| Relatório de Investigação | 30 (GRAVE) ou 90 (NÃO GRAVE) | Causa raiz preliminar, plano de ação | Gerente de Qualidade + RT |
| Relatório Final | 60 (GRAVE) ou 120 (NÃO GRAVE) | Causa raiz confirmada, ações implementadas, eficácia | RT |
| Follow-up de Eficácia | 180 (6 meses) | Validação de eficácia de longo prazo, recorrência | Gerente de Qualidade |

#### 7.3.4. Encerramento da Notificação

**Critérios para solicitar encerramento:**
- [ ] Investigação 100% completa
- [ ] Causa raiz confirmada
- [ ] Ações corretivas implementadas e verificadas como eficazes
- [ ] Não houve recorrência em período de monitoramento (mínimo 90 dias)
- [ ] Documentação atualizada (IFU, RMP, SRS)
- [ ] ANVISA está satisfeita com as informações prestadas

**Procedimento:**
- Enviar email formal ao canal de comunicação da ANVISA
- Anexar "Relatório de Encerramento" (PDF)
- Solicitar confirmação de encerramento
- Arquivar resposta da ANVISA

## 8. COMUNICAÇÃO INTERNA

### 8.1. Notificação Imediata (0-2h para Incidentes GRAVES)

**Destinatários obrigatórios:**
- **Email**: qualidade@hemodoctor.com
- **Email**: abel.costa@hemodoctor.com
- **Email**: ceo@hemodoctor.com (para incidentes GRAVES)
- **Telefone/WhatsApp**: RT (para incidentes GRAVES)

**Conteúdo do email inicial** (usar **ANEXO B - Template de Email**):
- Assunto: `[URGENTE] Incidente GRAVE Relatado - INC-YYYY-XXX`
- Número de protocolo: INC-YYYY-XXX
- Classificação: GRAVE / NÃO GRAVE
- Breve descrição (3-5 linhas)
- Houve dano ao paciente? Sim/Não
- Ação imediata necessária? Sim/Não
- Responsável pelo relato
- Data/hora do incidente

### 8.2. Reunião de Análise (48h para Incidentes GRAVES)

**Objetivo**: Análise preliminar, definir plano de investigação e ações imediatas.

**Participantes obrigatórios:**
- Gerente de Qualidade (organiza a reunião)
- Responsável Técnico
- Representante da equipe de desenvolvimento (se bug técnico)
- Médico/especialista clínico (se impacto clínico)
- CEO (se incidente GRAVE ou crítico)

**Pauta:**
1. Apresentação do incidente (10 min)
2. Evidências coletadas (15 min)
3. Análise preliminar de causa (20 min)
4. Avaliação de impacto e abrangência (10 min)
5. Decisão sobre ações imediatas (10 min)
6. Definição de responsáveis e prazos (5 min)
7. Comunicação externa necessária? (5 min)

**Ata de reunião**: Documentar decisões e responsabilidades.

### 8.3. Atualização Semanal (Quadro Kanban)

**Sistema**: Quadro Kanban de Qualidade (físico ou digital - ex: Trello, Jira)

**Colunas do Kanban:**
1. Relatado
2. Em Investigação
3. Aguardando CAPA
4. Em Implementação de CAPA
5. Aguardando Verificação de Eficácia
6. Fechado

**Card de incidente deve conter:**
- Número: INC-YYYY-XXX
- Título: Breve descrição (máx 60 caracteres)
- Severidade: Cor (Vermelho=GRAVE, Amarelo=NÃO GRAVE)
- Responsável: Foto/nome
- Prazo: Data limite
- Status: Coluna atual

**Atualização**: Mover cards conforme progresso da investigação, semanalmente (toda segunda-feira 14h).

### 8.4. Relatório Mensal para Direção

**Responsável**: Gerente de Qualidade

**Conteúdo**:

**1. Resumo Executivo (1 página)**
- Total de incidentes no mês: GRAVES (X) + NÃO GRAVES (Y)
- Incidentes fechados vs abertos
- Prazos atendidos vs atrasados
- Ações críticas em andamento

**2. Detalhamento (2-3 páginas)**
- Lista de incidentes GRAVES (descrição, status, ações)
- Análise de tendências (tipos de incidente mais frequentes)
- Gráficos (evolução mensal, distribuição por tipo, por severidade)

**3. Indicadores de Desempenho (KPIs)**
- Tempo médio de investigação
- Taxa de cumprimento de prazos ANVISA (meta: 100%)
- Taxa de recorrência de incidentes similares (meta: <5%)
- Backlog de incidentes abertos

**4. Recomendações**
- Ações preventivas sistêmicas
- Investimentos necessários (treinamento, tecnologia, processo)
- Riscos identificados

**Distribuição**:
- CEO
- Diretor Médico
- Responsável Técnico
- Gerente de Desenvolvimento
- Conselho (trimestral)

## 9. REGISTRO E DOCUMENTAÇÃO

### 9.1. Banco de Dados de Incidentes

**Sistema recomendado**: Planilha Excel estruturada (Registro_Incidentes.xlsx) com controle de versão.

**Alternativas**: Jira, Asana, sistema QMS dedicado (ex: MasterControl, Veeva Vault).

### 9.2. Campos Obrigatórios do Banco de Dados

| Campo | Tipo | Obrigatório | Exemplo |
|-------|------|-------------|---------|
| Número de Protocolo | Texto | SIM | INC-2025-001 |
| Data do Incidente | Data | SIM | 2025-03-15 14:30 |
| Data do Relato | Data | SIM | 2025-03-15 16:45 |
| Data do Registro | Data | SIM | 2025-03-16 09:00 |
| Classificação | Lista | SIM | GRAVE / NÃO GRAVE |
| Tipo | Lista | SIM | Evento Adverso / Queixa Técnica / Near Miss |
| Descrição Breve | Texto | SIM | "Sugestão incorreta de anemia ferropriva..." |
| Paciente (Iniciais) | Texto | Condicional | J.S.M. |
| Idade do Paciente | Número | Condicional | 45 |
| Houve Dano? | Sim/Não | SIM | Sim |
| Severidade do Dano | Lista | Condicional | Leve / Moderado / Grave / Ameaça à vida / Morte |
| Módulo/Funcionalidade | Texto | SIM | "Módulo de Inferência - Sugestão Diagnóstica" |
| Versão HemoDoctor | Texto | SIM | v1.5.2 |
| Hospital/Unidade | Texto | SIM | Hospital ABC - Unidade São Paulo |
| Relator | Texto | SIM | Dr. João Silva |
| Responsável Investigação | Texto | SIM | Maria Santos (Gerente de Qualidade) |
| Status | Lista | SIM | Relatado / Em Investigação / Aguardando CAPA / Fechado |
| Notificado ANVISA? | Sim/Não | SIM | Sim |
| Protocolo NOTIVISA | Texto | Condicional | NOTIVISA-12345-2025 |
| Data Notificação ANVISA | Data | Condicional | 2025-03-20 |
| Link CAPA | Texto | Condicional | CAPA-2025-005 |
| Data Fechamento | Data | Condicional | 2025-05-10 |
| Causa Raiz | Texto Longo | Condicional | "Algoritmo não validado para pacientes pediátricos..." |
| Ação Corretiva | Texto Longo | Condicional | "Implementar validação de idade no módulo Validation" |
| Recorrente? | Sim/Não | SIM | Não |
| Link Incidente Anterior | Texto | Condicional | INC-2024-089 |

### 9.3. Histórico Completo por Número de Protocolo

**Estrutura de pasta digital** (uma pasta por incidente):

```
INC-YYYY-XXX/
├── FORM-001_Relato_Incidente.pdf
├── FORM-002_Investigacao_Evento.pdf (se investigação completa)
├── FORM-004_Notificacao_ANVISA.pdf (se notificado)
├── Evidencias/
│   ├── Logs_Sistema_2025-03-15.txt
│   ├── Screenshot_Tela_Erro.png
│   ├── Dados_CBC_Paciente.csv
│   └── Relatorio_Medico_Desidentificado.pdf
├── Comunicacao/
│   ├── Email_Notificacao_Interna.pdf
│   ├── Ata_Reuniao_Analise.pdf
│   └── Protocolo_NOTIVISA.pdf
├── Acao_Corretiva/
│   ├── CAPA-2025-XXX.pdf (link para CAPA)
│   └── Relatorio_Implementacao.pdf
└── Fechamento/
    ├── Verificacao_Eficacia.pdf
    └── Email_Encerramento.pdf
```

### 9.4. Rastreabilidade de Ações Tomadas

**Manter log de ações** (dentro do banco de dados ou sistema):

| Data | Ação | Responsável | Status | Observações |
|------|------|-------------|--------|-------------|
| 2025-03-15 | Incidente relatado | Dr. João Silva | ✅ Concluído | Via email |
| 2025-03-16 | Classificado como GRAVE | Dr. Pedro RT | ✅ Concluído | RDC 67/2009 critério 4 |
| 2025-03-17 | Evidências coletadas | Maria QA | ✅ Concluído | Logs + screenshots |
| 2025-03-20 | Notificado ANVISA | Maria QA | ✅ Concluído | Protocolo NOTIVISA-12345 |
| 2025-03-25 | CAPA aberta | Maria QA | ✅ Concluído | CAPA-2025-005 |
| 2025-04-15 | Ação corretiva implementada | Dev Team | ✅ Concluído | Commit #a1b2c3 |
| 2025-05-15 | Eficácia verificada | Maria QA | ✅ Concluído | 0 recorrências em 30 dias |
| 2025-05-20 | Incidente fechado | Dr. Pedro RT | ✅ Concluído | Encerrado com sucesso |

### 9.5. Retenção de Registros

**Período mínimo de retenção**: **5 anos** a partir da data de fechamento do incidente (requisito ISO 13485:2016).

**Para dispositivos implantáveis** (não aplicável ao HemoDoctor, mas como referência): Vida útil do dispositivo + 5 anos.

**Formato de armazenamento**:
- Digital: Backup semanal (servidor + nuvem criptografada)
- Físico (opcional): Arquivo em local seguro (sala de qualidade, acesso restrito)

**Auditabilidade**: Registros devem ser imutáveis (versionamento de arquivos, logs de alteração).

## 10. INTEGRAÇÃO COM CAPA

### 10.1. Critérios para Abertura de CAPA

Nem todo incidente requer CAPA. Abrir CAPA quando:

**Obrigatório:**
- Incidente GRAVE com dano ao paciente
- Causa raiz identificada que requer ação corretiva de sistema/processo/código
- Incidente recorrente (≥ 3 ocorrências similares)
- Não-conformidade identificada durante investigação (gap de processo, de requisito, de validação)

**Opcional (decisão do Gerente de Qualidade):**
- Incidente NÃO GRAVE mas com risco potencial significativo
- Near miss que revelou fragilidade sistêmica
- Oportunidade de melhoria identificada

### 10.2. Procedimento de Abertura de CAPA

1. **Ao final da investigação** (PROC-002), decidir: "É necessário CAPA?"
2. Se SIM:
   - Preencher FORM-003_CAPA
   - Número de CAPA: CAPA-YYYY-XXX
   - **Link bidirecional**: Registrar no banco de dados
     - No incidente: Campo "Link CAPA" = CAPA-2025-XXX
     - No CAPA: Campo "Link Incidente" = INC-2025-XXX
3. Seguir procedimento PROC-003 (Procedimento CAPA)

### 10.3. Follow-up de Eficácia da Ação

**Fluxo integrado:**
1. CAPA implementado (PROC-003)
2. Eficácia verificada (PROC-003 §4.6)
3. Se eficaz: Fechar CAPA e fechar incidente
4. Se ineficaz: Reabrir investigação (PROC-002), identificar nova causa raiz

**Atualização do incidente:**
- Status: "Fechado - CAPA eficaz"
- Data de fechamento: DD/MM/AAAA
- Link para relatório de eficácia do CAPA

## 11. RELATÓRIOS PERIÓDICOS

### 11.1. Relatório Mensal

**Responsável**: Gerente de Qualidade

**Distribuição**: CEO, RT, Diretor Médico, Gerente de Desenvolvimento

**Formato**: Email + PDF anexo (3-5 páginas)

**Conteúdo**:

#### 11.1.1. Estatísticas de Incidentes

| Indicador | Valor Atual | Meta | Status |
|-----------|-------------|------|--------|
| Total de incidentes no mês | X | < 5 | 🟢 / 🔴 |
| Incidentes GRAVES | X | 0 | 🟢 / 🔴 |
| Incidentes NÃO GRAVES | X | < 5 | 🟢 / 🔴 |
| Incidentes fechados no mês | X | ≥ Abertos | 🟢 / 🔴 |
| Backlog (incidentes abertos) | X | < 10 | 🟢 / 🔴 |
| Prazos ANVISA atendidos | X% | 100% | 🟢 / 🔴 |

#### 11.1.2. Distribuição por Tipo

| Tipo | Quantidade | % do Total |
|------|------------|------------|
| Evento Adverso GRAVE | X | Y% |
| Evento Adverso NÃO GRAVE | X | Y% |
| Queixa Técnica | X | Y% |
| Near Miss | X | Y% |

#### 11.1.3. Distribuição por Módulo/Funcionalidade

Identificar módulos com mais incidentes (foco de melhoria):

| Módulo | Quantidade | Ação Recomendada |
|--------|------------|------------------|
| Inferência (HemoAI) | X | Melhorar validação de edge cases |
| Interface de Usuário | X | Treinamento de usuários |
| Integração FHIR | X | Testes de integração mais robustos |

#### 11.1.4. Gráficos

- Evolução temporal (últimos 12 meses) - gráfico de linha
- Distribuição por severidade (GRAVE vs NÃO GRAVE) - gráfico de pizza
- Tempo médio de investigação (em dias) - gráfico de barras

### 11.2. Relatório Trimestral

**Responsável**: Gerente de Qualidade

**Distribuição**: Direção, Conselho (se aplicável)

**Formato**: Apresentação (PowerPoint/Google Slides) + Documento PDF

**Conteúdo adicional** (além do mensal):

#### 11.2.1. Análise de Tendências

- Tipos de incidente mais comuns (top 5)
- Causas raízes recorrentes
- Eficácia das ações corretivas implementadas
- Novos riscos identificados

#### 11.2.2. Ações Preventivas Recomendadas

Com base nos incidentes do trimestre:
- Treinamento adicional necessário? (temas específicos)
- Melhorias de software prioritárias?
- Processos a revisar?
- Documentação a atualizar?

#### 11.2.3. Comparação com Período Anterior

| Indicador | Trimestre Atual | Trimestre Anterior | Tendência |
|-----------|-----------------|--------------------|-----------|
| Total de incidentes | X | Y | ↑ / ↓ / → |
| Incidentes GRAVES | X | Y | ↑ / ↓ / → |
| Tempo médio investigação | X dias | Y dias | ↑ / ↓ / → |
| Taxa de recorrência | X% | Y% | ↑ / ↓ / → |

### 11.3. Relatório Anual (PSUR - Periodic Safety Update Report)

**Responsável**: Responsável Técnico (RT)

**Distribuição**: ANVISA (submissão obrigatória), Direção

**Formato**: Documento formal estruturado conforme RDC 67/2009

**Prazo de submissão**: Anualmente, até 31 de março (referente ao ano anterior)

**Conteúdo obrigatório**:

#### 11.3.1. Sumário Executivo

- Total de unidades do HemoDoctor em uso (base instalada)
- Total de usuários estimados
- Total de pacientes analisados pelo sistema (estimativa)
- Resumo de incidentes (GRAVES vs NÃO GRAVES)
- Ações corretivas principais implementadas

#### 11.3.2. Descrição do Produto

- Nome comercial: HemoDoctor
- Registro ANVISA: [número]
- Classe de risco: II
- Versões em uso no período: [Ex: v1.4.0 a v1.6.2]
- Indicação de uso: Sistema de suporte à decisão clínica para interpretação de hemograma completo
- População alvo: Pacientes adultos e pediátricos com suspeita de doença hematológica

#### 11.3.3. Dados de Vendas e Distribuição

- Quantidade de licenças ativas no período
- Distribuição geográfica (estados brasileiros)
- Novos clientes no período

#### 11.3.4. Resumo de Incidentes

| Categoria | Quantidade | % Total |
|-----------|------------|---------|
| Eventos Adversos GRAVES | X | Y% |
| Eventos Adversos NÃO GRAVES | X | Y% |
| Queixas Técnicas | X | Y% |
| Near Miss | X | Y% |
| **TOTAL** | **X** | **100%** |

#### 11.3.5. Análise de Segurança

- **Taxa de incidentes**: X incidentes / 1000 usuários / ano
- **Taxa de eventos adversos graves**: X / 1000 usuários / ano
- **Comparação com benchmarks** (se disponível)
- **Avaliação**: O perfil de segurança do HemoDoctor é aceitável? Sim/Não (justificar)

#### 11.3.6. Ações Corretivas e Preventivas

Lista de CAPAs implementadas no ano, com foco em:
- Correções de bugs críticos
- Melhorias de segurança
- Atualizações de IFU ou rotulagem
- Recalls ou field safety notices (se houver)

#### 11.3.7. Mudanças de Design

- Novas funcionalidades adicionadas
- Módulos descontinuados
- Atualizações de algoritmo (especialmente HemoAI)
- Impacto nas análises de risco (RMP-001)

#### 11.3.8. Literatura Científica e Eventos Pós-Mercado

- Publicações científicas sobre o produto
- Eventos internacionais similares reportados (se relevante)
- Alertas de segurança de agências internacionais (FDA, Health Canada, CE)

#### 11.3.9. Conclusão e Recomendações

- Perfil de segurança geral do HemoDoctor
- Benefício-risco continua favorável? Sim/Não
- Ações planejadas para o próximo ano
- Mudanças regulatórias necessárias? (Ex: atualizar registro ANVISA)

## 12. TREINAMENTO

### 12.1. Treinamento para Usuários Finais (Básico)

**Público-alvo**: Todos os usuários do HemoDoctor (médicos, enfermeiros, técnicos)

**Duração**: 30 minutos

**Formato**: Online (vídeo gravado) ou presencial

**Conteúdo**:
1. O que é um incidente? (definições básicas)
2. Por que relatar é importante? (segurança do paciente, melhoria contínua)
3. Como relatar? (canais disponíveis, formulário web)
4. O que informar? (checklist de informações mínimas - ANEXO C)
5. O que acontece após o relato? (fluxo resumido, feedback esperado)

**Avaliação**: Quiz online (5 questões, nota mínima 80% para aprovação)

**Frequência**: Obrigatório para todos os novos usuários antes do primeiro uso do sistema.

### 12.2. Treinamento para Equipe Clínica (Completo)

**Público-alvo**: Equipe clínica HemoDoctor (médicos, enfermeiros, suporte técnico)

**Duração**: 2 horas

**Formato**: Presencial ou webinar interativo

**Conteúdo**:
1. Revisão de regulamentação (RDC 67/2009, ISO 13485)
2. Procedimento completo PROC-001 (todas as seções)
3. Classificação de severidade (GRAVE vs NÃO GRAVE) - casos práticos
4. Preenchimento de FORM-001 (exercício prático)
5. Coleta de evidências (técnicas e clínicas)
6. Comunicação interna e prazos
7. Integração com CAPA
8. Simulação de incidente real (role-play)

**Avaliação**:
- Quiz online (10 questões, nota mínima 80%)
- Exercício prático de preenchimento de formulário (avaliação qualitativa)

**Frequência**:
- Obrigatório para todos os membros da equipe clínica ao serem contratados
- Refresher: Anual

### 12.3. Treinamento para Equipe de Qualidade (Avançado)

**Público-alvo**: Gerente de Qualidade, Responsável Técnico, auditores internos

**Duração**: 4 horas

**Formato**: Presencial

**Conteúdo**:
1. Regulamentação aprofundada (RDC 67/2009, RDC 23/2012, ISO 13485, ISO 14971)
2. Procedimentos completos: PROC-001, PROC-002, PROC-003
3. Análise de causa raiz (5 Whys, Ishikawa, análise de falha)
4. Notificação ANVISA (portal NOTIVISA, passo a passo)
5. Gestão de CAPA (abertura, follow-up, verificação de eficácia)
6. Comunicação com ANVISA (respostas a solicitações, follow-up)
7. Relatórios periódicos (mensal, trimestral, anual PSUR)
8. Análise de tendências e KPIs
9. Casos complexos (discussão de casos reais ou hipotéticos)

**Avaliação**:
- Exame escrito (20 questões, nota mínima 85%)
- Apresentação de caso prático (avaliação qualitativa)

**Frequência**:
- Obrigatório para novos membros da equipe de qualidade
- Refresher: Anual

### 12.4. Refresher (Reciclagem)

**Público-alvo**: Todos os grupos acima

**Frequência**: Anual

**Duração**:
- Usuários finais: 15 minutos (vídeo curto)
- Equipe clínica: 1 hora (webinar)
- Equipe de qualidade: 2 horas (workshop)

**Conteúdo**:
- Revisão dos conceitos principais
- Atualizações de procedimento (se houver)
- Lições aprendidas de incidentes do ano anterior
- Novos casos práticos

**Avaliação**: Quiz simplificado (5 questões, nota mínima 80%)

### 12.5. Registro de Treinamento

**Manter registro**:
- Nome do participante
- Data do treinamento
- Tipo de treinamento (básico/completo/avançado/refresher)
- Instrutor
- Nota obtida na avaliação
- Status: Aprovado / Reprovado
- Certificado emitido: Sim/Não
- Validade do certificado (1 ano para refresher obrigatório)

**Armazenamento**: Pasta "Treinamentos" no sistema de gestão de qualidade, retenção mínima de 5 anos.

---

## ANEXOS

### ANEXO A: Fluxograma do Processo de Relato

```
┌─────────────────────────────────────────────┐
│  IDENTIFICAÇÃO DO INCIDENTE                 │
│  (Usuário, Paciente, Equipe, Qualquer Pessoa) │
└────────────────┬────────────────────────────┘
                 │
                 v
┌─────────────────────────────────────────────┐
│  RELATO VIA CANAL DISPONÍVEL                │
│  - Email: incidentes@hemodoctor.com (24/7)        │
│  - Telefone: +55 11 3456-7890 (24/7)        │
│  - Formulário Web (24/7)                    │
│  - Presencial (horário comercial)           │
└────────────────┬────────────────────────────┘
                 │
                 v
┌─────────────────────────────────────────────┐
│  REGISTRO IMEDIATO (0-24h)                  │
│  - Preencher FORM-001                       │
│  - Gerar número: INC-YYYY-XXX               │
│  - Preservar evidências                     │
│  - Notificar Gerente de Qualidade + RT      │
└────────────────┬────────────────────────────┘
                 │
                 v
┌─────────────────────────────────────────────┐
│  CLASSIFICAÇÃO DE SEVERIDADE (RT - 24h)     │
│  Critérios RDC 67/2009                      │
└────────┬────────────────────────┬───────────┘
         │                        │
         v                        v
┌──────────────────┐    ┌──────────────────┐
│  GRAVE           │    │  NÃO GRAVE       │
│  (10 dias úteis) │    │  (60 dias)       │
└────────┬─────────┘    └────────┬─────────┘
         │                        │
         v                        v
┌─────────────────────────────────────────────┐
│  AÇÃO IMEDIATA (0-24h se GRAVE)             │
│  - Avaliar necessidade de suspensão         │
│  - Alertar usuários (se necessário)         │
│  - Notificar stakeholders                   │
│  - Iniciar investigação preliminar          │
└────────────────┬────────────────────────────┘
                 │
                 v
┌─────────────────────────────────────────────┐
│  INVESTIGAÇÃO COMPLETA (PROC-002)           │
│  - Coleta de evidências                     │
│  - Análise de causa raiz                    │
│  - Relatório de investigação                │
│  Prazo: 30 dias (GRAVE) / 90 dias (NÃO GRAVE)│
└────────────────┬────────────────────────────┘
                 │
                 v
┌─────────────────────────────────────────────┐
│  NOTIFICAÇÃO ANVISA (NOTIVISA)              │
│  - FORM-004 preenchido                      │
│  - Evidências anexadas                      │
│  - Protocolo NOTIVISA recebido              │
│  Prazo: 10 dias (GRAVE) / 60 dias (NÃO GRAVE)│
└────────────────┬────────────────────────────┘
                 │
                 v
        ┌────────┴────────┐
        │  CAPA           │
        │  NECESSÁRIA?    │
        └────────┬────────┘
           │     │     │
         SIM     │    NÃO
           │     │     │
           v     │     v
┌───────────────┐│  ┌──────────────────┐
│ ABRIR CAPA    ││  │ FECHAR INCIDENTE │
│ (PROC-003)    ││  │ (Documentar)     │
└───────┬───────┘│  └──────────────────┘
        │        │
        v        │
┌───────────────┐│
│ IMPLEMENTAR   ││
│ AÇÃO          ││
└───────┬───────┘│
        │        │
        v        │
┌───────────────┐│
│ VERIFICAR     ││
│ EFICÁCIA      ││
└───────┬───────┘│
        │        │
        └────────┘
             │
             v
┌─────────────────────────────────────────────┐
│  RELATÓRIO FINAL ANVISA                     │
│  - Causa raiz confirmada                    │
│  - Ações corretivas implementadas           │
│  - Eficácia verificada                      │
│  Prazo: 60 dias (GRAVE) / 120 dias (NÃO GRAVE)│
└────────────────┬────────────────────────────┘
                 │
                 v
┌─────────────────────────────────────────────┐
│  FECHAMENTO DO INCIDENTE                    │
│  - Atualizar banco de dados                 │
│  - Arquivar documentação (5 anos)           │
│  - Comunicar stakeholders                   │
│  - Lições aprendidas                        │
└─────────────────────────────────────────────┘
```

---

### ANEXO B: Template de Email de Notificação Interna

**Assunto**: `[URGENTE - GRAVE] Incidente Relatado - INC-YYYY-XXX`
ou
**Assunto**: `[NÃO GRAVE] Incidente Relatado - INC-YYYY-XXX`

---

**De**: [Nome do relator ou Gerente de Qualidade]
**Para**: qualidade@hemodoctor.com, abel.costa@hemodoctor.com, ceo@hemodoctor.com (se GRAVE)
**CC**: [Equipe relevante]
**Data**: DD/MM/AAAA HH:MM

---

**INFORMAÇÕES DO INCIDENTE**

**Número de Protocolo**: INC-YYYY-XXX
**Data/Hora do Incidente**: DD/MM/AAAA HH:MM
**Classificação**: ☐ GRAVE (Notificar ANVISA em 10 dias úteis) / ☐ NÃO GRAVE (Notificar ANVISA em 60 dias)
**Tipo**: ☐ Evento Adverso / ☐ Queixa Técnica / ☐ Near Miss

---

**DESCRIÇÃO BREVE** (3-5 linhas):

[Inserir descrição clara e objetiva do que aconteceu]

---

**IMPACTO NO PACIENTE**:

☐ **SIM - Houve dano ao paciente** (Descrever: ____________________________________________)
☐ **NÃO - Sem dano ao paciente**
☐ **NÃO APLICÁVEL - Não havia paciente envolvido**

---

**MÓDULO/FUNCIONALIDADE AFETADA**:

[Ex: Módulo de Inferência - Sugestão Diagnóstica]

---

**VERSÃO DO HEMODOC**: vX.X.X
**HOSPITAL/UNIDADE**: [Nome do hospital/unidade]
**RELATOR**: [Nome + Função]

---

**AÇÃO IMEDIATA NECESSÁRIA?**

☐ **SIM** - Ação urgente requerida (descrever): ________________________________
☐ **NÃO** - Investigação em andamento conforme procedimento PROC-001

---

**PRÓXIMOS PASSOS**:

1. [ ] Investigação preliminar (Responsável: _______, Prazo: ___/___/___)
2. [ ] Reunião de análise agendada para: ___/___/___ às __:__
3. [ ] Notificação ANVISA até: ___/___/___ (prazo regulatório)

---

**RESPONSÁVEL PELA INVESTIGAÇÃO**: [Nome + Função]

---

**EVIDÊNCIAS COLETADAS**:
- [ ] Logs de sistema
- [ ] Screenshots
- [ ] Dados de CBC
- [ ] Prontuário médico (desidentificado)
- [ ] Outra: _____________

---

**ANEXOS**:
- FORM-001_Relato_Incidente.pdf

---

**CONTATO PARA DÚVIDAS**: [Nome] - [Email] - [Telefone]

---

_Este email foi gerado conforme PROC-001 (Procedimento de Relato de Incidentes e Tecnovigilância)._

---

### ANEXO C: Checklist de Informações Mínimas para Relato

Use esta checklist ao relatar um incidente para garantir que todas as informações essenciais sejam coletadas:

#### **INFORMAÇÕES DO INCIDENTE**
- [ ] **Data do incidente** (DD/MM/AAAA)
- [ ] **Hora do incidente** (HH:MM)
- [ ] **Local** (Hospital/Unidade/Cidade/Estado)

#### **INFORMAÇÕES DO DISPOSITIVO**
- [ ] **Nome do produto**: HemoDoctor
- [ ] **Versão do software** (Ex: v1.5.2) - verificar em "Configurações > Sobre"
- [ ] **Número de licença** (se disponível)

#### **DESCRIÇÃO DO INCIDENTE**
- [ ] **O que aconteceu?** (Descrição clara e objetiva, mínimo 3 linhas)
- [ ] **Módulo/funcionalidade afetada** (Ex: Sugestão Diagnóstica, Validação de Dados, Geração de Relatório)
- [ ] **Como foi detectado?** (Ex: Alerta do sistema, Observação do usuário, Comparação com exame confirmatório)

#### **INFORMAÇÕES DO PACIENTE** (se aplicável)
- [ ] **Iniciais** (Ex: J.S.M.) - NÃO incluir nome completo
- [ ] **Idade** (Ex: 45 anos)
- [ ] **Sexo** (M/F/Outro)
- [ ] **Prontuário** (apenas ID interno do hospital, SEM dados identificáveis)

#### **DADOS CLÍNICOS** (se aplicável)
- [ ] **Dados de CBC inseridos** (Cópia ou print dos valores inseridos no sistema)
- [ ] **Output do HemoDoctor** (Sugestão diagnóstica exibida, confidence score, alertas)
- [ ] **Diagnóstico final confirmado** (se disponível)
- [ ] **Exames complementares realizados** (se aplicável)

#### **IMPACTO NO PACIENTE**
- [ ] **Houve dano ao paciente?** (Sim/Não)
- [ ] Se SIM, descrever: **Tipo de dano** (Ex: Atraso no tratamento, Tratamento inadequado, Hospitalização)
- [ ] **Severidade do dano**:
  - [ ] Sem dano
  - [ ] Dano temporário/reversível
  - [ ] Dano permanente/incapacidade
  - [ ] Ameaça à vida
  - [ ] Morte

#### **EVIDÊNCIAS DISPONÍVEIS**
- [ ] **Screenshots/Prints de tela** (salvar como arquivo de imagem)
- [ ] **Logs de sistema** (solicitar ao suporte técnico se necessário)
- [ ] **Prontuário médico** (cópia relevante, desidentificada)
- [ ] **Outros documentos** (especificar): __________________

#### **INFORMAÇÕES DO RELATOR**
- [ ] **Nome completo**
- [ ] **Função/Cargo** (Ex: Médico Hematologista, Enfermeiro, Técnico de Laboratório)
- [ ] **Email**
- [ ] **Telefone** (com DDD)
- [ ] **Disponibilidade para entrevista?** (Sim/Não)

#### **AÇÃO IMEDIATA TOMADA** (se aplicável)
- [ ] Descrever ação imediata tomada pelo usuário (Ex: "Solicitei exames adicionais", "Consultei segundo especialista", "Suspendi uso do sistema")

---

**Enviar para**: incidentes@hemodoctor.com
ou
**Preencher formulário web**: https://idor.org/relatar-incidente

---

### ANEXO D: Lista de Contatos ANVISA

#### **PORTAL NOTIVISA** (Principal)
- **URL**: https://www.gov.br/anvisa/pt-br/assuntos/fiscalizacao/notivisa
- **Cadastro**: Requer cadastro prévio da empresa e do Responsável Técnico
- **Horário de funcionamento do portal**: 24/7 (portal online)
- **Tipo de notificação**: Eventos adversos, queixas técnicas, recalls

#### **ANVISA - GGMON (Gerência-Geral de Monitoramento de Produtos)**
- **Telefone**: +55 61 3462-6000 (Central de atendimento ANVISA)
- **Email**: notivisa@anvisa.gov.br
- **Horário de atendimento**: Segunda a sexta, 8h às 17h (horário de Brasília)
- **Uso**: Dúvidas sobre preenchimento, solicitações de informações adicionais

#### **ANVISA - Plantão de Emergência** (apenas para incidentes críticos)
- **Telefone**: 0800-642-9782 (ligação gratuita)
- **Disponibilidade**: 24/7 (final de semana e feriados)
- **Uso**: **APENAS** para incidentes GRAVES com risco iminente à saúde pública (Ex: recall urgente, multiple deaths, falha sistêmica crítica)

#### **ANVISA - Orientações e Manuais**
- **Guia de Preenchimento NOTIVISA**: https://www.gov.br/anvisa/pt-br/centraisdeconteudo/publicacoes/
- **RDC 67/2009 (Tecnovigilância)**: https://www.gov.br/anvisa
- **Legislação sobre Dispositivos Médicos**: https://www.gov.br/anvisa/pt-br/assuntos/regulamentacao/legislacao

#### **CONTATO INTERNO HEMODOCTOR** (para questões sobre relato de incidentes)
- **Gerente de Qualidade**: qualidade@hemodoctor.com / +55 11 XXXX-XXXX
- **Responsável Técnico**: abel.costa@hemodoctor.com / +55 11 XXXX-XXXX
- **CEO**: ceo@hemodoctor.com / +55 11 XXXX-XXXX
- **Plantão 24/7** (incidentes GRAVES): +55 11 3456-7890

---

## HISTÓRICO DE REVISÕES

| Versão | Data | Autor | Mudanças |
|--------|------|-------|----------|
| 1.0 | 2025-10-12 | ANVISA Regulatory Specialist | Versão inicial do procedimento de tecnovigilância conforme RDC 67/2009, ISO 13485:2016 e integração com PROC-002 e PROC-003 |

---

## APROVAÇÕES

| Função | Nome | Assinatura | Data |
|--------|------|------------|------|
| **Gerente de Qualidade** | _________________ | _________________ | ___/___/_____ |
| **Responsável Técnico** | _________________ | _________________ | ___/___/_____ |
| **CEO** | _________________ | _________________ | ___/___/_____ |

---

**FIM DO DOCUMENTO PROC-001**

**Próxima Revisão Programada**: 2026-10-12 (anual ou conforme necessário)
