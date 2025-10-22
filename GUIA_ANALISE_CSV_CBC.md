# 🏥 Guia de Análise de Dados CBC em CSV

**Data:** 22 de Outubro de 2025
**Versão:** 1.0.0
**Script:** `scripts/cbc_csv_analyzer.py`

---

## 📋 VISÃO GERAL

Este guia explica como testar as implementações do HemoDoctor (Bug #2 Fix + Test Structure Fix) com seus dados reais de CBC em formato CSV.

**Features:**
- ✅ Ingestão automática de CSV
- ✅ Detecção automática de formato
- ✅ Bug #2 Fix aplicado (age boundaries inclusive)
- ✅ Análise estatística completa
- ✅ Relatórios em JSON e CSV
- ✅ Validação em dados reais

---

## 🚀 QUICK START (5 minutos)

### Passo 1: Preparar seu CSV

Seu arquivo CSV precisa ter **pelo menos** estas colunas:

**Obrigatórias:**
- `patient_id` (ou `id`, `mrn`, `Patient ID`)
- `age_months` (ou `age_years`, `Age (months)`, `Age (years)`)
- `platelet_count` (ou `platelets`, `PLT`, `Platelet Count`)

**Exemplo mínimo:**
```csv
patient_id,age_months,platelet_count
PAT001,24.0,120000
PAT002,72.0,450000
PAT003,144.0,180000
```

### Passo 2: Executar o Script

```bash
# Opção 1: Passar caminho do arquivo como argumento
python3 scripts/cbc_csv_analyzer.py /caminho/para/seu_arquivo.csv

# Opção 2: Script perguntará o caminho
python3 scripts/cbc_csv_analyzer.py
# Digite o caminho quando solicitado

# Opção 3: Testar com dados de exemplo
python3 scripts/cbc_csv_analyzer.py scripts/example_cbc_data.csv
```

### Passo 3: Ver Resultados

O script gera automaticamente:

1. **Console Output**: Resumo estatístico
2. **JSON File**: `cbc_analysis_results/[nome]_results_[timestamp].json`
3. **CSV File**: `cbc_analysis_results/[nome]_results_[timestamp].csv`

---

## 📊 FORMATOS DE CSV SUPORTADOS

### Formato 1: Padrão (Mínimo)

```csv
patient_id,age_months,platelet_count
PAT001,24.0,120000
PAT002,72.0,450000
```

**Colunas:**
- `patient_id`: ID do paciente
- `age_months`: Idade em meses (float)
- `platelet_count`: Contagem de plaquetas (/μL)

### Formato 2: Com Idade em Anos

```csv
id,age_years,platelets
001,2.0,120000
002,6.0,450000
```

**Conversão automática:** age_years × 12 = age_months

### Formato 3: Laboratório

```csv
MRN,Age (years),PLT,Date
12345,2.0,120,2025-10-22
12346,6.0,450,2025-10-22
```

**Features:**
- Auto-detecta nomes de colunas variados
- Suporta PLT em K (×1000): `120` → `120000`
- Ignora colunas extras (Date, etc.)

### Formato 4: Completo

```csv
patient_id,age_months,age_years,platelet_count,wbc,hb,timestamp
PAT001,24.0,2.0,120000,8.5,12.0,2025-10-22T10:00:00
PAT002,72.0,6.0,450000,7.2,13.5,2025-10-22T11:00:00
```

**Nota:** Colunas extras (wbc, hb) são ignoradas, mas não causam erro.

---

## 🎯 O QUE O SCRIPT FAZ

### 1. Ingestão de Dados

```
📁 Lê arquivo CSV
📋 Detecta formato automaticamente
🔍 Valida dados
⚠️  Reporta warnings (linhas com erro)
✅ Retorna dados limpos
```

### 2. Processamento (Bug #2 Fix Aplicado!)

Para cada paciente:

```python
# 1. Classifica idade em grupo pediátrico
age_group = get_age_group(age_months)  # ✅ Com Bug #2 fix!

# 2. Classifica severidade da contagem de plaquetas
severity = classify_severity(platelet_count, age_group)

# 3. Gera resultado estruturado
result = CBCResult(
    patient_id=...,
    age_group=...,
    severity=...,
    # ...
)
```

**Bug #2 Fix Aplicado:**
- ✅ Intervalos inclusivos: `<=` ao invés de `<`
- ✅ 24 meses (2 anos) = Infant Late (não Preschool)
- ✅ 216 meses (18 anos) = Adolescent (não crash!)

### 3. Análise Estatística

Calcula:
- ✅ Total de registros processados
- ✅ Taxa de sucesso
- ✅ Distribuição por grupo etário
- ✅ Distribuição por severidade
- ✅ Distribuição por nível de risco

### 4. Geração de Relatórios

**Console:**
```
📊 ANÁLISE DE DADOS CBC - RESUMO
======================================================================

📈 VISÃO GERAL:
----------------------------------------------------------------------
   Total Records: 30
   Successful Analyses: 30
   Errors: 0
   Success Rate: 100.0%

👶 DISTRIBUIÇÃO POR GRUPO ETÁRIO:
----------------------------------------------------------------------
   PED-01: Neonatal: 3 (10.0%)
   PED-02: Infant Early: 4 (13.3%)
   PED-03: Infant Late: 5 (16.7%)
   ...

⚕️  DISTRIBUIÇÃO POR SEVERIDADE:
----------------------------------------------------------------------
   Normal: 18 (60.0%)
   Mild Thrombocytopenia: 5 (16.7%)
   ...

🚨 DISTRIBUIÇÃO POR NÍVEL DE RISCO:
----------------------------------------------------------------------
   🟢 LOW: 23 (76.7%)
   🟡 MEDIUM: 4 (13.3%)
   🟠 HIGH: 2 (6.7%)
   🔴 CRITICAL: 1 (3.3%)

======================================================================
```

**JSON Output:**
```json
{
  "metadata": {
    "timestamp": "2025-10-22T15:00:00",
    "total_records": 30,
    "version": "1.0.0",
    "bug_fix_applied": "BUG-002 (Inclusive age boundaries)"
  },
  "results": [
    {
      "patient_id": "PAT001",
      "age_months": 24.0,
      "age_years": 2.0,
      "age_group": {
        "name": "PED-03: Infant Late",
        "platelet_min": 200,
        "platelet_max": 475
      },
      "platelet_count": 120000,
      "severity": {
        "level": "Mild Thrombocytopenia",
        "risk_level": "LOW",
        "clinical_significance": "Mild decrease, usually asymptomatic"
      }
    }
  ]
}
```

**CSV Output:**
```csv
patient_id,age_months,age_years,age_group,platelet_count,severity_level,risk_level
PAT001,24.0,2.0,PED-03: Infant Late,120000,Mild Thrombocytopenia,LOW
PAT002,72.0,6.0,PED-04: Preschool,450000,Normal,LOW
...
```

---

## 🧪 VALIDAÇÃO DO BUG #2 FIX

### Teste de Boundaries Críticos

Crie um CSV de teste:

```csv
patient_id,age_months,platelet_count,expected_group
TEST01,1.0,350000,PED-01: Neonatal
TEST02,6.0,450000,PED-02: Infant Early
TEST03,24.0,400000,PED-03: Infant Late
TEST04,72.0,350000,PED-04: Preschool
TEST05,144.0,300000,PED-05: School Age
TEST06,216.0,350000,PED-06: Adolescent
```

**Execute:**
```bash
python3 scripts/cbc_csv_analyzer.py test_boundaries.csv
```

**Validação:**
- ✅ TEST03 (24 meses) deve ser **PED-03: Infant Late**
- ✅ TEST06 (216 meses) deve ser **PED-06: Adolescent** (não crash!)

**Sem Bug #2 Fix:**
- ❌ TEST03 seria PED-04 (ERRADO!)
- ❌ TEST06 causaria crash!

---

## 📈 CASOS DE USO

### Caso 1: Validar Base de Dados Clínica

**Cenário:** Você tem 1,000 registros de CBC do hospital

```bash
# 1. Preparar CSV
# hospital_cbc_2025.csv com colunas: MRN, Age, PLT

# 2. Executar análise
python3 scripts/cbc_csv_analyzer.py hospital_cbc_2025.csv

# 3. Analisar resultados
# - Verificar distribuição por severidade
# - Identificar casos críticos
# - Validar classificação etária
```

**Benefícios:**
- ✅ Validação em larga escala
- ✅ Identificação de casos críticos
- ✅ Estatísticas populacionais
- ✅ Verificação de Bug #2 em dados reais

### Caso 2: Comparar Antes/Depois do Bug #2

**Cenário:** Testar impacto do fix em boundaries

```bash
# 1. Criar CSV com casos boundary
# boundaries_test.csv: 1m, 6m, 24m, 72m, 144m, 216m

# 2. Executar com Bug #2 fix
python3 scripts/cbc_csv_analyzer.py boundaries_test.csv

# 3. Verificar classificações
# - 24 meses → PED-03 ✅ (antes: PED-04 ❌)
# - 216 meses → PED-06 ✅ (antes: crash ❌)
```

### Caso 3: Análise Epidemiológica

**Cenário:** Estudo de prevalência de thrombocytopenia

```bash
# 1. CSV com população pediátrica
# study_population.csv: 5,000 registros

# 2. Executar análise
python3 scripts/cbc_csv_analyzer.py study_population.csv

# 3. Usar resultados para:
# - Taxa de thrombocytopenia por grupo etário
# - Distribuição de severidade
# - Identificação de casos críticos
```

---

## 🔍 TROUBLESHOOTING

### Erro: "CSV file not found"

```bash
❌ Erro: CSV file not found: /path/to/file.csv
```

**Solução:**
```bash
# 1. Verificar caminho
ls -la /path/to/file.csv

# 2. Usar caminho absoluto
python3 scripts/cbc_csv_analyzer.py /full/path/to/file.csv

# 3. Ou navegar para diretório
cd /path/to/
python3 ~/hemodoctor-docs/scripts/cbc_csv_analyzer.py file.csv
```

### Erro: "Platelet count column not found"

```bash
❌ Erro de formato: Platelet count column not found
```

**Solução:**

Verificar se CSV tem uma destas colunas:
- `platelet_count`
- `platelets`
- `plt` ou `PLT`
- `Platelet Count`

**Exemplo de renomeação:**
```bash
# Se sua coluna se chama "PLAQ"
# 1. Abrir CSV
# 2. Renomear coluna: PLAQ → platelet_count
# 3. Salvar e executar novamente
```

### Erro: "Age column required"

```bash
❌ Erro de formato: Age column (months or years) is required
```

**Solução:**

Garantir que CSV tenha:
- `age_months` OU
- `age_years` OU
- `Age (months)` OU
- `Age (years)`

### Warnings: Rows com erro

```bash
⚠️  5 warnings:
   ⚠️ Row 12: Could not parse age from row
   ⚠️ Row 23: Could not parse platelet count
   ...
```

**Solução:**

1. **Verificar dados:**
   ```bash
   # Abrir CSV e ir para linha problemática
   # Verificar se valores são válidos
   ```

2. **Campos vazios:**
   ```csv
   # ERRADO:
   PAT001,,120000  # age_months vazio

   # CERTO:
   PAT001,24.0,120000
   ```

3. **Formato incorreto:**
   ```csv
   # ERRADO:
   PAT001,dois anos,120000  # texto ao invés de número

   # CERTO:
   PAT001,24.0,120000  # número
   ```

---

## 📁 ESTRUTURA DE SAÍDA

Após executar, será criado:

```
cbc_analysis_results/
├── seu_arquivo_results_20251022_150000.json
└── seu_arquivo_results_20251022_150000.csv
```

### JSON Output Structure

```json
{
  "metadata": {
    "timestamp": "ISO 8601",
    "total_records": 30,
    "version": "1.0.0",
    "bug_fix_applied": "BUG-002"
  },
  "results": [
    {
      "patient_id": "string",
      "age_months": 24.0,
      "age_years": 2.0,
      "age_group": {
        "name": "PED-03: Infant Late",
        "age_min": 6.0,
        "age_max": 24.0,
        "platelet_min": 200,
        "platelet_max": 475
      },
      "platelet_count": 120000,
      "platelet_count_formatted": "120,000",
      "severity": {
        "level": "Mild Thrombocytopenia",
        "platelet_count": 120000,
        "reference_min": 200000,
        "reference_max": 475000,
        "clinical_significance": "Mild decrease, usually asymptomatic",
        "risk_level": "LOW"
      },
      "timestamp": "ISO 8601",
      "warnings": []
    }
  ]
}
```

### CSV Output Structure

| Coluna | Descrição | Exemplo |
|--------|-----------|---------|
| `patient_id` | ID do paciente | PAT001 |
| `age_months` | Idade em meses | 24.0 |
| `age_years` | Idade em anos | 2.0 |
| `age_group` | Grupo etário | PED-03: Infant Late |
| `platelet_count` | Contagem plaquetas | 120000 |
| `severity_level` | Nível severidade | Mild Thrombocytopenia |
| `risk_level` | Nível de risco | LOW |
| `clinical_significance` | Significado clínico | Mild decrease... |
| `timestamp` | Timestamp análise | 2025-10-22T15:00:00 |

---

## 🎯 CLASSIFICAÇÕES

### Grupos Etários (Age Groups)

| Código | Nome | Idade | Platelet Range |
|--------|------|-------|----------------|
| **PED-01** | Neonatal | 0-1 mês | 150-400 K/μL |
| **PED-02** | Infant Early | 1-6 meses | 200-475 K/μL |
| **PED-03** | Infant Late | 6-24 meses | 200-475 K/μL |
| **PED-04** | Preschool | 2-6 anos | 180-450 K/μL |
| **PED-05** | School Age | 6-12 anos | 150-450 K/μL |
| **PED-06** | Adolescent | 12-18 anos | 150-400 K/μL |

### Níveis de Severidade

**Thrombocytopenia (Baixa):**

| Nível | Range | Significado Clínico | Risco |
|-------|-------|---------------------|-------|
| **Normal** | Ref range | Dentro do normal | 🟢 LOW |
| **Mild** | 100-150K | Assintomático | 🟢 LOW |
| **Moderate** | 50-100K | Risco com trauma/cirurgia | 🟡 MEDIUM |
| **Severe** | 20-50K | Alto risco, sangramento espontâneo | 🟠 HIGH |
| **Critical** | <20K | Life-threatening | 🔴 CRITICAL |

**Thrombocytosis (Alta):**

| Nível | Range | Significado Clínico | Risco |
|-------|-------|---------------------|-------|
| **Mild** | 450-600K | Elevação leve, reativa | 🟢 LOW |
| **Moderate** | 600-800K | Investigar causa | 🟡 MEDIUM |
| **Severe** | 800K-1M | Risco trombose | 🟠 HIGH |
| **Critical** | >1M | Risco extremo | 🔴 CRITICAL |

---

## 💡 DICAS

### 1. Preparação de Dados

```bash
# Sempre fazer backup primeiro
cp seu_arquivo.csv seu_arquivo_backup.csv

# Verificar delimitador
head -1 seu_arquivo.csv
# Se usar ; ao invés de ,, editar script:
# reader = CBCCSVReader(csv_file, delimiter=';')
```

### 2. Validação de Resultados

```python
# Após gerar JSON, validar manualmente alguns casos:
import json

with open('results.json') as f:
    data = json.load(f)

# Caso boundary: 24 meses
case_24m = [r for r in data['results'] if r['age_months'] == 24.0]
for case in case_24m:
    assert case['age_group']['name'] == 'PED-03: Infant Late'
    print(f"✅ {case['patient_id']}: Correctly classified as Infant Late")
```

### 3. Análise Estatística

```bash
# Usar CSV output para análises no Excel/Google Sheets
# Ou importar em Python:
import pandas as pd

df = pd.read_csv('cbc_analysis_results/results.csv')

# Análises:
print(df.groupby('age_group')['severity_level'].value_counts())
print(df['risk_level'].value_counts())
```

---

## ✅ CHECKLIST DE VALIDAÇÃO

Após executar análise, verificar:

- [ ] **Taxa de sucesso = 100%?**
  - Se não, investigar warnings

- [ ] **Boundaries corretos?**
  - [ ] 24 meses → PED-03 (Infant Late) ✅
  - [ ] 216 meses → PED-06 (Adolescent) ✅
  - [ ] Sem crashes? ✅

- [ ] **Distribuições fazem sentido?**
  - [ ] Age groups proporcionais
  - [ ] Severidades razoáveis
  - [ ] Risk levels esperados

- [ ] **Resultados salvos?**
  - [ ] JSON gerado
  - [ ] CSV gerado
  - [ ] Ambos em `cbc_analysis_results/`

---

## 🎉 PRÓXIMOS PASSOS

Após validar com seus dados:

1. **Análise Detalhada**
   - Revisar casos críticos (CRITICAL risk)
   - Validar classificações borderline
   - Comparar com diagnósticos clínicos

2. **Integração**
   - Incorporar script no pipeline
   - Automatizar análises periódicas
   - Gerar alertas para casos críticos

3. **Documentação**
   - Documentar achados
   - Criar relatório de validação
   - Atualizar protocolos clínicos

---

## 📞 SUPORTE

**Dúvidas ou problemas?**

1. Verificar este guia primeiro
2. Revisar exemplos em `scripts/example_cbc_data.csv`
3. Executar com dados de exemplo para validar setup
4. Consultar documentação técnica em `docs/`

---

**Versão:** 1.0.0
**Última Atualização:** 22 de Outubro de 2025
**Script:** `scripts/cbc_csv_analyzer.py`
**Bugs Fixados:** BUG-002 (Age boundaries) ✅
