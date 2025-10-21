# TEC-001 — Software Development Plan (SDP)

**Código:** TEC-001
**Versão:** v1.0 (MERGED - OFICIAL)
**Data:** 2025-10-07
**Autores:** Sofia Lima (Engenharia de Software MedTech) | Abel Costa (Consolidação)
**Revisores:** Helena Costa (RA/QA) | {REVISORES ANVISA}
**Aprovadores:** Diretor de Tecnologia | {APROVADORES}
**Status:** Consolidation Review
**Confidencialidade:** Controlado

---

## Executive Summary

This **Software Development Plan (SDP)** defines the lifecycle process for all software components of the **HemoDoctor SaMD** system. The purpose is to ensure systematic, controlled, and traceable development in full compliance with **IEC 62304:2006+A1:2015** for medical device software.

Based on preliminary risk analysis identifying potential for serious harm in case of failure, HemoDoctor SaMD software is classified as **Safety Class C** under IEC 62304, mandating the highest level of documentary and procedural rigor.

This plan details the adapted **V-Model lifecycle**, development activities, risk management processes, configuration management, problem resolution, and SOUP validation approach. This document serves as the master reference for all software engineering activities, ensuring the final product is safe, effective, and ready for regulatory submission (ANVISA Class III / FDA Class III).

---

## Resumo Executivo (Português)

Este **Plano de Desenvolvimento de Software (SDP)** define o processo de ciclo de vida para todos os componentes de software do sistema **HemoDoctor SaMD**. O objetivo é garantir desenvolvimento sistemático, controlado e rastreável, em total conformidade com a **IEC 62304:2006+A1:2015** para software de dispositivo médico.

Com base em análise de risco preliminar que identificou potencial de dano grave em caso de falha, o software HemoDoctor SaMD é classificado como **Classe de Segurança C** segundo a IEC 62304, exigindo o mais alto nível de rigor documental e processual.

Este plano detalha o **ciclo de vida V-Model** adaptado, atividades de desenvolvimento, processos de gerenciamento de risco, configuração e resolução de problemas, bem como a abordagem para validação de SOUP (Software of Unknown Provenance). Este documento é a referência mestra para todas as atividades de engenharia de software, garantindo que o produto final seja seguro, eficaz e pronto para submissão regulatória (ANVISA Classe III / FDA Classe III).

---

## 1. Scope and Context

### 1.1 Applicable Software

This SDP applies to all software developed and maintained for the HemoDoctor SaMD system, including:

1. **Embedded Software (Firmware):** Software operating on HemoSphere hardware device (if applicable)
2. **Cloud Platform:** Backend application receiving data, executing AI algorithm, managing user interface
3. **HemoAI Algorithm:** Machine Learning (ML) component performing CBC analysis
4. **API Layer:** REST/FHIR interfaces for LIS/HIS integration
5. **Web UI:** React-based operator dashboard
6. **Audit Service:** Immutable logging and traceability system

**Product Classification:**
- **ANVISA:** Class III SaMD (RDC 751/2022)
- **FDA:** Class III SaMD
- **IEC 62304:** **Safety Class C** (highest safety classification)

### 1.2 Intended Use

HemoDoctor SaMD is a Clinical Decision Support System (CDSS) for Complete Blood Count (CBC) evaluation that:

1. **Classifies** CBCs as *review-required* or *no-review* with high sensitivity (≥90%)
2. **Generates probabilities and scores** (HD_SCORE) and **diagnostic suggestions** (HD_SUGG) to support physicians
3. **Prioritizes cases** and provides performance metrics to reduce turnaround time and costs
4. **Records usage logs** ensuring data integrity and traceability

---

## 2. Regulatory Standards and References

### 2.1 Applicable Standards

| Standard | Title | Compliance |
|----------|-------|------------|
| **IEC 62304:2006+A1:2015** | Medical device software - Software life cycle processes | Class C |
| **ISO 13485:2016** | Medical devices - Quality management systems | Full |
| **ISO 14971:2019** | Medical devices - Application of risk management | Full |
| **IEC 62366-1:2015** | Medical devices - Usability engineering | Full |
| **ANVISA RDC 657/2022** | Clinical evidence requirements for SaMD | Class III |
| **ANVISA RDC 751/2022** | SaMD registration requirements | Class III |
| **FDA 21 CFR Part 820** | Quality System Regulation | Applicable |
| **FDA §524B** | Cybersecurity requirements | Full |

