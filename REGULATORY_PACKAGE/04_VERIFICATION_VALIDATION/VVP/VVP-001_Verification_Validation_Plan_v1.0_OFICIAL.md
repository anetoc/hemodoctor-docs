# VVP-001 — Verification & Validation Plan

**Código:** VVP-001  
**Versão:** v1.0  
**Data:** 12 de Outubro de 2025  
**Autor(es):** @quality-systems-specialist | Abel Costa  
**Revisores:** {QA Manager, Software Architect}  
**Aprovadores:** {Regulatory Affairs Director}  
**Status:** OFICIAL - Baseline Autorizada  
**Confidencialidade:** Interno/Confidencial

---

## DOCUMENT CONTROL | CONTROLE DO DOCUMENTO

| Campo | Valor |
|-------|-------|
| **Código do Documento** | VVP-001 |
| **Título** | Verification & Validation Plan - HemoDoctor SaMD |
| **Versão** | v1.0 (OFICIAL) |
| **Data de Emissão** | 12 de outubro de 2025 |
| **Classificação Regulatória** | IEC 62304 Class C | ANVISA Class III |
| **Normas Aplicáveis** | IEC 62304:2006+A1:2015, IEC 62366-1:2015, ISO 14971:2019 |
| **Documentos Relacionados** | TST-001 v1.0, SRS-001 v1.0, SDD-001 v1.0, TRC-001 v1.0 |
| **Próxima Revisão** | Anual ou após mudanças significativas no software |

---

## TABLE OF CONTENTS | ÍNDICE

