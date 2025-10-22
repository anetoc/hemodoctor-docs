# 📚 Histórico de Versões - AUTHORITATIVE_BASELINE

**Propósito**: Arquivo de versões anteriores dos documentos oficiais.  
**Data de Criação**: 12 de Outubro de 2025

---

## 📋 Por que este diretório existe?

Durante a **padronização para v1.0 unificada** (12 de Outubro de 2025), preservamos as versões anteriores dos documentos oficiais para:

1. ✅ **Rastreabilidade**: Manter histórico completo de evolução dos documentos
2. ✅ **Compliance**: Documentar todas as mudanças regulatórias para auditoria
3. ✅ **Referência**: Consulta de decisões de design e requisitos anteriores
4. ✅ **Auditoria**: Evidência de processo de desenvolvimento sistemático
5. ✅ **ISO 13485**: Conformidade com requisitos de controle de documentos

---

## 🗂️ Estrutura

```
00_HISTORICO/
├── README.md (este arquivo)
├── 01_REGULATORIO/
│   └── DMR-001_v2.0_ARCHIVE.md
├── 02_CONTROLES_DESIGN/
│   ├── SRS-001_v2.2_ARCHIVE.md
│   ├── SRS-001_v2.1_ARCHIVE.md (se existir)
│   ├── SRS-001_v2.0_ARCHIVE.md (se existir)
│   ├── SDD-001_v2.0_ARCHIVE.md
│   └── SDD-001_v1.1_ARCHIVE.md (se existir)
├── 05_AVALIACAO_CLINICA/
│   ├── CER-001_v1.2_ARCHIVE.md
│   └── CER-001_v1.1_ARCHIVE.md (se existir)
├── 06_RASTREABILIDADE/
│   ├── TRC-001_v2.1_ARCHIVE.md
│   └── TRC-001_v2.0_ARCHIVE.md (se existir)
└── 07_POS_MERCADO/
    └── PMS-001_v1.1_ARCHIVE.md
```

---

## 📝 Convenção de Nomenclatura

### Formato Padrão
```
{CODIGO}-{NUMERO}_v{VERSAO}_ARCHIVE.{extensao}
```

### Exemplos
- `SRS-001_v2.2_ARCHIVE.md` → Versão 2.2 do SRS arquivada
- `DMR-001_v2.0_ARCHIVE.md` → Versão 2.0 do DMR arquivada
- `CER-001_v1.2_ARCHIVE.md` → Versão 1.2 do CER arquivada

### Regras
- ✅ Sufixo `_ARCHIVE` obrigatório
- ✅ Versão sempre explícita no nome
- ✅ Extensão original preservada (.md, .pdf, .xlsx, etc.)
- ✅ Código e número mantidos do documento original

---

## ⚠️ Importante - Como Usar

### ❌ NÃO Faça
- ❌ **NÃO use** documentos deste diretório para desenvolvimento ativo
- ❌ **NÃO referencie** estes documentos em documentação oficial atual
- ❌ **NÃO modifique** arquivos arquivados (são histórico imutável)
- ❌ **NÃO delete** arquivos sem aprovação do controle de documentos

### ✅ Faça
- ✅ **Use apenas para consulta** histórica e rastreabilidade
- ✅ **Referencie** versões atuais (v1.0) nos módulos principais
- ✅ **Documente** referências a versões históricas se necessário
- ✅ **Preserve** como evidência de auditoria

---

## 🔍 Como Encontrar Versão Atual (v1.0)

As versões **oficiais v1.0** estão nos módulos principais da AUTHORITATIVE_BASELINE:

```
AUTHORITATIVE_BASELINE/
├── 01_REGULATORIO/
│   └── DMR/
│       └── DMR-001_Device_Master_Record_v1.0_OFICIAL.md ✅
├── 02_CONTROLES_DESIGN/
│   ├── SRS/
│   │   └── SRS-001_Software_Requirements_v1.0_OFICIAL.md ✅
│   └── SDD/
│       └── SDD-001_Software_Design_v1.0_OFICIAL.md ✅
├── 05_AVALIACAO_CLINICA/
│   └── CER/
│       └── CER-001_Clinical_Evaluation_v1.0_OFICIAL.md ✅
├── 06_RASTREABILIDADE/
│   └── TRC/
│       └── TRC-001_Traceability_Matrix_v1.0_OFICIAL.md ✅
└── 07_POS_MERCADO/
    └── PMS/
        └── PMS-001_PostMarket_Surveillance_v1.0_OFICIAL.md ✅
```

---

## 📊 Histórico de Padronização

### Documentos Padronizados para v1.0

| Documento | Versão Anterior | → Versão Atual | Data |
|-----------|-----------------|----------------|------|
| DMR | v2.0 | v1.0 | 12 Out 2025 |
| SRS | v2.2 | v1.0 | 12 Out 2025 |
| SDD | v2.0 | v1.0 | 12 Out 2025 |
| CER | v1.2 | v1.0 | 12 Out 2025 |
| TRC | v2.1 | v1.0 | 12 Out 2025 |
| PMS | v1.1 | v1.0 | 12 Out 2025 |

