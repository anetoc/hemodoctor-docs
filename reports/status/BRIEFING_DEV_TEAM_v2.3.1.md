# 🎯 BRIEFING DEV TEAM: HemoDoctor Hybrid v2.3.1 + CDSS

**Data:** 19 de Outubro de 2025  
**Duração:** 1 hora  
**Audiência:** Backend Engineers, QA, Arquiteto de Software  
**Apresentador:** Dr. Abel Costa + AI Medical Device Specialist  

---

## 📊 AGENDA (60 min)

```
┌─────────────────────────────────────────────────────────┐
│  00-10 min  │  Visão Geral e Contexto                   │
│  10-25 min  │  Arquitetura Técnica (YAMLs)              │
│  25-40 min  │  Correções Críticas e CDSS                │
│  40-50 min  │  Roadmap de Implementação (Sprints)       │
│  50-60 min  │  Q&A e Próximos Passos                    │
└─────────────────────────────────────────────────────────┘
```

---

## 1️⃣ VISÃO GERAL (10 min)

### O que é HemoDoctor?

**Sistema de Apoio à Decisão Clínica (CDSS)** para análise de hemogramas

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  CBC Input   │ ───▶ │  HemoDoctor  │ ───▶ │  Card Output │
│  (41 campos) │      │   v2.3.1     │      │ (não-diagn.) │
└──────────────┘      └──────────────┘      └──────────────┘
     YAML 01              YAMLs 02-12            YAML 04
```

**Objetivo:** Detectar 35 síndromes hematológicas com FN críticos = 0

### Contexto da Versão v2.3.1

**v1.0.0 (Outubro 2025):**
- 34 síndromes, 75 evidências
- ❌ **3 ERROS CRÍTICOS** descobertos na validação externa

**v2.3.1 (HOJE):**
- ✅ **3 erros corrigidos** (PV, Eritrocitose, Pancitopenia)
- 35 síndromes (+S-ACD), 79 evidências (+4)
- 🆕 **CDSS**: Microcopy segura não-diagnóstica
- 🆕 Gating inteligente, idempotência, triggers críticos

### Por que este briefing?

1. **Implementação Python:** Transformar YAMLs em código funcional
2. **Timeline:** 4 semanas (Sprint 0-4) para MVP
3. **Crítico:** FN em casos críticos = 0 (Red List)
4. **Regulatório:** ANVISA/FDA compliance (WORM log, auditoria)

---

## 2️⃣ ARQUITETURA TÉCNICA (15 min)

### Pipeline Completo

```python
# Pipeline de processamento
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  Input (CBC) → Normalizador → Evidence Engine →           │
│                                                            │
│  Syndrome Engine → Missingness Handler →                  │
│                                                            │
│  Route Policy → Next Steps → Output Templates →           │
│                                                            │
│  WORM Log → Card Final (JSON/HTML/Markdown)               │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### Stack Tecnológico Recomendado

```yaml
Backend:
  language: Python 3.11+
  framework: FastAPI (async)
  validation: Pydantic v2
  
Data:
  yaml_parser: PyYAML / ruamel.yaml
  database: PostgreSQL 15+ (TimescaleDB para WORM log)
  cache: Redis (opcional, para performance)
  
ML/Calibration:
  torch: ">=2.0" (Platt scaling, sem scikit-learn!)
  numpy: ">=1.24"
  sympy: ">=1.12" (isotônica)
  
Security:
  crypto: cryptography (HMAC-SHA256)
  kms: AWS KMS / Azure Key Vault / GCP KMS
  
Observability:
  metrics: Prometheus + Grafana
  logging: structlog (JSON logs)
  tracing: OpenTelemetry (opcional)
  
Testing:
  unit: pytest + pytest-cov
  integration: pytest + httpx
  e2e: Red List (240 casos críticos)
```

### Estrutura de Diretórios Proposta

