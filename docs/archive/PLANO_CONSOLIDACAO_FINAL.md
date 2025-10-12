# 🎯 PLANO DE CONSOLIDAÇÃO FINAL - HemoDoctor

**Data:** 2025-10-11 00:05 BRT
**Objetivo:** Deixar repositório 100% organizado, mantendo apenas essencial

---

## 📊 ANÁLISE DAS PASTAS LEGACY

### **1. hemodoctor versao fernanda/** (752 MB)

**Estrutura analisada:**
```
129M  Projeto/                           ← Duplicado (já em outros lugares)
128M  Projeto.zip                        ← ZIP duplicado
107M  Projeto-20250919.zip               ← ZIP duplicado
107M  @hemodoctor-20250916.zip           ← ZIP duplicado
106M  drive-download-20250919.zip        ← ZIP duplicado
 42M  HemoDoctor.pptx                    ← Apresentação
 39M  Pacote-de-Auditoria.pptx           ← Apresentação
 19M  synthetic_hemodoctor_50000/        ← Dados sintéticos
  5M  Validação Clínica.docx             ← Word doc
  5M  PROJETO HEMODOCTOR COMPLETO.docx   ← Word doc
  2M  hemodoctor_poc_jamia_5_1_artifacts ← Artifacts científicos
1.3M  Dossie Hemodoctor ANVISA:FDA/      ← Dossier antigo
+ openapi/, schemas/, tools/, docs/      ← JÁ MIGRADOS para CONSOLIDADO
```

**Total ZIPs duplicados:** ~450 MB (60% do total!)

**DECISÃO:**
- ✅ Manter: AUTHORITATIVE_BASELINE/ (já extraído)
- ✅ Migrar:
  - openapi/, schemas/ (se não estiverem em CONSOLIDADO)
  - hemodoctor_poc_jamia_5_1_artifacts/ (artigos científicos)
  - PowerPoints (documentação executiva)
- ❌ Arquivar: ZIPs, Projeto/, Word docs duplicados

**Economia:** ~500 MB (66%)

---

### **2. hemodoctor versao paulo/** (607 MB)

**Estrutura analisada:**
```
272M  4ec7ec47-8bf8...zip                ← ZIP gigante (LIXO)
107M  drive-download-20250923.zip        ← ZIP duplicado
 65M  drive-download-20250925.zip        ← ZIP duplicado
 44M  @hemodoctor/                       ← ⭐ CÓDIGO-FONTE PRINCIPAL
3.4M  Dicionário Variáveis/              ← Data dictionary
476K  HemoDoctor-SaMD-ANVISA/            ← ANVISA code
+ database/ (migrations, schema, seeds)  ← ⭐ DATABASE ESSENCIAL
+ docs/, tests/, admin/                  ← Suporte
```

**Total ZIPs duplicados:** ~444 MB (73% do total!)

**DECISÃO:**
- ✅ Extrair para CONSOLIDADO:
  - `@hemodoctor/` → `03_DESENVOLVIMENTO/CODIGO_FONTE/`
  - `database/` → `03_DESENVOLVIMENTO/DATABASE/`
  - `HemoDoctor-SaMD-ANVISA/` → `03_DESENVOLVIMENTO/ANVISA_CODE/`
  - `Dicionário Variáveis/` → `03_DESENVOLVIMENTO/DATA_DICTIONARY/`
- ❌ Arquivar: ZIPs, docs duplicados, testes antigos

**Economia:** ~500 MB (82%)

---

### **3. hemodoctor versao fabio/** (13 MB)

**Estrutura analisada:**
```
agents/                                  ← 10 agentes (já instalados em ~/.claude/agents/)
  ├── anvisa-regulatory-specialist/
  ├── clinical-evidence-specialist/
  ├── software-architecture-specialist/
  ├── risk-management-specialist/
  ├── quality-systems-specialist/
  ├── traceability-specialist/
  ├── regulatory-review-specialist/
  ├── hematology-technical-specialist/
  ├── documentation-finalization-specialist/
  └── external-regulatory-consultant/
docs/                                    ← Documentação agentes
docs_anvisa_structured/                  ← Estruturas ANVISA
CEP_Submission_Package_2025/             ← Package CEP
```

**DECISÃO:**
- ✅ Consolidar TUDO em: `HEMODOCTOR_AGENTES/`
  - Specs dos 10 agents
  - Tools/prompts
  - Documentação de uso
  - AGENTS.md, AGENTS_MATRIX.md
  - CEP package (se relevante)
- ❌ Arquivar: pasta original fabio/

**Resultado:** Pasta centralizada para TODOS os agentes

---

## 🎯 ESTRUTURA FINAL PROPOSTA

