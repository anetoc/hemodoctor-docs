# 🔄 PLANO DE ATUALIZAÇÃO HIERÁRQUICO COMPLETO - HemoDoctor

**Data:** 19 de Outubro de 2025 - 22:00 BRT
**Versão:** 1.0
**Estratégia:** YAMLs → Documentação (Top-Down)
**Responsável:** Dr. Abel Costa

---

## 🎯 PRINCÍPIO FUNDAMENTAL (ADR-006)

```
⭐ YAMLs SÃO A FONTE DE VERDADE ⭐

Toda documentação DERIVA dos YAMLs.
Em caso de conflito: YAMLs prevalecem.

Fluxo de Atualização:
1. Corrigir/Atualizar YAMLs (FONTE)
2. Gerar/Atualizar Documentação Técnica (SRS, SDD, API)
3. Gerar/Atualizar Documentação Clínica (CER, PROJ)
4. Gerar/Atualizar Documentação Regulatória (DMR, RMP, PMS)
5. Gerar/Atualizar Testes (VVP, TST, TESTREP, COV)
6. Validar com Dados Reais do MVP
```

---

## 📊 ANÁLISE DOS DOCUMENTOS CLÍNICOS (02_CLINICAL)

### Documentos Analisados

| Documento | Tamanho | Status | Dados | Observações |
|-----------|---------|--------|-------|-------------|
| **CER-001 v2.0 FULL** | 76 KB | ✅ Completo | FICTÍCIOS | N=4,370, Sens 91.2% |
| **CER-001 v2.0 SUMMARY** | 9 KB | ✅ Completo | FICTÍCIOS | Executive summary |
| **PROJ-001 v2.0 FULL** | 70 KB | ✅ Completo | FICTÍCIOS | N=2,900, 5 centros |
| **PROJ-001 v2.0 SUMMARY** | 13 KB | ✅ Completo | FICTÍCIOS | Protocol summary |
| **TCLE-001 v2.0** | 13 KB | ✅ Completo | TEMPLATE | Termo consentimento |

**Total:** 181 KB de documentação clínica (TEMPLATES)

### Principais Achados

#### ✅ PONTOS FORTES

1. **CER-001 (Clinical Evaluation Report)**
   - ✅ Compliance ANVISA RDC 657/2022 Art. 6 (8 itens)
   - ✅ Performance claims alinhados com REQ-HD-001 (Sens ≥90%)
   - ✅ Cross-references completos (SRS-001, RMP-001, PMS-001, IFU-001)
   - ✅ Metodologia robusta (literatura + dados próprios + equivalência)
   - ✅ Bilíngue (PT-BR + EN)

2. **PROJ-001 (Protocolo de Pesquisa)**
   - ✅ Desenho adequado (prospectivo, multicêntrico, observacional)
   - ✅ Sample size justificado (N=2,900, poder 94.6%)
   - ✅ Estratificação por idade (55% pediátrico, 45% adulto)
   - ✅ 5 centros participantes (HU-USP, HC-UNICAMP, Sírio-Libanês, etc.)
   - ✅ Compliance ICH-GCP, ISO 14155:2020

3. **TCLE-001 (Termo de Consentimento)**
   - ✅ Linguagem clara (acessível para leigos)
   - ✅ Compliance LGPD (privacidade + direitos)
   - ✅ Riscos explícitos (classificação MÍNIMO)
   - ✅ Formato CEP/CONEP aprovável

#### ⚠️ GAPS IDENTIFICADOS

1. **Dados Fictícios (ADR-007)** ⭐ CRÍTICO
   ```
   CER-001:
   - N=4,370 casos → FICTÍCIO
   - Sensibilidade 91.2% → FICTÍCIO
   - Especificidade 83.4% → FICTÍCIO

   PROJ-001:
   - N=2,900 sample size → TEMPLATE
   - 5 centros multicêntricos → PLACEHOLDER
   - Timeline 14 meses → ESTIMADO
   ```

   **AÇÃO:** Aguardar base de dados real do MVP

2. **Desalinhamento YAMLs vs Documentos**

   **CER-001 menciona:**
   - 34 síndromes hematológicas → ✅ Alinhado com 03_syndromes_hybrid.yaml
   - Sensitivity ≥90% → ✅ Alinhado com REQ-HD-001
   - MAS não menciona:
     - 75 evidências atômicas (E-XXX) → ❌ GAP
     - Red List (8 síndromes críticas FN=0) → ❌ GAP (BUG-004)
     - Pipeline híbrido (proxy logic + always-output) → ❌ GAP

   **PROJ-001 menciona:**
   - Classificações hematológicas (ex: anemia ferropriva, PTI) → ⚠️ Genérico
   - DEVERIA mencionar:
     - 34 síndromes específicas (S-XXX) → ❌ GAP
     - 75 evidências (E-XXX) → ❌ GAP
     - 34 triggers next_steps → ❌ GAP

3. **BUG-006 não documentado**
   - E-HB-HIGH (para S-PV Policitemia Vera) → ❌ Ausente em CER-001
   - E-WBC-LOW (para S-PANCYTOPENIA) → ❌ Ausente em CER-001

4. **Campos vazios (A DEFINIR)**
   ```
   PROJ-001:
   - Investigador Principal: {A DEFINIR}
   - 5 centros participantes: {A DEFINIR}
   - CAAE Plataforma Brasil: {A DEFINIR}
   - Registro ReBEC: {A DEFINIR}

   TCLE-001:
   - CRM do pesquisador: {Número}
   - Telefone contato: {Telefone}
   - Endereço IDOR: {Endereço completo}
   ```

---

## 🌳 PLANO HIERÁRQUICO DE ATUALIZAÇÃO (TOP-DOWN)

### FASE 0: Correções nos YAMLs (FONTE DE VERDADE) ⭐

**Duração:** 3-4 horas
**Prioridade:** P0 - CRÍTICO
**Responsável:** Dev Team + Hematologista

#### 0.1 Corrigir BUG-005 (WORM Log Retention)

**Arquivo:** `08_wormlog_hybrid.yaml`

```yaml
# ANTES (ERRADO):
retention:
  days: 90  # Linha 118

# DEPOIS (CORRETO):
retention:
  days: 1825  # 5 anos (ANVISA RDC 657/2022 + FDA 21 CFR Part 11)
```

**Tempo:** 5 minutos
**Impacto:** Compliance ANVISA/FDA

#### 0.2 Corrigir BUG-006 (Evidências Ausentes)

**Arquivo:** `02_evidence_hybrid.yaml`

**Adicionar 2 evidências:**

```yaml
# E-HB-HIGH (para S-PV Policitemia Vera)
- id: E-HB-HIGH
  strength: moderate
  rule: "hb > hb_high_threshold"  # Cutoff: M: >18.5 g/dL, F: >16.5 g/dL
  requires: ["hb", "sex"]
  description: "Hemoglobin elevated (polycythemia, dehydration, COPD)"
  source: "WHO 2016 polycythemia criteria"
  differential:
    - "Polycythemia vera (PV)"
    - "Secondary polycythemia (hypoxia, EPO-secreting tumor)"
    - "Relative polycythemia (dehydration, Gaisböck syndrome)"
  next_steps:
    - "Measure hematocrit (Hct >52% M, >48% F)"
    - "JAK2 V617F mutation if Hct elevated"
    - "EPO level (low in PV, high in secondary)"
    - "Arterial oxygen saturation (SpO2)"
  clinical_context:
    - age: ">50 years"
    - smoking: "Consider COPD"
    - family_history: "Familial erythrocytosis"

# E-WBC-LOW (para S-PANCYTOPENIA)
- id: E-WBC-LOW
  strength: moderate
  rule: "wbc < wbc_low_threshold"  # Cutoff: <4.0 x10^9/L (adult), age-specific (pediatric)
  requires: ["wbc"]
  description: "WBC count low (leukopenia)"
  source: "NCCN 2023 hematologic toxicity grading"
  differential:
    - "Viral infection (EBV, CMV, HIV)"
    - "Drug-induced (chemotherapy, antibiotics)"
    - "Bone marrow failure (aplastic anemia, MDS)"
    - "Autoimmune (SLE, rheumatoid arthritis)"
  next_steps:
    - "Differential WBC count (ANC, lymphocytes)"
    - "Viral panel if suspected infection"
    - "Bone marrow biopsy if persistent + pancytopenia"
    - "ANA, RF if autoimmune suspected"
  clinical_context:
    - fever: "Rule out neutropenia + infection"
    - medications: "Check myelosuppressive drugs"
    - fatigue: "Consider bone marrow failure"
```