```
hemodoctor/
├── src/
│   ├── config/                    # Módulo 00
│   │   ├── __init__.py
│   │   ├── loader.py              # Carrega 00_config_hybrid.yaml
│   │   └── models.py              # Pydantic models
│   │
│   ├── schema/                    # Módulo 01
│   │   ├── __init__.py
│   │   ├── cbc_input.py           # 41 campos CBC
│   │   └── normalizer.py          # Normalização + validação
│   │
│   ├── evidence/                  # Módulo 02
│   │   ├── __init__.py
│   │   ├── loader.py              # Carrega 02_evidence_hybrid.yaml
│   │   ├── engine.py              # Avalia 79 evidências
│   │   └── models.py              # Evidence dataclass
│   │
│   ├── syndrome/                  # Módulo 03
│   │   ├── __init__.py
│   │   ├── loader.py              # Carrega 03_syndromes_hybrid.yaml
│   │   ├── engine.py              # Combine logic (ALL/ANY/NEGATIVE)
│   │   ├── confidence.py          # Threshold → C0/C1/C2
│   │   └── models.py              # Syndrome dataclass
│   │
│   ├── missingness/               # Módulo 05
│   │   ├── __init__.py
│   │   ├── handler.py             # Always-output design
│   │   └── proxy_logic.py         # Inferência de campos
│   │
│   ├── route/                     # Módulo 06
│   │   ├── __init__.py
│   │   ├── policy.py              # Precedence, conflicts
│   │   └── deterministic.py       # Route SHA256
│   │
│   ├── wormlog/                   # Módulo 08
│   │   ├── __init__.py
│   │   ├── writer.py              # Append-only JSONL
│   │   ├── hmac.py                # HMAC-SHA256 signing
│   │   └── models.py              # WORM entry schema
│   │
│   ├── next_steps/                # Módulo 09
│   │   ├── __init__.py
│   │   ├── loader.py              # Carrega triggers
│   │   ├── engine.py              # Gating + prioritização
│   │   └── models.py              # NextStep dataclass
│   │
│   ├── output/                    # Módulos 04 + 12
│   │   ├── __init__.py
│   │   ├── templates.py           # 04_output_templates_hybrid.yaml
│   │   ├── policies.py            # 12_output_policies_cdss.yaml
│   │   ├── renderer.py            # Markdown/HTML/JSON
│   │   └── microcopy.py           # Léxico controlado
│   │
│   ├── state/                     # Módulo 11
│   │   ├── __init__.py
│   │   ├── machine.py             # State transitions
│   │   └── models.py              # Case state
│   │
│   └── api/
│       ├── __init__.py
│       ├── main.py                # FastAPI app
│       ├── routes.py              # Endpoints
│       └── middleware.py          # Auth, CORS, etc.
│
├── tests/
│   ├── unit/
│   │   ├── test_evidence_engine.py
│   │   ├── test_syndrome_engine.py
│   │   └── test_confidence_mapping.py
│   ├── integration/
│   │   ├── test_pipeline.py
│   │   └── test_api.py
│   └── e2e/
│       ├── red_list_240_cases.json
│       └── test_red_list.py       # FN críticos = 0
│
├── config/
│   └── yamls/                     # 14 YAMLs do repo
│
├── docs/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   └── DEVELOPER_GUIDE.md
│
├── pyproject.toml                 # Poetry/PDM
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### YAMLs → Python: Exemplo Prático

#### YAML (03_syndromes_hybrid.yaml)
```yaml
- id: S-PV
  criticality: priority
  combine:
    any: [E-HB-HIGH, E-HCT-HIGH]
  negative: [E-CRP-HIGH]
  threshold: 0.7
  actions:
    - "Repetir CBC"
    - "JAK2/CALR/MPL"
```

#### Python (Pydantic Models)
```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional

class Criticality(str, Enum):
    CRITICAL = "critical"
    PRIORITY = "priority"
    ROUTINE = "routine"
    REVIEW_SAMPLE = "review_sample"

class CombineLogic(BaseModel):
    all: Optional[List[str]] = None
    any: Optional[List[str]] = None
    negative: Optional[List[str]] = None

