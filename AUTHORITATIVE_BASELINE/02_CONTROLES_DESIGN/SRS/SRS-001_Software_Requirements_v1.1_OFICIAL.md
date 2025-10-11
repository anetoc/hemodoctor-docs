# SRS-001 — Software Requirements Specification

**Código:** SRS-001
**Versão:** v1.2 (SYSTEM BOUNDARIES ADDED)
**Data:** 2025-10-08
**Autor(es):** @spec-writer | Abel Costa
**Revisores:** {REVISORES}
**Aprovadores:** {APROVADORES}
**Status:** Under Review - System Boundaries Added (v1.2)
**Confidencialidade:** Interno/Confidencial

---

## 1. Scope & Purpose

**Product:** HemoDoctor SaMD (Software as Medical Device)
**Classification:** **Class C (IEC 62304)** | ANVISA Class III | FDA Class III
**Type:** Software-based CDSS (Clinical Decision Support System) for Complete Blood Count (CBC) evaluation and suggested clinical next steps
**Intended Use:** Assist healthcare professionals in hematological diagnosis and treatment planning

**v1.1 Changes:** Added 10 additional functional requirements (REQ-HD-006 to REQ-HD-015) and expanded NFRs to support enterprise deployment, regulatory compliance, and improved clinical usability.

**v1.2 Changes:** Added Section 1.3 System Boundaries and Limitations to clarify scope (what HemoDoctor IS and IS NOT) and use restrictions per CEO Consultant audit recommendations (QW-002). Added explicit SEC-001 cross-reference in NFR-003/REQ-HD-060 with detailed cybersecurity traceability (QW-003).

### 1.3 System Boundaries and Limitations

**What HemoDoctor IS:**
- Clinical decision support system (CDSS) for CBC interpretation
- Provides suspected diagnoses and recommended next exams
- Integrates with existing LIS/HIS via API

**What HemoDoctor IS NOT:**
- NOT a laboratory analyzer (receives pre-analyzed CBC data)
- NOT a replacement for physician judgment
- NOT a differential diagnosis system for non-hematological conditions
- NOT connected to imaging systems

**Use Restrictions:**
- Requires trained healthcare professional interpretation
- Not for use in emergency triage (decision latency)
- Not for use outside intended population (adults/pediatrics per validation study)

---

## 2. User Needs → Requirements Mapping

| User Need | REQ-ID | Description |
|-----------|--------|-------------|
| UN-001 | REQ-HD-001 | Faster diagnosis decisions → Automated anemia detection |
| UN-002 | REQ-HD-012 | Manage alert burden → Intelligent alert prioritization |
| UN-003 | REQ-HD-020 | Mitigate automation bias → Rationale transparency + override |
| UN-004 | REQ-HD-050 | High availability → System reliability ≥99.5% |
| UN-005 | REQ-HD-060 | Cyber resilience → Secure architecture + SBOM |
| UN-006 | REQ-HD-006 | Configurable alerts per institution → Alert system configuration |
| UN-007 | REQ-HD-007 | ML model quality assurance → Model versioning and rollback |
| UN-008 | REQ-HD-008 | Access control and security → Role-Based Access Control (RBAC) |
| UN-009 | REQ-HD-009 | Regulatory compliance → Data retention and archival (LGPD/ANVISA) |
| UN-010 | REQ-HD-010 | Clinical rule maintenance → Rules specification and versioning |
| UN-011 | REQ-HD-011 | Multi-region deployment → Multi-language support |
| UN-012 | REQ-HD-012 | Operational visibility → Performance monitoring and degradation alerts |
| UN-013 | REQ-HD-013 | Terminology standardization → External terminology server integration |
| UN-014 | REQ-HD-014 | Research capabilities → Batch processing mode |
| UN-015 | REQ-HD-015 | Healthcare interoperability → HL7 FHIR R4 export |

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
**Traceability:** → SDD-001 §3.2, §3.3 → TEST-HD-013 → RISK-HD-101 → IFU-001 §Data Entry → PMS-001 §Error Logs

### REQ-HD-003: Clinical Rationale Transparency
**Priority:** HIGH
**Description:** Display **clinical rationale** (rules, sources, confidence) for each recommendation to enable informed clinician decision-making
**Behavior:**
- Show triggered clinical rules (e.g., "Hb <7 g/dL + MCV <80 fL → Iron deficiency anemia suspected")
- Display evidence sources (guidelines, literature)
- Uncertainty quantification (confidence intervals, prediction intervals)
- Allow clinician override with mandatory justification logging
**Acceptance Criteria:** 100% recommendations have rationale, user can access full rule set
**Traceability:** → SDD-001 §3.8 → TEST-HD-017 → RISK-HD-008, RISK-HD-401 → IFU-001 §Instructions → PMS-001 §Override Rates

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
**Traceability:** → SDD-001 §3.9 → TEST-HD-018 → RISK-HD-103 → IFU-001 §Audit Trail → PMS-001 §Compliance

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
**Traceability:** → SDD-001 §3.1 (API Gateway) → TEST-HD-019 → RISK-HD-104 → IFU-001 §Integration → PMS-001 §API Performance