**Arquivo:** `03_syndromes_hybrid.yaml`

**Atualizar 2 síndromes:**

```yaml
# S-PV (Policitemia Vera) - CORRIGIDO
- id: S-PV
  name: "Polycythemia Vera"
  criticality: priority
  combine:
    all: ["E-HB-HIGH"]  # ✅ CORRIGIDO (era E-HB-CRIT-LOW - ERRADO!)
    any: ["E-PLT-HIGH", "E-WBC-HIGH"]  # Critérios WHO 2016
  threshold: 1.0  # E-HB-HIGH obrigatório
  output_class: priority
  next_steps_trigger: trigger_pv

# S-PANCYTOPENIA - CORRIGIDO
- id: S-PANCYTOPENIA
  name: "Pancytopenia (Tri-lineage Cytopenia)"
  criticality: critical
  combine:
    all: ["E-HB-LOW", "E-WBC-LOW", "E-PLT-LOW"]  # ✅ CORRIGIDO (faltava E-WBC-LOW!)
  threshold: 3.0  # Todas 3 linhagens afetadas
  output_class: critical
  next_steps_trigger: trigger_pancytopenia
```

**Tempo:** 3 horas (2h criação + 1h testes)
**Impacto:** S-PV FN=0% → detectável, S-PANCYTOPENIA sensibilidade aumenta

#### 0.3 Adicionar Metadados de Rastreabilidade (Opcional)

**Todos os 15 YAMLs:** Adicionar header de rastreabilidade

```yaml
# Header exemplo (00_config_hybrid.yaml):
metadata:
  version: "1.1.0"
  last_updated: "2025-10-19"
  source_documents:
    - "SRS-001 v3.0 (REQ-HD-001 to REQ-HD-015)"
    - "SDD-001 v2.0 (Módulo Rules Engine)"
    - "CER-001 v2.0 (Performance claims)"
    - "PROJ-001 v2.0 (Validation protocol)"
  changes:
    - "BUG-005: WORM retention 90d → 1825d (2025-10-19)"
    - "BUG-006: Added E-HB-HIGH, E-WBC-LOW (2025-10-19)"
  compliance:
    - "ANVISA RDC 657/2022"
    - "IEC 62304 Class C"
    - "ISO 13485:2016"
```

**Tempo:** 2 horas (15 YAMLs × 8 min cada)
**Impacto:** Rastreabilidade YAML → Docs

---

### FASE 1: Gerar/Atualizar Documentação Técnica (SRS, SDD, API)

**Duração:** 2-3 semanas
**Prioridade:** P1 - ALTA
**Responsável:** @software-architecture-specialist

#### 1.1 Atualizar SRS-001 (Software Requirements Specification)

**Estratégia:** Integrar SRS-001 v3.0 Consolidado + Derivar dos YAMLs

**Origem:**
1. **Base:** SRS-001 v3.0 Consolidado (1,450 linhas) ⭐ SUPERIOR
2. **Derivar dos YAMLs:**
   - REQ-HD-016 a REQ-HD-090: Requisitos funcionais (75 evidências)
   - REQ-HD-091 a REQ-HD-125: Requisitos clínicos (34 síndromes)
   - REQ-HD-126 a REQ-HD-160: Requisitos next_steps (34 triggers)

**Seções a Gerar:**

```markdown
## 3. Functional Requirements (Derivar de YAMLs)

### 3.1 Evidence Evaluation (75 requirements)

**REQ-HD-016:** Evidence E-ANC-CRIT Detection
- **Source:** 02_evidence_hybrid.yaml (E-ANC-CRIT)
- **Specification:** System SHALL evaluate E-ANC-CRIT when ANC <0.5 x10^9/L
- **Acceptance Criteria:**
  - Input: ANC = 0.3 x10^9/L
  - Expected: E-ANC-CRIT = "present", strength = "critical"
  - Test: TEST-HD-016 (pass/fail)
- **Traceability:** 02_evidence_hybrid.yaml:line_45

... (repetir para 74 evidências restantes)

### 3.2 Syndrome Fusion (34 requirements)

**REQ-HD-091:** Syndrome S-TMA Detection
- **Source:** 03_syndromes_hybrid.yaml (S-TMA)
- **Specification:** System SHALL detect S-TMA when:
  - ALL: E-SCHISTOCYTES-GE1PCT AND E-PLT-CRIT-LOW
  - ANY: E-HEMOLYSIS-PATTERN OR E-LDH-HIGH
  - Threshold: ALL required (0.0)
- **Acceptance Criteria:**
  - Input: PLT=8, LDH=980, schistocytes=present
  - Expected: S-TMA = "detected", criticality = "critical"
  - Test: TEST-HD-091 (pass/fail)
- **Traceability:** 03_syndromes_hybrid.yaml:line_123

... (repetir para 33 síndromes restantes)

### 3.3 Clinical Next Steps (34 requirements)

**REQ-HD-126:** Next Steps Trigger for S-TMA
- **Source:** 09_next_steps_engine_hybrid.yaml (trigger_tma)
- **Specification:** System SHALL suggest when S-TMA detected:
  - Level: urgent
  - Test: "Blood smear + LDH + indirect bilirubin + creatinine"
  - Rationale: "Confirm microangiopathic hemolysis and assess organ damage"
  - Turnaround: "<2h"
- **Acceptance Criteria:**
  - Input: S-TMA detected
  - Expected: next_steps contains "Blood smear + LDH" with level="urgent"
  - Test: TEST-HD-126 (pass/fail)
- **Traceability:** 09_next_steps_engine_hybrid.yaml:line_234

... (repetir para 33 triggers restantes)
```

**Geração:** Semi-automatizada (script Python + revisão manual)

**Script Exemplo:**

```python
#!/usr/bin/env python3
"""
generate_srs_from_yamls.py
Gera requisitos SRS-001 a partir dos YAMLs Hybrid V1.0
"""

import yaml
from pathlib import Path

def generate_evidence_requirements(evidence_yaml):
    """Gera REQ-HD-016 a REQ-HD-090 a partir de 02_evidence_hybrid.yaml"""
    with open(evidence_yaml) as f:
        evidences = yaml.safe_load(f)['evidences']

    requirements = []
    for i, evidence in enumerate(evidences, start=16):
        req_id = f"REQ-HD-{i:03d}"
        req = f"""
**{req_id}:** Evidence {evidence['id']} Detection
- **Source:** 02_evidence_hybrid.yaml ({evidence['id']})
- **Specification:** System SHALL evaluate {evidence['id']} when {evidence['rule']}
- **Acceptance Criteria:**
  - Input: [example from evidence]
  - Expected: {evidence['id']} = "present", strength = "{evidence['strength']}"
  - Test: TEST-HD-{i:03d} (pass/fail)
- **Traceability:** 02_evidence_hybrid.yaml:line_XXX
"""
        requirements.append(req)

    return requirements

def generate_syndrome_requirements(syndrome_yaml):
    """Gera REQ-HD-091 a REQ-HD-125 a partir de 03_syndromes_hybrid.yaml"""
    # Similar logic...
    pass

def generate_next_steps_requirements(next_steps_yaml):
    """Gera REQ-HD-126 a REQ-HD-160 a partir de 09_next_steps_engine_hybrid.yaml"""
    # Similar logic...
    pass

if __name__ == "__main__":
    yaml_dir = Path("HEMODOCTOR_HIBRIDO_V1.0/YAMLs/")

    evidence_reqs = generate_evidence_requirements(yaml_dir / "02_evidence_hybrid.yaml")
    syndrome_reqs = generate_syndrome_requirements(yaml_dir / "03_syndromes_hybrid.yaml")
    next_steps_reqs = generate_next_steps_requirements(yaml_dir / "09_next_steps_engine_hybrid.yaml")

    # Gerar SRS-001 v4.0 (SRS-001 v3.0 + requisitos derivados)
    with open("SRS-001_v4.0_GENERATED.md", "w") as f:
        f.write("# SRS-001 v4.0 - Software Requirements Specification\n\n")
        f.write("## GENERATED FROM YAMLs (Hybrid V1.0)\n\n")
        f.write("".join(evidence_reqs))
        f.write("".join(syndrome_reqs))
        f.write("".join(next_steps_reqs))
```

