# 🤖 AGENT_CONFIGS - Configurações de Agentes do Cursor

## 📋 Visão Geral

Este diretório contém configurações e instruções para cada agente especializado do sistema HemoDoctor. Cada workspace tem seu próprio agente configurado via `.cursorrules`.

## 🎯 Agentes Disponíveis

| Agente | Workspace | Foco Principal |
|--------|-----------|----------------|
| **CEP/Ethics Specialist** | 01_ETHICS_CEP/ | Protocolos CEP, TCLE, ética |
| **Dev/Technical Specialist** | 02_DEV_TECHNICAL/ | Arquitetura, ADRs, reuniões dev |
| **Clinical Decision Specialist** | 03_CLINICAL_DECISION/ | Fluxogramas, árvores decisão |
| **Regulatory Submission Specialist** | 04_REGULATORY_SUBMISSION/ | Submissões ANVISA/FDA |
| **Clinical Validation Specialist** | 05_CLINICAL_VALIDATION/ | Estudos, métricas, publicações |
| **Risk & Quality Specialist** | 06_RISK_QUALITY/ | Riscos, incidentes, CAPAs |

## 🔧 Como Funcionam os Agentes

### 1. Ativação Automática
Quando você abre um workspace específico no Cursor, o arquivo `.cursorrules` daquele diretório configura automaticamente o comportamento do agente.

### 2. Contexto Especializado
Cada agente tem:
- **Conhecimento específico** da área
- **Regras de verificação** (sempre checa o que existe)
- **Padrões de referência** (não duplica, apenas referencia)
- **Templates e workflows** específicos

### 3. Prevenção de Duplicação
Todos os agentes seguem a regra crítica:
```
ANTES de criar qualquer documento:
1. Verificar arquivos existentes no workspace
2. Consultar _links_baseline.md
3. Perguntar ao usuário sobre reutilização
```

## 📚 Documentação de Cada Agente

Veja os arquivos individuais para instruções detalhadas:

- [ethics_cep_agent.md](./ethics_cep_agent.md) - CEP/Ethics Specialist
- [dev_technical_agent.md](./dev_technical_agent.md) - Dev/Technical Specialist  
- [clinical_decision_agent.md](./clinical_decision_agent.md) - Clinical Decision Specialist
- [regulatory_agent.md](./regulatory_agent.md) - Regulatory Submission Specialist
- [validation_agent.md](./validation_agent.md) - Clinical Validation Specialist
- [risk_quality_agent.md](./risk_quality_agent.md) - Risk & Quality Specialist

## 🎮 Como Usar

### Opção 1: Trabalhar em um Workspace Específico
```bash
# Abrir workspace no Cursor
cd WORKSPACES/01_ETHICS_CEP/

# O agente CEP/Ethics ativa automaticamente
# Começar a trabalhar normalmente
```

### Opção 2: Trocar de Contexto
```bash
# Mudar de CEP para Dev
cd ../02_DEV_TECHNICAL/

# Agente Dev/Technical ativa automaticamente
# Novo contexto, novas regras
```

### Opção 3: Usar Agente Manualmente
Se o Cursor não detectar automaticamente, você pode:
1. Abrir o arquivo `.cursorrules` do workspace
2. O Cursor carregará as regras
3. Ou copiar as regras para o chat do Cursor

## ⚙️ Customização de Agentes

### Modificar Regras de um Agente
1. Editar `WORKSPACES/XX_NOME/.cursorrules`
2. Seguir o formato existente
3. Testar o comportamento
4. Documentar mudanças

### Adicionar Novo Agente
1. Criar novo workspace
2. Copiar `.cursorrules` de workspace similar
3. Adaptar para novo contexto
4. Adicionar entrada neste README

## 🔍 Verificação de Comportamento

### Como Testar um Agente
```
1. Abrir workspace
2. Pedir ao agente: "Crie documento X"
3. Verificar se agente:
   ✅ Pergunta sobre documentos existentes
   ✅ Consulta _links_baseline.md
   ✅ Oferece reutilização
   ❌ NÃO cria sem verificar
```

### Exemplo de Teste
```
User: "Crie um protocolo CEP"

Agente CEP Correto:
"Verificando PROTOCOLO_CEP/...
 Encontrei protocolo_pesquisa_v1.md (60% completo).
 Quer continuar este ou criar novo?"

Agente CEP Incorreto:
"Vou criar protocolo_cep.md"
[Cria sem verificar - ERRADO!]
```

## 📊 Princípios Fundamentais

Todos os agentes seguem estes princípios:

### 1. SEMPRE Verificar Primeiro
```
❌ Criar documento direto
✅ Verificar → Perguntar → Criar
```

### 2. Referenciar, Não Duplicar
```
❌ Copiar conteúdo de AUTHORITATIVE_BASELINE
✅ Linkar: "Ver CER v1.2, Seção 3.2"
```

### 3. Manter Rastreabilidade
```
✅ Registrar em HISTORICO.md
✅ Documentar decisões
✅ Manter versões
```

### 4. Respeitar Baseline
```
❌ Modificar docs em AUTHORITATIVE_BASELINE
✅ Trabalhar em WORKSPACES
✅ Promover quando pronto
```

## 🚀 Comandos Úteis

### Verificar Agente Ativo
```bash
# Ver regras do agente atual
cat .cursorrules
```

### Listar Todos os Agentes
```bash
# Ver todos os .cursorrules
find ../WORKSPACES -name ".cursorrules" -exec echo {} \;
```

### Comparar Agentes
```bash
# Ver diferenças entre agentes
diff WORKSPACES/01_ETHICS_CEP/.cursorrules \
     WORKSPACES/02_DEV_TECHNICAL/.cursorrules
```

## 📖 Recursos Adicionais

- **Proposta Completa**: Ver `/PROPOSTA_REORGANIZACAO_CONTEXTOS.md`
- **Guia de Uso**: Ver `/GUIA_USO_WORKSPACES.md`
- **Workspaces README**: Ver `/WORKSPACES/README.md`

## 🆘 Troubleshooting

### Agente não está verificando antes de criar
**Solução**: Verificar se `.cursorrules` existe no workspace e contém as regras de verificação.

### Agente está duplicando conteúdo
**Solução**: Revisar regras de referência no `.cursorrules`, adicionar verificação de `_links_baseline.md`.

### Agente não conhece contexto
**Solução**: Adicionar conhecimento específico na seção "Knowledge Base" do `.cursorrules`.

---

**Status**: ✅ Sistema de Agentes Completo  
**Versão**: 1.0  
**Data**: 12 de Outubro de 2025

