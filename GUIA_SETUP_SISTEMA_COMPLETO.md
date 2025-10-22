# 🏥 Guia de Setup - Sistema HemoDoctor Completo

**Data:** 22 de Outubro de 2025
**Versão:** 1.0.0
**Objetivo:** Rodar sistema FastAPI completo com dados CSV reais

---

## 📋 VISÃO GERAL

Este guia explica como configurar e rodar o **sistema HemoDoctor COMPLETO** (FastAPI + todas as análises hematológicas) com seus dados CSV reais.

**O que você vai conseguir:**
- ✅ Rodar servidor FastAPI completo
- ✅ Processar dados CBC em batch
- ✅ Análise hematológica completa (não só plaquetas)
- ✅ Relatórios consolidados
- ✅ API REST funcionando

---

## 🚀 QUICK START (15 minutos)

### Opção 1: Setup Manual

```bash
# 1. Navegar para código-fonte
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Iniciar servidor FastAPI
uvicorn main:app --reload --port 8000

# 4. Em outro terminal, processar CSV
cd ~/hemodoctor-docs
python3 scripts/hemodoctor_batch_processor.py
# API URL: http://localhost:8000
# CSV file: /caminho/para/seus_dados.csv
```

### Opção 2: Docker (Recomendado)

```bash
# 1. Usar docker-compose
cd ~/hemodoctor-docs
docker-compose up -d

# 2. Processar CSV
python3 scripts/hemodoctor_batch_processor.py
# API URL: http://localhost:8000
# CSV file: /caminho/para/seus_dados.csv

# 3. Ver logs
docker-compose logs -f hemodoctor-api
```

---

## 📦 PRÉ-REQUISITOS

### Software Necessário

```bash
# Python 3.9+
python3 --version

# pip (gerenciador de pacotes)
pip --version

# Git
git --version

# Docker (opcional, mas recomendado)
docker --version
docker-compose --version
```

### Dependências Python

```bash
# FastAPI e servidor
fastapi==0.114.1
uvicorn[standard]==0.30.6
pydantic==2.9.2

# HTTP requests
requests==2.31.0

# Autenticação
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4

# Banco de dados (se usar)
psycopg2-binary==2.9.9  # PostgreSQL
sqlalchemy==2.0.23

# Testes
pytest==7.4.0
pytest-asyncio==0.21.1
httpx==0.24.1

# Utilities
python-dotenv==1.0.0
```

---

## 📁 ESTRUTURA DO PROJETO

```
HEMODOCTOR_CONSOLIDADO_v2.0_20251010/
├── 03_DESENVOLVIMENTO/
│   ├── CODIGO_FONTE/
│   │   ├── main.py                    # FastAPI app
│   │   ├── requirements.txt           # Dependencies
│   │   ├── .env                       # Configuration
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── analyze.py         # /api/v1/analyze/cbc
│   │   │   │   └── health.py          # /health
│   │   │   └── models/
│   │   │       ├── cbc.py             # CBC data models
│   │   │       └── result.py          # Analysis results
│   │   ├── core/
│   │   │   ├── analyzers/
│   │   │   │   ├── platelet.py        # Platelet analysis (Bug #2 fix)
│   │   │   │   ├── anemia.py          # Anemia detection
│   │   │   │   ├── leukocyte.py       # WBC analysis
│   │   │   │   └── orchestrator.py    # Main analyzer
│   │   │   └── config.py              # App configuration
│   │   └── utils/
│   │       ├── validators.py          # Input validation
│   │       └── exceptions.py          # Custom exceptions
│   └── TESTES/
│       └── test_automation/           # Test suite
└── 02_SUBMISSAO_ANVISA/               # Regulatory docs
```

---

## ⚙️ CONFIGURAÇÃO

### 1. Criar Arquivo .env

```bash
# Navegar para código-fonte
cd /path/to/CODIGO_FONTE

# Criar .env
cat > .env << EOF
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_RELOAD=true
DEBUG=true

# CORS
CORS_ORIGINS=["http://localhost:3000", "http://localhost:8000"]

# Database (se usar)
DATABASE_URL=postgresql://user:pass@localhost:5432/hemodoctor

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Logging
LOG_LEVEL=INFO

# HemoDoctor Specific
ENABLE_BUG2_FIX=true
MAX_BATCH_SIZE=1000
ANALYSIS_TIMEOUT=30
EOF
```

### 2. Instalar Dependências

```bash
# Opção 1: pip
pip install -r requirements.txt

# Opção 2: pip com virtual environment (recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 3. Verificar Instalação

```bash
# Testar imports
python3 -c "import fastapi, uvicorn, pydantic; print('✅ Dependencies OK')"

# Verificar estrutura
ls -la main.py api/ core/
```

---

## 🚀 INICIAR SERVIDOR

### Método 1: Uvicorn Direto

```bash
# Desenvolvimento (com reload)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Produção (sem reload)
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Método 2: Python Script

```bash
# Se tiver script run.py
python3 run.py
```

### Método 3: Docker