---

### REQ-HD-006: Alert System Configuration
**Priority:** HIGH
**Description:** Enable **per-institution configuration** of alert thresholds, prioritization rules, and throttling parameters to prevent alert fatigue while maintaining patient safety
**Functionality:**
- **Configurable Thresholds:** Institutions can adjust Hb/WBC/Platelet thresholds within safe ranges (e.g., severe anemia threshold: 6.5-8.0 g/dL)
- **Alert Prioritization:** Four-level system (CRITICAL/HIGH/MEDIUM/LOW) with customizable rules
- **Alert Throttling:** Configurable maximum alerts per time window (default: 3 CRITICAL/hour, 10 HIGH/hour)
- **Intelligent Suppression:** Suppress duplicate alerts for same patient within configurable time window (default: 24 hours)
- **Escalation Rules:** Define escalation paths (e.g., CRITICAL alert → page physician if not acknowledged within 15 min)
**Configuration Interface:**
- Web-based admin portal (RBAC-protected, Admin role only)
- Configuration versioning (Git-backed, with approval workflow)
- Configuration validation (reject unsafe thresholds, e.g., Hb <5 g/dL would trigger safety override)
**Acceptance Criteria:**
- Admin can modify thresholds within safe ranges (±20% of default)
- Alert throttling prevents >3 CRITICAL alerts/hour per default config
- Configuration changes require dual approval (Admin + Clinical SME)
- All configuration changes logged in audit trail
**Traceability:** → SDD-001 §3.7 (Alert Orchestrator) → TEST-HD-020 → RISK-HD-002, RISK-HD-005, RISK-HD-008 → IFU-001 §Configuration → PMS-001 §Alert Metrics

---

### REQ-HD-007: ML Model Versioning and Rollback
**Priority:** CRITICAL
**Description:** Implement **robust ML model lifecycle management** including versioning, A/B testing, performance monitoring, and emergency rollback capability to ensure model quality and patient safety
**Functionality:**
- **Model Versioning:** Track model version (Git SHA + timestamp) for every prediction in audit log
- **Model Registry:** Centralized registry (MLflow or equivalent) storing all model versions with metadata (training date, performance metrics, approval status)
- **A/B Testing:** Deploy new models to subset of traffic (configurable %, default 10%) for validation before full rollout
- **Performance Monitoring:** Real-time monitoring of model performance metrics (sensitivity, specificity, ROC-AUC, drift detection)
- **Automated Alerts:** Generate HIGH alert if model performance degrades >5% from baseline
- **Emergency Rollback:** One-click rollback to previous model version with <15 min downtime
- **Rollback Testing:** Automated tests verify rollback procedure quarterly
**Model Promotion Criteria:**
- ROC-AUC ≥0.85 on validation set (per TRC-001)
- Sensitivity ≥90% for severe anemia detection
- No significant bias detected across age/sex/pregnancy subgroups (fairness testing)
- Dual approval required (Data Scientist + Clinical SME)
**Acceptance Criteria:**
- Every prediction logged with model version ID
- Rollback procedure completes in <15 min (tested quarterly)
- A/B testing supports traffic split 5-50%
- Model performance dashboard updates in real-time (latency <1 min)
**Traceability:** → SDD-001 §3.6 (Model Manager) → TEST-HD-021 → RISK-HD-103, RISK-HD-104, RISK-HD-106, RISK-HD-204 → IFU-001 §Model Management → PMS-001 §Model Performance

---

### REQ-HD-008: Role-Based Access Control (RBAC)
**Priority:** CRITICAL (security + regulatory)
**Description:** Implement **granular RBAC** with four primary roles to ensure principle of least privilege and compliance with LGPD/GDPR/HIPAA
**Roles and Permissions:**

| Role | Permissions | MFA Required | Examples |
|------|-------------|--------------|----------|
| **Admin** | Full system access: user management, configuration changes, model deployment, audit log access | ✅ YES (mandatory) | IT administrators, QA managers |
| **Laboratory Operator** | Submit CBC data, view analysis results, override recommendations (with justification), export reports | ❌ NO (optional) | Laboratory technicians |
| **Physician** | View analysis results, override recommendations (with justification), access patient history, export reports | ✅ YES (recommended) | Hematologists, physicians |
| **Auditor** | Read-only access to audit logs, export audit data, generate compliance reports | ✅ YES (mandatory) | QA auditors, regulatory affairs |

