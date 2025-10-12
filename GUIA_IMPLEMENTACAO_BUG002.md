# 🔧 Guia de Implementação - Bug #2 (Age Boundaries)

**Data:** 13 de Outubro de 2025  
**Tempo Estimado:** 30 minutos  
**Impacto:** +12 testes (68% → 81% pass rate)

---

## 📍 LOCALIZAÇÃO

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex
```

**Arquivo:** `platelet_severity_classifier.py` (ou similar)  
**Função:** `get_age_group(age_months: float)`  
**Linhas:** ~110-150

---

## 🔧 MUDANÇA NECESSÁRIA

### ANTES (Semi-Open [a, b))

```python
def get_age_group(age_months: float):
    if age_months < 1:
        return PED_01_NEONATAL
    elif age_months < 6:  # [1, 6)
        return PED_02_INFANT_EARLY
    elif age_months < 24:  # [6, 24)
        return PED_03_INFANT_LATE
    elif age_months < 72:  # [24, 72)
        return PED_04_PRESCHOOL
    elif age_months < 144:  # [72, 144)
        return PED_05_SCHOOL
    elif age_months < 216:  # [144, 216)
        return PED_06_ADOLESCENT
    else:
        raise ValueError("Age out of pediatric range")
```

### DEPOIS (Inclusive [a, b])

```python
def get_age_group(age_months: float):
    """
    Classify age into pediatric group using INCLUSIVE upper bounds.
    
    Clinical rationale:
    - A child at exactly 2.0 years (24 months) is still in Infant Late group
    - A teenager at exactly 18.0 years (216 months) is still in Adolescent group
    
    Age Groups (IEC 62304 Class C validation):
    - PED-01: [0, 1] months (0-30 days)
    - PED-02: (1, 6] months (31-182 days)
    - PED-03: (6, 24] months (183 days - 2 years)
    - PED-04: (24, 72] months (2-6 years)
    - PED-05: (72, 144] months (6-12 years)
    - PED-06: (144, 216] months (12-18 years)
    
    Args:
        age_months: Patient age in months (float for fractional months)
        
    Returns:
        AgeGroup dataclass with reference ranges
        
    Raises:
        ValueError: If age > 216 months (>18 years, adult range)
    """
    if age_months <= 1:  # Changed: < to <=
        return PED_01_NEONATAL
    elif age_months <= 6:  # Changed: < to <=
        return PED_02_INFANT_EARLY
    elif age_months <= 24:  # Changed: < to <=
        return PED_03_INFANT_LATE
    elif age_months <= 72:  # Changed: < to <=
        return PED_04_PRESCHOOL
    elif age_months <= 144:  # Changed: < to <=
        return PED_05_SCHOOL
    elif age_months <= 216:  # Changed: < to <=
        return PED_06_ADOLESCENT
    else:
        raise ValueError(
            f"Age {age_months} months (>{age_months/12:.1f} years) exceeds "
            "pediatric range (0-18 years). Use adult reference ranges."
        )
```

---

## ✅ MUDANÇAS ESPECÍFICAS

**Trocar 6 linhas:**
1. Linha ~115: `if age_months < 1:` → `if age_months <= 1:`
2. Linha ~117: `elif age_months < 6:` → `elif age_months <= 6:`
3. Linha ~119: `elif age_months < 24:` → `elif age_months <= 24:`
4. Linha ~121: `elif age_months < 72:` → `elif age_months <= 72:`
5. Linha ~123: `elif age_months < 144:` → `elif age_months <= 144:`
6. Linha ~125: `elif age_months < 216:` → `elif age_months <= 216:`

**Adicionar docstring** completa

**Melhorar ValueError** message

---

## 🧪 TESTES

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/TESTES/test_automation

# Ativar venv se necessário
source venv/bin/activate

# Executar todos os testes
pytest test_pediatric_platelet.py -v

# Executar apenas testes de boundary
pytest test_pediatric_platelet.py -v -k "boundary or edge"

# Ver coverage
pytest --cov --cov-report=html
```

---

## 📊 VALIDAÇÃO

### Testes que Devem Passar Agora

1. **TC-PED-01-07** (age=30d = 1.0m) → PED-01
2. **TC-PED-03-04** (age=24m = 2y) → PED-03
3. **TC-PED-03-05** (age=24m) → PED-03
4. **TC-PED-03-08** (age=24m) → PED-03
5. **TC-PED-04-12** (age=6y = 72m) → PED-04
6. **TC-PED-05-12** (age=12y = 144m) → PED-05
7. **TC-PED-06-12** (age=18y = 216m) → PED-06 (NO CRASH!)
8-14. **TC-EDGE-01 to TC-EDGE-06** → Todos os edge cases

**Total:** +12 testes passando

---

## 📈 IMPACTO ESPERADO

### Pass Rate

| Situação | Tests Passed | Pass Rate |
|----------|--------------|-----------|
| **Antes** | 65/95 | 68% |
| **Após Bug #2** | 77/95 | 81% |
| **Meta** | 86/95 | 90% |
| **Gap Restante** | 9 tests | (test structure issues) |

---

## 📝 DOCUMENTAÇÃO

Após implementação, atualizar:

1. **BUG-001:** Marcar Bug #2 como RESOLVED
2. **SRS-001:** Atualizar seção age classification
3. **TRC-001:** Atualizar rastreabilidade
4. **CHANGELOG:** Adicionar design change

---

## ⚡ COMANDO RÁPIDO

```bash
# 1. Navegar
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex

# 2. Editar arquivo
# (usar editor de código)

# 3. Testar
cd ../../TESTES/test_automation
pytest -v

# 4. Commit
git add .
git commit -m "🐛 Fix Bug #2: Inclusive age boundaries

- Changed semi-open [a,b) to inclusive [a,b]
- Fixes 12 test failures (age 1m, 2y, 18y crashes)
- Pass rate: 68% → 81%
- Clinical rationale: 2 years = still Infant Late

IEC 62304 Class C: Design change documented
Traceability: BUG-001 → SRS-001 → TRC-001"
```

---

**Status:** ✅ GUIA COMPLETO  
**Tempo:** 30 minutos implementação  
**Impacto:** +12 testes, 68% → 81%

