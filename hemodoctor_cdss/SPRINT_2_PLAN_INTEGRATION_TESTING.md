# 🔗 SPRINT 2 PLAN - INTEGRATION TESTING

**Projeto:** HemoDoctor CDSS v2.4.0
**Período:** 22-28 Outubro 2025 (7 dias)
**Objetivo:** Validar integração end-to-end e performance do sistema completo
**Status:** ⏳ PLANEJADO

---

## 📋 OBJETIVOS SPRINT 2

### Objetivo Principal

Validar que todos os componentes do sistema funcionam corretamente quando integrados, com foco em:
- Pipeline E2E (normalização → evidências → síndromes → next steps → output → WORM)
- Performance (latência <100ms, throughput >1000 casos/h)
- Clinical validation (casos reais + edge cases)
- API REST (4 endpoints)

### Critérios de Sucesso

1. ✅ **100 integration tests** criados e passing
2. ✅ **Latência média <100ms** por caso
3. ✅ **Throughput >1000 casos/h** (batch processing)
4. ✅ **30 clinical cases** validados (representativos)
5. ✅ **API REST** funcionando (4 endpoints testados)
6. ✅ **WORM log** integridade validada (append-only)

---

## 🎯 SPRINTS ANTERIORES COMPLETADOS

### Sprint 0: Core Implementation ✅
- Duração: 20-26 Out (7 dias)
- Resultado: 362 tests, 89% coverage
- Status: ✅ COMPLETO

### Sprint 1: Security Testing ✅
- Duração: 21 Out (1 dia - ANTECIPADO!)
- Resultado: 104 security tests, 100% compliance
- Status: ✅ COMPLETO

---

## 📦 ESTRUTURA DE TESTES

### Arquivos a Criar (6 novos)

```
tests/integration/
├── test_e2e_pipeline.py (30 tests) ⭐ NOVO
│   ├── test_complete_pipeline_normal_case()
│   ├── test_complete_pipeline_critical_case()
│   ├── test_complete_pipeline_missing_data()
│   ├── test_normalization_integration()
│   ├── test_evidence_to_syndrome_integration()
│   ├── test_next_steps_integration()
│   ├── test_worm_log_integration()
│   └── ... (23 more tests)
│
├── test_api_integration.py (20 tests) ⭐ NOVO
│   ├── test_analyze_endpoint_complete_flow()
│   ├── test_concurrent_requests()
│   ├── test_api_error_handling()
│   └── ... (17 more tests)
│
├── test_clinical_cases.py (30 tests) ⭐ NOVO
│   ├── test_ida_complete_case()
│   ├── test_tma_complete_case()
│   ├── test_apl_complete_case()
│   └── ... (27 more clinical syndromes)
│
├── test_performance.py (10 tests) ⭐ NOVO
│   ├── test_single_case_latency()
│   ├── test_batch_processing_throughput()
│   ├── test_memory_usage()
│   └── ... (7 more tests)
│
├── test_data_flow.py (5 tests) ⭐ NOVO
│   ├── test_cbc_input_to_worm_log()
│   ├── test_deterministic_route_id()
│   └── ... (3 more tests)
│
└── test_edge_cases.py (5 tests) ⭐ NOVO
    ├── test_all_missing_data()
    ├── test_extreme_values()
    └── ... (3 more tests)
```

**Total:** 100 integration tests

---

## 🗓️ CRONOGRAMA DETALHADO

### **Dia 1-2 (22-23 Out): E2E Pipeline + API** 🔧

**Objetivo:** Validar pipeline completo e API REST

**Tarefas:**
1. ✅ Criar `test_e2e_pipeline.py` (30 tests)
   - Normal cases (hb, wbc, plt normais)
   - Critical cases (TMA, APL, neutropenia grave)
   - Missing data handling
   - Edge cases

2. ✅ Criar `test_api_integration.py` (20 tests)
   - POST /analyze (complete flow)
   - GET /health (monitoring)
   - GET /version (versioning)
   - Concurrent requests (10 simultaneous)
   - Error handling (400, 500)

**Entregáveis:**
- 50 integration tests
- API validation report

**Tempo:** 16h (8h/dia × 2 dias)

---

### **Dia 3-4 (24-25 Out): Clinical Cases** 🩺

