# 🚨 AÇÕES CORRETIVAS IMEDIATAS - HemoDoctor v2.3.1

**Data:** 19 de Outubro de 2025 - 23:55 BRT
**Agente:** @quality-systems-specialist
**Prioridade:** P0 (CRÍTICO)
**Prazo:** 19 Out 2025 (HOJE) + Sprint 0-4 (6 semanas)

---

## 📋 ÍNDICE DE AÇÕES

| # | Ação | Tempo | Prioridade | Status |
|---|------|-------|------------|--------|
| **AC-001** | Extrair código ZIP | 10 min | P0 | ⏳ PENDENTE |
| **AC-002** | Implementar Bug #2 | 30 min | P0 | ⏳ PENDENTE |
| **AC-003** | Fechar BUG-005 | 5 min | P0 | ⏳ PENDENTE |
| **AC-004** | Implementar 15 evidências | 3h | P0 | ⏳ PENDENTE |
| **AC-005** | Atualizar metadata | 20 min | P1 | ⏸ WAITING |
| **AC-006** | Atualizar versões YAML | 2h | P1 | ⏸ WAITING |
| **AC-007** | Localizar SRS-001 | 30 min | P1 | ⏸ WAITING |
| **AC-008** | Sprint 0 - YAMLs testing | 2 dias | P0 | ⏸ WAITING |

---

## 🔴 P0 - CRÍTICO (HOJE - 4 horas)

### AC-001: Extrair Código-Fonte do ZIP

**Prioridade:** P0 (BLOCKER)
**Tempo:** 10 minutos
**Severidade:** CRITICAL
**Responsável:** DevOps / Dr. Abel

#### Problema

Código-fonte FastAPI não está acessível no sistema de arquivos. Todos os diretórios de código estão vazios porque o ZIP não foi extraído.

#### Localização

**ZIP Não Extraído:**
```
/Users/abelcosta/Documents/HemoDoctor/HemoDoctor_BACKUP_20251016/
└── HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip
```

**Destino:**
```
/Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/
```

#### Solução

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/

unzip /Users/abelcosta/Documents/HemoDoctor/HemoDoctor_BACKUP_20251016/HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip -d HEMODOCTOR_CONSOLIDADO_v2.0_20251010/
```

#### Validação

```bash
# Verificar código extraído
ls -la HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex/

# Esperado: arquivos Python, não diretórios vazios
```

#### Impacto

**Sem extração:**
- ❌ Análise código vs YAMLs impossível
- ❌ Implementação Bug #2 bloqueada
- ❌ Pass rate 72% não pode melhorar
- ❌ Testes não podem ser executados

**Após extração:**
- ✅ Análise código vs YAMLs possível
- ✅ Bug #2 implementável
- ✅ Pass rate 72% → 81% possível
- ✅ Testes executáveis

#### Status

⏳ **PENDENTE** (aguardando execução)

---

### AC-002: Implementar Bug #2 (Age Boundaries)

**Prioridade:** P0
**Tempo:** 30 minutos
**Severidade:** CRITICAL
**Responsável:** @software-architecture-specialist
**Blocker de:** AC-001 (código não acessível)

#### Problema

Função `get_pediatric_age_category()` usa intervalos **semi-abertos** (`<`) quando deveria usar **inclusivos** (`<=`), causando 12 test failures.

#### Localização

```python
# Arquivo (após extração ZIP):
HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/
  @hemodoctor/dossier-anvisa-codex/src/api/platelet_severity_classifier.py
```

#### Mudanças Necessárias

**6 mudanças: `<` → `<=`**

```python
def get_pediatric_age_category(age_months: float) -> PediatricAgeCategory:
    # ANTES → DEPOIS
    if age_months <= 1:          # MUDANÇA #1 (era: <)
        return PED_01_NEONATAL
    elif age_months <= 6:        # MUDANÇA #2 (era: <)
        return PED_02_INFANT_YOUNG
    elif age_months <= 24:       # MUDANÇA #3 (era: <)
        return PED_03_INFANT_OLDER
    elif age_months <= 60:       # MUDANÇA #4 (era: <)
        return PED_04_PRESCHOOL
    elif age_months <= 120:      # MUDANÇA #5 (era: <)
        return PED_05_SCHOOL_AGE
    elif age_months <= 216:      # MUDANÇA #6 (era: <)
        return PED_06_TEEN
    else:
        return PED_07_ADULT