class Syndrome(BaseModel):
    id: str
    criticality: Criticality
    combine: CombineLogic
    threshold: float = Field(ge=0.0, le=1.0)
    actions: List[str]
    next_steps: Optional[List[str]] = None
    evidence_trail_template: Optional[str] = None
    missing_fields_warn: Optional[List[str]] = None
    source: str

# Loader
import yaml
from pathlib import Path

def load_syndromes(yaml_path: Path) -> List[Syndrome]:
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    
    syndromes = []
    for section in ['critical_syndromes', 'priority_syndromes', ...]:
        if section in data:
            for s in data[section]:
                syndromes.append(Syndrome(**s))
    
    return syndromes

# Engine
class SyndromeEngine:
    def __init__(self, syndromes: List[Syndrome], config):
        self.syndromes = syndromes
        self.config = config
    
    def evaluate(self, evidences: dict) -> List[dict]:
        """
        Avalia todas as síndromes contra evidências disparadas.
        
        Args:
            evidences: {"E-HB-HIGH": True, "E-HCT-HIGH": True, ...}
        
        Returns:
            [{"id": "S-PV", "confidence": "C1", "score": 0.75}, ...]
        """
        results = []
        
        for syndrome in self.syndromes:
            score = self._compute_score(syndrome, evidences)
            
            if score >= syndrome.threshold:
                confidence = self._map_confidence(score)
                results.append({
                    "id": syndrome.id,
                    "name": syndrome.id.replace("S-", ""),
                    "criticality": syndrome.criticality,
                    "confidence": confidence,
                    "score": score,
                    "actions": syndrome.actions
                })
        
        return results
    
    def _compute_score(self, syndrome: Syndrome, evidences: dict) -> float:
        """
        Implementa lógica ALL/ANY/NEGATIVE.
        """
        score = 0.0
        
        # ALL: todas as evidências devem estar presentes
        if syndrome.combine.all:
            if all(evidences.get(e, False) for e in syndrome.combine.all):
                score += 1.0 * len(syndrome.combine.all)
        
        # ANY: pelo menos uma evidência presente
        if syndrome.combine.any:
            count = sum(1 for e in syndrome.combine.any if evidences.get(e, False))
            score += 0.5 * count
        
        # NEGATIVE: evidências que NÃO devem estar presentes
        if syndrome.combine.negative:
            if any(evidences.get(e, False) for e in syndrome.combine.negative):
                score -= 0.3 * len(syndrome.combine.negative)
        
        # Normalizar
        max_score = (
            (len(syndrome.combine.all or []) * 1.0) +
            (len(syndrome.combine.any or []) * 0.5)
        )
        
        if max_score > 0:
            return max(0.0, min(1.0, score / max_score))
        
        return 0.0
    
    def _map_confidence(self, score: float) -> str:
        """
        Score → C0/C1/C2 baseado em thresholds do config.
        """
        if score >= 0.80:
            return "C2"
        elif score >= 0.60:
            return "C1"
        else:
            return "C0"
```

---

## 3️⃣ CORREÇÕES CRÍTICAS + CDSS (15 min)

### 3 Erros Críticos Corrigidos

#### 1. S-PV (Policitemia Vera) ❌→✅

**ANTES (v1.0.0):**
```yaml
combine:
  all: [E-HB-CRIT-LOW]  # ❌ Anemia! (oposto de PV)
```

**DEPOIS (v2.3.1):**
```yaml
combine:
  any: [E-HB-HIGH, E-HCT-HIGH]  # ✅ Eritrocitose
negative: [E-CRP-HIGH]
```

**Impacto:**
- Sistema detectava ANEMIA quando devia detectar ERITROCITOSE
- **Falso Negativo crítico:** PV não diagnosticada
- **Risco clínico:** Pacientes com PV não identificados

**Teste Case:**
```python
test_pv = {
    "hb": 19.5,  # Alto (M)
    "ht": 55,    # Alto (M) → 52% limite
    "wbc": 12,
    "plt": 450,
    "age_years": 55,
    "sex": "M"
}

