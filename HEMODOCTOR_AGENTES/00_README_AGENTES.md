# 🤖 HEMODOCTOR AGENTES - Central de Agentes Claude Code

**Data:** 2025-10-11 00:10 BRT
**Total:** 12 agentes especializados
**Location (instalados):** `~/.claude/agents/`
**Source (specs + docs):** Esta pasta

---

## 📊 AGENTES DISPONÍVEIS

### **HemoDoctor Regulatory Agents (10)** ✅ INSTALADOS

1. **@anvisa-regulatory-specialist**
   - Expertise: ANVISA RDC 657/2022, RDC 751/2022
   - Uso: Compliance regulatório Brasil
   - Location: `anvisa-regulatory-specialist/`

2. **@clinical-evidence-specialist**
   - Expertise: Clinical validation, CER-001, evidência clínica
   - Uso: Validação de estudos clínicos
   - Location: `clinical-evidence-specialist/`

3. **@software-architecture-specialist**
   - Expertise: IEC 62304 Class C, software architecture
   - Uso: Arquitetura de software médico
   - Location: `software-architecture-specialist/`

4. **@risk-management-specialist**
   - Expertise: ISO 14971:2019, análise de risco
   - Uso: Risk management file, TEC-002
   - Location: `risk-management-specialist/`

5. **@quality-systems-specialist**
   - Expertise: ISO 13485:2016, QMS
   - Uso: Sistema de qualidade
   - Location: `quality-systems-specialist/`

6. **@traceability-specialist**
   - Expertise: Requirements traceability, TRC-001
   - Uso: Matrizes de rastreabilidade
   - Location: `traceability-specialist/`

7. **@regulatory-review-specialist**
   - Expertise: Document review, compliance check
   - Uso: Revisão de documentos regulatórios
   - Location: `regulatory-review-specialist/`

8. **@hematology-technical-specialist**
   - Expertise: Hematologia, CBC, classificação
   - Uso: Validação técnica hematológica
   - Location: `hematology-technical-specialist/`

9. **@documentation-finalization-specialist**
   - Expertise: Submission packages, ANVISA/FDA
   - Uso: Preparação final de pacotes
   - Location: `documentation-finalization-specialist/`

10. **@external-regulatory-consultant**
    - Expertise: Simulação de consultor externo
    - Uso: Revisão crítica independente
    - Location: `external-regulatory-consultant/`

---

### **Agentes Novos (2)** ⏳ A INSTALAR

11. **@biostatistics-specialist** (criado 2025-10-10)
    - Expertise: Sample size, power analysis, SAP
    - Uso: Cálculo amostral, análise estatística
    - Status: Spec criada, instalar em `~/.claude/agents/`

12. **@cep-protocol-specialist** (criado 2025-10-10)
    - Expertise: CEP protocols, TCLE, CNS 466/2012
    - Uso: Protocolos CEP, consentimento
    - Status: Spec criada, instalar em `~/.claude/agents/`

---

## 📂 ESTRUTURA DESTA PASTA

```
HEMODOCTOR_AGENTES/
├── 00_README_AGENTES.md                    ← VOCÊ ESTÁ AQUI
├── AGENTS.md                               ← Guia completo (se disponível)
├── AGENTS_MATRIX.md                        ← Matriz de uso (se disponível)
│
├── anvisa-regulatory-specialist/           ← Agente 1
│   ├── agent.json                          (config)
│   ├── prompt.md                           (prompt principal)
│   └── tools/                              (ferramentas específicas)
│
├── clinical-evidence-specialist/           ← Agente 2
├── software-architecture-specialist/       ← Agente 3
├── risk-management-specialist/             ← Agente 4
├── quality-systems-specialist/             ← Agente 5
├── traceability-specialist/                ← Agente 6
├── regulatory-review-specialist/           ← Agente 7
├── hematology-technical-specialist/        ← Agente 8
├── documentation-finalization-specialist/  ← Agente 9
├── external-regulatory-consultant/         ← Agente 10
│
└── docs/                                   ← Documentação técnica
    ├── agent_guidelines.md
    └── agent_workflows.md
```

---

## 🚀 COMO USAR

### **Chamando agentes:**

```bash
# Exemplo 1: Review compliance ANVISA
@anvisa-regulatory-specialist "Review SRS-001 for RDC 751/2022 compliance"

# Exemplo 2: Validação clínica
@clinical-evidence-specialist "Validate sample size calculation for HDOC-PROSP-003"

# Exemplo 3: Análise de risco
@risk-management-specialist "Analyze pediatric platelet classification risks"

# Exemplo 4: Traceability
@traceability-specialist "Update TRC-001 with new requirements from SRS v3.0"

# Exemplo 5: Documentação final
@documentation-finalization-specialist "Compile CER-001 Annexes B, D, E"
```

---

## 📋 WORKFLOWS COMUNS

### **Workflow 1: ANVISA Submission**
```
@anvisa-regulatory-specialist → @regulatory-review-specialist → @documentation-finalization-specialist
```

### **Workflow 2: Clinical Evidence**
```
@clinical-evidence-specialist → @biostatistics-specialist → @hematology-technical-specialist
```

### **Workflow 3: Risk Management**
```
@risk-management-specialist → @quality-systems-specialist → @traceability-specialist
```

### **Workflow 4: CEP Submission**
```
@cep-protocol-specialist → @biostatistics-specialist → @clinical-evidence-specialist
```

---

## 🔧 INSTALAÇÃO (para agentes novos)

```bash
# Instalar biostatistics-specialist
cp -r biostatistics-specialist/ ~/.claude/agents/

# Instalar cep-protocol-specialist
cp -r cep-protocol-specialist/ ~/.claude/agents/

# Verificar instalação
ls -la ~/.claude/agents/
```

---

## 📚 DOCUMENTAÇÃO

- **Guia completo:** `AGENTS.md` (se disponível)
- **Matriz de uso:** `AGENTS_MATRIX.md` (se disponível)
- **Docs técnicas:** `docs/`
- **CLAUDE.md (raiz):** `/Users/abelcosta/Documents/HemoDoctor/docs/CLAUDE.md`

---

## 🎯 PRÓXIMOS PASSOS

1. ☐ Instalar @biostatistics-specialist em `~/.claude/agents/`
2. ☐ Instalar @cep-protocol-specialist em `~/.claude/agents/`
3. ☐ Atualizar AGENTS_MATRIX.md com 12 agentes
4. ☐ Criar workflows específicos para CEP/ANVISA

---

**Última atualização:** 2025-10-11 00:10 BRT
**Versão:** 1.0
**Mantido por:** Abel Costa
