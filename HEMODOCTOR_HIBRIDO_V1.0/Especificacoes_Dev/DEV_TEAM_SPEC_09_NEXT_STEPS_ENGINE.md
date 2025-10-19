# DEV TEAM SPECIFICATION: Next Steps Engine (Módulo 09)
# HemoDoctor Hybrid V1.0 - Always-Output Design
# Dr. Abel Costa (IDOR-SP) - Outubro 2025

---

## 📋 SUMÁRIO EXECUTIVO

### O que é?
Motor inteligente que **sempre** gera recomendações de próximos passos clínicos, mesmo com dados parciais.

### Por que é crítico?
- ✅ **Safety:** Nunca deixa o clínico "sem ação" (sempre orienta o próximo passo)
- ✅ **ANVISA:** Transparência total (explica POR QUE solicitar cada exame)
- ✅ **Custo-efetividade:** Prioriza exames por custo/turnaround
- ✅ **UX:** Reduz carga cognitiva do médico (lista priorizada, não dump de opções)

### Integração no pipeline
```
CBC + Complementares 
  → Normalização (00_config)
  → Evidências (02_evidence)
  → Síndromes (03_syndromes)
  → Missingness (05_missingness) 
  → **Next Steps Engine (09)** ← VOCÊ ESTÁ AQUI
  → Output Policies (12)
  → Card Final
```

---

## 🎯 OBJETIVO DO MÓDULO

Dado um caso com:
- ✅ Dados disponíveis (CBC + complementares)
- ✅ Síndromes detectadas (ou ausentes)
- ✅ Missing keys (dados ausentes)

**Retornar:**
- Lista de 0-8 exames recomendados
- Priorizados por: `level` (critical > priority > routine) + `cost` + `turnaround`
- Com `rationale` clínico explícito
- Com `prereq` (pré-requisitos) para contexto

---

## 🏗️ ARQUITETURA

### Estrutura do YAML

```yaml
version: hybrid_v1.0.0
module: next_steps_engine

prioritization:
  levels: [critical, priority, routine]
  tie_break: cost_then_turnaround
  cost_bands: {low, mid, high}
  turnaround: {fast, medium, slow}

render:
  max_items: 8
  group_by_level: true
  deduplicate_by_test: true

triggers:
  - id: trigger-ida
    when: "(mcv < 80) and (rdw > 14.0) and ... and (ferritin is None)"
    syndromes: [S-IDA]
    suggest:
      - {level: priority, test: Ferritina, rationale: "...", cost: low, ...}
      - {level: priority, test: TSat, ...}
```

### Lógica de Execução

```python
def compute_next_steps(case: Dict) -> List[NextStep]:
    """
    1. Iterar sobre todos os triggers
    2. Avaliar 'when' (expressão Python sobre case)
    3. Se True: adicionar todos os 'suggest' do trigger à lista candidata
    4. Dedupe por 'test' (se mesmo teste sugerido por 2 triggers, manter 1)
    5. Ordenar por (level, cost_band, turnaround)
    6. Limitar a max_items (8)
    7. Retornar lista final
    """
    candidates = []
    
    for trigger in YAML['triggers']:
        if eval_safe(trigger['when'], case):  # Eval seguro!
            for item in trigger['suggest']:
                candidates.append({
                    'level': item['level'],
                    'test': item['test'],
                    'rationale': item['rationale'],
                    'cost': item['cost'],
                    'turnaround': item['turnaround'],
                    'prereq': item['prereq'],
                    'trigger_id': trigger['id']
                })
    
    # Dedupe
    seen = set()
    deduped = []
    for c in candidates:
        if c['test'] not in seen:
            deduped.append(c)
            seen.add(c['test'])
    
    # Sort
    level_order = {'critical': 0, 'priority': 1, 'routine': 2}
    cost_order = {'low': 0, 'mid': 1, 'high': 2}
    turnaround_order = {'fast': 0, 'medium': 1, 'slow': 2}
    
    deduped.sort(key=lambda x: (
        level_order[x['level']],
        cost_order[x['cost']],
        turnaround_order[x['turnaround']]
    ))
    
    return deduped[:8]  # Max 8 items
```

---

## 🔒 SEGURANÇA: Avaliação Segura de Expressões

**CRÍTICO:** O campo `when` contém expressões Python. **NUNCA** usar `eval()` diretamente!

