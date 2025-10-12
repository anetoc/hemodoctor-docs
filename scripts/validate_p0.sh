#!/bin/bash
# validate_p0.sh
# Validação P0 - Verificar se arquivos críticos foram copiados

set -euo pipefail

BASE_CONS="HEMODOCTOR_CONSOLIDADO_v2.0_20251010"

echo "================================================================================"
echo "VALIDAÇÃO P0 - Arquivos Críticos"
echo "================================================================================"
echo ""

TOTAL=6
OK=0
FAIL=0

# 1. ANVISA Checklist
echo -n "1/6 ANVISA_Submission_Checklist_v2.0_20251012.csv ... "
if [ -f "$BASE_CONS/02_SUBMISSAO_ANVISA/ANVISA_Submission_Checklist_v2.0_20251012.csv" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 2. ANVISA Package Builder
echo -n "2/6 ANVISA_v2.0_PACKAGE_BUILDER.sh (executável) ... "
if [ -x "$BASE_CONS/02_SUBMISSAO_ANVISA/scripts/ANVISA_v2.0_PACKAGE_BUILDER.sh" ]; then
    echo "✅ OK"
    ((OK++))
elif [ -f "$BASE_CONS/02_SUBMISSAO_ANVISA/scripts/ANVISA_v2.0_PACKAGE_BUILDER.sh" ]; then
    echo "⚠️  EXISTE (mas não executável)"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 3. BUG-001
echo -n "3/6 BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/TESTES/BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 4. TEST-REQ
echo -n "4/6 TEST-REQ_Traceability_Matrix_v1.0.md ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/TESTES/TEST-REQ_Traceability_Matrix_v1.0.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 5. TEST-HD-016
echo -n "5/6 TEST-HD-016_Pediatric_Test_Cases_v1.0.md ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/TESTES/TEST-HD-016_Pediatric_Test_Cases_v1.0.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 6. Duplicado removido
echo -n "6/6 Duplicado TERMO_COMPROMISSO_PESQUISADOR removido ... "
if [ ! -f "$BASE_CONS/01_SUBMISSAO_CEP/CONSENTIMENTO/TERMO_COMPROMISSO_PESQUISADOR_v1.0.md" ]; then
    echo "✅ OK (removido)"
    ((OK++))
else
    echo "❌ AINDA EXISTE"
    ((FAIL++))
fi

echo ""
echo "================================================================================"
echo "RESULTADO P0"
echo "================================================================================"
echo ""
echo "Total de verificações: $TOTAL"
echo "Sucesso: $OK/$TOTAL"
echo "Falhas: $FAIL/$TOTAL"
echo ""

if [ $FAIL -eq 0 ]; then
    echo "✅ VALIDAÇÃO P0 COMPLETA - Todos os arquivos críticos copiados"
    echo ""
    echo "PRÓXIMO PASSO: Executar migrate_p1_files.sh"
    exit 0
else
    echo "❌ VALIDAÇÃO P0 FALHOU - $FAIL arquivo(s) faltando"
    echo ""
    echo "AÇÃO: Re-executar migrate_p0_files.sh"
    exit 1
fi
