#!/bin/bash
# migrate_p1_files.sh
# Migração P1 (IMPORTANTE) - outputs/ → CONSOLIDADO/
# Executar esta semana: 9 arquivos importantes

set -euo pipefail

BASE_OUT="outputs"
BASE_CONS="HEMODOCTOR_CONSOLIDADO_v2.0_20251010"

echo "================================================================================"
echo "MIGRAÇÃO P1 (IMPORTANTE) - outputs/ → HEMODOCTOR_CONSOLIDADO_v2.0_20251010/"
echo "================================================================================"
echo ""
echo "Total de ações: 9 arquivos"
echo ""

# Verificar se diretórios existem
if [ ! -d "$BASE_OUT" ]; then
    echo "❌ ERRO: Diretório outputs/ não encontrado"
    echo "   Execute este script no diretório docs/"
    exit 1
fi

if [ ! -d "$BASE_CONS" ]; then
    echo "❌ ERRO: Diretório HEMODOCTOR_CONSOLIDADO_v2.0_20251010/ não encontrado"
    exit 1
fi

COPIED=0

# 1. FDA Compliance Report
echo "1/9 Copiando FDA_524B_COMPLIANCE_REPORT.md..."
if [ -f "$BASE_OUT/FDA_524B_COMPLIANCE_REPORT.md" ]; then
    mkdir -p "$BASE_CONS/02_SUBMISSAO_ANVISA/COMPLIANCE/"
    cp "$BASE_OUT/FDA_524B_COMPLIANCE_REPORT.md" \
       "$BASE_CONS/02_SUBMISSAO_ANVISA/COMPLIANCE/"
    echo "    ✅ Copiado para 02_SUBMISSAO_ANVISA/COMPLIANCE/ (33 KB)"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 2. Penetration Test RFP
echo "2/9 Copiando PENETRATION_TEST_RFP_REQUIREMENTS.md..."
if [ -f "$BASE_OUT/PENETRATION_TEST_RFP_REQUIREMENTS.md" ]; then
    mkdir -p "$BASE_CONS/03_DESENVOLVIMENTO/SEGURANCA/"
    cp "$BASE_OUT/PENETRATION_TEST_RFP_REQUIREMENTS.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/SEGURANCA/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/SEGURANCA/ (19 KB)"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 3. DevOps Security Hardening
echo "3/9 Copiando DEVOPS_SECURITY_HARDENING_CHECKLIST.md..."
if [ -f "$BASE_OUT/DEVOPS_SECURITY_HARDENING_CHECKLIST.md" ]; then
    mkdir -p "$BASE_CONS/03_DESENVOLVIMENTO/SEGURANCA/"
    cp "$BASE_OUT/DEVOPS_SECURITY_HARDENING_CHECKLIST.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/SEGURANCA/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/SEGURANCA/ (22 KB)"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 4. Validation Plan
echo "4/9 Copiando VAL-001_Validation_Plan_v1.0.md..."
if [ -f "$BASE_OUT/VAL-001_Validation_Plan_v1.0.md" ]; then
    mkdir -p "$BASE_CONS/03_DESENVOLVIMENTO/VALIDACAO/"
    cp "$BASE_OUT/VAL-001_Validation_Plan_v1.0.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/VALIDACAO/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/VALIDACAO/"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 5. M2 Regulatory Submission Status
echo "5/9 Copiando M2_REGULATORY_SUBMISSION_STATUS.md..."
if [ -f "$BASE_OUT/M2_REGULATORY_SUBMISSION_STATUS.md" ]; then
    cp "$BASE_OUT/M2_REGULATORY_SUBMISSION_STATUS.md" \
       "$BASE_CONS/05_MASTER_DOCUMENTATION/"
    echo "    ✅ Copiado para 05_MASTER_DOCUMENTATION/ (15 KB)"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 6. CEP Gaps
echo "6/9 Copiando CEP_GAPS_DEFINICOES_PENDENTES_20251010.md..."
if [ -f "$BASE_OUT/CEP_GAPS_DEFINICOES_PENDENTES_20251010.md" ]; then
    mkdir -p "$BASE_CONS/01_SUBMISSAO_CEP/GAPS/"
    cp "$BASE_OUT/CEP_GAPS_DEFINICOES_PENDENTES_20251010.md" \
       "$BASE_CONS/01_SUBMISSAO_CEP/GAPS/"
    echo "    ✅ Copiado para 01_SUBMISSAO_CEP/GAPS/"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 7. Milestone 1 Signoff
echo "7/9 Copiando MILESTONE_1_SIGNOFF_20251009.md..."
if [ -f "$BASE_OUT/MILESTONE_1_SIGNOFF_20251009.md" ]; then
    cp "$BASE_OUT/MILESTONE_1_SIGNOFF_20251009.md" \
       "$BASE_CONS/05_MASTER_DOCUMENTATION/"
    echo "    ✅ Copiado para 05_MASTER_DOCUMENTATION/ (17 KB)"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 8. REQ-HD-016
echo "8/9 Copiando REQ-HD-016_PEDIATRIC_REQUIREMENTS_REPORT.md..."
if [ -f "$BASE_OUT/REQ-HD-016_PEDIATRIC_REQUIREMENTS_REPORT.md" ]; then
    cp "$BASE_OUT/REQ-HD-016_PEDIATRIC_REQUIREMENTS_REPORT.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/ESPECIFICACOES/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/ESPECIFICACOES/"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado"
fi
echo ""

# 9. SEC-001 Consolidation Gap Report
echo "9/9 Copiando SEC-001_CONSOLIDATION_GAP_REPORT.md..."
if [ -f "$BASE_OUT/SEC-001_CONSOLIDATION_GAP_REPORT.md" ]; then
    mkdir -p "$BASE_CONS/03_DESENVOLVIMENTO/ESPECIFICACOES/REPORTS/"
    cp "$BASE_OUT/SEC-001_CONSOLIDATION_GAP_REPORT.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/ESPECIFICACOES/REPORTS/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/ESPECIFICACOES/REPORTS/"
    ((COPIED++))
else
    echo "    ⚠️  Arquivo não encontrado (opcional - relatório interno)"
fi
echo ""

echo "================================================================================"
echo "P1 CONCLUÍDO"
echo "================================================================================"
echo ""
echo "Arquivos copiados: $COPIED/9"
echo ""
echo "PRÓXIMOS PASSOS:"
echo "1. Validar com: bash validate_p1.sh"
echo "2. Decidir sobre documentos v2.0 em HDOC_Submission_Package_v2.0_20251012/"
echo "   (consultar Abel / Regulatory Lead)"
echo "3. Verificar duplicidade Annexes CER-001 em outputs/annexes/"
echo ""