```
/Users/abelcosta/Documents/HemoDoctor/docs/

├── HEMODOCTOR_CONSOLIDADO_v2.0_20251010/    ⭐⭐⭐ MAIN
│   ├── 01_SUBMISSAO_CEP/
│   ├── 02_SUBMISSAO_ANVISA/
│   ├── 03_DESENVOLVIMENTO/
│   │   ├── CODIGO_FONTE/                    ← NEW (de paulo/)
│   │   ├── DATABASE/                        ← NEW (de paulo/)
│   │   ├── ANVISA_CODE/                     ← NEW (de paulo/)
│   │   ├── DATA_DICTIONARY/                 ← NEW (de paulo/)
│   │   ├── ESPECIFICACOES/
│   │   ├── TESTES/
│   │   ├── API_SPECS/
│   │   └── DECISOES_TECNICAS/
│   ├── 04_ANALISES_ESTRATEGICAS/
│   └── 05_MASTER_DOCUMENTATION/
│
├── HEMODOCTOR_AGENTES/                      ⭐⭐ NEW (de fabio/)
│   ├── 00_README_AGENTES.md
│   ├── AGENTS.md
│   ├── AGENTS_MATRIX.md
│   ├── anvisa-regulatory-specialist/
│   ├── clinical-evidence-specialist/
│   ├── software-architecture-specialist/
│   ├── (... outros 7 agentes)
│   └── docs/
│
├── AUTHORITATIVE_BASELINE/                  ⭐ KEPT (source oficial)
│   └── (11 pastas, 43 arquivos OFICIAIS)
│
├── HEMODOCTOR_REFERENCIAS/                  ⭐ NEW (de fernanda/)
│   ├── powerpoints/                         (HemoDoctor.pptx, etc.)
│   ├── artigos_cientificos/                 (hemodoctor_poc_jamia)
│   └── openapi_schemas/                     (se não em CONSOLIDADO)
│
├── _ARCHIVE_LEGACY_20251010/                📦 ARCHIVED
│   ├── hemodoctor versao fernanda/          (ZIPs, duplicatas)
│   ├── hemodoctor versao paulo/             (ZIPs, build artifacts)
│   ├── hemodoctor versao fabio/             (migrado para HEMODOCTOR_AGENTES/)
│   ├── hemodoctor versao carlos/
│   ├── HemoDoctor versao paula/
│   ├── HemoDoctor versao daniel/
│   └── outputs/
│
└── _ARCHIVE_LEGACY_20251010.tar.gz          📦 COMPRESSED BACKUP
```

---

## 📋 PLANO DE EXECUÇÃO (5 passos)

### **PASSO 1: Extrair código-fonte essencial (de paulo/)**

```bash
# Criar pastas em CONSOLIDADO
mkdir -p HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE
mkdir -p HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/DATABASE
mkdir -p HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/ANVISA_CODE
mkdir -p HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/DATA_DICTIONARY

# Copiar código essencial
cp -r "hemodoctor versao paulo/@hemodoctor" \
      HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/CODIGO_FONTE/

cp -r "hemodoctor versao paulo/database" \
      HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/DATABASE/

cp -r "hemodoctor versao paulo/HemoDoctor-SaMD-ANVISA" \
      HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/ANVISA_CODE/

cp -r "hemodoctor versao paulo/Dicionário Variáveis" \
      HEMODOCTOR_CONSOLIDADO_v2.0_20251010/03_DESENVOLVIMENTO/DATA_DICTIONARY/
```

**Resultado:** ~50 MB código essencial extraído

---

### **PASSO 2: Consolidar agentes (de fabio/)**

```bash
# Criar estrutura HEMODOCTOR_AGENTES/
mkdir -p HEMODOCTOR_AGENTES
cp -r "hemodoctor versao fabio/agents/"* HEMODOCTOR_AGENTES/
cp -r "hemodoctor versao fabio/docs" HEMODOCTOR_AGENTES/
cp "hemodoctor versao paulo/AGENTS.md" HEMODOCTOR_AGENTES/

# Criar README_AGENTES.md
cat > HEMODOCTOR_AGENTES/00_README_AGENTES.md <<'EOF'
# HEMODOCTOR AGENTES - Central de Agentes Claude Code

**Total:** 12 agentes especializados
**Location:** ~/.claude/agents/ (instalados)
**Source:** Esta pasta (specs + docs)

## Agentes HemoDoctor Regulatory (10):
1. anvisa-regulatory-specialist
2. clinical-evidence-specialist
3. software-architecture-specialist
4. risk-management-specialist
5. quality-systems-specialist
6. traceability-specialist
7. regulatory-review-specialist
8. hematology-technical-specialist
9. documentation-finalization-specialist
10. external-regulatory-consultant

## Agentes Novos (2):
11. biostatistics-specialist (2025-10-10)
12. cep-protocol-specialist (2025-10-10)

## Documentação:
- AGENTS.md - Guia completo
- AGENTS_MATRIX.md - Matriz de uso
- docs/ - Documentação técnica
EOF
```

