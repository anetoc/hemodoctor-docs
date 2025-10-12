# 02_DEV_TECHNICAL - Desenvolvimento Técnico

## 🎯 Propósito
Documentação técnica, discussões com time de dev, decisões arquiteturais, e gestão de desenvolvimento.

## 📋 Quando Usar
- ✅ Discutir arquitetura com equipe de desenvolvimento
- ✅ Documentar decisões técnicas (ADRs)
- ✅ Registrar atas de reuniões técnicas
- ✅ Planejar sprints e features
- ✅ Especificar APIs e integrações
- ✅ Documentar stack tecnológico

## 📂 Estrutura
```
02_DEV_TECHNICAL/
├── ARQUITETURA/
│   ├── diagramas/              ← Diagramas de arquitetura
│   └── decisoes_tecnicas/      ← ADRs (Architecture Decision Records)
├── APIs/
│   ├── especificacoes/         ← Links para specs oficiais
│   └── exemplos_uso/           ← Exemplos e mock data
├── REUNIOES/
│   ├── atas/                   ← Atas de reuniões
│   └── decisoes/               ← Decisões tomadas
```

## 🤖 Agente: Dev/Technical Specialist

### Sempre Fazer
1. Verificar reuniões anteriores em REUNIOES/atas/
2. Consultar decisões técnicas existentes
3. Referenciar (não duplicar) SRS e SDD oficiais
4. Documentar novas decisões em ADR format

### Nunca Fazer
- Modificar especificações oficiais (SRS/SDD)
- Criar specs sem verificar existentes
- Duplicar conteúdo de AUTHORITATIVE_BASELINE

## 🔗 Links para Baseline
Ver `_links_baseline.md` para:
- SRS v2.2 (requisitos oficiais)
- SDD v2.0 (design oficial)
- 10 API Specifications (OpenAPI/AsyncAPI)

## 📝 Templates

### Template: ADR (Architecture Decision Record)
```markdown
# ADR-XXX: [Título da Decisão]

## Status
[Proposto | Aceito | Rejeitado | Obsoleto]

## Contexto
[Qual problema estamos tentando resolver?]

## Decisão
[O que decidimos fazer?]

## Consequências
### Positivas
- 
### Negativas
- 

## Alternativas Consideradas
1. 
2. 

## Data
YYYY-MM-DD

## Participantes
- 
```

### Template: Ata de Reunião
```markdown
# Reunião: [Assunto] - YYYY-MM-DD

## Participantes
- 
- 

## Pauta
1. 
2. 

## Discussões

### Item 1
[Resumo da discussão]

## Decisões
- [ ] Decisão 1
- [ ] Decisão 2

## Action Items
- [ ] [@responsável] Tarefa 1 - Prazo: YYYY-MM-DD
- [ ] [@responsável] Tarefa 2 - Prazo: YYYY-MM-DD

## Próxima Reunião
Data: YYYY-MM-DD
```

## 🚀 Ferramentas Sugeridas
- **Diagramas**: Mermaid, PlantUML, Draw.io
- **ADRs**: Markdown format (adr-tools compatible)
- **Versionamento**: Git para track de decisões

---
**Status**: ✅ Workspace Ativo  
**Última Atualização**: 12 de Outubro de 2025