### Opção A: Biblioteca `simpleeval` (RECOMENDADA)
```python
from simpleeval import simple_eval

SAFE_NAMES = {
    'sex': case.get('sex'),
    'hb': case.get('hb'),
    'mcv': case.get('mcv'),
    # ... todos os campos do schema
    'None': None,
    'true': True,
    'false': False
}

SAFE_FUNCTIONS = {
    # Nenhuma função permitida (apenas comparações)
}

def eval_safe(expression: str, case: Dict) -> bool:
    try:
        result = simple_eval(
            expression,
            names=SAFE_NAMES,
            functions=SAFE_FUNCTIONS
        )
        return bool(result)
    except Exception as e:
        logger.error(f"Trigger eval failed: {expression} | {e}")
        return False
```

### Opção B: AST Parsing (para máxima segurança)
```python
import ast

def eval_safe(expression: str, case: Dict) -> bool:
    try:
        tree = ast.parse(expression, mode='eval')
        # Validar: apenas operadores seguros (Compare, BoolOp, UnaryOp, etc.)
        # Não permitir: Call, Import, Lambda, etc.
        return eval(compile(tree, '<string>', 'eval'), {'__builtins__': {}}, case)
    except Exception:
        return False
```

---

## 📊 EXEMPLOS PRÁTICOS

### Exemplo 1: IDA Suspeita (dados parciais)

**Input:**
```json
{
  "hb": 9.5,
  "sex": "F",
  "mcv": 72,
  "rdw": 16,
  "ferritin": null,
  "tsat": null,
  "crp": null
}
```

**Trigger ativado:** `trigger-ida`
```yaml
when: "(mcv < 80) and (rdw > 14.0) and ((sex=='M' and hb < 13.0) or (sex=='F' and hb < 12.0)) and (ferritin is None or tsat is None)"
```

**Output:**
```json
[
  {
    "level": "priority",
    "test": "Ferritina",
    "rationale": "Confirmar IDA (ferritina <30 ng/mL) vs ACD (ferritina 30-100 com inflamação)",
    "cost": "low",
    "turnaround": "fast",
    "prereq": "CBC"
  },
  {
    "level": "priority",
    "test": "TSat",
    "rationale": "TSat <20% confirma deficiência de ferro funcional",
    "cost": "low",
    "turnaround": "fast",
    "prereq": "Ferro sérico"
  },
  {
    "level": "routine",
    "test": "CRP",
    "rationale": "Diferenciar IDA pura (CRP normal) vs ACD/IDA-inflam (CRP >10 mg/L)",
    "cost": "low",
    "turnaround": "fast",
    "prereq": "CBC"
  }
]
```

### Exemplo 2: TMA Crítica (dados completos, mas falta subtipar)

**Input:**
```json
{
  "plt": 25,
  "esquistocitos": true,
  "ldh": 980,
  "creatinine": 2.1,
  "adamts13_activity": null,
  "c3": null
}
```

**Trigger ativado:** `trigger-tma`

**Output:**
```json
[
  {
    "level": "critical",
    "test": "Esfregaço URGENTE",
    "rationale": "Confirmar esquistócitos ≥1% (fragmentação mecânica)",
    "cost": "low",
    "turnaround": "fast",
    "prereq": "CBC"
  },
  {
    "level": "priority",
    "test": "ADAMTS13 atividade + inibidor",
    "rationale": "ADAMTS13 <10% = PTT; >10% = SHU/SHUa/TMA secundária",
    "cost": "high",
    "turnaround": "slow",
    "prereq": "Creatinina"
  },
  {
    "level": "priority",
    "test": "Complemento (C3, C4, CH50)",
    "rationale": "C3 baixo = SHUa (complemento-mediada)",
    "cost": "high",
    "turnaround": "slow",
    "prereq": "ADAMTS13 >10%"
  }
]
```

### Exemplo 3: Borderline MCV (sem síndrome, mas output garantido)

**Input:**
```json
{
  "hb": 13.8,
  "sex": "M",
  "mcv": 81,
  "rdw": 12
}
```

**Trigger ativado:** `trigger-borderline-microcytosis`

**Output:**
```json
[
  {
    "level": "routine",
    "test": "CBC repeat (2-6 semanas)",
    "rationale": "MCV borderline: repetir para confirmar tendência",
    "cost": "low",
    "turnaround": "fast",
    "prereq": "CBC"
  },
  {
    "level": "routine",
    "test": "Ferritina",
    "rationale": "Se anemia limítrofe: descartar deficiência de ferro precoce",
    "cost": "low",
    "turnaround": "fast",
    "prereq": "Anemia ou tendência"
  }
]
```

