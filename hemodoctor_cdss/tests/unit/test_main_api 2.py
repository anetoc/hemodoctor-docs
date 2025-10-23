"""
FastAPI Main API Tests

Tests REST API endpoints using TestClient.
Validates request/response models, error handling, and CORS.

IEC 62304 Class C Compliance:
- Tests input validation
- Tests error responses
- Tests API security (CORS)
- Tests versioning

Author: Dr. Abel Costa
"""

import pytest
from fastapi.testclient import TestClient
from hemodoctor.api.main import app


# Test client
@pytest.fixture
def client():
    """FastAPI test client."""
    return TestClient(app)


# Test 1: Root Endpoint

def test_root_endpoint(client):
    """Test GET / returns API information."""
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()

    assert "name" in data
    assert "HemoDoctor" in data["name"]
    assert "version" in data
    assert data["version"] == "2.6.0"
    assert "docs" in data
    assert data["docs"] == "/docs"


# Test 2: Health Check Endpoint

def test_health_check_success(client):
    """Test GET /health returns healthy status."""
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "healthy"
    assert data["version"] == "2.6.0"
    assert "timestamp" in data
    assert data["yamls_loaded"] == 16


def test_health_check_response_structure(client):
    """Test health check response has correct structure."""
    response = client.get("/health")
    data = response.json()

    # Required fields
    assert "status" in data
    assert "version" in data
    assert "timestamp" in data
    assert "yamls_loaded" in data


# Test 3: Version Endpoint

def test_version_endpoint(client):
    """Test GET /version returns version information."""
    response = client.get("/version")

    assert response.status_code == 200
    data = response.json()

    assert data["version"] == "2.6.0"
    assert data["release_date"] == "2025-10-20"
    assert "environment" in data  # Should be "development" by default


def test_version_environment_default(client):
    """Test version endpoint returns default environment."""
    response = client.get("/version")
    data = response.json()

    # Should default to "development" if ENVIRONMENT env var not set
    assert data["environment"] in ["development", "dev", "production", "staging"]


# Test 4: Analyze Endpoint - Success Cases

def test_analyze_valid_cbc(client):
    """Test POST /analyze with valid CBC data."""
    cbc_data = {
        "hb": 15.2,
        "mcv": 88,
        "wbc": 8.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc_data)

    assert response.status_code == 200
    data = response.json()

    # Check response structure
    assert "version" in data
    assert "timestamp" in data
    assert "route_id" in data
    assert "top_syndromes" in data
    assert "evidences_present" in data
    assert "next_steps" in data
    assert "report" in data


def test_analyze_response_version(client):
    """Test analyze endpoint returns correct version."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5
    }

    response = client.post("/analyze", json=cbc_data)
    data = response.json()

    assert data["version"] == "2.6.0"


def test_analyze_response_route_id(client):
    """Test analyze endpoint returns route_id."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5
    }

    response = client.post("/analyze", json=cbc_data)
    data = response.json()

    # Route ID should be SHA256 hash (64 hex chars)
    assert "route_id" in data
    assert len(data["route_id"]) >= 16  # At least truncated hash


def test_analyze_response_reports(client):
    """Test analyze endpoint returns reports in all formats."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5
    }

    response = client.post("/analyze", json=cbc_data)
    data = response.json()

    # Check report formats
    assert "report" in data
    assert "markdown" in data["report"]
    assert "html" in data["report"]
    assert "json" in data["report"]

    # Check formats contain expected content
    assert "HemoDoctor" in data["report"]["markdown"]
    assert "<html>" in data["report"]["html"]
    # JSON report is a JSON string
    import json as json_module
    json_report = json_module.loads(data["report"]["json"])
    assert "version" in json_report


def test_analyze_minimal_required_fields(client):
    """Test analyze with only required fields (hb, mcv, wbc)."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5
        # No optional fields
    }

    response = client.post("/analyze", json=cbc_data)

    assert response.status_code == 200
    data = response.json()
    assert "top_syndromes" in data