**Objetivo:** Validar 30 clinical syndromes com casos reais

**Tarefas:**
1. ✅ Criar `test_clinical_cases.py` (30 tests)
   - 9 critical syndromes (obrigatório)
   - 21 priority/routine syndromes (representativos)

**Clinical Syndromes a Validar:**

**Critical (9):** ⭐ PRIORIDADE
- S-NEUTROPENIA-GRAVE (ANC <0.5)
- S-BLASTIC-SYNDROME (blasts present)
- S-TMA (schistocytes + PLT <30)
- S-PLT-CRITICA (PLT <20)
- S-ANEMIA-GRAVE (Hb <6.5 M / <6.0 F)
- S-NEUTROFILIA-LEFTSHIFT-CRIT
- S-THROMBOCITOSE-CRIT (PLT ≥1000)
- S-CIVD (≥2 markers altered)
- S-APL (promyelocytes + coagulopathy)

**Priority (15):**
- S-IDA (iron deficiency anemia)
- S-ACD (anemia of chronic disease)
- S-HEMOLYSIS
- S-PTI (immune thrombocytopenia)
- S-NEUTROPENIA-MODERADA
- S-LYMPHOCYTOSIS
- S-EOSINOPHILIA
- ... (8 more)

**Routine (6):**
- S-INCONCLUSIVO
- S-NORMAL
- ... (4 more)

**Entregáveis:**
- 30 clinical validation tests
- Clinical validation report (30 casos documentados)

**Tempo:** 16h (8h/dia × 2 dias)

---

### **Dia 5 (26 Out): Performance** ⚡

**Objetivo:** Validar latência e throughput

**Tarefas:**
1. ✅ Criar `test_performance.py` (10 tests)
   - Single case latency (<100ms target)
   - Batch processing (1000 cases throughput)
   - Memory usage (<500MB for 1000 cases)
   - CPU usage
   - Concurrent load (50 requests/sec)

**Métricas Target:**
- **Latência média:** <100ms/caso
- **Throughput:** >1000 casos/h
- **Memory:** <500MB (1000 casos)
- **CPU:** <50% (single core)

**Entregáveis:**
- 10 performance tests
- Performance benchmark report

**Tempo:** 8h

---

### **Dia 6 (27 Out): Data Flow + Edge Cases** 🔄

**Objetivo:** Validar data flow e edge cases

**Tarefas:**
1. ✅ Criar `test_data_flow.py` (5 tests)
   - CBC input → WORM log (full trace)
   - Deterministic route_id
   - HMAC integrity

2. ✅ Criar `test_edge_cases.py` (5 tests)
   - All fields missing
   - Extreme values (hb=0, wbc=500)
   - Invalid morphology
   - Conflicting evidences

**Entregáveis:**
- 10 data flow + edge case tests

**Tempo:** 8h

---

### **Dia 7 (28 Out): Review + Documentation** 📝

**Objetivo:** Review completo e documentação final

**Tarefas:**
1. ✅ Rodar suite completa (566 tests)
2. ✅ Review pass rate (target: 100%)
3. ✅ Review coverage (target: maintain 89%)
4. ✅ Criar `INTEGRATION_TEST_REPORT.md`
5. ✅ Criar `CLINICAL_VALIDATION_REPORT.md`
6. ✅ Criar `PERFORMANCE_BENCHMARK_REPORT.md`

**Entregáveis:**
- 3 relatórios técnicos
- Sprint 2 complete checklist

**Tempo:** 8h

---

## 📊 MÉTRICAS DE SUCESSO

### Testes

| Categoria | Target | Verificação |
|-----------|--------|-------------|
| **Integration Tests** | 100 | pytest count |
| **Pass Rate** | 100% | 566/566 passing |
| **Coverage** | ≥89% | pytest-cov |

### Performance

| Métrica | Target | Tool |
|---------|--------|------|
| **Latência (single)** | <100ms | pytest-benchmark |
| **Throughput** | >1000/h | custom script |
| **Memory** | <500MB | memory_profiler |
| **CPU** | <50% | psutil |

### Clinical

| Categoria | Target | Verificação |
|-----------|--------|-------------|
| **Critical Syndromes** | 9/9 validated | Manual review |
| **Priority Syndromes** | 15/15 validated | Manual review |
| **Routine Syndromes** | 6/6 validated | Manual review |

