# 🏥 HemoDoctor Scripts

Scripts utilitários para análise de dados CBC.

## 📁 Arquivos

### `cbc_csv_analyzer.py`
Script principal para análise de dados CBC em formato CSV.

**Features:**
- ✅ Bug #2 Fix aplicado (age boundaries inclusive)
- ✅ Auto-detect formato CSV
- ✅ Análise estatística completa
- ✅ Relatórios JSON + CSV
- ✅ Validação em dados reais

### `example_cbc_data.csv`
Arquivo CSV de exemplo com 30 registros de teste.

**Uso:**
```bash
python3 cbc_csv_analyzer.py example_cbc_data.csv
```

## 🚀 Quick Start

```bash
# Executar com seus dados
python3 cbc_csv_analyzer.py /caminho/para/seu_arquivo.csv

# Ou testar com exemplo
python3 cbc_csv_analyzer.py example_cbc_data.csv
```

## 📖 Documentação Completa

Ver: `../GUIA_ANALISE_CSV_CBC.md`

## 📊 Resultados

Gerados em: `../cbc_analysis_results/`
- JSON: Dados estruturados completos
- CSV: Análise tabulada

## ✅ Validação Bug #2

O script valida automaticamente:
- ✅ 24 meses → PED-03 (Infant Late)
- ✅ 216 meses → PED-06 (Adolescent)
- ✅ Sem crashes!

## 📞 Suporte

Ver guia completo em: `../GUIA_ANALISE_CSV_CBC.md`
