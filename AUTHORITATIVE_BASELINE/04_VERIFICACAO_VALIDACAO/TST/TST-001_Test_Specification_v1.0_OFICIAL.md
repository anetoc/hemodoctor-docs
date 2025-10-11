# TST-001 — Test Specification Document

**Código:** TST-001
**Versão:** v1.0
**Data:** 2025-10-08
**Autor(es):** @qa-specialist | Abel Costa
**Revisores:** {REVISORES}
**Aprovadores:** {APROVADORES}
**Status:** Under Review
**Confidencialidade:** Interno/Confidencial

---

## 1. Introduction

### 1.1 Scope
This Test Specification Document defines comprehensive test cases for **HemoDoctor SaMD Class C**, focusing on the 10 new functional requirements added in SRS-001 v1.1 (REQ-HD-006 to REQ-HD-015). These test cases ensure verification and validation compliance with IEC 62304 Class C requirements and ANVISA RDC 657/751 regulations.

### 1.2 Purpose
- Define detailed test cases for systematic verification of new requirements
- Establish pass/fail criteria for ANVISA submission readiness
- Enable regression testing after software updates
- Provide evidence for regulatory audits

### 1.3 Test Levels
Per IEC 62304 §5.5-5.8, testing is organized in four levels:

| Test Level | Scope | Coverage Target |
|------------|-------|-----------------|
| **Unit Testing** | Individual functions, clinical rules | 100% for Class C components |
| **Integration Testing** | API endpoints, service interactions | 100% for critical paths |
| **System Testing** | End-to-end clinical scenarios | 100% for functional requirements |
| **UAT (User Acceptance Testing)** | Real-world usability, clinical validation | 100% for critical tasks (IEC 62366-1) |

---

## 2. Test Strategy

### 2.1 IEC 62304 Compliance
- **§5.5 Software Unit Testing:** All Class C units have documented test cases
- **§5.6 Software Integration Testing:** All interfaces verified with integration tests
- **§5.7 Software System Testing:** All functional requirements verified with system tests
- **§5.8 Software Release Testing:** Pre-release regression testing of all CRITICAL/HIGH test cases

### 2.2 Test Coverage Targets
- **Class C Components:** 100% requirement coverage (all 28 requirements in SRS-001 v1.1)
- **Code Coverage:** Minimum 80% (target: 90% for Class C modules)
- **Critical Paths:** 100% coverage (e.g., anemia detection, alert generation)

### 2.3 Test Environments

| Environment | Purpose | Configuration |
|-------------|---------|---------------|
| **Development** | Developer unit/integration tests | Docker Compose, synthetic data |
| **Staging** | Pre-release system testing | Production-like AWS/Azure, anonymized real data |
| **Production-like** | Final validation, performance testing | Identical to production (hardware, network, load) |
| **UAT** | Clinical validation with end users | Staging environment + real clinicians |

### 2.4 Test Data Management
- **Synthetic Data:** Generated test datasets (unit/integration tests)
- **Anonymized Real Data:** De-identified historical CBC data (system/UAT tests)
- **Privacy:** All test data complies with LGPD (no PHI in test logs)

---

## 3. Existing Test Cases (Summary)

The following test cases were defined for REQ-HD-001 to REQ-HD-005 (documented in previous V&V activities):

| Test ID | Requirement | Type | Status |
|---------|-------------|------|--------|
| TEST-HD-011 | REQ-HD-001: Critical Anemia Detection | Functional + Performance | Defined |
| TEST-HD-012 | REQ-HD-001: False Negative Rate | Clinical Validation | Defined |
| TEST-HD-013 | REQ-HD-002: CBC Data Validation | Integration | Defined |
| TEST-HD-014 | REQ-HD-002: Unit Conversion | Functional | Defined |
| TEST-HD-015 | REQ-HD-003 + REQ-HD-008: RBAC + Override | Security + Functional | Defined |
| TEST-HD-016 | REQ-HD-003: Rationale Display | Usability | Defined |
| TEST-HD-017 | REQ-HD-003: Clinician Override Logging | Audit | Defined |
| TEST-HD-018 | REQ-HD-004: Audit Trail Integrity | Security + Compliance | Defined |
| TEST-HD-019 | REQ-HD-005: API Integration | Integration + Security | Defined |

**Note:** Detailed specifications for TEST-HD-011 to TEST-HD-019 are documented in separate V&V reports (referenced in TRC-001).

---

## 4. New Test Cases (TEST-HD-020 to TEST-HD-029)

### TEST-HD-020: Alert System Configuration

**REQ Traceability:** REQ-HD-006
**Type:** Functional + Security
**Priority:** HIGH
**IEC 62304 Level:** Integration Testing + System Testing

**Objective:** Verify alert configuration system allows institutional customization while preventing unsafe configurations that could compromise patient safety.

**Preconditions:**
- Admin user logged in with MFA enabled
- Default alert thresholds loaded from configuration database
- Staging environment with test institution profile

**Test Steps:**
1. Navigate to Alert Configuration interface (`/admin/alerts/config`)
2. Verify current CRITICAL alert threshold displayed (default: Hb <7 g/dL for adult males)
3. Attempt to modify CRITICAL alert threshold to unsafe value (Hb <4 g/dL)
4. Submit configuration change
5. Verify system blocks submission with error: "Unsafe threshold requires dual approval"
6. Log in as second Admin user (Clinical SME role)
7. Approve threshold change with clinical justification (e.g., "Institutional protocol for trauma unit")
8. Verify configuration saved with both admin IDs + justification in audit trail
9. Configure alert throttling to max 3 CRITICAL alerts per hour
10. Generate 5 CRITICAL alerts within 10 minutes using test script
11. Verify only 3 alerts delivered to physician dashboard
12. Verify remaining 2 alerts queued (not lost)
13. Wait 60 minutes and verify queued alerts delivered after throttle window expires
14. Configure intelligent suppression: 24-hour window for duplicate alerts (same patient + same condition)
15. Generate duplicate CRITICAL alert for same patient within 1 hour
16. Verify duplicate alert suppressed with log entry: "Alert suppressed (duplicate within 24h window)"
17. Configure escalation rule: CRITICAL alert not acknowledged within 15 min → page on-call physician
18. Generate CRITICAL alert and do not acknowledge
19. Wait 15 minutes and verify escalation notification sent (SMS/pager log)

**Expected Results:**
- Unsafe threshold change (Hb <4 g/dL) BLOCKED without dual approval
- After dual approval, configuration saved with both Admin IDs + justification in audit trail
- Alert throttling enforces max 3 CRITICAL/hour (alerts 4-5 queued, not lost)
- Queued alerts delivered after throttle window (60 min)
- Duplicate alert suppression works (same patient within 24h)
- Escalation rule triggered after 15 min (on-call physician paged)

**Pass/Fail Criteria:**
- **PASS:** All 19 test steps execute as expected, no alerts lost, audit trail complete
- **FAIL:** If unsafe config allowed without dual approval, OR throttling fails, OR alerts lost, OR audit trail incomplete

**Test Data:**
- Test institution profile with default thresholds
- 5 synthetic CBC cases with Hb <7 g/dL (trigger CRITICAL)
- Admin user credentials (2 accounts: Admin + Clinical SME)

**Risks Mitigated:**
- RISK-HD-002: False positive severe anemia
- RISK-HD-005: Alert fatigue
- RISK-HD-008: Automation bias

**Traceability:**
- → SDD-001 §3.7 Alert Orchestrator
- → RMP-001 RISK-HD-002, RISK-HD-005, RISK-HD-008
- → IFU-001 §Configuration
- → PMS-001 §Alert Metrics

---

### TEST-HD-021: ML Model Versioning and Rollback

**REQ Traceability:** REQ-HD-007
**Type:** Functional + Performance + Security
**Priority:** CRITICAL
**IEC 62304 Level:** System Testing

**Objective:** Verify robust ML model lifecycle management including versioning, A/B testing, performance monitoring, and emergency rollback capability to ensure model quality and patient safety.

**Preconditions:**
- Two model versions deployed in staging:
  - `model_v1.2.0` (current production, ROC-AUC 0.87)
  - `model_v1.3.0` (candidate, ROC-AUC 0.89 on validation set)
- Model Registry (MLflow) running with both models registered
- Monitoring dashboard configured (Prometheus + Grafana)
- Admin user with Model Manager role logged in

**Test Steps:**
1. **Model Versioning:**
   - Submit 10 CBC cases for analysis
   - Retrieve results via API and verify each response includes `model_version` field (e.g., `"model_version": "v1.2.0_a3f2b1c"`)
   - Query audit log and verify all 10 predictions logged with model version + Git SHA

2. **A/B Testing Setup:**
   - Navigate to Model Manager interface (`/admin/models`)
   - Configure A/B test: 90% traffic to `model_v1.2.0`, 10% traffic to `model_v1.3.0`
   - Submit configuration and verify A/B split enabled

3. **A/B Testing Execution:**
   - Submit 100 CBC cases via API
   - Verify ~90 cases processed by `model_v1.2.0` (tolerance: 85-95)
   - Verify ~10 cases processed by `model_v1.3.0` (tolerance: 5-15)
   - Verify all cases have correct `model_version` in response

4. **Performance Monitoring:**
   - View Model Performance Dashboard (`/admin/models/dashboard`)
   - Verify real-time metrics displayed for both models:
     - Sensitivity, Specificity, ROC-AUC
     - Prediction latency (P95)
     - Drift score (KL divergence from training distribution)
   - Verify dashboard updates within 1 min of new predictions