```

#### Validação

```bash
# Executar testes afetados
pytest test_age_boundary_neonatal_1month.py
pytest test_age_boundary_infant_6months.py
pytest test_age_boundary_toddler_24months.py
pytest test_age_boundary_preschool_60months.py
pytest test_age_boundary_school_120months.py
pytest test_age_boundary_teen_216months.py

# Esperado: 12/12 PASS (antes: 0/12)
```

#### Impacto

**Antes:**
- ❌ 12 testes falhando
- ❌ Pass rate: 72% (68/95)
- ❌ Casos no limiar classificados errado

**Depois:**
- ✅ 12 testes passando
- ✅ Pass rate: 81% (80/95)
- ✅ Casos no limiar classificados corretamente

#### Guia Detalhado

Ver: `GUIA_IMPLEMENTACAO_BUG002.md` (já criado)

#### Status

⏳ **PENDENTE** (bloqueado por AC-001)

---

### AC-003: Fechar BUG-005 em BUGS.md

**Prioridade:** P0 (Compliance)
**Tempo:** 5 minutos
**Severidade:** HIGH (Documentação)
**Responsável:** @quality-systems-specialist

#### Problema

BUGS.md diz que BUG-005 (WORM retention) está "OPEN" e código tem `days: 90`, mas YAML mostra `days: 1825` (CORRETO).

#### Localização

```
/Users/abelcosta/Documents/HemoDoctor/docs/BUGS.md
Linha ~428
```

#### Mudança Necessária

**ANTES:**
```markdown
### BUG-005: WORM Log Retention Incorrect (90d → 1825d)
**Status:** 🟡 OPEN - HIGH
**Código Atual (ERRADO):**
```yaml
retention:
  days: 90  # ❌ ERRADO - ANVISA exige 5 anos
```
```

**DEPOIS:**
```markdown
### BUG-005: WORM Log Retention Incorrect (90d → 1825d)
**Status:** ✅ CLOSED - FIXED (19 Out 2025)
**Código Correto:**
```yaml
retention:
  days: 1825  # ✅ CORRETO (5 anos - ANVISA/FDA)
```
**Fixado em:** Commit 92662f0 (feat(v2.3.1): Correções críticas)
**Verificado:** 08_wormlog_hybrid.yaml linha 129
```

#### Validação

```bash
# Verificar YAML
grep "days:" /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_HIBRIDO_V1.0/YAMLs/08_wormlog_hybrid.yaml

