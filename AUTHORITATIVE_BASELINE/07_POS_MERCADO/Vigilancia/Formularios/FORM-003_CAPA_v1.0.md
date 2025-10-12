---
document_id: "FORM-003"
title: "Formulário CAPA - Corrective and Preventive Actions"
version: "1.0"
status: "OFICIAL"
date: "2025-10-12"
usage: "Usado em PROC-003 (Procedimento CAPA)"
---

# FORM-003: Formulário CAPA - Corrective and Preventive Actions

**HemoDoctor - Dispositivo Médico Classe II (SaMD)**

---

## INSTRUÇÕES DE USO

**Quando usar:**
- Após identificar necessidade de ação corretiva ou preventiva (conforme PROC-003 §3)
- Quando gatilhos obrigatórios são acionados (incidente GRAVE, auditoria, reclamação recorrente, etc.)
- Para rastrear ações corretivas/preventivas do início ao fechamento

**Como preencher:**
- **Abertura** (Etapa 1): Preencher Seções A e B
- **Análise RCA** (Etapa 2): Preencher Seção C
- **Planejamento** (Etapa 3): Preencher Seções D e E
- **Implementação** (Etapa 5): Atualizar Seção F
- **Verificação** (Etapa 6): Preencher Seção G
- **Fechamento** (Etapa 8): Completar Seção H (assinaturas finais)

**Prazo de preenchimento:**
- Conforme SLA de prioridade (ver PROC-003 §6):
  - CRÍTICA: 30 dias | ALTA: 60 dias | MÉDIA: 90 dias | BAIXA: 120 dias

**Para onde enviar/arquivar:**
- Email: qualidade@hemodoctor.com
- Arquivo original: Pasta `CAPAs/YYYY/CAPA-YYYY-XXX/`
- Retenção: Mínimo 5 anos

---

## SEÇÃO A: IDENTIFICAÇÃO (5 campos)

### A.1. Número CAPA (gerado pela Qualidade)

**CAPA-________-________**

Formato: CAPA-YYYY-XXX (ano-sequencial)

### A.2. Data de Abertura

**Data:** ___/___/______ **Hora:** _____:_____

### A.3. Tipo de CAPA

☐ **Corretiva** (problema já ocorreu - eliminar causa raiz e prevenir recorrência)

☐ **Preventiva** (problema potencial identificado - prevenir ocorrência)

### A.4. Fonte do CAPA

☐ **Incidente** (referência: INC-________-________)

☐ **Auditoria** (interna/externa)
   - Tipo: ☐ Interna ☐ Externa (certificadora/ANVISA)
   - Data da auditoria: ___/___/______
   - Não-conformidade: ☐ MAIOR ☐ MENOR

☐ **Reclamação de usuário** (recorrente ≥ 3x)
   - Número de reclamações: ________

☐ **Near Miss** (quase-acidente com potencial de dano)

☐ **Análise de tendências** (padrão negativo identificado)

☐ **Falha em teste de sistema**

☐ **Desvio de processo de qualidade**

☐ **Recall ou FSCA** (Field Safety Corrective Action)

☐ **Outro:**
_____________________________________________________________________________

### A.5. Prioridade

☐ **CRÍTICA** 🔴 (SLA: 30 dias) - Risco à segurança do paciente

☐ **ALTA** 🟠 (SLA: 60 dias) - Não-conformidade regulatória

☐ **MÉDIA** 🟡 (SLA: 90 dias) - Reclamação recorrente ou bug médio

☐ **BAIXA** 🟢 (SLA: 120 dias) - Melhoria de processo

**Prazo de conclusão:**
___/___/______

---

## SEÇÃO B: DESCRIÇÃO DO PROBLEMA (4 campos)

### B.1. Descrição Detalhada do Problema

Descrever objetivamente o problema (mínimo 100 caracteres):

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

### B.2. Evidências Iniciais

Listar todos os documentos, dados e evidências que comprovam o problema:

1. _____________________________________________________________________________
2. _____________________________________________________________________________
3. _____________________________________________________________________________
4. _____________________________________________________________________________
5. _____________________________________________________________________________