5. **Automated Degradation Alert:**
   - Simulate model performance degradation: inject 50 cases with known ground truth where `model_v1.3.0` has 80% sensitivity (5% below baseline 85%)
   - Wait 5 minutes
   - Verify HIGH alert generated: "Model v1.3.0 performance degraded: Sensitivity 80% (<85% threshold)"
   - Verify alert delivered to Model Manager and Clinical SME (Slack/email)

6. **Emergency Rollback:**
   - Acknowledge degradation alert
   - Initiate emergency rollback to `model_v1.2.0` via Model Manager interface (single-click "Rollback" button)
   - Monitor rollback process:
     - Verify service downtime <15 min (measured from rollback initiation to first successful prediction)
     - Verify all traffic routed to `model_v1.2.0` after rollback
   - Submit 10 test cases and verify all processed by `model_v1.2.0`

7. **Rollback Audit:**
   - Query audit log for rollback event
   - Verify log entry includes:
     - Admin user ID who initiated rollback
     - Timestamp (ISO 8601 format)
     - Previous model version (`v1.3.0`)
     - Current model version (`v1.2.0`)
     - Justification (e.g., "Performance degradation: Sensitivity 80%")

8. **Model Promotion Validation:**
   - Attempt to promote `model_v1.3.0` to production
   - Verify system blocks promotion with error: "Model fails promotion criteria: Sensitivity 80% (<90% required)"
   - Retrain `model_v1.3.0` (simulated: upload new model artifact with 92% sensitivity)
   - Re-attempt promotion
   - Verify dual approval required (Data Scientist + Clinical SME)
   - Approve with both accounts
   - Verify `model_v1.3.0` promoted to production (100% traffic)

**Expected Results:**
- Every prediction logged with model version ID (Git SHA + timestamp)
- A/B testing supports traffic split (90/10 verified with 100 test cases)
- Model performance dashboard updates in real-time (<1 min latency)
- Automated alert triggered when performance degrades >5% (HIGH priority)
- Emergency rollback completes in <15 min (measured downtime: 12 min ± 2 min)
- Rollback audit trail complete (user ID, timestamp, justification)
- Model promotion blocked if criteria not met (sensitivity <90%)
- Dual approval enforced for production promotion

**Pass/Fail Criteria:**
- **PASS:** All 8 test steps execute as expected, rollback downtime <15 min, audit trail complete
- **FAIL:** If rollback downtime >15 min, OR alerts not triggered, OR audit trail incomplete, OR dual approval bypassed

**Test Data:**
- 100 synthetic CBC cases (balanced across anemia severity)
- 50 ground-truth cases with known labels (for degradation simulation)
- Two model artifacts (`v1.2.0`, `v1.3.0`) in MLflow registry

**Risks Mitigated:**
- RISK-HD-103: Database corruption (model registry integrity)
- RISK-HD-104: API interface failure (rollback mechanism)
- RISK-HD-106: Algorithm version mismatch (versioning in audit log)
- RISK-HD-204: Model poisoning (validation before promotion)

**Traceability:**
- → SDD-001 §3.6 Model Manager
- → RMP-001 RISK-HD-103, RISK-HD-104, RISK-HD-106, RISK-HD-204
- → IFU-001 §Model Management
- → PMS-001 §Model Performance

---

### TEST-HD-022: Role-Based Access Control (RBAC) Security Testing

**REQ Traceability:** REQ-HD-008
**Type:** Security + Penetration Testing
**Priority:** CRITICAL
**IEC 62304 Level:** Integration Testing + System Testing

**Objective:** Verify granular RBAC implementation prevents unauthorized access and enforces principle of least privilege across all four roles (Admin, Laboratory Operator, Physician, Auditor).

**Preconditions:**
- Staging environment with RBAC enabled
- Four test user accounts:
  - `admin_user` (Admin role, MFA enabled)
  - `lab_user` (Laboratory Operator role, MFA disabled)
  - `physician_user` (Physician role, MFA enabled)
  - `auditor_user` (Auditor role, MFA enabled)
- Permission matrix documented in SDD-001 §6.2

**Test Steps:**

**1. Admin Role Testing:**
- Log in as `admin_user` with MFA (TOTP code)
- Verify access to all admin endpoints:
  - User management (`GET /admin/users`, `POST /admin/users`)
  - Configuration (`PUT /admin/alerts/config`)
  - Model deployment (`POST /admin/models/deploy`)
  - Audit logs (`GET /admin/audit`)
- Attempt to submit CBC data (`POST /api/v1/cbc/analyze`)
- Verify BLOCKED with error: "Admin role cannot submit clinical data (separation of duties)"
- Log out

**2. Laboratory Operator Role Testing:**
- Log in as `lab_user` (no MFA required, username/password only)
- Verify access to:
  - Submit CBC data (`POST /api/v1/cbc/analyze`) → SUCCESS
  - View analysis results (`GET /api/v1/results/{case_id}`) → SUCCESS
  - Override recommendation with justification → SUCCESS
  - Export reports (`GET /api/v1/reports/{case_id}`) → SUCCESS
- Attempt unauthorized actions:
  - User management (`GET /admin/users`) → BLOCKED (403 Forbidden)
  - Configuration (`PUT /admin/alerts/config`) → BLOCKED (403 Forbidden)
  - Audit logs (`GET /admin/audit`) → BLOCKED (403 Forbidden)
- Log out

**3. Physician Role Testing:**
- Log in as `physician_user` with MFA (SMS code)
- Verify access to:
  - View analysis results (`GET /api/v1/results/{case_id}`) → SUCCESS
  - Override recommendation with justification → SUCCESS
  - Access patient history (`GET /api/v1/history/{patient_id}`) → SUCCESS
  - Export reports → SUCCESS
- Attempt unauthorized actions:
  - Submit CBC data (`POST /api/v1/cbc/analyze`) → BLOCKED (403 Forbidden - operators only)
  - User management → BLOCKED (403 Forbidden)
  - Model deployment → BLOCKED (403 Forbidden)
- Log out

**4. Auditor Role Testing:**
- Log in as `auditor_user` with MFA (TOTP code)
- Verify read-only access:
  - Audit logs (`GET /admin/audit`) → SUCCESS
  - Export audit data (`GET /admin/audit/export?start_date=X&end_date=Y`) → SUCCESS
  - Generate compliance reports (`GET /admin/reports/compliance`) → SUCCESS
- Attempt write actions:
  - Submit CBC data → BLOCKED (403 Forbidden)
  - Modify configuration → BLOCKED (403 Forbidden)
  - Delete audit logs → BLOCKED (403 Forbidden)
- Log out

**5. MFA Enforcement Testing:**
- Attempt to log in as `admin_user` with correct password but NO MFA code
- Verify login BLOCKED with error: "MFA required for Admin role"
- Attempt to log in as `admin_user` with incorrect MFA code (wrong TOTP)
- Verify login BLOCKED with error: "Invalid MFA code"
- After 5 failed MFA attempts within 15 min, verify account locked with error: "Account locked (max attempts exceeded)"
- Verify rate limiting: max 5 login attempts per 15 min per IP address

**6. Session Management Testing:**
- Log in as `physician_user`
- Wait 30 minutes with no activity (idle session)
- Attempt to access protected endpoint (`GET /api/v1/results/123`)
- Verify session expired with error: "Session timeout (30 min inactivity)"
- Require re-authentication

**7. Privileged Action Logging:**
- Log in as `admin_user`
- Perform privileged action: Deploy new ML model (`POST /admin/models/deploy`)
- Verify dual approval required (second Admin must approve)
- Log in as second Admin account (`admin_user_2`)
- Approve model deployment
- Query audit log and verify log entry includes:
  - Primary admin user ID (`admin_user`)
  - Approver user ID (`admin_user_2`)
  - Action: "Model deployment"
  - Timestamp (ISO 8601)
  - Justification (free-text)

**8. Penetration Testing (Basic):**
- **SQL Injection Test:** Attempt to inject SQL in username field: `admin' OR '1'='1`
  - Verify login BLOCKED with error: "Invalid credentials"
- **XSS Test:** Attempt to inject JavaScript in justification field: `<script>alert('XSS')</script>`
  - Verify input sanitized (script tags escaped, not executed)
- **CSRF Test:** Attempt to forge cross-site request to `/admin/users/delete` without CSRF token
  - Verify request BLOCKED with error: "CSRF token invalid"
- **Authorization Bypass Test:** Attempt to access admin endpoint directly with Lab Operator JWT token
  - Verify request BLOCKED with error: "Insufficient permissions"

**Expected Results:**
- No user can access functionality outside their role (100% authorization enforcement)
- MFA enforced for Admin, Auditor, Physician roles (configurable)
- Failed authentication attempts rate-limited (max 5 attempts/15 min)
- Session timeout enforced after 30 min inactivity
- All authentication events logged in audit trail (success + failure + IP address)
- Privileged actions require dual approval (logged with both user IDs)
- Penetration testing passes with zero unauthorized access findings

**Pass/Fail Criteria:**
- **PASS:** All 8 test steps execute as expected, zero unauthorized access, all attacks blocked
- **FAIL:** If any unauthorized access allowed, OR MFA bypassed, OR audit trail incomplete, OR penetration test fails

