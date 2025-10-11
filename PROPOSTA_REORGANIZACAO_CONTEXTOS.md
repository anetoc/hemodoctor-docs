# 🎯 Proposta: Reorganização por Contextos de Trabalho

**Objetivo**: Estruturar o repositório para trabalho com **agentes especializados no Cursor**, evitando duplicação e mantendo contextos claros para cada área de atuação.

---

## 🚨 Problema Atual

Hoje o repositório está organizado por **tipo de documento** (AUTHORITATIVE_BASELINE com 10 módulos), mas você trabalha por **contexto de tarefa**:

❌ **Estrutura Atual** (orientada a compliance):
```
AUTHORITATIVE_BASELINE/
  ├── 01_REGULATORIO/
  ├── 02_CONTROLES_DESIGN/
  ├── 03_GESTAO_RISCO/
  └── ...
```

✅ **Como Você Trabalha** (orientada a tarefas):
- "Quero trabalhar na submissão ao CEP"
- "Preciso discutir arquitetura com o time de dev"
- "Vou criar os fluxogramas de decisão clínica"

---

## 💡 Solução Proposta: WORKSPACE POR CONTEXTOS

### Estrutura Híbrida

Manter `AUTHORITATIVE_BASELINE/` como **fonte autoritativa** (para submissão regulatória), mas adicionar **workspaces por contexto**:

```
hemodoctor-docs/
│
├── AUTHORITATIVE_BASELINE/          # 📦 Fonte Autoritativa (não mexer diretamente)
│   ├── 01_REGULATORIO/
│   ├── 02_CONTROLES_DESIGN/
│   └── ...
│
├── WORKSPACES/                       # 🎯 Contextos de Trabalho
│   │
│   ├── 01_ETHICS_CEP/               # Comitê de Ética
│   │   ├── README.md
│   │   ├── .cursorrules             # Regras específicas do agente
│   │   ├── PROTOCOLO_CEP.md
│   │   ├── TCLE/
│   │   ├── JUSTIFICATIVAS/
│   │   ├── CRONOGRAMA/
│   │   └── _links_baseline.md       # Links para docs oficiais
│   │
│   ├── 02_DEV_TECHNICAL/            # Time de Desenvolvimento
│   │   ├── README.md
│   │   ├── .cursorrules
│   │   ├── ARQUITETURA/
│   │   │   ├── diagramas/
│   │   │   ├── decisoes_tecnicas/
│   │   │   └── stack_tecnologico.md
│   │   ├── APIs/
│   │   │   ├── especificacoes/      # Links para API_SPECS oficial
│   │   │   └── exemplos_uso/
│   │   ├── REUNIOES/
│   │   │   ├── atas/
│   │   │   └── decisoes/
│   │   └── _links_baseline.md
│   │
│   ├── 03_CLINICAL_DECISION/        # Fluxogramas e Árvores de Decisão
│   │   ├── README.md
│   │   ├── .cursorrules
│   │   ├── FLUXOGRAMAS/
│   │   │   ├── mieloma_multiplo/
│   │   │   ├── linfomas/
│   │   │   └── leucemias/
│   │   ├── ARVORES_DECISAO/
│   │   │   ├── triagem_inicial/
│   │   │   ├── estratificacao_risco/
│   │   │   └── selecao_tratamento/
│   │   ├── CAMADAS_DECISORIAS/
│   │   │   ├── camada_1_triagem.md
│   │   │   ├── camada_2_classificacao.md
│   │   │   ├── camada_3_estratificacao.md
│   │   │   └── camada_4_recomendacao.md
│   │   ├── ALGORITMOS/
│   │   └── _links_baseline.md
│   │
│   ├── 04_REGULATORY_SUBMISSION/    # Submissões Regulatórias
│   │   ├── README.md
│   │   ├── .cursorrules
│   │   ├── ANVISA/
│   │   │   ├── checklist.md
│   │   │   ├── documentos_pendentes/
│   │   │   └── comunicacoes/
│   │   ├── FDA/
│   │   ├── TIMELINE/
│   │   └── _links_baseline.md
│   │
│   ├── 05_CLINICAL_VALIDATION/      # Validação Clínica
│   │   ├── README.md
│   │   ├── .cursorrules
│   │   ├── ESTUDOS/
│   │   │   ├── protocolo_validacao/
│   │   │   ├── dados_coletados/
│   │   │   └── analises/
│   │   ├── METRICAS/
│   │   ├── PUBLICACOES/
│   │   └── _links_baseline.md
│   │
│   └── 06_RISK_QUALITY/             # Riscos e Qualidade
│       ├── README.md
│       ├── .cursorrules
│       ├── ANALISES_RISCO/
│       ├── INCIDENTES/
│       ├── ACOES_CORRETIVAS/
│       ├── AUDITORIAS/
│       └── _links_baseline.md
│
├── HEMODOCTOR_AGENTES/              # Agentes Especializados
│
└── AGENT_CONFIGS/                    # 🤖 Configurações de Agentes Cursor
    ├── README.md
    ├── ethics_cep_agent.md          # Instruções para agente CEP
    ├── dev_technical_agent.md       # Instruções para agente Dev
    ├── clinical_decision_agent.md   # Instruções para agente Clínico
    ├── regulatory_agent.md          # Instruções para agente Regulatório
    └── validation_agent.md          # Instruções para agente Validação
```