**Arquivos anexos localizados em:**
_____________________________________________________________________________

### B.3. Impacto

Marcar todas as áreas impactadas:

☐ **Paciente** (risco à segurança ou eficácia do tratamento)

☐ **Sistema** (funcionalidade, performance, disponibilidade)

☐ **Regulatório** (conformidade ANVISA, ISO, FDA)

☐ **Financeiro** (custos, perdas, multas)

☐ **Reputacional** (imagem da empresa, confiança dos usuários)

### B.4. Severidade

☐ **Crítica** (impacto imediato à segurança do paciente ou conformidade regulatória)

☐ **Alta** (impacto significativo ao sistema ou processo crítico)

☐ **Média** (impacto moderado, problema recorrente)

☐ **Baixa** (impacto mínimo, oportunidade de melhoria)

---

## SEÇÃO C: ANÁLISE DE CAUSA RAIZ (4 campos)

### C.1. Metodologia Utilizada

Metodologias aplicadas (marcar todas as utilizadas):

☐ **5 Whys** (Método Toyota)

☐ **Ishikawa** (Espinha de Peixe - 6M: Método, Máquina, Material, Mão de obra, Medida, Meio ambiente)

☐ **Análise de Modo de Falha** (Bug/Dados/Uso/Design/Infra)

☐ **Outra:**
_____________________________________________________________________________

### C.2. Análise Detalhada

**Documento de análise RCA anexo:**
☐ Sim (arquivo: _____________________________________________________________)
☐ Resumo abaixo:

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

### C.3. Causa Raiz Identificada

**Causa raiz fundamental** (específica, verificável, eliminável):

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

**Categoria da causa raiz:**
☐ Bug Crítico de software
☐ Bug Alto de software
☐ Dados Inválidos (validação faltante)
☐ Uso Inadequado (treinamento, UX)
☐ Limitação de Design (edge case não coberto)
☐ Infraestrutura (ambiente técnico)
☐ Outro: _____________________________________________________________________

### C.4. Evidências que Suportam a Causa Raiz

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

**Verificação:**
- ☐ Causa raiz é **específica** (não vaga)
- ☐ Causa raiz é **verificável** (pode ser testada)
- ☐ Causa raiz **explica 100%** do problema
- ☐ Causa raiz é **eliminável** (viável eliminar)

---

## SEÇÃO D: AÇÃO PROPOSTA (9 campos)

### D.1. Descrição da Ação (SMART)

Descrever ação em detalhes (Specific, Measurable, Achievable, Relevant, Time-bound):

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

### D.2. Objetivos da Ação

O que se espera alcançar com esta ação?

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

### D.3. Responsável Primário

**Nome completo:**
_____________________________________________________________________________

**Função:**
_____________________________________________________________________________

**Email:**
_____________________________________________________________________________

**Telefone:**
_____________________________________________________________________________

### D.4. Responsável Secundário (apoio/revisão)

**Nome completo:**
_____________________________________________________________________________

**Função:**
_____________________________________________________________________________

### D.5. Prazo de Implementação

**Data de início:** ___/___/______

**Data de conclusão prevista:** ___/___/______

**Duração estimada:** ________ dias

### D.6. Recursos Necessários

**A) Recursos Humanos:**
- Função/especialidade: ________________________ Horas estimadas: __________
- Função/especialidade: ________________________ Horas estimadas: __________
- **Total horas-pessoa:** __________

**B) Recursos Financeiros:**
- Custo de desenvolvimento: R$ ______________
- Custo de infraestrutura: R$ ______________
- Custo de treinamento: R$ ______________
- Outros custos: R$ ______________
- **Custo total estimado: R$ ______________**

**C) Recursos Técnicos:**
_____________________________________________________________________________
_____________________________________________________________________________

### D.7. Impacto em Outros Processos

**Documentos a atualizar:**
☐ SRS-001 (Software Requirements Specification)
☐ SDD (Software Design Description)
☐ TST-001 (Test Specification)
☐ IFU-001 (Instructions for Use)
☐ RMP-001 (Risk Management Plan)
☐ Outro: _____________________________________________________________________

