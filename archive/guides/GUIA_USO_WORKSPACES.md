# 📖 Guia de Uso dos Workspaces

## 🎯 Início Rápido

### Passo 1: Escolha o Workspace
Pergunte-se: "O que vou fazer agora?"

| Atividade | Workspace |
|-----------|-----------|
| Trabalhar no protocolo CEP | `01_ETHICS_CEP/` |
| Reunião com time de dev | `02_DEV_TECHNICAL/` |
| Criar fluxogramas clínicos | `03_CLINICAL_DECISION/` |
| Preparar submissão ANVISA | `04_REGULATORY_SUBMISSION/` |
| Analisar dados clínicos | `05_CLINICAL_VALIDATION/` |
| Gerenciar riscos/qualidade | `06_RISK_QUALITY/` |

### Passo 2: Abra o Workspace
```bash
cd WORKSPACES/[nome_do_workspace]/
```

### Passo 3: Trabalhe Normalmente
O agente especializado está automaticamente ativo e irá:
- ✅ Verificar documentos existentes
- ✅ Consultar referências oficiais
- ✅ Sugerir reutilização
- ✅ Prevenir duplicação

## 📚 Workflows Comuns

### Workflow 1: Elaborar Protocolo CEP

```bash
# 1. Abrir workspace CEP
cd WORKSPACES/01_ETHICS_CEP/

# 2. Iniciar conversa com agente
> "Preciso criar o protocolo de pesquisa para o CEP"

# 3. Agente verifica automaticamente
Agente: "Verificando PROTOCOLO_CEP/...
         Encontrei protocolo_pesquisa_v1.md (60% completo).
         Quer continuar este ou criar novo?"

# 4. Você decide
> "Continuar o v1"

# 5. Agente trabalha com contexto
Agente: "Vou continuar protocolo_pesquisa_v1.md.
         Consultando CER v1.2 para evidências clínicas...
         O que quer adicionar/modificar?"
```

### Workflow 2: Documentar Reunião Técnica

```bash
# 1. Abrir workspace técnico
cd WORKSPACES/02_DEV_TECHNICAL/

# 2. Solicitar ata de reunião
> "Tivemos reunião hoje sobre arquitetura de microservices"

# 3. Agente consulta histórico
Agente: "Verificando REUNIOES/atas/...
         Encontrei 3 reuniões anteriores sobre arquitetura.
         Vou criar ata de hoje. Quem participou?"

# 4. Fornecer informações
> "Participaram: João, Maria, Pedro
   Decidimos usar PostgreSQL em vez de MongoDB"

# 5. Agente documenta com contexto
Agente: "Vou documentar como ADR-XXX também,
         pois é uma decisão arquitetural importante."
```

### Workflow 3: Criar Fluxograma Clínico

```bash
# 1. Abrir workspace de decisão clínica
cd WORKSPACES/03_CLINICAL_DECISION/

# 2. Solicitar fluxograma
> "Criar fluxograma de triagem para mieloma múltiplo"

# 3. Agente verifica
Agente: "Verificando FLUXOGRAMAS/mieloma_multiplo/...
         Não há fluxograma de triagem ainda.
         
         Vou criar baseado em:
         - Critérios IMWG
         - CER v1.2 (evidências)
         - Camada 1: TRIAGEM
         
         Usar Mermaid para o diagrama?"

# 4. Confirmar e colaborar
> "Sim, use Mermaid. Incluir critérios CRAB e SLiM"

# 5. Agente cria com validação
Agente: "Fluxograma criado. 
         ⚠️ Precisa validação clínica antes de usar.
         Quer que eu marque isso no documento?"
```

## 🔄 Promovendo Trabalho para Baseline

Quando um documento está **finalizado e aprovado**:

### Passo 1: Revisar e Finalizar
```bash
# Certificar que documento está completo
# Revisar com equipe apropriada
# Obter aprovações necessárias
```

### Passo 2: Promover para Baseline
```bash
# Exemplo: Protocolo CEP finalizado
cp WORKSPACES/01_ETHICS_CEP/PROTOCOLO_CEP/protocolo_final.md \
   AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/Evidencias/PROTOCOLO_CEP_v1.0_OFICIAL.md

# Versionar adequadamente (v1.0, OFICIAL)
```

### Passo 3: Atualizar Rastreabilidade
```bash
# Adicionar entrada na matriz TRC
# Referenciar requisitos relacionados
# Documentar em HISTORICO.md
```

### Passo 4: Commit Formal
```bash
git add .
git commit -m "docs: Promove Protocolo CEP v1.0 para baseline oficial

- Protocolo completo e aprovado
- Adicionado à baseline autoritativa
- TRC atualizada
- Ref: WORKSPACES/01_ETHICS_CEP/PROTOCOLO_CEP/"

git push
```

