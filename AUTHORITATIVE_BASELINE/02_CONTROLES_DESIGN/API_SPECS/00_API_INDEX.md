# HemoDoctor API Specifications - Master Index

**Document Code:** API-INDEX-001
**Version:** 1.0
**Date:** 2025-10-08
**Author:** @software-architecture-specialist | Abel Costa
**Status:** Under Review
**Confidentiality:** Internal/Confidential

---

## 1. Overview

This directory contains comprehensive API specifications for all 9 HemoDoctor microservices:

| Service | API Type | File | IEC 62304 Class | Status |
|---------|----------|------|-----------------|--------|
| **API Gateway** | REST (OpenAPI 3.1) | `01_API_Gateway_OpenAPI_v1.0.yaml` | Class B | Complete |
| **Ingestion Service** | REST (OpenAPI 3.1) | `02_Ingestion_Service_OpenAPI_v1.0.yaml` | Class B | Complete |
| **Validation Service** | REST (OpenAPI 3.1) | `03_Validation_Service_OpenAPI_v1.0.yaml` | Class B | Complete |
| **Rules Engine** | REST (OpenAPI 3.1) | `04_Rules_Engine_OpenAPI_v1.0.yaml` | **Class C** | Complete |
| **HemoAI Inference** | REST (OpenAPI 3.1) | `05_HemoAI_Inference_OpenAPI_v1.0.yaml` | **Class C** | Complete |
| **Alert Orchestrator** | REST (OpenAPI 3.1) | `06_Alert_Orchestrator_OpenAPI_v1.0.yaml` | **Class C** | Complete |
| **Audit Service** | REST (OpenAPI 3.1) | `07_Audit_Service_OpenAPI_v1.0.yaml` | Class A | Complete |
| **Model Manager** | REST (OpenAPI 3.1) | `08_Model_Manager_OpenAPI_v1.0.yaml` | Class A | Complete |
| **UI Backend** | REST (OpenAPI 3.1) | `09_UI_Backend_OpenAPI_v1.0.yaml` | Class B | Complete |
| **Async Events** | AsyncAPI 2.6 | `10_Async_Events_AsyncAPI_v1.0.yaml` | Mixed | Complete |

---

## 2. API Architecture Principles

### 2.1 RESTful Design

All synchronous APIs follow REST best practices:
- Resource-based URLs (`/api/v1/orders/{order_id}`)
- Standard HTTP methods (GET, POST, PUT, PATCH, DELETE)
- HTTP status codes per RFC 7231
- Hypermedia controls (HATEOAS) for navigation
- Content negotiation (`Accept: application/json`)

### 2.2 API Versioning Strategy

**URL-based versioning:** `/api/v1/`, `/api/v2/`

**Version lifecycle:**
- **v1.0**: Initial release (current)
- **v1.x**: Backward-compatible changes (new optional fields, new endpoints)
- **v2.0**: Breaking changes (deprecated endpoints removed, schema changes)

**Deprecation policy:**
- 6 months notice before breaking changes
- Deprecated endpoints return `Deprecation` header with sunset date
- All versions documented in OpenAPI specs

**Version support:**
- Current version (v1): Full support
- Previous version (v0, if exists): Security patches only for 12 months
- Older versions: Unsupported

### 2.3 Security Architecture

**Authentication:**
- **OAuth 2.0 / OpenID Connect** for external clients (LIS/HIS systems)
- **JWT Bearer tokens** for inter-service communication
- **Mutual TLS (mTLS)** for Class C service-to-service calls (optional)

**Authorization:**
- **Role-Based Access Control (RBAC):**
  - `lab_operator`: Read results, export reports
  - `lab_supervisor`: Override recommendations, manage alerts
  - `admin`: System configuration, user management
  - `auditor`: Read-only audit trail access
  - `system`: Internal service-to-service communication

**JWT Token Structure:**
```json
{
  "sub": "user123",
  "iss": "https://auth.hemodoctor.com",
  "aud": "hemodoctor-api",
  "exp": 1696790400,
  "iat": 1696762400,
  "scope": "clinical_analysis",
  "roles": ["lab_operator"],
  "tenant_id": "hospital-001"
}
```

**Class C Protection:**
- Class C endpoints require `scope: clinical_analysis`
- Only internal services can call Class C APIs directly
- External clients route through API Gateway only

### 2.4 Error Handling (RFC 7807)

All errors follow **Problem Details for HTTP APIs** (RFC 7807):

```json
{
  "type": "https://api.hemodoctor.com/errors/validation-error",
  "title": "Invalid CBC data",
  "status": 400,
  "detail": "Hemoglobin value 35.2 g/dL exceeds physiological limit (max 25 g/dL)",
  "instance": "/api/v1/cbc/analyze",
  "trace_id": "TRACE-2025-001234",
  "invalid_params": [
    {
      "name": "cbc.hemoglobin.value",
      "reason": "Value exceeds physiological maximum"
    }
  ]
}
```