**Resultado:** Pasta centralizada 13 MB

---

### **PASSO 3: Extrair referências (de fernanda/)**

```bash
# Criar HEMODOCTOR_REFERENCIAS/
mkdir -p HEMODOCTOR_REFERENCIAS/powerpoints
mkdir -p HEMODOCTOR_REFERENCIAS/artigos_cientificos

# Copiar PowerPoints executivos
cp "hemodoctor versao fernanda/HemoDoctor.pptx" \
   HEMODOCTOR_REFERENCIAS/powerpoints/

cp "hemodoctor versao fernanda/Pacote-de-Auditoria-e-Prontidao-para-Submissao.pptx" \
   HEMODOCTOR_REFERENCIAS/powerpoints/

# Copiar artigos científicos
cp -r "hemodoctor versao fernanda/hemodoctor_poc_jamia_5_1_artifacts" \
      HEMODOCTOR_REFERENCIAS/artigos_cientificos/

# Verificar se openapi/schemas já estão em CONSOLIDADO
# Se não estiverem:
# cp -r "hemodoctor versao fernanda/openapi" HEMODOCTOR_REFERENCIAS/
# cp -r "hemodoctor versao fernanda/schemas" HEMODOCTOR_REFERENCIAS/
```

**Resultado:** ~100 MB referências organizadas

---

### **PASSO 4: Arquivar pastas legacy**

```bash
# Criar pasta de arquivo
mkdir _ARCHIVE_LEGACY_20251010

# Mover pastas legacy COMPLETAS
mv "hemodoctor versao fernanda" _ARCHIVE_LEGACY_20251010/
mv "hemodoctor versao paulo" _ARCHIVE_LEGACY_20251010/
mv "hemodoctor versao fabio" _ARCHIVE_LEGACY_20251010/
mv "hemodoctor versao carlos - nova" _ARCHIVE_LEGACY_20251010/
mv "HemoDoctor versao paula - nova" _ARCHIVE_LEGACY_20251010/
mv "HemoDoctor versao daniel" _ARCHIVE_LEGACY_20251010/
mv outputs _ARCHIVE_LEGACY_20251010/

# Comprimir
tar -czf _ARCHIVE_LEGACY_20251010.tar.gz _ARCHIVE_LEGACY_20251010/

# Verificar tamanho comprimido
ls -lh _ARCHIVE_LEGACY_20251010.tar.gz
```

**Resultado:** ~1.4 GB → ~300 MB comprimido (economia 78%)

---

### **PASSO 5: Verificar estrutura final**

```bash
# Listar estrutura limpa
ls -lh

# Contar arquivos por pasta
find HEMODOCTOR_CONSOLIDADO_v2.0_20251010 -type f | wc -l
find HEMODOCTOR_AGENTES -type f | wc -l
find HEMODOCTOR_REFERENCIAS -type f | wc -l
find AUTHORITATIVE_BASELINE -type f | wc -l

# Tamanho total
du -sh HEMODOCTOR_*
du -sh AUTHORITATIVE_BASELINE
du -sh _ARCHIVE_LEGACY_20251010.tar.gz
```

---

## 📊 MÉTRICAS ESPERADAS

| Antes | Depois | Economia |
|-------|--------|----------|
| **7 pastas legacy** (1.5 GB) | **4 pastas organizadas** (~250 MB) | **83% redução** |
| hemodoctor versao X/ (7 pastas) | 1 arquivo .tar.gz (~300 MB) | Backup comprimido |
| Código espalhado | CODIGO_FONTE/, DATABASE/ organizados | 100% extraído |
| Agentes em fabio/ | HEMODOCTOR_AGENTES/ centralizado | 100% consolidado |
| Duplicatas (ZIPs) | Eliminadas (~900 MB) | 100% removidas |

---

## ✅ RESULTADO ESPERADO

**Estrutura final:**
```
docs/
├── HEMODOCTOR_CONSOLIDADO_v2.0_20251010/  (~150 MB)
├── HEMODOCTOR_AGENTES/                     (~13 MB)
├── HEMODOCTOR_REFERENCIAS/                 (~100 MB)
├── AUTHORITATIVE_BASELINE/                 (~10 MB)
└── _ARCHIVE_LEGACY_20251010.tar.gz         (~300 MB)
```

**Total visível:** ~273 MB (was 1.5 GB)
**Economia espaço:** **82% redução**
**Backup:** 300 MB comprimido (fácil recuperar se necessário)

---

**Aprovado por:** Abel Costa
**Data execução:** 2025-10-11
**Tempo estimado:** 15-20 minutos
