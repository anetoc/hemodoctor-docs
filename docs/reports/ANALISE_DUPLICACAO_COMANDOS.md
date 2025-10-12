# 🔍 ANÁLISE DE DUPLICAÇÃO DE COMANDOS

## 📊 ESTATÍSTICAS

| Métrica | Valor |
|---------|-------|
| **Total de Comandos Únicos** | 119 |
| **Comandos Duplicados** | 4 (3.4%) |
| **Comandos Únicos** | 115 (96.6%) |
| **Total de Instâncias** | 123 |
| **Instâncias Duplicadas** | 4 |
| **Taxa de Redundância** | 3.3% |

---

## 🔄 COMANDOS DUPLICADOS (4)

### **/gap-analysis** (2 agentes)
- anvisa-regulatory-specialist
- regulatory-review-specialist

### **/sample-size** (2 agentes)
- biostatistics-specialist
- clinical-evidence-specialist

### **/interim-analysis** (2 agentes)
- biostatistics-specialist
- clinical-evidence-specialist

### **/crf-design** (2 agentes)
- cep-protocol-specialist
- clinical-evidence-specialist

---

## ✅ COMANDOS ÚNICOS (115)

### **external-regulatory-consultant** (14 únicos)
- /independent-validation
- /global-regulatory-update
- /benchmark-similar-devices
- /cost-optimization-analysis
- /external-gap-identification
- /regulatory-risk-assessment
- /best-practices-validation
- /facilitate-agent-discussion
- /agent-knowledge-validation
- /consensus-building
- /competitive-intelligence
- /market-access-strategy
- /regulatory-precedent-analysis
- /multi-region-harmonization

### **documentation-finalization-specialist** (12 únicos)
- /expand-document
- /package-assembly
- /cross-reference-integration
- /regulatory-writing
- /submission-package-complete
- /document-quality-assurance
- /executive-summary-master
- /template-application
- /version-control-final
- /submission-checklist-complete
- /document-index-master
- /compliance-final-validation

### **hematology-technical-specialist** (12 únicos)
- /clinical-workflow-validation
- /variable-clinical-mapping
- /reference-ranges-specification
- /algorithm-clinical-review
- /api-routes-clinical-spec
- /data-dictionary-complete
- /clinical-equivalencies
- /database-schema-clinical
- /dev-team-guidance
- /clinical-technical-bridge
- /modification-requirements
- /critical-values-setup

### **regulatory-review-specialist** (11 únicos)
- /comprehensive-review
- /context-alignment
- /checklist-master
- /quality-gate
- /submission-readiness
- /cross-validation
- /asset-utilization
- /compliance-audit
- /timeline-validation
- /stakeholder-alignment
- /risk-benefit-review

### **quality-systems-specialist** (10 únicos)
- /quality-manual
- /document-control
- /capa-system
- /internal-audit
- /supplier-control
- /management-review
- /training-system
- /design-controls
- /quality-metrics
- /change-control

### **traceability-specialist** (10 únicos)
- /traceability-matrix
- /requirements-trace
- /risk-traceability
- /test-traceability
- /document-links
- /configuration-baseline
- /impact-analysis
- /gap-detection
- /compliance-mapping
- /audit-package

### **cep-protocol-specialist** (9 únicos)
- /protocol-create
- /tcle-create
- /opt-out-justification
- /dpia-create
- /institutional-approvals
- /plataforma-brasil
- /cep-submission-package
- /tale-create
- /cep-response

### **risk-management-specialist** (9 únicos)
- /risk-analysis
- /hazard-identification
- /fmea-analysis
- /risk-controls
- /risk-benefit
- /post-market-risks
- /risk-matrix
- /residual-risk
- /clinical-risks

### **software-architecture-specialist** (9 únicos)
- /system-architecture
- /api-specification
- /database-design
- /security-architecture
- /performance-specs
- /integration-design
- /iec62304-compliance
- /ai-architecture
- /deployment-strategy

### **anvisa-regulatory-specialist** (7 únicos)
- /reg-strategy
- /consulta-anvisa
- /intended-use
- /regulatory-intel
- /submission-package
- /classification-analysis
- /compliance-check

### **biostatistics-specialist** (6 únicos)
- /power-analysis
- /sap-create
- /diagnostic-accuracy
- /randomization-plan
- /missing-data-plan
- /statistical-report

### **clinical-evidence-specialist** (6 únicos)
- /clinical-protocol
- /endpoints-definition
- /statistical-plan
- /clinical-sites
- /clinical-report
- /real-world-evidence

---

## 🎯 ANÁLISE SEMÂNTICA

### **Funções Semanticamente Relacionadas:**

**submission-package:**
- /cep-submission-package: cep-protocol-specialist

---

## 💡 RECOMENDAÇÕES

### **1. Duplicações Legítimas (Manter):**

Comandos onde a duplicação faz sentido (expertise diferente):

- **/gap-analysis**: Especialidades complementares
- **/sample-size**: Especialidades complementares
- **/interim-analysis**: Especialidades complementares
- **/crf-design**: Especialidades complementares

### **2. Duplicações para Revisar:**

Comandos com >2 implementações (possível consolidação):


### **3. Comandos para Padronizar:**

Comandos similares com nomes diferentes:

- /submission-package ≈ /submission-package-complete ≈ /cep-submission-package
  - /submission-package: anvisa-regulatory-specialist
  - /submission-package-complete: documentation-finalization-specialist
  - /cep-submission-package: cep-protocol-specialist

- /gap-analysis ≈ /external-gap-identification ≈ /gap-detection
  - /gap-analysis: anvisa-regulatory-specialist, regulatory-review-specialist
  - /external-gap-identification: external-regulatory-consultant
  - /gap-detection: traceability-specialist

- /clinical-protocol ≈ /protocol-create
  - /clinical-protocol: clinical-evidence-specialist
  - /protocol-create: cep-protocol-specialist

