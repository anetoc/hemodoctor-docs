# ⚠️ YAMLs MOVIDOS

**Data:** 21 de Outubro de 2025
**Motivo:** Consolidação para única fonte da verdade

---

## 📍 NOVA LOCALIZAÇÃO

Os 16 arquivos YAML que estavam neste diretório foram **movidos** para:

```
/Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss/config/
```

---

## 📋 ARQUIVOS MOVIDOS (16 total)

```
✅ 00_config_hybrid.yaml
✅ 01_schema_hybrid.yaml
✅ 02_evidence_hybrid.yaml (79 evidências v2.4.0)
✅ 03_syndromes_hybrid.yaml (35 síndromes v2.3.1)
✅ 04_output_templates_hybrid.yaml
✅ 05_missingness_hybrid_v2.3.yaml
✅ 05_missingness_hybrid.yaml
✅ 06_route_policy_hybrid.yaml
✅ 07_conflict_matrix_hybrid.yaml
✅ 07_normalization_heuristics.yaml
✅ 08_wormlog_hybrid.yaml
✅ 09_next_steps_engine_hybrid.yaml
✅ 10_runbook_hybrid.yaml
✅ 11_case_state_hybrid.yaml
✅ 12_output_policies_cdss.yaml
✅ 12_output_policies_hybrid.yaml
```

---

## 🎯 RAZÃO DA MUDANÇA

**Problema:** YAMLs duplicados em 2 locais diferentes
- ⚠️ `HEMODOCTOR_HIBRIDO_V1.0/YAMLs/` (especificação - AQUI)
- ✅ `hemodoctor_cdss/config/` (implementação ativa - MOVIDO PARA CÁ)

**Risco:** Dessincronização se editados em locais diferentes

**Solução:** **Única fonte da verdade** em `hemodoctor_cdss/config/`

---

## 🔧 PARA DESENVOLVEDORES

### Leitura de YAMLs

**ANTES:**
```python
# ❌ NÃO FAZER MAIS
config_path = "HEMODOCTOR_HIBRIDO_V1.0/YAMLs/00_config_hybrid.yaml"
```

**AGORA:**
```python
# ✅ CORRETO
config_path = "hemodoctor_cdss/config/00_config_hybrid.yaml"
```

### Edições

**TODOS OS EDITS** devem ser feitos em:
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss/config/
```

---

## 📚 DOCUMENTAÇÃO TÉCNICA

A documentação técnica permanece neste diretório:

```
HEMODOCTOR_HIBRIDO_V1.0/
├── README.md                       # Visão geral V1.0
├── INDEX_COMPLETO.md               # Índice detalhado
├── QUICKSTART_IMPLEMENTACAO.md     # Guia dev team
├── CLAUDE.md                       # Contexto para IA
├── Analise_Comparativa/            # Design decisions
├── Documentacao_Tecnica/           # Specs técnicos
└── YAMLs/README_MOVED.md          # Este arquivo
```

---

## ⚡ ACESSO RÁPIDO

```bash
# Ir para YAMLs ativos
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss/config

# Validar YAML
python3 -c "import yaml; yaml.safe_load(open('02_evidence_hybrid.yaml'))"

# Rodar testes
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss
export PYTHONPATH=src
python3 -m pytest tests/ -v
```

---

## 📊 VERIFICAÇÃO

**Status:** ✅ Todos os 16 YAMLs movidos com sucesso
**Data:** 21 Out 2025
**Commit:** (ver git log)
**Impacto:** Estrutura limpa + Única fonte verdade

---

**Para mais informações:** Ver `/Users/abelcosta/Documents/HemoDoctor/docs/PROGRESS.md`
