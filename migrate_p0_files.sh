#!/bin/bash
# migrate_p0_files.sh
# Migração P0 (CRÍTICO) - outputs/ → CONSOLIDADO/
# Executar HOJE: 6 ações críticas

set -euo pipefail

BASE_OUT="outputs"
BASE_CONS="HEMODOCTOR_CONSOLIDADO_v2.0_20251010"

echo "================================================================================"
echo "MIGRAÇÃO P0 (CRÍTICO) - outputs/ → HEMODOCTOR_CONSOLIDADO_v2.0_20251010/"
echo "================================================================================"
echo ""
echo "Total de ações: 6"
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

# 1. ANVISA Checklist
echo "1/6 Copiando ANVISA_Submission_Checklist_v2.0_20251012.csv..."
if [ -f "$BASE_OUT/ANVISA_Submission_Checklist_v2.0_20251012.csv" ]; then
    cp "$BASE_OUT/ANVISA_Submission_Checklist_v2.0_20251012.csv" \
       "$BASE_CONS/02_SUBMISSAO_ANVISA/"
    echo "    ✅ Copiado para 02_SUBMISSAO_ANVISA/"
else
    echo "    ⚠️  Arquivo não encontrado em outputs/"
fi
echo ""

# 2. ANVISA Package Builder
echo "2/6 Copiando ANVISA_v2.0_PACKAGE_BUILDER.sh..."
if [ -f "$BASE_OUT/ANVISA_v2.0_PACKAGE_BUILDER.sh" ]; then
    mkdir -p "$BASE_CONS/02_SUBMISSAO_ANVISA/scripts/"
    cp "$BASE_OUT/ANVISA_v2.0_PACKAGE_BUILDER.sh" \
       "$BASE_CONS/02_SUBMISSAO_ANVISA/scripts/"
    chmod +x "$BASE_CONS/02_SUBMISSAO_ANVISA/scripts/ANVISA_v2.0_PACKAGE_BUILDER.sh"
    echo "    ✅ Copiado para 02_SUBMISSAO_ANVISA/scripts/ (executável)"
else
    echo "    ⚠️  Arquivo não encontrado em outputs/"
fi
echo ""

# 3. BUG-001
echo "3/6 Copiando BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md..."
if [ -f "$BASE_OUT/BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md" ]; then
    cp "$BASE_OUT/BUG-001_PLATELET_CLASSIFIER_CRITICAL_BUGS.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/TESTES/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/TESTES/"
    echo "    📋 22 bugs documentados (crítico para Milestone 1)"
else
    echo "    ⚠️  Arquivo não encontrado em outputs/"
fi
echo ""

# 4. TEST-REQ
echo "4/6 Copiando TEST-REQ_Traceability_Matrix_v1.0.md..."
if [ -f "$BASE_OUT/TEST-REQ_Traceability_Matrix_v1.0.md" ]; then
    cp "$BASE_OUT/TEST-REQ_Traceability_Matrix_v1.0.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/TESTES/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/TESTES/"
else
    echo "    ⚠️  Arquivo não encontrado em outputs/"
fi
echo ""

# 5. TEST-HD-016
echo "5/6 Copiando TEST-HD-016_Pediatric_Test_Cases_v1.0.md..."
if [ -f "$BASE_OUT/TEST-HD-016_Pediatric_Test_Cases_v1.0.md" ]; then
    cp "$BASE_OUT/TEST-HD-016_Pediatric_Test_Cases_v1.0.md" \
       "$BASE_CONS/03_DESENVOLVIMENTO/TESTES/"
    echo "    ✅ Copiado para 03_DESENVOLVIMENTO/TESTES/"
else
    echo "    ⚠️  Arquivo não encontrado em outputs/"
fi
echo ""

# 6. Remover duplicado
echo "6/6 Removendo duplicado TERMO_COMPROMISSO_PESQUISADOR..."
DUPLICADO="$BASE_CONS/01_SUBMISSAO_CEP/CONSENTIMENTO/TERMO_COMPROMISSO_PESQUISADOR_v1.0.md"
if [ -f "$DUPLICADO" ]; then
    rm "$DUPLICADO"
    echo "    ✅ Removido de 01_SUBMISSAO_CEP/CONSENTIMENTO/"
    echo "    📁 Mantida cópia em 01_SUBMISSAO_CEP/DECLARACOES/"
else
    echo "    ℹ️  Duplicado já foi removido"
fi
echo ""

echo "================================================================================"
echo "P0 CONCLUÍDO"
echo "================================================================================"
echo ""
echo "Ações executadas: 6/6"
echo ""
echo "PRÓXIMOS PASSOS:"
echo "1. Validar com: bash validate_p0.sh"
echo "2. Executar migração P1: bash migrate_p1_files.sh"
echo ""