---

## 🎯 Como Funciona

### 1. **AUTHORITATIVE_BASELINE** = Fonte da Verdade
- **Nunca editar diretamente** (exceto atualizações oficiais)
- Contém todos os documentos para submissão
- Versionado e rastreado formalmente

### 2. **WORKSPACES** = Áreas de Trabalho Ativas
- Cada workspace é um **contexto específico**
- Contém documentação de trabalho, rascunhos, discussões
- **Referencia** (não duplica) documentos da baseline
- Cada workspace tem seu próprio `.cursorrules`

### 3. **AGENT_CONFIGS** = Instruções para Agentes
- Define o comportamento de cada agente especializado
- Especifica quais arquivos/pastas cada agente deve focar
- Previne duplicação de documentos

---

## 🤖 Agentes Especializados do Cursor

### Agent: CEP/Ethics Specialist
**Contexto**: `WORKSPACES/01_ETHICS_CEP/`

**Instruções** (`.cursorrules`):
```markdown
# CEP/Ethics Specialist Agent

## Escopo
Você é especialista em Comitês de Ética em Pesquisa (CEP).

## Sempre Verificar ANTES de Criar Documentos
1. Check `WORKSPACES/01_ETHICS_CEP/` para documentos existentes
2. Check `AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER/` para evidências oficiais
3. Use `_links_baseline.md` para referenciar documentos oficiais

## Nunca
- Criar novos documentos sem verificar o que existe
- Duplicar conteúdo da AUTHORITATIVE_BASELINE
- Modificar documentos oficiais diretamente

## Tarefas Principais
- Elaborar protocolo CEP
- Preparar TCLE (Termo de Consentimento)
- Justificativas éticas
- Responder questionamentos do CEP
```

### Agent: Dev/Technical Specialist
**Contexto**: `WORKSPACES/02_DEV_TECHNICAL/`

**Instruções**:
```markdown
# Dev/Technical Specialist Agent

## Escopo
Arquitetura técnica, APIs, decisões de desenvolvimento.

## Sempre Verificar
1. `WORKSPACES/02_DEV_TECHNICAL/ARQUITETURA/`
2. `AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/` (especificações oficiais)
3. Discussões anteriores em `REUNIOES/`

## Foco
- Diagramas de arquitetura
- Decisões técnicas (ADRs)
- Discussões com time de dev
- Especificações de APIs (referência, não duplicação)
```

### Agent: Clinical Decision Specialist
**Contexto**: `WORKSPACES/03_CLINICAL_DECISION/`

**Instruções**:
```markdown
# Clinical Decision Specialist Agent

## Escopo
Fluxogramas, árvores de decisão, algoritmos clínicos.

## Sempre Verificar
1. `WORKSPACES/03_CLINICAL_DECISION/FLUXOGRAMAS/`
2. `WORKSPACES/03_CLINICAL_DECISION/ARVORES_DECISAO/`
3. Referências clínicas em `AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/`

## Foco
- Criar/atualizar fluxogramas por doença
- Definir camadas decisórias
- Documentar algoritmos
- Árvores de decisão clínica
```

---

## 📋 Arquivo `_links_baseline.md` (em cada workspace)

Exemplo para `WORKSPACES/01_ETHICS_CEP/_links_baseline.md`:

```markdown
# Links para Documentos Oficiais

## Documentos Relacionados na Baseline

### Clinical Evaluation Report
- [CER v1.2](../../AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER/CER-001_Clinical_Evaluation_Report_v1.2_OFICIAL.md)

### Software Requirements
- [SRS v2.2](../../AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/SRS-001_Software_Requirements_v2.2_AUTHORITATIVE_20251008.md)

### Risk Management
- [RMP v1.0](../../AUTHORITATIVE_BASELINE/03_GESTAO_RISCO/RMP/RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md)

## Não Duplicar
Estes documentos são oficiais. Referencie-os, não os copie.
```

---

## 🚀 Workflow Proposto

### Cenário 1: Trabalhar no Protocolo CEP

```bash
# 1. Abrir o workspace específico
cd WORKSPACES/01_ETHICS_CEP/

# 2. Ativar agente CEP no Cursor (ou usar .cursorrules)
# O agente automaticamente:
#   - Verifica documentos existentes
#   - Referencia baseline quando necessário
#   - Não duplica informações

# 3. Trabalhar no protocolo
# O agente sabe que já existe CER v1.2 e vai referenciar

# 4. Quando necessário, promover para baseline
# Copiar documento finalizado para AUTHORITATIVE_BASELINE
```