**Sistemas/módulos afetados:**
_____________________________________________________________________________

**Necessidade de retreinamento:**
☐ Sim (público-alvo: _______________________________________________________)
☐ Não

### D.8. Aprovações Necessárias

☐ Gerente de Qualidade (sempre obrigatório)
☐ Responsável Técnico (sempre obrigatório)
☐ CEO (se custo > R$ 50.000 ou prazo > 90 dias ou risco regulatório)

### D.9. Comunicação

**Stakeholders a notificar:**
_____________________________________________________________________________

**Método:**
☐ Email ☐ Reunião ☐ Treinamento formal ☐ Release notes

---

## SEÇÃO E: CRITÉRIOS DE EFICÁCIA (3 campos)

### E.1. Como Medir Eficácia

Descrever método objetivo de verificação:

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

### E.2. Indicador Quantitativo

**Métrica específica:**
_____________________________________________________________________________

**Fórmula de cálculo:**
_____________________________________________________________________________

**Exemplo:** "0 ocorrências do bug em 60 dias" ou "100% testes passam" ou "Tempo de resposta < 5s"

### E.3. Meta e Período de Monitoramento

**Meta:** _____________________________________________________________________

**Período de monitoramento:** ________ dias (mínimo 30 dias após implementação)

**Data de início do monitoramento:** ___/___/______

**Data de fim do monitoramento:** ___/___/______

---

## SEÇÃO F: STATUS E EXECUÇÃO (5 campos)

### F.1. Status Atual

☐ **Aberto** (aguardando análise de causa raiz)

☐ **Em Análise** (RCA em andamento)

☐ **Aprovado** (plano de ação aprovado, pronto para implementação)

☐ **Em Implementação** (ação sendo executada)

☐ **Aguardando Verificação** (implementação concluída, aguardando período de monitoramento)

☐ **Em Verificação** (verificando eficácia conforme critérios)

☐ **Fechado** (eficácia verificada, CAPA concluído com sucesso)

☐ **Cancelado** (CAPA cancelado - justificar)

### F.2. Percentual de Conclusão

**% Conclusão:** _________ % (0-100%)

**Última atualização:** ___/___/______

### F.3. Datas Importantes

**Data de abertura:** ___/___/______

**Data de aprovação do plano:** ___/___/______

**Data de implementação completa:** ___/___/______

**Data de início da verificação:** ___/___/______

**Data de fechamento:** ___/___/______

### F.4. Evidências de Implementação

Listar todas as evidências de que a ação foi implementada:

☐ Código corrigido (Pull Request #________)
☐ Teste executado (relatório: _______________________________________________)
☐ Documentação atualizada (versão: ________________________________________)
☐ Treinamento realizado (certificados: _____________________________________)
☐ Outro: _____________________________________________________________________

**Arquivos de evidência localizados em:**
_____________________________________________________________________________

### F.5. Bloqueios ou Atrasos

**Houve bloqueios?**
☐ Não
☐ Sim (descrever):

_____________________________________________________________________________
_____________________________________________________________________________

**Ações tomadas para resolver bloqueios:**
_____________________________________________________________________________

---

## SEÇÃO G: VERIFICAÇÃO DE EFICÁCIA (3 campos)

### G.1. Eficácia Verificada?

☐ **Sim** ✅ (critérios 100% atendidos - prosseguir para fechamento)

☐ **Parcialmente** ⚠️ (critérios 50-99% atendidos - ações adicionais necessárias)

☐ **Não** ❌ (critérios < 50% atendidos - reavaliar causa raiz)

### G.2. Resultado da Verificação

**Comparação ANTES vs DEPOIS:**

| Métrica | Antes da Ação | Depois da Ação | Meta | Status |
|---------|---------------|----------------|------|--------|
| _________________ | __________ | __________ | __________ | ☐ ✅ ☐ ❌ |
| _________________ | __________ | __________ | __________ | ☐ ✅ ☐ ❌ |
| _________________ | __________ | __________ | __________ | ☐ ✅ ☐ ❌ |

**Análise qualitativa:**
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

**Conclusão:**
_____________________________________________________________________________

### G.3. Evidências de Eficácia

Listar evidências objetivas de que a ação foi eficaz:

1. _____________________________________________________________________________
2. _____________________________________________________________________________
3. _____________________________________________________________________________
4. _____________________________________________________________________________

**Arquivos de evidência localizados em:**
_____________________________________________________________________________

### G.4. Ações Adicionais Necessárias (se eficácia parcial ou não verificada)

☐ Não são necessárias

☐ Sim (descrever):

_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________

---

## SEÇÃO H: ASSINATURAS (4 níveis)

### H.1. Responsável do CAPA

Declaro que:
- A análise de causa raiz foi completa e verificável
- A ação foi implementada conforme planejado
- A eficácia foi verificada e os critérios foram atingidos
- Todas as evidências estão documentadas e arquivadas

**Nome completo:**
_____________________________________________________________________________

**Função:**
_____________________________________________________________________________

**Assinatura:**
_______________________________________ **Data:** ___/___/______

---

### H.2. Gerente de Qualidade (OBRIGATÓRIO)

Declaro que:
- Revisei a análise de causa raiz e a considero adequada
- Revisei o plano de ação e o considero apropriado
- Revisei a verificação de eficácia e aprovo o fechamento do CAPA
- O CAPA atendeu aos requisitos de ISO 13485:2016 e 21 CFR Part 820.100

**Aprovações por etapa:**

| Etapa | Data | Assinatura | Comentários |
|-------|------|------------|-------------|
| Abertura | ___/___/___ | _________________ | _______________ |
| Análise RCA | ___/___/___ | _________________ | _______________ |
| Plano de Ação | ___/___/___ | _________________ | _______________ |
| Fechamento | ___/___/___ | _________________ | _______________ |

**Nome completo:**
_____________________________________________________________________________

**Assinatura final:**
_______________________________________ **Data:** ___/___/______

---

### H.3. Responsável Técnico (OBRIGATÓRIO)

Declaro que:
- Revisei os aspectos técnicos da análise e da ação
- O prazo proposto é realista considerando a complexidade técnica
- Os riscos de implementação foram considerados
- A mudança está alinhada com a arquitetura do sistema
- Aprovo o fechamento do CAPA do ponto de vista técnico

**Aprovações por etapa:**

| Etapa | Data | Assinatura | Comentários |
|-------|------|------------|-------------|
| Plano de Ação | ___/___/___ | _________________ | _______________ |
| Implementação | ___/___/___ | _________________ | _______________ |
| Fechamento | ___/___/___ | _________________ | _______________ |

**Nome completo:**
_____________________________________________________________________________

**Assinatura final:**
_______________________________________ **Data:** ___/___/______

---

### H.4. CEO (SE APLICÁVEL)

**Critérios de escalonamento ao CEO:**
- ☐ Custo > R$ 50.000
- ☐ Prazo > 90 dias
- ☐ Impacto em múltiplos sistemas ou processos críticos
- ☐ Risco regulatório (recall, suspensão de vendas, perda de certificação)
- ☐ Exposição legal significativa
- ☐ Necessidade de mudança organizacional

Declaro que:
- Revisei o impacto no negócio e considero o investimento justificado
- Os riscos foram adequadamente avaliados
- Aprovo a execução deste CAPA

**Nome completo:**
_____________________________________________________________________________

**Assinatura:**
_______________________________________ **Data:** ___/___/______

**Comentários/Condições:**
_____________________________________________________________________________
_____________________________________________________________________________

---

## SEÇÃO ADICIONAL: REVISÃO DA GESTÃO DE RISCO (se aplicável)

**A ação implementada introduziu novo risco?**
☐ Sim ☐ Não

**Se Sim:**
- Novo risco adicionado ao RMP-001: ___________________________________________
- Controles de mitigação: ___________________________________________________

**A ação afetou riscos existentes?**
☐ Sim ☐ Não

**Se Sim, listar riscos atualizados:**

| Risco (RMP-001) | Mudança | RPN Antes | RPN Depois |
|-----------------|---------|-----------|------------|
| R___ | Probabilidade reduzida | ______ | ______ |
| R___ | Severidade alterada | ______ | ______ |
| R___ | Controle adicionado | ______ | ______ |

**Riscos residuais são aceitáveis?**
☐ Sim (RPN < 50) ☐ Não (ações adicionais necessárias)

**RMP-001 atualizado:**
☐ Sim (versão: ________ , data: ___/___/______)
☐ Não aplicável

---

## CHECKLIST DE FECHAMENTO

Antes de fechar o CAPA, verificar:

- [ ] Análise de causa raiz completa e aprovada (Seção C)
- [ ] Ação implementada e evidenciada (Seção D + F.4)
- [ ] Eficácia VERIFICADA e confirmada ≥ 80% critérios (Seção G)
- [ ] Gestão de risco revisada se aplicável
- [ ] Documentação atualizada (SRS, IFU, TST, RMP conforme Seção D.7)
- [ ] Treinamento realizado se aplicável
- [ ] Comunicação aos stakeholders realizada
- [ ] Todas as evidências arquivadas (pasta CAPAs/YYYY/CAPA-YYYY-XXX/)
- [ ] Todas as assinaturas obtidas (Seção H)

---

## EXEMPLO DE PREENCHIMENTO

**Cenário:** CAPA-2025-012 - Validação de Idade Pediátrica

### Exemplo - Seção A (Identificação)

- **Número:** CAPA-2025-012
- **Data de Abertura:** 15/10/2025
- **Tipo:** Corretiva
- **Fonte:** Incidente (INC-2025-008)
- **Prioridade:** ALTA (SLA 60 dias)

### Exemplo - Seção B (Problema)

**Descrição:** "Sistema HemoDoctor aceitou input de paciente pediátrico (2 anos) sem validação de idade, resultando em sugestão diagnóstica inadequada (LMA). Médico não seguiu sugestão (near miss), mas expõe risco de uso em população não validada."

**Impacto:** Paciente, Sistema, Regulatório

**Severidade:** Alta

### Exemplo - Seção C (Causa Raiz)

**Metodologia:** 5 Whys + Ishikawa

**Causa Raiz:** "Requisito REQ-FUNC-015 (validação de idade 18-80 anos) estava especificado em SRS-001 mas não foi implementado. Gap de rastreabilidade entre SRS e TST-001 (teste não cobria este requisito)."

**Categoria:** Limitação de Design + Dados Inválidos

### Exemplo - Seção D (Ação)

**Descrição:** "Implementar validação de idade pediátrica no módulo Validation Service: rejeitar input se idade < 18 anos com mensagem 'HemoDoctor validado apenas para adultos 18-80 anos'. Atualizar IFU seção Limitações. Adicionar teste TST-015."

**Responsável:** João Silva (Desenvolvedor Backend)

**Prazo:** 15/11/2025 (30 dias)

**Recursos:** R$ 1.900 (14 horas-pessoa × R$100/h + R$ 500 deploy)

### Exemplo - Seção E (Eficácia)

**Como Medir:** "Executar TST-015 (20 casos de teste). Monitorar incidentes pediátricos por 60 dias."

**Indicador:** "100% inputs com idade < 18 anos são rejeitados. 0 incidentes pediátricos em 60 dias."

**Meta:** 100% pass rate + 0 incidentes

### Exemplo - Seção G (Verificação)

**Eficácia:** Sim ✅

**Resultado:**
- TST-015: 20/20 testes passaram (100%)
- Monitoramento 60 dias (15/11 a 15/01): 0 incidentes pediátricos
- RMP-001-R12: RPN reduzido de 12 → 4

**Conclusão:** Ação foi 100% eficaz. CAPA pode ser fechado.

---

**FIM DO FORM-003**

---

*Documento controlado. Versão digital é a oficial. Cópias impressas devem ser verificadas antes do uso.*

*Total de campos: 30 (conforme PROC-003 §5)*

*Retenção: 5 anos mínimo (ISO 13485:2016)*