**Additional Features:**
- **Permission Matrix:** Detailed matrix documenting all API endpoints and required roles (maintained in SDD-001 §6.2)
- **Session Management:** Session timeout after 30 min inactivity (configurable per institution)
- **Login Monitoring:** Log all authentication attempts (success/failure) with IP address, timestamp
- **MFA Support:** TOTP (Google Authenticator, Authy) or SMS-based MFA
- **Password Policy:** Minimum 12 characters, complexity requirements, rotation every 90 days (configurable)
- **Privileged Action Logging:** All Admin actions logged with dual verification (two-person rule for critical changes)
**Acceptance Criteria:**
- No user can access functionality outside their role
- MFA enforced for Admin and Auditor roles (configurable for Physician)
- Failed authentication attempts rate-limited (max 5 attempts/15 min)
- All authentication events logged in audit trail
- RBAC penetration testing passes with zero unauthorized access findings
**Traceability:** → SDD-001 §6.2 (Access Control) → TEST-HD-015, TEST-HD-022 → RISK-HD-201, RISK-HD-202, RISK-HD-205 → IFU-001 §Security → PMS-001 §Security Incidents

---

### REQ-HD-009: Data Retention and Archival
**Priority:** HIGH (regulatory compliance)
**Description:** Implement **automated data lifecycle management** compliant with LGPD (Brazil), GDPR (EU), HIPAA (US), and ANVISA regulations
**Retention Policies:**
- **Audit Logs:** Retain for **5 years minimum** (LGPD Art. 16, ANVISA RDC 657/2022)
- **CBC Data + Results:** Retain for **5 years minimum** (medical record retention requirement)
- **PHI (Personal Health Information):** Retain only as long as clinically necessary + legal retention period
- **Model Artifacts:** Retain all deployed models for **10 years** (traceability for retrospective analysis)
**Archival Strategy:**
- **Hot Storage (0-1 year):** PostgreSQL + S3 Standard (fast retrieval)
- **Warm Storage (1-3 years):** S3 Infrequent Access (retrieval within minutes)
- **Cold Storage (3-5 years):** S3 Glacier (retrieval within hours)
- **Deletion:** Automated deletion after retention period expires (with 30-day grace period + approval)
**Data Subject Rights (LGPD Art. 18):**
- **Right to Access:** Patient can request copy of their data (fulfilled within 15 days)
- **Right to Deletion:** Patient can request deletion (fulfilled within 30 days, except where legal retention required)
- **Right to Portability:** Data exportable in machine-readable format (JSON, CSV)
- **Right to Correction:** Patient can request correction of inaccurate data
**Acceptance Criteria:**
- Audit logs retained for 5 years minimum, accessible within SLA (hot: <1s, warm: <1 min, cold: <24 hours)
- Automated archival moves data to warm storage after 1 year (verified monthly)
- Data deletion requests processed within 30 days (with audit trail)
- Deletion verification: deleted data unrecoverable (cryptographic erasure or physical deletion)
- Annual compliance audit passes with zero retention policy violations
**Traceability:** → SDD-001 §3.9 (Audit Service), §9 (Data Management) → TEST-HD-023 → RISK-HD-103 → NFR-004 (Privacy) → IFU-001 §Data Management → PMS-001 §Compliance

---

### REQ-HD-010: Clinical Rules Specification and Maintenance
**Priority:** HIGH (clinical safety)
**Description:** Maintain **clinical decision rules** in version-controlled, testable, auditable format with mandatory expert review to ensure clinical safety and regulatory compliance
**Rules Management:**
- **Specification Format:** Clinical rules defined in structured YAML or JSON format (human-readable, machine-parseable)
- **Version Control:** All rules stored in Git repository with commit history, branch protection (require review before merge)
- **Clinical Review:** All rule changes reviewed and approved by licensed hematologist (documented in Git commit message)
- **Annual Review:** Complete rule set reviewed annually by clinical advisory board (documented in QMS)
**Rule Categories:**
- **Anemia Detection Rules:** Hb thresholds, MCV-based classification (microcytic/normocytic/macrocytic)
- **Leukemia Screening Rules:** Blast cell detection, WBC differential abnormalities
- **Hemolysis Detection Rules:** LDH elevation, reticulocyte count, haptoglobin
- **Alert Prioritization Rules:** Map clinical findings to alert levels (CRITICAL/HIGH/MEDIUM/LOW)
**Testing Strategy:**
- **Unit Tests:** Each rule testable independently (100% rule coverage)
- **Regression Tests:** Test suite with 100+ clinical scenarios (updated quarterly)
- **Clinical Validation:** New rules validated on retrospective dataset (minimum 1000 cases) before production deployment
**Rule Traceability:**
- Each rule maps to:
  - Evidence source (guideline, literature reference)
  - Risk control (RMP-001 risk ID)
  - Test case (TEST-HD-xxx)
