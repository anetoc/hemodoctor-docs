# 🚀 PRÓXIMOS PASSOS - Sprint 0 (98% → 100%)

**Data:** 21 de Outubro de 2025
**Status Atual:** Sprint 0 98% completo
**Objetivo:** Completar Sprint 0 para 100% (Coverage 44% → 85%)
**Tempo Estimado:** ~4h de trabalho

---

## 📋 CONTEXTO RÁPIDO

### ✅ **O QUE JÁ ESTÁ PRONTO:**

| Componente | Status |
|------------|--------|
| **Implementação** | 98% ✅ (8 engines + FastAPI) |
| **BUG-014** | ✅ RESOLVIDO (nested logic) |
| **Síndromes** | 35/35 funcionais (100%) ✅ |
| **Integration Tests** | 7/7 passing (100%) ✅ |
| **Test Infrastructure** | 323 tests parametrizados ✅ |
| **Coverage** | 44% ⚠️ (meta: 85%) |

### ⏳ **O QUE FALTA:**

**Para chegar a Coverage 85%:**
1. Fix parametrized test fixtures (~30 min)
2. Add tests for normalization.py (25%→80%)
3. Add tests for schema_validator.py (35%→80%)
4. Add tests for output_renderer.py (8%→80%)
5. Add tests for worm_log.py (42%→80%)
6. Add tests for main.py FastAPI (0%→60%)

---

## 🎯 PLANO DE AÇÃO (4 Tarefas Priorizadas)

### **TAREFA 1: Fix Parametrized Test Fixtures** ⚡ P0
**Tempo:** ~30 min
**Arquivos:** `tests/unit/test_all_evidences.py`, `test_all_syndromes.py`

**Problema Atual:**
```python
# ERRADO (linha 38 test_all_evidences.py):
@pytest.fixture(scope="module")
def config(yaml_parser):
    return yaml_parser.get_config()  # ❌ Método não existe
```

**Solução:**
```python
# CORRETO:
@pytest.fixture(scope="module")
def config(yaml_parser):
    """Get config from YAML files loaded by yaml_parser."""
    # Config está embutido no yaml_parser
    # Retornar um dict básico para os testes
    return {
        "cutoffs": yaml_parser._config_data.get("cutoffs", {}),
        # ... outros campos necessários
    }
```

**OU** (mais simples):
```python
# Remover fixture config e usar yaml_parser diretamente nos testes
# Evidence engine já recebe yaml_parser, não config
```

**Comandos:**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# Testar evidences
PYTHONPATH=src python3 -m pytest tests/unit/test_all_evidences.py -v

# Testar syndromes
PYTHONPATH=src python3 -m pytest tests/unit/test_all_syndromes.py -v
```

**Critério de Sucesso:** 79+ tests passing em test_all_evidences.py

---

### **TAREFA 2: Add Tests for normalization.py** 🔥 P1
**Tempo:** ~1h
**Cobertura Atual:** 25% → Meta: 80%
**Arquivo:** `tests/unit/test_normalization.py` (criar)

**Funções Não Testadas (src/hemodoctor/engines/normalization.py):**
- `normalize_cbc()` - linhas 78-186 (PRINCIPAL)
- `detect_unit_conversion_needed()` - linhas 220-255
- `apply_unit_conversions()` - linhas 283-313
- `compute_absolute_counts()` - linhas 344-377

**Template de Teste:**
```python
"""
Normalization Engine Tests

Tests unit conversion heuristics and validation.
"""

import pytest
from hemodoctor.engines.normalization import normalize_cbc, apply_unit_conversions


def test_normalize_wbc_per_1000_conversion():
    """Test WBC /1000 conversion when WBC >200."""
    cbc_input = {
        "wbc": 7500,  # Should be 7.5
        "age_years": 35,
        "sex": "M"
    }

    result = normalize_cbc(cbc_input)

    assert result["normalized"]["wbc"] == 7.5
    assert "wbc" in result["conversion_log"]
    assert result["conversion_log"]["wbc"]["from"] == 7500
    assert result["conversion_log"]["wbc"]["to"] == 7.5


