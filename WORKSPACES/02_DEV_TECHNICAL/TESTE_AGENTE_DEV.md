# 🧪 Guia de Teste: Agente Dev/Technical

**Data**: 12 de Outubro de 2025  
**Workspace**: 02_DEV_TECHNICAL  
**Status**: Pronto para teste

---

## 📊 Contexto Atual do Workspace

### Reuniões Existentes
1. ✅ **2025-10-01**: Planning Sprint 14
2. ✅ **2025-10-05**: Decisão Banco de Dados (PostgreSQL escolhido)

### Decisões Importantes
- PostgreSQL como BD principal
- MongoDB apenas para logs/cache
- Conformidade com IEC 62304 e ANVISA

---

## 🧪 TESTE 1: Criar Nova Ata de Reunião

### Cenário
Você teve uma reunião técnica hoje (12/10/2025) sobre implementação da API Gateway.

### Como Testar no Cursor

**Passo 1**: Abrir este workspace no Cursor
```bash
# No terminal do Cursor
cd /Users/abelcosta/Documents/HemoDoctor/docs/WORKSPACES/02_DEV_TECHNICAL
```

**Passo 2**: Dar o comando ao agente
```
"Tivemos uma reunião hoje sobre implementação da API Gateway. 
Participaram: Abel, João, Maria.
Decisões: Usar Kong como gateway, implementar rate limiting.
Preciso documentar essa reunião."
```

### ✅ Comportamento CORRETO do Agente

```
Agente: "Verificando REUNIOES/atas/...

Encontrei 2 reuniões anteriores:
1. 2025-10-01: Planning Sprint 14
2. 2025-10-05: Decisão Banco de Dados

Vou criar a ata de hoje (2025-10-12) sobre API Gateway.

Estrutura sugerida:
- Participantes: Abel, João, Maria
- Discussão sobre Kong
- Decisão: Kong + rate limiting
- Action items

Usar o template padrão de ata? (Ver README.md)"
```

### ❌ Comportamento INCORRETO

```
Agente: "Vou criar ata_reuniao.md"
[Cria sem verificar histórico]
[Não usa template]
[Não consulta reuniões anteriores]
```

---

## 🧪 TESTE 2: Criar ADR (Architecture Decision Record)

### Cenário
Precisa formalizar a decisão do PostgreSQL em um ADR.

### Como Testar

**Comando**:
```
"Preciso criar um ADR formalizando a decisão de usar PostgreSQL. 
Esta decisão foi tomada na reunião de 05/10."
```

### ✅ Comportamento CORRETO

```
Agente: "Verificando ARQUITETURA/decisoes_tecnicas/...

Não encontrei ADRs existentes ainda.

Vou criar ADR-001 sobre PostgreSQL.

Consultando informações:
- Reunião 2025-10-05 (decisão banco de dados)
- _links_baseline.md para SRS v2.2 (requisitos)
- Template ADR do README.md

Estrutura ADR:
- Status: Aceito
- Contexto: Necessidade de BD conformidade regulatória
- Decisão: PostgreSQL
- Consequências: [preciso que você detalhe]
- Alternativas: MongoDB (descartado por...)
- Referências: SRS v2.2, Reunião 05/10

Confirma?"
```

### ❌ Comportamento INCORRETO

```
Agente: "Vou criar o ADR"
[Não verifica ADRs existentes]
[Não consulta reunião de 05/10]
[Não referencia SRS]
[Não usa template]
```

---

## 🧪 TESTE 3: Consultar Especificações de API

### Cenário
Precisa ver as especificações da API Gateway oficial.

### Como Testar

**Comando**:
```
"Onde está a especificação oficial da API Gateway?"
```

### ✅ Comportamento CORRETO

```
Agente: "Consultando _links_baseline.md...

A especificação oficial da API Gateway está em:
AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/API_SPECS/01_API_Gateway_OpenAPI_v1.0.yaml

Este é um documento OFICIAL. 

Para trabalhar com ele aqui:
1. Consulte o arquivo oficial (não copie)
2. Se precisar de exemplos de uso, posso criar em APIs/exemplos_uso/
3. Se precisar documentar mudanças, use ARQUITETURA/decisoes_tecnicas/

Quer que eu mostre o conteúdo ou criar exemplos de uso?"
```

### ❌ Comportamento INCORRETO

```
Agente: [Copia todo o arquivo OpenAPI para o workspace]
[Não consulta _links_baseline.md]
[Cria duplicação]
```

---

## 🧪 TESTE 4: Criar Diagrama de Arquitetura

