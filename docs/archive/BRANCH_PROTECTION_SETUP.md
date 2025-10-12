# Configuração de Branch Protection

## Como Configurar Manualmente

A proteção da branch `main` deve ser configurada via interface do GitHub:

### Passo a Passo

1. Acesse: https://github.com/anetoc/hemodoctor-docs/settings/branches

2. Clique em **"Add rule"** ou **"Add branch protection rule"**

3. Configure:
   - **Branch name pattern**: `main`
   
4. Ative as seguintes proteções:

#### ✅ Protect matching branches

**Require a pull request before merging:**
- [x] Require a pull request before merging
- [x] Require approvals: **1**
- [x] Dismiss stale pull request approvals when new commits are pushed
- [ ] Require review from Code Owners (opcional - requer CODEOWNERS file)

**Require status checks to pass before merging:**
- [x] Require status checks to pass before merging
- [x] Require branches to be up to date before merging
- Status checks que devem passar:
  - `documentation-check` (do GitHub Actions)

**Other settings:**
- [x] Require conversation resolution before merging
- [x] Require signed commits (opcional - mais seguro)
- [ ] Require linear history (opcional)
- [x] Include administrators (recomendado)

**Do not allow bypassing the above settings:**
- [x] Do not allow bypassing the above settings

**Rules applied to everyone including administrators:**
- [ ] Allow force pushes (NUNCA ativar para main)
- [ ] Allow deletions (NUNCA ativar para main)

5. Clique em **"Create"** ou **"Save changes"**

---

## ⚠️ Regras Importantes

### ❌ NUNCA Permitir
- Force pushes em `main`
- Deletar a branch `main`
- Bypass de proteções sem revisão

### ✅ SEMPRE Exigir
- Pull request com 1 aprovação mínima
- Status checks passando (CI/CD)
- Conversas resolvidas
- Branch atualizada

---

## 🔒 Impacto da Proteção

Com essas proteções ativas:

1. **Ninguém pode fazer push direto** na `main` (nem você)
2. **Todas as mudanças** devem passar por Pull Request
3. **GitHub Actions** deve passar (validation)
4. **Pelo menos 1 aprovação** necessária
5. **Histórico limpo** e auditável

---

## 🚀 Workflow com Branch Protection

```bash
# 1. Criar nova branch
git checkout -b feature/nova-funcionalidade

# 2. Fazer mudanças
git add .
git commit -m "Descrição"

# 3. Push da branch
git push origin feature/nova-funcionalidade

# 4. Criar PR via GitHub ou CLI
gh pr create --title "Título" --body "Descrição"

# 5. Aguardar aprovação e merge
# O merge só será possível após aprovação e CI passar
```

---

**Configuração recomendada aplicada!**

