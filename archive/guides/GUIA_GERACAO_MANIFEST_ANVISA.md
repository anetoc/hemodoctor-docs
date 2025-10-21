# 📦 Guia de Geração - DMR Manifest v2.0 + SHA256SUMS

**Data:** 13 de Outubro de 2025  
**Tempo Estimado:** 30 minutos  
**Objetivo:** Gerar manifesto oficial para submissão ANVISA

---

## 📍 LOCALIZAÇÃO DO SCRIPT

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex/tools
```

**Script:** `build_pre_anvisa_pack.py`

---

## 🔧 EXECUÇÃO

### Passo 1: Verificar Script Existe

```bash
ls -lh build_pre_anvisa_pack.py
# Se existir, prosseguir
```

### Passo 2: Executar Script

```bash
python build_pre_anvisa_pack.py
```

**Saída Esperada:**
```
Scanning AUTHORITATIVE_BASELINE/...
Found 67 documents
Generating checksums...
Creating DMR_MANIFEST_v2.0_20251012_OFICIAL.json...
Creating SHA256SUMS_v2.0_20251012.txt...
✅ Done!
```

---

## 📄 ARQUIVOS GERADOS

### 1. DMR_MANIFEST_v2.0_20251012_OFICIAL.json

**Estrutura:**
```json
{
  "device": {
    "name": "HemoDoctor",
    "version": "1.0",
    "classification": "ANVISA Class III",
    "manufacturer": "HemoDoctor Tecnologia Médica Ltda",
    "date": "2025-10-12"
  },
  "modules": {
    "00_INDICE_GERAL": {
      "files": [...],
      "count": 11
    },
    "01_REGULATORIO": {
      "files": [...],
      "count": 5
    },
    ...
  },
  "statistics": {
    "total_files": 67,
    "total_size_mb": 12.5,
    "checksum_algorithm": "SHA-256"
  },
  "checksums": {
    "file1.md": "abc123...",
    "file2.md": "def456...",
    ...
  }
}
```

### 2. SHA256SUMS_v2.0_20251012.txt

**Formato:**
```
abc123...  AUTHORITATIVE_BASELINE/00_INDICE_GERAL/file1.md
def456...  AUTHORITATIVE_BASELINE/01_REGULATORIO/file2.md
...
```

---

## 📋 VALIDAÇÃO

### Passo 1: Verificar Arquivos Gerados

```bash
ls -lh DMR_MANIFEST_v2.0_*.json
ls -lh SHA256SUMS_v2.0_*.txt
```

### Passo 2: Validar JSON

```bash
# Verificar se JSON é válido
python -m json.tool DMR_MANIFEST_v2.0_20251012_OFICIAL.json > /dev/null
echo "JSON válido!"
```

### Passo 3: Contar Arquivos

```bash
# Verificar se todos os 67 docs estão no manifesto
jq '.statistics.total_files' DMR_MANIFEST_v2.0_20251012_OFICIAL.json
# Saída esperada: 67
```

### Passo 4: Validar Checksums

```bash
# Verificar se checksums estão corretos
cd /Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE
sha256sum -c ../SHA256SUMS_v2.0_20251012.txt
# Todos devem passar
```

---

## 📦 COPIAR PARA BASELINE

```bash
# Copiar arquivos para BASELINE oficial
cp DMR_MANIFEST_v2.0_20251012_OFICIAL.json /Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/

cp SHA256SUMS_v2.0_20251012.txt /Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/
```

---

## ✅ CHECKLIST

- [ ] Script executado sem erros
- [ ] DMR_MANIFEST gerado (JSON válido)
- [ ] SHA256SUMS gerado
- [ ] 67 arquivos no manifesto
- [ ] Checksums validados
- [ ] Arquivos copiados para BASELINE
- [ ] Commit realizado

---

## 🚀 COMANDO COMPLETO

```bash
#!/bin/bash
# Script completo de geração de manifest

cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/@hemodoctor/dossier-anvisa-codex/tools

# 1. Executar script
python build_pre_anvisa_pack.py

# 2. Validar JSON
python -m json.tool DMR_MANIFEST_v2.0_20251012_OFICIAL.json > /dev/null && echo "✅ JSON válido"

# 3. Verificar contagem
TOTAL=$(jq '.statistics.total_files' DMR_MANIFEST_v2.0_20251012_OFICIAL.json)
echo "Total de arquivos: $TOTAL (esperado: 67)"

# 4. Copiar para BASELINE
cp DMR_MANIFEST_v2.0_20251012_OFICIAL.json /Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/
cp SHA256SUMS_v2.0_20251012.txt /Users/abelcosta/Documents/HemoDoctor/docs/AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/

# 5. Commit
cd /Users/abelcosta/Documents/HemoDoctor/docs
git add AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/DMR_MANIFEST_v2.0_20251012_OFICIAL.json
git add AUTHORITATIVE_BASELINE/01_REGULATORIO/DMR/SHA256SUMS_v2.0_20251012.txt
git commit -m "📦 Adiciona DMR Manifest v2.0 + SHA256SUMS para ANVISA

- 67 documentos oficiais catalogados
- Checksums SHA-256 validados
- Pronto para submissão ANVISA"

echo "✅ Manifest gerado e commitado!"
```

---

**Status:** ✅ GUIA COMPLETO  
**Tempo:** 30 minutos execução  
**Output:** 2 arquivos (JSON + TXT)