---

## 🧪 TESTES UNITÁRIOS

### Casos de Teste Obrigatórios

```python
import pytest
from next_steps_engine import compute_next_steps

def test_ida_complete():
    """IDA com ferritina/TSat completos → não sugere mais nada"""
    case = {
        'hb': 9.5, 'sex': 'F', 'mcv': 72, 'rdw': 16,
        'ferritin': 8, 'tsat': 12, 'crp': 3
    }
    result = compute_next_steps(case)
    assert len(result) == 0  # Já tem tudo

def test_ida_partial():
    """IDA sem ferritina/TSat → sugere ambos"""
    case = {
        'hb': 9.5, 'sex': 'F', 'mcv': 72, 'rdw': 16
    }
    result = compute_next_steps(case)
    assert len(result) >= 2
    assert 'Ferritina' in [r['test'] for r in result]
    assert 'TSat' in [r['test'] for r in result]

def test_tma_critical():
    """TMA → sempre sugere esfregaço urgente primeiro"""
    case = {
        'plt': 25, 'esquistocitos': True, 'ldh': 980
    }
    result = compute_next_steps(case)
    assert result[0]['level'] == 'critical'
    assert 'Esfregaço' in result[0]['test']

def test_borderline_always_output():
    """MCV borderline → sempre gera output (rotina)"""
    case = {
        'hb': 13.8, 'sex': 'M', 'mcv': 81, 'rdw': 12
    }
    result = compute_next_steps(case)
    assert len(result) > 0

def test_prioritization():
    """Críticos sempre antes de priority"""
    case = {
        'anc': 0.3,  # Neutropenia grave (crítico)
        'mcv': 72, 'rdw': 16, 'hb': 9.5, 'sex': 'F'  # IDA (priority)
    }
    result = compute_next_steps(case)
    # Primeiro item deve ser crítico
    assert result[0]['level'] == 'critical'

def test_dedupe():
    """Se 2 triggers sugerem mesmo exame, dedupe"""
    case = {
        'plt': 25, 'esquistocitos': True,  # TMA
        'ldh': None  # Ambos TMA e hemólise sugeririam LDH
    }
    result = compute_next_steps(case)
    ldh_count = sum(1 for r in result if r['test'] == 'LDH')
    assert ldh_count <= 1

def test_max_items():
    """Nunca retornar mais de 8 itens"""
    # Caso patológico com múltiplos triggers
    case = {
        'hb': 6.0, 'sex': 'F', 'mcv': 72, 'rdw': 16,
        'plt': 25, 'esquistocitos': True, 'anc': 0.3,
        'wbc': 90, 'blasts': True
    }
    result = compute_next_steps(case)
    assert len(result) <= 8
```

---

## 🚨 CASOS DE BORDA

### Caso 1: Sem dados suficientes para qualquer síndrome
**Input:** `{hb: 13.5, sex: 'M'}`  
**Comportamento:** Triggers borderline não disparam → retorna `[]` (lista vazia OK)  
**Fallback:** Módulo 12 (output_policies) garante card "ROTINA" mesmo com lista vazia.

### Caso 2: Múltiplos triggers conflitantes
**Input:** IDA + ACD (ambos verdadeiros)  
**Comportamento:** Ambos triggers disparam → dedupe por `test` → lista única.

### Caso 3: Trigger com `when` inválido
**Erro:** `when: "mcv < INVALIDO"`  
**Comportamento:** `eval_safe()` retorna `False` → trigger ignorado → log de erro.

### Caso 4: Exame já presente no caso
**Input:** `{ferritin: 8}`  
**Trigger:** `trigger-ida` sugere "Ferritina"  
**Comportamento:** Módulo 05 (missingness) já deveria ter filtrado o trigger. Se não filtrou, output_policies (12) pode filtrar na renderização.

---

## 🔗 INTEGRAÇÃO COM OUTROS MÓDULOS

### Com Módulo 05 (Missingness)
- **Missingness** avalia lacunas e define `missing_keys`
- **Next Steps Engine** usa `missing_keys` nas condições `when`
- Exemplo: `when: "ferritin is None"` → só dispara se ferritina ausente

### Com Módulo 12 (Output Policies)
- **Next Steps Engine** retorna lista bruta de 0-8 itens
- **Output Policies** renderiza no card final:
  - Formata em markdown/HTML
  - Agrupa por `level`
  - Mostra custo/turnaround se configurado
  - Adiciona disclaimer (ex.: "Atualizar caso ao receber resultados")