### 2.2 Related Documents

- **SRS-001 v1.0:** Software Requirements Specification
- **SDD-001 v1.0:** Software Design Document
- **TST-001:** Test Plan and Test Reports
- **RMP-001 (TEC-002):** Risk Management File (ISO 14971)
- **QMS-001:** Quality Management System Manual
- **SEC-001:** Cybersecurity Documentation (SBOM, CVD, VEX)
- **TRC-001:** Traceability Matrix
- **SOUP-001:** Software of Unknown Provenance Analysis

---

## 3. Software Lifecycle Model

### 3.1 V-Model Overview

HemoDoctor development follows the **V-Model** adapted for IEC 62304:

```
        Requirements ←→ Validation
              ↓             ↑
         Architecture ←→ Integration Testing
              ↓             ↑
      Detailed Design ←→ Unit Testing
              ↓             ↑
          Implementation
```

**Phases:**

1. **Software Planning** (this document - TEC-001)
2. **Requirements Analysis** (SRS-001)
3. **Architecture Design** (SDD-001 high-level)
4. **Detailed Design** (SDD-001 components)
5. **Implementation & Unit Testing** (Code + TST-001)
6. **Integration Testing** (TST-001)
7. **System Testing** (TST-001)
8. **Validation** (Clinical validation, usability testing)
9. **Release** (Deployment procedures)
10. **Maintenance** (Post-market surveillance, updates)

### 3.2 Rationale for V-Model

**Why V-Model for Class C:**
- Enforces traceability: Each requirement mapped to design, test, and validation
- Early verification planning: Test cases defined during requirements phase
- Risk mitigation: Design reviews and inspections at each stage
- Regulatory compliance: Aligns with IEC 62304 §5.x processes

---

## 4. Development Activities per IEC 62304

### 4.1 Software Development Planning (§5.1)

**Deliverables:**
- TEC-001 (this document)
- Software Development Plan updates for each release

**Activities:**
- Define lifecycle model
- Identify deliverables and milestones
- Establish verification and validation plans
- Define configuration management plan
- Define problem resolution plan
- Identify SOUP components

**Responsibility:** Software Development Manager + QA Lead

---

### 4.2 Software Requirements Analysis (§5.2)

**Deliverables:**
- SRS-001 Software Requirements Specification

**Activities:**
- Transform user needs into software requirements (UN-001 → REQ-HD-001, etc.)
- Define functional requirements (FR-001 to FR-004, REQ-HD-001 to REQ-HD-005)
- Define non-functional requirements (performance, security, usability)
- Identify safety requirements and risk controls
- Establish requirements traceability

**Acceptance Criteria:**
- All requirements have unique ID
- All requirements testable/verifiable
- Requirements reviewed and approved by stakeholders

**Responsibility:** Requirements Engineer + Clinical SME + QA

**Traceability:** SRS-001 → SDD-001 (design) → TST-001 (tests)

---

### 4.3 Software Architectural Design (§5.3)

**Deliverables:**
- SDD-001 Software Design Document (§2 Architecture)
- Global Architecture Diagram (TEC-001_Diagram_Global_Architecture_20250916.png)

**Activities:**
- Define high-level architecture (microservices)
- Identify software items (components/services)
- Define interfaces between items and external systems
- **Segregate software items by safety class** (Class C: Rules Engine, HemoAI, Alerts)
- Specify risk control measures in architecture
- Document SOUP components and interfaces

**Acceptance Criteria:**
- Architecture supports all requirements
- Safety-critical components isolated
- Interfaces well-defined with contracts
- Architecture reviewed and approved

**Responsibility:** Software Architect + Security Engineer

**Traceability:** SRS-001 → SDD-001 §2 → Integration Tests (TST-001)

---

### 4.4 Software Detailed Design (§5.4)

**Deliverables:**
- SDD-001 §3-9 (Component Design, Sequence Diagrams, Data Model)

**Activities:**
- Refine each software item into detailed units
- Define algorithms and data structures
- Specify unit interfaces and contracts
- Document design decisions and trade-offs
- Identify and document SOUP usage within units

