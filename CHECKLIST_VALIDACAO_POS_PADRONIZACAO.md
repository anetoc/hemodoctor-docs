# ✅ Checklist de Validação Pós-Padronização v1.0

**Data**: 12 de Outubro de 2025  
**Responsável**: Dr. Abel Costa - IDOR-SP  
**Status**: Template para execução após Fases 1-4

---

## 🎯 Propósito

Este checklist garante que a padronização v1.0 foi executada corretamente e está pronta para submissão ANVISA.

---

## 📋 PARTE 1: Validação de Estrutura

### 1.1. Diretórios Criados

- [ ] `/AUTHORITATIVE_BASELINE/00_HISTORICO/` existe
- [ ] `/AUTHORITATIVE_BASELINE/00_HISTORICO/01_REGULATORIO/` existe
- [ ] `/AUTHORITATIVE_BASELINE/00_HISTORICO/02_CONTROLES_DESIGN/` existe
- [ ] `/AUTHORITATIVE_BASELINE/00_HISTORICO/05_AVALIACAO_CLINICA/` existe
- [ ] `/AUTHORITATIVE_BASELINE/00_HISTORICO/06_RASTREABILIDADE/` existe
- [ ] `/AUTHORITATIVE_BASELINE/00_HISTORICO/07_POS_MERCADO/` existe
- [ ] `/AUTHORITATIVE_BASELINE/00_HISTORICO/README.md` existe e está completo

**Comando para verificar**:
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs
ls -la AUTHORITATIVE_BASELINE/00_HISTORICO/
```

---

## 📋 PARTE 2: Validação de Documentos Arquivados

### 2.1. Versões Antigas Arquivadas

- [ ] `00_HISTORICO/01_REGULATORIO/DMR-001_v2.0_ARCHIVE.md` existe
- [ ] `00_HISTORICO/02_CONTROLES_DESIGN/SRS-001_v2.2_ARCHIVE.md` existe
- [ ] `00_HISTORICO/02_CONTROLES_DESIGN/SDD-001_v2.0_ARCHIVE.md` existe
- [ ] `00_HISTORICO/05_AVALIACAO_CLINICA/CER-001_v1.2_ARCHIVE.md` existe
- [ ] `00_HISTORICO/06_RASTREABILIDADE/TRC-001_v2.1_ARCHIVE.md` existe
- [ ] `00_HISTORICO/07_POS_MERCADO/PMS-001_v1.1_ARCHIVE.md` existe

**Comando para verificar**:
```bash
find AUTHORITATIVE_BASELINE/00_HISTORICO/ -name "*_ARCHIVE.md" | sort
```

**Resultado esperado**: 6 arquivos listados

---

## 📋 PARTE 3: Validação de Documentos v1.0

### 3.1. Nomenclatura Correta

Todos os documentos oficiais devem seguir o padrão:
`{CODIGO}-{NUM}_{Nome}_v1.0_OFICIAL.md`

**Verificar cada documento**:

- [ ] `01_REGULATORIO/DMR/DMR-001_Device_Master_Record_v1.0_OFICIAL.md`
- [ ] `02_CONTROLES_DESIGN/SRS/SRS-001_Software_Requirements_v1.0_OFICIAL.md`
- [ ] `02_CONTROLES_DESIGN/SDD/SDD-001_Software_Design_v1.0_OFICIAL.md`
- [ ] `02_CONTROLES_DESIGN/TEC/TEC-001_Technical_Documentation_v1.0_OFICIAL.md`
- [ ] `03_GESTAO_RISCO/RMP/RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md`
- [ ] `04_VERIFICACAO_VALIDACAO/TST/TST-001_Test_Specification_v1.0_OFICIAL.md`
- [ ] `05_AVALIACAO_CLINICA/CER/CER-001_Clinical_Evaluation_v1.0_OFICIAL.md`
- [ ] `06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v1.0_OFICIAL.md`
- [ ] `07_POS_MERCADO/PMS/PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md`
- [ ] `08_ROTULAGEM/IFU/IFU-001_*_v1.0_OFICIAL.pdf` (2 arquivos: PT-BR e EN-US)
- [ ] `09_CYBERSECURITY/SEC/SEC-001_Security_Documentation_v1.0_OFICIAL.md`
- [ ] `09_CYBERSECURITY/SBOM/SBOM-001_*_v1.0_OFICIAL.*`
- [ ] `10_SOUP/SOUP-001_Analysis_v1.0_OFICIAL.md`

**Comando para listar todos**:
```bash
find AUTHORITATIVE_BASELINE/ -name "*_v1.0_OFICIAL.*" | sort
```

**Resultado esperado**: 14+ arquivos (alguns módulos têm múltiplos arquivos)

### 3.2. Verificar que NÃO existem versões antigas fora de 00_HISTORICO/

- [ ] NÃO existe nenhum arquivo v2.2 em SRS/
- [ ] NÃO existe nenhum arquivo v2.0 em SDD/
- [ ] NÃO existe nenhum arquivo v2.0 em DMR/
- [ ] NÃO existe nenhum arquivo v1.2 em CER/
- [ ] NÃO existe nenhum arquivo v2.1 em TRC/
- [ ] NÃO existe nenhum arquivo v1.1 em PMS/

**Comando para verificar**:
```bash
# Buscar versões antigas fora de 00_HISTORICO
find AUTHORITATIVE_BASELINE/ -name "*v2.2*.md" ! -path "*/00_HISTORICO/*"
find AUTHORITATIVE_BASELINE/ -name "*v2.0*.md" ! -path "*/00_HISTORICO/*"
find AUTHORITATIVE_BASELINE/ -name "*v1.2*.md" ! -path "*/00_HISTORICO/*"
find AUTHORITATIVE_BASELINE/ -name "*v2.1*.md" ! -path "*/00_HISTORICO/*"
find AUTHORITATIVE_BASELINE/ -name "*v1.1*.md" ! -path "*/00_HISTORICO/*"
```

**Resultado esperado**: Nenhum arquivo encontrado

---

## 📋 PARTE 4: Validação de Headers dos Documentos

### 4.1. Header Padrão v1.0

Cada documento v1.0 deve ter header no formato:

```yaml
---
document_id: "{CODIGO}-{NUM}"
title: "{Título Completo}"
version: "1.0"
status: "OFICIAL"
date: "2025-10-12"
author: "Dr. Abel Costa"
organization: "IDOR-SP"
classification: "Dispositivo Médico - Classe II"
history:
  - version: "1.0"
    date: "2025-10-12"
    changes: "Versão unificada para primeira submissão oficial ANVISA"
    previous_versions: [lista de versões anteriores]
    author: "Dr. Abel Costa"