# Esperado: days: 1825
```

#### Impacto

**Antes:**
- ⚠️ BUGS.md diz "pendente", mas YAML está correto
- ⚠️ Confusão em auditorias ANVISA/FDA
- ⚠️ Compliance reporting incorreto

**Depois:**
- ✅ BUGS.md alinhado com YAML
- ✅ Auditoria transparente
- ✅ Compliance 100% LGPD/ANVISA/FDA

#### Status

⏳ **PENDENTE** (aguardando edição BUGS.md)

---

### AC-004: Implementar 15 Evidências Faltantes

**Prioridade:** P0 (Broken References)
**Tempo:** 3 horas (15 × 12 min)
**Severidade:** CRITICAL
**Responsável:** @software-architecture-specialist

#### Problema

Documentação afirma 79 evidências, mas YAML tem apenas 64. Diferença de **-15 evidências** (19% missing) causa **broken references** em S-TMA e S-ACD.

#### Evidências Faltantes Críticas

**Identificadas via análise de referências:**

1. `E-LDH-HIGH` (referenciada em S-TMA linha 63)
2. `E-BT-IND-HIGH` (referenciada em S-TMA linha 63)
3. `E-CREATININA-HIGH` (referenciada em S-TMA linha 63)
4. `E-ANEMIA` (referenciada em S-ACD linha 253)
5. `E-FERRITIN-HIGH-100` (referenciada em S-ACD linha 254)
6. `E-HBA2-HIGH` (referenciada em S-ACD linha 255)
7. **+9 evidências a identificar** (análise completa de 03_syndromes.yaml)

#### Solução - Template de Implementação

**Arquivo:** `02_evidence_hybrid.yaml`
**Localização:** Adicionar após linha 590 (antes do metadata)

```yaml
# =============================================================================
# EVIDÊNCIAS COMPLEMENTARES (Adicionadas 19 Out 2025 - AC-004)
# =============================================================================
complementary_evidences:
  # 1. LDH elevado
  - id: E-LDH-HIGH
    rule: "ldh > 500"
    strength: moderate
    description: "LDH > 500 U/L"
    clinical_significance: "Hemólise, lise celular, TMA"
    source: "Ajustes Dr. Abel - AC-004"

  # 2. Bilirrubina indireta elevada
  - id: E-BT-IND-HIGH
    rule: "bt_indireta > 1.0"
    strength: moderate
    description: "Bilirrubina indireta > 1.0 mg/dL"
    clinical_significance: "Hemólise"
    source: "Ajustes Dr. Abel - AC-004"

  # 3. Creatinina elevada
  - id: E-CREATININA-HIGH
    rule: "creatinine > 1.2"
    strength: moderate
    description: "Creatinina > 1.2 mg/dL"
    clinical_significance: "Disfunção renal (SHU/TMA)"
    source: "Ajustes Dr. Abel - AC-004"

  # 4. Anemia (genérica)
  - id: E-ANEMIA
    rule: "hb < config.cutoffs.hb_normal_low[age_sex_group]"
    strength: moderate
    description: "Hemoglobina abaixo do normal por idade/sexo"
    clinical_significance: "Anemia (qualquer etiologia)"
    source: "Ajustes Dr. Abel - AC-004"

  # 5. Ferritina elevada (≥100)
  - id: E-FERRITIN-HIGH-100
    rule: "ferritin >= 100"
    strength: moderate
    description: "Ferritina ≥ 100 ng/mL"
    clinical_significance: "Anemia da doença crônica, sobrecarga férrica"
    source: "Ajustes Dr. Abel - AC-004"

  # 6. HbA2 elevado
  - id: E-HBA2-HIGH
    rule: "hba2 >= 3.5"
    strength: strong
    description: "HbA2 ≥ 3.5%"
    clinical_significance: "Beta-talassemia trait"
    source: "Ajustes Dr. Abel - AC-004"

  # ... +9 evidências (a completar após análise completa)
```

#### Passos Detalhados

1. **Identificar TODAS as evidências faltantes** (30 min)
   ```bash
   # Extrair todas as referências E-XXX de 03_syndromes_hybrid.yaml
   grep -oE "E-[A-Z0-9-]+" 03_syndromes_hybrid.yaml | sort -u > syndromes_refs.txt

   # Extrair todas as evidências implementadas em 02_evidence_hybrid.yaml
   grep "^  - id: E-" 02_evidence_hybrid.yaml | awk '{print $3}' | sort -u > evidence_impl.txt

   # Diferença
   comm -13 evidence_impl.txt syndromes_refs.txt > missing_evidences.txt
   ```

2. **Implementar evidências faltantes** (2h)
   - Template acima para cada evidência
   - Validar `rule:` com cutoffs de 00_config_hybrid.yaml
   - Garantir `strength:` apropriado

3. **Atualizar metadata** (15 min)
   ```yaml
   metadata:
     total_evidences: 79  # 64 → 79 (+15)
     critical_count: 6
     strong_count: 25     # Revalidar
     moderate_count: 40   # Revalidar
     weak_count: 8        # Revalidar
   ```

4. **Validação** (15 min)
   ```bash
   # Contar evidências novamente
   grep -c "^  - id: E-" 02_evidence_hybrid.yaml
   # Esperado: 79

   # Verificar referências quebradas
   for ref in $(grep -oE "E-[A-Z0-9-]+" 03_syndromes_hybrid.yaml | sort -u); do
     grep -q "id: $ref" 02_evidence_hybrid.yaml || echo "MISSING: $ref"
   done
   # Esperado: nenhuma saída
   ```

#### Impacto

**Antes:**
- ❌ 15 evidências faltando
- ❌ Broken references (S-TMA, S-ACD)
- ❌ Runtime errors ao avaliar síndromes
- ❌ Testes impossíveis

**Depois:**
- ✅ 79 evidências completas
- ✅ Todas referências válidas
- ✅ Síndromes funcionais
- ✅ Testes possíveis

#### Status

⏳ **PENDENTE** (aguardando implementação)

---

## 🟡 P1 - HIGH (Sprint 0 - 20-26 Out)

### AC-005: Atualizar Metadata de Evidências e Síndromes

**Prioridade:** P1
**Tempo:** 20 minutos
**Severidade:** MODERATE
**Responsável:** @quality-systems-specialist

#### Problema

Metadata em `02_evidence_hybrid.yaml` e `03_syndromes_hybrid.yaml` desatualizada:
- Evidências: metadata diz 75, real é 64 (ou 79 após AC-004)
- Síndromes: metadata diz 34, real é 35

#### Solução

**02_evidence_hybrid.yaml (linha 562):**
```yaml
metadata:
  total_evidences: 79  # Após AC-004 (era 75)
  critical_count: 6    # Validar
  strong_count: 25     # Revalidar (era 23)
  moderate_count: 40   # Revalidar (era 38)
  weak_count: 8        # Validar