**Acceptance Criteria:**
- Design traceable to architecture and requirements
- All units have clear responsibilities
- Design supports verification strategy
- Design reviewed with focus on safety and security

**Responsibility:** Software Engineers + Code Reviewers

**Traceability:** SDD-001 §2 → SDD-001 §3-9 → Unit Tests (TST-001)

---

### 4.5 Software Unit Implementation and Verification (§5.5)

**Deliverables:**
- Source code (Git repository)
- Unit test code and reports
- Code review records

**Activities:**
- Implement software units per detailed design
- Apply coding standards (PEP 8 for Python, ESLint for JavaScript)
- Perform code reviews (pull request process)
- Execute unit tests (pytest, Jest)
- Achieve code coverage targets (≥80% for Class C)
- Static analysis (SonarQube, Pylint)

**Coding Standards:**
- **Python:** PEP 8, type hints (mypy), docstrings
- **JavaScript:** ESLint + Airbnb style guide
- **Security:** OWASP ASVS guidelines, no hardcoded secrets

**Acceptance Criteria:**
- All units pass unit tests
- Code coverage ≥80%
- Zero critical/high severity issues in static analysis
- Code reviewed and approved by peer

**Responsibility:** Software Developers + Code Reviewers

**Tools:**
- **Version Control:** Git + GitHub/GitLab
- **CI/CD:** GitHub Actions / GitLab CI
- **Testing:** pytest (Python), Jest (JavaScript)
- **Static Analysis:** SonarQube, Pylint, ESLint
- **Code Coverage:** coverage.py, Istanbul

---

### 4.6 Software Integration and Integration Testing (§5.6)

**Deliverables:**
- Integration test plan and reports (TST-001)
- Integrated software build

**Activities:**
- Integrate software units according to integration plan
- Execute integration tests (API tests, service-to-service tests)
- Verify interfaces between components
- Test error handling and edge cases
- Document integration issues and resolutions

**Integration Strategy:**
- Bottom-up integration (units → components → services)
- Continuous integration (automated builds on each commit)

**Acceptance Criteria:**
- All integration tests pass
- No integration defects outstanding
- Performance meets NFR-001 targets (P95 latency <2s)

**Responsibility:** Integration Test Engineer + DevOps

**Tools:**
- **Integration Testing:** Postman/Newman, pytest with fixtures
- **Service Mocking:** WireMock, Docker Compose for test environments

---

### 4.7 Software System Testing (§5.7)

**Deliverables:**
- System test plan and reports (TST-001, TEST-HD-004 to TEST-HD-016)
- Regression test suite

**Activities:**
- Execute end-to-end system tests
- Verify all requirements (SRS-001)
- Perform regression testing (automated test suite)
- Test with production-like data
- Validate risk control measures (RMP-001)
- Security testing (SAST/DAST, penetration testing)

**Test Types:**
- **Functional:** All REQ-HD-001 to REQ-HD-005 verified
- **Performance:** Latency, throughput, scalability (NFR-001, NFR-002)
- **Security:** OWASP Top 10, §524B cybersecurity (NFR-003)
- **Usability:** IEC 62366-1 critical tasks (NFR-003)
- **Robustness:** Edge cases, error handling, failover

**Acceptance Criteria:**
- 100% critical requirements pass
- ≥95% high-priority requirements pass
- Zero high-severity defects open
- Regression suite passes

**Responsibility:** QA Engineer + Clinical Validation Lead

---

### 4.8 Software Release (§5.8)

**Deliverables:**
- Release package (Docker images, binaries, documentation)
- Release notes
- DMR MANIFEST with checksums (SHA256)
- Deployment runbook

**Activities:**
- Final verification of all deliverables (docs, code, tests)
- Generate SBOM (CycloneDX format via SEC-001)
- Archive source code and build artifacts (S3 + Git tag)
- Create deployment package
- Update traceability matrix (TRC-001)
- Obtain final approvals (QA + Regulatory + CTO)

**Release Checklist:**
- [ ] All tests passed (unit, integration, system)
- [ ] Code coverage ≥80%
- [ ] Documentation complete and approved (SRS, SDD, TST, RMP)
- [ ] SBOM generated and reviewed (no critical vulnerabilities)
- [ ] Traceability matrix 100% complete (TRC-001)
- [ ] Regulatory submission package prepared
- [ ] Deployment runbook tested in staging