**Acceptance Criteria:**
- 100% clinical rules in version control with hematologist approval
- All rules have unit tests (pass rate 100%)
- Annual clinical review documented in QMS (with approval signatures)
- Rule deployment requires dual approval (Hematologist + QA Manager)
- All rule changes logged in audit trail
**Traceability:** → SDD-001 §3.4 (Rules Engine) → TEST-HD-024 → RISK-HD-004, RISK-HD-401 → IFU-001 §Clinical Rules → PMS-001 §Clinical Performance

---

### REQ-HD-011: Multi-Language Support
**Priority:** MEDIUM
**Description:** Support **internationalization (i18n)** for three languages (Brazilian Portuguese, US English, Spanish) to enable deployment in LATAM and US markets
**Supported Languages:**
- **pt-BR:** Brazilian Portuguese (primary, default)
- **en-US:** US English (required for FDA submission)
- **es-ES:** European Spanish (LATAM market expansion)
**Localized Elements:**
- **UI Text:** All user interface strings (buttons, labels, messages)
- **Clinical Terminology:** Disease names, recommendations (source: SNOMED CT translations)
- **Documentation:** IFU (Instructions for Use) translated and reviewed by clinical SME per language
- **Alert Messages:** CRITICAL/HIGH/MEDIUM/LOW alerts in user's selected language
**Not Localized:**
- **Audit Logs:** Always in English (for regulatory consistency)
- **API Payloads:** Always in English (for integration consistency)
**Implementation:**
- **i18n Framework:** React-i18next or equivalent
- **Translation Quality:** All clinical translations reviewed by native-speaking hematologist
- **Fallback:** If translation missing, display English with warning log (no system failure)
**Acceptance Criteria:**
- 100% UI strings translatable (no hard-coded text)
- Clinical terminology translations validated by hematologist per language
- User can switch language dynamically (session preference + per-user default)
- IFU available in all three languages (regulatory approval per region)
**Traceability:** → SDD-001 §3.8 (UI Service) → TEST-HD-025 → IFU-001 (multi-language versions) → PMS-001 §International Deployment

---

### REQ-HD-012: Performance Monitoring and Degradation Alerts
**Priority:** HIGH
**Description:** Implement **comprehensive observability** with real-time performance monitoring, anomaly detection, and automated alerting to ensure SLA compliance (99.5% uptime, P95 latency <2s)
**Monitored Metrics:**
- **Latency:** P50, P95, P99 per API endpoint (alert if P95 >2s)
- **Throughput:** Requests/second, cases/hour (alert if <80% of baseline)
- **Error Rate:** 4xx/5xx errors per endpoint (alert if >1% error rate)
- **Availability:** Service uptime (alert if <99.5% over 24-hour window)
- **Resource Utilization:** CPU, memory, disk I/O per container (alert if >80% sustained)
- **Model Performance:** Real-time sensitivity/specificity (alert if drift >5% from baseline)
- **Database Performance:** Query latency, connection pool saturation (alert if degraded)
**Alerting Strategy:**
- **Severity Levels:** CRITICAL (immediate page), HIGH (Slack notification), MEDIUM (email), LOW (dashboard only)
- **Escalation:** CRITICAL alerts not acknowledged within 15 min → escalate to on-call manager
- **Alert Correlation:** Group related alerts (e.g., high latency + high CPU) to reduce noise
- **Runbooks:** Each alert type has documented runbook (diagnosis steps, remediation)
**Observability Stack:**
- **Metrics:** Prometheus + Grafana dashboards
- **Logging:** ELK stack (Elasticsearch, Logstash, Kibana) or Splunk
- **Tracing:** OpenTelemetry for distributed tracing
- **APM (Application Performance Monitoring):** Datadog, New Relic, or equivalent
**Acceptance Criteria:**
- All critical metrics monitored with <1 min lag
- CRITICAL alerts trigger within 1 min of threshold breach
- 100% CRITICAL alerts have documented runbooks
- Monthly performance review identifies trends (capacity planning)
- SLA compliance (99.5% uptime) measured and reported monthly
**Traceability:** → SDD-001 §8 (Performance Design), §10 (Observability) → TEST-HD-026 → NFR-001, NFR-002 → IFU-001 §System Requirements → PMS-001 §SLAs

---