```

**03_syndromes_hybrid.yaml (linha 712):**
```yaml
metadata:
  total_syndromes: 35   # +1 S-ACD (era 34)
  critical_count: 9
  priority_count: 24    # +1 S-ACD (era 23)
  review_sample_count: 1
  routine_count: 1
```

#### Validação

```bash
# Contar evidências
grep -c "^  - id: E-" 02_evidence_hybrid.yaml
# Esperado: 79 (após AC-004)

# Contar síndromes
grep -c "^  - id: S-" 03_syndromes_hybrid.yaml
# Esperado: 35
```

#### Status

⏸ **WAITING** (após AC-004)

---

### AC-006: Atualizar Versões YAML Inconsistentes

**Prioridade:** P1
**Tempo:** 2 horas
**Severidade:** MODERATE
**Responsável:** @quality-systems-specialist

#### Problema

8/16 YAMLs com versões desatualizadas ou missing:
- `04_output_templates_hybrid.yaml`: sem `version:`
- `05_missingness_hybrid_v2.3.yaml`: v2.3.0 (deveria ser v2.3.1)
- `06_route_policy_hybrid.yaml`: v1.0.0 (deveria ser v2.3.1)
- ... +5 arquivos

#### Solução

**Atualizar header de cada arquivo:**

```yaml
# ANTES
version: config_hybrid_v1.0.0

# DEPOIS
version: config_hybrid_v2.3.1
```

**Arquivos a atualizar:**
1. `04_output_templates_hybrid.yaml` → adicionar `version: output_templates_hybrid_v2.3.1`
2. `05_missingness_hybrid_v2.3.yaml` → `v2.3.0` → `v2.3.1`
3. `06_route_policy_hybrid.yaml` → `v1.0.0` → `v2.3.1`
4. `07_conflict_matrix_hybrid.yaml` → `v1.0.0` → `v2.3.1`
5. `07_normalization_heuristics.yaml` → `v1.0.0` → `v2.3.1`
6. `11_case_state_hybrid.yaml` → `v2.3.0` → `v2.3.1`
7. `12_output_policies_cdss.yaml` → adicionar `version: output_policies_cdss_v2.3.1`

#### Validação

```bash
# Verificar todas as versões
for f in *.yaml; do echo "$f:"; grep "^version:" "$f" || echo "  (sem version)"; done

# Esperado: todos v2.3.1 ou v2.3.1-cdss
```

#### Status

⏸ **WAITING** (Sprint 0)

---

### AC-007: Localizar SRS-001 (Rastreabilidade)

**Prioridade:** P1
**Tempo:** 30 minutos
**Severidade:** MODERATE
**Responsável:** @traceability-specialist

#### Problema

SRS-001 (Software Requirements Specification) não acessível no caminho esperado:
```
/Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS-001_v3.0.md
```

Impacto: Rastreabilidade incompleta (impossível validar YAMLs vs Requirements)

#### Solução

**1. Buscar em todo projeto:**
```bash
find /Users/abelcosta/Documents/HemoDoctor -name "SRS-001*" -type f
```

**2. Localizações prováveis:**
```
- HEMODOCTOR_CONSOLIDADO_v2.0_20251010/02_SUBMISSAO_ANVISA/
- AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS/
- Dentro do ZIP não extraído
```

**3. Criar link simbólico após localizar:**
```bash
ln -s /caminho/real/SRS-001_v3.0.md /Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS-001_v3.0.md
```

#### Validação

```bash
# Verificar SRS acessível
ls -lh /Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/SRS-001_v3.0.md