**Standard Error Types:**
- `validation-error` (400): Invalid request data
- `authentication-required` (401): Missing or invalid token
- `forbidden` (403): Insufficient permissions
- `not-found` (404): Resource not found
- `conflict` (409): Resource state conflict
- `rate-limit-exceeded` (429): Too many requests
- `internal-error` (500): Server error
- `service-unavailable` (503): Temporary unavailability

### 2.5 Rate Limiting

**Per-client limits:**
- **External clients:** 100 requests/min (API Gateway)
- **Internal services (Class B → Class C):** 50 requests/min
- **Internal services (Class C internal):** 200 requests/min

**Headers:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1696762500
Retry-After: 45
```

**Exceeded limit:**
```json
{
  "type": "https://api.hemodoctor.com/errors/rate-limit-exceeded",
  "title": "Rate limit exceeded",
  "status": 429,
  "detail": "You have exceeded 100 requests per minute",
  "retry_after": 45
}
```

### 2.6 Pagination

**Cursor-based pagination** for large result sets:

```
GET /api/v1/orders?limit=50&cursor=eyJvcmRlcl9pZCI6Ik9SRC0yMDI1LTAwMTIzNCJ9
```

**Response:**
```json
{
  "data": [...],
  "pagination": {
    "cursor": "eyJvcmRlcl9pZCI6Ik9SRC0yMDI1LTAwMTIzNSJ9",
    "has_more": true,
    "total_count": 1234
  }
}
```

### 2.7 Idempotency

**POST/PUT/PATCH/DELETE operations:**
- Client provides `Idempotency-Key` header (UUID)
- Server stores key + response for 24 hours
- Duplicate requests return cached response (same status code + body)

```
POST /api/v1/cbc/analyze
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
```

---

## 3. Data Standards

### 3.1 Date/Time Format

**ISO 8601 with UTC timezone:**
```json
{
  "timestamp": "2025-10-08T15:32:10Z",
  "created_at": "2025-10-08T15:32:10.123Z"
}
```

### 3.2 Units of Measure

**UCUM (Unified Code for Units of Measure):**
- Hemoglobin: `g/dL`
- MCV: `fL`
- WBC: `10*3/uL` (thousands per microliter)
- Ferritin: `ng/mL`

### 3.3 Identifiers

**UUID v4** for all IDs:
```json
{
  "order_id": "550e8400-e29b-41d4-a716-446655440000",
  "case_id": "6fa459ea-ee8a-3ca4-894e-db77e160355e",
  "trace_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"
}
```

**External IDs** (from LIS/HIS):
```json
{
  "external_order_id": "ORD-2025-001234",
  "patient_external_id": "PAT-HOSP-001-456789"
}
```

### 3.4 LOINC Codes

All CBC parameters mapped to LOINC codes (see SRS-001 Data Dictionary):
```json
{
  "loinc_code": "718-7",
  "loinc_display": "Hemoglobin [Mass/volume] in Blood"
}
```

---

## 4. Common Schemas

### 4.1 CBC Data

**Used by:** Ingestion, Validation, Rules Engine, HemoAI

```yaml
CBCData:
  type: object
  required: [order_id, patient, hemogram]
  properties:
    order_id:
      type: string
      format: uuid
      example: "550e8400-e29b-41d4-a716-446655440000"
    patient:
      $ref: '#/components/schemas/PatientProfile'
    hemogram:
      $ref: '#/components/schemas/Hemogram'
    complementary:
      $ref: '#/components/schemas/ComplementaryTests'
```

### 4.2 Analysis Result

**Used by:** Rules Engine, HemoAI, Alert Orchestrator, UI

```yaml
AnalysisResult:
  type: object
  required: [case_id, timestamp, risk_score, recommendations, confidence]
  properties:
    case_id:
      type: string
      format: uuid
    timestamp:
      type: string
      format: date-time
    risk_score:
      type: number
      minimum: 0
      maximum: 1
      description: Overall risk score (0-1 scale)
    recommendations:
      type: array
      items:
        $ref: '#/components/schemas/Recommendation'
    clinical_rationale:
      type: string
      description: Human-readable explanation
    confidence:
      type: number
      minimum: 0
      maximum: 1
    model_version:
      type: string
      example: "hemoai-v1.2.3"
    rules_version:
      type: string
      example: "rules-v2.3.1"
    trace_id:
      type: string
      format: uuid
