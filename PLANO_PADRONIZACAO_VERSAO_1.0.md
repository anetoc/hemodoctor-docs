# 📋 Plano de Padronização - Versão 1.0 Unificada

**Data de Criação**: 12 de Outubro de 2025  
**Responsável**: Dr. Abel Costa - IDOR-SP  
**Agente Recomendado**: `documentation-finalization-specialist`  
**Objetivo**: Unificar todas as versões de documentos para v1.0

---

## 🎯 Objetivo

Padronizar **todos os documentos do AUTHORITATIVE_BASELINE** para a versão **v1.0**, criando uma baseline unificada e submission-ready para a primeira submissão oficial ANVISA.

---

## 📊 Status Atual das Versões

### Documentos com Versões Múltiplas

| Módulo | Documento | Versão Atual | → Versão Alvo |
|--------|-----------|--------------|---------------|
| 01 - Regulatório | DMR | v2.0 | → v1.0 |
| 02 - Controles Design | SRS | v2.2 | → v1.0 |
| 02 - Controles Design | SDD | v2.0 | → v1.0 |
| 02 - Controles Design | TEC | v1.0 | ✅ (já está) |
| 02 - Controles Design | API Specs | v1.0 | ✅ (já está) |
| 03 - Gestão Risco | RMP | v1.0 | ✅ (já está) |
| 04 - V&V | TST | v1.0 | ✅ (já está) |
| 05 - Avaliação Clínica | CER | v1.2 | → v1.0 |
| 06 - Rastreabilidade | TRC | v2.1 | → v1.0 |
| 07 - Pós-Mercado | PMS | v1.1 | → v1.0 |
| 08 - Rotulagem | IFU | v1.0 | ✅ (já está) |
| 09 - Cybersecurity | SEC | v1.0 | ✅ (já está) |
| 09 - Cybersecurity | SBOM | v1.0 | ✅ (já está) |
| 10 - SOUP | SOUP | v1.0 | ✅ (já está) |

### Resumo

- ✅ **Já em v1.0**: 8 documentos
- ⚠️ **Precisam padronização**: 6 documentos
  - DMR v2.0 → v1.0
  - SRS v2.2 → v1.0
  - SDD v2.0 → v1.0
  - CER v1.2 → v1.0
  - TRC v2.1 → v1.0
  - PMS v1.1 → v1.0

---

## 🔄 Estratégia de Padronização

### Opção A: Renomear Mantendo Histórico (RECOMENDADA)

**Vantagem**: Preserva evolução histórica dos documentos

**Estratégia**:
1. Renomear arquivos v2.x/v1.x para v1.0_OFICIAL
2. Mover versões antigas para `/AUTHORITATIVE_BASELINE/00_HISTORICO/`
3. Atualizar todas as referências cruzadas
4. Documentar mudanças de versão no CHANGELOG.md

**Exemplo**:
```
Antes: SRS-001_Software_Requirements_v2.2_OFICIAL.md
Depois: SRS-001_Software_Requirements_v1.0_OFICIAL.md

Versão antiga movida para:
00_HISTORICO/02_CONTROLES_DESIGN/SRS-001_v2.2_ARCHIVE.md
```

### Opção B: Consolidar e Resetar (LIMPEZA TOTAL)

**Vantagem**: Baseline completamente limpa

**Estratégia**:
1. Deletar versões intermediárias
2. Renomear versões finais para v1.0
3. Iniciar histórico de versões do zero
4. Documentar como "Primeira Submissão Oficial"

---

## 📝 Plano de Execução - 4 Fases

### **Fase 1: Auditoria e Mapeamento** (2 horas)

**Agente**: `documentation-finalization-specialist`

**Tarefas**:
1. [ ] Listar todos os documentos atuais com versões
2. [ ] Identificar todas as referências cruzadas entre documentos
3. [ ] Mapear dependências de versionamento
4. [ ] Criar matriz de impacto de mudança de versões

**Comando**:
```bash
# Como documentation-finalization-specialist
/document-index-master hierarchical hyperlinked
```

**Output Esperado**:
- `RELATORIO_MAPEAMENTO_VERSOES.md`
- `MATRIZ_REFERENCIAS_CRUZADAS.xlsx`

---

### **Fase 2: Backup e Preparação** (1 hora)

**Tarefas**:
1. [ ] Criar branch Git: `feature/versao-1.0-unificada`
2. [ ] Criar diretório `00_HISTORICO/` em AUTHORITATIVE_BASELINE
3. [ ] Backup completo do estado atual
4. [ ] Documentar estado "antes" para comparação

**Comandos**:
```bash
git checkout -b feature/versao-1.0-unificada
mkdir -p AUTHORITATIVE_BASELINE/00_HISTORICO/{01..10}_MODULOS
```

---

### **Fase 3: Execução da Padronização** (4-6 horas)

**Agente**: `documentation-finalization-specialist`

**Comando Principal**:
```bash
# Como documentation-finalization-specialist
/version-control-final all-docs v1.0-unificada
```

**Subtarefas Detalhadas**:

#### 3.1. Módulo 02 - SRS e SDD
1. [ ] Mover `SRS-001_v2.2_OFICIAL.md` → `00_HISTORICO/02_CONTROLES_DESIGN/SRS-001_v2.2_ARCHIVE.md`
2. [ ] Copiar conteúdo para `SRS-001_Software_Requirements_v1.0_OFICIAL.md`
3. [ ] Atualizar header do documento:
   ```yaml
   version: "1.0"
   status: "OFICIAL - Primeira Submissão ANVISA"
   history:
     - version: "1.0"
       date: "2025-10-12"
       changes: "Versão unificada para primeira submissão oficial"
       previous_versions: ["v2.2", "v2.1", "v2.0", "v1.1", "v1.0"]
   ```
4. [ ] Repetir processo para SDD v2.0 → v1.0

#### 3.2. Módulo 01 - DMR
1. [ ] `DMR-001_v2.0_OFICIAL.md` → `00_HISTORICO/01_REGULATORIO/`
2. [ ] Renomear para `DMR-001_Device_Master_Record_v1.0_OFICIAL.md`
3. [ ] Atualizar versão e histórico

#### 3.3. Módulo 05 - CER
1. [ ] `CER-001_v1.2_OFICIAL.md` → `00_HISTORICO/05_AVALIACAO_CLINICA/`
2. [ ] Renomear para `CER-001_Clinical_Evaluation_Report_v1.0_OFICIAL.md`

#### 3.4. Módulo 06 - TRC
1. [ ] `TRC-001_v2.1_OFICIAL.md` → `00_HISTORICO/06_RASTREABILIDADE/`
2. [ ] Renomear para `TRC-001_Traceability_Matrix_v1.0_OFICIAL.md`

#### 3.5. Módulo 07 - PMS
1. [ ] `PMS-001_v1.1_OFICIAL.md` → `00_HISTORICO/07_POS_MERCADO/`
2. [ ] Renomear para `PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md`

---

### **Fase 4: Validação e Atualização de Referências** (3-4 horas)

**Agente**: `documentation-finalization-specialist`

**Tarefas**:

#### 4.1. Atualizar Referências Cruzadas
1. [ ] Executar busca global por referências de versão antiga:
   ```bash
   grep -r "v2.2" AUTHORITATIVE_BASELINE/
   grep -r "v2.0" AUTHORITATIVE_BASELINE/
   grep -r "v1.2" AUTHORITATIVE_BASELINE/
   grep -r "v2.1" AUTHORITATIVE_BASELINE/
   grep -r "v1.1" AUTHORITATIVE_BASELINE/
   ```

2. [ ] Atualizar todas as referências para v1.0

**Comando**:
```bash
# Como documentation-finalization-specialist
/cross-reference-integration all-67-docs master-matrix
```

#### 4.2. Validar Consistência
1. [ ] Verificar que todos os links internos funcionam
2. [ ] Confirmar nomenclatura padronizada
3. [ ] Validar headers de todos os documentos

**Comando**:
```bash
# Como documentation-finalization-specialist
/document-quality-assurance all-PKGs ANVISA-standards
```

#### 4.3. Atualizar Documentação do Repositório
1. [ ] Atualizar `VERSION.md`:
   ```yaml
   version: "1.0.0"
   baseline_version: "1.0"
   description: "Baseline unificada - Primeira submissão oficial ANVISA"
   all_documents: "v1.0"
   ```

2. [ ] Atualizar `CHANGELOG.md`:
   ```markdown
   ## [1.0.0] - 2025-10-12
   
   ### 🎯 Baseline Unificada - Primeira Submissão Oficial
   
   #### Padronizado
   - Todos os documentos oficiais unificados para v1.0
   - DMR: v2.0 → v1.0
   - SRS: v2.2 → v1.0
   - SDD: v2.0 → v1.0
   - CER: v1.2 → v1.0
   - TRC: v2.1 → v1.0
   - PMS: v1.1 → v1.0
   
   #### Adicionado
   - Diretório 00_HISTORICO/ com versões anteriores arquivadas
   - Headers padronizados em todos os documentos
   - Histórico de evolução documentado
   ```

3. [ ] Atualizar `README.md` com versões v1.0

---

## 🔍 Checklist de Validação Final

### Documentos
- [ ] Todos os 42+ documentos oficiais têm versão v1.0
- [ ] Nomenclatura consistente: `CODIGO-XXX_Nome_v1.0_OFICIAL.md`
- [ ] Headers padronizados com:
  - version: "1.0"
  - status: "OFICIAL"
  - history: documentado
  - previous_versions: listadas

### Referências Cruzadas
- [ ] Todas as referências a versões antigas atualizadas
- [ ] Links internos funcionando
- [ ] TRC atualizada com v1.0 de todos os documentos

### Repositório
- [ ] VERSION.md atualizado para v1.0.0
- [ ] CHANGELOG.md documentado
- [ ] README.md atualizado
- [ ] 00_HISTORICO/ criado e populado