### REQ-HD-013: Integration with External Terminology Servers
**Priority:** MEDIUM
**Description:** Enable **integration with external medical terminology servers** (SNOMED CT, LOINC, ICD-10) for standardized coding, terminology validation, and clinical interoperability
**Supported Terminologies:**
- **SNOMED CT:** Clinical findings, diseases (e.g., "Iron deficiency anemia" → SNOMED 87522002)
- **LOINC:** Laboratory tests (e.g., "Hemoglobin [Mass/volume] in Blood" → LOINC 718-7)
- **ICD-10:** Diagnosis codes for billing and reporting (e.g., "D50.9 Iron deficiency anemia, unspecified")
- **ATC (Anatomical Therapeutic Chemical):** Medication codes (future enhancement)
**Integration Features:**
- **Terminology Lookup:** Query terminology server for code validation (e.g., verify LOINC code valid)
- **Code Mapping:** Map internal disease names to standard codes (e.g., "Anemia ferropriva" → SNOMED 87522002)
- **Concept Expansion:** Expand diagnosis to include related concepts (e.g., "Anemia" → all anemia subtypes)
- **Multi-Lingual Support:** Retrieve terminology in user's language (pt-BR, en-US, es-ES)
**Terminology Server Options:**
- **Internal:** Deploy terminology server (e.g., Ontoserver, HAPI FHIR Terminology Service)
- **External:** Integrate with institutional terminology server (if available)
- **Fallback:** Embedded terminology database (updated quarterly) if external server unavailable
**Acceptance Criteria:**
- All CBC parameters mapped to LOINC codes (100% coverage for core 15 parameters)
- All hematological diagnoses mapped to SNOMED CT codes (100% coverage for top 50 diagnoses)
- Terminology lookup latency <500ms (P95)
- Fallback to embedded terminology if external server unavailable (graceful degradation)
- Quarterly terminology database updates documented and validated
**Traceability:** → SDD-001 §3.3 (Validation Service) → TEST-HD-027 → REQ-HD-002 → IFU-001 §Interoperability → PMS-001 §Integration

---

### REQ-HD-014: Batch Processing Mode
**Priority:** LOW
**Description:** Support **batch processing** of historical CBC data for retrospective clinical research, quality improvement studies, and regulatory post-market surveillance
**Use Cases:**
- **Retrospective Analysis:** Analyze 10,000+ historical CBC cases to identify trends (e.g., seasonal anemia prevalence)
- **Model Retraining:** Process historical data to retrain ML models (with proper train/test split)
- **Quality Audits:** Re-analyze cases to validate alert accuracy (calibration studies)
- **Regulatory Reporting:** Generate aggregate statistics for ANVISA post-market surveillance reports
**Functionality:**
- **Batch Ingestion:** Upload CSV/Parquet file with multiple CBC cases (up to 100,000 cases per batch)
- **Asynchronous Processing:** Process batches asynchronously (queue-based, no real-time constraint)
- **Progress Tracking:** Web UI shows batch processing status (queued/processing/completed/failed)
- **Batch Results:** Export batch results as CSV/JSON (includes all predictions, alerts, rationale)
- **De-Identification:** Optional de-identification mode (remove PHI, keep only clinical data + aggregated statistics)
**Performance Requirements:**
- **Throughput:** Process 10,000 cases/hour (lower priority than real-time processing)
- **Resource Isolation:** Batch processing uses separate resource pool (no impact on real-time latency)
**Acceptance Criteria:**
- Batch mode processes 10,000 cases/hour (validated with load testing)
- Batch processing does not degrade real-time P95 latency (isolation verified)
- Batch results match real-time results for same input data (100% consistency)
- De-identification mode removes all 18 HIPAA identifiers (validated with PII detection tools)
**Traceability:** → SDD-001 §3.2 (Ingestion Service - batch mode) → TEST-HD-028 → IFU-001 §Batch Processing → PMS-001 §Research Use

---

### REQ-HD-015: Export to HL7 FHIR R4 Format
**Priority:** MEDIUM
**Description:** Enable **export of CBC analysis results** in HL7 FHIR R4 format for seamless integration with Electronic Health Record (EHR) systems and healthcare data exchanges
**FHIR Resources:**
- **DiagnosticReport:** CBC analysis summary (status, issued date, performer, results)
- **Observation:** Individual CBC parameters (Hb, MCV, WBC, etc.) as FHIR Observations with LOINC codes
- **RiskAssessment:** HemoDoctor risk score and differential diagnosis probabilities
- **Provenance:** Audit trail (who, when, what algorithm version)
**FHIR Profiles:**
- **US Core:** Compliance with US Core IG (Implementation Guide) for DiagnosticReport, Observation
- **Brazilian RNDS (Rede Nacional de Dados em Saúde):** Compliance with Brazilian national health data network profiles (if applicable)
**Export Modes:**
- **REST API:** `GET /api/v1/fhir/DiagnosticReport/{case_id}` returns FHIR JSON
- **Bulk Export:** `GET /api/v1/fhir/export?start_date=X&end_date=Y` returns NDJSON (newline-delimited JSON) for bulk export
- **Push Notification:** Optional webhook to send FHIR bundle to EHR when analysis completes
**FHIR Validation:**
- All exported FHIR resources validated against FHIR R4 schema (using HAPI FHIR Validator or equivalent)
- Validation errors logged and reported (no export if validation fails)
**Acceptance Criteria:**
- 100% CBC results exportable as valid FHIR R4 DiagnosticReport
- All CBC parameters mapped to LOINC codes in FHIR Observations
- FHIR export includes Provenance resource (algorithm version, timestamp, user ID)
- FHIR validation passes with zero errors (warnings acceptable, documented)
- Bulk export supports up to 10,000 reports per request (with pagination)
**Traceability:** → SDD-001 §3.1 (API Gateway - FHIR endpoints) → TEST-HD-029 → REQ-HD-005 → IFU-001 §FHIR Export → PMS-001 §Interoperability