**Test Data:**
- Four test user accounts with different roles
- Synthetic CBC cases for Lab Operator testing
- Penetration testing payloads (SQL injection, XSS, CSRF)

**Risks Mitigated:**
- RISK-HD-201: Unauthorized access
- RISK-HD-202: Malicious data injection
- RISK-HD-205: Session hijacking

**Traceability:**
- → SDD-001 §6.2 Access Control
- → TEST-HD-015 (previous RBAC testing)
- → RMP-001 RISK-HD-201, RISK-HD-202, RISK-HD-205
- → IFU-001 §Security
- → PMS-001 §Security Incidents

---

### TEST-HD-023: Data Retention and Deletion

**REQ Traceability:** REQ-HD-009
**Type:** Functional + Compliance
**Priority:** HIGH
**IEC 62304 Level:** System Testing

**Objective:** Verify automated data lifecycle management complies with LGPD (Brazil), GDPR (EU), HIPAA (US), and ANVISA regulations, including retention policies, archival strategies, and data subject rights.

**Preconditions:**
- Staging environment with three storage tiers configured:
  - Hot storage: PostgreSQL + S3 Standard (0-1 year)
  - Warm storage: S3 Infrequent Access (1-3 years)
  - Cold storage: S3 Glacier (3-5 years)
- Automated archival cron jobs enabled (run daily)
- Test data with known timestamps:
  - 100 CBC cases from 6 months ago (hot storage)
  - 100 CBC cases from 2 years ago (warm storage)
  - 100 CBC cases from 4 years ago (cold storage)
  - 50 CBC cases from 5 years + 1 day ago (deletion candidates)

**Test Steps:**

**1. Retention Policy Validation:**
- Query database for audit logs from 5 years ago
- Verify logs retained and accessible (LGPD Art. 16 minimum 5 years)
- Query for audit logs from 5 years + 1 day ago
- Verify logs marked for deletion (status: `DELETION_PENDING`)
- Verify 30-day grace period before actual deletion

**2. Automated Archival (Hot → Warm):**
- Query for CBC cases from 13 months ago (should be in warm storage)
- Verify storage class: `S3 Infrequent Access` (check S3 metadata)
- Retrieve one case and measure retrieval time
- Verify retrieval latency <1 min (warm storage SLA)

**3. Automated Archival (Warm → Cold):**
- Query for CBC cases from 3 years + 1 month ago (should be in cold storage)
- Verify storage class: `S3 Glacier` (check S3 metadata)
- Initiate retrieval (Glacier Standard retrieval)
- Verify retrieval latency <24 hours (cold storage SLA)

**4. Data Deletion Request (LGPD Art. 18):**
- Simulate patient deletion request for `patient_id: PAT-12345`
- Submit deletion request via web UI (`/privacy/deletion-request`)
- Verify request logged in audit trail:
  - Patient ID (pseudonymized hash)
  - Request timestamp
  - Requester justification
- Verify deletion task queued (status: `DELETION_QUEUED`)
- Wait 30 days (or simulate time advance in staging)
- Verify deletion executed:
  - CBC data deleted from all storage tiers (hot/warm/cold)
  - Audit logs retained (anonymized: patient ID replaced with `<DELETED>`)
  - Aggregated statistics retained (no individual-level data)
- Attempt to retrieve deleted patient data via API
- Verify response: `404 Not Found - Data deleted per patient request`

**5. Deletion Verification (Cryptographic Erasure):**
- After deletion, verify data unrecoverable:
  - Query database for `patient_id: PAT-12345` → 0 results
  - Check S3 bucket for patient files → 0 results
  - Verify encryption keys rotated (if using customer-managed keys)
- Attempt data recovery using backup restoration
- Verify patient data NOT present in backups after deletion (backup retention policy: 30 days)

**6. Data Access Request (LGPD Art. 18):**
- Simulate patient access request for `patient_id: PAT-67890`
- Submit access request via web UI (`/privacy/access-request`)
- Verify request logged in audit trail
- Verify data export generated within 15 days (SLA):
  - All CBC data (JSON format)
  - All analysis results
  - All audit logs for patient
- Verify export delivered via secure download link (expires after 7 days)

**7. Data Portability (LGPD Art. 18):**
- For same patient `PAT-67890`, request data portability
- Verify export format: machine-readable (JSON, CSV options)
- Verify export includes:
  - CBC parameters with LOINC codes
  - Analysis results with timestamps
  - Metadata (reference ranges, units)
- Verify export does NOT include:
  - Internal system IDs
  - Algorithm internals (proprietary)

**8. Data Correction Request (LGPD Art. 18):**
- Simulate patient correction request: "My birthdate is wrong"
- Submit correction request via web UI
- Verify request routed to Lab Operator for review
- Lab Operator approves correction (with clinical justification)
- Verify correction logged in audit trail:
  - Original value (birthdate: 1990-01-01)
  - Corrected value (birthdate: 1985-05-15)
  - Approver user ID
  - Timestamp
- Verify future analyses use corrected birthdate (affects age-based reference ranges)

**9. Annual Compliance Audit:**
- Run annual compliance audit report (`/admin/reports/compliance`)
- Verify report includes:
  - Total data retention violations: 0
  - Total deletion requests processed: X (within 30 days)
  - Total access requests processed: Y (within 15 days)
  - Storage tier distribution (% in hot/warm/cold)
- Verify report exportable (PDF format)

**Expected Results:**
- Audit logs retained for 5 years minimum (accessible within SLA)
- Automated archival moves data to warm storage after 1 year (verified)
- Automated archival moves data to cold storage after 3 years (verified)
- Data deletion requests processed within 30 days (audit trail complete)
- Deleted data unrecoverable (cryptographic erasure verified)
- Data access requests fulfilled within 15 days (secure download)
- Data portability export in machine-readable format (JSON/CSV)
- Data correction requests logged with approval (audit trail complete)
- Annual compliance audit passes with zero retention policy violations

**Pass/Fail Criteria:**
- **PASS:** All 9 test steps execute as expected, zero compliance violations
- **FAIL:** If data retained beyond policy, OR deletion not executed, OR audit incomplete, OR SLA violated

**Test Data:**
- 300 synthetic CBC cases distributed across storage tiers (hot/warm/cold)
- 50 deletion candidates (5 years + 1 day old)
- Test patient IDs for deletion/access/correction requests

**Risks Mitigated:**
- RISK-HD-103: Database corruption (data retention integrity)

**Traceability:**
- → SDD-001 §3.9 Audit Service, §9 Data Management
- → RMP-001 RISK-HD-103
- → NFR-004 Privacy
- → IFU-001 §Data Management
- → PMS-001 §Compliance

---

### TEST-HD-024: Clinical Rules Unit Testing

**REQ Traceability:** REQ-HD-010
**Type:** Unit Testing + Clinical Validation
**Priority:** HIGH
**IEC 62304 Level:** Unit Testing + System Testing

**Objective:** Verify clinical decision rules are testable, auditable, and clinically validated to ensure patient safety and regulatory compliance.

**Preconditions:**
- Clinical rules defined in YAML format in Git repository (`/rules/hematology_rules.yaml`)
- Rules Engine service deployed in staging
- Hematologist approval documented for all rules (Git commit messages)
- Unit test suite with 100+ clinical scenarios

**Test Steps:**

**1. Rules Specification Format Validation:**
- Clone rules repository: `git clone <rules_repo>`
- Verify all rules in structured YAML format
- Validate YAML syntax (no parsing errors)
- Verify each rule has required fields:
  - `rule_id` (unique identifier, e.g., `RULE-ANEMIA-001`)
  - `name` (human-readable, e.g., "Severe Anemia Detection")
  - `category` (e.g., "Anemia Detection")
  - `condition` (logical expression, e.g., `Hb < 7 AND age >= 18`)
  - `action` (e.g., `GENERATE_ALERT(level='CRITICAL')`)
  - `evidence` (guideline reference, e.g., "WHO 2011 Hemoglobin thresholds")
  - `risk_id` (e.g., `RISK-HD-001`)
- Verify 100% rules have all required fields

**2. Version Control and Review:**
- Check Git commit history for rule changes in past 6 months
- Verify each rule change has:
  - Commit message with hematologist approval (e.g., "Approved by Dr. Silva (CRM 12345)")
  - Code review approval (GitHub pull request with ≥1 approval)
  - No direct commits to main branch (branch protection enforced)
- Attempt to push rule change without approval
- Verify push rejected with error: "Branch protection: review required"

**3. Unit Test Coverage:**
- Run unit test suite: `pytest tests/rules/test_hematology_rules.py`
- Verify 100% rule coverage (each rule has ≥1 unit test)
- Example unit test for `RULE-ANEMIA-001`:
  ```python
  def test_severe_anemia_detection():
      rule = load_rule("RULE-ANEMIA-001")
      cbc = {"Hb": 6.5, "age": 30, "sex": "M"}
      result = rule.evaluate(cbc)
      assert result.triggered == True
      assert result.alert_level == "CRITICAL"
      assert result.recommendation == "Immediate medical evaluation"
  ```
- Verify all tests pass (100% pass rate)

**4. Regression Testing (100+ Scenarios):**
- Run regression test suite: `pytest tests/rules/test_clinical_scenarios.py`
- Verify suite includes:
  - 30+ severe anemia scenarios (various Hb/MCV/age/sex combinations)
  - 20+ leukemia screening scenarios (blast cells, WBC differential)
  - 20+ hemolysis detection scenarios (LDH, reticulocytes, haptoglobin)
  - 30+ alert prioritization scenarios (CRITICAL/HIGH/MEDIUM/LOW mapping)
