# 🚀 QUICKSTART - IMPLEMENTAÇÃO HEMODOCTOR HYBRID V1.0
# Guia Rápido para Dev Team
# Dr. Abel Costa (IDOR-SP) - Outubro 2025

---

## ⏱️ TEMPO ESTIMADO DE LEITURA: 15 minutos

**Objetivo:** Colocar dev team operacional em Sprint 0 (primeira semana).

---

## 📋 RESUMO EXECUTIVO

**O que é?** Sistema de apoio à decisão médica para análise de hemogramas (CBC), classificando casos em:
- 🔴 **CRÍTICO** (8 síndromes: TMA, neutropenia grave, blástica, etc.)
- 🟠 **PRIORIDADE** (23 síndromes: IDA, beta-talassemia, hemólise, etc.)
- 🔵 **ROTINA** (2: normal, borderline)
- ⚪ **REVER AMOSTRA** (erro pré-analítico)

**Como?** Via regras determinísticas em YAML (V0) + calibração probabilística (V1) + ML explicável (V2).

**Por que YAML?** Hematologistas podem revisar/validar regras diretamente. **Nenhum modelo opaco em V0.**

---

## 🎯 ANTES DE COMEÇAR

### **1. Leia PRIMEIRO (30 min):**
1. ✅ `README.md` (5 min) — visão geral
2. ✅ `10_runbook_hybrid.yaml` (10 min) — roadmap V0→V1→V2
3. ✅ `DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md` (15 min) — exemplo técnico com código

### **2. Setup inicial (1h):**
```bash
# Clone do repo (se ainda não tiver)
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_HIBRIDO_V1.0

# Crie ambiente Python
python3 -m venv venv
source venv/bin/activate

# Instale dependências
pip install pyyaml jsonschema pytest simpleeval python-dateutil hashlib

# Valide YAMLs
python -c "import yaml; yaml.safe_load(open('YAMLs/00_config_hybrid.yaml'))"
```

### **3. Arquitetura rápida:**
```
Entrada (CBC + Morfologia) 
  ↓
[A] Ingestão & Normalização (00_config, 01_schema)
  ↓
[B] Evidências por série (02_evidence) → 75 rules atômicas
  ↓
[C] Fusão DAG (03_syndromes) → 34 síndromes
  ↓
[D] Orquestrador (12_output_policies, 09_next_steps) → Card final
  ↓
[E] WORM log (08_wormlog) → Auditoria ANVISA/FDA
```

---

## 🛠️ SPRINT 0 (Semana 1) — CHECKLIST

### **Dia 1-2: Parser & Normalização**
- [ ] **Parser CSV/JSON básico** (`parse_cbc()`):
  - Entrada: `{hb: 12.5, plt: 180, wbc: 6.5, ...}`
  - Saída: Dict canônico conforme `01_schema_hybrid.yaml`
  - Trate unidades (`hb` em `g/dL`, `plt` em `1e9/L`)
  - Derive `mch`, `mchc` se `rbc`, `ht` disponíveis
  - **Test:** 10 casos sintéticos (adulto M/F, pediatria, valores críticos)

- [ ] **Pre-analytical gates** (`check_preanalytical()`):
  - Implemente `00_config → pre_analytical_gates`:
    - `mchc_implausible` (MCHC >38)
    - `cold_agglutinin_suspect` (MCV >130, aglutinação visível)
    - `pseudo_thrombocytopenia_suspect` (aglomerados ou MPV >12)
  - Se flag → retornar `review_sample` + mensagem
  - **Test:** 3 casos (MCHC 40, MCV 135, aglomerados true)

### **Dia 3-4: Evidências**
- [ ] **Evidence engine** (`evaluate_evidences()`):
  - Carregar `02_evidence_hybrid.yaml` (75 evidências)
  - Para cada evidência:
    - Avaliar `rule` (ex: `anc < 0.5`)
    - Se dados ausentes → `status=unknown`
    - Se presente → `status=present`, `strength=strong/moderate/weak`
    - Se ausente → `status=absent`
  - **Segurança:** Usar `simpleeval` ou AST parsing (NUNCA `eval()` direto)
  - **Test:** 
    - E-ANC-CRIT (anc=0.3 → present, anc=0.6 → absent, anc=None → unknown)
    - E-IDA-LABS (ferritin=8 → present, ferritin=120 → absent, ferritin=None → unknown)
    - E-SCHISTOCYTES-GE1PCT (morfologia.esquistocitos=true → present, false → absent, unknown → unknown)