---
```

**Verificar manualmente em cada documento v1.0**:

- [ ] DMR-001 v1.0: Header correto e completo
- [ ] SRS-001 v1.0: Header correto e completo
- [ ] SDD-001 v1.0: Header correto e completo
- [ ] TEC-001 v1.0: Header correto e completo
- [ ] RMP-001 v1.0: Header correto e completo
- [ ] TST-001 v1.0: Header correto e completo
- [ ] CER-001 v1.0: Header correto e completo
- [ ] TRC-001 v1.0: Header correto e completo
- [ ] PMS-001 v1.0: Header correto e completo
- [ ] SEC-001 v1.0: Header correto e completo
- [ ] SOUP-001 v1.0: Header correto e completo

**Comando auxiliar**:
```bash
# Verificar se todos têm version: "1.0"
grep -r 'version:' AUTHORITATIVE_BASELINE/ --include="*_OFICIAL.md" | grep -v "00_HISTORICO"
```

---

## 📋 PARTE 5: Validação de Referências Cruzadas

### 5.1. Buscar Referências a Versões Antigas

Não deve haver referências a versões antigas nos documentos v1.0:

- [ ] Nenhuma referência a "v2.2" (exceto em history)
- [ ] Nenhuma referência a "v2.0" (exceto em history)
- [ ] Nenhuma referência a "v1.2" (exceto em history)
- [ ] Nenhuma referência a "v2.1" (exceto em history)
- [ ] Nenhuma referência a "v1.1" (exceto em history)

**Comandos de verificação**:
```bash
# Buscar referências problemáticas (fora de 00_HISTORICO e seção history)
grep -r "SRS.*v2\.2" AUTHORITATIVE_BASELINE/ --include="*.md" ! -path "*/00_HISTORICO/*" | grep -v "previous_versions"
grep -r "SDD.*v2\.0" AUTHORITATIVE_BASELINE/ --include="*.md" ! -path "*/00_HISTORICO/*" | grep -v "previous_versions"
grep -r "DMR.*v2\.0" AUTHORITATIVE_BASELINE/ --include="*.md" ! -path "*/00_HISTORICO/*" | grep -v "previous_versions"
grep -r "CER.*v1\.2" AUTHORITATIVE_BASELINE/ --include="*.md" ! -path "*/00_HISTORICO/*" | grep -v "previous_versions"
grep -r "TRC.*v2\.1" AUTHORITATIVE_BASELINE/ --include="*.md" ! -path "*/00_HISTORICO/*" | grep -v "previous_versions"
grep -r "PMS.*v1\.1" AUTHORITATIVE_BASELINE/ --include="*.md" ! -path "*/00_HISTORICO/*" | grep -v "previous_versions"
```

**Resultado esperado**: Nenhuma referência encontrada (ou apenas em contexto de histórico)

### 5.2. Validar Referências Corretas para v1.0

Documentos devem referenciar versões v1.0:

- [ ] TRC referencia SRS v1.0 (não v2.2)
- [ ] TRC referencia SDD v1.0 (não v2.0)
- [ ] SDD referencia SRS v1.0 (não v2.2)
- [ ] RMP referencia SRS v1.0 (não v2.2)
- [ ] TST referencia SRS v1.0 e SDD v1.0

**Comando para verificar TRC especificamente**:
```bash
# TRC deve ter apenas referências v1.0
grep -i "version\|v1\.0\|v2\." AUTHORITATIVE_BASELINE/06_RASTREABILIDADE/TRC/*v1.0*.md | head -20
```

---

## 📋 PARTE 6: Validação de Links Internos

### 6.1. Testar Links entre Documentos

Verificar que links relativos funcionam:

- [ ] Links no README.md principal funcionam
- [ ] Links no TRC para outros documentos funcionam
- [ ] Links entre SRS e SDD funcionam
- [ ] Links no RMP para outros documentos funcionam

**Teste manual**: Abrir cada documento no editor e clicar nos links internos.

**Comando auxiliar** (encontrar todos os links markdown):
```bash
# Listar todos os links markdown
grep -r "\[.*\](.*.md)" AUTHORITATIVE_BASELINE/ --include="*.md" ! -path "*/00_HISTORICO/*" | head -30
```

---

## 📋 PARTE 7: Validação de Documentação do Repositório

### 7.1. VERSION.md

- [ ] `VERSION.md` existe na raiz
- [ ] version: "1.0.0" ou superior
- [ ] baseline_version: "1.0"
- [ ] Todos os módulos listados com v1.0
- [ ] Seção de histórico atualizada
- [ ] Roadmap presente

**Verificar conteúdo**:
```bash
head -50 VERSION.md | grep -E "version:|baseline_version:"
```

### 7.2. CHANGELOG.md

- [ ] `CHANGELOG.md` existe na raiz
- [ ] Entrada para v1.0.0 ou superior existe
- [ ] Lista de documentos padronizados presente
- [ ] Data (2025-10-12) documentada
- [ ] Justificativa da padronização presente

**Verificar entrada**:
```bash
grep -A 30 "## \[1.0.0\]" CHANGELOG.md
```

### 7.3. README.md

- [ ] `README.md` existe na raiz
- [ ] Todos os documentos listados com v1.0
- [ ] Referência ao VERSION.md presente
- [ ] Status "SUBMISSION READY" confirmado
- [ ] Data de atualização: 12 Out 2025 ou posterior

**Verificar versões listadas**:
```bash
grep -E "v[0-9]\.[0-9]" README.md | head -20
```

---

## 📋 PARTE 8: Validação Git

### 8.1. Branch e Commits

- [ ] Branch `feature/versao-1.0-unificada` existe
- [ ] Commits atômicos por módulo realizados
- [ ] Mensagens de commit descritivas
- [ ] Todos os arquivos commitados

**Verificar branch**:
```bash
git branch -a | grep "versao-1.0"
```

**Verificar commits**:
```bash
git log --oneline feature/versao-1.0-unificada | head -20
```

### 8.2. Tag Git

- [ ] Tag `v1.0.0-baseline-unificada` criada
- [ ] Tag tem mensagem descritiva
- [ ] Tag enviada para GitHub

**Verificar tag**:
```bash
git tag -l "*baseline*"
git show v1.0.0-baseline-unificada
```

### 8.3. Estado Git Limpo

- [ ] Não há arquivos não rastreados importantes
- [ ] Não há modificações pendentes de commit
- [ ] Branch está sincronizada com remote

**Verificar estado**:
```bash
git status
```

---

## 📋 PARTE 9: Validação de Backup

### 9.1. Arquivos de Backup

- [ ] Backup `.tar.gz` criado antes da padronização
- [ ] Backup contém estado completo pré-v1.0
- [ ] Backup está em local seguro fora do repositório
- [ ] Nome do backup inclui timestamp

**Verificar backup**:
```bash
ls -lh ~/Documents/HemoDoctor/docs_backup_*.tar.gz
```

### 9.2. Snapshot do Estado Anterior

- [ ] Arquivo `SNAPSHOT_ANTES_V1.0_UNIFICADA.md` existe
- [ ] Lista completa de documentos pré-padronização
- [ ] Versões antigas documentadas

---

## 📋 PARTE 10: Validação Final com Agente

### 10.1. Comando QA do Agente

Executar com `documentation-finalization-specialist`:

```
Execute validação final completa:
/compliance-final-validation RDC657+751 complete-evidence

Gere relatório de conformidade final: RELATORIO_VALIDACAO_FINAL_V1.0.md
```

- [ ] Comando executado
- [ ] Relatório gerado
- [ ] Status: PASS ou APROVADO
- [ ] Nenhum issue crítico identificado

### 10.2. Checklist do Agente

- [ ] 100% documentos em v1.0
- [ ] 100% referências cruzadas corretas
- [ ] 100% headers padronizados
- [ ] 100% nomenclatura consistente
- [ ] 100% histórico preservado

---

## 📊 RESUMO DE VALIDAÇÃO

### Critérios de Aprovação

Para considerar a padronização v1.0 **APROVADA**, todos os itens abaixo devem ser **SIM**:

| Critério | Status | Observações |
|----------|--------|-------------|
| Estrutura de diretórios correta | ⬜ | 00_HISTORICO/ completo |
| 6 documentos arquivados em 00_HISTORICO/ | ⬜ | Versões antigas preservadas |
| 14+ documentos v1.0 nos módulos principais | ⬜ | Nomenclatura correta |
| Nenhuma versão antiga fora de 00_HISTORICO/ | ⬜ | Busca confirmada |
| Headers v1.0 em 100% dos documentos | ⬜ | Formato padronizado |
| Referências cruzadas atualizadas | ⬜ | Nenhuma ref a versões antigas |
| Links internos funcionando | ⬜ | Testado manualmente |
| VERSION.md atualizado | ⬜ | baseline_version: 1.0 |
| CHANGELOG.md atualizado | ⬜ | Entrada v1.0.0 presente |
| README.md atualizado | ⬜ | Todos docs em v1.0 |
| Git: Branch criada | ⬜ | feature/versao-1.0-unificada |
| Git: Commits realizados | ⬜ | Mensagens descritivas |
| Git: Tag criada | ⬜ | v1.0.0-baseline-unificada |
| Backup realizado | ⬜ | .tar.gz seguro |
| Validação final agente PASS | ⬜ | Relatório aprovado |

### Resultado Final

- [ ] ✅ **APROVADO** - Todos os critérios atendidos, pronto para próximos passos
- [ ] ⚠️ **APROVADO COM RESSALVAS** - Issues menores identificados, documentar e proceder
- [ ] ❌ **REPROVADO** - Issues críticos, correção necessária antes de prosseguir

---

## 🚨 Issues Encontrados

Se algum item falhou, documentar aqui:

### Issue #1
- **Descrição**: 
- **Severidade**: (Crítica/Alta/Média/Baixa)
- **Ação Corretiva**: 
- **Responsável**: 
- **Prazo**: 

### Issue #2
- **Descrição**: 
- **Severidade**: 
- **Ação Corretiva**: 
- **Responsável**: 
- **Prazo**: 

---

## ✅ Aprovação Final

### Assinaturas

**Responsável Técnico**: _______________________  
Dr. Abel Costa  
Data: ___/___/2025

**Qualidade**: _______________________  
Sistema de Gestão da Qualidade  
Data: ___/___/2025

**Regulatório** (se aplicável): _______________________  
Data: ___/___/2025

---

## 📞 Contato

**Dúvidas sobre validação**: quality-hemodoctor@idor.org  
**Issues técnicos**: dev-hemodoctor@idor.org

---

**Próximo Documento**: `PROXIMOS_PASSOS_POS_V1.0.md`

---

**Status**: ⏳ Aguardando execução após conclusão das Fases 1-4  
**Versão deste Checklist**: 1.0  
**Última Atualização**: 12 de Outubro de 2025