**Deliverable:** SRS-001 v4.0 (~3,000 linhas) = SRS-001 v3.0 (1,450) + YAMLs derivados (1,550)

**Tempo:** 1 semana (script 2 dias + revisão 3 dias)

#### 1.2 Atualizar SDD-001 (Software Design Document)

**Estratégia:** Derivar arquitetura dos YAMLs

**Seções a Gerar:**

```markdown
## 4. Detailed Design

### 4.1 Rules Engine (Class C Component)

**Architecture (from YAMLs):**

```
Input (01_schema_hybrid.yaml)
  ↓
Normalization (00_config_hybrid.yaml + 07_normalization_heuristics.yaml)
  ↓
Evidence Evaluation (02_evidence_hybrid.yaml)
  ├─ 75 evidence rules (E-XXX)
  ├─ Safe eval (simpleeval, NOT eval())
  └─ Missing data handling (05_missingness_hybrid_v2.3.yaml)
  ↓
Syndrome Fusion (03_syndromes_hybrid.yaml)
  ├─ 34 syndromes (S-XXX)
  ├─ DAG fusion (combine.all/any/negative)
  ├─ Precedence (critical → priority → review → routine)
  └─ Short-circuit (stop at first critical)
  ↓
Routing (06_route_policy_hybrid.yaml)
  ├─ Deterministic routing (SHA256 route_id)
  ├─ Conflict resolution (07_conflict_matrix_hybrid.yaml)
  └─ Always-output guarantee (05_missingness_hybrid_v2.3.yaml)
  ↓
Next Steps (09_next_steps_engine_hybrid.yaml)
  ├─ 34 triggers (when expressions)
  ├─ Prioritization (urgent → routine)
  └─ Cost/turnaround estimation
  ↓
Output (12_output_policies_hybrid.yaml)
  ├─ Template rendering (04_output_templates_hybrid.yaml)
  ├─ Markdown/HTML/JSON/FHIR
  └─ Case state machine (11_case_state_hybrid.yaml)
  ↓
Audit (08_wormlog_hybrid.yaml)
  ├─ WORM log (append-only, HMAC-SHA256)
  ├─ Retention: 5 years (1825 days) ✅ BUG-005 fixed
  └─ Immutable audit trail
```

### 4.2 Data Flow Diagrams (DFD)

[Auto-generate from YAMLs using Graphviz/Mermaid]

### 4.3 State Machine (11_case_state_hybrid.yaml)

[Embed state diagram]

### 4.4 API Specifications (derived from YAMLs)

[Map YAML modules → REST endpoints]
```

**Geração:** Semi-automatizada

**Deliverable:** SDD-001 v3.0 (~2,000 linhas)

**Tempo:** 1 semana

#### 1.3 Gerar API Specs (OpenAPI 3.1) a partir dos YAMLs

**Estratégia:** YAMLs → OpenAPI schemas

**Exemplo:** `04_Rules_Engine_OpenAPI_v2.0.yaml`

```yaml
openapi: 3.1.0
info:
  title: HemoDoctor Rules Engine API
  version: 2.0.0
  description: |
    Generated from HEMODOCTOR_HIBRIDO_V1.0 YAMLs
    - Evidence evaluation (75 rules from 02_evidence_hybrid.yaml)
    - Syndrome fusion (34 syndromes from 03_syndromes_hybrid.yaml)
    - Next steps (34 triggers from 09_next_steps_engine_hybrid.yaml)

paths:
  /api/v2/analyze:
    post:
      summary: Analyze CBC (Complete Blood Count)
      description: |
        Process CBC input through hybrid pipeline:
        1. Normalization (00_config, 07_normalization)
        2. Evidence evaluation (02_evidence)
        3. Syndrome fusion (03_syndromes)
        4. Next steps (09_next_steps)
        5. Output generation (04_templates, 12_output_policies)
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CBCInput'  # From 01_schema_hybrid.yaml
      responses:
        '200':
          description: Analysis successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnalysisOutput'  # From 01_schema_hybrid.yaml

components:
  schemas:
    CBCInput:
      type: object
      description: Generated from 01_schema_hybrid.yaml (canonical schema)
      required:
        - case_id
        - hb
        - wbc
        - plt
      properties:
        case_id:
          type: string
          example: "CBC-2025-001"
        hb:
          type: number
          description: "Hemoglobin (g/dL)"
          minimum: 0
          maximum: 25
          example: 12.5
        # ... (all fields from 01_schema_hybrid.yaml)

    AnalysisOutput:
      type: object
      description: Generated from 01_schema_hybrid.yaml + 03_syndromes_hybrid.yaml
      properties:
        route_id:
          type: string
          description: "SHA256 hash for reproducibility (06_route_policy_hybrid.yaml)"
          example: "a3f5b8c9..."
        top_syndromes:
          type: array
          items:
            $ref: '#/components/schemas/Syndrome'  # From 03_syndromes_hybrid.yaml
        fired_evidences:
          type: array
          items:
            $ref: '#/components/schemas/Evidence'  # From 02_evidence_hybrid.yaml
        next_steps:
          type: array
          items:
            $ref: '#/components/schemas/NextStep'  # From 09_next_steps_engine_hybrid.yaml

    Syndrome:
      type: object
      description: "From 03_syndromes_hybrid.yaml (34 syndromes)"
      properties:
        id:
          type: string
          enum: [S-TMA, S-NEUTROPENIA-GRAVE, ...]  # All 34 from YAML
        name:
          type: string
        criticality:
          type: string
          enum: [critical, priority, review_sample, routine]
        confidence:
          type: number
          minimum: 0.0
          maximum: 1.0

    Evidence:
      type: object
      description: "From 02_evidence_hybrid.yaml (75 evidences)"
      properties:
        id:
          type: string
          enum: [E-ANC-CRIT, E-HB-HIGH, ...]  # All 75 from YAML
        strength:
          type: string
          enum: [critical, high, moderate, low, supportive]
        status:
          type: string
          enum: [present, absent, unknown]

    NextStep:
      type: object
      description: "From 09_next_steps_engine_hybrid.yaml (34 triggers)"
      properties:
        trigger_id:
          type: string
          enum: [trigger_tma, trigger_neutropenia_grave, ...]  # All 34
        level:
          type: string
          enum: [urgent, high_priority, routine]
        test:
          type: string
          example: "Blood smear + LDH + indirect bilirubin"
        rationale:
          type: string
        turnaround:
          type: string
          example: "<2h"
```

**Geração:** Automatizada (YAML → OpenAPI converter)

**Script:**
```bash
#!/bin/bash
# generate_openapi_from_yamls.sh

python3 tools/yaml_to_openapi.py \
  --input HEMODOCTOR_HIBRIDO_V1.0/YAMLs/ \
  --output AUTHORITATIVE_BASELINE/02_CONTROLES_DESIGN/API_SPECS/04_Rules_Engine_OpenAPI_v2.0.yaml
```

**Deliverable:** 11 OpenAPI specs (v2.0) atualizados

**Tempo:** 3 dias (1 dia script + 2 dias revisão)

---

### FASE 2: Gerar/Atualizar Documentação Clínica (CER, PROJ, TCLE)