# v1.0.0: NÃO detectava S-PV ❌
# v2.3.1: Detecta S-PV (C1 ou C2) ✅
```

#### 2. S-ERITROCITOSE-SECUNDARIA ❌→✅

**Mesmo problema:** Detectava anemia em vez de eritrocitose

#### 3. S-PANCYTOPENIA ❌→✅

**ANTES (v1.0.0):**
```yaml
combine:
  all: [E-HB-CRIT-LOW, E-PLT-LOW]
  any: [E-ANC-CRIT, E-WBC-HIGH]  # ❌ Leucocitose!
```

**DEPOIS (v2.3.1):**
```yaml
combine:
  all: [E-ANEMIA, E-PLT-LOW, E-WBC-LOW]  # ✅ Leucopenia
```

**Teste Case:**
```python
test_pancytopenia = {
    "hb": 8.0,    # Baixo
    "wbc": 2.5,   # Baixo (< 4.0)
    "plt": 80,    # Baixo
    "anc": 1.2,
    "age_years": 45,
    "sex": "F"
}

# v1.0.0: NÃO detectava S-PANCYTOPENIA ❌
# v2.3.1: Detecta S-PANCYTOPENIA (C1 ou C2) ✅
```

### Nova Síndrome: S-ACD ✨

**S-ACD (Anemia da Doença Crônica/Inflamatória)**

```yaml
- id: S-ACD
  criticality: priority
  combine:
    all: [E-ANEMIA]
    any: [E-FERRITIN-HIGH-100, E-CRP-HIGH]
  negative: [E-HBA2-HIGH, E-HEMOLYSIS-PATTERN]
  threshold: 0.7
```

**Clínica:**
- Anemia + ferritina alta (≥100) OU CRP alto
- Exclui talassemia (HbA2 alto) e hemólise
- Tratamento: Condição inflamatória de base

### Módulos CDSS (Microcopy Segura)

#### Módulo 04: Output Templates

**Propósito:** NUNCA usar linguagem diagnóstica

```yaml
lexicon:
  allowed_verbs:
    - "padrão compatível com"
    - "sugere"
    - "pode representar"
    - "considerar"
  
  avoid:
    - "diagnóstico de"
    - "tem (doença)"
    - "confirma"
    - "é (doença)"
```

**Templates:**
```yaml
critical:
  header: "CRÍTICO — {headline}"
  body: |
    Hipótese: **{syndrome_name} (C{confidence})** — {compat_phrase}.
    **Por quê:** {evidence_short}. {values_line}
    **Ação tempo-sensível:** {next_step_1}; {next_step_2}; {next_step_3}.
    *CDSS de apoio à decisão. Não substitui julgamento clínico.*
```

**Implementação Python:**
```python
from string import Template

class OutputRenderer:
    def __init__(self, templates_yaml: Path):
        self.templates = self._load_templates(templates_yaml)
    
    def render_critical(self, syndrome: dict, values: dict) -> str:
        """
        Renderiza card crítico com microcopy segura.
        """
        template = Template(self.templates['critical']['body'])
        
        # Placeholder substitution
        return template.safe_substitute(
            syndrome_name=syndrome['name'],
            confidence=syndrome['confidence'],
            compat_phrase=self._get_compat_phrase(syndrome['confidence']),
            evidence_short=self._format_evidence(syndrome['evidences']),
            values_line=self._format_values(values),
            next_step_1=syndrome['actions'][0],
            next_step_2=syndrome['actions'][1],
            next_step_3=syndrome['actions'][2]
        )
    
    def _get_compat_phrase(self, confidence: str) -> str:
        """
        C0/C1/C2 → frase de compatibilidade.
        """
        mapping = {
            "C0": "indícios insuficientes",
            "C1": "padrão compatível",
            "C2": "padrão sugestivo"
        }
        return mapping.get(confidence, "padrão compatível")