---

## 4. Non-functional Requirements

### NFR-001: Performance
- **Latency:** P95 ≤ 2s per CBC case analysis (real-time)
- **Throughput:** Support 1000 cases/hour per instance (real-time), 10,000 cases/hour (batch mode)
- **Scalability:** Horizontal scaling support (containerized deployment, Kubernetes HPA)
- **Batch Processing:** Process 10,000 historical cases/hour without impacting real-time latency

### NFR-002: Reliability
- **Uptime:** ≥99.5% availability (SLA)
- **Automated Regression Testing:** 100% critical paths covered
- **Failover:** Graceful degradation if ML model unavailable (fallback to rule-based)
- **Disaster Recovery:** RPO (Recovery Point Objective) ≤1 hour, RTO (Recovery Time Objective) ≤4 hours

### NFR-003: Security & Cybersecurity (REQ-HD-060)
**Priority:** CRITICAL
**Description:** Implement secure architecture with RBAC, SBOM, VEX, and hardening per industry best practices.

**Detailed Requirements:** See **SEC-001 Cybersecurity Documentation** for:
- Threat modeling (STRIDE methodology)
- Vulnerability management processes
- Software Bill of Materials (SBOM)
- Vulnerability Exploitability eXchange (VEX)
- Security hardening procedures
- Penetration testing results

**Security Controls:**
- **IAM:** Role-Based Access Control (RBAC) with 4 roles (Admin, Lab Operator, Physician, Auditor)
- **MFA:** Multi-Factor Authentication mandatory for Admin and Auditor roles
- **Encryption:** TLS 1.3 for data in transit, AES-256 for data at rest
- **SBOM:** Software Bill of Materials (CycloneDX/SPDX format)
- **SAST/DAST:** Static and Dynamic Application Security Testing in CI/CD
- **Threat Model:** STRIDE-based threat analysis documented
- **Compliance:** FDA §524B Cybersecurity requirements, ISO/IEC 27001 baselines
- **Vulnerability Management:** CVD (Coordinated Vulnerability Disclosure), VEX (Vulnerability Exploitability eXchange)
- **Secure Updates:** Signed updates with rollback capability
- **Penetration Testing:** Annual third-party penetration testing

**Regulatory Compliance:** FDA §524B, ANVISA RDC 751/2022 cyber requirements
**Traceability:** → SEC-001 §All → RISK-HD-CYB-001 to RISK-HD-CYB-010 → TST-SEC-001 to TST-SEC-005

### NFR-004: Privacy
- **Data Minimization:** Collect only clinically necessary data
- **Pseudonymization:** De-identify PHI in logs and exports
- **Retention & Disposal:** Automated data lifecycle management (5-year retention, secure deletion)
- **Compliance:** LGPD (Brazil) / GDPR (EU) / HIPAA (US)
- **Data Subject Rights:** Support patient access, deletion, portability, correction requests (LGPD Art. 18)

### NFR-005: Usability
- **IEC 62366-1 Compliance:** Usability engineering process documented (separate HFE report)
- **Critical Task Success Rate:** 100% (validated with usability testing)
- **Accessibility:** WCAG 2.1 Level AA compliance
- **Multi-Language Support:** UI available in pt-BR, en-US, es-ES
- **Training Materials:** Comprehensive user training (IFU-001, video tutorials, in-app help)

### NFR-006: Maintainability
- **Code Quality:** SonarQube quality gate pass (0 critical bugs, code coverage ≥80%)
- **Documentation:** All components documented (architecture, API, deployment)
- **Versioning:** Semantic versioning for all releases (MAJOR.MINOR.PATCH)
- **Dependency Management:** Automated dependency updates (Dependabot, Renovate)
- **Technical Debt:** Quarterly technical debt review and prioritization