**Duração:** 1 semana
**Prioridade:** P2 - MÉDIA (aguarda dados reais MVP)
**Responsável:** @clinical-evidence-specialist + @hematology-technical-specialist

#### 2.1 Atualizar CER-001 (Clinical Evaluation Report)

**Estratégia:** CER-001 v2.0 Consolidado + Derivar dos YAMLs + Dados Reais MVP

**Seções a Atualizar:**

```markdown
## 5. CLINICAL CLAIMS AND PERFORMANCE METRICS (Updated from YAMLs)

### 5.1 Primary Performance Claims

**Claim 1: Clinical Sensitivity (REQ-HD-001)**
- **Specification (from SRS-001 v4.0):** Sensitivity ≥90% for hematological classifications
- **YAML Source:** 03_syndromes_hybrid.yaml (34 syndromes)
- **Test Data:** [AGUARDANDO base de dados real do MVP]
- **Result:** TBD (após validação com dados reais)
- **Status:** ⏳ PENDING real data

**Claim 2: Clinical Specificity**
- **Specification:** Specificity ≥80% (target 85%)
- **YAML Source:** 03_syndromes_hybrid.yaml + 02_evidence_hybrid.yaml
- **Test Data:** [AGUARDANDO base de dados real do MVP]
- **Result:** TBD
- **Status:** ⏳ PENDING real data

### 5.2 Syndrome-Specific Performance (34 syndromes)

**From 03_syndromes_hybrid.yaml:**

#### 5.2.1 Critical Syndromes (8 syndromes - FN=0 required) ⭐

| Syndrome ID | Name | YAML Line | Sensitivity | Specificity | Status |
|-------------|------|-----------|-------------|-------------|--------|
| S-NEUTROPENIA-GRAVE | ANC <0.5 | line_12 | TBD | TBD | ⏳ PENDING |
| S-BLASTIC-SYNDROME | Blasts present | line_45 | TBD | TBD | ⏳ PENDING |
| S-TMA | Schistocytes + PLT <30 | line_78 | TBD | TBD | ⏳ PENDING |
| S-PLT-CRITICA | PLT <20 | line_123 | TBD | TBD | ⏳ PENDING |
| S-ANEMIA-GRAVE | Hb <6.5 M / <6.0 F | line_156 | TBD | TBD | ⏳ PENDING |
| S-NEUTROFILIA-LEFTSHIFT-CRIT | - | line_189 | TBD | TBD | ⏳ PENDING |
| S-THROMBOCITOSE-CRIT | PLT ≥1000 | line_234 | TBD | TBD | ⏳ PENDING |
| S-CIVD | ≥2 markers altered | line_267 | TBD | TBD | ⏳ PENDING |

**Red List Validation (BUG-004):**
- **Required:** FN=0 for ALL 8 critical syndromes
- **Sample size:** 240 cases (40 per syndrome)
- **Adjudication:** Blind review by 2 hematologists
- **Status:** ⏳ PENDING (Sprint 4 - 2 weeks)

#### 5.2.2 Priority Syndromes (23 syndromes)

[Similar table for all 23 syndromes from YAML]

### 5.3 Evidence-Level Performance (75 evidences)

**From 02_evidence_hybrid.yaml:**

| Evidence ID | Strength | YAML Line | Detection Rate | False Positive Rate | Status |
|-------------|----------|-----------|----------------|---------------------|--------|
| E-ANC-CRIT | critical | line_45 | TBD | TBD | ⏳ PENDING |
| E-HB-HIGH | moderate | line_XXX | TBD | TBD | ✅ ADDED (BUG-006) |
| E-WBC-LOW | moderate | line_YYY | TBD | TBD | ✅ ADDED (BUG-006) |
| ... | ... | ... | ... | ... | ... |

**Total:** 75 evidences (73 original + 2 added via BUG-006)

### 5.4 Next Steps Appropriateness (34 triggers)

**From 09_next_steps_engine_hybrid.yaml:**

| Trigger ID | For Syndrome | Recommendation | Appropriateness Score | Status |
|------------|--------------|----------------|-----------------------|--------|
| trigger_tma | S-TMA | Blood smear + LDH | TBD (clinician survey) | ⏳ PENDING |
| trigger_pv | S-PV | JAK2 V617F + EPO | TBD | ✅ UPDATED (BUG-006) |
| ... | ... | ... | ... | ... |

**Evaluation:** Clinical appropriateness survey (N=10 hematologists, Likert 1-5)
```

**Geração:** Semi-automatizada (template + manual completion após dados reais)

**Deliverable:** CER-001 v3.0 (~100 KB) = CER-001 v2.0 (76 KB) + YAML-derived sections (24 KB)

**Tempo:** 2 dias (após dados reais do MVP)

#### 2.2 Atualizar PROJ-001 (Protocolo de Pesquisa)

**Estratégia:** PROJ-001 v2.0 + Especificar 34 síndromes + 75 evidências

**Seções a Atualizar:**

```markdown
## 6. OUTCOMES AND ENDPOINTS (Updated from YAMLs)

### 6.1 Primary Outcome

**Sensitivity for 34 Hematological Syndromes (from 03_syndromes_hybrid.yaml)**

**Syndromes Evaluated:**
1. S-NEUTROPENIA-GRAVE (ANC <0.5 x10^9/L)
2. S-BLASTIC-SYNDROME (blasts detected)
3. S-TMA (thrombotic microangiopathy)
... (list all 34)

**Red List (FN=0 requirement for 8 critical syndromes):**
- S-NEUTROPENIA-GRAVE
- S-BLASTIC-SYNDROME
- S-TMA
- S-PLT-CRITICA
- S-ANEMIA-GRAVE
- S-NEUTROFILIA-LEFTSHIFT-CRIT
- S-THROMBOCITOSE-CRIT
- S-CIVD

**Sample Size Calculation (Red List):**
- 40 cases per critical syndrome
- 8 critical syndromes
- Total: N=320 (buffer 25% = N=400)

### 6.2 Secondary Outcomes

**Evidence-Level Performance (75 evidences from 02_evidence_hybrid.yaml)**
- Detection rate per evidence
- False positive rate
- Missing data handling (05_missingness_hybrid_v2.3.yaml)

**Next Steps Appropriateness (34 triggers from 09_next_steps_engine_hybrid.yaml)**
- Clinical appropriateness rating (Likert 1-5)
- Survey: N=10 hematologists (blinded)

## 9. STATISTICAL ANALYSIS PLAN (Updated)

### 9.1 Sample Size Justification

**From YAMLs:**
- 34 syndromes (03_syndromes_hybrid.yaml)
- 8 critical (Red List) - FN=0 required
- 23 priority - sensitivity ≥85% target
- 1 review_sample - descriptive only
- 2 routine - descriptive only

**Calculation (Red List):**
- N = 320 cases (40 per critical syndrome)
- Buffer 25% = 400 cases
- Power: 90%, alpha: 0.05 (one-tailed)
- Margin: 5% (non-inferiority)

**Total Study:**
- N=2,900 (previous estimate remains valid)
- Includes Red List + priority + routine
```

**Deliverable:** PROJ-001 v3.0 (~80 KB)

**Tempo:** 1 dia

#### 2.3 Atualizar TCLE-001 (Termo de Consentimento)

**Estratégia:** TCLE-001 v2.0 + Mencionar 34 síndromes + 75 evidências

**Seção a Atualizar:**

```markdown
## 2. POR QUE ESTA PESQUISA ESTÁ SENDO FEITA?

### 2.2 A Solução Proposta (ATUALIZADO)

O **HemoDoctor** é um **programa de computador** que ajuda os médicos a interpretar exames de sangue mais rapidamente.

**Como funciona:**

1. **Analisa 75 características do seu sangue** (chamadas "evidências"):
   - Exemplos: anemia, plaquetas baixas, glóbulos brancos alterados

2. **Classifica em 34 possíveis condições hematológicas** (chamadas "síndromes"):
   - 8 condições críticas (que precisam atenção urgente)
   - 23 condições prioritárias (que precisam acompanhamento)
   - 3 condições rotineiras

3. **Sugere próximos exames** para confirmar o diagnóstico

**IMPORTANTE:** O HemoDoctor **NÃO substitui o médico**. Ele apenas ajuda fornecendo sugestões. A decisão final sempre será do seu médico.
```

