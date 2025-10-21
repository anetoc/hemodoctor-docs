# 📊 AVALIAÇÃO: Prometheus MCP para Monitoring

**Data:** 19 de Outubro de 2025
**Decisão Necessária:** Adicionar Prometheus MCP ao ecossistema?

---

## 🎯 CONTEXTO

**Necessidade:** Monitoring avançado de produção para HemoDoctor

**Atual:** `@monitor-agent` existe mas sem MCP dedicado para métricas

**Proposta:** Adicionar Prometheus MCP para:
- Métricas de aplicação em tempo real
- Alerting automático
- Dashboards (Grafana integration)
- Historical metrics analysis
- Performance monitoring

---

## 📋 SITUAÇÃO ATUAL

### **@monitor-agent (Existente)**

**Status:** ✅ Instalado
**Capabilities:**
- Observability 24/7
- Anomaly detection
- Alerts setup
- Dashboards

**MCPs Atuais:**
- `postgresql` → Metrics storage
- `github` → Config management

**Limitações:**
- ❌ Sem integração Prometheus nativa
- ❌ Sem scraping automático de métricas
- ❌ Sem alertmanager integration
- ❌ Sem Grafana dashboards prontos
- ❌ Metrics manuais via SQL (não ideal)

---

## 🔍 PROMETHEUS MCP - PROPOSTA

### **O que é Prometheus?**

**Prometheus** = Sistema de monitoring open-source + time-series database

**Features:**
- ✅ Métricas em tempo real
- ✅ PromQL (query language poderosa)
- ✅ Alerting (AlertManager)
- ✅ Service discovery automático
- ✅ Grafana integration nativa
- ✅ Exporters para tudo (FastAPI, PostgreSQL, Redis, etc.)

### **Prometheus MCP - Capabilities**

**1. Metrics Collection:**
```python
# Expose metrics endpoint
from prometheus_client import Counter, Histogram

cbc_analysis_total = Counter('cbc_analysis_total', 'Total CBC analyses')
analysis_duration = Histogram('analysis_duration_seconds', 'Analysis duration')

# MCP queries via PromQL
@monitor-agent /metrics "cbc_analysis_total[5m]"
→ Rate: 120 analyses/min
```

**2. Alerting:**
```yaml
# Alert rules via MCP
@monitor-agent /alert-rule "high_error_rate"
  expr: rate(cbc_errors_total[5m]) > 0.05
  severity: critical
  annotations:
    summary: "CBC error rate > 5%"
    action: "Check evidence engine logs"
```

**3. Dashboards:**
```bash
# Create Grafana dashboard via MCP
@monitor-agent /dashboard "hemodoctor-production"
  - Panel: CBC analysis rate (5min)
  - Panel: Response time p95
  - Panel: Error rate by syndrome
  - Panel: Resource usage (CPU, memory)
```

**4. Queries (PromQL):**
```bash
# Complex queries
@monitor-agent /query "rate(cbc_analysis_total{syndrome='S-TMA'}[1h])"
→ TMA syndrome: 3.2 analyses/hour

@monitor-agent /query "histogram_quantile(0.95, analysis_duration_seconds)"
→ P95 response time: 87ms
```

---

## 🎯 USE CASES HEMODOCTOR

### **Use Case 1: Production Monitoring**

**Workflow:**
```
@monitor-agent /setup-monitoring "hemodoctor-production"

# Agent creates:
# 1. Prometheus config (scrape FastAPI /metrics)
# 2. AlertManager rules (errors, latency, availability)
# 3. Grafana dashboard (real-time metrics)

# User gets:
# - Real-time dashboard
# - Alerts on Slack/Email
# - Historical metrics (retention 30 days)
```

### **Use Case 2: Performance Analysis**

**Workflow:**
```
@analyzer-agent "Analyze performance last 7 days"

# Uses: prometheus MCP
# Queries:
# - rate(cbc_analysis_total[7d])
# - histogram_quantile(0.95, analysis_duration_seconds[7d])
# - rate(cbc_errors_total[7d]) by syndrome

# Returns:
# - 850K analyses total
# - P95: 92ms (target <100ms ✅)
# - Error rate: 0.3% (target <1% ✅)
# - S-TMA: 0.1% FN rate (target 0% ⚠️)
```

### **Use Case 3: Alerting**

**Example Alerts:**
```yaml
# Critical: False Negatives on S-TMA
- alert: TMA_FalseNegative
  expr: tma_false_negatives_total > 0
  severity: critical
  action: Immediate review by hematologist

# Warning: High latency
- alert: HighLatency
  expr: histogram_quantile(0.95, analysis_duration_seconds) > 0.1
  severity: warning
  action: Check evidence engine performance

# Info: High volume
- alert: HighVolume
  expr: rate(cbc_analysis_total[5m]) > 200
  severity: info
  action: Scale infrastructure if needed
```

---

## 📊 COMPARAÇÃO: Com vs Sem Prometheus MCP

| Feature | Sem Prometheus | Com Prometheus MCP |
|---------|---------------|-------------------|
| **Métricas em tempo real** | ❌ Manual (SQL) | ✅ Automático (scraping) |
| **Alerting** | ⚠️ Basic | ✅ Advanced (AlertManager) |
| **Dashboards** | ❌ Custom build | ✅ Grafana ready |
| **Query language** | SQL (limited) | PromQL (powerful) |
| **Retention** | PostgreSQL (manual) | Time-series DB (optimized) |
| **Service discovery** | ❌ Manual | ✅ Automático |
| **Exporters** | ❌ None | ✅ 100+ exporters |
| **Integration** | Custom code | ✅ MCP native |
| **Cost** | $0 | $0 (local/cloud) |

---

## 💰 CUSTO-BENEFÍCIO