**Responsibility:** Release Manager + QA + Regulatory

---

## 5. Supporting Processes

### 5.1 Configuration Management (§5.1.9, §8)

**Objective:** Ensure all software items, documents, and deliverables are uniquely identified, versioned, and controlled.

**Activities:**
- **Version Control:** Git with semantic versioning (MAJOR.MINOR.PATCH)
- **Branching Strategy:** Gitflow (main, develop, feature/*, release/*, hotfix/*)
- **Baseline Management:** Tag releases (e.g., `v1.0.0`, `v1.1.0`)
- **Document Control:** All docs versioned (e.g., SRS-001 v1.0, SDD-001 v1.0)
- **Configuration Items:** Source code, tests, docs, SBOM, build scripts
- **Archive:** Released versions stored in S3 with immutability enabled

**Change Control Process:**
1. Change request submitted (Jira/GitHub issue)
2. Impact analysis (requirements, design, tests, risks)
3. Approval by Change Control Board (CCB)
4. Implementation + verification
5. Update traceability matrix (TRC-001)
6. Document change in release notes

**Responsibility:** Configuration Manager + Development Team

**Tools:**
- **Git:** Version control for code
- **Confluence/SharePoint:** Document management
- **Jira:** Issue tracking and change requests
- **S3:** Artifact archive with versioning

---

### 5.2 Problem Resolution (§9)

**Objective:** Systematically identify, record, analyze, and resolve problems (bugs, defects, incidents).

**Problem Categories:**
- **P1 - Critical:** System down, data loss, patient safety risk → Fix within 4 hours
- **P2 - High:** Major functionality broken → Fix within 24 hours
- **P3 - Medium:** Minor functionality issue → Fix within 1 week
- **P4 - Low:** Cosmetic, documentation errors → Fix in next release

**Problem Resolution Workflow:**
1. **Report:** Problem reported in Jira with reproducible steps
2. **Triage:** Categorize severity and assign to developer
3. **Analysis:** Root cause analysis (5 Whys, fishbone diagram)
4. **Fix:** Implement fix + unit test + regression test
5. **Verification:** QA verifies fix in test environment
6. **Regression Analysis:** Check if fix introduces new problems
7. **Closure:** Update documentation if needed, close issue

**Post-Market Problems:**
- Reported via PMS-001 Post-Market Surveillance
- Mandatory reporting to ANVISA per Tecnovigilância regulations
- Corrective and Preventive Action (CAPA) initiated if pattern detected

**Responsibility:** Problem Resolution Lead + QA + Regulatory (for post-market)

**Tools:**
- **Jira:** Issue tracking and workflow management
- **Sentry:** Runtime error monitoring

---

### 5.3 Risk Management Integration (§7)

**Objective:** Integrate risk management activities throughout the software lifecycle per ISO 14971.

**Risk Management File:** RMP-001 (TEC-002)

**Integration Points:**

| Lifecycle Phase | Risk Activity | Deliverable |
|-----------------|---------------|-------------|
| Requirements | Identify safety requirements | SRS-001 §6 Risk Controls |
| Architecture | Identify risk control measures in architecture | SDD-001 §7 Safety Design |
| Detailed Design | Refine risk controls | SDD-001 components with fail-safe |
| Implementation | Implement risk control measures | Code with error handling, validation |
| Testing | Verify risk control measures | TEST-HD-011 (sensitivity ≥90%), FMEA validation |
| Validation | Validate residual risk acceptable | Clinical validation report (CER-001) |
| Post-Market | Monitor residual risk | PMS-001 real-world performance |

**Risk-based Testing:**
- High-risk requirements (REQ-HD-001: anemia detection) → 100% test coverage
- Medium-risk requirements → ≥80% test coverage
- Low-risk requirements → ≥50% test coverage

**Responsibility:** Risk Manager + Software Development Team

**Traceability:** RISK-HD-001 to RISK-HD-106 (RMP-001) → REQ-HD-xxx (SRS-001) → Tests (TST-001)

---

### 5.4 SOUP Management (§8.1.2)

**Objective:** Identify, evaluate, and validate all Software of Unknown Provenance (third-party libraries, frameworks, open-source components).

**SOUP Analysis Deliverable:** SOUP-001 (to be created - CRITICAL GAP)

**SOUP Validation Activities:**

1. **Identification:**
   - List all SOUP components (name, version, purpose)
   - Generate SBOM (CycloneDX/SPDX format)

2. **Evaluation:**
   - Assess each SOUP: license compatibility, security vulnerabilities (CVE), maintenance status
   - Document functional requirements from SOUP (what we depend on)
   - Document known anomalies (bugs, limitations)

3. **Validation:**
   - Test SOUP in context of HemoDoctor system
   - Verify SOUP behavior meets functional requirements
   - Establish monitoring for SOUP updates/vulnerabilities

4. **Maintenance:**
   - Track SOUP updates and security patches
   - Re-validate after SOUP version changes
   - Document in change control

**Example SOUP Components (HemoDoctor):**
- **Python:** numpy, pandas, scikit-learn, xgboost, shap, flask/fastapi
- **JavaScript:** React, axios, Material-UI
- **Infrastructure:** PostgreSQL, Redis, Docker, Kubernetes

**Responsibility:** SOUP Coordinator + Security Engineer

**Tools:**
- **SBOM Generation:** Syft, CycloneDX CLI
- **Vulnerability Scanning:** Snyk, Trivy, OWASP Dependency-Check

---

## 6. Build and Release Procedures

### 6.1 Build Process

**Objective:** Automated, repeatable build process from source code to deployable artifacts.

**Build Pipeline (CI/CD):**

1. **Trigger:** Git push to `develop` or `release/*` branch
2. **Lint:** Run static analysis (Pylint, ESLint)
3. **Unit Tests:** Run pytest, Jest (must pass 100%)
4. **Code Coverage:** Generate coverage report (enforce ≥80%)
5. **SAST:** SonarQube security scan (no critical/high issues)
6. **Build Artifacts:** Create Docker images (HemoAI service, API gateway, UI)
7. **Tag Images:** version tag (e.g., `hemodoctor-api:v1.0.0`)
8. **Push to Registry:** Docker Hub / AWS ECR
9. **Generate SBOM:** CycloneDX JSON for each image
10. **Smoke Tests:** Deploy to staging, run health checks

**Build Tools:**
- **CI/CD Platform:** GitHub Actions / GitLab CI / Jenkins
- **Containerization:** Docker + Docker Compose
- **Artifact Registry:** Docker Hub (private) / AWS ECR

**Build Outputs:**
- Docker images (tagged with semantic version)
- SBOM files (CycloneDX JSON)
- Test reports (JUnit XML format)
- Code coverage reports (HTML + JSON)

**Responsibility:** DevOps Engineer + CI/CD Automation

---

### 6.2 Release Procedures

**Release Types:**

1. **Major Release (X.0.0):** New features, breaking changes, requires full validation
2. **Minor Release (x.Y.0):** New features, backwards compatible, regression testing required
3. **Patch Release (x.y.Z):** Bug fixes only, targeted testing

**Release Procedure:**

1. **Pre-Release:**
   - Create `release/vX.Y.Z` branch from `develop`
   - Run full test suite (unit, integration, system, regression)
   - Generate release notes (changelog from commit history)
   - Update documentation versions (SRS, SDD, etc.)
   - Update TRC-001 traceability matrix

2. **Release:**
   - Merge `release/vX.Y.Z` → `main`
   - Tag `main` with `vX.Y.Z`
   - Build production artifacts
   - Generate final SBOM
   - Create DMR_MANIFEST.json with SHA256 checksums
   - Archive to S3: source code (Git tag), artifacts, docs, SBOM

3. **Deployment:**
   - Deploy to production (blue-green deployment for zero downtime)
   - Run smoke tests in production
   - Monitor logs and metrics (first 24h intensive monitoring)
   - Rollback plan ready (previous version kept warm)

4. **Post-Release:**
   - Update PMS-001 monitoring dashboard
   - Notify stakeholders (clinical users, regulatory)
   - Merge `main` → `develop` (backport any hotfixes)

**Approval Gates:**
- **QA Sign-off:** All tests passed
- **Security Sign-off:** SBOM reviewed, no critical CVEs
- **Regulatory Sign-off:** Documentation complete
- **CTO Approval:** Final go/no-go decision

**Responsibility:** Release Manager + QA + Security + Regulatory + CTO

---

## 7. Maintenance and Updates (§6)

### 7.1 Post-Market Maintenance

**Objective:** Monitor deployed software, address issues, and release updates safely.

**Maintenance Activities:**

1. **Monitoring:**
   - Real-time metrics (Prometheus + Grafana)
   - Error tracking (Sentry)
   - Audit log analysis (detect anomalies)
   - Performance monitoring (latency P95, uptime)

2. **Problem Reports:**
   - User-reported issues (via support portal)
   - Automated error reports (Sentry alerts)
   - Security vulnerability notifications (Snyk, CVE feeds)

3. **Updates:**
   - **Security Patches:** Expedited release (P1 priority)
   - **Bug Fixes:** Patch release (x.y.Z)
   - **Enhancements:** Minor/major release (x.Y.0 / X.0.0)

4. **Re-Validation:**
   - Regression testing for all updates
   - Clinical validation required for algorithm changes (HemoAI updates)
   - Usability re-testing if UI changes

**Responsibility:** Maintenance Team + DevOps + Support

---

### 7.2 Software Update Deployment

**Safe Update Mechanism:**
- **Signed Updates:** All packages signed with private key (verified on deployment)
- **Rollback Capability:** Previous version kept for instant rollback
- **Blue-Green Deployment:** New version deployed alongside old, traffic switched after validation
- **Canary Deployment:** Gradual rollout (10% → 50% → 100% traffic)

**Notification:**
- Users notified 48h before major updates
- Emergency patches deployed with immediate notification

**Traceability:** All updates tracked in PMS-001 post-market surveillance log

---

## 8. Team Roles and Responsibilities

| Role | Responsibilities | IEC 62304 Sections |
|------|------------------|-------------------|
| **Software Development Manager** | Overall SDP execution, resource allocation, schedule | §5.1 Planning |
| **Requirements Engineer** | Requirements elicitation, SRS-001 maintenance | §5.2 Requirements |
| **Software Architect** | Architecture design, SDD-001 high-level design | §5.3 Architecture |
| **Software Engineers** | Detailed design, implementation, unit testing | §5.4-5.5 Design & Implementation |
| **QA Engineer** | Test planning, execution, defect tracking | §5.6-5.7 Testing |
| **Integration Engineer / DevOps** | Integration testing, CI/CD, deployment | §5.6 Integration |
| **Security Engineer** | SBOM, CVD, security testing, SEC-001 | §8.1.2 SOUP, NFR-003 Security |
| **Risk Manager** | Risk analysis, RMP-001, risk-based testing | §7 Risk Management |
| **Configuration Manager** | Version control, baselines, change control | §8 Configuration Management |
| **Problem Resolution Lead** | Issue triage, root cause analysis, CAPA | §9 Problem Resolution |
| **Release Manager** | Release planning, DMR MANIFEST, deployment | §5.8 Release |
| **Clinical SME** | Clinical validation, CER-001, usability testing | Validation |
| **Regulatory Affairs** | Regulatory compliance, ANVISA submission | Overall compliance |

---

## 9. Verification and Validation Summary

### 9.1 Verification Strategy

**Objective:** Ensure software correctly implements specified requirements.

**Verification Activities:**
- **Unit Testing:** Each unit verified against detailed design (§5.5)
- **Integration Testing:** Interfaces verified against architecture (§5.6)
- **System Testing:** All requirements verified (§5.7)
- **Code Reviews:** Peer review of all code changes
- **Static Analysis:** Automated verification of coding standards and security

**Coverage Targets:**
- Unit test coverage: ≥80%
- Integration test coverage: 100% critical paths
- System test coverage: 100% requirements

**Traceability:** TST-001 test cases → SRS-001 requirements (via TRC-001)

---

### 9.2 Validation Strategy

**Objective:** Ensure software meets user needs and intended use.

**Validation Activities:**

1. **Clinical Validation:**
   - ROC/PR curve analysis (TEST-HD-011)
   - Sensitivity ≥90% for REQ-HD-001 (anemia detection)
   - Real-world performance monitoring (PMS-001)

2. **Usability Validation (IEC 62366-1):**
   - Critical tasks testing with representative users
   - Human Factors Engineering (HFE) validation
   - IFU (Instructions for Use) comprehension testing

3. **Performance Validation:**
   - Latency P95 <2s (NFR-001)
   - Uptime ≥99.5% (NFR-002)
   - Scalability testing (1000 cases/hour per instance)

4. **Security Validation:**
   - Penetration testing (OWASP Top 10)
   - Cybersecurity assessment (§524B compliance)

**Acceptance Criteria:**
- Clinical performance meets targets (Sensitivity ≥90%)
- No usability issues in critical tasks
- Performance meets NFRs
- No high-severity security findings

**Responsibility:** Clinical Validation Lead + Usability Engineer + QA

---

## 10. Document Control and Traceability

### 10.1 Document Hierarchy

```
TEC-001 (Software Development Plan)
    ├─> SRS-001 (Requirements)
    │     └─> SDD-001 (Design)
    │           └─> Source Code
    │                 └─> TST-001 (Tests)
    ├─> RMP-001 (Risk Management)
    ├─> SEC-001 (Cybersecurity)
    ├─> SOUP-001 (SOUP Analysis)
    └─> TRC-001 (Traceability Matrix)
```

### 10.2 Traceability

**Full traceability maintained via TRC-001:**
- User Needs → Requirements (UN-001 → REQ-HD-001)
- Requirements → Design (REQ-HD-001 → SDD-001 §3.2)
- Design → Implementation (SDD-001 → Source Code)
- Requirements → Tests (REQ-HD-001 → TEST-HD-011)
- Requirements → Risks (REQ-HD-001 → RISK-HD-001)
- Requirements → Label (REQ-HD-001 → IFU-001 §Performance)
- Requirements → PMS (REQ-HD-001 → PMS-001 §SLAs)

**Traceability Matrix:** TRC-001 v1.0 (18 requirements, 100% coverage)

---

## 11. Standards Compliance Matrix

| IEC 62304 Section | Deliverable | Status |
|-------------------|-------------|--------|
| §5.1 Software Development Planning | TEC-001 (this doc) | ✅ |
| §5.2 Software Requirements Analysis | SRS-001 v1.0 | ✅ |
| §5.3 Software Architectural Design | SDD-001 v1.0 §2 | ✅ |
| §5.4 Software Detailed Design | SDD-001 v1.0 §3-9 | ✅ |
| §5.5 Software Unit Implementation | Source Code + Unit Tests | ✅ |
| §5.6 Software Integration & Testing | Integration Tests (TST-001) | ✅ |
| §5.7 Software System Testing | System Tests (TST-001) | ✅ |
| §5.8 Software Release | DMR MANIFEST + Deployment | ✅ |
| §6 Software Maintenance | PMS-001 + Maintenance Log | ✅ |
| §7 Risk Management | RMP-001 (TEC-002) | ✅ |
| §8 Configuration Management | Git + Change Control | ✅ |
| §8.1.2 SOUP | SOUP-001 | ⚠️ PENDING |
| §9 Problem Resolution | Jira + CAPA | ✅ |

**Critical Gap:** SOUP-001 Analysis (IEC 62304 §8.1.2) - **BLOCKER for submission**

---

## 12. Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-08-28 | Engenharia de Software | Initial draft (V-Model, Classe B declaration) |
| 1.0 | 2025-09-08 | Sofia Lima (GPT/Projeto) | Consolidated for submission, Class C correction |
| 1.0 (MERGED) | 2025-10-07 | Abel Costa | Merged GPT + Projeto versions, enforced Class C, added build/release procedures, SOUP validation, full IEC 62304 compliance |

---

## 13. Approval Signatures

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Software Development Manager** | {NOME} | {ASSINATURA} | {DATA} |
| **QA Lead** | Helena Costa | {ASSINATURA} | {DATA} |
| **Risk Manager** | {NOME} | {ASSINATURA} | {DATA} |
| **Regulatory Affairs** | {NOME} | {ASSINATURA} | {DATA} |
| **CTO (Final Approver)** | {NOME} | {ASSINATURA} | {DATA} |

---

**Next Steps:**
1. Create SOUP-001 Analysis (CRITICAL - 2-3 hours)
2. Validate build/release procedures in staging environment
3. Review with @software-architecture-specialist
4. Obtain regulatory approval for Class C classification
5. Final approval signatures

---

**END OF DOCUMENT**
