# Proposta de Limpeza do Repositório HemoDoctor

**Data:** 23 Outubro 2025
**Branch Atual:** feature/hemodoctor-hibrido-v1.0
**Objetivo:** Limpar arquivos obsoletos e consolidar na branch `main`

---

## 📊 SITUAÇÃO ATUAL

### Estrutura Consolidada (MANTER) ✅

```
docs/
├── 📄 Essenciais (7 arquivos)
│   ├── CLAUDE.md
│   ├── README.md
│   ├── PROGRESS.md
│   ├── BUGS.md
│   ├── DECISIONS.md
│   ├── VERSION.md
│   └── STATUS_ATUAL.md
│
├── 📦 REGULATORY_PACKAGE/ (61 arquivos - v2.2/v3.2) ✅
├── 💻 hemodoctor_cdss/ (69 arquivos - código) ✅
├── 📊 reports/ (76 relatórios organizados) ✅
├── 📚 specifications/ (7 arquivos) ✅
├── 🗂️ archive/ (backups organizados) ✅
├── 🤖 .claude/skills/ (11 skills) ✅
└── 📋 Outros essenciais:
    ├── LICENSE
    ├── VERIFICACAO_ESTRUTURA_GITHUB_23OUT2025.md
    └── RESUMO_SESSAO_22_OUT_2025.md
```

**Total Essencial:** ~220 arquivos consolidados ✅

---

## 🗑️ PROPOSTA DE REMOÇÃO

### Categoria 1: Arquivos Temporários (DELETAR) ❌

**No git (6 arquivos - já no stash):**
1. `ANALISE_HYBRID_VS_AUTHORITATIVE_21OUT2025.md`
2. `CONSOLIDACAO_ESTRUTURA_COMPLETA_21OUT2025.md`
3. `FASE1_INVENTARIO_COMPLETO_21OUT2025.md`
4. `FASE2_VERSOES_IDENTIFICADAS_21OUT2025.md`
5. `FASE3_MAPEAMENTO_CATEGORIAS_21OUT2025.md`
6. `FASE4_ESTRUTURA_CONSOLIDADA_FINAL_21OUT2025.md`

**Ação:** Recuperar stash e commitar deleções

---

### Categoria 2: Diretórios Backup/Obsoletos (DELETAR) ❌

**Não rastreados pelo git:**

| Diretório | Tamanho | Motivo | Ação |
|-----------|---------|--------|------|
| `HEMODOCTOR_CONSOLIDADO_v2.0_20251010/` | 57 MB | Backup antigo (20 Out) | ❌ DELETAR |
| `HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/` | 12 KB | Backup pequeno | ❌ DELETAR |

**Rastreados pelo git (avaliar):**

| Diretório | Tamanho | Motivo | Proposta |
|-----------|---------|--------|----------|
| `AUTHORITATIVE_BASELINE/` | 1.3 MB | Docs originais v1.0 | ⚠️ Mover para `archive/` |
| `HEMODOCTOR_HIBRIDO_V1.0/` | 2.2 MB | YAMLs + specs | ⚠️ Avaliar conteúdo único |
| `HEMODOCTOR_AGENTES/` | 1.7 MB | Agentes antigos? | ⚠️ Avaliar vs .claude/skills |
| `docs/` | 576 KB | Documentação? | ⚠️ Avaliar duplicação |
| `WORKSPACES/` | 248 KB | ? | ⚠️ Avaliar necessidade |
| `templates/` | 60 KB | Templates? | ⚠️ Avaliar uso |

---

### Categoria 3: Arquivos de Análise/Scripts (AVALIAR) 🟡

**Scripts Python (mover ou deletar):**
- `generate_clinical_doc.py` (5.5 KB)
- `generate_technical_doc.py` (13 KB)

**Proposta:** Mover para `scripts/` ou `archive/scripts/`