```

#### Módulo 12-CDSS: Gating Inteligente

**Problema:** Sistema sugeria exames avançados antes dos básicos

**Solução:** Gating rules

```yaml
gating:
  - name: anemia_workup
    if: "S-IDA OR S-ACD OR S-MACRO-B12-FOLATE"
    require_first: ["Ferritina", "TSat", "CRP", "B12", "Folato"]
  
  - name: thrombocytopenia_workup
    if: "plt<150"
    require_first: ["Esfregaço", "MPV"]
```

**Implementação Python:**
```python
class GatingEngine:
    def __init__(self, gating_rules: List[dict]):
        self.rules = gating_rules
    
    def filter_next_steps(
        self,
        syndrome_id: str,
        suggested_steps: List[str],
        ordered_tests: List[str]
    ) -> List[str]:
        """
        Filtra próximos passos baseado em gating rules.
        
        Args:
            syndrome_id: S-IDA, S-PTI, etc.
            suggested_steps: ["JAK2", "Medula óssea", ...]
            ordered_tests: ["Ferritina", "TSat", "CRP", ...]
        
        Returns:
            Apenas steps permitidos pelo gating
        """
        for rule in self.rules:
            if self._matches_condition(rule['if'], syndrome_id):
                required = set(rule['require_first'])
                ordered = set(ordered_tests)
                
                # Se algum exame básico está faltando, bloquear avançados
                if not required.issubset(ordered):
                    missing = required - ordered
                    return [f"PRIMEIRO: {', '.join(missing)}"] + \
                           [s for s in suggested_steps if s in required]
        
        return suggested_steps
```

---

## 4️⃣ ROADMAP DE IMPLEMENTAÇÃO (10 min)

### Sprint 0 (Semana 1): Setup + Parser

**Objetivo:** Infraestrutura básica funcional

**Tasks:**
```
[ ] 1. Repo setup
    - Git, Docker, CI/CD (GitHub Actions)
    - Pre-commit hooks (black, ruff, mypy)
    - Poetry/PDM para dependências

[ ] 2. YAML Parser
    - Loader para 00-12 YAMLs
    - Pydantic models (type-safe)
    - Validação de schema

[ ] 3. Normalizer (01_schema)
    - CBC input (41 campos)
    - Validação de ranges fisiológicos
    - Unidades LOINC

[ ] 4. Evidence Engine básico (02_evidence)
    - Avaliação de regras (79 evidências)
    - Teste: 10 evidências core

[ ] 5. Testes unitários
    - pytest setup
    - Coverage mínimo: 60%
```

**Entregável:** Pipeline parcial (Input → Evidences)

### Sprint 1-2 (Semanas 2-3): Engines Core

**Objetivo:** Syndrome detection + Next steps

**Tasks:**
```
[ ] 1. Syndrome Engine (03_syndromes)
    - Combine logic (ALL/ANY/NEGATIVE)
    - Confidence mapping (C0/C1/C2)
    - Teste: 35 síndromes

[ ] 2. Missingness Handler (05_missingness)
    - Always-output design
    - Proxy logic (inferência)

[ ] 3. Route Policy (06_route)
    - Precedence (critical > priority > routine)
    - Conflicts resolution
    - Route SHA256

[ ] 4. Next Steps Engine (09_next_steps)
    - Triggers (54 triggers)
    - Gating rules
    - Prioritização (impact, cost, turnaround)

[ ] 5. Testes de integração
    - Pipeline completo (Input → Output)
    - 50 casos de teste
```

**Entregável:** Pipeline end-to-end (sem WORM log)

### Sprint 3 (Semana 4): Output + Auditoria

**Objetivo:** CDSS completo + WORM log

**Tasks:**
```
[ ] 1. Output Templates (04_output)
    - Renderer Markdown/HTML/JSON
    - Microcopy (léxico controlado)
    - Validator (regex para linguagem proibida)

[ ] 2. Output Policies (12_output_policies)
    - Card selection (hierarchical)
    - Gating engine
    - Borderline rules

[ ] 3. WORM Log (08_wormlog)
    - Writer append-only (JSONL)
    - HMAC-SHA256 signing
    - PostgreSQL TimescaleDB