### **Dia 5: Síndromes (MVP)**
- [ ] **Syndrome fusion (MVPisable)** (`fuse_syndromes()`):
  - Carregar `03_syndromes_hybrid.yaml` (foco em 3 síndromes MVP: neutropenia_grave, IDA, TMA)
  - Para cada síndrome:
    - `combine.all`: todas evidências presentes?
    - `combine.any`: pelo menos uma presente?
    - `combine.negative`: nenhuma presente?
    - `threshold`: score ≥ threshold?
  - **Short-circuit:** Se `criticality=critical` → parar imediatamente, retornar
  - **Test:**
    - Caso TMA: esquistocitos=true, plt=8, ldh=980, bt_indireta=1.8 → S-TMA (critical)
    - Caso IDA: mcv=72, rdw=18, ferritin=8 → S-IDA (priority)
    - Caso neutropenia: anc=0.3 → S-NEUTROPENIA-GRAVE (critical)

### **Fim da Semana: Validação**
- [ ] **Pipeline end-to-end** (CSV → card):
  ```python
  cbc = parse_csv("test_case_tma.csv")
  canonical = normalize(cbc, config="00_config_hybrid.yaml")
  preanalytical = check_preanalytical(canonical)
  if preanalytical.flag: return review_sample_card(preanalytical)
  evidences = evaluate_evidences(canonical, "02_evidence_hybrid.yaml")
  syndromes = fuse_syndromes(evidences, "03_syndromes_hybrid.yaml")
  card = render_simple_card(syndromes)
  print(card)
  ```
- [ ] **Output esperado:**
  ```
  🔴 CRÍTICO: TMA (S-TMA)
  Evidências: E-SCHISTOCYTES-GE1PCT (esquistocitos ≥1%), E-PLT-CRIT-LOW (plt=8), E-HEMOLYSIS-PATTERN (ldh=980, bt_indireta=1.8)
  Próximos passos:
    1. Esfregaço urgente + LDH + BT indireta + creatinina
    2. Considerar escore PLASMIC
    3. Avaliar ADAMTS13 e complemento conforme idade
  ```

---

## 📂 ARQUIVOS ESSENCIAIS (SPRINT 0)

### **Core (leia nesta ordem):**
1. `YAMLs/00_config_hybrid.yaml` (cutoffs, units)
2. `YAMLs/01_schema_hybrid.yaml` (canonical schema)
3. `YAMLs/02_evidence_hybrid.yaml` (75 evidências)
4. `YAMLs/03_syndromes_hybrid.yaml` (34 síndromes — foco MVP: 3-5)
5. `YAMLs/10_runbook_hybrid.yaml` (roadmap completo)

### **Postpone para Sprint 1-2:**
- `04_output_templates_hybrid.yaml` (cartões formatados)
- `05_missingness_hybrid_v2.3.yaml` (missingness + proxy logic)
- `09_next_steps_engine_hybrid.yaml` (next steps inteligente)
- `12_output_policies_hybrid.yaml` (confidence C0/C1/C2)

### **Postpone para Sprint 3 (auditoria):**
- `06_route_policy_hybrid.yaml` (route_id SHA256)
- `07_conflict_matrix_hybrid.yaml` (resolução conflitos)
- `08_wormlog_hybrid.yaml` (WORM log imutável)
- `11_case_state_hybrid.yaml` (state machine)

---

## 🧪 TESTES OBRIGATÓRIOS (SPRINT 0)