### NFR-007: Regulatory Compliance
- **IEC 62304:** Class C lifecycle compliance (100% traceability)
- **ISO 14971:** Risk management (RMP-001, FMEA, residual risk acceptance)
- **ISO 13485:** Quality Management System
- **ANVISA RDC 657/2022:** Clinical evidence for Class III SaMD
- **ANVISA RDC 751/2022:** SaMD registration requirements
- **FDA Premarket Submission:** 510(k) or PMA (if US market expansion)
- **21 CFR Part 11:** Electronic records and signatures (if FDA submission)

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
- **FHIR R4:** Interoperability with EHR systems (DiagnosticReport, Observation, RiskAssessment)
- **CSV/Parquet:** Bulk import for batch processing
- **Terminology Servers:** SNOMED CT, LOINC, ICD-10 lookups

### 6.2 User Interface
- **Web UI:** For laboratory operators (React-based SPA)
- **Critical Tasks:**
  - Review and approve automated reports
  - Override recommendations with justification
  - Export audit logs
  - Configure alert thresholds (Admin role only)
- **Accessibility:** WCAG 2.1 Level AA compliance
- **Usability Testing:** IEC 62366-1 conformity (documented in separate HFE report)
- **Multi-Language:** pt-BR, en-US, es-ES

### 6.3 Observability
- **Metrics:** Prometheus-compatible endpoints (latency, throughput, error rates)
- **Logging:** Structured JSON logs (ELK/Splunk compatible)
- **Tracing:** Distributed tracing (OpenTelemetry)
- **Audit Trail:** Separate immutable audit database (append-only)
- **Performance Dashboards:** Grafana dashboards for real-time monitoring

---

## 7. Safety & Risk Controls (ISO 14971 Linkage)

### Risk Mitigation Strategies:
- **False Negative/Positive Thresholds:** Configurable sensitivity/specificity tradeoffs (REQ-HD-006)
- **Alert Throttling:** Prevent alert fatigue (max 3 critical alerts per session) (REQ-HD-006)
- **Training & HFE:** Mandatory user training + Human Factors Engineering validation
- **Failover:** Rule-based fallback if ML model fails (REQ-HD-007)
- **Manual Override:** Clinician can always override with audit trail (REQ-HD-003)
- **RBAC:** Role-based access control prevents unauthorized actions (REQ-HD-008)
- **Data Retention:** Compliance with LGPD/ANVISA retention requirements (REQ-HD-009)

### Link to Risk Management:
- **RISK-HD-001:** False negative severe anemia → Mitigation: High sensitivity (≥90%), REQ-HD-001
- **RISK-HD-002:** False positive severe anemia → Mitigation: Configurable thresholds, REQ-HD-006
- **RISK-HD-003:** Missed leukemia indicators → Mitigation: WBC differential rules, REQ-HD-010
- **RISK-HD-004:** Incorrect differential diagnosis → Mitigation: Clinical rules versioning, REQ-HD-010
- **RISK-HD-005:** Alert fatigue → Mitigation: Alert throttling, REQ-HD-006
- **RISK-HD-008:** Automation bias → Mitigation: Mandatory rationale display, REQ-HD-003
- **RISK-HD-101:** Data parsing error → Mitigation: Unit validation, REQ-HD-002
- **RISK-HD-103:** Database corruption → Mitigation: WORM audit logs, REQ-HD-004
- **RISK-HD-104:** API interface failure → Mitigation: Retry logic, REQ-HD-005
- **RISK-HD-106:** Algorithm version mismatch → Mitigation: Model versioning, REQ-HD-007
- **RISK-HD-201:** Unauthorized access → Mitigation: RBAC + MFA, REQ-HD-008
- **RISK-HD-202:** Malicious data injection → Mitigation: Input validation, REQ-HD-002
- **RISK-HD-204:** Model poisoning → Mitigation: Model validation, REQ-HD-007
- **RISK-HD-401:** User misinterprets recommendation → Mitigation: Usability testing + training, REQ-HD-003

Detailed risk analysis in **RMP-001** (Risk Management Plan).

---

## 8. Cybersecurity (FDA §524B Compliance)

### Cybersecurity Controls:
- **CVD (Coordinated Vulnerability Disclosure):** Public security.txt + bug bounty
- **SBOM:** CycloneDX/SPDX format, updated per release
- **VEX (Vulnerability Exploitability eXchange):** Communicate patch status for known CVEs
- **Secure Update/Rollback:** Signed firmware/software updates with atomic rollback (REQ-HD-007)
- **Logging:** Security event logging (failed auth, privilege escalation attempts)
- **RBAC:** Least privilege access control (REQ-HD-008)
- **Crypto Baselines:** NIST FIPS 140-2 compliant cryptographic modules
- **Penetration Testing:** Annual third-party pentesting

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