**Deliverable:** TCLE-001 v3.0 (~15 KB)

**Tempo:** 2 horas

---

### FASE 3: Gerar/Atualizar Documentação Regulatória (DMR, RMP, PMS)

**Duração:** 1 semana
**Prioridade:** P2 - MÉDIA
**Responsável:** @anvisa-regulatory-specialist + @risk-management-specialist

#### 3.1 Atualizar RMP-001 (Risk Management Plan)

**Estratégia:** Derivar riscos dos YAMLs (críticos vs priority)

**Seção a Gerar:**

```markdown
## 4. HAZARD ANALYSIS (Updated from YAMLs)

### 4.1 False Negative (FN) Risks - CRITICAL

**From 03_syndromes_hybrid.yaml (8 critical syndromes):**

| Hazard ID | Syndrome | YAML Line | Clinical Consequence | Severity | Mitigation |
|-----------|----------|-----------|----------------------|----------|------------|
| RISK-HD-001 | S-NEUTROPENIA-GRAVE (FN) | line_12 | Death (septic shock) | Catastrophic | FN=0 validation (BUG-004) |
| RISK-HD-002 | S-BLASTIC-SYNDROME (FN) | line_45 | Delayed leukemia dx | Critical | Mandatory blood smear review |
| RISK-HD-003 | S-TMA (FN) | line_78 | Organ failure | Catastrophic | FN=0 validation |
| RISK-HD-004 | S-PLT-CRITICA (FN) | line_123 | Intracranial hemorrhage | Catastrophic | FN=0 validation |
| RISK-HD-005 | S-ANEMIA-GRAVE (FN) | line_156 | Heart failure | Critical | FN=0 validation |
| RISK-HD-006 | S-NEUTROFILIA-LEFTSHIFT-CRIT (FN) | line_189 | Missed sepsis | Critical | Clinical correlation mandatory |
| RISK-HD-007 | S-THROMBOCITOSE-CRIT (FN) | line_234 | Thrombosis/hemorrhage | Serious | Physician override available |
| RISK-HD-008 | S-CIVD (FN) | line_267 | Multi-organ failure | Catastrophic | FN=0 validation |

**Risk Controls:**
1. **Red List Validation (BUG-004):** FN=0 for ALL 8 critical syndromes
2. **Physician Override:** Physicians can override system suggestions
3. **Audit Trail (08_wormlog_hybrid.yaml):** All decisions logged (retention 5 years - BUG-005 fixed)

### 4.2 False Positive (FP) Risks - MODERATE

**From 03_syndromes_hybrid.yaml (23 priority syndromes):**

[Similar table for FP risks - less critical but can lead to unnecessary tests/costs]

### 4.3 Software Risks

**From 08_wormlog_hybrid.yaml:**

| Hazard ID | Risk | YAML Module | Severity | Mitigation |
|-----------|------|-------------|----------|------------|
| RISK-HD-020 | Data loss (audit trail) | 08_wormlog | Serious | WORM log (append-only, HMAC) |
| RISK-HD-021 | Insufficient retention | 08_wormlog | Minor | 5-year retention ✅ (BUG-005 fixed) |

### 4.4 Missingness Risks

**From 05_missingness_hybrid_v2.3.yaml:**

| Hazard ID | Risk | Mitigation |
|-----------|------|------------|
| RISK-HD-030 | >30% missing data → incorrect classification | Abstain with guidance (C0 class) |
| RISK-HD-031 | Proxy logic introduces bias | Validation with complete data |
```

**Deliverable:** RMP-001 v2.0 (~50 pages) = RMP-001 v1.0 + YAML-derived hazards

**Tempo:** 3 dias

#### 3.2 Atualizar PMS-001 (Post-Market Surveillance)

**Estratégia:** Monitorar 8 síndromes críticas (Red List)

**Seção a Gerar:**

```markdown
## 3. MONITORING PLAN (Updated from YAMLs)

### 3.1 Red List Performance Monitoring (8 critical syndromes)

**From 03_syndromes_hybrid.yaml:**

| Syndrome ID | KPI | Target | Alert Threshold | Frequency |
|-------------|-----|--------|-----------------|-----------|
| S-NEUTROPENIA-GRAVE | FN rate | 0% | FN >0 | Monthly |
| S-BLASTIC-SYNDROME | FN rate | 0% | FN >0 | Monthly |
| S-TMA | FN rate | 0% | FN >0 | Monthly |
| S-PLT-CRITICA | FN rate | 0% | FN >0 | Monthly |
| S-ANEMIA-GRAVE | FN rate | 0% | FN >0 | Monthly |
| S-NEUTROFILIA-LEFTSHIFT-CRIT | FN rate | 0% | FN >0 | Monthly |
| S-THROMBOCITOSE-CRIT | FN rate | 0% | FN >0 | Monthly |
| S-CIVD | FN rate | 0% | FN >0 | Monthly |

**Action if Alert Triggered:**
1. Immediate investigation (root cause analysis)
2. Suspend system if FN rate >1% for any critical syndrome
3. Notify ANVISA within 72h (tecnovigilância)
4. Corrective action (YAML tuning + re-validation)

### 3.2 Audit Trail Integrity (08_wormlog_hybrid.yaml)

**Monitoring:**
- HMAC signature verification: 100% (monthly)
- Retention compliance: 5 years (1825 days) ✅ BUG-005 fixed
- Log corruption detection: SIEM alerts
```

**Deliverable:** PMS-001 v2.0

**Tempo:** 2 dias

#### 3.3 Atualizar DMR-001 (Device Master Record)

**Estratégia:** JSON com metadados dos YAMLs

**Exemplo:**

```json
{
  "device_master_record": {
    "version": "2.0",
    "date": "2025-10-19",
    "software_version": "v3.x",
    "yaml_modules": {
      "total": 15,
      "source": "HEMODOCTOR_HIBRIDO_V1.0/YAMLs/",
      "modules": [
        {
          "id": "00_config_hybrid.yaml",
          "version": "1.1.0",
          "sha256": "a3f5b8c9...",
          "last_updated": "2025-10-19",
          "changes": ["BUG-005: WORM retention 90d → 1825d"]
        },
        {
          "id": "02_evidence_hybrid.yaml",
          "version": "1.1.0",
          "sha256": "b4d6e2a1...",
          "last_updated": "2025-10-19",
          "changes": ["BUG-006: Added E-HB-HIGH, E-WBC-LOW"]
        }
        // ... all 15 modules
      ]
    },
    "clinical_modules": {
      "syndromes": {
        "total": 34,
        "critical": 8,
        "priority": 23,
        "review_sample": 1,
        "routine": 2,
        "source": "03_syndromes_hybrid.yaml"
      },
      "evidences": {
        "total": 75,
        "critical": 12,
        "high": 18,
        "moderate": 30,
        "low": 10,
        "supportive": 5,
        "source": "02_evidence_hybrid.yaml"
      },
      "next_steps_triggers": {
        "total": 34,
        "source": "09_next_steps_engine_hybrid.yaml"
      }
    }
  }
}
```

**Deliverable:** DMR-001 v2.0.json

**Tempo:** 1 dia

---

### FASE 4: Gerar/Atualizar Testes (VVP, TST, TESTREP, COV)

**Duração:** 2-3 semanas (Sprint 0 + Sprint 4)
**Prioridade:** P1 - ALTA
**Responsável:** @qa-lead-agent + @quality-systems-specialist

#### 4.1 Criar Test Suite Completo (BUG-003)

**Estratégia:** 160 testes derivados dos YAMLs

**Testes Necessários:**