```bash
# Build image
docker build -t hemodoctor-api:latest .

# Run container
docker run -d \
  --name hemodoctor-api \
  -p 8000:8000 \
  -v $(pwd):/app \
  hemodoctor-api:latest
```

### Verificar Se Está Rodando

```bash
# Teste manual
curl http://localhost:8000/health

# Deve retornar:
# {"status": "healthy", "version": "2.0.0"}

# Ou abrir no navegador:
open http://localhost:8000/docs  # Swagger UI
open http://localhost:8000/redoc # ReDoc
```

---

## 📝 API ENDPOINTS

### 1. Health Check

```bash
GET /health

Response:
{
  "status": "healthy",
  "version": "2.0.0",
  "timestamp": "2025-10-22T15:00:00Z"
}
```

### 2. CBC Analysis (Principal)

```bash
POST /api/v1/analyze/cbc

Request Body:
{
  "patient_id": "PAT001",
  "age_months": 24.0,
  "platelet_count": 120000,
  "hemoglobin": 11.5,
  "hematocrit": 35.0,
  "wbc": 8500,
  "rbc": 4.2,
  "mcv": 85.0,
  "mch": 28.0,
  "mchc": 33.0
}

Response:
{
  "patient_id": "PAT001",
  "analysis_timestamp": "2025-10-22T15:00:00Z",
  "age_classification": {
    "age_months": 24.0,
    "age_group": "PED-03: Infant Late",
    "reference_ranges": {...}
  },
  "platelet_analysis": {
    "count": 120000,
    "severity": "Mild Thrombocytopenia",
    "risk_level": "LOW",
    "clinical_significance": "..."
  },
  "anemia_analysis": {
    "present": false,
    "type": null,
    ...
  },
  "leukocyte_analysis": {
    "count": 8500,
    "classification": "Normal",
    ...
  },
  "comprehensive_assessment": {
    "critical_findings": [],
    "recommendations": [...],
    "risk_score": "LOW"
  }
}
```

### 3. Batch Analysis

```bash
POST /api/v1/analyze/batch

Request Body:
{
  "records": [
    {"patient_id": "PAT001", "age_months": 24.0, ...},
    {"patient_id": "PAT002", "age_months": 72.0, ...}
  ]
}

Response:
{
  "total": 2,
  "successful": 2,
  "failed": 0,
  "results": [...]
}
```

---

## 🔧 PROCESSAR DADOS CSV

### Usar Batch Processor

```bash
# 1. Certifique-se que API está rodando
curl http://localhost:8000/health

# 2. Execute batch processor
python3 scripts/hemodoctor_batch_processor.py

# 3. Responda às perguntas:
API Base URL [http://localhost:8000]: <ENTER>
CSV file path: /path/to/seu_arquivo.csv

# 4. Aguarde processamento
🚀 Processing 100 records with 5 workers...
✅ [1/100] PAT001
✅ [2/100] PAT002
...

# 5. Ver resultados
📊 BATCH PROCESSING SUMMARY
...
✅ Results saved to: hemodoctor_batch_results/batch_results_20251022_150000.json
```

### Formato do CSV de Entrada

```csv
patient_id,age_months,platelet_count,hemoglobin,wbc,rbc
PAT001,24.0,120000,11.5,8500,4.2
PAT002,72.0,450000,13.0,7200,4.8
```

**Colunas suportadas:**
- `patient_id` (obrigatório)
- `age_months` ou `age_years` (obrigatório)
- `platelet_count` (obrigatório)
- `hemoglobin`, `hematocrit`, `wbc`, `rbc`, `mcv`, `mch`, `mchc` (opcionais)

### Resultados Gerados

**JSON Output:**
```json
{
  "metadata": {
    "timestamp": "2025-10-22T15:00:00",
    "total_records": 100,
    "successful": 98,
    "failed": 2,
    "version": "1.0.0"
  },
  "results": [
    {
      "success": true,
      "patient_id": "PAT001",
      "data": {
        "age_classification": {...},
        "platelet_analysis": {...},
        "anemia_analysis": {...},
        "comprehensive_assessment": {...}
      }
    }
  ]
}
```

---

## 🐳 DOCKER SETUP

### docker-compose.yml

Veja: `docker-compose.yml` na raiz do projeto

```bash
# Iniciar serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down

# Rebuild após mudanças
docker-compose up -d --build
```

---

## 🧪 TESTAR O SISTEMA

### 1. Teste Manual com cURL

```bash
# Health check
curl http://localhost:8000/health

# Análise simples
curl -X POST http://localhost:8000/api/v1/analyze/cbc \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": "TEST001",
    "age_months": 24.0,
    "platelet_count": 120000,
    "hemoglobin": 11.5
  }'
```

### 2. Teste com Python

```python
import requests

# Análise individual
response = requests.post(
    'http://localhost:8000/api/v1/analyze/cbc',
    json={
        'patient_id': 'TEST001',
        'age_months': 24.0,
        'platelet_count': 120000,
        'hemoglobin': 11.5
    }
)

print(response.json())
```