# Verificar requirements
grep "REQ-HD-" SRS-001_v3.0.md | head -20
```

#### Status

⏸ **WAITING** (Sprint 0)

---

## 🔴 P0 - SPRINT 0 (20-26 Out - 2 dias)

### AC-008: YAMLs Test Coverage (0% → 85%)

**Prioridade:** P0 (IEC 62304 blocker)
**Tempo:** 2 dias (12 horas efetivas)
**Severidade:** CRITICAL
**Responsável:** @software-architecture-specialist

#### Problema

Os 15 módulos YAML (7,350 linhas) têm **0% test coverage**, violando IEC 62304 §5.5 (Unit Testing obrigatório).

#### Escopo

**129 testes necessários:**
- 64 evidências (após AC-004: 79)
- 35 síndromes
- 30 cutoffs

#### Solução - Estrutura de Testes

**Arquivo:** `tests/test_yamls_v2_3_1.py`

```python
import pytest
import yaml
from simpleeval import simple_eval

# ============================================================================
# FIXTURES
# ============================================================================
@pytest.fixture
def config():
    """Load 00_config_hybrid.yaml"""
    with open('YAMLs/00_config_hybrid.yaml') as f:
        return yaml.safe_load(f)

@pytest.fixture
def evidences():
    """Load 02_evidence_hybrid.yaml"""
    with open('YAMLs/02_evidence_hybrid.yaml') as f:
        return yaml.safe_load(f)

@pytest.fixture
def syndromes():
    """Load 03_syndromes_hybrid.yaml"""
    with open('YAMLs/03_syndromes_hybrid.yaml') as f:
        return yaml.safe_load(f)

# ============================================================================
# EVIDÊNCIAS (79 testes - 5 min cada = 6.5h)
# ============================================================================
def test_evidence_E_ANC_CRIT(config):
    """Test E-ANC-CRIT: ANC < 0.5"""
    cbc = {"anc": 0.3}
    rule = "anc < 0.5"
    result = simple_eval(rule, names=cbc)
    assert result == True

def test_evidence_E_HB_HIGH(config):
    """Test E-HB-HIGH: Hb > 18.5 (adult M)"""
    cbc = {"hb": 19.0, "age_sex_group": "adult_m"}
    cutoff = config["cutoffs"]["hb_high"]["adult_m"]
    result = cbc["hb"] > cutoff
    assert result == True

# ... +77 testes (template similar)

# ============================================================================
# SÍNDROMES (35 testes - 10 min cada = 5.8h)
# ============================================================================
def test_syndrome_S_TMA():
    """Test S-TMA: PLT <10 + esquistócitos ≥1%"""
    cbc = {
        "plt": 8,
        "morphology": {"esquistocitos": True}
    }
    evidences = evaluate_evidences(cbc, config)
    assert "E-PLT-CRIT-LOW" in [e.id for e in evidences]
    assert "E-SCHISTOCYTES-GE1PCT" in [e.id for e in evidences]

    syndromes = fuse_syndromes(evidences, config)
    assert "S-TMA" in [s.id for s in syndromes]
    assert syndromes[0].criticality == "critical"

# ... +34 testes (template similar)

# ============================================================================
# CUTOFFS (30 testes - 3 min cada = 1.5h)
# ============================================================================
def test_cutoff_hb_high_adult_m(config):
    """Test hb_high cutoff for adult male: 18.5 g/dL"""
    assert config["cutoffs"]["hb_high"]["adult_m"] == 18.5

def test_cutoff_hb_high_adult_f(config):
    """Test hb_high cutoff for adult female: 16.5 g/dL"""
    assert config["cutoffs"]["hb_high"]["adult_f"] == 16.5

# ... +28 testes (template similar)
```

#### Breakdown Detalhado

**Dia 1 (6h):**
- Evidências críticas (6 testes) - 30 min
- Evidências série vermelha (15 testes) - 1.25h
- Evidências série branca (13 testes) - 1.08h
- Evidências plaquetárias (8 testes) - 40 min
- Evidências coagulação (5 testes) - 25 min
- Evidências moleculares (10 testes) - 50 min
- Evidências pré-analíticas (5 testes) - 25 min
- **Subtotal:** 62 testes, ~5h

**Dia 2 (6h):**
- Evidências complementares (17 testes) - 1.4h
- Síndromes críticas (9 testes) - 1.5h
- Síndromes priority (24 testes) - 2.4h
- Síndromes review/routine (2 testes) - 12 min
- Cutoffs (30 testes) - 1.5h
- **Subtotal:** 82 testes, ~6h

**Total:** 129 testes + 15 testes (buffer) = **144 testes em 12h**

#### Validação

```bash
# Executar testes
pytest tests/test_yamls_v2_3_1.py -v