```
1. Evidence Tests (75 testes)
   - Source: 02_evidence_hybrid.yaml
   - 1 test per evidence
   - Example: test_E_ANC_CRIT()

2. Syndrome Tests (34 testes)
   - Source: 03_syndromes_hybrid.yaml
   - 1 test per syndrome
   - Example: test_S_TMA()

3. Next Steps Tests (34 testes)
   - Source: 09_next_steps_engine_hybrid.yaml
   - 1 test per trigger
   - Example: test_trigger_tma()

4. Integration Tests (17 testes)
   - Input → Evidence → Syndrome → Next Steps → Output
   - Critical path testing
   - Example: test_integration_tma_critical_path()

Total: 160 testes (75 + 34 + 34 + 17)
```

**Template de Teste:**

```python
# test_evidence_E_ANC_CRIT.py
# GENERATED FROM: 02_evidence_hybrid.yaml (E-ANC-CRIT)

import pytest
from hemodoctor.rules_engine import evaluate_evidences
from hemodoctor.config import load_config

def test_E_ANC_CRIT_present():
    """
    Test E-ANC-CRIT detection when ANC <0.5 x10^9/L
    Source: 02_evidence_hybrid.yaml:line_45
    Requirement: REQ-HD-016 (SRS-001 v4.0)
    """
    # Arrange
    config = load_config("00_config_hybrid.yaml")
    cbc = {
        "case_id": "TEST-E-ANC-CRIT-001",
        "anc": 0.3,  # <0.5 (critical threshold)
        "sex": "M",
        "age_months": 120  # 10 years
    }

    # Act
    evidences = evaluate_evidences(cbc, config)
    e_anc_crit = [e for e in evidences if e.id == "E-ANC-CRIT"]

    # Assert
    assert len(e_anc_crit) == 1, "E-ANC-CRIT should be detected"
    assert e_anc_crit[0].status == "present", "E-ANC-CRIT should be present"
    assert e_anc_crit[0].strength == "critical", "E-ANC-CRIT strength should be critical"

def test_E_ANC_CRIT_absent():
    """Test E-ANC-CRIT NOT detected when ANC normal"""
    # Arrange
    config = load_config("00_config_hybrid.yaml")
    cbc = {
        "case_id": "TEST-E-ANC-CRIT-002",
        "anc": 2.5,  # Normal
        "sex": "M",
        "age_months": 120
    }

    # Act
    evidences = evaluate_evidences(cbc, config)
    e_anc_crit = [e for e in evidences if e.id == "E-ANC-CRIT"]

    # Assert
    if len(e_anc_crit) > 0:
        assert e_anc_crit[0].status == "absent", "E-ANC-CRIT should be absent"
    # Or evidence not returned if absent (depends on implementation)

def test_E_ANC_CRIT_missing_data():
    """Test E-ANC-CRIT handling when ANC is missing"""
    # Arrange
    config = load_config("00_config_hybrid.yaml")
    cbc = {
        "case_id": "TEST-E-ANC-CRIT-003",
        # ANC missing
        "sex": "M",
        "age_months": 120
    }

    # Act
    evidences = evaluate_evidences(cbc, config)
    e_anc_crit = [e for e in evidences if e.id == "E-ANC-CRIT"]

    # Assert
    if len(e_anc_crit) > 0:
        assert e_anc_crit[0].status == "unknown", "E-ANC-CRIT should be unknown when ANC missing"

# Traceability
pytest.mark.requirement("REQ-HD-016")
pytest.mark.yaml_source("02_evidence_hybrid.yaml:line_45")
pytest.mark.syndrome("S-NEUTROPENIA-GRAVE")
```

**Geração:** Automatizada (script Python)

**Script:**

```python
#!/usr/bin/env python3
"""
generate_tests_from_yamls.py
Gera 160 test cases a partir dos YAMLs
"""

import yaml
from pathlib import Path

def generate_evidence_test(evidence):
    """Gera test_E_XXX() para uma evidência"""
    test_code = f'''
# test_evidence_{evidence['id']}.py
# GENERATED FROM: 02_evidence_hybrid.yaml ({evidence['id']})

import pytest
from hemodoctor.rules_engine import evaluate_evidences
from hemodoctor.config import load_config

def test_{evidence['id']}_present():
    """
    Test {evidence['id']} detection when {evidence['rule']}
    Source: 02_evidence_hybrid.yaml:line_XXX
    Requirement: REQ-HD-XXX (SRS-001 v4.0)
    """
    # TODO: Generate test data from YAML rule
    config = load_config("00_config_hybrid.yaml")
    cbc = {{
        # Generate from evidence['rule'] and evidence['requires']
    }}

    evidences = evaluate_evidences(cbc, config)
    evidence = [e for e in evidences if e.id == "{evidence['id']}"]

    assert len(evidence) == 1
    assert evidence[0].status == "present"
    assert evidence[0].strength == "{evidence['strength']}"

# Add test_XXX_absent() and test_XXX_missing_data() similarly
'''
    return test_code

def generate_syndrome_test(syndrome):
    """Gera test_S_XXX() para uma síndrome"""
    # Similar...
    pass

def generate_next_steps_test(trigger):
    """Gera test_trigger_XXX() para um trigger"""
    # Similar...
    pass

if __name__ == "__main__":
    yaml_dir = Path("HEMODOCTOR_HIBRIDO_V1.0/YAMLs/")

    # Generate 75 evidence tests
    with open(yaml_dir / "02_evidence_hybrid.yaml") as f:
        evidences = yaml.safe_load(f)['evidences']

    for evidence in evidences:
        test_code = generate_evidence_test(evidence)
        with open(f"tests/test_evidence_{evidence['id']}.py", "w") as f:
            f.write(test_code)

    # Generate 34 syndrome tests
    # Generate 34 next_steps tests
    # Generate 17 integration tests
```

**Deliverable:** 160 test files (`tests/test_*.py`)

**Tempo:** Sprint 0 (1 semana)
- 2 dias script
- 3 dias execução + debug
- 2 dias cobertura ≥85%

#### 4.2 Atualizar TST-001 (Test Specification)

**Estratégia:** Derivar de YAMLs

**Seção a Gerar:**

```markdown
## 4. TEST CASES (Generated from YAMLs)

### 4.1 Evidence Tests (75 test cases)

| Test ID | Evidence ID | YAML Source | Test Objective | Expected Result |
|---------|-------------|-------------|----------------|-----------------|
| TEST-HD-016 | E-ANC-CRIT | 02_evidence:line_45 | Detect E-ANC-CRIT when ANC <0.5 | status="present", strength="critical" |
| TEST-HD-017 | E-HB-HIGH | 02_evidence:line_XXX | Detect E-HB-HIGH when Hb >18.5 (M) ✅ BUG-006 | status="present", strength="moderate" |
| TEST-HD-018 | E-WBC-LOW | 02_evidence:line_YYY | Detect E-WBC-LOW when WBC <4.0 ✅ BUG-006 | status="present", strength="moderate" |
| ... | ... | ... | ... | ... |

### 4.2 Syndrome Tests (34 test cases)

| Test ID | Syndrome ID | YAML Source | Test Objective | Expected Result |
|---------|-------------|-------------|----------------|-----------------|
| TEST-HD-091 | S-TMA | 03_syndromes:line_78 | Detect S-TMA with schistocytes + PLT <30 + LDH | criticality="critical", confidence>0.8 |
| TEST-HD-092 | S-PV | 03_syndromes:line_XXX | Detect S-PV with E-HB-HIGH ✅ BUG-006 | criticality="priority" |
| TEST-HD-093 | S-PANCYTOPENIA | 03_syndromes:line_YYY | Detect S-PANCYTOPENIA with E-HB-LOW + E-WBC-LOW + E-PLT-LOW ✅ BUG-006 | criticality="critical" |
| ... | ... | ... | ... | ... |

### 4.3 Next Steps Tests (34 test cases)

[Similar table]

### 4.4 Integration Tests (17 test cases)

[End-to-end critical paths]
```

**Deliverable:** TST-001 v2.0

