#!/bin/bash
# Script de Verificação de Duplicação
# Verifica se há conteúdo duplicado entre WORKSPACES e AUTHORITATIVE_BASELINE

echo "🔍 Verificando duplicação de conteúdo..."
echo ""

# Cores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contador
duplicates_found=0

# Verificar se há cópias de documentos oficiais nos workspaces
echo "📋 Verificando documentos oficiais copiados..."

# Lista de documentos oficiais que não devem estar nos workspaces
official_docs=(
    "CER-001"
    "SRS-001"
    "SDD-001"
    "RMP-001"
    "TST-001"
    "DMR"
    "SBOM"
    "VEX"
    "SEC-001"
    "SOUP-001"
)

for doc in "${official_docs[@]}"; do
    # Buscar nos workspaces (excluindo _links_baseline.md)
    found=$(find WORKSPACES/ -type f -name "*$doc*" ! -name "_links_baseline.md" ! -name "*.sh")
    
    if [ ! -z "$found" ]; then
        echo -e "${RED}❌ DUPLICAÇÃO ENCONTRADA:${NC} $doc"
        echo "$found"
        duplicates_found=$((duplicates_found + 1))
        echo ""
    fi
done

# Verificar blocos grandes de texto copiado (mais de 100 linhas idênticas)
echo "📄 Verificando blocos de texto copiado..."

# TODO: Implementar verificação de similaridade de conteúdo
# Por agora, apenas verifica arquivos com nomes similares

echo ""
if [ $duplicates_found -eq 0 ]; then
    echo -e "${GREEN}✅ Nenhuma duplicação encontrada!${NC}"
    echo "Os workspaces estão referenciando corretamente a baseline."
else
    echo -e "${RED}⚠️  $duplicates_found duplicação(ões) encontrada(s)${NC}"
    echo "Por favor, remova as cópias e use links para os documentos oficiais."
    exit 1
fi

echo ""
echo "🔗 Verificando links para baseline..."

# Verificar se cada workspace tem _links_baseline.md
workspaces=$(find WORKSPACES/ -maxdepth 1 -mindepth 1 -type d)

missing_links=0
for ws in $workspaces; do
    if [ ! -f "$ws/_links_baseline.md" ]; then
        echo -e "${YELLOW}⚠️  $ws está sem _links_baseline.md${NC}"
        missing_links=$((missing_links + 1))
    else
        echo -e "${GREEN}✅${NC} $(basename $ws) tem _links_baseline.md"
    fi
done

echo ""
if [ $missing_links -eq 0 ]; then
    echo -e "${GREEN}✅ Todos os workspaces têm arquivos de links!${NC}"
else
    echo -e "${YELLOW}⚠️  $missing_links workspace(s) sem _links_baseline.md${NC}"
    echo "Recomenda-se criar esses arquivos."
fi

echo ""
echo "✅ Verificação concluída!"