def test_normalize_plt_per_1000_conversion():
    """Test PLT /1000 conversion when PLT >2000."""
    cbc_input = {
        "plt": 250000,  # Should be 250
        "age_years": 35,
        "sex": "M"
    }

    result = normalize_cbc(cbc_input)

    assert result["normalized"]["plt"] == 250
    assert "plt" in result["conversion_log"]


def test_normalize_hb_per_10_conversion():
    """Test Hb /10 conversion when Hb >25."""
    cbc_input = {
        "hb": 145,  # Should be 14.5
        "age_years": 35,
        "sex": "M"
    }

    result = normalize_cbc(cbc_input)

    assert result["normalized"]["hb"] == 14.5


def test_normalize_no_conversion_needed():
    """Test that normal values are not converted."""
    cbc_input = {
        "wbc": 7.5,
        "plt": 250,
        "hb": 14.5,
        "age_years": 35,
        "sex": "M"
    }

    result = normalize_cbc(cbc_input)

    # Should be unchanged
    assert result["normalized"]["wbc"] == 7.5
    assert result["normalized"]["plt"] == 250
    assert result["normalized"]["hb"] == 14.5
    assert len(result["conversion_log"]) == 0  # No conversions


def test_compute_absolute_counts():
    """Test computation of absolute counts from percentages."""
    # TODO: Add test for computing anc, alc, etc.
    pass
```

**Comandos:**
```bash
# Criar e testar
touch tests/unit/test_normalization.py
# Adicionar testes acima
PYTHONPATH=src python3 -m pytest tests/unit/test_normalization.py -v --cov=src/hemodoctor/engines/normalization
```

**Critério de Sucesso:** normalization.py coverage 25% → 80%

---

### **TAREFA 3: Add Tests for schema_validator.py** 🔥 P1
**Tempo:** ~1h
**Cobertura Atual:** 35% → Meta: 80%
**Arquivo:** `tests/unit/test_schema_validator.py` (criar)

**Funções Não Testadas:**
- `validate_cbc()` - linhas 84-185
- `check_field_types()` - linhas 209-216
- `check_physiological_ranges()` - linhas 240-308

**Template:**
```python
"""Schema Validator Tests"""

import pytest
from hemodoctor.engines.schema_validator import validate_cbc


def test_validate_cbc_valid_input():
    """Test validation with valid CBC."""
    cbc = {
        "hb": 14.5,
        "wbc": 7.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M"
    }

    result = validate_cbc(cbc)

    assert result["valid"] == True
    assert len(result["warnings"]) == 0


def test_validate_cbc_out_of_range_warning():
    """Test warnings for out-of-range values."""
    cbc = {
        "hb": 50,  # Impossibly high
        "wbc": 7.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M"
    }

    result = validate_cbc(cbc)

    # Should have warnings but still be valid (fail-safe)
    assert result["valid"] == True
    assert len(result["warnings"]) > 0
    assert any("hb" in w for w in result["warnings"])


def test_validate_cbc_wrong_type():
    """Test type checking."""
    cbc = {
        "hb": "fourteen",  # Wrong type (should be float)
        "wbc": 7.5,
        "age_years": 35,
        "sex": "M"
    }

    result = validate_cbc(cbc)

    assert len(result["warnings"]) > 0
```

**Comandos:**
```bash
PYTHONPATH=src python3 -m pytest tests/unit/test_schema_validator.py -v --cov=src/hemodoctor/engines/schema_validator
```

**Critério de Sucesso:** schema_validator.py coverage 35% → 80%

---

### **TAREFA 4: Add Tests for output_renderer.py & worm_log.py** 🔥 P2
**Tempo:** ~1.5h
**Arquivos:** `test_output_renderer.py`, `test_worm_log.py`

**Output Renderer (8% → 60%):**
```python
def test_render_markdown():
    """Test markdown output rendering."""
    pass

def test_render_html():
    """Test HTML output rendering."""
    pass

def test_render_json():
    """Test JSON output rendering."""
    pass
