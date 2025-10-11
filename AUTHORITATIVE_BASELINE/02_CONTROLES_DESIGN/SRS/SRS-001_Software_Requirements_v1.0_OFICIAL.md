# SRS-001 — Software Requirements Specification

**Código:** SRS-001
**Versão:** v1.0 (MERGED)
**Data:** 2025-10-07
**Autor(es):** Agente HemoDoctor SaMD | Abel Costa
**Revisores:** {REVISORES}
**Aprovadores:** {APROVADORES}
**Status:** Consolidation Review
**Confidencialidade:** Interno/Confidencial

---

## 1. Scope & Purpose

**Product:** HemoDoctor SaMD (Software as Medical Device)
**Classification:** **Class C (IEC 62304)** | ANVISA Class III | FDA Class III
**Type:** Software-based CDSS (Clinical Decision Support System) for Complete Blood Count (CBC) evaluation and suggested clinical next steps
**Intended Use:** Assist healthcare professionals in hematological diagnosis and treatment planning

---

## 2. User Needs → Requirements Mapping

| User Need | REQ-ID | Description |
|-----------|--------|-------------|
| UN-001 | REQ-HD-001 | Faster diagnosis decisions → Automated anemia detection |
| UN-002 | REQ-HD-012 | Manage alert burden → Intelligent alert prioritization |
| UN-003 | REQ-HD-020 | Mitigate automation bias → Rationale transparency + override |
| UN-004 | REQ-HD-050 | High availability → System reliability ≥99.5% |
| UN-005 | REQ-HD-060 | Cyber resilience → Secure architecture + SBOM |

---

## 3. Functional Requirements

### REQ-HD-001: Critical Anemia Detection
**Priority:** CRITICAL
**Description:** Identify **severe anemia** (Hb below age/sex/pregnancy-adjusted threshold) with **sensitivity ≥90%** (target 100% for POC validation)
**Behavior:** Generate CRITICAL_ALERT with immediate notification
**Acceptance Criteria:**
- Sensitivity ≥90% (per TRC-001)
- False negative rate <10%
- Alert latency P95 < 2s
**Traceability:** → SDD-001 §3.2 → TEST-HD-011 (ROC/PR curves) → RISK-HD-001 → IFU-001 §Performance → PMS-001 §SLAs

### REQ-HD-002: CBC Data Ingestion and Validation
**Priority:** HIGH
**Description:** Allow ingestion of CBC + complementary tests (ferritin, iron, B12, folate, LDH, etc.) with **unit validation** and age/sex/pregnancy-specific reference ranges
**Input Data:**
- **CBC Core:** Hb, Ht, MCV, RDW, WBC (total + differential), Platelets, Reticulocytes
- **Complementary:** Ferritin, serum iron, B12, folate, LDH, hemolysis markers, renal/thyroid/inflammatory function
- **Metadata:** Patient age, sex, pregnancy status, comorbidities
**Validation:**
- Unit conversion (g/dL ↔ g/L, mg/dL ↔ μmol/L)
- LOINC code mapping (when applicable)
- Out-of-range detection per patient profile
**Acceptance Criteria:** 100% unit validation, zero unit-related errors in production

### REQ-HD-003: Clinical Rationale Transparency
**Priority:** HIGH
**Description:** Display **clinical rationale** (rules, sources, confidence) for each recommendation to enable informed clinician decision-making
**Behavior:**
- Show triggered clinical rules (e.g., "Hb <7 g/dL + MCV <80 fL → Iron deficiency anemia suspected")
- Display evidence sources (guidelines, literature)
- Uncertainty quantification (confidence intervals, prediction intervals)
- Allow clinician override with mandatory justification logging
**Acceptance Criteria:** 100% recommendations have rationale, user can access full rule set

### REQ-HD-004: Audit Trail and Logging
**Priority:** CRITICAL (regulatory compliance)
**Description:** Export **auditable logs** (WORM - Write Once Read Many) capturing all clinical decisions, user interactions, and system events
**Logged Events:**
- CBC data ingestion timestamp + user ID
- Risk score computation + algorithm version
- Recommendations generated + confidence
- Clinician decisions (accept/override/defer)
- Justifications for overrides
- System alerts and exceptions
**Retention:** Per LGPD/GDPR requirements (minimum 5 years for medical records in Brazil)
**Acceptance Criteria:** Zero audit gaps, immutable logs, exportable to CSV/JSON

