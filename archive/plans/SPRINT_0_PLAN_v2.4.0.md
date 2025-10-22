# Sprint 0: Reconstrução Código a partir dos YAMLs
## HemoDoctor Hybrid v2.4.0

**Data Início:** 20 de Outubro de 2025
**Data Fim:** 26 de Outubro de 2025 (7 dias)
**Status:** PLANEJADO
**Objetivo:** Implementar 100% do sistema a partir das especificações YAML

---

## 🎯 OBJETIVO DO SPRINT

Reconstruir completamente o código-fonte FastAPI do HemoDoctor a partir dos YAMLs v2.4.0, dado que o ZIP original está vazio (0 bytes - BUG-001).

**Entregáveis:**
1. ✅ Código Python funcional (5 módulos principais)
2. ✅ 160 testes pytest (85% coverage)
3. ✅ API FastAPI completa
4. ✅ Docker container pronto para deploy

---

## 📊 MÉTRICAS DE SUCESSO

| Métrica | Target | Atual | Status |
|---------|--------|-------|--------|
| **Modules** | 5 | 0 | ⏳ |
| **Test Coverage** | 85% | 0% | ⏳ |
| **Pass Rate** | 90% | 0% | ⏳ |
| **API Endpoints** | 4 | 0 | ⏳ |
| **YAMLs Implemented** | 16 | 16 spec | ✅ |

---

## 📁 ESTRUTURA DO PROJETO

```
hemodoctor-hybrid-v2.4.0/
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py                  # FastAPI app
│   │   ├── input_validator.py      # Schema validation
│   │   └── routes.py                # API endpoints
│   ├── engines/
│   │   ├── __init__.py
│   │   ├── evidence_engine.py      # 79 evidências
│   │   ├── syndrome_engine.py      # 35 síndromes (DAG fusion)
│   │   ├── next_steps_engine.py    # 40 triggers
│   │   └── config_loader.py        # YAML loaders
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cbc.py                  # CBC data model
│   │   ├── evidence.py             # Evidence model
│   │   ├── syndrome.py             # Syndrome model
│   │   └── next_step.py            # NextStep model
│   ├── audit/
│   │   ├── __init__.py
│   │   └── worm_logger.py          # Immutable audit log
│   └── utils/
│       ├── __init__.py
│       ├── normalization.py        # Unit conversion
│       └── age_sex_utils.py        # Age/sex groups
├── tests/
│   ├── unit/
│   │   ├── test_evidence_engine.py (79 tests)
│   │   ├── test_syndrome_engine.py (35 tests)
│   │   └── test_next_steps_engine.py (40 tests)
│   ├── integration/
│   │   ├── test_api_endpoints.py
│   │   └── test_end_to_end.py
│   └── fixtures/
│       ├── cbc_samples.yaml        # Test cases
│       └── red_list_240.yaml       # Critical cases
├── config/
│   └── YAMLs/ -> ../HEMODOCTOR_HIBRIDO_V1.0/YAMLs/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── requirements.txt
├── pytest.ini
├── README.md
└── .env.example
```

---

## 📅 CRONOGRAMA DETALHADO

### **Dia 1-2 (20-21 Out): Setup + Core Infrastructure**

**Objetivo:** Projeto base + validação de entrada

**Tarefas:**
- [ ] Criar estrutura de diretórios
- [ ] Setup Python 3.11+ + venv
- [ ] Criar requirements.txt:
  ```
  fastapi==0.104.1
  uvicorn[standard]==0.24.0
  pydantic==2.5.0
  pyyaml==6.0.1
  simpleeval==0.9.13
  pytest==7.4.3
  pytest-cov==4.1.0
  python-dateutil==2.8.2
  cryptography==41.0.7
  ```
- [ ] Implementar `config_loader.py`:
  - Carregar todos os 16 YAMLs
  - Validar sintaxe
  - Cache configs em memória
- [ ] Implementar `input_validator.py`:
  - Schema validation (01_schema_hybrid.yaml)
  - Type checking (42 campos)
  - Range validation
  - Missing data detection
- [ ] Setup pytest + fixtures básicos

**Entregável:** Projeto base + validação entrada funcionando

---

### **Dia 3-4 (22-23 Out): Evidence + Syndrome Engines**

**Objetivo:** Motores principais de decisão

**Tarefas:**

#### Evidence Engine (79 evidências)
- [ ] Implementar `evidence_engine.py`:
  ```python
  def evaluate_evidences(cbc: dict, config: dict) -> List[Evidence]:
      """Avalia todas as 79 evidências"""
      evidences = []
      for category in config['evidence_categories']:
          for evidence_def in category['evidences']:
              status = evaluate_single_evidence(
                  evidence_def['rule'],
                  cbc,
                  config
              )
              evidences.append(Evidence(
                  id=evidence_def['id'],
                  status=status,  # present/absent/unknown
                  strength=evidence_def['strength'],
                  clinical_significance=evidence_def['clinical_significance']
              ))
      return evidences
  ```