[ ] 4. Case State (11_case_state)
    - State machine (OPEN → WAITING → CLOSED)
    - Transitions + timeouts

[ ] 5. Red List validation
    - 240 casos críticos
    - FN críticos = 0 obrigatório
```

**Entregável:** Sistema completo funcional

### Sprint 4 (Semana 5): Calibration + Performance

**Objetivo:** Otimização e retrospectiva

**Tasks:**
```
[ ] 1. Retrospectiva 500 casos IDOR-SP
    - Sensibilidade/especificidade
    - Alert burden (<50/1000)

[ ] 2. Platt Calibration (10_runbook)
    - torch.nn (logistic sigmoid)
    - Validation hold-out
    - ECE <0.05

[ ] 3. Performance tuning
    - P99 latency <5s
    - Batch processing (1000 casos/hora)

[ ] 4. Documentação técnica
    - API docs (OpenAPI)
    - Architecture decision records
    - Developer guide

[ ] 5. IFU Draft
    - Instruções de uso
    - CDSS disclaimer
    - Limitações conhecidas
```

**Entregável:** Sistema production-ready

### Timeline Visual

```
Semana 1       Semana 2-3     Semana 4       Semana 5
───────────────────────────────────────────────────────
[Sprint 0]     [Sprint 1-2]   [Sprint 3]     [Sprint 4]
   Setup    →   Core Engines → Output+Audit → Calibration
   Parser       Syndrome       WORM Log       Retrospect
   Evidence     Next Steps     Red List       Performance
```

### Recursos Necessários

**Equipe:**
- 2 Backend Engineers (full-time, 4 semanas)
- 1 QA Engineer (full-time, 4 semanas)
- Dr. Abel Costa (part-time, 10h/semana)

**Infra:**
- Docker + Docker Compose
- PostgreSQL 15 (8GB RAM, 100GB storage)
- Redis (opcional, cache)
- GitHub Actions (CI/CD)

**Dados:**
- 240 casos Red List (críticos FN=0)
- 500 casos retrospectivos IDOR-SP
- 100 casos prospectivos (opcional)

---

## 5️⃣ Q&A ANTECIPADO (10 min)

### P1: Por que não usar scikit-learn?

**R:** Requisito do runbook v2.3.1

```yaml
# 10_runbook_hybrid.yaml
calibration:
  toolchain:
    logistic_platt: "torch.nn (sigmoid)"
    isotonic: "numpy/sympy"  # ❌ SEM scikit-learn
```

**Razão:** Reduzir dependências, usar apenas PyTorch

### P2: Como garantir FN críticos = 0?

**R:** Red List + CI/CD blocking

```python
# tests/e2e/test_red_list.py
@pytest.mark.critical
def test_red_list_fn_zero():
    """
    ⚠️ BLOQUEANTE: Se falhar, merge é impedido.
    """
    red_list = load_red_list_cases()  # 240 casos
    
    for case in red_list:
        result = pipeline.process(case['input'])
        
        # Verificar que síndrome crítica foi detectada
        detected = any(
            s['id'] == case['expected_syndrome']
            for s in result['syndromes']
        )
        
        assert detected, f"❌ FN crítico: {case['id']} não detectado"
```

**CI/CD:**
```yaml
# .github/workflows/ci.yml
- name: Red List (CRITICAL)
  run: pytest tests/e2e/test_red_list.py -v
  continue-on-error: false  # ❌ Bloqueia merge se falhar