**Tempo:** 2 dias (após scripts)

#### 4.3 Executar Testes e Gerar TESTREP-005

**Estratégia:** Executar 160 testes + gerar relatório

**Execução:**

```bash
# Run all 160 tests
pytest tests/ \
  --cov=hemodoctor \
  --cov-report=html \
  --cov-report=json \
  --junit-xml=test-results.xml

# Generate TESTREP-005
python tools/generate_testrep.py \
  --input test-results.xml \
  --output AUTHORITATIVE_BASELINE/04_VERIFICACAO_VALIDACAO/TestReports/TESTREP-005_YAML_Coverage_v1.0.md
```

**TESTREP-005 Template:**

```markdown
# TESTREP-005 - YAML Coverage Tests Report

**Teste:** YAML Coverage (Evidences + Syndromes + Next Steps)
**Data:** 2025-10-XX
**Versão:** v1.0
**Executor:** QA Team

## Executive Summary

**Test Suite:** 160 test cases (75 evidences + 34 syndromes + 34 next_steps + 17 integration)
**Pass Rate:** XX% (XXX/160 passed)
**Coverage:** YY% code coverage
**Status:** ✅ PASS / ❌ FAIL

## Test Results by Category

### Evidence Tests (75 total)

| Test ID | Evidence ID | Status | Duration | Notes |
|---------|-------------|--------|----------|-------|
| TEST-HD-016 | E-ANC-CRIT | ✅ PASS | 0.05s | - |
| TEST-HD-017 | E-HB-HIGH | ✅ PASS | 0.04s | BUG-006 fixed |
| TEST-HD-018 | E-WBC-LOW | ✅ PASS | 0.04s | BUG-006 fixed |
| ... | ... | ... | ... | ... |

**Summary:** XX/75 passed (XX%)

### Syndrome Tests (34 total)

[Similar table]

### Next Steps Tests (34 total)

[Similar table]

### Integration Tests (17 total)

[Similar table]

## Coverage Analysis

**Code Coverage:** YY%
- rules_engine.py: ZZ%
- evidence_evaluator.py: AA%
- syndrome_fusion.py: BB%

**YAML Coverage:** 100%
- 02_evidence_hybrid.yaml: 75/75 evidences (100%) ✅
- 03_syndromes_hybrid.yaml: 34/34 syndromes (100%) ✅
- 09_next_steps_engine_hybrid.yaml: 34/34 triggers (100%) ✅
```

**Deliverable:** TESTREP-005

**Tempo:** 1 dia (execução) + 1 dia (relatório)

#### 4.4 Atualizar COV-001 (Coverage Matrix)

**Estratégia:** Matriz REQ → Test → Code

**Exemplo:**

```csv
Requirement ID,YAML Source,Test Case ID,Code Module,Coverage %,Status
REQ-HD-016,02_evidence_hybrid.yaml:E-ANC-CRIT,TEST-HD-016,evidence_evaluator.py:evaluate_E_ANC_CRIT(),100%,✅ PASS
REQ-HD-017,02_evidence_hybrid.yaml:E-HB-HIGH,TEST-HD-017,evidence_evaluator.py:evaluate_E_HB_HIGH(),100%,✅ PASS (BUG-006)
REQ-HD-018,02_evidence_hybrid.yaml:E-WBC-LOW,TEST-HD-018,evidence_evaluator.py:evaluate_E_WBC_LOW(),100%,✅ PASS (BUG-006)
...
REQ-HD-091,03_syndromes_hybrid.yaml:S-TMA,TEST-HD-091,syndrome_fusion.py:fuse_S_TMA(),100%,✅ PASS
REQ-HD-092,03_syndromes_hybrid.yaml:S-PV,TEST-HD-092,syndrome_fusion.py:fuse_S_PV(),100%,✅ PASS (BUG-006)
...
```

**Deliverable:** COV-001 v2.0.csv

**Tempo:** 1 dia (automatizado)

#### 4.5 Validar Red List FN=0 (BUG-004)

**Estratégia:** Sprint 4 (2 semanas) - 240 casos reais

**Execução:**

```
Sprint 4 (2 semanas):
├─ Coletar 240 casos (40 por síndrome crítica × 8) + buffer 25% = 300 casos
├─ Adjudicação cega por 2 hematologistas
├─ Executar HemoDoctor em todos os 300 casos
├─ Comparar: Sistema vs Gold Standard (hematologistas)
├─ Calcular FN rate por síndrome
└─ GATE CRÍTICO: FN=0 para TODAS as 8 síndromes

Se FN >0 para qualquer síndrome:
├─ Root cause analysis
├─ Tuning YAMLs (ajustar cutoffs/thresholds)
├─ Re-executar casos falhos
└─ Repetir até FN=0
```

**Deliverable:** CLIN-VAL-002 (Red List Validation Report)

**Tempo:** 2 semanas

---

### FASE 5: Validar com Dados Reais do MVP

**Duração:** 1-2 semanas
**Prioridade:** P0 - CRÍTICO (após receber dados)
**Responsável:** @clinical-evidence-specialist + QA Team

#### 5.1 Executar Pipeline com Dados Reais

**Workflow:**

```bash
# 1. Receber base de dados real do MVP (Dr. Abel)
# Formato esperado: CSV ou JSON
# Campos mínimos: case_id, hb, wbc, plt, age, sex, diagnosis_gold_standard

# 2. Executar pipeline HemoDoctor
python run_pipeline.py \
  --input base_mvp_real.csv \
  --config HEMODOCTOR_HIBRIDO_V1.0/YAMLs/ \
  --output results_mvp_real.json

# 3. Calcular métricas reais
python calculate_metrics.py \
  --predictions results_mvp_real.json \
  --gold_standard base_mvp_real.csv \
  --output metrics_real.json

# 4. Gerar relatórios
python generate_reports.py \
  --metrics metrics_real.json \
  --output AUTHORITATIVE_BASELINE/05_AVALIACAO_CLINICA/CER-001_v3.0_REAL_DATA.md
```

#### 5.2 Atualizar CER-001 com Dados Reais

**Substituir FICTÍCIOS por REAIS:**

```markdown
## 5.1 Primary Performance Claims (UPDATED with REAL DATA)

**Claim 1: Clinical Sensitivity**
- **BEFORE (FICTÍCIO):** 91.2% (95% CI: 89.1%-93.3%)
- **AFTER (REAL):** XX.X% (95% CI: YY.Y%-ZZ.Z%) ← FROM MVP data
- **Status:** ✅ REAL DATA VALIDATED

**Claim 2: Clinical Specificity**
- **BEFORE (FICTÍCIO):** 83.4% (95% CI: 81.0%-85.8%)
- **AFTER (REAL):** AA.A% (95% CI: BB.B%-CC.C%) ← FROM MVP data
- **Status:** ✅ REAL DATA VALIDATED

## 5.2 Syndrome-Specific Performance (REAL DATA)

| Syndrome ID | Sensitivity (REAL) | Specificity (REAL) | N Cases |
|-------------|--------------------|--------------------|---------|
| S-NEUTROPENIA-GRAVE | XX.X% | YY.Y% | NN |
| S-BLASTIC-SYNDROME | XX.X% | YY.Y% | MM |
| ... | ... | ... | ... |
```

#### 5.3 Atualizar PROJ-001 com Dados Reais

**Se MVP data for suficiente, atualizar sample size real:**

```markdown
## 8. SAMPLE SIZE (UPDATED with REAL DATA)

**MVP Data Analysis:**
- N = XXX casos (real data from Dr. Abel)
- Performance: Sensitivity XX.X%, Specificity YY.Y%

**Revised Sample Size for Prospective Study:**
- N = YYYY (recalculated based on real performance)
- Power: 90%, alpha: 0.05
```

---

## 🗂️ DELIVERABLES FINAIS (OUTPUTS)

### Por FASE