- [ ] Usar **simpleeval** (NUNCA eval() direto)
- [ ] Handle missing data → status="unknown"
- [ ] 79 unit tests (1 por evidência)

#### Syndrome Engine (35 síndromes)
- [ ] Implementar `syndrome_engine.py`:
  ```python
  def fuse_syndromes(evidences: List[Evidence], config: dict) -> List[Syndrome]:
      """DAG fusion com short-circuit para critical"""
      syndromes = []
      evidence_ids = {e.id for e in evidences if e.status == 'present'}

      # Ordenar por criticidade (critical first)
      sorted_defs = sorted(
          config['syndromes'],
          key=lambda s: (s['criticality'] != 'critical', s['id'])
      )

      for syndrome_def in sorted_defs:
          if matches_syndrome(syndrome_def, evidence_ids):
              syndrome = Syndrome(
                  id=syndrome_def['id'],
                  criticality=syndrome_def['criticality'],
                  evidences=[e for e in evidences if e.id in syndrome_def['combine']]
              )
              syndromes.append(syndrome)

              # Short-circuit se critical
              if syndrome.criticality == 'critical':
                  break

      return syndromes
  ```
- [ ] Lógica ALL/ANY/NEGATIVE + threshold
- [ ] Short-circuit para critical
- [ ] 35 unit tests (1 por síndrome)

**Entregável:** Engines funcionando + 114 testes (79 + 35)

---

### **Dia 5-6 (24-25 Out): Next Steps + WORM + API**

**Objetivo:** Recomendações clínicas + auditoria + API

**Tarefas:**

#### Next Steps Engine
- [ ] Implementar `next_steps_engine.py`:
  ```python
  def recommend_next_steps(
      syndromes: List[Syndrome],
      cbc: dict,
      config: dict
  ) -> List[NextStep]:
      """Avalia 40 triggers e retorna recomendações priorizadas"""
      next_steps = []

      for trigger_def in config['triggers']:
          # Avaliar condição "when"
          if evaluate_when_condition(trigger_def['when'], syndromes, cbc):
              for suggestion in trigger_def['suggest']:
                  next_steps.append(NextStep(
                      level=suggestion['level'],
                      test=suggestion['test'],
                      rationale=suggestion['rationale'],
                      cost=suggestion['cost'],
                      turnaround=suggestion['turnaround']
                  ))

      # Priorizar: critical > priority > routine
      next_steps.sort(key=lambda ns: PRIORITY_ORDER[ns.level])
      return next_steps
  ```
- [ ] 40 unit tests (1 por trigger)

#### WORM Logger
- [ ] Implementar `worm_logger.py`:
  - Append-only log (JSONL)
  - HMAC-SHA256 signature
  - Pseudonymization (SHA256 hashing)
  - Zero PHI in logs
  - Retention: 1825 dias (5 anos)
- [ ] Integration tests

#### FastAPI
- [ ] Implementar `main.py` + `routes.py`:
  ```python
  @app.post("/api/v1/analyze")
  async def analyze_cbc(cbc_input: CBCInput) -> CBCAnalysisResponse:
      # 1. Validate input
      cbc = validate_input(cbc_input)

      # 2. Evaluate evidences
      evidences = evaluate_evidences(cbc, config)

      # 3. Fuse syndromes
      syndromes = fuse_syndromes(evidences, config)

      # 4. Recommend next steps
      next_steps = recommend_next_steps(syndromes, cbc, config)

      # 5. Log to WORM
      log_id = worm_logger.log_analysis(cbc, evidences, syndromes)

      # 6. Return response
      return CBCAnalysisResponse(
          route_id=generate_route_id(evidences, syndromes),
          syndromes=syndromes,
          next_steps=next_steps,
          worm_log_id=log_id
      )
  ```
- [ ] Endpoints:
  - POST /api/v1/analyze
  - GET /api/v1/health
  - GET /api/v1/version
  - POST /api/v1/audit/verify
- [ ] Integration tests
- [ ] Swagger docs auto-gerado

**Entregável:** Sistema completo funcionando + 160 testes

---

### **Dia 7 (26 Out): Testing + Docker + Docs**

**Objetivo:** Validação final + deploy ready

**Tarefas:**
- [ ] Coverage report (target 85%):
  ```bash
  pytest --cov=src --cov-report=html --cov-report=term
  ```
- [ ] Fix tests até pass rate ≥90%
- [ ] Dockerfile:
  ```dockerfile
  FROM python:3.11-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY src/ ./src/
  COPY config/ ./config/
  CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- [ ] docker-compose.yml
- [ ] README.md:
  - Setup instructions
  - API documentation
  - Running tests
  - Deployment
- [ ] Sprint 0 Review:
  - Demo para stakeholders
  - Retrospectiva
  - Planning Sprint 1

**Entregável:** Sistema containerizado + documentação completa

---

## 🧪 ESTRATÉGIA DE TESTES

### Unit Tests (154 testes)

**Evidence Engine:** 79 testes
```python
def test_evidence_E_ANC_CRIT():
    cbc = {'anc': 0.3}
    config = load_config()
    evidences = evaluate_evidences(cbc, config)
    assert 'E-ANC-CRIT' in [e.id for e in evidences if e.status == 'present']