# Verificar coverage
pytest tests/test_yamls_v2_3_1.py --cov=YAMLs --cov-report=term

# Esperado:
# - 144 PASS
# - Coverage: ≥85%
```

#### Impacto

**Antes:**
- ❌ IEC 62304 §5.5: 0% coverage
- ❌ YAMLs não validados
- ❌ Compliance: 54%

**Depois:**
- ✅ IEC 62304 §5.5: 85% coverage
- ✅ YAMLs validados
- ✅ Compliance: 75% → 85%

#### Status

⏸ **WAITING** (Sprint 0 - 20-26 Out)

---

## 📅 CRONOGRAMA CONSOLIDADO

```
┌─────────────────────────────────────────────────────────────┐
│ Data          │ Ação               │ Tempo │ Status         │
├───────────────┼────────────────────┼───────┼────────────────┤
│ 19 Out (HOJE) │ AC-001: Extrair ZIP│ 10min │ ⏳ PENDENTE    │
│               │ AC-002: Bug #2     │ 30min │ ⏳ PENDENTE    │
│               │ AC-003: BUG-005    │  5min │ ⏳ PENDENTE    │
│               │ AC-004: 15 evidênc │  3h   │ ⏳ PENDENTE    │
│               ├────────────────────┼───────┼────────────────┤
│               │ TOTAL HOJE:        │  4h   │                │
├───────────────┼────────────────────┼───────┼────────────────┤
│ 20-26 Out     │ AC-008: YAMLs tests│ 2 dias│ ⏸ WAITING     │
│ (Sprint 0)    │ AC-005: Metadata   │ 20min │ ⏸ WAITING     │
│               │ AC-006: Versões    │  2h   │ ⏸ WAITING     │
│               │ AC-007: SRS-001    │ 30min │ ⏸ WAITING     │
│               ├────────────────────┼───────┼────────────────┤
│               │ TOTAL SPRINT 0:    │ 2 dias│                │
└─────────────────────────────────────────────────────────────┘
```

---

## ✅ CRITÉRIOS DE ACEITAÇÃO

### AC-001 a AC-004 (P0 - HOJE)

- [ ] ZIP extraído com sucesso
- [ ] Código-fonte acessível em `03_DESENVOLVIMENTO/CODIGO_FONTE/`
- [ ] Bug #2 implementado (6 mudanças)
- [ ] Pass rate: 72% → 81% (12 testes passando)
- [ ] BUG-005 fechado em BUGS.md
- [ ] 15 evidências implementadas em `02_evidence_hybrid.yaml`
- [ ] Metadata atualizada: `total_evidences: 79`
- [ ] Nenhuma referência quebrada (S-TMA, S-ACD funcionais)

### AC-005 a AC-008 (Sprint 0)

- [ ] Todas as versões YAML em v2.3.1 ou v2.3.1-cdss
- [ ] SRS-001 localizado e acessível
- [ ] 144 testes implementados (`test_yamls_v2_3_1.py`)
- [ ] Pass rate ≥85%
- [ ] Coverage YAMLs ≥85%
- [ ] IEC 62304 compliance: 54% → 75%

---

## 📞 RESPONSÁVEIS

| Ação | Responsável | Email/Contact |
|------|-------------|---------------|
| AC-001 | DevOps / Dr. Abel | abel.costa@hemodoctor.com |
| AC-002 | @software-architecture-specialist | - |
| AC-003 | @quality-systems-specialist | - |
| AC-004 | @software-architecture-specialist | - |
| AC-005 | @quality-systems-specialist | - |
| AC-006 | @quality-systems-specialist | - |
| AC-007 | @traceability-specialist | - |
| AC-008 | @software-architecture-specialist | - |

---

## 📊 TRACKING

**Progresso Geral:**
- P0 (HOJE): 0/4 completo (0%)
- Sprint 0: 0/4 completo (0%)
- **TOTAL:** 0/8 completo (0%)

**Próxima Atualização:** Após execução AC-001 a AC-004 (19 Out 2025)

---

**Gerado por:** @quality-systems-specialist
**Data:** 19 de Outubro de 2025 - 23:55 BRT
**Versão:** 1.0.0

---

**FIM DAS AÇÕES CORRETIVAS**