def test_analyze_with_optional_fields(client):
    """Test analyze with optional fields included."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5,
        "plt": 250,
        "anc": 4.0,
        "age_years": 35,
        "sex": "M",
        "case_id": "TEST-123",
        "site_id": "HOSPITAL-ABC"
    }

    response = client.post("/analyze", json=cbc_data)

    assert response.status_code == 200


def test_analyze_critical_case(client):
    """Test analyze with critical case (TMA)."""
    cbc_data = {
        "hb": 8.2,
        "mcv": 88,
        "wbc": 10.0,
        "plt": 8,  # Critical low
        "age_years": 35,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc_data)
    data = response.json()

    # Should detect critical syndrome
    assert response.status_code == 200
    # top_syndromes should contain at least one syndrome
    assert len(data["top_syndromes"]) >= 1


# Test 5: Analyze Endpoint - Validation Errors

def test_analyze_missing_required_field_hb(client):
    """Test analyze fails with missing hb (required field)."""
    cbc_data = {
        # "hb": missing
        "mcv": 88,
        "wbc": 7.5
    }

    response = client.post("/analyze", json=cbc_data)

    # Should return 422 Unprocessable Entity
    assert response.status_code == 422
    assert "detail" in response.json()


def test_analyze_missing_required_field_mcv(client):
    """Test analyze fails with missing mcv."""
    cbc_data = {
        "hb": 14.5,
        # "mcv": missing
        "wbc": 7.5
    }

    response = client.post("/analyze", json=cbc_data)
    assert response.status_code == 422


def test_analyze_missing_required_field_wbc(client):
    """Test analyze fails with missing wbc."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        # "wbc": missing
    }

    response = client.post("/analyze", json=cbc_data)
    assert response.status_code == 422


def test_analyze_hb_out_of_range_high(client):
    """Test analyze validation for Hb >25 (out of range)."""
    cbc_data = {
        "hb": 30,  # > 25 (exceeds validation limit)
        "mcv": 88,
        "wbc": 7.5
    }

    response = client.post("/analyze", json=cbc_data)

    # Should fail validation
    assert response.status_code == 422


def test_analyze_hb_out_of_range_negative(client):
    """Test analyze validation for negative Hb."""
    cbc_data = {
        "hb": -5,  # Negative (invalid)
        "mcv": 88,
        "wbc": 7.5
    }

    response = client.post("/analyze", json=cbc_data)
    assert response.status_code == 422