### **Opções de Deployment**

**Opção 1: Local (Desenvolvimento)**
```bash
# Docker Compose
docker-compose up prometheus grafana
# Cost: $0 ✅
# Setup: 15 min
```

**Opção 2: Cloud (Produção)**
```bash
# Grafana Cloud (Free tier)
# - 10K series
# - 14 days retention
# - 3 users
# Cost: $0 ✅

# Ou Prometheus managed
# AWS Managed Prometheus
# Cost: ~$5-10/mês (produção)
```

**Opção 3: Self-Hosted (Institutional)**
```bash
# Servidor institucional
# Cost: $0 (infraestrutura existente)
```

### **ROI**

| Aspecto | Valor |
|---------|-------|
| **Tempo de Setup** | 30 min - 1h |
| **Custo Operacional** | $0 - $10/mês |
| **ROI Esperado** | 2-3x faster incident detection |
| **MTTR** | -50% (Mean Time To Recovery) |
| **Visibility** | +90% (real-time vs manual) |

---

## 🎯 DECISÃO RECOMENDADA

### **⏸️ AGUARDAR até Produção**

**Motivos:**

1. **Projeto em Desenvolvimento:** HemoDoctor ainda não está em produção
2. **Prioridade Atual:** Submissão ANVISA (20 Out) e CEP (14 Nov)
3. **Necessidade Real:** Monitoring avançado só necessário EM produção
4. **Timing:** Implementar Prometheus 1-2 semanas ANTES de go-live

**Recomendação:** ✅ **Adicionar na roadmap** mas **não implementar agora**

### **📅 Quando Implementar?**

**Timeline Recomendado:**
```
HOJE (19 Out)
  → Foco: ANVISA submission (P0)

20 Out - 14 Nov
  → Foco: CEP submission

Dez 2025 - Jan 2026
  → Pré-produção prep
  ✅ IMPLEMENTAR PROMETHEUS aqui
  - Setup local
  - Configure exporters
  - Create dashboards
  - Setup alerts

Fev 2026
  → Production go-live
  ✅ Prometheus monitoring ATIVO
```

---

## 📋 PLANO DE IMPLEMENTAÇÃO (FUTURO)

### **Quando Implementar (Pré-Produção)**

**Fase 1: Setup Prometheus (30 min)**
```bash
# 1. Docker Compose
version: '3.8'
services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
```

**Fase 2: FastAPI Integration (30 min)**
```python
# Add to main.py
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Metrics available at /metrics
```

**Fase 3: MCP Configuration (30 min)**
```json
// ~/.claude.json
{
  "mcpServers": {
    "prometheus": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-prometheus"],
      "env": {
        "PROMETHEUS_URL": "http://localhost:9090"
      }
    }
  }
}
```

**Fase 4: Alerting Setup (1h)**
```yaml
# alertmanager.yml
global:
  slack_api_url: 'https://hooks.slack.com/...'

route:
  receiver: 'hemodoctor-alerts'
  group_by: ['alertname', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h

receivers:
  - name: 'hemodoctor-alerts'
    slack_configs:
      - channel: '#hemodoctor-alerts'
        title: '{{ .GroupLabels.alertname }}'
        text: '{{ .CommonAnnotations.summary }}'
```

**Fase 5: Grafana Dashboards (1h)**
```bash
# Import HemoDoctor dashboard
@monitor-agent /import-dashboard "hemodoctor-production.json"

# Panels:
# 1. CBC Analysis Rate (5min window)
# 2. Response Time (P50, P95, P99)
# 3. Error Rate by Syndrome
# 4. False Negative Rate (S-TMA, S-PLT-CRITICA, etc.)
# 5. Resource Usage (CPU, Memory, Disk)
```

**Total Setup Time:** 3-4 horas (one-time)

---

## ✅ APROVAÇÃO NECESSÁRIA

**Dr. Abel, você aprova o plano?**

**Opções:**

1. ✅ **APROVAR PLANO** → Adicionar à roadmap pré-produção (Dez 2025)
2. ✅ **IMPLEMENTAR AGORA** → Setup imediato (3-4h hoje)
3. ❌ **NÃO NECESSÁRIO** → Usar monitoring básico (postgresql + logs)

**Recomendação:** ✅ **Opção 1** (aprovar plano, implementar em Dez 2025)

---

## 📊 RESUMO EXECUTIVO

| Item | Status | Recomendação |
|------|--------|--------------|
| **Prometheus MCP** | Não instalado | ⏸️ Aguardar pré-produção |
| **Necessidade** | Alta (produção) | Baixa (desenvolvimento) |
| **Timing** | Dez 2025 | ✅ Ideal |
| **Custo** | $0 - $10/mês | ✅ Aceitável |
| **Setup Time** | 3-4 horas | ✅ Razoável |
| **ROI** | 2-3x | ✅ Alto |

**Decisão:** ⏸️ **Adicionar à roadmap** (implementar em Dez 2025, 1-2 semanas antes de produção)

---

## 🎯 PRÓXIMOS PASSOS

**SE APROVADO (Opção 1 - Recomendado):**
1. Adicionar "Prometheus MCP setup" à roadmap Dez 2025
2. Criar issue/task no backlog
3. Revisitar em Nov 2025 (1 mês antes)

**SE APROVADO (Opção 2 - Implementar Agora):**
1. Setup Docker Compose (30 min)
2. Configure FastAPI metrics (30 min)
3. Add Prometheus MCP (30 min)
4. Create alerts (1h)
5. Create dashboards (1h)
6. Test integration (30 min)

**Total:** 4 horas

---

**Aguardando suas decisões sobre:**
- ✅ Item 7: data-analyst-agent?
- ✅ Item 8: Prometheus MCP?

**Para continuar com a implementação...**