```

### P3: Como funciona o WORM log?

**R:** Append-only JSONL + HMAC + Hash chain

```python
# Estrutura do log
{
  "event_id": "uuid4",           # Idempotência
  "event_ts": "2025-10-19T21:00:00Z",
  "case_id_hash": "sha256:...",  # LGPD (pseudonimização)
  "route_id": "sha256:...",      # Determinístico
  "fired_evidences": ["E-HB-HIGH", "E-HCT-HIGH"],
  "top_syndromes": [{"id": "S-PV", "confidence": "C1"}],
  "engine_versions": "v2.3.1",
  "config_hash": "sha256:...",
  "code_hash": "sha256:...",
  "previous_segment_hash": "sha256:...",  # Chain
  "hmac_signature": "hmac_sha256:..."     # Autenticidade
}
```

**Imutabilidade:**
- Append-only (nunca update/delete)
- HMAC impede adulteração
- Hash chain detecta remoção de eventos
- Retenção: 90 dias (LGPD)

### P4: Como testar localmente?

**R:** Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/hemodoctor
      REDIS_URL: redis://redis:6379
      CONFIG_PATH: /app/config/yamls
    volumes:
      - ./config/yamls:/app/config/yamls
    depends_on:
      - db
      - redis
  
  db:
    image: timescale/timescaledb:latest-pg15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: hemodoctor
    volumes:
      - db_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  db_data:
```

**Comandos:**
```bash
# Setup
docker-compose up -d

# Testar endpoint
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d @test_case_pv.json

# Ver logs
docker-compose logs -f api

# Rodar testes
docker-compose exec api pytest -v
```

### P5: Qual a prioridade de implementação?

**R:** Red List primeiro

**Prioridade 1 (CRÍTICO):**
1. Evidence Engine (02_evidence) → 79 evidências
2. Syndrome Engine (03_syndromes) → 35 síndromes
3. Red List validation → FN críticos = 0

**Prioridade 2 (HIGH):**
4. Next Steps Engine (09_next_steps) → 54 triggers
5. Output Templates (04_output) → Microcopy
6. WORM Log (08_wormlog) → Auditoria

**Prioridade 3 (MEDIUM):**
7. Calibration (10_runbook) → Platt scaling
8. Performance tuning → P99 <5s
9. Retrospectiva 500 casos

### P6: Como validar microcopy (não-diagnóstica)?

**R:** Regex + LLM opcional

```python
# src/output/microcopy.py
FORBIDDEN_PATTERNS = [
    r'\bdiagnóstico\s+de\b',
    r'\btem\s+(a|o)\s+\w+',  # "tem a doença"
    r'\bconfirma\b',
    r'\bé\s+(uma|um)\s+\w+',  # "é uma leucemia"
    r'\bcâncer\b(?!\s+suspeita)',  # "câncer" sem "suspeita"
    r'\bleucemia\b(?!\s+suspeita)',
]

def validate_microcopy(text: str) -> tuple[bool, list[str]]:
    """
    Valida que texto não usa linguagem diagnóstica.
    
    Returns:
        (is_valid, violations)
    """
    violations = []
    
    for pattern in FORBIDDEN_PATTERNS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            violations.append(f"Proibido: '{pattern}' encontrado")
    
    return len(violations) == 0, violations

# Teste
@pytest.mark.parametrize("text,should_pass", [
    ("Padrão compatível com anemia ferropriva (C1)", True),
    ("Diagnóstico de anemia ferropriva", False),
    ("Paciente tem leucemia", False),
    ("Suspeita de leucemia", True),
])
def test_microcopy_validation(text, should_pass):
    valid, _ = validate_microcopy(text)
    assert valid == should_pass
```

---

## 📦 MATERIAL DE APOIO

### Arquivos Essenciais para Devs

**Leitura OBRIGATÓRIA (2 horas):**

1. `GUIA_COMPLETO_POS_IMPLEMENTACAO_v2.3.1.md` (20 min)
   - Estrutura do repositório
   - Pipeline completo
   - Instruções de uso

2. `RELATORIO_IMPLEMENTACAO_v2.3.1_FINAL.md` (15 min)
   - Correções críticas (antes/depois)
   - Patches aplicados

3. `RELATORIO_MODULOS_CDSS_v2.3.1.md` (10 min)
   - Microcopy segura
   - Gating inteligente

4. **YAMLs (1 hora):**
   - `00_config_hybrid.yaml` — Cutoffs, unidades
   - `02_evidence_hybrid.yaml` — 79 evidências
   - `03_syndromes_hybrid.yaml` — 35 síndromes
   - `09_next_steps_engine_hybrid.yaml` — 54 triggers