---

## 🛠️ FERRAMENTAS UTILIZADAS

### Testing
- `pytest` - Test framework
- `pytest-cov` - Coverage reporting
- `pytest-benchmark` - Performance benchmarking
- `pytest-asyncio` - Async testing
- `httpx` - HTTP client (API testing)

### Performance
- `memory_profiler` - Memory usage
- `psutil` - CPU/memory monitoring
- `cProfile` - Profiling

### Data Generation
- `faker` - Fake data generation
- `hypothesis` - Property-based testing (optional)

---

## 📝 REPORTS A GERAR

### 1. INTEGRATION_TEST_REPORT.md

**Conteúdo:**
- E2E pipeline validation
- API integration results
- Data flow validation
- Edge cases handling
- Pass rate summary

**Target:** 30 páginas, 10 KB

---

### 2. CLINICAL_VALIDATION_REPORT.md

**Conteúdo:**
- 30 clinical cases detailed
- Syndrome detection accuracy
- False positive/negative analysis
- Clinical rationale validation
- Hematologist approval checklist

**Target:** 50 páginas, 20 KB

---

### 3. PERFORMANCE_BENCHMARK_REPORT.md

**Conteúdo:**
- Latency distribution (p50, p95, p99)
- Throughput analysis
- Memory usage profile
- CPU usage profile
- Bottleneck identification
- Optimization recommendations

**Target:** 20 páginas, 8 KB

---

## 🚦 DEFINITION OF DONE

Sprint 2 é considerado completo quando:

1. ✅ **100 integration tests** criados
2. ✅ **566/566 tests passing** (100% pass rate)
3. ✅ **Coverage ≥89%** mantido
4. ✅ **Latência <100ms** validada
5. ✅ **Throughput >1000/h** validada
6. ✅ **30 clinical cases** validados
7. ✅ **3 reports** gerados
8. ✅ **Code review** completo
9. ✅ **Documentation** atualizada
10. ✅ **Git push** to remote

---

## 🔗 PRÓXIMOS SPRINTS

### Sprint 3: Audit & Traceability (29 Out - 2 Nov)
- WORM log audit trail validation
- Traceability matrix completion
- Regulatory documentation

### Sprint 4: Red List Validation (23 Nov - 6 Dez)
- 240 critical cases (FN=0 mandatory)
- Blind hematologist adjudication
- Sensitivity ≥99% for critical syndromes

---

## 📞 CONTATOS

| Função | Responsável |
|--------|-------------|
| **Sprint Owner** | @coder-agent |
| **Clinical Reviewer** | Dr. Abel Costa |
| **QA Lead** | @qa-lead-agent |

---

## 🎯 COMANDOS ÚTEIS

### Setup

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/hemodoctor_cdss

# Install performance tools
pip install pytest-benchmark memory-profiler psutil

# Verify installation
python3 -m pytest --version
```

### Run Tests

```bash
# All integration tests
PYTHONPATH=src python3 -m pytest tests/integration/ -v

# With coverage
PYTHONPATH=src python3 -m pytest tests/integration/ -v --cov=src/hemodoctor --cov-report=term

# With benchmark
PYTHONPATH=src python3 -m pytest tests/integration/test_performance.py -v --benchmark-only

# Full suite (566 tests)
PYTHONPATH=src python3 -m pytest tests/ -v
```

### Performance Profiling

```bash
# Memory profiling
python3 -m memory_profiler scripts/profile_memory.py

# CPU profiling
python3 -m cProfile -o profile.stats scripts/profile_cpu.py
```

---

## 📚 REFERÊNCIAS

- Sprint 0 Plan: `SPRINT_0_PLAN_v2.4.0.md`
- Security Report: `SECURITY_TEST_REPORT.md`
- YAML Specs: `config/*.yaml` (16 files)
- Clinical Rules: `02_evidence_hybrid.yaml`, `03_syndromes_hybrid.yaml`

---

**Última Atualização:** 21 de Outubro de 2025 - 23:55 BRT
**Versão:** 1.0
**Status:** ⏳ READY TO START (22 Out 2025)

---

**🚀 Sprint 2: Integration Testing - READY!**