### Git
- [ ] Branch `feature/versao-1.0-unificada` criada
- [ ] Commits atômicos por módulo
- [ ] Mensagens de commit descritivas
- [ ] Tag `v1.0.0-baseline-unificada` criada

---

## 📊 Matriz de Referências Cruzadas a Atualizar

| Documento | Referencia | Versão Antiga | → Nova |
|-----------|-----------|---------------|--------|
| TRC v1.0 | SRS | v2.2 | v1.0 |
| TRC v1.0 | SDD | v2.0 | v1.0 |
| TRC v1.0 | DMR | v2.0 | v1.0 |
| SDD v1.0 | SRS | v2.2 | v1.0 |
| RMP v1.0 | SRS | v2.2 | v1.0 |
| TST v1.0 | SRS | v2.2 | v1.0 |
| TST v1.0 | SDD | v2.0 | v1.0 |
| PMS v1.0 | CER | v1.2 | v1.0 |
| CER v1.0 | DMR | v2.0 | v1.0 |

---

## ⏱️ Timeline Estimado

| Fase | Duração | Responsável |
|------|---------|-------------|
| Fase 1: Auditoria | 2 horas | documentation-finalization-specialist |
| Fase 2: Backup | 1 hora | Dev/Git |
| Fase 3: Execução | 4-6 horas | documentation-finalization-specialist |
| Fase 4: Validação | 3-4 horas | documentation-finalization-specialist + qa |
| **TOTAL** | **10-13 horas** | **1-2 dias de trabalho** |

---

## 🚀 Comandos para Iniciar

### 1. Ativar o Agente

No Cursor, abrir chat com o agente:

```
@documentation-finalization-specialist Olá! Preciso padronizar todos os documentos do AUTHORITATIVE_BASELINE para versão v1.0 unificada. 

Vamos seguir o PLANO_PADRONIZACAO_VERSAO_1.0.md que está na raiz do repositório.

Podemos começar pela Fase 1 (Auditoria e Mapeamento)?
```

### 2. Comandos Específicos do Agente

```bash
# Fase 1: Auditoria
/document-index-master hierarchical hyperlinked

# Fase 3: Execução principal
/version-control-final all-docs v1.0-unificada

# Fase 4: Validação
/cross-reference-integration all-docs master-matrix
/document-quality-assurance all-PKGs ANVISA-standards
/compliance-final-validation RDC657+751 complete-evidence
```

---

## 📝 Estrutura Final Esperada

```
AUTHORITATIVE_BASELINE/
├── 00_HISTORICO/                    ✨ NOVO
│   ├── README.md                    (Explica arquivo de versões antigas)
│   ├── 01_REGULATORIO/
│   │   └── DMR-001_v2.0_ARCHIVE.md
│   ├── 02_CONTROLES_DESIGN/
│   │   ├── SRS-001_v2.2_ARCHIVE.md
│   │   └── SDD-001_v2.0_ARCHIVE.md
│   ├── 05_AVALIACAO_CLINICA/
│   │   └── CER-001_v1.2_ARCHIVE.md
│   ├── 06_RASTREABILIDADE/
│   │   └── TRC-001_v2.1_ARCHIVE.md
│   └── 07_POS_MERCADO/
│       └── PMS-001_v1.1_ARCHIVE.md
├── 01_REGULATORIO/
│   └── DMR/
│       └── DMR-001_Device_Master_Record_v1.0_OFICIAL.md  ✅
├── 02_CONTROLES_DESIGN/
│   ├── SRS/
│   │   └── SRS-001_Software_Requirements_v1.0_OFICIAL.md  ✅
│   └── SDD/
│       └── SDD-001_Software_Design_v1.0_OFICIAL.md  ✅
├── 05_AVALIACAO_CLINICA/
│   └── CER/
│       └── CER-001_Clinical_Evaluation_v1.0_OFICIAL.md  ✅
├── 06_RASTREABILIDADE/
│   └── TRC/
│       └── TRC-001_Traceability_Matrix_v1.0_OFICIAL.md  ✅
└── 07_POS_MERCADO/
    └── PMS/
        └── PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md  ✅
```

---

## ✅ Critérios de Sucesso

1. ✅ **100% documentos em v1.0**: Todos os documentos oficiais padronizados
2. ✅ **Histórico preservado**: Versões antigas arquivadas em 00_HISTORICO/
3. ✅ **Referências atualizadas**: Todas as referências cruzadas corretas
4. ✅ **Headers padronizados**: Formato consistente em todos os documentos
5. ✅ **Git organizado**: Branch, commits e tag criados
6. ✅ **Documentação atualizada**: VERSION.md, CHANGELOG.md, README.md
7. ✅ **QA aprovado**: Validação final do quality-systems-specialist

---

## 📞 Contatos e Aprovações

**Responsável Técnico**: Dr. Abel Costa  
**Aprovação Regulatória**: Necessária após conclusão  
**Aprovação Qualidade**: Necessária após Fase 4

---

**Status**: 📝 Pronto para execução  
**Próximo Passo**: Ativar `@documentation-finalization-specialist` e iniciar Fase 1