### Justificativa da Padronização

**Objetivo**: Criar baseline unificada v1.0 para primeira submissão oficial ANVISA.

**Razão**: Apesar de alguns documentos terem evoluído para versões 2.x durante desenvolvimento, a submissão regulatória requer uma baseline inicial unificada v1.0. Versões anteriores são preservadas aqui para rastreabilidade.

**Impacto**: Todas as referências cruzadas atualizadas, headers padronizados, nomenclatura consistente.

---

## 🔐 Controle de Documentos

### Status dos Arquivos Arquivados
- **Status**: ARCHIVED (arquivado, somente leitura)
- **Modificações**: Não permitidas
- **Acesso**: Consulta e auditoria apenas
- **Retenção**: Permanente (requisito ISO 13485)

### Aprovações
Arquivamento autorizado por:
- **Responsável Técnico**: Dr. Abel Costa
- **Data**: 12 de Outubro de 2025
- **Processo**: Padronização v1.0 Unificada
- **Registro**: Git commit + tag v1.0.0-baseline-unificada

---

## 📅 Evolução dos Documentos

### DMR - Device Master Record
- **v1.0** → draft inicial
- **v2.0** → versão consolidada (arquivada)
- **v1.0** → baseline unificada oficial ✅

### SRS - Software Requirements Specification
- **v1.0-draft** → versão inicial
- **v2.0** → primeira consolidação
- **v2.1** → refinamento de requisitos
- **v2.2** → versão final pré-padronização (arquivada)
- **v1.0** → baseline unificada oficial ✅

### SDD - Software Design Document
- **v1.0** → design inicial
- **v1.1** → iteração de arquitetura
- **v2.0** → design consolidado (arquivada)
- **v1.0** → baseline unificada oficial ✅

### CER - Clinical Evaluation Report
- **v1.0** → avaliação inicial
- **v1.1** → evidências adicionais
- **v1.2** → validação completa (arquivada)
- **v1.0** → baseline unificada oficial ✅

### TRC - Traceability Matrix
- **v1.0** → rastreabilidade básica
- **v2.0** → cobertura expandida
- **v2.1** → 100% cobertura (arquivada)
- **v1.0** → baseline unificada oficial ✅

### PMS - Post-Market Surveillance
- **v1.0** → plano inicial
- **v1.1** → procedimentos detalhados (arquivada)
- **v1.0** → baseline unificada oficial ✅

---

## 🔗 Referências

### Documentação Relacionada
- **Plano de Padronização**: `/PLANO_PADRONIZACAO_VERSAO_1.0.md`
- **Guia de Execução**: `/GUIA_EXECUCAO_FASES_2_3_4.md`
- **VERSION.md**: Controle de versões do repositório
- **CHANGELOG.md**: Histórico completo de mudanças

### Processo de Gestão
- **ISO 13485**: Controle de documentos (Seção 4.2.4)
- **IEC 62304**: Configuração de software (Seção 5.1.9)
- **ANVISA**: Requisitos de rastreabilidade

---

## 📞 Contato

### Dúvidas sobre Versões Históricas
- **E-mail**: quality-hemodoctor@hemodoctor.com
- **Responsável**: Sistema de Gestão da Qualidade

### Solicitação de Acesso a Versões Antigas
1. Identificar documento e versão necessária
2. Justificar necessidade de acesso
3. Solicitar via e-mail ao SGQ
4. Aguardar autorização

---

## 📋 Checklist de Uso

Antes de consultar documentos arquivados, confirme:

- [ ] Você verificou que a versão v1.0 atual não atende sua necessidade?
- [ ] Você tem justificativa documentada para acessar versão antiga?
- [ ] Você entende que estas são versões SOMENTE LEITURA?
- [ ] Você NÃO vai referenciar versões antigas em documentos oficiais?
- [ ] Você vai documentar o motivo da consulta (se para auditoria)?

---

## ⚖️ Conformidade Regulatória

Este diretório é parte do **Design History File (DHF)** do HemoDoctor e atende:

- ✅ **ISO 13485:2016** - Controle de documentos
- ✅ **IEC 62304:2006** - Configuração de software
- ✅ **ANVISA RDC 185/2001** - Registro de dispositivos
- ✅ **21 CFR Part 820** - Quality System Regulation (FDA)
- ✅ **LGPD** - Lei Geral de Proteção de Dados

---

## 📜 Log de Mudanças deste Diretório

| Data | Mudança | Responsável |
|------|---------|-------------|
| 12 Out 2025 | Criação do diretório e estrutura inicial | Dr. Abel Costa |
| 12 Out 2025 | Arquivo de 6 documentos (DMR, SRS, SDD, CER, TRC, PMS) | Padronização v1.0 |

---

**Última Atualização**: 12 de Outubro de 2025  
**Versão deste README**: 1.0  
**Status**: OFICIAL

---

*Este diretório faz parte do sistema de gestão de configuração e controle de documentos do HemoDoctor, dispositivo médico Classe II (ANVISA) para suporte à decisão clínica em oncologia hematológica.*

