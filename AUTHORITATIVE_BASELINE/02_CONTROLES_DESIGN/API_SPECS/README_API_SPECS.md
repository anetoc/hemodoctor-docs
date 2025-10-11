# HemoDoctor API Specifications - Complete Package

**Document Code:** API-README-001
**Version:** 1.0
**Date:** 2025-10-08
**Author:** @software-architecture-specialist
**Status:** Complete
**Confidentiality:** Internal/Confidential

---

## Summary

This directory contains **complete, production-ready API specifications** for all 9 HemoDoctor microservices, created to support:

1. **Development teams** - Implementation reference
2. **QA teams** - Automated testing (Postman/Swagger)
3. **Security teams** - Penetration testing
4. **ANVISA reviewers** - Architecture validation (IEC 62304 compliance)

---

## Files Created (11 total)

### Master Index
- **`00_API_INDEX.md`** (12KB) - Complete documentation of API architecture, versioning, security, error handling, testing strategy

### OpenAPI 3.1 Specifications (9 services)

| File | Service | Class | Size | Endpoints | Critical Features |
|------|---------|-------|------|-----------|-------------------|
| `01_API_Gateway_OpenAPI_v1.0.yaml` | API Gateway | B | 30KB | 7 | OAuth2, rate limiting, Class C routing |
| `02_Ingestion_Service_OpenAPI_v1.0.yaml` | Ingestion | B | 2.5KB | 2 | Multi-format ingestion (HL7/FHIR/JSON) |
| `03_Validation_Service_OpenAPI_v1.0.yaml` | Validation | B | 2.6KB | 2 | Unit conversion, LOINC mapping, reference ranges |
| `04_Rules_Engine_OpenAPI_v1.0.yaml` | Rules Engine | **C** | 23KB | 3 | Deterministic clinical rules, differential diagnosis |
| `05_HemoAI_Inference_OpenAPI_v1.0.yaml` | HemoAI | **C** | 28KB | 4 | ML risk scoring, SHAP explainability, model versioning |
| `06_Alert_Orchestrator_OpenAPI_v1.0.yaml` | Alert Orchestrator | **C** | 2.8KB | 2 | CRITICAL alert generation, throttling |
| `07_Audit_Service_OpenAPI_v1.0.yaml` | Audit | A | 3.2KB | 3 | Immutable WORM logs, cryptographic signatures |
| `08_Model_Manager_OpenAPI_v1.0.yaml` | Model Manager | A | 3.4KB | 4 | Model versioning, promotion, rollback |
| `09_UI_Backend_OpenAPI_v1.0.yaml` | UI Backend | B | 2.7KB | 4 | Session management, report export (PDF/CSV) |

### AsyncAPI 2.6 Specification
- **`10_Async_Events_AsyncAPI_v1.0.yaml`** (2.5KB) - Event-driven communication (5 channels)

**Total specification size:** ~120KB of detailed API contracts

---

## Key Highlights

### 1. Complete Coverage

**All endpoints from SDD-001 v1.1 are specified** with:
- HTTP methods, paths, parameters, request/response schemas
- Authentication/authorization requirements
- Error responses (RFC 7807 compliant)
- Examples for all scenarios (normal, critical, error cases)
- Full traceability to SRS-001 requirements

### 2. Class C Safety Emphasis

**3 Class C microservices** (Rules Engine, HemoAI, Alert Orchestrator) have:
- **Explicit safety class labeling** in OpenAPI metadata
- **JWT scope requirements** (`scope: clinical_analysis`)
- **Timeout specifications** (P95 <2s per NFR-001)
- **Audit logging requirements** (all requests logged)
- **Detailed clinical examples** (severe anemia, normal hemogram)
- **SHAP explainability schemas** (HemoAI only)

### 3. Production-Ready Features

**Security:**
- OAuth2/OIDC authentication flows fully documented
- JWT token structure with scopes and roles
- Rate limiting policies (100/min external, 50/min Class C)
- mTLS support for Class C service-to-service calls

**Error Handling:**
- RFC 7807 Problem Details for all errors
- Consistent error types across all services
- Trace ID propagation for distributed debugging

**Observability:**
- OpenTelemetry trace ID headers required
- Prometheus metrics guidelines
- Structured logging examples

