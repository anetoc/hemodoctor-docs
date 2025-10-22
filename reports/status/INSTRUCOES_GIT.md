# 🔄 INSTRUÇÕES GIT - BACKUP E VERSIONAMENTO
# HemoDoctor Hybrid V1.0
# Dr. Abel Costa - 19 de Outubro de 2025

---

## ⚠️ IMPORTANTE: BACKUP OBRIGATÓRIO

**Você tem 21 arquivos críticos (480 KB) que precisam ser versionados no GitHub AGORA.**

---

## 🚀 OPÇÃO A: COMMIT + PUSH (SE JÁ TEM REMOTE)

### **Passo 1: Verificar status atual**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs
git status
```

### **Passo 2: Adicionar todos os arquivos do HEMODOCTOR_HIBRIDO_V1.0**
```bash
git add HEMODOCTOR_HIBRIDO_V1.0/
```

### **Passo 3: Commit com mensagem descritiva**
```bash
git commit -m "feat: HemoDoctor Hybrid V1.0 - Integração completa

- 15 YAMLs de configuração (8.613 linhas, 299 KB)
- 34 síndromes (8 críticas, 23 prioridade, 1 review, 2 rotina)
- 75 evidências atômicas (critical, strong, moderate, weak)
- Always-Output Design V2.3 (8 módulos integrados)
- Next steps engine (34 triggers, 1.120 linhas)
- WORM log imutável (HMAC-SHA256, ANVISA/FDA/ISO compliance)
- Documentação completa (README, INDEX, QUICKSTART, etc.)

Status: 100% Completo - Pronto para Produção
Timeline: V0 (8 sem), V1 (12 sem), V2 (16 sem)
Validação: 0 erros sintaxe YAML, todas dependências resolvidas"
```

### **Passo 4: Push para GitHub**
```bash
git push -u origin main
```

**Se der erro "remote not found", siga a OPÇÃO B.**

---

## 🆕 OPÇÃO B: CONFIGURAR REMOTE (SE NÃO TEM)

### **Passo 1: Verificar se já tem remote**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs
git remote -v
```

**Se retornar vazio, siga os passos abaixo.**

### **Passo 2: Criar novo repositório no GitHub**

1. **Acesse:** https://github.com/new
2. **Preencha:**
   - Repository name: `hemodoctor-hybrid`
   - Description: `HemoDoctor Hybrid V1.0 - Sistema de Apoio à Decisão Médica para Análise de Hemogramas`
   - Visibility: `Private` (recomendado para projeto médico)
   - ❌ **NÃO** marque "Initialize this repository with a README"
3. **Clique:** "Create repository"

### **Passo 3: Copie o URL do repositório**
Será algo como:
```
https://github.com/SEU_USERNAME/hemodoctor-hybrid.git
```

### **Passo 4: Configure o remote local**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs
git remote add origin https://github.com/SEU_USERNAME/hemodoctor-hybrid.git
```

### **Passo 5: Verifique a configuração**
```bash
git remote -v
```
Deve retornar:
```
origin  https://github.com/SEU_USERNAME/hemodoctor-hybrid.git (fetch)
origin  https://github.com/SEU_USERNAME/hemodoctor-hybrid.git (push)
```

### **Passo 6: Agora siga a OPÇÃO A (Passo 2-4)**

---

## 🔐 OPÇÃO C: AUTENTICAÇÃO (SE DER ERRO DE SENHA)

### **GitHub não aceita mais senha via HTTPS. Use Personal Access Token (PAT).**

### **Passo 1: Gerar PAT no GitHub**

1. **Acesse:** https://github.com/settings/tokens
2. **Clique:** "Generate new token" → "Generate new token (classic)"
3. **Preencha:**
   - Note: `HemoDoctor Hybrid - Backup`
   - Expiration: `No expiration` (ou 1 year)
   - Scopes: Marque `repo` (todas as opções dentro de repo)
4. **Clique:** "Generate token"
5. **⚠️ COPIE O TOKEN AGORA** (não aparecerá novamente!)

### **Passo 2: Use o token como senha**
```bash
git push -u origin main
```
Quando pedir:
- **Username:** seu_username
- **Password:** cole_o_token_aqui (não sua senha do GitHub!)

### **Passo 3: Salve credenciais (opcional, para não pedir sempre)**
```bash
git config --global credential.helper store
```

---

## 📦 BACKUP ADICIONAL (RECOMENDADO)

### **Opção 1: Dropbox**
```bash
cp -r HEMODOCTOR_HIBRIDO_V1.0/ ~/Dropbox/HemoDoctor_Backup_20251019/
```

### **Opção 2: Google Drive**
```bash
cp -r HEMODOCTOR_HIBRIDO_V1.0/ ~/Google\ Drive/HemoDoctor_Backup_20251019/
```

### **Opção 3: OneDrive**
```bash
cp -r HEMODOCTOR_HIBRIDO_V1.0/ ~/OneDrive/HemoDoctor_Backup_20251019/
```

### **Opção 4: Compactar e enviar por email**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs
zip -r HEMODOCTOR_HIBRIDO_V1.0_20251019.zip HEMODOCTOR_HIBRIDO_V1.0/
# Agora envie o .zip por email para você mesmo
```