### Quick Start para Devs

```bash
# 1. Clone repo
git clone <repo-url>
cd HemoDoctor/docs
git checkout feature/hemodoctor-hibrido-v1.0

# 2. Explorar YAMLs
cd HEMODOCTOR_HIBRIDO_V1.0/YAMLs
ls -lh *.yaml

# 3. Validar YAML syntax
python3 -c "import yaml; [yaml.safe_load(open(f)) for f in [...]]"

# 4. Ler documentação
cd ..
open GUIA_COMPLETO_POS_IMPLEMENTACAO_v2.3.1.md
```

### Recursos Adicionais

**GitHub:**
- Repo: (fornecer URL)
- Branch: `feature/hemodoctor-hibrido-v1.0`
- Commit: `92662f0` (feat v2.3.1 + CDSS)

**Documentação Online:**
- LOINC: https://loinc.org/
- WHO 2016 PV criteria: (fornecer ref)
- ANVISA RDC 657/2022: (fornecer link)

**Contatos:**
- Dr. Abel Costa (IDOR-SP): abel@idor.org
- AI Medical Device Specialist: (contexto)

---

## 🎯 PRÓXIMOS PASSOS IMEDIATOS

### Após este Briefing (Hoje)

1. ✅ **Acesso ao Repositório**
   - Todos os devs clonarem repo
   - Verificar acesso aos YAMLs

2. ✅ **Leitura Obrigatória** (2h)
   - Guia completo
   - Relatórios técnicos
   - YAMLs principais

3. ✅ **Setup Local** (1h)
   - Docker + Docker Compose
   - Python 3.11+, Poetry
   - VSCode/PyCharm

### Segunda-Feira (Sprint 0 Kickoff)

1. **Planning Sprint 0** (2h)
   - Divisão de tasks
   - Definition of Done
   - Estimativas

2. **Spike Técnico** (4h)
   - Parser YAML → Pydantic
   - Evidence engine POC
   - Teste 5 evidências

3. **Daily Standup** (15 min/dia)
   - O que foi feito
   - O que será feito
   - Bloqueadores

---

## 📊 CRITÉRIOS DE SUCESSO

### Sprint 0 (Semana 1)
- [ ] Repo setup completo (Docker, CI/CD)
- [ ] Parser YAML funcional (10 YAMLs)
- [ ] Evidence engine: 10 evidências testadas
- [ ] Coverage ≥60%

### Sprint 1-2 (Semanas 2-3)
- [ ] Syndrome engine: 35 síndromes implementadas
- [ ] Next steps: 54 triggers funcionais
- [ ] Pipeline end-to-end: Input → Output
- [ ] 50 casos de teste passando

### Sprint 3 (Semana 4)
- [ ] CDSS completo (templates + policies)
- [ ] WORM log funcional (HMAC + chain)
- [ ] **Red List: FN críticos = 0** ⚠️
- [ ] 240 casos críticos validados

### Sprint 4 (Semana 5)
- [ ] Retrospectiva: 500 casos IDOR-SP
- [ ] Calibration: ECE <0.05
- [ ] Performance: P99 <5s
- [ ] Documentação técnica completa

---

## 🎉 CONCLUSÃO

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║     HemoDoctor Hybrid v2.3.1 + CDSS               ║
║                                                   ║
║  ✅ 35 síndromes, 79 evidências                   ║
║  ✅ 3 erros críticos CORRIGIDOS                   ║
║  ✅ Microcopy segura não-diagnóstica              ║
║  ✅ Pipeline completo especificado                ║
║  ✅ Roadmap 4 semanas definido                    ║
║                                                   ║
║     🚀 PRONTO PARA IMPLEMENTAÇÃO 🚀               ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

**Perguntas?**

---

**Apresentado por:** Dr. Abel Costa + AI Medical Device Specialist  
**Data:** 19 de Outubro de 2025  
**Duração:** 60 minutos  
**Next Meeting:** Sprint 0 Planning (Segunda-feira)

---

**FIM DO BRIEFING**