### Cenário 2: Discutir Arquitetura com Dev

```bash
# 1. Abrir workspace técnico
cd WORKSPACES/02_DEV_TECHNICAL/

# 2. Agente Dev ativo
# Automaticamente verifica:
#   - Discussões anteriores em REUNIOES/
#   - Decisões técnicas existentes
#   - APIs especificadas oficialmente

# 3. Criar nova ata de reunião
# Agente pergunta: "Vejo que já temos 3 reuniões anteriores. 
# Quer que eu resuma o contexto?"
```

### Cenário 3: Criar Fluxogramas Clínicos

```bash
# 1. Workspace de decisão clínica
cd WORKSPACES/03_CLINICAL_DECISION/

# 2. Agente Clinical Decision ativo
# Verifica fluxogramas existentes por doença

# 3. Criar novo fluxograma para Mieloma Múltiplo
# Agente: "Já temos fluxogramas para:
# - Linfoma Hodgkin
# - Leucemia Mieloide Aguda
# Quer usar como template?"
```

---

## 🔄 Sincronização com Baseline

### Quando Promover Workspace → Baseline

Documentos de trabalho devem ser promovidos para `AUTHORITATIVE_BASELINE` quando:

1. ✅ **Finalizados e revisados**
2. ✅ **Aprovados por especialistas**
3. ✅ **Versionados adequadamente**
4. ✅ **Necessários para submissão regulatória**

### Processo de Promoção

```bash
# 1. Finalizar documento no workspace
cd WORKSPACES/01_ETHICS_CEP/PROTOCOLO_CEP_FINAL.md

# 2. Revisar e aprovar

# 3. Copiar para baseline com versionamento
cp PROTOCOLO_CEP_FINAL.md \
   ../../AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/Evidencias/PROTOCOLO_CEP_v1.0_OFICIAL.md

# 4. Atualizar rastreabilidade
# Adicionar entrada na TRC

# 5. Commit com mensagem clara
git add .
git commit -m "docs: Promove protocolo CEP v1.0 para baseline oficial"
```

---

## 📊 Benefícios da Reorganização

### ✅ Para Você
1. **Contextos Claros**: Cada workspace = uma "sala" de trabalho
2. **Sem Duplicação**: Agentes verificam antes de criar
3. **Foco**: Trabalhe só no que importa agora
4. **Rastreabilidade**: Links claros para documentos oficiais

### ✅ Para os Agentes
1. **Escopo Definido**: Cada agente sabe seu território
2. **Verificação Automática**: Sempre checa o que existe
3. **Referência, Não Duplicação**: Links em vez de cópias
4. **Contexto Preservado**: Histórico de discussões mantido

### ✅ Para a Equipe
1. **Organização Clara**: Fácil encontrar documentos
2. **Colaboração**: Cada área tem seu espaço
3. **Baseline Protegida**: Fonte da verdade intocada
4. **Workspaces Flexíveis**: Experimentação sem risco

---

## 🎯 Implementação Sugerida

### Fase 1: Criar Estrutura (1 dia)
```bash
# Criar todos os workspaces
# Adicionar READMEs e .cursorrules
# Criar AGENT_CONFIGS
```

### Fase 2: Migrar Documentos de Trabalho (2-3 dias)
```bash
# Identificar docs que são "trabalho em progresso"
# Mover para workspaces apropriados
# Criar _links_baseline.md
```

### Fase 3: Configurar Agentes (1 dia)
```bash
# Criar arquivos .cursorrules para cada workspace
# Testar comportamento dos agentes
# Ajustar conforme necessário
```

### Fase 4: Documentar Workflow (1 dia)
```bash
# Criar guias de uso
# Documentar processo de promoção
# Treinar equipe
```

---

## 🤔 Decisões Necessárias

Antes de implementar, precisamos decidir:

### 1. Workspaces Iniciais
Concordo com os 6 workspaces propostos ou quer adicionar/remover algum?

### 2. Nomenclatura
Prefere nomes em português ou manter em inglês?

### 3. Ferramentas
Quer integrar alguma ferramenta específica (Mermaid para fluxogramas, PlantUML para diagramas, etc.)?

### 4. Automação
Quer scripts para:
- Verificar duplicação automática?
- Sincronizar workspace ↔ baseline?
- Validar referências?

---

## 📞 Próximo Passo

**Você decide**:

1. ✅ **Implementar agora**: Eu crio toda a estrutura
2. 🤔 **Ajustar primeiro**: Discutir modificações antes
3. 🧪 **Protótipo**: Criar só 1-2 workspaces para testar

**O que prefere?**

---

**Autor**: Agent Consultant  
**Data**: 11 de Outubro de 2025  
**Status**: 🟡 Proposta para Revisão