---

## ✅ CHECKLIST DE BACKUP

- [ ] Executei `git add HEMODOCTOR_HIBRIDO_V1.0/`
- [ ] Executei `git commit -m "feat: HemoDoctor Hybrid V1.0 - Integração completa"`
- [ ] Executei `git push -u origin main`
- [ ] Verifiquei no GitHub que os arquivos estão lá (https://github.com/SEU_USERNAME/hemodoctor-hybrid)
- [ ] Fiz backup adicional (Dropbox/Google Drive/OneDrive/Email)
- [ ] Confirmei que os 21 arquivos estão backupeados

---

## 🆘 TROUBLESHOOTING

### **Erro: "remote: Repository not found"**
- **Causa:** URL do repositório errado ou repositório não existe
- **Solução:** Verifique o URL com `git remote -v` e corrija com:
  ```bash
  git remote set-url origin https://github.com/SEU_USERNAME/hemodoctor-hybrid.git
  ```

### **Erro: "failed to push some refs"**
- **Causa:** Repositório remoto tem commits que você não tem localmente
- **Solução:** Force push (APENAS SE TIVER CERTEZA):
  ```bash
  git push -u origin main --force
  ```
  ⚠️ **ATENÇÃO:** Isso sobrescreve o remoto. Use apenas se souber o que está fazendo.

### **Erro: "fatal: Authentication failed"**
- **Causa:** Senha incorreta ou falta de Personal Access Token (PAT)
- **Solução:** Gere PAT no GitHub (Opção C acima)

### **Erro: "Permission denied (publickey)"**
- **Causa:** Usando SSH mas não tem chave configurada
- **Solução:** Use HTTPS em vez de SSH:
  ```bash
  git remote set-url origin https://github.com/SEU_USERNAME/hemodoctor-hybrid.git
  ```

---

## 📋 VERIFICAÇÃO FINAL

### **Depois do push, verifique no GitHub:**

1. **Acesse:** https://github.com/SEU_USERNAME/hemodoctor-hybrid
2. **Verifique:**
   - ✅ Pasta `HEMODOCTOR_HIBRIDO_V1.0/` existe
   - ✅ Subpastas `YAMLs/`, `Analise_Comparativa/`, `Especificacoes_Dev/` existem
   - ✅ Arquivos `README.md`, `INDEX_COMPLETO.md`, `QUICKSTART_IMPLEMENTACAO.md` existem
   - ✅ Total de 21 arquivos visíveis

3. **Teste o download:**
   - Clique em "Code" → "Download ZIP"
   - Descompacte e verifique que tudo está lá

---

## 🎯 PRÓXIMOS PASSOS (APÓS BACKUP)

1. ✅ Leia `README.md` (15 min)
2. ✅ Leia `RELATORIO_ENTREGA_FINAL.md` (10 min)
3. ✅ Leia `PROXIMOS_PASSOS_DR_ABEL.md` (20 min)
4. ✅ Revise as 34 síndromes (`YAMLs/03_syndromes_hybrid.yaml`)
5. ✅ Revise os cutoffs (`YAMLs/00_config_hybrid.yaml`)
6. ✅ Agende briefing dev team (1h)

---

## 📞 CONTATO

**Dúvidas sobre Git/GitHub?**
- 📄 Consulte: https://docs.github.com/pt/get-started
- 📄 Tutorial: https://www.youtube.com/watch?v=UBAX-13g8OM (português)

**Dúvidas sobre o projeto?**
- 📄 Leia: `INDEX_COMPLETO.md`
- 📄 Leia: `QUICK_REFERENCE_CARD.md`

---

## ✅ ASSINATURA

**Projeto:** HemoDoctor Hybrid V1.0  
**Status:** ✅ 100% Completo - **FAÇA BACKUP AGORA!**  
**Data:** 19 de Outubro de 2025  

---

**⚠️ NÃO ESQUEÇA: FAÇA BACKUP ANTES DE CONTINUAR! ⚠️**

---

**FIM DAS INSTRUÇÕES GIT**