```

**Syndrome Engine:** 35 testes
```python
def test_syndrome_S_TMA():
    evidences = [
        Evidence(id='E-SCHISTOCYTES-GE1PCT', status='present'),
        Evidence(id='E-PLT-CRIT-LOW', status='present')
    ]
    syndromes = fuse_syndromes(evidences, config)
    assert 'S-TMA' in [s.id for s in syndromes]
    assert syndromes[0].criticality == 'critical'
```

**Next Steps Engine:** 40 testes
```python
def test_trigger_tma_urgent():
    syndrome = Syndrome(id='S-TMA', criticality='critical')
    next_steps = recommend_next_steps([syndrome], {}, config)
    assert next_steps[0].level == 'urgent'
    assert 'Blood smear' in next_steps[0].test
```

### Integration Tests (6 testes)

- **test_end_to_end_critical:** Caso TMA completo
- **test_end_to_end_priority:** Caso IDA completo
- **test_end_to_end_routine:** Caso normal completo
- **test_api_health:** Health check
- **test_api_analyze:** POST /analyze
- **test_worm_log_integrity:** HMAC verification

### Red List Prep (240 casos)

Preparar casos para Sprint 4:
- 40 casos × 8 síndromes críticas
- Adjudicação cega (2 hematologistas)
- FN=0 validation

---

## 🛡️ REQUISITOS DE SEGURANÇA

### Input Validation
- ✅ **NUNCA usar eval() direto** → sempre simpleeval
- ✅ Validar ranges numéricos
- ✅ Sanitizar strings
- ✅ Rate limiting: 1000 req/hour

### Data Protection
- ✅ Pseudonymization: SHA256(patient_id)
- ✅ Zero PHI in logs
- ✅ WORM log HMAC-SHA256
- ✅ Retention: 1825 dias

### Compliance
- ✅ ANVISA RDC 657/2022
- ✅ FDA 21 CFR Part 11
- ✅ ISO 13485:2016
- ✅ LGPD Art. 16

---

## ⚡ PERFORMANCE TARGETS

| Métrica | Target | Como Medir |
|---------|--------|------------|
| **Latency (p95)** | <100ms | wrk benchmark |
| **Throughput** | >1000 cases/hour | Locust load test |
| **Concurrency** | 50 simultaneous | wrk -c 50 |
| **Memory** | <512MB | Docker stats |

---

## 📚 MATERIAIS DE REFERÊNCIA

**YAMLs v2.4.0:**
- `/Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_HIBRIDO_V1.0/YAMLs/`

**Excel Completo:**
- `HEMODOCTOR_REGRAS_COMPLETAS_v2.4.0.xlsx` (34 KB)

**Documentação Técnica:**
- `ESPECIFICACAO_TECNICA_DEV_TEAM_v2.4.0.md` (8 KB)

**Documentação Clínica:**
- `VALIDACAO_CLINICA_HEMATOLOGISTA_v2.4.0.md` (61 KB)

**Quickstart:**
- `HEMODOCTOR_HIBRIDO_V1.0/QUICKSTART_IMPLEMENTACAO.md`

**Runbook:**
- `HEMODOCTOR_HIBRIDO_V1.0/YAMLs/10_runbook_hybrid.yaml`

---

## 🎯 DEFINITION OF DONE

Sprint 0 está COMPLETO quando:

- [ ] ✅ Todos os 5 módulos implementados
- [ ] ✅ 160 testes pytest passando (≥90% pass rate)
- [ ] ✅ Coverage ≥85%
- [ ] ✅ API FastAPI funcionando (4 endpoints)
- [ ] ✅ Dockerfile + docker-compose prontos
- [ ] ✅ README.md completo
- [ ] ✅ WORM logger com HMAC funcionando
- [ ] ✅ Zero security vulnerabilities (Bandit scan)
- [ ] ✅ Demo aprovada pelo Product Owner

---

## 🚀 PRÓXIMOS SPRINTS

### Sprint 1 (27 Out-9 Nov): Security Testing
- Penetration testing
- Input fuzzing
- OWASP Top 10 validation
- IEC 62304 §7 compliance

### Sprint 4 (23 Nov-6 Dez): Red List FN=0
- 240 casos críticos
- Adjudicação cega (2 hematologistas)
- FN=0 validation
- CLIN-VAL-002 report

### Release V1.0 (30 Nov): ANVISA Submission
- Compliance ≥98%
- Pass rate ≥90%
- Coverage ≥85%
- Red List FN=0 garantido
- Documentação regulatória completa

---

## 📞 CONTATOS

| Papel | Nome | Email |
|-------|------|-------|
| **Product Owner** | Dr. Abel Costa | abel.costa@hemodoctor.com |
| **Tech Lead** | [A definir] | - |
| **QA Lead** | [A definir] | - |

---

**Gerado em:** 20 de Outubro de 2025
**Versão:** v1.0
**Status:** APROVADO para execução
**Próxima Revisão:** 26 Out 2025 (Sprint Review)
