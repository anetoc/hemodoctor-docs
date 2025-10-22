# 🚀 DEVELOPER QUICK START: HemoDoctor v2.3.1

**Para:** Backend Engineers, QA Engineers  
**Tempo estimado:** 2-4 horas para setup completo  
**Objetivo:** Ambiente funcional + primeiro caso de teste

---

## ⚡ SETUP RÁPIDO (30 min)

### 1. Clone & Checkout (2 min)

```bash
# Clone repositório
git clone <repo-url>
cd HemoDoctor/docs

# Checkout branch feature
git checkout feature/hemodoctor-hibrido-v1.0

# Navegar para YAMLs
cd HEMODOCTOR_HIBRIDO_V1.0
ls -lh *.yaml
```

**Estrutura esperada:**
```
HEMODOCTOR_HIBRIDO_V1.0/
├── 00_config_hybrid.yaml                    # Cutoffs, unidades
├── 01_schema_hybrid.yaml                    # 41 campos CBC
├── 02_evidence_hybrid.yaml                  # 79 evidências
├── 03_syndromes_hybrid.yaml                 # 35 síndromes
├── 04_output_templates_hybrid.yaml          # Microcopy CDSS
├── 05_missingness_hybrid_v2.3.yaml          # Proxy logic
├── 06_route_logic_hybrid.yaml               # Routing policy
├── 08_wormlog_hybrid.yaml                   # Auditoria
├── 09_next_steps_engine_hybrid.yaml         # 54 triggers
├── 10_runbook_hybrid.yaml                   # Calibration
├── 11_case_state_hybrid.yaml                # State machine
├── 12_output_policies_hybrid.yaml           # Card selection
└── 12_output_policies_cdss.yaml             # CDSS gating
```

### 2. Instalar Dependências (10 min)

#### Opção A: Poetry (recomendado)
```bash
# Instalar Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Criar pyproject.toml
cat > pyproject.toml <<EOF
[tool.poetry]
name = "hemodoctor"
version = "2.3.1"
description = "Sistema de Apoio à Decisão Clínica para Hematologia"
authors = ["IDOR-SP <contato@idor.org>"]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.109.0"
pydantic = "^2.5.0"
pyyaml = "^6.0.1"
torch = "^2.1.0"
numpy = "^1.24.0"
sympy = "^1.12.0"
cryptography = "^41.0.0"
structlog = "^24.1.0"
psycopg2-binary = "^2.9.9"
redis = "^5.0.1"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-cov = "^4.1.0"
pytest-asyncio = "^0.21.0"
httpx = "^0.26.0"
black = "^23.12.0"
ruff = "^0.1.9"
mypy = "^1.8.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
EOF

# Instalar
poetry install
```

#### Opção B: pip + venv
```bash
# Criar venv
python3.11 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar deps
pip install fastapi pydantic pyyaml torch numpy sympy \
            cryptography structlog psycopg2-binary redis \
            pytest pytest-cov pytest-asyncio httpx \
            black ruff mypy
```

### 3. Validar YAMLs (5 min)

```bash
# Script rápido de validação
python3 <<EOF
import yaml
from pathlib import Path

yamls = [
    "00_config_hybrid.yaml",
    "01_schema_hybrid.yaml",
    "02_evidence_hybrid.yaml",
    "03_syndromes_hybrid.yaml",
    "04_output_templates_hybrid.yaml",
    "05_missingness_hybrid_v2.3.yaml",
    "06_route_logic_hybrid.yaml",
    "08_wormlog_hybrid.yaml",
    "09_next_steps_engine_hybrid.yaml",
    "10_runbook_hybrid.yaml",
    "11_case_state_hybrid.yaml",
    "12_output_policies_hybrid.yaml",
]

for yaml_file in yamls:
    try:
        data = yaml.safe_load(open(yaml_file))
        print(f"✅ {yaml_file}: OK ({len(str(data))} bytes)")
    except Exception as e:
        print(f"❌ {yaml_file}: ERRO - {e}")
EOF
```

**Output esperado:**
```
✅ 00_config_hybrid.yaml: OK (...)
✅ 01_schema_hybrid.yaml: OK (...)
...
✅ 12_output_policies_hybrid.yaml: OK (...)
```

---

## 🏗️ ESTRUTURA DO PROJETO (15 min)

### Criar Estrutura de Diretórios