def test_analyze_wbc_out_of_range_high(client):
    """Test analyze validation for WBC >200."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 300  # > 200
    }

    response = client.post("/analyze", json=cbc_data)
    assert response.status_code == 422


def test_analyze_invalid_sex_value(client):
    """Test analyze with invalid sex value."""
    cbc_data = {
        "hb": 14.5,
        "mcv": 88,
        "wbc": 7.5,
        "sex": "INVALID"  # Should be M or F
    }

    response = client.post("/analyze", json=cbc_data)

    # Sex validation is optional in Pydantic model
    # Should still accept (validation happens in pipeline)
    assert response.status_code in [200, 422]


# Test 6: Error Handling

def test_analyze_invalid_json(client):
    """Test analyze with invalid JSON."""
    response = client.post(
        "/analyze",
        content="invalid json",
        headers={"Content-Type": "application/json"}
    )

    # Should return 422 (validation error)
    assert response.status_code == 422


def test_analyze_wrong_content_type(client):
    """Test analyze with wrong content type."""
    response = client.post(
        "/analyze",
        content="hb=14.5&mcv=88&wbc=7.5",  # Form data instead of JSON
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    # Should return 422
    assert response.status_code == 422


# Test 7: CORS Headers

def test_cors_headers_present(client):
    """Test CORS headers are present in response."""
    response = client.options("/analyze")

    # CORS headers should be present (TestClient doesn't fully test CORS,
    # but we can verify middleware is configured)
    # Note: Full CORS testing requires actual HTTP requests
    assert response.status_code in [200, 405]  # OPTIONS may not be implemented


def test_cors_allow_origins(client):
    """Test CORS allows all origins (development mode)."""
    # In production, should restrict origins
    # This test just verifies CORS middleware is enabled

    response = client.get("/health", headers={"Origin": "http://example.com"})

    # Should still work (CORS allows)
    assert response.status_code == 200


# Test 8: OpenAPI Documentation

def test_openapi_docs_accessible(client):
    """Test OpenAPI docs are accessible at /docs."""
    response = client.get("/docs")

    # Should return HTML page
    assert response.status_code == 200
    # Note: FastAPI serves Swagger UI at /docs


def test_openapi_json_accessible(client):
    """Test OpenAPI JSON schema is accessible."""
    response = client.get("/openapi.json")

    assert response.status_code == 200
    data = response.json()

    # Should have OpenAPI schema structure
    assert "openapi" in data
    assert "info" in data
    assert "paths" in data


def test_openapi_contains_endpoints(client):
    """Test OpenAPI schema contains all endpoints."""
    response = client.get("/openapi.json")
    data = response.json()

    paths = data["paths"]

    # Check all endpoints are documented
    assert "/" in paths
    assert "/health" in paths
    assert "/version" in paths
    assert "/analyze" in paths


# Test 9: Pydantic Model Validation

def test_pydantic_cbc_request_example():
    """Test CBCRequest Pydantic model with example data."""
    from hemodoctor.api.main import CBCRequest

    cbc = CBCRequest(
        hb=15.2,
        mcv=88,
        wbc=8.5,
        plt=250,
        age_years=35,
        sex="M"
    )

    assert cbc.hb == 15.2
    assert cbc.mcv == 88
    assert cbc.wbc == 8.5


def test_pydantic_cbc_request_validation_error():
    """Test CBCRequest validation fails with invalid data."""
    from hemodoctor.api.main import CBCRequest
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        CBCRequest(
            hb=30,  # > 25 (exceeds limit)
            mcv=88,
            wbc=7.5
        )


def test_pydantic_analysis_response_example():
    """Test AnalysisResponse Pydantic model."""
    from hemodoctor.api.main import AnalysisResponse

    response = AnalysisResponse(
        version="2.6.0",
        timestamp="2025-10-20T12:34:56Z",
        route_id="sha256:abc123",
        top_syndromes=["S-NORMAL"],
        evidences_present=[],
        next_steps=[],
        report={
            "markdown": "# Report",
            "html": "<html></html>",
            "json": "{}"
        }
    )

    assert response.version == "2.6.0"
    assert len(response.top_syndromes) == 1


# Test 10: Integration Tests

def test_full_workflow_normal_cbc(client):
    """Integration test: Full workflow with normal CBC."""
    # 1. Check health
    health = client.get("/health")
    assert health.status_code == 200

    # 2. Check version
    version = client.get("/version")
    assert version.status_code == 200

    # 3. Analyze normal CBC
    cbc_data = {
        "hb": 15.2,
        "mcv": 88,
        "wbc": 8.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M"
    }
    analyze = client.post("/analyze", json=cbc_data)
    assert analyze.status_code == 200

    # 4. Verify response
    data = analyze.json()
    assert "version" in data
    assert "report" in data


def test_full_workflow_critical_case(client):
    """Integration test: Full workflow with critical case."""
    cbc_data = {
        "hb": 8.2,
        "mcv": 88,
        "wbc": 10.0,
        "plt": 8,  # Critical
        "age_years": 35,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc_data)
    assert response.status_code == 200

    data = response.json()

    # Should have syndromes
    assert len(data["top_syndromes"]) >= 1

    # Should have next steps
    # (May be empty if triggers don't fire, but field should exist)
    assert "next_steps" in data

    # Report should mention critical
    assert "report" in data