**Outros arquivos:**
- `DASHBOARD_AGENTES_HEMODOCTOR.html` (17 KB)
- `LEIAME_COMPARACAO.txt`
- `MIGRATION_COMPARISON_STATS.txt`
- `ESTRUTURA_CONSOLIDADA_PROPOSTA.md`

**Proposta:** Mover para `archive/analysis/`

---

## 🎯 PLANO DE EXECUÇÃO

### Fase 1: Análise Detalhada (15 min)

```bash
# 1. Verificar conteúdo de HEMODOCTOR_HIBRIDO_V1.0
cd HEMODOCTOR_HIBRIDO_V1.0
ls -la
# Comparar com REGULATORY_PACKAGE para evitar perda

# 2. Verificar AUTHORITATIVE_BASELINE
cd ../AUTHORITATIVE_BASELINE
ls -la
# Confirmar se é duplicação de REGULATORY_PACKAGE

# 3. Verificar HEMODOCTOR_AGENTES
cd ../HEMODOCTOR_AGENTES
ls -la
# Comparar com .claude/skills/
```

### Fase 2: Backup Seguro (5 min)

```bash
# Criar tag de backup antes da limpeza
git tag -a backup-pre-cleanup-$(date +%Y%m%d) -m "Backup before repository cleanup"
git push origin backup-pre-cleanup-$(date +%Y%m%d)

# Criar branch de backup
git branch backup-feature-$(date +%Y%m%d)
```

### Fase 3: Limpeza (30 min)

**3.1 Recuperar deletions do stash:**
```bash
git stash pop
git add -u  # Stage deletions
git commit -m "chore: Remove temporary analysis files (FASE1-4, etc)"
```

**3.2 Deletar backups não rastreados:**
```bash
rm -rf HEMODOCTOR_CONSOLIDADO_v2.0_20251010/
rm -rf HEMODOCTOR_OFICIAL_CONSOLIDADO_20251018/
```

**3.3 Mover para archive (se conteúdo único):**
```bash
# Se AUTHORITATIVE_BASELINE tem docs v1.0 únicos
git mv AUTHORITATIVE_BASELINE archive/AUTHORITATIVE_BASELINE_v1.0

# Se HEMODOCTOR_HIBRIDO_V1.0 tem YAMLs únicos
git mv HEMODOCTOR_HIBRIDO_V1.0 archive/HEMODOCTOR_HIBRIDO_V1.0_SPECS

git commit -m "chore: Archive legacy baseline and specs"
```

**3.4 Deletar duplicações confirmadas:**
```bash
# Após confirmar duplicação
git rm -rf <diretório_duplicado>
git commit -m "chore: Remove duplicate directory <nome>"
```

### Fase 4: Merge para Main (10 min)

```bash
# Atualizar main local
git checkout main
git pull origin main

# Merge da feature
git merge feature/hemodoctor-hibrido-v1.0 --no-ff

# Push
git push origin main
```

### Fase 5: Limpeza Final (5 min)

```bash
# Deletar branch feature (opcional)
git branch -d feature/hemodoctor-hibrido-v1.0
git push origin --delete feature/hemodoctor-hibrido-v1.0

# Ou manter como archive
# git branch -m feature/hemodoctor-hibrido-v1.0 archive/feature-hemodoctor-v1.0
```

---

## 🔍 ANÁLISE NECESSÁRIA ANTES DE EXECUTAR

### Verificações Críticas:

1. ⚠️ **HEMODOCTOR_HIBRIDO_V1.0/** vs **REGULATORY_PACKAGE/**
   - Verificar se YAMLs são os mesmos ou há versões únicas
   - Confirmar que nenhum arquivo essencial será perdido

2. ⚠️ **AUTHORITATIVE_BASELINE/** vs **REGULATORY_PACKAGE/**
   - Comparar documentos v1.0 vs v2.2/v3.2
   - Decidir se preservar v1.0 para histórico

3. ⚠️ **HEMODOCTOR_AGENTES/** vs **.claude/skills/**
   - Verificar se há agentes únicos não migrados
   - Confirmar qual é a fonte da verdade

4. ⚠️ **docs/** - Avaliar conteúdo
   - Verificar se há duplicação de specs
   - Identificar arquivos únicos

---

## 📋 CHECKLIST DE APROVAÇÃO

Antes de executar a limpeza, Dr. Abel deve aprovar:

- [ ] **Fase 1:** Executar análise detalhada dos diretórios
- [ ] **Fase 2:** Criar backups (tag + branch)
- [ ] **Fase 3.1:** Deletar 6 arquivos temporários (FASE1-4, etc)
- [ ] **Fase 3.2:** Deletar 2 backups não rastreados (57 MB)
- [ ] **Fase 3.3:** Decidir sobre AUTHORITATIVE_BASELINE (mover ou deletar)
- [ ] **Fase 3.3:** Decidir sobre HEMODOCTOR_HIBRIDO_V1.0 (mover ou deletar)
- [ ] **Fase 3.3:** Decidir sobre HEMODOCTOR_AGENTES (mover ou deletar)
- [ ] **Fase 3.3:** Decidir sobre docs/ (mover ou deletar)
- [ ] **Fase 4:** Merge para main
- [ ] **Fase 5:** Deletar ou arquivar branch feature

---

## 🎯 RESULTADO ESPERADO

**Estrutura Final em `main`:**

```
hemodoctor-docs/ (main)
├── 📄 Essenciais (7 arquivos)
├── 📦 REGULATORY_PACKAGE/ (61 arquivos v2.2/v3.2) ✅
├── 💻 hemodoctor_cdss/ (69 arquivos código) ✅
├── 📊 reports/ (76 relatórios) ✅
├── 📚 specifications/ (7 arquivos) ✅
├── 🗂️ archive/ (backups + legacy docs) ✅
├── 🤖 .claude/skills/ (11 skills) ✅
├── 🔧 scripts/ (scripts úteis)
└── 📋 LICENSE + docs essenciais
```

**Eliminado:**
- ❌ 6 arquivos temporários FASE1-4 (análises concluídas)
- ❌ 57 MB backup HEMODOCTOR_CONSOLIDADO (obsoleto)
- ❌ Duplicações confirmadas
- ✅ Tudo preservado em tags/branches de backup

**Ganhos:**
- ✅ Estrutura limpa e profissional
- ✅ Sem duplicações
- ✅ Apenas arquivos essenciais na `main`
- ✅ Backups preservados (tags + archive)
- ✅ Redução de ~60-70 MB

---

## ❓ DECISÕES NECESSÁRIAS

**Dr. Abel, por favor responda:**

1. **Análise primeiro?**
   - [ ] SIM - Executar Fase 1 (análise 15 min) e reportar antes de deletar
   - [ ] NÃO - Já sei o que pode ser deletado, execute Fase 2-5

2. **AUTHORITATIVE_BASELINE/ (1.3 MB):**
   - [ ] Mover para `archive/` (preservar histórico v1.0)
   - [ ] Deletar completamente (v2.2/v3.2 são suficientes)

3. **HEMODOCTOR_HIBRIDO_V1.0/ (2.2 MB):**
   - [ ] Mover para `archive/` (preservar specs antigas)
   - [ ] Deletar completamente (consolidado em REGULATORY_PACKAGE)
   - [ ] Analisar primeiro

4. **HEMODOCTOR_AGENTES/ (1.7 MB):**
   - [ ] Mover para `archive/` (agentes legados)
   - [ ] Deletar completamente (migrado para .claude/skills)
   - [ ] Analisar primeiro

5. **Estratégia de merge:**
   - [ ] Merge e manter feature branch
   - [ ] Merge e deletar feature branch
   - [ ] Merge e arquivar feature branch

---

**Aguardando aprovação para prosseguir!** ⏳