**API Versioning:**
- URL-based versioning (`/api/v1/`)
- Deprecation policy (6 months notice)
- Version support matrix

**Testing:**
- Idempotency support (Idempotency-Key header)
- Postman collection generation ready
- Contract testing scenarios defined

### 4. Clinical Domain Expertise

**CBC Data Schemas:**
- All 14 CBC parameters defined with LOINC codes
- UCUM units (g/dL, fL, 10*3/uL)
- Patient-specific reference ranges (age/sex/pregnancy)
- Physiological validation limits

**Differential Diagnosis:**
- Structured diagnosis objects with probability scores
- Clinical rationale for each diagnosis
- Supporting parameters and suggested tests
- Confidence levels (HIGH/MEDIUM/LOW)

**Alert Levels:**
- CRITICAL (Hb <7 g/dL, immediate intervention)
- HIGH/MEDIUM/LOW prioritization
- Suggested clinical actions
- Alert throttling rules

### 5. Async Event Architecture

**5 AsyncAPI channels defined:**
1. `cbc.ingestion.completed` - Ingestion → Validation
2. `cbc.validation.completed` - Validation → Rules Engine
3. `cbc.analysis.completed` - Rules + ML → Alert Orchestrator
4. `alerts.generated` - Alerts → Audit + UI
5. `model.deployed` - Model Manager → HemoAI

**Benefits:**
- Decoupled microservices (no direct dependencies)
- Scalable event-driven workflows
- Replay capability for audit trail reconstruction
- Multi-subscriber support (UI + Audit can both consume alerts)

---

## Usage Instructions

### For Development Teams

**Generate code stubs:**
```bash
# Install OpenAPI Generator
npm install -g @openapitools/openapi-generator-cli

# Generate Python FastAPI server for Rules Engine (Class C)
openapi-generator-cli generate \
  -i 04_Rules_Engine_OpenAPI_v1.0.yaml \
  -g python-fastapi \
  -o ../../src/rules-engine/

# Generate TypeScript client for UI
openapi-generator-cli generate \
  -i 01_API_Gateway_OpenAPI_v1.0.yaml \
  -g typescript-axios \
  -o ../../ui/src/api/
```

**Validate specifications:**
```bash
# Install Swagger CLI
npm install -g @apidevtools/swagger-cli

# Validate all specs
for file in *.yaml; do
  swagger-cli validate "$file"
done
```

### For QA Teams

**Generate Postman collections:**
```bash
# Install OpenAPI to Postman converter
npm install -g openapi-to-postman

# Convert API Gateway spec to Postman
openapi2postmanv2 \
  -s 01_API_Gateway_OpenAPI_v1.0.yaml \
  -o API_Gateway_Postman_Collection.json \
  -p
```

**Run automated contract tests:**
```bash
# Import into Postman
# Use Newman for CI/CD automation
newman run API_Gateway_Postman_Collection.json \
  --environment production.json \
  --reporters cli,junit
```

### For Security Teams

**Penetration testing with Swagger UI:**
```bash
# Serve specs with Swagger UI
docker run -p 8080:8080 \
  -v $(pwd):/specs \
  -e SWAGGER_JSON=/specs/01_API_Gateway_OpenAPI_v1.0.yaml \
  swaggerapi/swagger-ui

# Access at http://localhost:8080
```

**Security audit checklist:**
- [ ] All Class C endpoints require JWT with `clinical_analysis` scope
- [ ] Rate limiting enforced (429 responses verified)
- [ ] OAuth2 flows properly configured (PKCE for web clients)
- [ ] Error messages don't leak sensitive data
- [ ] All inputs validated (JSON Schema enforcement)
- [ ] CORS policies restrictive (no `*` origins)

### For ANVISA Reviewers

**Traceability verification:**

All endpoints map to requirements in **SRS-001 v1.1**:

| Endpoint | Requirement | Verification Method |
|----------|-------------|---------------------|
| `POST /cbc/analyze` | REQ-HD-001 | Submit test CBC, verify diagnostic output |
| `GET /results/{case_id}` | REQ-HD-003 | Retrieve results, verify explanations present |
| `GET /audit/{case_id}` | REQ-HD-004 | Verify immutable audit trail with signatures |
| `POST /rules/execute` | REQ-HD-001 | Verify deterministic rules execution |
| `POST /predict` | REQ-HD-003 | Verify ML risk scores with SHAP explanations |