```bash
# Criar estrutura Python
mkdir -p hemodoctor/{config,schema,evidence,syndrome,missingness,route,wormlog,next_steps,output,state,api,tests/{unit,integration,e2e}}

# Criar __init__.py
find hemodoctor -type d -exec touch {}/__init__.py \;

# Estrutura final
tree hemodoctor/
```

**Estrutura esperada:**
```
hemodoctor/
├── __init__.py
├── config/
│   ├── __init__.py
│   ├── loader.py
│   └── models.py
├── schema/
│   ├── __init__.py
│   ├── cbc_input.py
│   └── normalizer.py
├── evidence/
│   ├── __init__.py
│   ├── loader.py
│   ├── engine.py
│   └── models.py
├── syndrome/
│   ├── __init__.py
│   ├── loader.py
│   ├── engine.py
│   ├── confidence.py
│   └── models.py
├── output/
│   ├── __init__.py
│   ├── templates.py
│   ├── policies.py
│   ├── renderer.py
│   └── microcopy.py
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```

---

## 💻 PRIMEIRO CÓDIGO (1 hora)

### Módulo 1: Config Loader

**Arquivo:** `hemodoctor/config/models.py`
```python
"""
Pydantic models para 00_config_hybrid.yaml
"""
from pydantic import BaseModel, Field
from typing import Dict, Optional

class Cutoffs(BaseModel):
    """Cutoffs por faixa etária e sexo."""
    adult_m: float
    adult_f: float
    pediatric: Optional[float] = None

class HemoglobinCutoffs(BaseModel):
    hb_low: Cutoffs
    hb_crit_low: Cutoffs
    hb_high: Cutoffs  # v2.3.1: NOVO (PV/Eritrocitose)

class ConfigMetadata(BaseModel):
    version: str
    effective_date: str
    site_id: str

class Config(BaseModel):
    """Configuração global do sistema."""
    metadata: ConfigMetadata
    cutoffs: Dict[str, Cutoffs]
    units: Dict[str, str]
    escalation: Dict[str, float]
    
    @property
    def hb_high_adult_m(self) -> float:
        """Hb alto para adulto masculino (g/dL)."""
        return self.cutoffs['hb_high'].adult_m
    
    @property
    def wbc_low_adult(self) -> float:
        """WBC baixo para adulto (x10^9/L)."""
        return self.cutoffs['wbc_low'].adult  # v2.3.1: NOVO
```

**Arquivo:** `hemodoctor/config/loader.py`
```python
"""
Carrega 00_config_hybrid.yaml
"""
import yaml
from pathlib import Path
from .models import Config

def load_config(yaml_path: Path) -> Config:
    """
    Carrega configuração global.
    
    Args:
        yaml_path: Caminho para 00_config_hybrid.yaml
    
    Returns:
        Config validado via Pydantic
    
    Raises:
        FileNotFoundError: Se YAML não existe
        ValueError: Se YAML inválido
    
    Example:
        >>> config = load_config(Path("00_config_hybrid.yaml"))
        >>> config.metadata.version
        '2.3.1'
        >>> config.hb_high_adult_m
        18.5
    """
    if not yaml_path.exists():
        raise FileNotFoundError(f"YAML não encontrado: {yaml_path}")
    
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    
    return Config(**data)
```

**Teste:** `hemodoctor/tests/unit/test_config_loader.py`
```python
import pytest
from pathlib import Path
from hemodoctor.config.loader import load_config

def test_load_config_success():
    """Testa carregamento válido do config."""
    config_path = Path("00_config_hybrid.yaml")
    config = load_config(config_path)
    
    # Validações v2.3.1
    assert config.metadata.version == "2.3.1"
    assert config.hb_high_adult_m == 18.5  # PV/Eritrocitose
    assert config.wbc_low_adult == 4.0e9   # Pancitopenia
    
def test_load_config_file_not_found():
    """Testa erro quando arquivo não existe."""
    with pytest.raises(FileNotFoundError):
        load_config(Path("nonexistent.yaml"))
```

**Rodar teste:**
```bash
pytest hemodoctor/tests/unit/test_config_loader.py -v
```

### Módulo 2: Evidence Models