1. [Introduction](#1-introduction)
2. [Verification & Validation Strategy](#2-verification--validation-strategy)
3. [Test Levels](#3-test-levels)
4. [Acceptance Criteria](#4-acceptance-criteria)
5. [Resources and Schedule](#5-resources-and-schedule)
6. [Responsibilities](#6-responsibilities)
7. [Test Environments](#7-test-environments)
8. [Traceability](#8-traceability)
9. [Risk Management Integration](#9-risk-management-integration)
10. [Configuration Management](#10-configuration-management)
11. [Deviation and Non-Conformance Handling](#11-deviation-and-non-conformance-handling)
12. [Compliance and Regulatory Considerations](#12-compliance-and-regulatory-considerations)
13. [References](#13-references)
14. [Appendices](#14-appendices)

---

## 1. INTRODUCTION

### 1.1 Purpose

This Verification & Validation Plan (VVP) establishes the comprehensive strategy, procedures, and criteria for verifying and validating the **HemoDoctor SaMD (Software as Medical Device)** to ensure compliance with:

- **IEC 62304:2006+A1:2015** (Medical Device Software - Software Life Cycle Processes) - Class C
- **IEC 62366-1:2015** (Medical Devices - Application of Usability Engineering)
- **ISO 14971:2019** (Medical Devices - Application of Risk Management)
- **ANVISA RDC 657/2022** (SaMD Registration Requirements)
- **ANVISA RDC 751/2022** (Device Classification)

**Definitions:**
- **Verification:** Confirmation by examination and provision of objective evidence that specified requirements have been fulfilled (IEC 62304 §5.5-5.7)
- **Validation:** Confirmation by examination and provision of objective evidence that the particular requirements for the specific intended use can be consistently fulfilled (IEC 62304 §5.8)

### 1.2 Scope

This VVP covers all verification and validation activities for **HemoDoctor SaMD v1.0**, including:

**In Scope:**
- Unit testing of all Class C software units
- Integration testing of all interfaces (API, LIS, database)
- System testing of all 28 functional requirements (REQ-HD-001 to REQ-HD-016) and 7 non-functional requirements (NFR-001 to NFR-007)
- User Acceptance Testing (UAT) with clinical users
- Performance testing (P95/P99 latency, throughput)
- Security testing (penetration testing, vulnerability scanning)
- Usability testing per IEC 62366-1
- Regulatory compliance validation (ANVISA RDC 657/751)

**Out of Scope:**
- Third-party SOUP components (validated separately per SOUP-001 v1.0)
- Infrastructure testing (AWS/Azure managed services)
- Non-medical features (admin dashboards not impacting clinical decisions)

### 1.3 Product Overview

**Product:** HemoDoctor SaMD  
**Classification:** IEC 62304 Class C | ANVISA Class III | FDA Class III  
**Intended Use:** Clinical decision support for hematological diagnosis based on CBC analysis  
**Safety Classification:** High risk (direct impact on patient diagnosis and treatment decisions)

**Key Safety-Critical Functions:**
- Anemia detection (REQ-HD-001: Sensitivity ≥90%)
- Critical alert generation (RISK-HD-001: False negatives)
- Clinical rationale transparency (RISK-HD-008: Automation bias)
- Audit trail integrity (REQ-HD-004: LGPD compliance)

**Traceability:** → SRS-001 v1.0 §1 (Scope) → SDD-001 v1.0 §1 (Architecture)

---

## 2. VERIFICATION & VALIDATION STRATEGY

### 2.1 Overall V&V Approach

HemoDoctor V&V follows a **risk-based testing strategy** aligned with ISO 14971:2019, prioritizing:

1. **Safety-Critical Functions:** 100% coverage with redundant testing (unit + integration + system + UAT)
2. **High-Risk Functions:** Minimum 95% code coverage, all edge cases tested
3. **Medium-Risk Functions:** Minimum 85% code coverage, nominal + boundary testing
4. **Low-Risk Functions:** Minimum 70% code coverage, nominal testing only

**V&V Phases:**

| Phase | Activities | Timeline | Deliverables |
|-------|------------|----------|--------------|
| **Phase 1: Unit Testing** | Developer-led, TDD approach | Continuous (sprint-based) | Unit test reports (TESTREP-001) |
| **Phase 2: Integration Testing** | QA-led, API/interface validation | Weekly integration cycles | Integration test reports (TESTREP-002) |
| **Phase 3: System Testing** | QA-led, end-to-end scenarios | Pre-release (2 weeks) | System test reports (TESTREP-003) |
| **Phase 4: Validation (UAT)** | Clinical users, real-world scenarios | Pre-release (2 weeks) | Validation test reports (TESTREP-004) |
| **Phase 5: Regression Testing** | Automated, post-change verification | Every release | Regression test reports |

### 2.2 IEC 62304 Compliance Mapping

**IEC 62304 §5.5 Software Unit Testing:**
- All Class C units have documented unit tests (target: 100% coverage)
- Unit tests execute automatically in CI/CD pipeline (GitHub Actions)
- Test framework: pytest (Python), Jest (JavaScript)

**IEC 62304 §5.6 Software Integration Testing:**
- All interfaces tested (API Gateway, Ingestion Service, LIS/HIS integration)
- Integration tests verify data flow between components
- Test environment: Staging (Docker Compose + AWS staging)

**IEC 62304 §5.7 Software System Testing:**
- All 28 functional requirements verified with system tests
- End-to-end clinical scenarios tested (anemia detection, alert generation)
- Test environment: Production-like (identical hardware/network/load)

**IEC 62304 §5.8 Software Release Testing:**
- Pre-release regression testing of all CRITICAL/HIGH test cases
- Clinical validation with 10+ hematologists (UAT)
- Final sign-off by QA Manager + Regulatory Affairs Director

**Traceability:** → TST-001 v1.0 §2 (Test Strategy) → IEC 62304:2006+A1:2015

### 2.3 Risk-Based Testing

**Risk Categories (per RMP-001 v1.0):**

| Risk Level | Test Coverage | Test Types | Acceptance Criteria |
|------------|---------------|------------|---------------------|
| **CRITICAL** (RISK-HD-001 to RISK-HD-008) | 100% | Unit + Integration + System + UAT + Regression | Zero failures |
| **HIGH** (RISK-HD-101 to RISK-HD-106) | ≥95% | Unit + Integration + System | ≤1% failure rate |
| **MEDIUM** (RISK-HD-201 to RISK-HD-206) | ≥85% | Unit + Integration | ≤5% failure rate |
| **LOW** (RISK-HD-301 to RISK-HD-305) | ≥70% | Unit | ≤10% failure rate |

**Critical Risks Requiring Exhaustive Testing:**
- **RISK-HD-001:** False negative critical anemia (death risk)
  - **Test Coverage:** 100% (all edge cases, boundary values, corner cases)
  - **Test Cases:** TEST-HD-011, TEST-HD-012 (CER-001 validation n=4,370)
- **RISK-HD-002:** False positive severe anemia (alert fatigue)
  - **Test Coverage:** 100% (specificity target ≥80%)
  - **Test Cases:** TEST-HD-012 (precision/recall analysis)
- **RISK-HD-003:** Data quality issues (incorrect diagnosis)
  - **Test Coverage:** 100% (validation logic, unit conversion, LOINC mapping)
  - **Test Cases:** TEST-HD-013, TEST-HD-014
- **RISK-HD-004:** Drift/degradation over time (performance decay)
  - **Test Coverage:** 100% (drift detection, model monitoring)
  - **Test Cases:** TEST-HD-014 (drift simulation), PMS-001 (real-world monitoring)

**Traceability:** → RMP-001 v1.0 (Risk Management Plan) → TRC-001 v1.0 (RISK_ID column)

---

## 3. TEST LEVELS

### 3.1 Unit Testing

**Objective:** Verify individual software units (functions, classes, modules) behave as designed.

**Scope:**
- All Python functions in clinical_rules.py, validation.py, model_inference.py
- All JavaScript functions in UI components (React)
- All database queries (SQL validation)

**Coverage Target:**
- **Class C Units:** 100% code coverage (mandatory per IEC 62304)
- **Class B Units:** 95% code coverage
- **Class A Units:** 80% code coverage

**Test Framework:**
- **Python:** pytest + pytest-cov (coverage reporting)
- **JavaScript:** Jest + Istanbul (coverage)
- **Database:** SQL linting + query plan analysis

**Test Data:**
- Synthetic datasets (edge cases, boundary values)
- Equivalence partitioning for input ranges
- Example: Hb values [0, 4, 7, 10, 13, 16, 20, 99999] to test boundaries

**Automation:**
- 100% automated in CI/CD pipeline
- Triggered on every commit (GitHub Actions)
- Execution time: <5 minutes

**Deliverable:**
- **TESTREP-001:** Unit Tests Report v1.0

**Traceability:** → TST-001 v1.0 §4 (Test Cases) → SDD-001 v1.0 §3 (Component Design)

---

### 3.2 Integration Testing

**Objective:** Verify interfaces between software components and external systems work correctly.

**Scope:**
- **API Gateway:** REST endpoints (POST /analyze_cbc, GET /alert_history)
- **Ingestion Service:** CBC data ingestion from LIS/HIS (HL7 FHIR R4)
- **Validation Service:** Unit conversion, LOINC mapping, age/sex/pregnancy validation
- **Rules Engine:** Clinical rules execution (anemia detection logic)
- **HemoAI:** ML model inference (XGBoost + SHAP explainability)
- **Alert Orchestrator:** Alert prioritization and throttling
- **Audit Service:** WORM logs, cryptographic signatures

**Coverage Target:**
- **Critical Interfaces:** 100% (API, LIS/HIS, Audit)
- **Non-Critical Interfaces:** 90%

**Test Framework:**
- **API Testing:** Postman + Newman (automated)
- **Integration:** pytest + requests library
- **Database:** PostgreSQL test database (Docker)

**Test Data:**
- Anonymized real CBC data (n=500 cases from CER-001 validation)
- Synthetic edge cases (invalid HL7 messages, malformed JSON)

**Automation:**
- 95% automated (manual verification for LIS/HIS integration in staging)
- Triggered daily (nightly builds)
- Execution time: <15 minutes

**Deliverable:**
- **TESTREP-002:** Integration Tests Report v1.0

**Traceability:** → TST-001 v1.0 §4 (Test Cases TEST-HD-013 to TEST-HD-019) → SDD-001 v1.0 §3 (Services)

---

### 3.3 System Testing

**Objective:** Verify the complete HemoDoctor system meets all functional and non-functional requirements.

**Scope:**
- All 28 functional requirements (REQ-HD-001 to REQ-HD-016)
- All 7 non-functional requirements (NFR-001 to NFR-007)
- End-to-end clinical scenarios (anemia diagnosis, alert generation, rationale display)

**Coverage Target:**
- **Functional Requirements:** 100% (all 28 requirements tested)
- **Non-Functional Requirements:** 100% (performance, security, usability)

**Test Framework:**
- **E2E Testing:** Cypress (web UI automation)
- **Performance Testing:** k6 (load testing, latency measurement)
- **Security Testing:** OWASP ZAP (penetration testing), Snyk (vulnerability scanning)

**Test Scenarios (Examples):**

1. **Anemia Detection (REQ-HD-001):**
   - Input: CBC with Hb=6.5 g/dL (adult male)
   - Expected: CRITICAL alert generated, sensitivity ≥90%
   - Test Case: TEST-HD-011

2. **Clinical Rationale Transparency (REQ-HD-003):**
   - Input: CRITICAL alert triggered
   - Expected: Display rule ID, evidence source, SHAP values, override button
   - Test Case: TEST-HD-015, TEST-HD-016, TEST-HD-017

3. **Performance (NFR-001):**
   - Load: 1000 CBC analyses/hour
   - Expected: P95 ≤2s, P99 ≤5s, API timeout 30s
   - Test Case: TEST-HD-015, TEST-HD-026, TEST-HD-050

**Test Data:**
- Anonymized real CBC data (n=1,523 from CER-001 prospective validation)
- Synthetic stress test data (10,000 cases for load testing)

**Automation:**
- 80% automated (E2E scenarios in Cypress)
- 20% manual (usability, exploratory testing)
- Execution time: 2-4 hours (full regression suite)

**Deliverable:**
- **TESTREP-003:** System Tests Report v1.0

**Traceability:** → TST-001 v1.0 §4 (All test cases) → SRS-001 v1.0 (All requirements) → TRC-001 v1.0

---

### 3.4 Validation Testing (UAT - User Acceptance Testing)

**Objective:** Confirm HemoDoctor meets the needs of end users in real-world clinical scenarios.

**Scope:**
- Clinical validation with hematologists (n=10+)
- Usability testing per IEC 62366-1 (critical tasks success rate 100%)
- Real-world performance (Time-to-Diagnosis reduction ≥30%)

**Coverage Target:**
- **Critical Tasks:** 100% success rate (zero errors)
- **Non-Critical Tasks:** ≥95% success rate
- **Clinical Accuracy:** Sensitivity ≥90%, Specificity ≥80% (per CER-001 v1.0)

**Test Framework:**
- **Usability:** IEC 62366-1 summative evaluation (UEF-001)
- **Clinical Validation:** Prospective study (PPC-001 - n=1,500 participants, CEP-approved)

**Test Scenarios (Examples):**

1. **Critical Task 1:** Analyze CBC and identify critical anemia
   - Participants: 10 hematologists
   - Success Criteria: 100% identify Hb <7 g/dL as CRITICAL
   - Test Case: TEST-HD-013 (HFE Summative)

2. **Critical Task 2:** Override false positive alert
   - Participants: 10 hematologists
   - Success Criteria: 100% successfully override with clinical justification
   - Test Case: TEST-HD-017

3. **Real-World Performance (Time-to-Diagnosis):**
   - Baseline: 14-21 days (standard of care)
   - Target: ≤10 days (30% reduction)
   - Measurement: PPC-001 prospective study

**Test Data:**
- Real clinical cases (anonymized, CEP-approved per PPC-001)
- n=1,500 participants (adults + pediatrics)

**Automation:**
- Not applicable (human factors testing)
- Manual execution with clinical users
- Duration: 6 months (PPC-001 timeline)

**Deliverable:**
- **TESTREP-004:** Validation Tests Report v1.0
- **CER-001 Update:** Clinical Evaluation Report with UAT results

**Traceability:** → PPC-001 (Clinical Research Protocol) → CER-001 v1.0 (Clinical Evidence) → IEC 62366-1 (UEF-001)

---

## 4. ACCEPTANCE CRITERIA

### 4.1 Functional Requirements Acceptance

**Criteria for PASS:**
- ✅ All 28 functional requirements (REQ-HD-001 to REQ-HD-016) verified with test cases
- ✅ Test results documented in TST-001 v1.0 with status PASS
- ✅ Traceability matrix TRC-001 v1.0 shows 100% requirement coverage

**Specific Thresholds:**

| Requirement | Metric | Threshold | Test Case |
|-------------|--------|-----------|-----------|
| REQ-HD-001 | Clinical Sensitivity | ≥90% | TEST-HD-011, CER-001 |
| REQ-HD-001 | Clinical Specificity | ≥80% | TEST-HD-012, CER-001 |
| REQ-HD-002 | Alert Burden | <15% of cases | TEST-HD-012 |
| REQ-HD-003 | Override Success Rate | 100% (critical tasks) | TEST-HD-013 (HFE) |
| REQ-HD-004 | Audit Trail Integrity | 100% (no tampering) | TEST-HD-018 |
| REQ-HD-005 | API Availability | 99.5% uptime | PMS-001 (Ops KPIs) |
| NFR-001 | Performance P95 | ≤2s | TEST-HD-015, TEST-HD-026 |
| NFR-001 | Performance P99 | ≤5s | TEST-HD-015, TEST-HD-050 |
| NFR-002 | System Availability | 99.5% uptime | TEST-HD-014 |
| NFR-003 | Security (Penetration Test) | Zero critical vulnerabilities | TEST-SEC-001 to SEC-010 |

### 4.2 Non-Functional Requirements Acceptance

**Performance (NFR-001):**
- P95 latency ≤2 seconds
- P99 latency ≤5 seconds
- Throughput ≥1000 cases/hour
- API timeout 30 seconds

**Reliability (NFR-002):**
- System uptime ≥99.5% (SLA)
- Graceful degradation (fallback to rules-only if ML fails)
- Automated regression testing (no breaking changes)

**Security (NFR-003):**
- Zero critical vulnerabilities (OWASP Top 10)
- RBAC enforced (4 roles: Admin, Lab, Physician, Auditor)
- MFA enabled for all users
- TLS 1.3 for all communications
- AES-256 encryption at rest

**Usability (NFR-005):**
- Critical task success rate 100% (IEC 62366-1)
- SUS (System Usability Scale) score ≥70
- WCAG 2.1 Level AA compliance

**Regulatory Compliance (NFR-007):**
- IEC 62304 Class C compliance (all 8 process areas)
- ISO 14971:2019 risk management (all 34 hazards analyzed)
- ISO 13485:2016 QMS (design controls)
- ANVISA RDC 657/751 compliance (SaMD registration requirements)

**Traceability:** → SRS-001 v1.0 §3 (Requirements) → TST-001 v1.0 (Test Cases)

### 4.3 Code Quality Acceptance

**Code Coverage:**
- Class C units: ≥100%
- Class B units: ≥95%
- Overall: ≥85%

**Static Analysis (SonarQube):**
- Quality Gate: PASS
- Code Smells: ≤50 (minor)
- Bugs: 0 (critical/major)
- Vulnerabilities: 0 (critical/major)
- Technical Debt: <1% (max 1 day per 100 lines of code)

**Linting:**
- Python: flake8, black (formatter)
- JavaScript: ESLint, Prettier
- SQL: sqlfluff

### 4.4 Regulatory Acceptance

**ANVISA RDC 657/2022 Article 6 (8 mandatory items):**
- ✅ Clinical Evaluation (CER-001 v1.0)
- ✅ Risk Management (RMP-001 v1.0)
- ✅ Software Requirements (SRS-001 v1.0)
- ✅ Software Design (SDD-001 v1.0)
- ✅ Verification & Validation (VVP-001 + TESTREP-001 to TESTREP-004)
- ✅ Traceability Matrix (TRC-001 v1.0)
- ✅ Instructions for Use (IFU-001 v1.0)
- ✅ Post-Market Surveillance (PMS-001 v1.0)

**Final Approval:**
- QA Manager sign-off
- Software Architect sign-off
- Regulatory Affairs Director sign-off
- CEO sign-off (for ANVISA submission)

---

## 5. RESOURCES AND SCHEDULE

### 5.1 Human Resources

| Role | Responsibility | Time Allocation | Personnel |
|------|----------------|-----------------|-----------|
| **QA Manager** | Overall V&V coordination, approval | 20% (8h/week) | {Name} |
| **QA Engineer 1** | System testing, automation | 100% (40h/week) | {Name} |
| **QA Engineer 2** | Integration testing, security | 100% (40h/week) | {Name} |
| **Software Architect** | Unit test review, design verification | 15% (6h/week) | {Name} |
| **Clinical SME (Hematologist)** | Clinical validation, UAT | 10% (4h/week) | {Name} |
| **DevOps Engineer** | Test infrastructure, CI/CD | 20% (8h/week) | {Name} |
| **Regulatory Affairs Specialist** | Compliance validation, documentation | 10% (4h/week) | {Name} |

**Total Effort:** 3.75 FTE (Full-Time Equivalents)

### 5.2 Infrastructure Resources

**Test Environments:**

| Environment | Purpose | Configuration | Cost (USD/month) |
|-------------|---------|---------------|------------------|
| **Development** | Unit/integration testing | Docker Compose (local) | $0 (local) |
| **Staging** | System testing | AWS EC2 t3.large (2 vCPU, 8GB RAM) | $75 |
| **Production-like** | Performance/validation | AWS EC2 m5.xlarge (4 vCPU, 16GB RAM) | $150 |
| **UAT** | Clinical validation | Staging environment (shared) | $0 (shared) |

**Total Infrastructure Cost:** $225/month

**CI/CD Pipeline:**
- GitHub Actions (included in GitHub license)
- SonarQube Cloud (free for open source)
- Snyk (free tier for vulnerability scanning)

### 5.3 Test Tools

| Tool | Purpose | License Cost (annual) |
|------|---------|----------------------|
| **pytest** | Unit testing (Python) | Free (open source) |
| **Jest** | Unit testing (JavaScript) | Free (open source) |
| **Postman/Newman** | API testing | Free (team plan) |
| **Cypress** | E2E testing | Free (open source) |
| **k6** | Load testing | Free (open source) |
| **OWASP ZAP** | Penetration testing | Free (open source) |
| **SonarQube** | Code quality | Free (community edition) |
| **Snyk** | Vulnerability scanning | $0 (free tier) |
| **REDCap** | Clinical data collection (UAT) | Institutional license |

**Total Tool Cost:** $0/year (all free/open source)

### 5.4 Schedule

**V&V Timeline (6 weeks):**

| Week | Activities | Deliverables | Status |
|------|------------|--------------|--------|
| W1 | VVP creation, test environment setup | VVP-001 v1.0 | ✅ COMPLETE |
| W2-W3 | Unit testing (all modules) | TESTREP-001 v1.0 | ⏳ PENDING |
| W3-W4 | Integration testing (APIs, services) | TESTREP-002 v1.0 | ⏳ PENDING |
| W4-W5 | System testing (E2E scenarios) | TESTREP-003 v1.0 | ⏳ PENDING |
| W5-W6 | Validation testing (UAT with clinicians) | TESTREP-004 v1.0 | ⏳ PENDING |
| W6 | Coverage analysis, final report | COV-001 v1.0 | ⏳ PENDING |

**Critical Path:**
- Week 1: VVP approval (mandatory before testing starts)
- Week 2-3: Unit testing (blocks integration testing)
- Week 4: System testing (blocks UAT)
- Week 6: Final approval (QA Manager + Regulatory Affairs)

**Buffer:** 1 week contingency for re-testing if critical failures found

**Traceability:** → PROXIMOS_PASSOS_POS_V1.0.md (Fase A timeline)

---

## 6. RESPONSIBILITIES

### 6.1 RACI Matrix

| Activity | QA Manager | QA Engineer 1 | QA Engineer 2 | Software Architect | Clinical SME | Regulatory Affairs |
|----------|------------|---------------|---------------|-------------------|--------------|-------------------|
| **VVP Creation** | A | C | C | C | I | R |
| **Unit Testing** | A | R | C | R | I | I |
| **Integration Testing** | A | R | R | C | I | I |
| **System Testing** | A | R | R | C | I | I |
| **UAT (Clinical Validation)** | A | C | C | I | R | C |
| **Performance Testing** | A | C | R | C | I | I |
| **Security Testing** | A | I | R | C | I | C |
| **Test Report Approval** | A | C | C | C | I | R |
| **Final Sign-Off** | R | I | I | A | A | R |

**Legend:**
- **R (Responsible):** Executes the task
- **A (Accountable):** Ultimately answerable for completion
- **C (Consulted):** Provides input
- **I (Informed):** Kept updated on progress

### 6.2 Escalation Path

**Issue Severity Levels:**

| Level | Description | Escalation Timeline | Escalated To |
|-------|-------------|---------------------|--------------|
| **Critical** | Blocker preventing testing | Immediate (1 hour) | QA Manager → CTO |
| **High** | Major issue affecting schedule | 4 hours | QA Manager |
| **Medium** | Workaround available | 24 hours | QA Engineer Lead |
| **Low** | Minor issue, no impact | 72 hours | QA Engineer |

**Escalation Contacts:**
- **QA Manager:** {Email} | {Phone}
- **Software Architect:** {Email} | {Phone}
- **CTO:** {Email} | {Phone}

---

## 7. TEST ENVIRONMENTS

### 7.1 Development Environment

**Purpose:** Developer unit testing and integration testing (local)

**Configuration:**
- Docker Compose with 9 services (PostgreSQL, Neo4j, Qdrant, Redis, etc.)
- Synthetic test data (pre-loaded fixtures)
- Local Ollama (for ML inference testing)

**Access:** All developers (no authentication required for local)

**Data:** Synthetic only (no PHI)

**Backup:** Not required (ephemeral environment)

### 7.2 Staging Environment

**Purpose:** Integration testing, system testing, pre-release validation

**Configuration:**
- AWS EC2 t3.large (2 vCPU, 8GB RAM)
- PostgreSQL RDS (db.t3.medium)
- Docker Swarm orchestration
- Anonymized real data (n=500 cases from CER-001)

**Access:** QA team + Software Architect (RBAC enforced)

**Data:** Anonymized real CBC data (LGPD-compliant)

**Backup:** Daily automated backups (7-day retention)

**URL:** https://staging.hemodoctor.idor.org

### 7.3 Production-like Environment

**Purpose:** Performance testing, final validation, regulatory demonstration

**Configuration:**
- AWS EC2 m5.xlarge (4 vCPU, 16GB RAM)
- PostgreSQL RDS (db.m5.large)
- Kubernetes (EKS)
- Identical to production (hardware, network latency, load balancer)

**Access:** QA Manager + DevOps (MFA required)

**Data:** Anonymized real data (n=1,523 from CER-001 prospective study)

**Backup:** Daily automated backups (30-day retention)

**URL:** https://prod-like.hemodoctor.idor.org (internal only)

### 7.4 UAT Environment

**Purpose:** Clinical validation with hematologists (PPC-001 study)

**Configuration:**
- Shared with Staging environment
- Dedicated subdomain: https://uat.hemodoctor.idor.org
- Real clinical data (CEP-approved, anonymized per PPC-001)

**Access:** Clinical SME + 10 hematologists (study participants)

**Data:** Real clinical cases (anonymized, n=1,500 per PPC-001)

**Backup:** Daily automated backups (5-year retention per CNS 466/2012)

### 7.5 Environment Promotion Process

**Promotion Flow:**
```
Development (local)
    ↓ (unit tests PASS)
Staging (AWS)
    ↓ (integration tests PASS)
Production-like (AWS)
    ↓ (system tests + performance tests PASS)
UAT (clinical validation)
    ↓ (UAT approval by Clinical SME)
Production (AWS)
```

**Approval Gates:**
- Development → Staging: Automated (CI/CD pipeline)
- Staging → Production-like: QA Engineer approval
- Production-like → UAT: QA Manager approval
- UAT → Production: QA Manager + Regulatory Affairs + CEO approval

---

## 8. TRACEABILITY

### 8.1 Requirements Traceability

All requirements in SRS-001 v1.0 are traced to:
- **Design:** SDD-001 v1.0 (component design)
- **Test Cases:** TST-001 v1.0 (verification)
- **Risks:** RMP-001 v1.0 (risk mitigations)
- **Labels:** IFU-001 v1.0 (user instructions)
- **Post-Market:** PMS-001 v1.0 (surveillance)

**Traceability Matrix:** TRC-001 v1.0 (CSV format)

**Coverage Metrics:**
- Requirements → Design: 100% (all 28 requirements mapped to SDD-001)
- Requirements → Test Cases: 100% (all 28 requirements have test cases in TST-001)
- Requirements → Risks: 95% (26/28 requirements linked to risks in RMP-001)

**Example Traceability:**
```
REQ-HD-001 (Critical Anemia Detection)
    → SDD-001 §3.4 Rules Engine, §3.5 HemoAI
    → TEST-HD-011, TEST-HD-012 (TST-001)
    → RISK-HD-001 (False negative critical anemia)
    → IFU-001 §Performance, §Warnings
    → PMS-001 §SLAs, §Real-world Sensitivity
```

### 8.2 Test Traceability

**Test Case → Requirement Mapping:**

| Test Case | Requirement | Design Ref | Risk ID | Status |
|-----------|-------------|------------|---------|--------|
| TEST-HD-011 | REQ-HD-001 | SDD-001 §3.4 | RISK-HD-001 | PASS |
| TEST-HD-012 | REQ-HD-002 | SDD-001 §3.4 | RISK-HD-002 | PASS |
| TEST-HD-013 | REQ-HD-002 | SDD-001 §3.2 | RISK-HD-003 | PASS |
| ... | ... | ... | ... | ... |

**Coverage Verification:**
- All 28 functional requirements have ≥1 test case
- All 7 non-functional requirements have ≥1 test case
- All CRITICAL risks (RISK-HD-001 to RISK-HD-008) have ≥2 redundant test cases

**Traceability Tools:**
- TRC-001 v1.0 (CSV matrix)
- GitHub Projects (test case → requirement linking)
- SonarQube (code coverage → requirement mapping)

---

## 9. RISK MANAGEMENT INTEGRATION

### 9.1 Risk-Based Testing Approach

Per ISO 14971:2019 and RMP-001 v1.0, testing prioritizes:

1. **CRITICAL Risks (RISK-HD-001 to RISK-HD-008):**
   - 100% test coverage
   - Redundant testing (multiple test methods)
   - Example: RISK-HD-001 (False negative anemia) tested with:
     - Unit tests (clinical rules logic)
     - Integration tests (end-to-end CBC analysis)
     - System tests (real clinical scenarios)
     - UAT (clinical validation with hematologists)

2. **HIGH Risks (RISK-HD-101 to RISK-HD-106):**
   - ≥95% test coverage
   - Focus on boundary conditions

3. **MEDIUM/LOW Risks:**
   - Standard testing (nominal + boundary)

### 9.2 Residual Risk Verification

**After Risk Controls (per RMP-001):**
- All residual risks ≤ MEDIUM level (acceptable per risk acceptability matrix)
- Verification tests confirm risk controls are effective
- Example: RISK-HD-001 (False negative anemia)
  - **Initial Risk:** HIGH (death risk)
  - **Risk Control:** Sensitivity ≥90% (REQ-HD-001)
  - **Verification:** TEST-HD-011 confirms sensitivity 91.2% (CER-001)
  - **Residual Risk:** LOW (acceptable)

**Post-Market Surveillance (PMS-001):**
- Continuous monitoring of residual risks
- Monthly reports on false negative rate
- CAPA triggered if false negative rate >5%

**Traceability:** → RMP-001 v1.0 (Risk controls) → TST-001 v1.0 (Verification) → PMS-001 v1.0 (Monitoring)

---

## 10. CONFIGURATION MANAGEMENT

### 10.1 Version Control

**Source Code:**
- Git repository (GitHub)
- Branching strategy: GitFlow (main, develop, feature/*, hotfix/*)
- Commit message format: Conventional Commits (feat, fix, test, docs)

**Documentation:**
- All V&V documents in Git (Markdown format)
- Version tagging: v1.0.0 (Semantic Versioning)

**Test Artifacts:**
- Test scripts in Git (tests/ directory)
- Test data in Git LFS (large files)

### 10.2 Baseline Management

**Baseline Versions (Aligned with v1.0 Unification):**
- SRS-001 v1.0
- SDD-001 v1.0
- TST-001 v1.0
- TRC-001 v1.0
- **VVP-001 v1.0** (this document)

**Change Control:**
- All changes to baseline documents require Change Control Board (CCB) approval
- CCB members: QA Manager, Software Architect, Regulatory Affairs Director

**Traceability:**
- Git tags for baseline versions (v1.0.0-baseline)
- Backup tag: backup-pre-v1.0-unification

---

## 11. DEVIATION AND NON-CONFORMANCE HANDLING

### 11.1 Test Failure Management

**When a Test Fails:**
1. QA Engineer logs failure in GitHub Issues (label: test-failure)
2. Root Cause Analysis (RCA) performed by Software Architect
3. Bug fix prioritized (P0=Critical, P1=High, P2=Medium, P3=Low)
4. Fix implemented and re-tested
5. Regression test suite updated if necessary
6. Failure documented in Test Report with RCA

**Failure Categories:**
- **Category A (Critical):** False negative critical anemia → P0 (immediate fix)
- **Category B (Major):** Performance degradation → P1 (fix within 1 sprint)
- **Category C (Minor):** UI glitch → P2 (fix within 2 sprints)
- **Category D (Cosmetic):** Typo in label → P3 (backlog)

### 11.2 Deviation Requests

**If VVP Cannot Be Followed:**
- Deviation Request Form submitted to QA Manager
- Justification required (technical, schedule, resource constraints)
- QA Manager + Regulatory Affairs review
- Approval/rejection within 48 hours
- If approved: Document deviation in Test Report with risk assessment

**Example Deviation:**
- **Deviation:** Unit test coverage 98% (target 100%)
- **Justification:** Legacy code refactoring in progress
- **Risk Assessment:** LOW (legacy code not used in critical path)
- **Approval:** QA Manager approved with condition (legacy code refactor by next release)

---

## 12. COMPLIANCE AND REGULATORY CONSIDERATIONS

### 12.1 IEC 62304 Compliance

**IEC 62304 §5.5 Software Unit Testing:**
- ✅ All Class C units have unit tests
- ✅ Unit tests documented in TESTREP-001
- ✅ Automated execution in CI/CD

**IEC 62304 §5.6 Software Integration Testing:**
- ✅ All interfaces tested (API, LIS, database)
- ✅ Integration tests documented in TESTREP-002
- ✅ Traceability to SDD-001 interfaces

**IEC 62304 §5.7 Software System Testing:**
- ✅ All requirements tested (28 functional + 7 non-functional)
- ✅ System tests documented in TESTREP-003
- ✅ Traceability to SRS-001 requirements

**IEC 62304 §5.8 Software Release Testing:**
- ✅ Pre-release regression testing (all CRITICAL/HIGH tests)
- ✅ Clinical validation (UAT)
- ✅ Final sign-off by QA Manager + Regulatory Affairs

### 12.2 ANVISA RDC 657/2022 Compliance

**Article 6 (V&V Requirements):**
- ✅ Verification & Validation Plan (VVP-001 v1.0) ✅ THIS DOCUMENT
- ✅ Test Specification (TST-001 v1.0)
- ✅ Test Reports (TESTREP-001 to TESTREP-004) - IN PROGRESS
- ✅ Traceability Matrix (TRC-001 v1.0)
- ✅ Clinical Validation (CER-001 v1.0 + PPC-001 study)

### 12.3 IEC 62366-1 Compliance (Usability)

**Usability Engineering File (UEF-001):**
- Summative evaluation with 10+ hematologists
- Critical tasks success rate 100% (mandatory)
- Documented in TESTREP-004 (Validation Tests Report)

**Traceability:** → IEC 62366-1:2015 → TEST-HD-013 (HFE Summative)

---

## 13. REFERENCES

### 13.1 Normative References

1. **IEC 62304:2006+A1:2015** - Medical device software - Software life cycle processes
2. **IEC 62366-1:2015** - Medical devices - Part 1: Application of usability engineering to medical devices
3. **ISO 14971:2019** - Medical devices - Application of risk management to medical devices
4. **ISO 13485:2016** - Medical devices - Quality management systems
5. **ANVISA RDC 657/2022** - Registro de Software como Dispositivo Médico (SaMD)
6. **ANVISA RDC 751/2022** - Classificação de Dispositivos Médicos

### 13.2 Project References

1. **SRS-001 v1.0** - Software Requirements Specification
2. **SDD-001 v1.0** - Software Design Document
3. **TST-001 v1.0** - Test Specification Document
4. **TRC-001 v1.0** - Traceability Matrix
5. **RMP-001 v1.0** - Risk Management Plan (ISO 14971:2019)
6. **CER-001 v1.0** - Clinical Evaluation Report
7. **PMS-001 v1.0** - Post-Market Surveillance Plan
8. **IFU-001 v1.0** - Instructions for Use (PT-BR + EN-US)
9. **PPC-001 v1.0** - Protocolo de Pesquisa Clínica (CEP-approved)

### 13.3 External References

1. **FDA Guidance:** Content of Premarket Submissions for Software Contained in Medical Devices (2005)
2. **FDA Guidance:** Software Validation (1997, updated 2002)
3. **IMDRF SaMD Working Group:** Software as a Medical Device (SaMD): Clinical Evaluation (2017)

---

## 14. APPENDICES

### Appendix A: Test Case Summary

*See TST-001 v1.0 for detailed test cases*

**Total Test Cases:** 30+ (TEST-HD-001 to TEST-HD-029 + TEST-SEC-001 to TEST-SEC-010)

**By Priority:**
- CRITICAL: 15 test cases (50%)
- HIGH: 10 test cases (33%)
- MEDIUM: 5 test cases (17%)

**By Type:**
- Functional: 20 test cases (67%)
- Non-Functional: 10 test cases (33%)

### Appendix B: Test Environment Details

*See Section 7 for full environment specifications*

### Appendix C: Test Data Catalog

**Synthetic Datasets:**
- synthetic_cbc_normal.csv (n=100)
- synthetic_cbc_anemia.csv (n=100)
- synthetic_cbc_edge_cases.csv (n=50)

**Anonymized Real Data:**
- cer_001_retrospective_2847_cases.csv (CER-001 validation)
- cer_001_prospective_1523_cases.csv (CER-001 validation)
- ppc_001_uat_1500_cases.csv (PPC-001 clinical study) - PENDING

**Data Access:**
- All datasets stored in encrypted AWS S3 bucket
- Access restricted to QA team (RBAC enforced)
- LGPD-compliant (no PHI)

### Appendix D: Glossary

| Term | Definition |
|------|------------|
| **V&V** | Verification & Validation |
| **SaMD** | Software as Medical Device |
| **UAT** | User Acceptance Testing |
| **HFE** | Human Factors Engineering |
| **PHI** | Protected Health Information |
| **LGPD** | Lei Geral de Proteção de Dados (Brazil GDPR) |
| **ANVISA** | Agência Nacional de Vigilância Sanitária (Brazil FDA) |
| **CBC** | Complete Blood Count |
| **TTD** | Time-to-Diagnosis |
| **CAPA** | Corrective and Preventive Action |
| **PMS** | Post-Market Surveillance |

---

## APPROVAL SIGNATURES

### Quality Assurance

**Name:** {QA Manager Name}  
**Role:** QA Manager  
**Signature:** ______________________________  
**Date:** ____/____/______

### Software Development

**Name:** {Software Architect Name}  
**Role:** Software Architect  
**Signature:** ______________________________  
**Date:** ____/____/______

### Regulatory Affairs

**Name:** {Regulatory Affairs Director Name}  
**Role:** Regulatory Affairs Director  
**Signature:** ______________________________  
**Date:** ____/____/______

---

**Document:** VVP-001  
**Version:** v1.0 OFICIAL  
**Date:** 12 de Outubro de 2025  
**Next Review:** 12 de Outubro de 2026 (annual) or after significant software changes

---

**END OF VERIFICATION & VALIDATION PLAN**