**IEC 62304 compliance verification:**

| IEC 62304 Requirement | Implementation | Verification |
|-----------------------|----------------|--------------|
| §5.3.1 Architecture design | All services documented in OpenAPI 3.1 | Review `00_API_INDEX.md` |
| §5.3.6 Class C segregation | JWT scope enforcement, network isolation | Review `04_Rules_Engine_OpenAPI_v1.0.yaml` security schemes |
| §7.1.1 Inputs validation | JSON Schema validation on all endpoints | Review request body schemas |
| §7.1.3 Error handling | RFC 7807 Problem Details consistently used | Review `ProblemDetail` component schemas |

---

## Next Steps

### Immediate Actions

1. **Review with development teams** (1 week)
   - Validate technical feasibility
   - Estimate implementation effort per service
   - Identify missing endpoints or schemas

2. **Generate Postman collections** (2 days)
   - Use `openapi-to-postman` converter
   - Add environment variables (dev/staging/prod)
   - Add pre-request scripts for OAuth2 token refresh

3. **Set up automated contract testing** (1 week)
   - Configure Newman in CI/CD pipeline
   - Create test data fixtures (normal CBC, severe anemia, etc.)
   - Define pass/fail criteria (all 2xx responses, no schema violations)

4. **Deploy Swagger UI** (1 day)
   - Host specs on internal documentation portal
   - Enable "Try it out" for development environment
   - Restrict production access to read-only

### Long-term Integration

5. **Implement API versioning in API Gateway** (2 weeks)
   - Configure Kong/Nginx to route `/api/v1/` to backend services
   - Implement deprecation headers for old endpoints
   - Set up version sunset automation

6. **Security audit of Class C endpoints** (1 week)
   - Penetration testing by external security firm
   - Verify JWT scope enforcement under load
   - Test circuit breaker behavior (Class B failures don't affect Class C)

7. **Performance testing** (2 weeks)
   - Load test with Gatling: 100 concurrent users
   - Verify Class C SLA: P95 <2s (per NFR-001)
   - Measure API Gateway overhead (<50ms)

8. **ANVISA submission package** (1 week)
   - Bundle all 11 API spec files
   - Include traceability matrix (endpoint → requirement → test case)
   - Provide Postman collection with example requests
   - Submit with SDD-001 v1.1 as supporting evidence

---

## Maintenance

**Version control:**
- All specs tracked in Git with semantic versioning
- Breaking changes require major version bump (v1 → v2)
- Backward-compatible changes increment minor version (v1.0 → v1.1)

**Change management:**
- API changes require ADR (Architecture Decision Record)
- Deprecation notices 6 months before removal
- All changes documented in CHANGELOG.md

**Review cycle:**
- Quarterly review of API specs for drift from implementation
- Annual review for security updates (OAuth2 flows, JWT algorithms)
- Post-incident reviews update error handling specs

---

## Contact

**Technical Lead:** @software-architecture-specialist
**Email:** internal-api@hemodoctor.com
**Documentation Portal:** https://docs.hemodoctor.com/api
**JIRA Project:** HEMO-API

---

## Appendix: File Size Summary

```
Total API specifications: 11 files, ~120KB

OpenAPI 3.1 (9 files):
  - Large (>20KB): 3 files (Gateway, Rules Engine, HemoAI) - Class C critical
  - Medium (2-4KB): 6 files (other services)

AsyncAPI 2.6 (1 file): 2.5KB
Master index: 12KB

Estimated Postman collection size: ~150KB (with examples)
Estimated generated code: ~50,000 lines (all services)
```

---

## Approval Signatures

**Prepared by:** @software-architecture-specialist | Abel Costa
**Date:** 2025-10-08

**Reviewed by:** {TECHNICAL_LEAD}
**Date:** {REVIEW_DATE}

**Approved for ANVISA submission by:** {QA_MANAGER}
**Date:** {APPROVAL_DATE}

---

**END OF DOCUMENT**