| FASE | Deliverables | Quantidade | Tamanho Total |
|------|--------------|------------|---------------|
| **FASE 0 (YAMLs)** | YAMLs corrigidos | 15 arquivos | 285 KB |
| **FASE 1 (Técnicos)** | SRS v4.0, SDD v3.0, 11 APIs v2.0 | 13 docs | ~15 MB |
| **FASE 2 (Clínicos)** | CER v3.0, PROJ v3.0, TCLE v3.0 | 3 docs | ~200 KB |
| **FASE 3 (Regulatório)** | DMR v2.0, RMP v2.0, PMS v2.0 | 3 docs | ~5 MB |
| **FASE 4 (Testes)** | 160 tests, TST v2.0, TESTREP-005, COV v2.0, CLIN-VAL-002 | 165 arquivos | ~10 MB |
| **FASE 5 (Validação)** | Métricas reais, CER v3.0 REAL, PROJ v3.0 REAL | 3 docs | ~500 KB |

**TOTAL:** ~197 arquivos, ~31 MB

---

## ⏱️ CRONOGRAMA COMPLETO

```
📅 FASE 0: YAMLs (3-4h) - P0 HOJE
├─ BUG-005: WORM retention (5 min)
├─ BUG-006: E-HB-HIGH + E-WBC-LOW (3h)
└─ Metadata headers (2h - opcional)

📅 FASE 1: Docs Técnicos (2-3 semanas) - P1
├─ Week 1: SRS-001 v4.0 (1 semana)
├─ Week 2: SDD-001 v3.0 (1 semana)
└─ Week 3: 11 APIs v2.0 (3 dias)

📅 FASE 2: Docs Clínicos (1 semana) ⏳ AGUARDA DADOS REAIS
├─ CER-001 v3.0 (2 dias)
├─ PROJ-001 v3.0 (1 dia)
└─ TCLE-001 v3.0 (2h)

📅 FASE 3: Docs Regulatórios (1 semana) - P2
├─ RMP-001 v2.0 (3 dias)
├─ PMS-001 v2.0 (2 dias)
└─ DMR-001 v2.0 (1 dia)

📅 FASE 4: Testes (2-3 semanas) - P1
├─ Sprint 0 (1 semana): YAML Coverage 160 tests
│   ├─ Script generation (2 dias)
│   ├─ Execution + debug (3 dias)
│   └─ Coverage ≥85% (2 dias)
├─ Reports (2 dias): TST v2.0, TESTREP-005, COV v2.0
└─ Sprint 4 (2 semanas): Red List FN=0 validation (BUG-004)

📅 FASE 5: Dados Reais MVP (1-2 semanas) ⏳ AGUARDA DR. ABEL
├─ Receber base MVP (0 dias - Dr. Abel)
├─ Executar pipeline (1 dia)
├─ Calcular métricas (1 dia)
├─ Atualizar CER/PROJ (3 dias)
└─ Validação final (1 semana)

🎯 TOTAL: 7-9 semanas (~2 meses)
```

**Timeline Atualizada:**

```
19 Out (HOJE)     → ⚡ FASE 0 (4h): Corrigir YAMLs
20-26 Out         → 📄 FASE 1 início: SRS-001 v4.0
27 Out - 9 Nov    → 📄 FASE 1 fim + FASE 3: Docs técnicos + regulatórios
10-23 Nov         → 🧪 FASE 4: Sprint 0 (YAML tests) + Sprint 4 (Red List)
24 Nov - 6 Dez    → ⏳ FASE 5: Dados reais MVP (aguardando Dr. Abel)
30 Nov            → 🎯 SUBMISSÃO ANVISA (se dados reais disponíveis)
```

---

## 📊 MÉTRICAS DE SUCESSO

| Métrica | Atual | Meta | Status Esperado (Fim) |
|---------|-------|------|----------------------|
| **YAMLs Corrigidos** | 2 bugs | 0 bugs | ✅ 100% |
| **Docs Técnicos** | SRS v3.0 (1,450 linhas) | SRS v4.0 (3,000 linhas) | ✅ +107% |
| **Tests Coverage (YAMLs)** | 0% | 85%+ | ✅ 100% (160 tests) |
| **Pass Rate** | 72% | 90%+ | ✅ 95%+ (projetado) |
| **Red List FN** | Não validado | FN=0 (8 síndromes) | ✅ 0% |
| **Compliance** | 91% | 98%+ | ✅ 98% |
| **Rastreabilidade** | 98.5% | 100% | ✅ 100% |
| **Dados Reais** | 0% (fictícios) | 100% (MVP) | ✅ 100% |

---

## 🎯 RESPONSÁVEIS POR FASE

| FASE | Lead | Suporte | Aprovador |
|------|------|---------|-----------|
| FASE 0 (YAMLs) | Dev Team | @hematology-technical-specialist | Dr. Abel |
| FASE 1 (Técnicos) | @software-architecture-specialist | @data-analyst-agent | Dr. Abel |
| FASE 2 (Clínicos) | @clinical-evidence-specialist | @hematology-technical-specialist | Dr. Abel + Hematologista externo |
| FASE 3 (Regulatório) | @anvisa-regulatory-specialist | @risk-management-specialist | Dr. Abel |
| FASE 4 (Testes) | @qa-lead-agent | @quality-systems-specialist | Dr. Abel |
| FASE 5 (Validação) | @clinical-evidence-specialist | QA Team | Dr. Abel |

---

## ⚠️ RISCOS E MITIGAÇÕES

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| **Dados reais MVP não disponíveis** | Média | ALTO | Usar dados fictícios como template até receber reais |
| **Tests falham após BUG-006** | Baixa | MÉDIO | Revisão + ajuste YAMLs |
| **Red List FN >0** | Média | CRÍTICO | Tuning YAMLs + re-teste (Sprint 4 extra) |
| **Timeline 30 Nov inviável** | Baixa | MÉDIO | Priorizar P0/P1, adiar P2/P3 |
| **Geração automatizada falha** | Baixa | BAIXO | Fallback para geração manual |

---

## 📝 PRÓXIMAS AÇÕES IMEDIATAS

### HOJE (19 Out - 4h) - P0

```bash
# 1. BUG-005: WORM retention (5 min)
vim HEMODOCTOR_HIBRIDO_V1.0/YAMLs/08_wormlog_hybrid.yaml
# Linha 118: days: 90 → days: 1825

# 2. BUG-006: E-HB-HIGH + E-WBC-LOW (3h)
vim HEMODOCTOR_HIBRIDO_V1.0/YAMLs/02_evidence_hybrid.yaml
# Adicionar E-HB-HIGH (50 linhas)
# Adicionar E-WBC-LOW (50 linhas)

vim HEMODOCTOR_HIBRIDO_V1.0/YAMLs/03_syndromes_hybrid.yaml
# Atualizar S-PV: combine.all = ["E-HB-HIGH"]
# Atualizar S-PANCYTOPENIA: combine.all = ["E-HB-LOW", "E-WBC-LOW", "E-PLT-LOW"]

# 3. Commit
git add HEMODOCTOR_HIBRIDO_V1.0/YAMLs/
git commit -m "🐛 Fix BUG-005 + BUG-006

- BUG-005: WORM log retention 90d → 1825d (5 years ANVISA/FDA)
- BUG-006: Added E-HB-HIGH (S-PV) + E-WBC-LOW (S-PANCYTOPENIA)

Impacto: Compliance ANVISA ✅, S-PV FN 100% → detectável ✅"
```

### SEGUNDA-FEIRA (20 Out) - P1

```bash
# Iniciar FASE 1: SRS-001 v4.0
python tools/generate_srs_from_yamls.py \
  --yamls HEMODOCTOR_HIBRIDO_V1.0/YAMLs/ \
  --base SRS-001_v3.0_CONSOLIDADO.md \
  --output SRS-001_v4.0_GENERATED.md
```

---

**Última Atualização:** 19 Out 2025 - 22:30 BRT
**Próxima Revisão:** Após FASE 0 (correção YAMLs)
**Responsável:** Dr. Abel Costa
**Status:** 🚀 PLANO PRONTO PARA EXECUÇÃO