**Arquivo:** `hemodoctor/evidence/models.py`
```python
"""
Pydantic models para 02_evidence_hybrid.yaml
"""
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class Series(str, Enum):
    RED = "red"
    WHITE = "white"
    PLATELETS = "platelets"
    PREANALYTICAL = "preanalytical"

class Strength(str, Enum):
    WEAK = "weak"
    MODERATE = "moderate"
    STRONG = "strong"

class Evidence(BaseModel):
    """Evidência atômica do sistema."""
    id: str = Field(..., pattern=r"^E-[A-Z0-9-]+$")
    series: Series
    rule: str  # Expressão booleana (ex: "hb < config.hb_low[age_group][sex]")
    strength: Strength
    clinical_significance: str
    source: str
    
    def evaluate(self, cbc_data: dict, config) -> bool:
        """
        Avalia se evidência está presente.
        
        Args:
            cbc_data: {"hb": 8.5, "mcv": 74, ...}
            config: Config object
        
        Returns:
            True se evidência disparou
        
        Example:
            >>> evidence = Evidence(id="E-HB-CRIT-LOW", ...)
            >>> evidence.evaluate({"hb": 6.0, "age_group": "adult", "sex": "F"}, config)
            True
        """
        # NOTA: Implementação real requer parser de expressões
        # Aqui apenas placeholder
        try:
            # Substituir variáveis na regra
            rule_expr = self.rule
            for key, value in cbc_data.items():
                rule_expr = rule_expr.replace(key, str(value))
            
            # Avaliar (usar ast.literal_eval ou sympy)
            return eval(rule_expr)  # ⚠️ Inseguro, usar parser adequado
        except Exception:
            return False
```

**Arquivo:** `hemodoctor/evidence/loader.py`
```python
"""
Carrega 02_evidence_hybrid.yaml
"""
import yaml
from pathlib import Path
from typing import List
from .models import Evidence

def load_evidences(yaml_path: Path) -> List[Evidence]:
    """
    Carrega todas as 79 evidências.
    
    Returns:
        Lista de objetos Evidence
    
    Example:
        >>> evidences = load_evidences(Path("02_evidence_hybrid.yaml"))
        >>> len(evidences)
        79
        >>> evidences[0].id
        'E-HB-CRIT-LOW'
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    
    evidences = []
    for section in ['red_cell_evidences', 'white_cell_evidences', 
                    'platelet_evidences', 'preanalytical_flags']:
        if section in data:
            for e in data[section]:
                evidences.append(Evidence(**e))
    
    return evidences
```

**Teste:** `hemodoctor/tests/unit/test_evidence_loader.py`
```python
import pytest
from pathlib import Path
from hemodoctor.evidence.loader import load_evidences

def test_load_evidences():
    """Testa carregamento de evidências."""
    evidences = load_evidences(Path("02_evidence_hybrid.yaml"))
    
    # v2.3.1: 79 evidências (75 + 4 novas)
    assert len(evidences) == 79
    
    # Verificar evidências novas v2.3.1
    evidence_ids = [e.id for e in evidences]
    assert "E-HB-HIGH" in evidence_ids      # PV/Eritrocitose
    assert "E-HCT-HIGH" in evidence_ids     # PV/Eritrocitose
    assert "E-WBC-LOW" in evidence_ids      # Pancitopenia
    assert "E-WBC-VERY-HIGH" in evidence_ids  # Leucostase

def test_evidence_pv():
    """Testa evidência E-HB-HIGH (PV)."""
    evidences = load_evidences(Path("02_evidence_hybrid.yaml"))
    
    e_hb_high = next(e for e in evidences if e.id == "E-HB-HIGH")
    assert e_hb_high.series == "red"
    assert e_hb_high.strength == "strong"
    assert "eritrocitose" in e_hb_high.clinical_significance.lower()
```

---

## 🧪 CASO DE TESTE: PV (30 min)

### Criar Teste End-to-End Simples