### REQ-HD-005: LIS/HIS Integration API
**Priority:** HIGH
**Description:** Provide REST API for integration with Laboratory Information Systems (LIS) and Hospital Information Systems (HIS) with secure authentication (OIDC/OAuth2)
**Endpoints:**
- POST /api/v1/cbc/analyze - Submit CBC data for analysis
- GET /api/v1/results/{case_id} - Retrieve analysis results
- GET /api/v1/audit/{case_id} - Retrieve audit trail
**Authentication:** OpenID Connect (OIDC) or OAuth2 with MFA
**Rate Limiting:** 100 requests/min per client
**Interoperability:** Support HL7 FHIR R4 (optional), CSV/Parquet import

---

## 4. Non-functional Requirements

### NFR-001: Performance
- **Latency:** P95 ≤ 2s per CBC case analysis
- **Throughput:** Support 1000 cases/hour per instance
- **Scalability:** Horizontal scaling support (containerized deployment)

### NFR-002: Reliability
- **Uptime:** ≥99.5% availability (SLA)
- **Automated Regression Testing:** 100% critical paths covered
- **Failover:** Graceful degradation if ML model unavailable (fallback to rule-based)

### NFR-003: Security & Cybersecurity
- **IAM:** Role-Based Access Control (RBAC) + Multi-Factor Authentication (MFA)
- **Encryption:** TLS 1.3 for data in transit, AES-256 for data at rest
- **SBOM:** Software Bill of Materials (CycloneDX/SPDX format)
- **SAST/DAST:** Static and Dynamic Application Security Testing in CI/CD
- **Threat Model:** STRIDE-based threat analysis documented
- **Compliance:** FDA §524B Cybersecurity requirements
- **Vulnerability Management:** CVD (Coordinated Vulnerability Disclosure), VEX (Vulnerability Exploitability eXchange)
- **Secure Updates:** Signed updates with rollback capability

### NFR-004: Privacy
- **Data Minimization:** Collect only clinically necessary data
- **Pseudonymization:** De-identify PHI in logs and exports
- **Retention & Disposal:** Automated data lifecycle management (retention policy + secure deletion)
- **Compliance:** LGPD (Brazil) / GDPR (EU) / HIPAA (US if applicable)

---

## 5. Data Dictionary

### CBC Core Parameters:
| Variable | Unit | Reference Range (Example: Adult Male) | LOINC |
|----------|------|---------------------------------------|-------|
| Hemoglobin (Hb) | g/dL | 13.5-17.5 | 718-7 |
| Hematocrit (Ht) | % | 38-50 | 4544-3 |
| MCV | fL | 80-100 | 787-2 |
| RDW | % | 11.5-14.5 | 788-0 |
| WBC | 10³/μL | 4.5-11.0 | 6690-2 |
| Neutrophils | 10³/μL | 1.5-8.0 | 751-8 |
| Lymphocytes | 10³/μL | 1.0-4.8 | 731-0 |
| Platelets | 10³/μL | 150-400 | 777-3 |
| Reticulocytes | % | 0.5-2.5 | 4679-7 |

### Complementary Tests:
| Variable | Unit | Clinical Use | LOINC |
|----------|------|--------------|-------|
| Ferritin | ng/mL | Iron deficiency diagnosis | 2276-4 |
| Serum Iron | μg/dL | Iron metabolism | 2498-4 |
| Vitamin B12 | pg/mL | Megaloblastic anemia | 2132-9 |
| Folate | ng/mL | Megaloblastic anemia | 2284-8 |
| LDH | U/L | Hemolysis marker | 2532-0 |

**Note:** Reference ranges vary by age, sex, pregnancy status, and altitude. System must support patient-profile-specific thresholds.

---

## 6. Interfaces

### 6.1 External Interfaces
- **REST API:** JSON over HTTPS (OpenAPI v1.1 spec)
- **Messaging (optional):** AMQP/Kafka for asynchronous LIS integration
- **FHIR R4 (optional):** Interoperability with EHR systems
- **CSV/Parquet:** Bulk import for batch processing

### 6.2 User Interface
- **Web UI:** For laboratory operators (React-based SPA)
- **Critical Tasks:**
  - Review and approve automated reports
  - Override recommendations with justification
  - Export audit logs
- **Accessibility:** WCAG 2.1 Level AA compliance
- **Usability Testing:** IEC 62366-1 conformity (documented in separate HFE report)

### 6.3 Observability
- **Metrics:** Prometheus-compatible endpoints (latency, throughput, error rates)
- **Logging:** Structured JSON logs (ELK/Splunk compatible)
- **Tracing:** Distributed tracing (OpenTelemetry)
- **Audit Trail:** Separate immutable audit database (append-only)

---

## 7. Safety & Risk Controls (ISO 14971 Linkage)