## ⚙️ Comandos Úteis

### Verificar Duplicação
```bash
./scripts/check_duplicates.sh
```

### Ver Status de um Workspace
```bash
cd WORKSPACES/01_ETHICS_CEP/
cat HISTORICO.md
```

### Listar Todos os Workspaces
```bash
ls -la WORKSPACES/
```

### Ver Regras do Agente Atual
```bash
cat .cursorrules
```

### Buscar Documento em Todos os Workspaces
```bash
grep -r "termo_busca" WORKSPACES/
```

## 🎨 Boas Práticas

### ✅ Faça

1. **Sempre comece no workspace apropriado**
   - Contexto correto = agente correto

2. **Confie no agente para verificar existentes**
   - Ele foi treinado para isso

3. **Mantenha HISTORICO.md atualizado**
   - Registre atividades importantes

4. **Use _links_baseline.md para referenciar**
   - Nunca copie conteúdo oficial

5. **Documente decisões importantes**
   - ADRs, atas de reunião, justificativas

### ❌ Não Faça

1. **Não trabalhe diretamente em AUTHORITATIVE_BASELINE**
   - Use workspaces, promova quando pronto

2. **Não copie documentos oficiais**
   - Referencie via links

3. **Não crie documentos sem verificar**
   - Deixe o agente verificar primeiro

4. **Não misture contextos**
   - CEP em workspace CEP, Dev em workspace Dev

5. **Não ignore sugestões do agente**
   - Se ele encontrou algo existente, considere usar

## 🐛 Troubleshooting

### Problema: Agente não está verificando antes de criar
**Solução**:
```bash
# Verificar se está no workspace correto
pwd

# Verificar se .cursorrules existe
ls -la .cursorrules

# Se necessário, reabrir o Cursor no workspace
```

### Problema: Não sei qual workspace usar
**Solução**:
```bash
# Ver descrição de todos
cat WORKSPACES/README.md

# Ou perguntar ao agente geral
> "Qual workspace devo usar para [atividade]?"
```

### Problema: Documentos ficando desorganizados
**Solução**:
```bash
# Revisar estrutura do workspace
tree WORKSPACES/01_ETHICS_CEP/

# Seguir estrutura definida no README
cat WORKSPACES/01_ETHICS_CEP/README.md
```

### Problema: Preciso de documentação que não existe
**Solução**:
1. Verificar se deveria estar em AUTHORITATIVE_BASELINE
2. Se sim, consultar via _links_baseline.md
3. Se não, criar no workspace apropriado
4. Documentar em HISTORICO.md

## 📊 Exemplo Completo: Dia de Trabalho

```bash
# Manhã: Trabalhar no protocolo CEP
cd WORKSPACES/01_ETHICS_CEP/
# [Trabalhar no protocolo com agente CEP]

# Meio-dia: Reunião técnica com dev team
cd ../02_DEV_TECHNICAL/
# [Documentar reunião com agente Dev]

# Tarde: Criar fluxogramas clínicos
cd ../03_CLINICAL_DECISION/
# [Criar fluxogramas com agente Clinical]

# Fim do dia: Verificar se tudo está ok
cd ../..
./scripts/check_duplicates.sh

# Commit do trabalho do dia
git add WORKSPACES/
git commit -m "docs: Trabalho do dia - CEP, reunião dev, fluxogramas"
git push
```

## 🆘 Ajuda

### Dúvidas sobre Workspaces
- Ver: `WORKSPACES/README.md`
- Ver: `PROPOSTA_REORGANIZACAO_CONTEXTOS.md`

### Dúvidas sobre Agentes
- Ver: `AGENT_CONFIGS/README.md`
- Ver: Arquivo `.cursorrules` do workspace

### Dúvidas Técnicas
- Ver: `AUTHORITATIVE_BASELINE/README_FINAL.md`
- Ver: Documentação oficial nos módulos

---

## ✅ Checklist de Uso Efetivo

Use este checklist para garantir que está usando os workspaces corretamente:

- [ ] Escolhi o workspace apropriado para a tarefa
- [ ] Li o README do workspace
- [ ] Deixei o agente verificar existentes antes de criar
- [ ] Estou referenciando (não copiando) docs oficiais
- [ ] Registrei atividades em HISTORICO.md
- [ ] Documentei decisões importantes
- [ ] Verifiquei duplicação com script
- [ ] Versionei documentos adequadamente

---

**Status**: ✅ Guia Completo  
**Versão**: 1.0  
**Data**: 12 de Outubro de 2025  
**Feedback**: hemodoctor@hemodoctor.com

