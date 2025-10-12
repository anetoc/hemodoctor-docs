#!/bin/bash
# validate_p1.sh
# Validação P1 - Verificar se arquivos importantes foram copiados

set -euo pipefail

BASE_CONS="HEMODOCTOR_CONSOLIDADO_v2.0_20251010"

echo "================================================================================"
echo "VALIDAÇÃO P1 - Arquivos Importantes"
echo "================================================================================"
echo ""

TOTAL=9
OK=0
FAIL=0

# 1. FDA Compliance Report
echo -n "1/9 FDA_524B_COMPLIANCE_REPORT.md ... "
if [ -f "$BASE_CONS/02_SUBMISSAO_ANVISA/COMPLIANCE/FDA_524B_COMPLIANCE_REPORT.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 2. Penetration Test RFP
echo -n "2/9 PENETRATION_TEST_RFP_REQUIREMENTS.md ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/SEGURANCA/PENETRATION_TEST_RFP_REQUIREMENTS.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 3. DevOps Security Hardening
echo -n "3/9 DEVOPS_SECURITY_HARDENING_CHECKLIST.md ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/SEGURANCA/DEVOPS_SECURITY_HARDENING_CHECKLIST.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 4. Validation Plan
echo -n "4/9 VAL-001_Validation_Plan_v1.0.md ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/VALIDACAO/VAL-001_Validation_Plan_v1.0.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 5. M2 Regulatory Status
echo -n "5/9 M2_REGULATORY_SUBMISSION_STATUS.md ... "
if [ -f "$BASE_CONS/05_MASTER_DOCUMENTATION/M2_REGULATORY_SUBMISSION_STATUS.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 6. CEP Gaps
echo -n "6/9 CEP_GAPS_DEFINICOES_PENDENTES_20251010.md ... "
if [ -f "$BASE_CONS/01_SUBMISSAO_CEP/GAPS/CEP_GAPS_DEFINICOES_PENDENTES_20251010.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 7. Milestone 1 Signoff
echo -n "7/9 MILESTONE_1_SIGNOFF_20251009.md ... "
if [ -f "$BASE_CONS/05_MASTER_DOCUMENTATION/MILESTONE_1_SIGNOFF_20251009.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 8. REQ-HD-016
echo -n "8/9 REQ-HD-016_PEDIATRIC_REQUIREMENTS_REPORT.md ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/ESPECIFICACOES/REQ-HD-016_PEDIATRIC_REQUIREMENTS_REPORT.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "❌ FALTANDO"
    ((FAIL++))
fi

# 9. SEC-001 Consolidation Gap Report (opcional)
echo -n "9/9 SEC-001_CONSOLIDATION_GAP_REPORT.md (opcional) ... "
if [ -f "$BASE_CONS/03_DESENVOLVIMENTO/ESPECIFICACOES/REPORTS/SEC-001_CONSOLIDATION_GAP_REPORT.md" ]; then
    echo "✅ OK"
    ((OK++))
else
    echo "ℹ️  NÃO COPIADO (relatório interno opcional)"
    # Não contar como falha
fi

echo ""
echo "================================================================================"
echo "RESULTADO P1"
echo "================================================================================"
echo ""
echo "Total de verificações: $TOTAL (8 obrigatórias + 1 opcional)"
echo "Sucesso: $OK/$TOTAL"
echo "Falhas: $FAIL/$TOTAL"
echo ""

if [ $FAIL -eq 0 ]; then
    echo "✅ VALIDAÇÃO P1 COMPLETA - Todos os arquivos importantes copiados"
    echo ""
    echo "PRÓXIMOS PASSOS:"
    echo "1. Decidir sobre documentos v2.0 em HDOC_Submission_Package_v2.0_20251012/"
    echo "2. Verificar duplicidade Annexes CER-001"
    echo "3. Atualizar INDEX_COMPLETO_CONSOLIDADO.md"
    exit 0
else
    echo "❌ VALIDAÇÃO P1 FALHOU - $FAIL arquivo(s) faltando"
    echo ""
    echo "AÇÃO: Re-executar migrate_p1_files.sh"
    exit 1
fi
