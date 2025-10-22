# 🤖 Guia Rápido para Novo Agente - HemoDoctor

**Tempo de Leitura:** 10 minutos  
**Objetivo:** Colocar você operacional RAPIDAMENTE

---

## ⚡ START AQUI (2 minutos)

### Passo 1: Contexto Mínimo

**Projeto:** HemoDoctor = SaMD Classe II (hematologia pediátrica)  
**Status:** 90% completo  
**Prazo Crítico:** ANVISA em 8 dias (20/10/2025)  
**Seu Papel:** Executar tarefas da TODO list

### Passo 2: Localização

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs
```

Você está agora na raiz do projeto.

### Passo 3: Leitura Obrigatória (5 min)

1. **`CLAUDE.md`** (este arquivo) ← Contexto completo
2. **`PLANO_CONSOLIDACAO_COMPLETO_20251012.md`** ← TODO list
3. **`README.md`** ← Visão geral

---

## 📋 TODO LIST (19 Itens)

### ⚡ P0 - CRÍTICO (Próximos 8 dias)

**ANVISA (Prazo: 20 Out):**
1. [ ] Compilar 3 annexos PDF do CER-001
2. [ ] Obter 3 sign-offs (Medical, RA, QA)
3. [ ] Criar cover letter + petition
4. [ ] Gerar manifest v2.0

**TESTES (Prazo: 18 Out):**
5. [ ] Corrigir 22 bugs críticos (plaquetas)
6. [ ] Atingir 90% pass rate (atual: 72%)
7. [ ] Reunião com hematologista

### 📊 P1 - ALTA (Próximas 3 semanas)

**V&V (Prazo: 02 Nov):**
8. [ ] VVP-001 (Validation Plan)
9. [ ] TESTREP-001 (Unit Tests)
10. [ ] TESTREP-002 (Integration Tests)
11. [ ] TESTREP-003 (System Tests)
12. [ ] COV-001 (Coverage Analysis)
13. [ ] Módulo 04 completo

### 🏥 P2 - MÉDIA (Próximo mês)

**CEP (Prazo: 14 Nov):**
14. [ ] Definir equipe (PI, Co-PI, etc.)
15. [ ] Atualizar 29 docs CEP
16. [ ] Obter 5 anuências
17. [ ] Submeter Plataforma Brasil

### 📚 P3 - BAIXA (Backlog)

18. [ ] Consolidar BASELINE
19. [ ] Revisar versões

**Ver detalhes:** `PLANO_CONSOLIDACAO_COMPLETO_20251012.md`

---

## 🤖 ESCOLHER AGENTE CERTO

| Preciso... | Usar Agente... | Localização |
|------------|----------------|-------------|
| Corrigir bugs Python | `@software-architecture-specialist` | `HEMODOCTOR_AGENTES/software-architecture-specialist/` |
| Criar docs V&V | `@quality-systems-specialist` | `HEMODOCTOR_AGENTES/quality-systems-specialist/` |
| Compilar annexos | `@clinical-evidence-specialist` | `HEMODOCTOR_AGENTES/clinical-evidence-specialist/` |
| Criar formulários ANVISA | `@anvisa-regulatory-specialist` | `HEMODOCTOR_AGENTES/anvisa-regulatory-specialist/` |
| Atualizar docs CEP | `@cep-protocol-specialist` | `HEMODOCTOR_AGENTES/cep-protocol-specialist/` |
| Matriz rastreabilidade | `@traceability-specialist` | `HEMODOCTOR_AGENTES/traceability-specialist/` |

---

## 🛠️ COMANDOS ESSENCIAIS

### Navegação Básica

```bash
# Voltar para raiz
cd /Users/abelcosta/Documents/HemoDoctor/docs

# Ver estrutura
tree -L 2

# Ver arquivos recentes
ls -lt | head -20

# Ver status Git
git status
git log --oneline -10
```

### Explorar Código-Fonte

```bash
# Ir para CONSOLIDADO
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010

# Ver código Python
cd 03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex
cat api/main.py
cat api/requirements.txt

# Ver bugs
cd ../../TESTES
cat BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md
```

### Executar Testes

```bash
# Ir para testes
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/TESTES/test_automation

# Rodar todos
pytest -v

# Rodar com coverage
pytest --cov --cov-report=html

# Rodar P0 apenas
pytest -m "priority=='P0'"
```

### Ver Documentação Oficial

```bash
# Ir para BASELINE
cd AUTHORITATIVE_BASELINE

# Listar módulos
ls -1

# Ver módulo específico
cd 04_VERIFICACAO_VALIDACAO
ls -R

# Ver README
cat ../README_FINAL.md
```

### Gerar Reports

```bash
# Ir para scripts
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex/tools

# Gerar manifest ANVISA
python build_pre_anvisa_pack.py

# Gerar coverage
python coverage_report.py

# Gerar TRC (rastreabilidade)
python generate_trc.py
```

---

## 📁 ONDE ESTÁ TUDO

```
docs/
├── AUTHORITATIVE_BASELINE/          # 📄 61 docs oficiais
│   └── 01-10 Módulos/               # 9/10 completos
│
├── HEMODOCTOR_CONSOLIDADO_v2.0/     # 🔥 CÓDIGO-FONTE
│   ├── 01_SUBMISSAO_CEP/            # CEP (29 docs)
│   ├── 02_SUBMISSAO_ANVISA/         # ANVISA (52 docs)
│   ├── 03_DESENVOLVIMENTO/          # Python (2,217 arquivos)
│   ├── 04_ANALISES_ESTRATEGICAS/    # Roadmap
│   └── 05_MASTER_DOCUMENTATION/     # Inventários
│
├── HEMODOCTOR_AGENTES/              # 🤖 13 agentes
├── WORKSPACES/                      # 🏢 6 contextos
├── docs/reports/                    # 📊 19 relatórios
└── scripts/                         # 🛠️ 11 utilitários
```

---

## 🎯 PRÓXIMA AÇÃO (ESCOLHA UMA)

### Opção A: Corrigir Bugs (P0.5)

**Objetivo:** 72% → 90% pass rate

```bash
# 1. Ver bugs
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/TESTES
cat BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md