- Verify all scenarios pass (100% pass rate)
- Generate test coverage report: `pytest --cov=rules`
- Verify coverage ≥95% for rules module

**5. Clinical Validation (Retrospective Dataset):**
- Load retrospective dataset: 1000 anonymized CBC cases with ground truth labels
- Execute rules engine on all 1000 cases
- Calculate performance metrics:
  - Sensitivity for severe anemia detection: ≥90%
  - Specificity for severe anemia detection: ≥85%
  - PPV (Positive Predictive Value): ≥80%
  - NPV (Negative Predictive Value): ≥95%
- Verify all metrics meet thresholds

**6. Rule Traceability Validation:**
- For rule `RULE-ANEMIA-001`, verify traceability:
  - Evidence source: WHO 2011 guideline (reference link valid)
  - Risk control: Maps to `RISK-HD-001` in RMP-001
  - Test case: Maps to `TEST-HD-011` (severe anemia detection)
- Repeat for 10 randomly selected rules
- Verify 100% rules have complete traceability (evidence + risk + test)

**7. Annual Clinical Review:**
- Verify annual review documented in QMS:
  - Review date: 2024-10-01
  - Clinical advisory board members: 3 hematologists (names + credentials)
  - Review outcome: "All rules approved, no changes required"
  - Approval signatures (digital or scanned)
- Verify next review scheduled: 2025-10-01

**8. Rule Deployment Validation:**
- Attempt to deploy new rule `RULE-ANEMIA-007` to production
- Verify dual approval required:
  - Hematologist approval (clinical safety)
  - QA Manager approval (verification testing complete)
- Simulate approval from both roles
- Verify rule deployed to production
- Query audit log for deployment event:
  - Rule ID: `RULE-ANEMIA-007`
  - Deployer user ID
  - Hematologist approver ID
  - QA Manager approver ID
  - Deployment timestamp

**9. Alert Prioritization Rules Testing:**
- Load clinical scenario: Hb 6.0 g/dL + MCV 75 fL + Ferritin 5 ng/mL
- Execute rules engine
- Verify alert prioritization:
  - Triggered rules:
    - `RULE-ANEMIA-001` (Severe anemia) → CRITICAL
    - `RULE-ANEMIA-002` (Microcytic anemia) → HIGH
    - `RULE-IRON-001` (Iron deficiency) → HIGH
  - Final alert level: CRITICAL (highest priority wins)
  - Recommendation: "Immediate transfusion evaluation + iron supplementation"

**Expected Results:**
- 100% clinical rules in version control with hematologist approval
- All rules have unit tests (100% coverage, 100% pass rate)
- Regression test suite passes (100+ scenarios, 100% pass rate)
- Clinical validation on 1000 cases meets performance thresholds (sensitivity ≥90%)
- 100% rules have complete traceability (evidence + risk + test)
- Annual clinical review documented in QMS (with signatures)
- Rule deployment requires dual approval (logged in audit trail)
- Alert prioritization rules work correctly (highest priority wins)

**Pass/Fail Criteria:**
- **PASS:** All 9 test steps execute as expected, 100% rules approved and tested
- **FAIL:** If any rule missing approval, OR unit tests fail, OR clinical validation fails, OR traceability incomplete

**Test Data:**
- Clinical rules repository (YAML files)
- Unit test suite (pytest)
- Regression test suite (100+ scenarios)
- Retrospective dataset (1000 CBC cases with ground truth)

**Risks Mitigated:**
- RISK-HD-004: Incorrect differential diagnosis
- RISK-HD-401: User misinterprets recommendation

**Traceability:**
- → SDD-001 §3.4 Rules Engine
- → RMP-001 RISK-HD-004, RISK-HD-401
- → IFU-001 §Clinical Rules
- → PMS-001 §Clinical Performance

---

### TEST-HD-025: Multi-Language UI Testing

**REQ Traceability:** REQ-HD-011
**Type:** Functional + Usability
**Priority:** MEDIUM
**IEC 62304 Level:** System Testing + UAT

**Objective:** Verify internationalization (i18n) support for three languages (Brazilian Portuguese, US English, Spanish) to enable deployment in LATAM and US markets.

**Preconditions:**
- Staging environment with i18n framework configured (React-i18next)
- Three language files:
  - `pt-BR.json` (Brazilian Portuguese - default)
  - `en-US.json` (US English)
  - `es-ES.json` (European Spanish)
- Clinical terminology translations reviewed by native-speaking hematologists
- IFU (Instructions for Use) translated for all three languages

**Test Steps:**

**1. UI String Translation Coverage:**
- Open web UI in browser
- Set language to `pt-BR` (default)
- Navigate through all screens (Dashboard, CBC Entry, Results, Reports, Admin)
- Verify NO hard-coded English strings visible
- Verify all UI elements in Portuguese:
  - Buttons: "Enviar", "Cancelar", "Exportar"
  - Labels: "Hemoglobina", "Hemácias", "Leucócitos"
  - Messages: "Análise concluída com sucesso"
- Switch language to `en-US`
- Verify all UI elements in English:
  - Buttons: "Submit", "Cancel", "Export"
  - Labels: "Hemoglobin", "Red Blood Cells", "White Blood Cells"
  - Messages: "Analysis completed successfully"
- Switch language to `es-ES`
- Verify all UI elements in Spanish:
  - Buttons: "Enviar", "Cancelar", "Exportar"
  - Labels: "Hemoglobina", "Glóbulos rojos", "Glóbulos blancos"
  - Messages: "Análisis completado exitosamente"

**2. Clinical Terminology Translation:**
- Submit CBC case with severe anemia (Hb 6.0 g/dL)
- View analysis result in `pt-BR`
- Verify diagnosis: "Anemia grave" (SNOMED CT pt-BR translation)
- Switch to `en-US`
- Verify diagnosis: "Severe anemia" (SNOMED CT en-US translation)
- Switch to `es-ES`
- Verify diagnosis: "Anemia grave" (SNOMED CT es-ES translation)
- Verify all clinical terminology translations reviewed by hematologist (check translation approval log)

**3. Alert Message Translation:**
- Generate CRITICAL alert (Hb <7 g/dL)
- View alert in `pt-BR`
- Verify alert message: "CRÍTICO: Anemia grave detectada. Avaliação médica imediata necessária."
- Switch to `en-US`
- Verify alert message: "CRITICAL: Severe anemia detected. Immediate medical evaluation required."
- Switch to `es-ES`
- Verify alert message: "CRÍTICO: Anemia grave detectada. Se requiere evaluación médica inmediata."

**4. Dynamic Language Switching:**
- Log in as `lab_user` with language preference set to `pt-BR`
- Verify UI loads in Portuguese
- Navigate to user preferences (`/profile/settings`)
- Change language preference to `en-US`
- Verify UI updates immediately (no page reload required)
- Verify language preference saved (persist across sessions)
- Log out and log back in
- Verify UI still in English (preference persisted)

**5. IFU Translation Validation:**
- Access IFU (Instructions for Use) from Help menu
- Verify three versions available:
  - `IFU-001_pt-BR.pdf` (Brazilian Portuguese)
  - `IFU-001_en-US.pdf` (US English)
  - `IFU-001_es-ES.pdf` (European Spanish)
- Download `IFU-001_pt-BR.pdf`
- Verify document language: Portuguese
- Verify clinical content reviewed by hematologist (check approval signature on cover page)
- Repeat for `en-US` and `es-ES`

**6. Fallback Mechanism Testing:**
- Manually corrupt one translation string in `en-US.json`:
  - Delete key: `"submit_button": "Submit"`
- Reload UI in English
- Click submit button
- Verify button displays English fallback: "Submit" (from default en-US fallback)
- Verify warning log generated: "Translation missing: submit_button (en-US)"
- Verify system does NOT crash (graceful degradation)

**7. Audit Log Language Consistency:**
- Submit CBC case with UI in Portuguese
- View audit log (`/admin/audit`)
- Verify audit log always in English (regulatory consistency):
  - Log entry: "CBC submitted by user lab_user at 2025-10-08T14:30:00Z"
  - NOT translated: "CBC enviado por usuário lab_user em 2025-10-08T14:30:00Z"

**8. API Payload Language Consistency:**
- Submit CBC via API with `Accept-Language: pt-BR` header
- Verify API response payload in English (integration consistency):
  ```json
  {
    "case_id": "CASE-12345",
    "diagnosis": "Severe anemia",  // NOT translated
    "alert_level": "CRITICAL"       // NOT translated
  }
  ```
- Verify only UI displays translated text (API always English)

**Expected Results:**
- 100% UI strings translatable (no hard-coded text)
- Clinical terminology translations validated by hematologist (all three languages)
- Alert messages translated correctly (CRITICAL/HIGH/MEDIUM/LOW)
- User can switch language dynamically (session preference + per-user default)
- Language preference persists across sessions
- IFU available in all three languages (regulatory approval per region)
- Fallback mechanism works (missing translation → display English + log warning)
- Audit logs always in English (regulatory consistency)
- API payloads always in English (integration consistency)

**Pass/Fail Criteria:**
- **PASS:** All 8 test steps execute as expected, 100% UI strings translated, fallback works
- **FAIL:** If hard-coded strings found, OR clinical translations not approved, OR fallback fails