```

**WORM Log (42% → 60%):**
```python
def test_worm_log_append():
    """Test appending to WORM log."""
    pass

def test_worm_log_hmac_signature():
    """Test HMAC signature generation."""
    pass

def test_worm_log_rotation():
    """Test daily rotation logic."""
    pass
```

---

## 🎯 QUICK START (Para Nova Sessão)

### **Opção A: Começar do Zero (Recomendado)**

```bash
# 1. Navegar para o projeto
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# 2. Ler contexto
cat /Users/abelcosta/Documents/HemoDoctor/docs/CLAUDE.md
cat /Users/abelcosta/Documents/HemoDoctor/docs/PROXIMOS_PASSOS_SPRINT_0.md

# 3. Ver status atual
git log --oneline -5
git status

# 4. Rodar testes existentes
PYTHONPATH=src python3 -m pytest tests/integration/test_critical_fixes.py -v

# 5. Ver coverage atual
PYTHONPATH=src python3 -m pytest tests/ -v --cov=src/hemodoctor --cov-report=term-missing

# 6. Começar TAREFA 1 (fix fixtures)
```

### **Opção B: Continuar de Onde Parou**

Se preferir continuar direto:
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# Fix fixtures imediatamente
# Editar: tests/unit/test_all_evidences.py linha 34-38
# Remover fixture 'config' e usar yaml_parser diretamente
```

---

## 📊 MÉTRICAS DE SUCESSO

**Quando Sprint 0 estiver 100% completo:**
- [ ] Coverage ≥ 85%
- [ ] Pass rate ≥ 90% (tests passing)
- [ ] 0 failing tests
- [ ] All engines tested
- [ ] FastAPI endpoints tested

**Comandos de Validação Final:**
```bash
# Coverage check
PYTHONPATH=src python3 -m pytest tests/ --cov=src/hemodoctor --cov-report=html

# Ver relatório
open htmlcov/index.html

# Pass rate
PYTHONPATH=src python3 -m pytest tests/ -v --tb=short
```

---

## 🔗 REFERÊNCIAS ÚTEIS

**Arquivos Importantes:**
```
/Users/abelcosta/Documents/HemoDoctor/docs/
├── CLAUDE.md                           # Contexto completo
├── PROXIMOS_PASSOS_SPRINT_0.md        # Este arquivo
├── BUGS.md                            # Bugs (5 open, 6 closed)
├── PROGRESS.md                         # Histórico
└── hemodoctor_cdss/
    ├── src/hemodoctor/engines/        # Código fonte
    ├── tests/
    │   ├── unit/                      # Unit tests
    │   └── integration/               # Integration tests
    └── pytest.ini                     # Config pytest
```

**Commits Relevantes:**
- `7315b8d` - Test suite created (último commit)
- `69b7253` - BUG-014 resolved
- `e930758` - Critical fixes validation

**Comandos Git:**
```bash
# Ver histórico
git log --oneline --graph -10

# Ver mudanças
git show 7315b8d

# Ver arquivos modificados
git diff --stat HEAD~3
```

---

## 💡 DICAS

1. **Comece pela TAREFA 1** (fix fixtures) - desbloq

ueia 79 tests
2. **Teste incrementalmente** - rode pytest após cada fix
3. **Use coverage report** - `--cov-report=html` para visualizar
4. **Mantenha commits pequenos** - 1 commit por tarefa
5. **Atualize CLAUDE.md** ao final - documente o progresso

---

## ⚡ ESTIMATIVAS

| Tarefa | Tempo | Coverage Ganho |
|--------|-------|----------------|
| 1. Fix fixtures | 30 min | +20% (79 tests passing) |
| 2. Normalization tests | 1h | +10% (25%→80% no módulo) |
| 3. Schema validator tests | 1h | +8% (35%→80% no módulo) |
| 4. Output/WORM tests | 1.5h | +7% |
| **TOTAL** | **4h** | **44% → 85%** ✅ |

---

**🎯 Objetivo:** Sprint 0 100% completo até 26 Out (sexta-feira)
**🚀 Timeline:** 30 Nov 2025 mantida
**✨ Boa sorte!**