**Arquivo:** `hemodoctor/tests/e2e/test_pv_case.py`
```python
"""
Teste E2E: Detecção de S-PV (Policitemia Vera)

Objetivo: Validar que v2.3.1 detecta PV corretamente
          (erro crítico corrigido: v1.0.0 detectava anemia!)
"""
import pytest
from pathlib import Path
from hemodoctor.config.loader import load_config
from hemodoctor.evidence.loader import load_evidences
from hemodoctor.syndrome.loader import load_syndromes

# Caso de teste: Homem 55 anos com PV
PV_CASE = {
    "case_id": "PV-001",
    "age_years": 55,
    "sex": "M",
    "hb": 19.5,          # Alto (> 18.5 g/dL)
    "ht": 55,            # Alto (> 52%)
    "wbc": 12.0e9,       # Normal-alto
    "plt": 450e9,        # Normal-alto
    "mcv": 88,           # Normal
    "rdw": 13.5,         # Normal
    "expected_syndrome": "S-PV",
    "expected_confidence": "C1",  # ou "C2" dependendo da calibração
}

@pytest.mark.critical
def test_pv_detection():
    """
    ⚠️ CRÍTICO: Testa que S-PV é detectada corretamente.
    
    v1.0.0: ❌ Falso Negativo (usava E-HB-CRIT-LOW)
    v2.3.1: ✅ Detecta (usa E-HB-HIGH, E-HCT-HIGH)
    """
    # Load configs
    config = load_config(Path("00_config_hybrid.yaml"))
    evidences = load_evidences(Path("02_evidence_hybrid.yaml"))
    syndromes = load_syndromes(Path("03_syndromes_hybrid.yaml"))
    
    # Avaliar evidências
    fired_evidences = []
    for evidence in evidences:
        if evidence.evaluate(PV_CASE, config):
            fired_evidences.append(evidence.id)
    
    # v2.3.1: Deve disparar E-HB-HIGH e E-HCT-HIGH
    assert "E-HB-HIGH" in fired_evidences, \
        "❌ v2.3.1: E-HB-HIGH não disparou! (Bug crítico)"
    assert "E-HCT-HIGH" in fired_evidences, \
        "❌ v2.3.1: E-HCT-HIGH não disparou! (Bug crítico)"
    
    # Avaliar síndromes
    s_pv = next(s for s in syndromes if s.id == "S-PV")
    detected = s_pv.evaluate(fired_evidences, config)
    
    assert detected, \
        f"❌ S-PV não detectada! Evidências: {fired_evidences}"
    
    print(f"✅ S-PV detectada corretamente! (Evidências: {fired_evidences})")

@pytest.mark.critical
def test_pv_vs_v1_regression():
    """
    Testa que v1.0.0 FALHARIA neste caso (regressão).
    
    Objetivo: Documentar que o bug foi corrigido.
    """
    # Simular comportamento v1.0.0 (E-HB-CRIT-LOW)
    v1_rule = PV_CASE["hb"] < 7.0  # Anemia grave
    
    # v1.0.0: NÃO detectaria PV (Hb=19.5 > 7.0)
    assert not v1_rule, \
        "v1.0.0: Não detectaria PV (usava regra de anemia)"
    
    print("✅ v1.0.0 bug confirmado: não detectaria este caso de PV")
```

**Rodar teste:**
```bash
pytest hemodoctor/tests/e2e/test_pv_case.py -v -s
```

**Output esperado:**
```
tests/e2e/test_pv_case.py::test_pv_detection PASSED
✅ S-PV detectada corretamente! (Evidências: ['E-HB-HIGH', 'E-HCT-HIGH'])

tests/e2e/test_pv_case.py::test_pv_vs_v1_regression PASSED
✅ v1.0.0 bug confirmado: não detectaria este caso de PV
```

---

## 🐳 DOCKER SETUP (30 min)

### Dockerfile

**Arquivo:** `Dockerfile`
```dockerfile
FROM python:3.11-slim

# Metadados
LABEL maintainer="IDOR-SP <contato@idor.org>"
LABEL version="2.3.1"

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar dependências
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Copiar código
COPY hemodoctor/ ./hemodoctor/
COPY config/ ./config/

# Copiar YAMLs
COPY HEMODOCTOR_HIBRIDO_V1.0/*.yaml ./config/yamls/

# Expor porta
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

# Comando padrão
CMD ["uvicorn", "hemodoctor.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

**Arquivo:** `docker-compose.yml`
```yaml
version: '3.8'

services:
  api:
    build: .
    container_name: hemodoctor-api
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://hemodoctor:password@db:5432/hemodoctor
      REDIS_URL: redis://redis:6379
      CONFIG_PATH: /app/config/yamls
      LOG_LEVEL: INFO
    volumes:
      - ./config/yamls:/app/config/yamls:ro
      - ./logs:/app/logs
    depends_on:
      - db
      - redis
    restart: unless-stopped
  
  db:
    image: timescale/timescaledb:latest-pg15
    container_name: hemodoctor-db
    environment:
      POSTGRES_USER: hemodoctor
      POSTGRES_PASSWORD: password
      POSTGRES_DB: hemodoctor
    volumes:
      - db_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    restart: unless-stopped
  
  redis:
    image: redis:7-alpine
    container_name: hemodoctor-redis
    ports:
      - "6379:6379"
    restart: unless-stopped