```

### 4.3 Alert

**Used by:** Alert Orchestrator, UI, Audit

```yaml
Alert:
  type: object
  required: [alert_id, level, case_id, message, triggered_at]
  properties:
    alert_id:
      type: string
      format: uuid
    level:
      type: string
      enum: [CRITICAL, HIGH, MEDIUM, LOW]
    case_id:
      type: string
      format: uuid
    message:
      type: string
      maxLength: 500
    suggested_actions:
      type: array
      items:
        type: string
    triggered_at:
      type: string
      format: date-time
    acknowledged:
      type: boolean
      default: false
    acknowledged_by:
      type: string
    acknowledged_at:
      type: string
      format: date-time
```

---

## 5. Traceability

### 5.1 Requirements Mapping

All API endpoints trace to requirements in SRS-001:

| Endpoint | Requirement | Description |
|----------|-------------|-------------|
| `POST /api/v1/cbc/analyze` | REQ-HD-001 | Submit CBC for analysis |
| `GET /api/v1/results/{case_id}` | REQ-HD-003 | Retrieve analysis results |
| `GET /api/v1/audit/{case_id}` | REQ-HD-004 | Retrieve audit trail |
| `POST /api/v1/alerts` | REQ-HD-001 | Generate clinical alerts |
| `GET /api/v1/models/{version}` | NFR-002 | Model versioning |

### 5.2 IEC 62304 Compliance

All Class C endpoints:
- **Authentication required** (JWT with `clinical_analysis` scope)
- **Input validation** (JSON Schema)
- **Audit logging** (all requests logged to Audit Service)
- **Error handling** (RFC 7807 compliant)
- **Timeouts enforced** (5s for Class C calls)

---

## 6. Testing Strategy

### 6.1 Contract Testing

**Tools:** Postman, Swagger UI, Pact

**Test scenarios:**
- Valid requests with all required fields
- Invalid requests (missing fields, wrong types, out-of-range values)
- Authentication/authorization failures
- Rate limiting enforcement
- Idempotency verification

### 6.2 Security Testing

**OWASP ASVS Level 2 compliance:**
- SQL injection (parameterized queries)
- XSS (output encoding)
- CSRF (token validation)
- Broken authentication (JWT validation)
- Sensitive data exposure (TLS 1.3 only)

### 6.3 Performance Testing

**Load testing with Gatling/JMeter:**
- Target: 100 concurrent users
- API Gateway: P95 <500ms
- Class C endpoints: P95 <2s (per NFR-001)
- Rate limit enforcement under load

---

## 7. Monitoring & Observability

### 7.1 Metrics (Prometheus)

**Per-endpoint metrics:**
- `http_requests_total` (counter, by endpoint/status)
- `http_request_duration_seconds` (histogram, P50/P95/P99)
- `http_requests_in_flight` (gauge)

**Class C specific:**
- `classc_boundary_calls_total` (counter, by source/destination)
- `classc_response_time_seconds` (histogram)
- `classc_circuit_breaker_state` (gauge)

### 7.2 Distributed Tracing

**OpenTelemetry + Jaeger:**
- Trace ID propagated via `X-Trace-ID` header
- Spans created for each service call
- Critical Class C calls tagged with `safety_class=C`

### 7.3 Logging

**Structured JSON logs:**
```json
{
  "timestamp": "2025-10-08T15:32:10Z",
  "level": "INFO",
  "service": "rules-engine",
  "trace_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
  "user_id": "user123",
  "endpoint": "POST /api/internal/rules",
  "status": 200,
  "latency_ms": 145,
  "safety_class": "C"
}
```

---

## 8. Changelog

### Version 1.0 (2025-10-08)

**Initial release:**
- 9 OpenAPI 3.1 specifications (REST APIs)
- 1 AsyncAPI 2.6 specification (async events)
- Master index document (this file)
- Common schemas and error handling
- Security, versioning, and testing strategies

**Coverage:**
- 100% of endpoints from SDD-001 v1.1
- All Class C endpoints explicitly marked
- Full traceability to SRS-001 requirements

---

## 9. Related Documents

- **SDD-001 v1.1:** Software Design Document (architecture reference)
- **SRS-001 v1.1:** Software Requirements Specification (functional requirements)
- **TRC-001 v1.0:** Traceability Matrix (requirement → design → test)
- **VVP-001:** Verification & Validation Plan (API testing strategy)
- **SEC-001:** Cybersecurity Plan (SBOM, threat model, CVD)

---

## 10. Next Steps

1. Review API specs with development teams
2. Generate Postman collections from OpenAPI specs
3. Set up automated contract testing in CI/CD
4. Implement API versioning in API Gateway (Kong/Nginx)
5. Deploy Swagger UI for API documentation portal
6. Conduct security audit of Class C endpoints
7. Submit to ANVISA reviewers with SDD-001 v1.1

---

**END OF DOCUMENT**
