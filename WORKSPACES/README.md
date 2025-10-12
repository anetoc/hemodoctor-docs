# 🎯 WORKSPACES - Áreas de Trabalho por Contexto

## 📋 Visão Geral

Os **WORKSPACES** são áreas de trabalho organizadas por **contexto funcional**, não por tipo de documento. Cada workspace contém todos os arquivos relacionados a uma atividade específica do projeto.

## 🎯 Workspaces Disponíveis

### 01_ETHICS_CEP/ - Comitê de Ética em Pesquisa
**Quando usar**: Trabalhar em documentação para submissão ao CEP, responder questionamentos, preparar TCLE.

**Contém**:
- Protocolo de pesquisa para CEP
- Termos de Consentimento (TCLE)
- Justificativas éticas
- Cronograma de atividades
- Respostas a pareceres do CEP

**Agente Especializado**: CEP/Ethics Specialist

---

### 02_DEV_TECHNICAL/ - Desenvolvimento Técnico
**Quando usar**: Discutir arquitetura com time de dev, documentar decisões técnicas, planejar sprints.

**Contém**:
- Diagramas de arquitetura
- Decisões técnicas (ADRs)
- Especificações de APIs (links)
- Atas de reuniões com dev team
- Decisões de implementação

**Agente Especializado**: Dev/Technical Specialist

---

### 03_CLINICAL_DECISION/ - Fluxogramas e Árvores de Decisão
**Quando usar**: Criar/atualizar fluxogramas clínicos, documentar árvores de decisão, definir camadas decisórias.

**Contém**:
- Fluxogramas por doença
- Árvores de decisão clínica
- Camadas decisórias (triagem → classificação → estratificação → recomendação)
- Algoritmos de suporte à decisão

**Agente Especializado**: Clinical Decision Specialist

---

### 04_REGULATORY_SUBMISSION/ - Submissões Regulatórias
**Quando usar**: Preparar documentação para ANVISA/FDA, organizar cronograma de submissão, responder questionamentos.

**Contém**:
- Checklists de submissão
- Documentos pendentes
- Comunicações com agências regulatórias
- Timeline de submissão
- Tracking de status

**Agente Especializado**: Regulatory Submission Specialist

---

### 05_CLINICAL_VALIDATION/ - Validação Clínica
**Quando usar**: Planejar estudos de validação, analisar dados clínicos, preparar publicações.

**Contém**:
- Protocolos de validação
- Dados coletados (anonimizados)
- Análises estatísticas
- Métricas de performance
- Manuscritos para publicação

**Agente Especializado**: Clinical Validation Specialist

---

### 06_RISK_QUALITY/ - Gestão de Riscos e Qualidade
**Quando usar**: Analisar riscos, gerenciar incidentes, implementar ações corretivas, preparar auditorias.

**Contém**:
- Análises de risco detalhadas
- Registro de incidentes
- Ações corretivas e preventivas
- Preparação para auditorias
- Documentação de qualidade

**Agente Especializado**: Risk & Quality Specialist

---

## 🤖 Como Funcionam os Agentes

Cada workspace tem um arquivo `.cursorrules` que configura o comportamento do agente quando você está trabalhando naquele contexto:

### O Agente Sempre Faz:
1. ✅ **Verifica** documentos existentes no workspace
2. ✅ **Consulta** `_links_baseline.md` para referências oficiais
3. ✅ **Pergunta** se quer reutilizar conteúdo existente
4. ✅ **Referencia** (não duplica) documentos da AUTHORITATIVE_BASELINE

### O Agente Nunca Faz:
1. ❌ Cria documento sem verificar o que existe
2. ❌ Duplica conteúdo da baseline autoritativa
3. ❌ Modifica documentos oficiais diretamente
4. ❌ Trabalha sem contexto do histórico

---

## 📂 Estrutura de Cada Workspace

Todos os workspaces seguem o mesmo padrão:

```
WORKSPACES/XX_NOME/
├── README.md              ← Guia do workspace
├── .cursorrules          ← Configuração do agente
├── _links_baseline.md    ← Links para docs oficiais
├── [subpastas]           ← Conteúdo específico
└── HISTORICO.md          ← Log de mudanças importantes
```

---

## 🔄 Relação com AUTHORITATIVE_BASELINE

### AUTHORITATIVE_BASELINE = Fonte da Verdade
- Contém documentos **oficiais** para submissão regulatória
- **Não editar diretamente** (exceto atualizações formais)
- Versionado rigorosamente
- Rastreado na matriz TRC

### WORKSPACES = Área de Trabalho
- Contém documentos **de trabalho** e discussões
- **Referencia** baseline via `_links_baseline.md`
- Flexível para experimentação
- Quando finalizado → promove para baseline

---

## 🚀 Workflow Típico

### 1. Escolher Workspace Apropriado
```bash
cd WORKSPACES/01_ETHICS_CEP/    # Trabalhar no CEP
cd WORKSPACES/03_CLINICAL_DECISION/  # Criar fluxogramas
```

### 2. Agente Ativa Automaticamente
O arquivo `.cursorrules` configura o comportamento do agente para aquele contexto.

### 3. Trabalhar com Contexto Completo
- Vê histórico de trabalho anterior
- Acessa referências oficiais via links
- Agente sugere reutilização quando apropriado

### 4. Promover para Baseline (Quando Pronto)
```bash
# Documento finalizado e aprovado
cp WORKSPACES/01_ETHICS_CEP/PROTOCOLO_CEP_FINAL.md \
   AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/Evidencias/PROTOCOLO_CEP_v1.0_OFICIAL.md

# Atualizar TRC
# Commit com mensagem clara
git commit -m "docs: Promove protocolo CEP v1.0 para baseline"
```

---

## 📊 Benefícios dos Workspaces

### Para Você
- 🎯 **Foco**: Trabalha só no contexto relevante agora
- 🧹 **Organização**: Tudo relacionado em um lugar
- 🔍 **Encontra Fácil**: Sabe onde procurar
- ❌ **Zero Duplicação**: Agente verifica antes de criar

### Para os Agentes
- 🤖 **Contexto Claro**: Sabe o que fazer
- 📋 **Verifica Primeiro**: Não duplica
- 🔗 **Referencia Certo**: Links em vez de cópias
- 💡 **Sugere Melhor**: Conhece o histórico

### Para a Equipe
- 👥 **Colaboração**: Cada um no seu workspace
- 🛡️ **Baseline Protegida**: Ninguém mexe por engano
- 📖 **Documentado**: Tudo tem histórico
- 🔄 **Processo Claro**: Workspace → Baseline

---

## 📚 Recursos Adicionais

- **Configurações de Agentes**: Ver `/AGENT_CONFIGS/`
- **Proposta Completa**: Ver `/PROPOSTA_REORGANIZACAO_CONTEXTOS.md`
- **Guia de Uso**: Ver `/GUIA_USO_WORKSPACES.md` (a criar)

---

## 🆘 Ajuda

### "Como escolho qual workspace usar?"
Pergunte: "O que vou fazer agora?"
- Trabalhar no CEP? → `01_ETHICS_CEP/`
- Discutir com dev? → `02_DEV_TECHNICAL/`
- Criar fluxogramas? → `03_CLINICAL_DECISION/`

### "Posso criar novos workspaces?"
Sim! Siga o padrão:
```bash
mkdir -p WORKSPACES/07_NOVO_CONTEXTO/
# Copie .cursorrules e README.md de outro workspace
# Adapte para o novo contexto
```

### "E se um documento se encaixa em múltiplos workspaces?"
- Escolha o workspace **principal** (onde mais vai trabalhar)
- Crie **links** nos outros workspaces apontando para ele

---

**Status**: ✅ Sistema Implementado  
**Versão**: 1.0  
**Data**: 12 de Outubro de 2025