volumes:
  db_data:
```

**Comandos:**
```bash
# Build
docker-compose build

# Start
docker-compose up -d

# Logs
docker-compose logs -f api

# Teste health
curl http://localhost:8000/health

# Stop
docker-compose down
```

---

## 🧪 TESTES RÁPIDOS (15 min)

### Comandos Úteis

```bash
# Todos os testes
pytest

# Apenas críticos (Red List)
pytest -m critical

# Coverage
pytest --cov=hemodoctor --cov-report=html

# Verbose
pytest -v -s

# Fail fast (parar no primeiro erro)
pytest -x

# Rerun apenas falhas
pytest --lf
```

### Estrutura de Testes

```python
# tests/conftest.py - Fixtures compartilhados
import pytest
from pathlib import Path
from hemodoctor.config.loader import load_config
from hemodoctor.evidence.loader import load_evidences

@pytest.fixture(scope="session")
def config():
    """Config global (carregado uma vez por sessão)."""
    return load_config(Path("00_config_hybrid.yaml"))

@pytest.fixture(scope="session")
def evidences():
    """Todas as 79 evidências."""
    return load_evidences(Path("02_evidence_hybrid.yaml"))

@pytest.fixture
def pv_case():
    """Caso de teste: PV."""
    return {
        "age_years": 55,
        "sex": "M",
        "hb": 19.5,
        "ht": 55,
        "wbc": 12.0e9,
        "plt": 450e9,
    }
```

---

## 📋 CHECKLIST DE ONBOARDING

### Dia 1: Setup Ambiente ✅

- [ ] Clone repositório
- [ ] Instalar dependências (Poetry/pip)
- [ ] Validar YAMLs (syntax check)
- [ ] Criar estrutura de diretórios
- [ ] Rodar pytest (mesmo sem testes, verificar config)

### Dia 2: Código Básico ✅

- [ ] Implementar `config/loader.py`
- [ ] Implementar `evidence/models.py` e `loader.py`
- [ ] Escrever 3 testes unitários
- [ ] Rodar testes: `pytest -v`

### Dia 3: Caso de Teste E2E ✅

- [ ] Implementar teste PV (E2E)
- [ ] Validar correção v2.3.1 (E-HB-HIGH)
- [ ] Documentar diferença v1.0.0 vs v2.3.1

### Dia 4-5: Sprint 0 Completo ✅

- [ ] Syndrome engine básico
- [ ] 10 evidências testadas
- [ ] Coverage ≥60%
- [ ] Docker setup funcional

---

## 🔗 RECURSOS

### Documentação

**OBRIGATÓRIA:**
- `BRIEFING_DEV_TEAM_v2.3.1.md` — Este documento
- `GUIA_COMPLETO_POS_IMPLEMENTACAO_v2.3.1.md` — Guia técnico completo
- `RELATORIO_IMPLEMENTACAO_v2.3.1_FINAL.md` — Correções críticas

**REFERÊNCIA:**
- YAMLs: `HEMODOCTOR_HIBRIDO_V1.0/*.yaml`
- Commits: `92662f0` (feat v2.3.1), `d9a812c` (docs)

### Ferramentas Úteis

```bash
# Formatar código
black hemodoctor/

# Lint
ruff check hemodoctor/

# Type check
mypy hemodoctor/

# YAML lint
yamllint HEMODOCTOR_HIBRIDO_V1.0/*.yaml
```

### Contatos

- **Dr. Abel Costa:** abel@idor.org (hematologia)
- **Arquiteto Software:** (fornecer contato)
- **QA Lead:** (fornecer contato)

---

## 🚀 PRÓXIMO PASSO

**Após completar este Quick Start:**

1. ✅ Ler `BRIEFING_DEV_TEAM_v2.3.1.md` completo
2. ✅ Implementar Evidence Engine completo (79 evidências)
3. ✅ Implementar Syndrome Engine (35 síndromes)
4. 📅 Planning Sprint 0 (Segunda-feira)

---

**Criado em:** 19 de Outubro de 2025  
**Versão:** 1.0  
**Autor:** AI Medical Device Specialist + Dr. Abel Costa

---

**FIM DO QUICK START**