### **Test suite MVP (20 casos):**
```python
# test_sprint0.py
import pytest

# Parsers
def test_parse_cbc_adult_male():
    cbc = parse_csv("data/adult_male_normal.csv")
    assert cbc["hb"] == 15.2
    assert cbc["sex"] == "M"
    assert cbc["age_years"] == 45

# Pre-analytical
def test_mchc_implausible():
    cbc = {"mchc": 40.5}
    flag = check_preanalytical(cbc, config)
    assert flag.type == "mchc_implausible"
    assert "REVER AMOSTRA" in flag.message

# Evidences
def test_evidence_anc_critical():
    cbc = {"anc": 0.3}
    evidences = evaluate_evidences(cbc, config)
    assert "E-ANC-CRIT" in [e.id for e in evidences if e.status == "present"]

def test_evidence_schisto_positive():
    cbc = {"morphology": {"esquistocitos": True}}
    evidences = evaluate_evidences(cbc, config)
    assert "E-SCHISTOCYTES-GE1PCT" in [e.id for e in evidences if e.status == "present"]

# Syndromes
def test_syndrome_tma_critical():
    cbc = {"plt": 8, "ldh": 980, "morphology": {"esquistocitos": True}}
    evidences = evaluate_evidences(cbc, config)
    syndromes = fuse_syndromes(evidences, config)
    assert "S-TMA" in [s.id for s in syndromes]
    assert syndromes[0].criticality == "critical"

def test_syndrome_ida_priority():
    cbc = {"mcv": 72, "rdw": 18, "ferritin": 8, "hb": 9.5}
    evidences = evaluate_evidences(cbc, config)
    syndromes = fuse_syndromes(evidences, config)
    assert "S-IDA" in [s.id for s in syndromes]
    assert syndromes[0].criticality == "priority"

# Short-circuit
def test_shortcircuit_critical():
    cbc = {"anc": 0.1, "mcv": 72}  # neutropenia grave + microcitose
    evidences = evaluate_evidences(cbc, config)
    syndromes = fuse_syndromes(evidences, config)  # deve parar em neutropenia
    assert syndromes[0].id == "S-NEUTROPENIA-GRAVE"
    assert len(syndromes) == 1  # short-circuit ativo

# End-to-end
def test_e2e_tma_case():
    csv = "data/tma_case_57yo_male.csv"
    card = pipeline_full(csv)
    assert "🔴 CRÍTICO" in card
    assert "S-TMA" in card
    assert "Esfregaço urgente" in card
```

### **Validação (semana 1):**
- [ ] 20 testes unitários passando (100%)
- [ ] 3 casos E2E passando (TMA, IDA, neutropenia grave)
- [ ] Pre-analytical gates funcionando (MCHC >38, pseudo-thrombocytopenia)

---

## 🚨 ARMADILHAS COMUNS (EVITE!)

### **1. NÃO use `eval()` direto:**
❌ **ERRADO:**
```python
result = eval(f"{cbc['anc']} < {config['anc_critical']}")  # VULNERÁVEL!
```

✅ **CORRETO:**
```python
from simpleeval import simple_eval
result = simple_eval(
    "anc < anc_critical",
    names={"anc": cbc["anc"], "anc_critical": config["cutoffs"]["anc_critical"]}
)
```

### **2. NÃO ignore missing data:**
❌ **ERRADO:**
```python
if cbc["ferritin"] < 30:  # KeyError se ferritin ausente!
```

✅ **CORRETO:**
```python
if cbc.get("ferritin") is not None and cbc["ferritin"] < 30:
    return "present"
else:
    return "unknown"
```

### **3. NÃO quebre short-circuit:**
❌ **ERRADO:**
```python
syndromes = []
for s in syndrome_list:  # processa TODOS, mesmo após encontrar critical
    syndromes.append(evaluate(s))
```

✅ **CORRETO:**
```python
syndromes = []
for s in sorted_by_precedence(syndrome_list):
    syndrome = evaluate(s)
    syndromes.append(syndrome)
    if syndrome.criticality == "critical":  # PARAR aqui
        break
```

### **4. NÃO misture unidades:**
❌ **ERRADO:**
```python
hb = 125  # g/L? g/dL? mmol/L?
```

✅ **CORRETO:**
```python
hb_gdl = normalize_units(hb, from_unit="g/L", to_unit="g/dL", config)
# hb_gdl = 12.5
```

---

## 📊 MÉTRICAS DE SUCESSO (SPRINT 0)

### **Técnicas:**
- [ ] 20 testes unitários passando
- [ ] 3 casos E2E (TMA, IDA, neutropenia)
- [ ] Pipeline < 100ms por caso (target: <50ms V0)
- [ ] 0 `eval()` direto no código
- [ ] 100% missing data tratado (unknown, não KeyError)

### **Clínicas (validação posterior):**
- [ ] Red List FN = 0 (Sprint 4)
- [ ] Sensibilidade críticos ≥99%
- [ ] Especificidade geral ≥80%

---