# 2. Identificar código
cd ../CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex

# 3. Usar agente
# @software-architecture-specialist analyze and fix bugs in platelet classifier
```

**Tempo:** 3-4 dias  
**Bloqueador:** Sim (P0)

---

### Opção B: Completar ANVISA (P0.1-P0.4)

**Objetivo:** Compilar annexos + sign-offs

```bash
# 1. Ver CER-001
cd AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER
cat CER-001*.md

# 2. Ver templates
cd ../../02_SUBMISSAO_ANVISA/02_APROVACOES/templates

# 3. Usar agente
# @clinical-evidence-specialist compile Annex B, D, E for CER-001
# @anvisa-regulatory-specialist create cover letter and petition
```

**Tempo:** 2-3 dias  
**Bloqueador:** Sim (P0)

---

### Opção C: Criar V&V (P1.1-P1.5)

**Objetivo:** Completar Módulo 04

```bash
# 1. Ver instruções
cat INSTRUCOES_AGENTES_FASES_A_B.md

# 2. Ver template
cd AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO

# 3. Usar agente
# @quality-systems-specialist create VVP-001 v1.0
# @quality-systems-specialist create TESTREP-001 v1.0
```

**Tempo:** 1 semana  
**Bloqueador:** Não (mas importante)

---

### Opção D: Preparar CEP (P2.1-P2.4)

**Objetivo:** Definir equipe + anuências

```bash
# 1. Ver docs CEP
cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010/01_SUBMISSAO_CEP

# 2. Ver protocolo
cat PROTOCOLO/PROJ-001*.md

# 3. Usar agente
# @cep-protocol-specialist update CEP documents with team info
```

**Tempo:** 2-3 semanas  
**Bloqueador:** Sim (mas prazo mais longo)

---

## 📊 MÉTRICAS ATUAIS

| Métrica | Valor | Meta |
|---------|-------|------|
| Completude Geral | 90% | 100% |
| Pass Rate Testes | 72% | 90% |
| Módulos Completos | 9/10 | 10/10 |
| Bugs Críticos | 22 | 0 |
| Docs Oficiais | 61 | 66 |

---

## 🚦 REGRAS DE OURO

1. **SEMPRE** leia TODO list antes de começar
2. **SEMPRE** use agente especializado apropriado
3. **SEMPRE** faça commit após mudanças
4. **NUNCA** modifique AUTHORITATIVE_BASELINE sem revisar
5. **NUNCA** crie documentos duplicados
6. **NUNCA** ignore P0

---

## 💡 DICAS

### Git Commits

```bash
# Formato preferido
git add .
git commit -m "🎯 [Categoria] Ação

Detalhes:
- Item 1
- Item 2

Impacto: P0
Módulo: 04"

git push
```

### Atalhos

```bash
# Criar aliases úteis
alias hemo='cd /Users/abelcosta/Documents/HemoDoctor/docs'
alias consol='cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010'
alias base='cd AUTHORITATIVE_BASELINE'
alias tests='cd HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/TESTES'
```

### Buscar Arquivos

```bash
# Encontrar arquivo por nome
find . -name "SRS-001*"

# Encontrar string em arquivos
grep -r "PLATELET_CLASSIFIER" .

# Contar arquivos por tipo
find . -name "*.md" | wc -l
find . -name "*.py" | wc -l
```

---

## 📞 AJUDA

### Problemas Comuns

**1. "Não sei qual agente usar"**
→ Ver tabela "ESCOLHER AGENTE CERTO" acima

**2. "Não encontro um arquivo"**
→ Use `find . -name "nome*"`

**3. "Testes não rodam"**
→ Verifique venv: `cd test_automation && source venv/bin/activate`

**4. "Git não deixa commitar"**
→ Verifique: `git status` e `git diff`

### Contato

**Responsável:** Dr. Abel Costa  
**Email:** abel.costa@hemodoctor.com

---

## ✅ CHECKLIST INICIAL

Antes de começar, verifique:

- [ ] Li `CLAUDE.md`
- [ ] Li `PLANO_CONSOLIDACAO_COMPLETO_20251012.md`
- [ ] Entendi estrutura do projeto
- [ ] Identifiquei P0 na TODO list
- [ ] Escolhi agente apropriado
- [ ] Testei comandos básicos
- [ ] Sei onde está código-fonte
- [ ] Sei onde está BASELINE

**Tudo OK?** → Escolha Opção A, B, C ou D acima e comece! 🚀

---

## 🎉 BOA SORTE!

**Você tem tudo para ter sucesso:**
- ✅ Código-fonte funcional
- ✅ Documentação 90% completa
- ✅ 13 agentes especializados
- ✅ TODO list clara
- ✅ Timeline definido

**Próxima milestone:** ANVISA (20/10 - 8 dias)

**Vamos lá!** 💪

---

**Última Atualização:** 12 de Outubro de 2025 - 23:30 BRT  
**Versão:** 1.0