### Test Coverage (v1.1):
- **REQ-HD-001 to HD-005:** TEST-HD-011 to HD-019 (existing)
- **REQ-HD-006:** TEST-HD-020 (alert configuration testing)
- **REQ-HD-007:** TEST-HD-021 (model versioning and rollback testing)
- **REQ-HD-008:** TEST-HD-015, TEST-HD-022 (RBAC penetration testing)
- **REQ-HD-009:** TEST-HD-023 (data retention and deletion testing)
- **REQ-HD-010:** TEST-HD-024 (clinical rules unit testing)
- **REQ-HD-011:** TEST-HD-025 (multi-language UI testing)
- **REQ-HD-012:** TEST-HD-026 (performance monitoring and alerting)
- **REQ-HD-013:** TEST-HD-027 (terminology server integration)
- **REQ-HD-014:** TEST-HD-028 (batch processing performance)
- **REQ-HD-015:** TEST-HD-029 (FHIR R4 validation)

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

Example (REQ-HD-007 - NEW):
```
REQ-HD-007 (ML Model Versioning and Rollback)
  → SDD-001 §3.6 (Model Manager design)
  → TEST-HD-021 (Rollback testing, A/B testing, drift detection)
  → RISK-HD-103, RISK-HD-104, RISK-HD-106, RISK-HD-204 (Model-related risks)
  → IFU-001 §Model Management (Model lifecycle documentation)
  → PMS-001 §Model Performance (Real-world drift monitoring)
```

Full traceability documented in **TRC-001_Traceability_Matrix_v1.1.csv** (28 requirements mapped, 100% coverage).

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
| Privacy | LGPD (Brazil), GDPR (EU), HIPAA (US) | Full |
| Security | ISO/IEC 27001:2022, OWASP ASVS | Baselines |
| Interoperability | HL7 FHIR R4 | US Core IG |

---

## 12. Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v0.0 | 2025-09-16 | HemoDoctor Agent | Initial draft with Class C declaration |
| v1.0 | 2025-09-19 | HemoDoctor Agent | Added detailed CBC requirements (REQ-HD-001 to 005) |
| v1.0 (MERGED) | 2025-10-07 | Abel Costa | Merged v0.0 + v1.0, added traceability, cybersecurity |
| **v1.1 (EXPANDED)** | **2025-10-08** | **@spec-writer** | **Added 10 new functional requirements (REQ-HD-006 to 015):** Alert system configuration, ML model versioning, RBAC, data retention, clinical rules management, multi-language support, performance monitoring, terminology integration, batch processing, FHIR export. Expanded NFRs (disaster recovery, penetration testing, data subject rights). Updated traceability to 28 requirements. |

---

## 13. Summary of v1.1 Additions

### New Functional Requirements (10):
1. **REQ-HD-006:** Alert System Configuration - Configurable thresholds, throttling, prioritization per institution
2. **REQ-HD-007:** ML Model Versioning and Rollback - Model lifecycle, A/B testing, emergency rollback <15 min
3. **REQ-HD-008:** Role-Based Access Control (RBAC) - 4 roles (Admin, Lab Operator, Physician, Auditor) with MFA
4. **REQ-HD-009:** Data Retention and Archival - 5-year retention, automated lifecycle, LGPD compliance
5. **REQ-HD-010:** Clinical Rules Specification and Maintenance - Version-controlled rules, annual expert review
6. **REQ-HD-011:** Multi-Language Support - pt-BR, en-US, es-ES for UI and documentation
7. **REQ-HD-012:** Performance Monitoring and Degradation Alerts - Real-time observability, SLA compliance
8. **REQ-HD-013:** Integration with External Terminology Servers - SNOMED CT, LOINC, ICD-10 lookups
9. **REQ-HD-014:** Batch Processing Mode - 10,000 cases/hour for retrospective analysis
10. **REQ-HD-015:** Export to HL7 FHIR R4 - DiagnosticReport, Observation, RiskAssessment resources

### Expanded Non-Functional Requirements:
- **NFR-002:** Added disaster recovery (RPO ≤1 hour, RTO ≤4 hours)
- **NFR-003:** Added penetration testing requirement (annual)
- **NFR-004:** Added data subject rights support (LGPD Art. 18)
- **NFR-005:** Added multi-language support
- **NFR-006:** New maintainability requirements
- **NFR-007:** Comprehensive regulatory compliance matrix

### Traceability Updates:
- Increased from 18 to **28 requirements** (100% coverage maintained)
- All new requirements traced to:
  - Design elements (SDD-001 sections)
  - Test cases (TEST-HD-020 to HD-029)
  - Risk controls (RMP-001 risk IDs)
  - IFU sections
  - PMS monitoring

---

**Next Steps:**
1. Review v1.1 with @software-architecture-specialist (verify SDD-001 design coverage)
2. Update TRC-001 v1.1 (add new requirements to traceability matrix)
3. Create new test cases (TEST-HD-020 to TEST-HD-029) in TST-001
4. Update RMP-001 if new risks identified (preliminary: all risks already covered)
5. Update IFU-001 with new features (alert configuration, model management, FHIR export, etc.)
6. Approval by regulatory team

---

**END OF DOCUMENT**