### 3. Teste com Swagger UI

```bash
# Abrir navegador
open http://localhost:8000/docs

# Clicar em POST /api/v1/analyze/cbc
# Clicar em "Try it out"
# Preencher JSON de exemplo
# Clicar em "Execute"
```

---

## 🔍 TROUBLESHOOTING

### Problema 1: Servidor não inicia

```bash
❌ Error: [Errno 48] Address already in use
```

**Solução:**
```bash
# Verificar o que está usando porta 8000
lsof -i :8000

# Matar processo
kill -9 <PID>

# Ou usar outra porta
uvicorn main:app --port 8001
```

### Problema 2: ModuleNotFoundError

```bash
❌ ModuleNotFoundError: No module named 'fastapi'
```

**Solução:**
```bash
# Instalar dependências
pip install -r requirements.txt

# Ou ativar venv
source venv/bin/activate
```

### Problema 3: API não responde

```bash
❌ Error: Cannot connect to HemoDoctor API
```

**Solução:**
```bash
# 1. Verificar se servidor está rodando
curl http://localhost:8000/health

# 2. Verificar logs
docker-compose logs -f

# 3. Verificar porta correta
# Se mudou porta, ajustar no batch processor
```

### Problema 4: Timeout em batch

```bash
❌ Request timeout
```

**Solução:**
```bash
# Aumentar timeout no batch processor
# Editar hemodoctor_batch_processor.py:
# api_timeout: int = 60  # Aumentar para 60s

# Ou reduzir workers paralelos
# max_workers: int = 2  # Reduzir para 2
```

---

## 📊 MONITORAMENTO

### Logs

```bash
# Ver logs do FastAPI
tail -f logs/hemodoctor.log

# Ou se usar docker
docker-compose logs -f hemodoctor-api

# Filtrar por erro
docker-compose logs -f | grep ERROR
```

### Métricas

```bash
# Endpoint de métricas (se configurado)
curl http://localhost:8000/metrics

# Ou usar ferramentas:
# - Prometheus
# - Grafana
# - New Relic
```

---

## 🎯 CASOS DE USO

### Caso 1: Análise de Base Hospitalar

```bash
# 1. Preparar CSV (1000+ registros)
# hospital_cbc_2025.csv

# 2. Iniciar API
docker-compose up -d

# 3. Processar em batch
python3 scripts/hemodoctor_batch_processor.py

# 4. Analisar resultados
python3 -c "
import json
with open('hemodoctor_batch_results/batch_results_*.json') as f:
    data = json.load(f)
    print(f\"Total: {data['metadata']['total_records']}\")
    print(f\"Success: {data['metadata']['successful']}\")
"
```

### Caso 2: Validação Clínica

```bash
# 1. CSV com casos validados
# validated_cases.csv com diagnósticos conhecidos

# 2. Processar
python3 scripts/hemodoctor_batch_processor.py

# 3. Comparar resultados do sistema vs diagnóstico real
# 4. Calcular accuracy, sensitivity, specificity
```

### Caso 3: Monitoramento em Tempo Real

```bash
# 1. Integrar com sistema laboratorial
# 2. Enviar cada CBC assim que completar
# 3. Receber análise imediata
# 4. Alertar casos críticos
```

---

## 📚 RECURSOS ADICIONAIS

### Documentação API

```bash
# Swagger UI (interativo)
http://localhost:8000/docs

# ReDoc (mais clean)
http://localhost:8000/redoc

# OpenAPI schema (JSON)
http://localhost:8000/openapi.json
```

### Scripts Úteis

```bash
# scripts/hemodoctor_batch_processor.py
# - Processa CSV em batch

# scripts/cbc_csv_analyzer.py
# - Análise standalone (sem API)

# scripts/validate_boundaries.py
# - Valida Bug #2 fix
```

---

## ✅ CHECKLIST DE SETUP

- [ ] Python 3.9+ instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] Arquivo `.env` configurado
- [ ] Servidor FastAPI iniciado
- [ ] Health check respondendo (`curl http://localhost:8000/health`)
- [ ] Swagger UI acessível (`http://localhost:8000/docs`)
- [ ] CSV de teste preparado
- [ ] Batch processor funcionando
- [ ] Resultados gerados corretamente
- [ ] Bug #2 fix validado (24m → PED-03, 216m → PED-06)

---

## 🎉 PRÓXIMOS PASSOS

Após setup completo:

1. **Processar dados reais**
   - Use seu CSV de dados hospitalares
   - Valide resultados

2. **Integração**
   - Integrar com sistema laboratorial
   - Automatizar envio de resultados

3. **Monitoramento**
   - Setup logs e métricas
   - Alertas para casos críticos

4. **Documentação**
   - Documentar achados
   - Relatório de validação clínica

---

**Versão:** 1.0.0
**Última Atualização:** 22 de Outubro de 2025
**Suporte:** Ver `GUIA_ANALISE_CSV_CBC.md` para mais detalhes