**Test Data:**
- Three language files (pt-BR, en-US, es-ES)
- Synthetic CBC cases (for testing translations)
- Three IFU versions (PDF documents)

**Risks Mitigated:**
- None directly (usability enhancement)

**Traceability:**
- → SDD-001 §3.8 UI Service
- → IFU-001 (multi-language versions)
- → PMS-001 §International Deployment

---

### TEST-HD-026: Performance Monitoring and Degradation Alerts

**REQ Traceability:** REQ-HD-012
**Type:** Performance + Monitoring
**Priority:** HIGH
**IEC 62304 Level:** System Testing

**Objective:** Verify comprehensive observability with real-time performance monitoring, anomaly detection, and automated alerting to ensure SLA compliance (99.5% uptime, P95 latency <2s).

**Preconditions:**
- Staging environment with observability stack deployed:
  - Metrics: Prometheus + Grafana
  - Logging: ELK stack (Elasticsearch, Logstash, Kibana)
  - Tracing: OpenTelemetry
  - APM: Datadog (or equivalent)
- Monitoring dashboards configured (`/admin/monitoring`)
- Alert rules configured (Prometheus AlertManager)
- On-call rotation configured (PagerDuty or equivalent)

**Test Steps:**

**1. Latency Monitoring:**
- Load test: Submit 1000 CBC cases via API over 10 minutes (100 req/min)
- Monitor API endpoint latency in Grafana dashboard
- Verify metrics displayed:
  - P50 latency: <500ms
  - P95 latency: <2s (SLA threshold)
  - P99 latency: <5s
- Verify dashboard updates in real-time (<1 min lag)

**2. Latency Degradation Alert:**
- Simulate high load: Submit 500 CBC cases simultaneously (stress test)
- Monitor P95 latency
- Verify P95 latency increases to >2s (SLA breach)
- Wait 1 minute
- Verify HIGH alert triggered: "API latency degraded: P95 = 3.2s (>2s threshold)"
- Verify alert delivered via Slack notification
- Verify alert includes runbook link: `/runbooks/high-latency`

**3. Throughput Monitoring:**
- Monitor baseline throughput: 100 cases/hour (expected for low-traffic period)
- Simulate traffic spike: Submit 1000 cases/hour (10x baseline)
- Verify throughput metric increases to 1000 cases/hour in dashboard
- Verify no alerts triggered (throughput increase acceptable)

**4. Throughput Degradation Alert:**
- Simulate service degradation: Stop 2 out of 3 API replicas (Kubernetes pod deletion)
- Monitor throughput
- Verify throughput drops to 30 cases/hour (<80% of baseline 100 cases/hour)
- Wait 1 minute
- Verify CRITICAL alert triggered: "Throughput degraded: 30 cases/hour (<80 cases/hour threshold)"
- Verify alert delivered via PagerDuty page (on-call engineer notified)
- Verify alert includes runbook link: `/runbooks/low-throughput`

**5. Error Rate Monitoring:**
- Submit 100 valid CBC cases
- Verify error rate: 0% (all requests succeed)
- Simulate API errors: Submit 10 invalid CBC cases (missing required fields)
- Verify 10 errors (400 Bad Request) logged in Kibana
- Calculate error rate: 10 / 110 = 9.1%
- Verify CRITICAL alert triggered: "Error rate high: 9.1% (>1% threshold)"
- Verify alert includes sample error logs (Kibana link)

**6. Availability Monitoring:**
- Monitor service uptime over 24-hour window
- Verify uptime: 100% (no downtime)
- Simulate downtime: Stop all API replicas for 10 minutes
- Wait 10 minutes
- Verify CRITICAL alert triggered: "Service down: 0% availability"
- Restart API replicas
- Verify service recovers
- Calculate 24-hour uptime: (24 * 60 - 10) / (24 * 60) = 99.3% (<99.5% SLA)
- Verify availability SLA breach logged in compliance dashboard

**7. Resource Utilization Monitoring:**
- Monitor baseline resource utilization:
  - CPU: 30% (per container)
  - Memory: 50% (per container)
  - Disk I/O: 20 MB/s
- Simulate resource spike: Submit 5000 cases simultaneously
- Monitor resource utilization:
  - CPU: 85% (sustained for 5 minutes)
  - Memory: 75%
  - Disk I/O: 100 MB/s
- Verify HIGH alert triggered: "CPU utilization high: 85% (>80% threshold)"
- Verify alert includes resource usage graph (Grafana link)

**8. Model Performance Monitoring:**
- Monitor baseline model performance (from TEST-HD-021):
  - Sensitivity: 92%
  - Specificity: 88%
  - ROC-AUC: 0.89
- Simulate model drift: Inject 100 cases with distribution shift (e.g., elderly patients only)
- Monitor model performance
- Verify drift score increases (KL divergence >0.1)
- Verify HIGH alert triggered: "Model drift detected: KL divergence 0.12 (>0.1 threshold)"
- Verify alert delivered to Model Manager + Clinical SME

**9. Database Performance Monitoring:**
- Monitor baseline database performance:
  - Query latency P95: <100ms
  - Connection pool: 30% saturated
- Simulate slow query: Execute complex analytics query (joins 5 tables)
- Monitor database latency
- Verify query latency P95 increases to 500ms
- Verify MEDIUM alert triggered: "Database latency degraded: P95 = 500ms (>200ms threshold)"
- Verify alert includes slow query log (PostgreSQL log)

**10. Alert Correlation:**
- Simulate cascading failure: Stop database replica
- Verify multiple related alerts triggered within 1 minute:
  - CRITICAL: "Database unavailable"
  - HIGH: "API latency degraded"
  - HIGH: "Error rate high"
- Verify alerts correlated (grouped under single incident: "Database outage")
- Verify incident runbook displayed: `/runbooks/database-outage`

**11. Escalation Testing:**
- Generate CRITICAL alert: "Service down"
- Wait 15 minutes without acknowledgment
- Verify alert escalated to on-call manager (PagerDuty escalation policy)
- Verify escalation logged in audit trail

**12. Runbook Validation:**
- For each alert type (latency, throughput, error rate, availability, resource, drift, database):
  - Verify runbook exists (documented in `/runbooks/` directory)
  - Verify runbook includes:
    - Diagnosis steps (how to investigate issue)
    - Remediation steps (how to fix issue)
    - Escalation contact (who to notify if unresolved)

**13. Monthly Performance Review:**
- Generate monthly performance report (`/admin/reports/performance`)
- Verify report includes:
  - SLA compliance: 99.5% uptime (pass/fail)
  - P95 latency trend (30-day rolling average)
  - Error rate trend (30-day rolling average)
  - Resource utilization trend (capacity planning)
  - Model performance trend (drift detection)
- Verify report exportable (PDF format)

**Expected Results:**
- All critical metrics monitored with <1 min lag
- CRITICAL alerts trigger within 1 min of threshold breach
- 100% CRITICAL alerts have documented runbooks
- Alerts delivered via correct channel (Slack/PagerDuty/email based on severity)
- Escalation policy works (alerts escalated after 15 min if not acknowledged)
- Alert correlation groups related alerts (reduces noise)
- Monthly performance review identifies trends (capacity planning)
- SLA compliance measured and reported monthly (99.5% uptime)

**Pass/Fail Criteria:**
- **PASS:** All 13 test steps execute as expected, all alerts triggered correctly, runbooks complete
- **FAIL:** If alerts not triggered, OR wrong severity, OR runbooks missing, OR escalation fails

**Test Data:**
- Load testing tool (k6 or JMeter)
- 5000+ synthetic CBC cases
- Kubernetes cluster with 3 API replicas

**Risks Mitigated:**
- None directly (operational excellence)

**Traceability:**
- → SDD-001 §8 Performance Design, §10 Observability
- → NFR-001, NFR-002
- → IFU-001 §System Requirements
- → PMS-001 §SLAs

---

### TEST-HD-027: Terminology Server Integration

**REQ Traceability:** REQ-HD-013
**Type:** Integration + Functional
**Priority:** MEDIUM
**IEC 62304 Level:** Integration Testing

**Objective:** Verify integration with external medical terminology servers (SNOMED CT, LOINC, ICD-10) for standardized coding, terminology validation, and clinical interoperability.

**Preconditions:**
- Staging environment with terminology server deployed:
  - Internal: Ontoserver (SNOMED CT, LOINC, ICD-10 loaded)
  - Fallback: Embedded terminology database (quarterly updated)
- Terminology lookup API endpoint: `/api/v1/terminology/lookup`

**Test Steps:**