### Risk Mitigation Strategies:
- **False Negative/Positive Thresholds:** Configurable sensitivity/specificity tradeoffs
- **Alert Throttling:** Prevent alert fatigue (max 3 critical alerts per session)
- **Training & HFE:** Mandatory user training + Human Factors Engineering validation
- **Failover:** Rule-based fallback if ML model fails
- **Manual Override:** Clinician can always override with audit trail

### Link to Risk Management:
- **RISK-HD-101:** False negative severe anemia → Mitigation: High sensitivity (≥90%)
- **RISK-HD-102:** Alert fatigue → Mitigation: Alert throttling + prioritization
- **RISK-HD-103:** Automation bias → Mitigation: Mandatory rationale display
- **RISK-HD-104:** Data breach → Mitigation: Encryption + RBAC + Audit
- **RISK-HD-105:** Cyberattack → Mitigation: SBOM + SAST/DAST + Secure updates
- **RISK-HD-106:** System downtime → Mitigation: Failover + 99.5% SLA

Detailed risk analysis in **RMP-001** (Risk Management Plan).

---

## 8. Cybersecurity (FDA §524B Compliance)

### Cybersecurity Controls:
- **CVD (Coordinated Vulnerability Disclosure):** Public security.txt + bug bounty
- **SBOM:** CycloneDX/SPDX format, updated per release
- **VEX (Vulnerability Exploitability eXchange):** Communicate patch status for known CVEs
- **Secure Update/Rollback:** Signed firmware/software updates with atomic rollback
- **Logging:** Security event logging (failed auth, privilege escalation attempts)
- **RBAC:** Least privilege access control
- **Crypto Baselines:** NIST FIPS 140-2 compliant cryptographic modules

### Threat Model:
- **STRIDE Analysis:** Documented in **SEC-001** (Cybersecurity documentation)
- **Attack Surface:** Network (API), Physical (server access), Supply Chain (dependencies)

---

## 9. Verification & Validation

### Verification (IEC 62304 §5.5-5.7):
- Each REQ-ID mapped to TEST-ID in **TRC-001** (Traceability Matrix)
- Unit tests: 80% code coverage minimum
- Integration tests: 100% API endpoint coverage
- System tests: End-to-end clinical scenarios

### Validation (IEC 62304 §5.8):
- Clinical validation: ROC/PR curves (TEST-HD-011)
- Usability validation: IEC 62366-1 HFE testing
- Post-market validation: PMS-001 real-world performance monitoring

### Pass/Fail Criteria:
- All critical requirements (CRITICAL priority): 100% pass rate
- High priority requirements: ≥95% pass rate
- Performance NFRs: Meet or exceed specified thresholds

---

## 10. Traceability

### Requirements Linkage:
**REQ ↔ Design ↔ Tests ↔ Risks ↔ Label ↔ PMS**

Example (REQ-HD-001):
```
REQ-HD-001 (Anemia detection, Sensitivity ≥90%)
  → SDD-001 §3.2 (Algorithm design)
  → TEST-HD-011 (ROC/PR validation, confusion matrix)
  → RISK-HD-001 (False negative risk mitigation)
  → IFU-001 §Performance (User-facing performance claims)
  → PMS-001 §SLAs (Real-world sensitivity monitoring)
```

Full traceability documented in **TRC-001_Traceability_Matrix_v1.0.csv** (18 requirements mapped, 100% coverage).

---

## 11. Standards & Regulatory Guidance

| Content Area | Standard/Regulation | Compliance |
|--------------|---------------------|------------|
| Software Lifecycle | IEC 62304:2006/Amd 1:2015 | Class C |
| Risk Management | ISO 14971:2019 | Full |
| Quality Management | ISO 13485:2016 | Full |
| Clinical Evidence | ANVISA RDC 657/2022 | Class III |
| SaMD Registration | ANVISA RDC 751/2022 | Class III |
| AI/ML Reporting | TRIPOD-AI, MI-CLAIM | Guidelines |
| Usability | IEC 62366-1:2015 | Full |
| Cybersecurity | FDA §524B | Full |
| Privacy | LGPD (Brazil), GDPR (EU) | Full |
| Security | ISO/IEC 27001:2022, OWASP ASVS | Baselines |

---

## 12. Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v0.0 | 2025-09-16 | HemoDoctor Agent | Initial draft with Class C declaration |
| v1.0 | 2025-09-19 | HemoDoctor Agent | Added detailed CBC requirements |
| v1.0 (MERGED) | 2025-10-07 | Abel Costa | Merged v0.0 + v1.0, added traceability, cybersecurity |

---

**Next Steps:**
1. Review with @software-architecture-specialist
2. Validate traceability with TRC-001 (all 18 requirements must be present)
3. Cross-check with SDD-001 (design must cover all requirements)
4. Approval by regulatory team

---

**END OF DOCUMENT**