### Cenário
Quer documentar a arquitetura de microservices visualmente.

### Como Testar

**Comando**:
```
"Preciso criar um diagrama mostrando a arquitetura geral: 
API Gateway → Microservices → PostgreSQL"
```

### ✅ Comportamento CORRETO

```
Agente: "Verificando ARQUITETURA/diagramas/...

Não há diagramas ainda.

Vou criar um diagrama da arquitetura geral.

Sugestões:
1. Usar Mermaid (integrado no markdown)
2. Referenciar SDD v2.0 para detalhes arquiteturais
3. Salvar em: ARQUITETURA/diagramas/arquitetura_geral_v2025-10-12.md

Informações que consultei:
- SDD v2.0 (design oficial)
- Reuniões anteriores (decisão PostgreSQL)
- Padrão de microservices do projeto

Criar diagrama Mermaid?"
```

### ❌ Comportamento INCORRETO

```
Agente: [Cria diagrama sem verificar ARQUITETURA/diagramas/]
[Não referencia SDD v2.0]
[Não consulta decisões anteriores]
```

---

## 📋 Checklist de Verificação

Após cada teste, verificar se o agente:

### Verificações Básicas
- [ ] ✅ Verificou arquivos existentes na pasta apropriada
- [ ] ✅ Consultou _links_baseline.md quando relevante
- [ ] ✅ Consultou HISTORICO.md para contexto
- [ ] ✅ Perguntou antes de criar (não assumiu)

### Referências
- [ ] ✅ Referenciou (não copiou) documentos oficiais
- [ ] ✅ Citou SRS/SDD quando apropriado
- [ ] ✅ Linkou para reuniões/decisões anteriores

### Templates e Padrões
- [ ] ✅ Usou ou ofereceu template apropriado
- [ ] ✅ Seguiu convenções de nomenclatura
- [ ] ✅ Sugeriu estrutura adequada

### Documentação
- [ ] ✅ Mencionou atualizar HISTORICO.md
- [ ] ✅ Versionou adequadamente (se aplicável)
- [ ] ✅ Manteve contexto do trabalho anterior

---

## 🎯 Teste Completo Sugerido

### Sequência de Comandos

Execute estes comandos em sequência no Cursor:

```
1. "Tivemos reunião hoje sobre API Gateway. Documentar?"
   → Verificar se agente consulta reuniões anteriores

2. "Criar ADR formalizando decisão PostgreSQL"
   → Verificar se agente referencia reunião de 05/10

3. "Onde está spec oficial da API Gateway?"
   → Verificar se agente consulta _links_baseline.md

4. "Criar diagrama de arquitetura de microservices"
   → Verificar se agente referencia SDD v2.0

5. "Criar outra ata de reunião"
   → Verificar se agente detecta a que acabou de criar
```

---

## 🐛 Problemas Comuns

### Problema 1: Agente não verifica arquivos existentes
**Solução**: Verificar se está no diretório correto e .cursorrules está presente

### Problema 2: Agente não consulta _links_baseline.md
**Solução**: Verificar conteúdo de .cursorrules, pode precisar recarregar

### Problema 3: Agente cria duplicações
**Solução**: Reforçar no prompt que deve verificar primeiro

---

## ✅ Resultado Esperado

Ao final dos testes, você deve ter:

1. ✅ Pelo menos 1 nova ata de reunião criada (sem duplicação)
2. ✅ Pelo menos 1 ADR criado (ADR-001 sobre PostgreSQL)
3. ✅ Nenhum documento oficial duplicado no workspace
4. ✅ Todas as referências usando links (não cópias)
5. ✅ HISTORICO.md atualizado com novas atividades

---

## 📊 Como Verificar Sucesso

```bash
# Verificar estrutura criada
tree REUNIOES/atas/
tree ARQUITETURA/decisoes_tecnicas/

# Verificar que não há duplicações
../../scripts/check_duplicates.sh

# Ver histórico atualizado
cat HISTORICO.md
```

---

## 🎉 Próximos Passos

Após completar estes testes:

1. ✅ Testar outros workspaces (CEP, Clinical Decision)
2. ✅ Ajustar .cursorrules se necessário
3. ✅ Documentar feedback em HISTORICO.md
4. ✅ Começar a usar em trabalho real

---

**Status**: 📋 Guia de Teste Completo  
**Pronto para**: Teste no Cursor  
**Duração Estimada**: 15-20 minutos  
**Dificuldade**: 🟢 Fácil a 🟡 Médio