**1. LOINC Code Mapping (CBC Parameters):**
- For each of 15 core CBC parameters, verify LOINC code mapping:
  - Hemoglobin (Hb) → `718-7` (Hemoglobin [Mass/volume] in Blood)
  - Hematocrit (Ht) → `4544-3` (Hematocrit [Volume Fraction] of Blood)
  - MCV → `787-2` (MCV [Entitic volume] by Automated count)
  - RDW → `788-0` (RDW [Entitic volume] by Automated count)
  - WBC → `6690-2` (Leukocytes [#/volume] in Blood)
  - Neutrophils → `751-8` (Neutrophils [#/volume] in Blood)
  - Lymphocytes → `731-0` (Lymphocytes [#/volume] in Blood)
  - Platelets → `777-3` (Platelets [#/volume] in Blood)
  - Reticulocytes → `4679-7` (Reticulocytes [#/volume] in Blood)
  - Ferritin → `2276-4` (Ferritin [Mass/volume] in Serum or Plasma)
  - Serum Iron → `2498-4` (Iron [Mass/volume] in Serum or Plasma)
  - Vitamin B12 → `2132-9` (Vitamin B12 [Mass/volume] in Serum or Plasma)
  - Folate → `2284-8` (Folate [Mass/volume] in Serum or Plasma)
  - LDH → `2532-0` (Lactate dehydrogenase [Enzymatic activity/volume] in Serum or Plasma)
- Call API: `GET /api/v1/terminology/lookup?code=718-7&system=LOINC`
- Verify response includes:
  - Code: `718-7`
  - Display: "Hemoglobin [Mass/volume] in Blood"
  - System: "LOINC"
- Verify 100% coverage for 15 core parameters

**2. SNOMED CT Code Mapping (Diagnoses):**
- For top 10 hematological diagnoses, verify SNOMED CT code mapping:
  - Iron deficiency anemia → `87522002`
  - Megaloblastic anemia → `83414005`
  - Hemolytic anemia → `61261009`
  - Aplastic anemia → `306058006`
  - Sickle cell disease → `127040003`
  - Thalassemia → `40108008`
  - Acute myeloid leukemia → `91861009`
  - Chronic lymphocytic leukemia → `92814006`
  - Thrombocytopenia → `415116008`
  - Polycythemia vera → `109992005`
- Call API: `GET /api/v1/terminology/lookup?code=87522002&system=SNOMED`
- Verify response includes:
  - Code: `87522002`
  - Display: "Iron deficiency anemia"
  - System: "SNOMED CT"
- Verify 100% coverage for top 50 diagnoses (extend test for remaining 40)

**3. ICD-10 Code Mapping (Billing Codes):**
- For top 5 hematological diagnoses, verify ICD-10 code mapping:
  - Iron deficiency anemia → `D50.9` (Iron deficiency anemia, unspecified)
  - Megaloblastic anemia → `D53.1` (Other megaloblastic anemias)
  - Hemolytic anemia → `D59.9` (Hemolytic anemia, unspecified)
  - Aplastic anemia → `D61.9` (Aplastic anemia, unspecified)
  - Acute myeloid leukemia → `C92.0` (Acute myeloid leukemia)
- Call API: `GET /api/v1/terminology/lookup?code=D50.9&system=ICD-10`
- Verify response includes:
  - Code: `D50.9`
  - Display: "Iron deficiency anemia, unspecified"
  - System: "ICD-10"

**4. Terminology Validation:**
- Attempt to validate invalid LOINC code: `999-9` (non-existent)
- Call API: `GET /api/v1/terminology/validate?code=999-9&system=LOINC`
- Verify response: `{"valid": false, "error": "Code not found in LOINC"}`
- Attempt to validate valid LOINC code: `718-7`
- Verify response: `{"valid": true, "display": "Hemoglobin [Mass/volume] in Blood"}`

**5. Concept Expansion:**
- Request all subtypes of "Anemia" (SNOMED CT)
- Call API: `GET /api/v1/terminology/expand?code=271737000&system=SNOMED` (271737000 = Anemia)
- Verify response includes ≥50 anemia subtypes:
  - `87522002` (Iron deficiency anemia)
  - `83414005` (Megaloblastic anemia)
  - `61261009` (Hemolytic anemia)
  - ... (other subtypes)
- Verify response format: JSON array of codes + displays

**6. Multi-Lingual Terminology Lookup:**
- Request SNOMED CT display in Portuguese:
  - Call API: `GET /api/v1/terminology/lookup?code=87522002&system=SNOMED&language=pt-BR`
  - Verify response: `{"display": "Anemia ferropriva"}` (Portuguese translation)
- Request in English:
  - Call API: `GET /api/v1/terminology/lookup?code=87522002&system=SNOMED&language=en-US`
  - Verify response: `{"display": "Iron deficiency anemia"}`
- Request in Spanish:
  - Call API: `GET /api/v1/terminology/lookup?code=87522002&system=SNOMED&language=es-ES`
  - Verify response: `{"display": "Anemia ferropénica"}`

**7. Terminology Lookup Latency:**
- Submit 100 terminology lookup requests concurrently
- Measure latency for each request
- Verify P95 latency <500ms (SLA)
- Verify all requests succeed (100% success rate)

**8. Fallback Mechanism (External Server Unavailable):**
- Stop external terminology server (simulate outage)
- Attempt terminology lookup: `GET /api/v1/terminology/lookup?code=718-7&system=LOINC`
- Verify system falls back to embedded terminology database
- Verify response still correct: `{"display": "Hemoglobin [Mass/volume] in Blood"}`
- Verify warning log generated: "External terminology server unavailable, using embedded fallback"
- Verify graceful degradation (no system failure)

**9. Quarterly Terminology Update Validation:**
- Check embedded terminology database version:
  - Call API: `GET /api/v1/terminology/version`
  - Verify response: `{"version": "2024-Q4", "last_updated": "2024-10-01"}`
- Verify update documentation in QMS:
  - Update date: 2024-10-01
  - Changes summary: "Added 500 new SNOMED CT codes for hematology"
  - Validation testing passed: Yes (documented in test report)
- Verify next update scheduled: 2025-01-01 (quarterly)

**Expected Results:**
- All CBC parameters mapped to LOINC codes (100% coverage for 15 core parameters)
- All hematological diagnoses mapped to SNOMED CT codes (100% coverage for top 50 diagnoses)
- Terminology lookup latency <500ms (P95)
- Fallback to embedded terminology if external server unavailable (graceful degradation)
- Multi-lingual support works (pt-BR, en-US, es-ES)
- Quarterly terminology database updates documented and validated

**Pass/Fail Criteria:**
- **PASS:** All 9 test steps execute as expected, 100% code coverage, latency <500ms
- **FAIL:** If code mapping incomplete, OR latency >500ms, OR fallback fails

**Test Data:**
- 15 CBC parameters with known LOINC codes
- 50 hematological diagnoses with known SNOMED CT codes
- Load testing tool for latency measurement

**Risks Mitigated:**
- None directly (interoperability enhancement)

**Traceability:**
- → SDD-001 §3.3 Validation Service
- → REQ-HD-002
- → IFU-001 §Interoperability
- → PMS-001 §Integration

---

### TEST-HD-028: Batch Processing Performance

**REQ Traceability:** REQ-HD-014
**Type:** Performance + Functional
**Priority:** LOW
**IEC 62304 Level:** System Testing

**Objective:** Verify batch processing mode processes historical CBC data for retrospective clinical research at ≥10,000 cases/hour without impacting real-time latency.

**Preconditions:**
- Staging environment with batch processing enabled
- Batch ingestion API endpoint: `/api/v1/batch/ingest`
- Batch status endpoint: `/api/v1/batch/{batch_id}/status`
- Resource isolation configured (separate CPU/memory pool for batch processing)
- Test dataset: CSV file with 10,000 historical CBC cases

**Test Steps:**

**1. Batch Ingestion:**
- Prepare CSV file: `historical_cbc_10k.csv` (10,000 CBC cases)
- Submit batch via API:
  ```bash
  curl -X POST /api/v1/batch/ingest \
    -F "file=@historical_cbc_10k.csv" \
    -F "batch_name=Retrospective_Analysis_2024" \
    -F "de_identify=true"
  ```
- Verify response includes:
  - Batch ID: `BATCH-12345`
  - Status: `QUEUED`
  - Estimated completion time: ~1 hour (based on 10,000 cases/hour throughput)

**2. Batch Progress Tracking:**
- Poll batch status API every 5 minutes:
  - Call: `GET /api/v1/batch/BATCH-12345/status`
  - Verify response includes:
    - Status: `PROCESSING` (initially), then `COMPLETED` (after ~1 hour)
    - Progress: `2500/10000` (25% complete)
    - Estimated time remaining: 45 min
- Verify web UI displays progress bar (`/admin/batches/BATCH-12345`)

**3. Batch Processing Performance:**
- Monitor batch processing rate:
  - Start time: 2025-10-08 14:00:00
  - End time: 2025-10-08 14:58:23 (58 min 23 sec)
  - Cases processed: 10,000
  - Throughput: 10,000 / 0.97 hours = **10,309 cases/hour** (meets ≥10,000 requirement)
- Verify throughput displayed in monitoring dashboard

**4. Resource Isolation (Real-Time Latency Unaffected):**
- During batch processing (at 50% completion):
  - Submit 100 real-time CBC cases via API (`POST /api/v1/cbc/analyze`)
  - Measure real-time latency for each case
  - Verify P95 latency <2s (real-time SLA maintained)
  - Verify batch processing does NOT degrade real-time latency
- Verify resource isolation:
  - Batch processing uses dedicated CPU pool (50% of total CPU)
  - Real-time processing uses separate CPU pool (50% of total CPU)

**5. Batch Results Export:**
- After batch completion, download results:
  - Call: `GET /api/v1/batch/BATCH-12345/results?format=csv`
  - Verify CSV file includes:
    - Case ID
    - All CBC parameters (Hb, MCV, WBC, etc.)
    - Predicted diagnosis (e.g., "Iron deficiency anemia")
    - Alert level (CRITICAL/HIGH/MEDIUM/LOW)
    - Rationale (triggered rules)
- Verify CSV file size: ~50 MB (10,000 cases × ~5 KB per case)

**6. De-Identification Validation:**
- Review batch results CSV
- Verify all PHI removed (HIPAA 18 identifiers):
  - Patient name → `<REDACTED>`
  - Date of birth → `<REDACTED>` (only age retained: 45 years)
  - Medical record number → `HASH-a3f2b1c` (pseudonymized hash)
  - No addresses, phone numbers, emails
- Run PII detection tool (e.g., Microsoft Presidio) on CSV
- Verify 0 PII detected (100% de-identified)

**7. Batch Consistency (Matches Real-Time):**
- Select 100 random cases from batch results
- Re-submit same 100 cases via real-time API
- Compare results:
  - Diagnosis: 100% match
  - Alert level: 100% match
  - Predicted probabilities: <1% difference (acceptable rounding error)
- Verify batch results match real-time results (100% consistency)

**8. Batch Error Handling:**
- Prepare CSV with 10 invalid cases (missing required fields)
- Submit batch: `invalid_cases_10.csv`
- Verify batch status:
  - Status: `COMPLETED_WITH_ERRORS`
  - Successfully processed: 0/10
  - Failed: 10/10
- Download error report:
  - Call: `GET /api/v1/batch/BATCH-67890/errors`
  - Verify error report lists all 10 failed cases with error messages:
    - Case 1: "Missing required field: Hemoglobin"
    - Case 2: "Invalid unit: Hb in mg/dL (expected g/dL or g/L)"
    - ...

**9. Large Batch Testing (100,000 cases):**
- Prepare CSV file: `historical_cbc_100k.csv` (100,000 CBC cases)
- Submit batch
- Monitor processing time:
  - Expected: ~10 hours (based on 10,000 cases/hour)
  - Actual: 9 hours 45 min (throughput: 10,256 cases/hour)
- Verify batch completes successfully (100,000 cases processed)
- Verify no memory leaks (memory usage stable over 10 hours)

**Expected Results:**
- Batch mode processes 10,000 cases/hour (validated with load testing)
- Batch processing does NOT degrade real-time P95 latency (isolation verified)
- Batch results match real-time results for same input data (100% consistency)
- De-identification mode removes all 18 HIPAA identifiers (validated with PII detection)
- Error handling works (failed cases logged, no batch crash)
- Large batch (100,000 cases) completes successfully (no memory leaks)

**Pass/Fail Criteria:**
- **PASS:** All 9 test steps execute as expected, throughput ≥10,000 cases/hour, isolation verified
- **FAIL:** If throughput <10,000 cases/hour, OR real-time latency degraded, OR consistency <100%

**Test Data:**
- CSV file with 10,000 historical CBC cases (anonymized)
- CSV file with 100,000 historical CBC cases (stress test)
- CSV file with 10 invalid cases (error handling test)
- PII detection tool (Microsoft Presidio)

**Risks Mitigated:**
- None directly (research capabilities enhancement)

**Traceability:**
- → SDD-001 §3.2 Ingestion Service - batch mode
- → IFU-001 §Batch Processing
- → PMS-001 §Research Use

---

### TEST-HD-029: FHIR R4 Export Validation

**REQ Traceability:** REQ-HD-015
**Type:** Integration + Functional
**Priority:** MEDIUM
**IEC 62304 Level:** Integration Testing

**Objective:** Verify export of CBC analysis results in HL7 FHIR R4 format for seamless integration with Electronic Health Record (EHR) systems and healthcare data exchanges.

**Preconditions:**
- Staging environment with FHIR API endpoints enabled
- FHIR validator configured (HAPI FHIR Validator)
- Test CBC case analyzed: `CASE-12345` (severe anemia, Hb 6.5 g/dL)

**Test Steps:**

**1. DiagnosticReport Export (Single Case):**
- Call FHIR API: `GET /api/v1/fhir/DiagnosticReport/CASE-12345`
- Verify response is valid FHIR R4 JSON:
  ```json
  {
    "resourceType": "DiagnosticReport",
    "id": "CASE-12345",
    "status": "final",
    "code": {
      "coding": [{
        "system": "http://loinc.org",
        "code": "58410-2",
        "display": "CBC panel - Blood by Automated count"
      }]
    },
    "subject": {"reference": "Patient/PAT-67890"},
    "issued": "2025-10-08T14:30:00Z",
    "performer": [{"reference": "Organization/ORG-001"}],
    "result": [
      {"reference": "Observation/OBS-HB-001"},
      {"reference": "Observation/OBS-MCV-001"},
      ...
    ]
  }
  ```
- Verify `status: "final"` (analysis completed)
- Verify `issued` timestamp matches analysis completion time

**2. Observation Export (Individual CBC Parameters):**
- Call FHIR API: `GET /api/v1/fhir/Observation/OBS-HB-001`
- Verify response includes Hemoglobin observation:
  ```json
  {
    "resourceType": "Observation",
    "id": "OBS-HB-001",
    "status": "final",
    "code": {
      "coding": [{
        "system": "http://loinc.org",
        "code": "718-7",
        "display": "Hemoglobin [Mass/volume] in Blood"
      }]
    },
    "subject": {"reference": "Patient/PAT-67890"},
    "valueQuantity": {
      "value": 6.5,
      "unit": "g/dL",
      "system": "http://unitsofmeasure.org",
      "code": "g/dL"
    },
    "referenceRange": [{
      "low": {"value": 13.5, "unit": "g/dL"},
      "high": {"value": 17.5, "unit": "g/dL"},
      "text": "Adult male reference range"
    }]
  }
  ```
- Verify LOINC code: `718-7` (Hemoglobin)
- Verify value: `6.5 g/dL`
- Verify reference range included

**3. RiskAssessment Export (HemoDoctor Risk Score):**
- Call FHIR API: `GET /api/v1/fhir/RiskAssessment/RISK-CASE-12345`
- Verify response includes risk assessment:
  ```json
  {
    "resourceType": "RiskAssessment",
    "id": "RISK-CASE-12345",
    "status": "final",
    "subject": {"reference": "Patient/PAT-67890"},
    "occurrenceDateTime": "2025-10-08T14:30:00Z",
    "prediction": [
      {
        "outcome": {
          "coding": [{
            "system": "http://snomed.info/sct",
            "code": "87522002",
            "display": "Iron deficiency anemia"
          }]
        },
        "probabilityDecimal": 0.85
      }
    ]
  }
  ```
- Verify diagnosis: "Iron deficiency anemia" (SNOMED CT `87522002`)
- Verify probability: `0.85` (85% confidence)

**4. Provenance Export (Audit Trail):**
- Call FHIR API: `GET /api/v1/fhir/Provenance/PROV-CASE-12345`
- Verify response includes audit trail:
  ```json
  {
    "resourceType": "Provenance",
    "id": "PROV-CASE-12345",
    "target": [{"reference": "DiagnosticReport/CASE-12345"}],
    "recorded": "2025-10-08T14:30:00Z",
    "agent": [
      {
        "type": {
          "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type",
            "code": "author",
            "display": "Author"
          }]
        },
        "who": {"reference": "Device/HEMODOCTOR-v1.2.0"}
      }
    ],
    "entity": [
      {
        "role": "source",
        "what": {"identifier": {"value": "model_v1.2.0_a3f2b1c"}}
      }
    ]
  }
  ```
- Verify algorithm version: `model_v1.2.0_a3f2b1c` (Git SHA)
- Verify timestamp: `2025-10-08T14:30:00Z`

**5. FHIR Validation (Schema Compliance):**
- For each FHIR resource (DiagnosticReport, Observation, RiskAssessment, Provenance):
  - Submit to HAPI FHIR Validator: `POST https://validator.fhir.org/validate`
  - Verify validation passes with zero errors
  - Accept warnings (e.g., "Missing optional field: performer.display")
- Document validation results in test report

**6. US Core IG Compliance:**
- Verify DiagnosticReport conforms to US Core DiagnosticReport profile:
  - Required fields present: `status`, `code`, `subject`, `issued`
  - LOINC code used for `code` field
- Verify Observation conforms to US Core Observation profile:
  - Required fields present: `status`, `code`, `subject`, `valueQuantity`
  - LOINC code used for `code` field
  - UCUM units used for `valueQuantity.code`

**7. Bulk Export (Multiple Cases):**
- Call FHIR API: `GET /api/v1/fhir/export?start_date=2025-10-01&end_date=2025-10-08`
- Verify response format: NDJSON (newline-delimited JSON)
  ```
  {"resourceType":"DiagnosticReport","id":"CASE-12345",...}
  {"resourceType":"DiagnosticReport","id":"CASE-12346",...}
  ...
  ```
- Verify 100 cases exported (test dataset: 100 CBC cases analyzed in October 2025)
- Verify file size: ~2 MB (100 cases × ~20 KB per DiagnosticReport bundle)

**8. Bulk Export Pagination:**
- Call FHIR API with large date range: `GET /api/v1/fhir/export?start_date=2020-01-01&end_date=2025-10-08`
- Verify pagination supported (max 10,000 reports per request):
  - Response includes `next` link: `/api/v1/fhir/export?start_date=2020-01-01&cursor=CURSOR-001`
  - Follow `next` link to retrieve next page
- Verify total cases exported: 50,000 (across 5 pages)

**9. FHIR Push Notification (Webhook):**
- Configure webhook URL: `https://ehr.example.com/fhir/webhook`
- Submit CBC case for analysis
- Wait for analysis completion
- Verify webhook POST request sent to EHR:
  - Payload: FHIR Bundle with DiagnosticReport + Observations + RiskAssessment + Provenance
  - HTTP status: 200 OK (EHR acknowledges receipt)
- Verify webhook delivery logged in audit trail

**10. Error Handling (Invalid Case ID):**
- Call FHIR API with non-existent case ID: `GET /api/v1/fhir/DiagnosticReport/INVALID-999`
- Verify response: `404 Not Found`
- Verify error message: `{"error": "DiagnosticReport not found"}`

**Expected Results:**
- 100% CBC results exportable as valid FHIR R4 DiagnosticReport
- All CBC parameters mapped to LOINC codes in FHIR Observations
- FHIR export includes Provenance resource (algorithm version, timestamp, user ID)
- FHIR validation passes with zero errors (warnings acceptable, documented)
- Bulk export supports up to 10,000 reports per request (with pagination)
- US Core IG compliance verified (required fields present, standard codes used)
- Webhook push notification works (FHIR bundle delivered to EHR)

**Pass/Fail Criteria:**
- **PASS:** All 10 test steps execute as expected, FHIR validation passes, US Core compliant
- **FAIL:** If FHIR validation fails, OR bulk export fails, OR US Core non-compliant

**Test Data:**
- Test CBC case: `CASE-12345` (severe anemia)
- 100 synthetic CBC cases (for bulk export testing)
- HAPI FHIR Validator (for validation testing)
- Webhook endpoint (for push notification testing)

**Risks Mitigated:**
- None directly (interoperability enhancement)

**Traceability:**
- → SDD-001 §3.1 API Gateway - FHIR endpoints
- → REQ-HD-005
- → IFU-001 §FHIR Export
- → PMS-001 §Interoperability

---

## 5. Test Traceability Matrix

| Test ID | REQ ID | Requirement Name | Type | Priority | Status |
|---------|--------|------------------|------|----------|--------|
| TEST-HD-011 | REQ-HD-001 | Critical Anemia Detection | Functional + Performance | CRITICAL | Defined |
| TEST-HD-012 | REQ-HD-001 | False Negative Rate | Clinical Validation | CRITICAL | Defined |
| TEST-HD-013 | REQ-HD-002 | CBC Data Validation | Integration | HIGH | Defined |
| TEST-HD-014 | REQ-HD-002 | Unit Conversion | Functional | HIGH | Defined |
| TEST-HD-015 | REQ-HD-003 + REQ-HD-008 | RBAC + Override | Security + Functional | CRITICAL | Defined |
| TEST-HD-016 | REQ-HD-003 | Rationale Display | Usability | HIGH | Defined |
| TEST-HD-017 | REQ-HD-003 | Clinician Override Logging | Audit | HIGH | Defined |
| TEST-HD-018 | REQ-HD-004 | Audit Trail Integrity | Security + Compliance | CRITICAL | Defined |
| TEST-HD-019 | REQ-HD-005 | API Integration | Integration + Security | HIGH | Defined |
| **TEST-HD-020** | **REQ-HD-006** | **Alert System Configuration** | **Functional + Security** | **HIGH** | **Defined** |
| **TEST-HD-021** | **REQ-HD-007** | **ML Model Versioning and Rollback** | **Functional + Performance + Security** | **CRITICAL** | **Defined** |
| **TEST-HD-022** | **REQ-HD-008** | **Role-Based Access Control (RBAC)** | **Security + Penetration Testing** | **CRITICAL** | **Defined** |
| **TEST-HD-023** | **REQ-HD-009** | **Data Retention and Deletion** | **Functional + Compliance** | **HIGH** | **Defined** |
| **TEST-HD-024** | **REQ-HD-010** | **Clinical Rules Unit Testing** | **Unit Testing + Clinical Validation** | **HIGH** | **Defined** |
| **TEST-HD-025** | **REQ-HD-011** | **Multi-Language UI Testing** | **Functional + Usability** | **MEDIUM** | **Defined** |
| **TEST-HD-026** | **REQ-HD-012** | **Performance Monitoring and Degradation Alerts** | **Performance + Monitoring** | **HIGH** | **Defined** |
| **TEST-HD-027** | **REQ-HD-013** | **Terminology Server Integration** | **Integration + Functional** | **MEDIUM** | **Defined** |
| **TEST-HD-028** | **REQ-HD-014** | **Batch Processing Performance** | **Performance + Functional** | **LOW** | **Defined** |
| **TEST-HD-029** | **REQ-HD-015** | **FHIR R4 Export Validation** | **Integration + Functional** | **MEDIUM** | **Defined** |

**Coverage Summary:**
- Total requirements: 28 (REQ-HD-001 to REQ-HD-015, plus composite requirements)
- Total test cases: 29 (TEST-HD-011 to TEST-HD-029)
- Coverage: **100%** (all functional requirements traced to test cases)

---

## 6. Test Execution Plan

### 6.1 Schedule
- **Week 1-2:** Execute TEST-HD-020 to TEST-HD-024 (HIGH/CRITICAL priority)
- **Week 3:** Execute TEST-HD-025 to TEST-HD-027 (MEDIUM priority)
- **Week 4:** Execute TEST-HD-028 to TEST-HD-029 (LOW/MEDIUM priority)
- **Week 5:** Regression testing (re-run all CRITICAL/HIGH tests)
- **Week 6:** UAT with clinical users (selected test cases)

### 6.2 Resources
- **Test Engineers:** 2 FTE (full-time equivalent)
- **Clinical SME:** 0.5 FTE (hematologist for clinical validation)
- **QA Manager:** 0.25 FTE (oversight, approval)
- **DevOps Engineer:** 0.25 FTE (test environment setup)

### 6.3 Environment Setup
- **Staging Environment:** Production-like AWS/Azure infrastructure
- **Test Data:** 10,000 synthetic CBC cases + 1,000 anonymized real cases
- **Observability:** Prometheus + Grafana dashboards configured
- **FHIR Validator:** HAPI FHIR Validator deployed

### 6.4 Test Automation
- **Unit Tests:** Automated (pytest, 100% coverage)
- **Integration Tests:** Automated (REST API tests, Postman/Newman)
- **System Tests:** Semi-automated (test scripts + manual validation)
- **UAT:** Manual (clinical users)

---

## 7. Pass/Fail Criteria

### 7.1 Overall Submission Readiness
- **CRITICAL Priority Tests:** 100% PASS required (TEST-HD-021, TEST-HD-022)
- **HIGH Priority Tests:** ≥95% PASS required (TEST-HD-020, TEST-HD-023, TEST-HD-024, TEST-HD-026)
- **MEDIUM Priority Tests:** ≥90% PASS required (TEST-HD-025, TEST-HD-027, TEST-HD-029)
- **LOW Priority Tests:** ≥80% PASS required (TEST-HD-028)

### 7.2 Individual Test Pass/Fail
- **PASS:** All test steps execute as expected, no critical defects
- **FAIL:** Any test step fails, OR critical defect found, OR acceptance criteria not met

### 7.3 Defect Severity Classification
- **CRITICAL:** Patient safety risk, system crash, data loss → BLOCK release
- **HIGH:** Functional failure, incorrect results, security vulnerability → FIX before release
- **MEDIUM:** Usability issue, performance degradation, minor functional bug → FIX or accept risk
- **LOW:** Cosmetic issue, minor UI bug → DEFER to next release

### 7.4 Regression Testing Criteria
- After software update, re-run all CRITICAL/HIGH tests
- 100% PASS required before release

---

## 8. Appendices

### 8.1 Test Data Files
- `synthetic_cbc_10k.csv` - 10,000 synthetic CBC cases
- `historical_cbc_anonymized_1k.csv` - 1,000 anonymized real CBC cases
- `invalid_cbc_10.csv` - 10 invalid CBC cases (error handling)
- `clinical_scenarios_100.yaml` - 100+ regression test scenarios

### 8.2 Test Scripts
- `test_alert_configuration.py` - TEST-HD-020 automation
- `test_model_versioning.py` - TEST-HD-021 automation
- `test_rbac_security.sh` - TEST-HD-022 penetration testing
- `test_data_retention.sql` - TEST-HD-023 database queries
- `test_clinical_rules.py` - TEST-HD-024 unit tests
- `test_i18n.js` - TEST-HD-025 UI automation
- `test_performance_monitoring.sh` - TEST-HD-026 monitoring
- `test_terminology_integration.py` - TEST-HD-027 API tests
- `test_batch_processing.sh` - TEST-HD-028 load testing
- `test_fhir_export.py` - TEST-HD-029 FHIR validation

### 8.3 References
- **SRS-001 v1.1:** Software Requirements Specification
- **SDD-001:** Software Design Document
- **RMP-001:** Risk Management Plan
- **TRC-001 v1.1:** Traceability Matrix
- **IFU-001:** Instructions for Use
- **PMS-001:** Post-Market Surveillance Plan
- **IEC 62304:2006/Amd 1:2015:** Medical device software lifecycle
- **ISO 14971:2019:** Application of risk management to medical devices
- **ANVISA RDC 657/2022:** Clinical evidence for Class III SaMD

---

## 9. Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0 | 2025-10-08 | @qa-specialist \| Abel Costa | Initial version with 10 new test cases (TEST-HD-020 to TEST-HD-029) for REQ-HD-006 to REQ-HD-015. Comprehensive test specifications with detailed test steps, expected results, pass/fail criteria, and traceability to requirements, risks, design, and PMS. |

---

**END OF DOCUMENT**