### Com Módulo 11 (Case State)
- Quando novo exame chega (evento `RESULTS_ARRIVED`):
  - State machine dispara `recompute_syndromes`
  - Next Steps Engine roda novamente
  - Lista de próximos passos é atualizada (pode diminuir ou mudar)

---

## 📈 MÉTRICAS DE QUALIDADE

### Durante Desenvolvimento
- **Coverage:** 100% das 34 síndromes têm trigger (validado por script)
- **Dedupe:** 0 testes duplicados por caso (teste automatizado)
- **Max Items:** Nunca > 8 (teste automatizado)

### Em Produção (PMS)
- **Alert Fatigue:** % de médicos que ignoram >50% das sugestões
  - **Target:** <10% (significa que sugestões são relevantes)
- **Test Completion Rate:** % de exames sugeridos que são efetivamente realizados
  - **Target:** >60% para priority, >30% para routine
- **Time to Diagnosis:** Tempo médio entre CBC inicial e diagnóstico definitivo
  - **Target:** Redução de 20% vs baseline sem next_steps_engine

---

## 🛠️ IMPLEMENTAÇÃO EM ETAPAS

### Sprint 0 (1 semana)
- [ ] Parser YAML (carregar 09_next_steps_engine_hybrid.yaml)
- [ ] Função `eval_safe()` (simpleeval ou AST)
- [ ] Função `compute_next_steps()` (lógica core)
- [ ] 6 testes unitários básicos (IDA, TMA, neutropenia, borderline, dedupe, max_items)

### Sprint 1 (1 semana)
- [ ] Integrar com módulo 05 (missingness) para receber `missing_keys`
- [ ] Integrar com módulo 03 (syndromes) para receber síndromes detectadas
- [ ] Testes de integração (pipeline completo)

### Sprint 2 (1 semana)
- [ ] Validação retrospectiva com 100 casos reais (IDOR-SP)
- [ ] Ajustar triggers se taxa de sugestão irrelevante >20%
- [ ] Documentação final para médicos (interpretação dos próximos passos)

---

## 🎓 GLOSSÁRIO PARA DEVS NÃO-MÉDICOS

| Termo | Significado |
|-------|-------------|
| **IDA** | Iron Deficiency Anemia (anemia por deficiência de ferro) |
| **ACD** | Anemia of Chronic Disease (anemia de doença crônica/inflamação) |
| **TMA** | Microangiopatia Trombótica (esquistócitos + plaquetas baixas + hemólise) |
| **PTI** | Púrpura Trombocitopênica Imune (plaquetas baixas por anticorpos) |
| **PTT** | Púrpura Trombocitopênica Trombótica (TMA por deficiência de ADAMTS13) |
| **SHU** | Síndrome Hemolítico-Urêmica (TMA + insuficiência renal) |
| **CIVD** | Coagulação Intravascular Disseminada (consumo de plaquetas + coagulopatia) |
| **LPA (M3)** | Leucemia Promielocítica Aguda (emergência hematológica) |
| **MDS** | Mielodisplasia (displasia medular com risco de leucemia) |
| **MPN** | Neoplasia Mieloproliferativa (TE, PV, MF) |
| **TE** | Trombocitemia Essencial (plaquetas altas clonais) |
| **PV** | Policitemia Vera (hemoglobina alta clonal) |
| **CBC** | Complete Blood Count (hemograma completo) |

---

## 📞 CONTATO E SUPORTE

**Product Owner Clínico:** Dr. Abel Costa (IDOR-SP)  
**Arquiteto Técnico:** Dev Team HemoDoctor  
**Referência YAML:** `ARVORE_DECISAO_HIBRIDA_DEFINITIVA/09_next_steps_engine_hybrid.yaml`  
**Documento Master:** `ANALISE_COMPARATIVA_TRIPLA_HEMODOCTOR_SADMH_DEVTEAM.md`

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO

- [ ] Parser YAML funcional
- [ ] `eval_safe()` com simpleeval ou AST
- [ ] `compute_next_steps()` implementado
- [ ] 6 testes unitários passando
- [ ] Integração com módulo 05 (missingness)
- [ ] Integração com módulo 12 (output_policies)
- [ ] Validação com 100 casos reais
- [ ] Code review por hematologista (Dr. Abel)
- [ ] Documentação de API atualizada
- [ ] Deploy em staging
- [ ] Aprovação QA/Regulatório

---

**FIM DO DOCUMENTO**