## 🔄 PRÓXIMOS PASSOS (APÓS SPRINT 0)

### **Sprint 1 (semana 2-3): Evidências + Síndromes completas**
- Implementar 75 evidências (todas)
- Implementar 34 síndromes (todas)
- Validar combine logic (ALL/ANY/NEGATIVE)
- Testes: 100 casos sintéticos

### **Sprint 2 (semana 4-5): Missingness + Next Steps**
- `05_missingness` (proxy logic, borderline rules)
- `09_next_steps_engine` (exames priorizados)
- `12_output_policies` (confidence C0/C1/C2)
- Testes: 200 casos sintéticos + 50 com missing

### **Sprint 3 (semana 6): Auditoria**
- `08_wormlog` (WORM log HMAC-SHA256)
- `06_route_policy` (route_id determinístico)
- `07_conflict_matrix` (resolução conflitos)
- `11_case_state` (state machine)

### **Sprint 4 (semana 7-8): Validação clínica**
- Red List (n≥40 por síndrome crítica, FN=0)
- Retrospectiva (n≥500 casos reais)
- Ajuste thresholds conforme resultados
- **Release V0**

---

## 📚 REFERÊNCIAS TÉCNICAS

### **Standards:**
- IEC 62304 (Software Class C)
- ISO 14971:2019 (Risk Management)
- ANVISA RDC 657/2022 (Software as Medical Device)
- FDA 21 CFR Part 11 (Electronic Records)
- LGPD (Lei Geral de Proteção de Dados)

### **Leitura adicional:**
- `ANALISE_COMPARATIVA_TRIPLA_*.md` — decisões de design
- `COMPARACAO_HIBRIDO_vs_SADMH_V2.3.md` — módulos integrados
- `INDEX_COMPLETO.md` — navegação completa

---

## 🆘 SUPORTE

### **Dúvidas técnicas:**
- 📄 Leia `DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md` (exemplo completo com código)
- 📄 Consulte `10_runbook_hybrid.yaml` (roadmap detalhado)
- 📄 Veja `INDEX_COMPLETO.md` (mapa de dependências)

### **Dúvidas clínicas:**
- 📄 Consulte glossário em `DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md` (IDA, ACD, TMA, PTI, etc.)
- 🩺 Contato: Dr. Abel Costa (IDOR-SP)

### **Bugs/issues:**
- Documente no WORM log (após Sprint 3)
- Tag: `BUG-SPRINT-X-YYYY`
- Include: input canônico, evidências esperadas vs. reais, YAML version hash

---

## ✅ CHECKLIST FINAL (ANTES DE SPRINT 1)

- [ ] Python env configurado
- [ ] YAMLs carregam sem erro (`yaml.safe_load()`)
- [ ] Parser CSV → canonical dict funcionando
- [ ] Pre-analytical gates implementado
- [ ] Evidence engine (3 evidências MVP: ANC-CRIT, IDA-LABS, SCHISTOCYTES)
- [ ] Syndrome fusion (3 síndromes MVP: neutropenia, IDA, TMA)
- [ ] Short-circuit críticos funcionando
- [ ] 20 testes unitários passando
- [ ] 3 casos E2E (TMA, IDA, neutropenia)
- [ ] 0 uso de `eval()` direto
- [ ] Missing data tratado (unknown, não KeyError)
- [ ] Pipeline < 100ms por caso

---

## 🎉 BEM-VINDO AO HEMODOCTOR HYBRID!

**Você está construindo um sistema que pode:**
- 🔴 Salvar vidas (detecção TMA, neutropenia grave, blástica)
- 🟠 Acelerar diagnósticos (IDA, talassemia, hemólise)
- 🔵 Reduzir alert fatigue (apenas alertas relevantes)
- ⚪ Prevenir erros pré-analíticos (pseudo-trombocitopenia, aglutinina fria)

**Com:**
- ✅ Transparência total (regras YAML legíveis por hematologistas)
- ✅ Segurança regulatória (ANVISA/FDA/ISO compliance)
- ✅ Explicabilidade (rationale + evidências + valores-chave)
- ✅ Auditoria imutável (WORM log HMAC-SHA256)

**Versão:** V1.0  
**Data:** Outubro 2025  
**Status:** ✅ **Pronto para Sprint 0**

**Boa sorte! 🚀**

---

**FIM DO QUICKSTART**

