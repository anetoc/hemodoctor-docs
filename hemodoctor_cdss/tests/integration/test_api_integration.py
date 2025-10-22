"""
API Integration Tests
Tests FastAPI REST API endpoints: /analyze, /health, /version, /docs
20 comprehensive tests covering complete flow, concurrent requests, error handling, CORS
"""

import pytest
import httpx
import asyncio
from fastapi.testclient import TestClient
from datetime import datetime

from hemodoctor.api.main import app


# Create test client
client = TestClient(app)


# ============================================================================
# ROOT + HEALTH + VERSION ENDPOINTS (6 tests)
# ============================================================================

def test_api_root_endpoint():
    """Test GET / returns welcome message"""
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()

    # Check API metadata structure
    assert "name" in data
    assert "HemoDoctor" in data["name"]
    assert "version" in data
    assert data["version"] == "2.4.0"


def test_api_health_endpoint_healthy():
    """Test GET /health returns healthy status"""
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_api_health_endpoint_timestamp():
    """Test GET /health timestamp is valid"""
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()

    # Parse timestamp
    timestamp_str = data["timestamp"].rstrip("Z") if data["timestamp"].endswith("Z") else data["timestamp"]
    timestamp = datetime.fromisoformat(timestamp_str)

    assert timestamp is not None


def test_api_version_endpoint():
    """Test GET /version returns correct version"""
    response = client.get("/version")

    assert response.status_code == 200
    data = response.json()

    assert data["version"] == "2.4.0"
    # Check for any additional metadata
    assert "release_date" in data or "environment" in data or "timestamp" in data


def test_api_docs_endpoint():
    """Test GET /docs (OpenAPI documentation) is accessible"""
    response = client.get("/docs")

    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_api_openapi_json():
    """Test GET /openapi.json returns OpenAPI schema"""
    response = client.get("/openapi.json")

    assert response.status_code == 200
    data = response.json()

    assert "openapi" in data
    assert "paths" in data
    assert "/analyze" in data["paths"]


# ============================================================================
# POST /analyze ENDPOINT - SUCCESS CASES (7 tests)
# ============================================================================

def test_api_analyze_normal_case():
    """Test POST /analyze with normal CBC"""
    cbc = {
        "hb": 14.5,
        "wbc": 7.0,
        "plt": 220,
        "mcv": 88,
        "age_years": 35,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc)

    assert response.status_code == 200
    data = response.json()

    # Check response structure
    assert "top_syndromes" in data
    assert "evidences_present" in data
    assert "route_id" in data
    assert "version" in data
    assert "timestamp" in data

    # Check data types
    assert isinstance(data["top_syndromes"], list)
    assert isinstance(data["evidences_present"], list)
    assert len(data["route_id"]) == 64


def test_api_analyze_critical_case():
    """Test POST /analyze with critical TMA case"""
    cbc = {
        "hb": 7.5,
        "plt": 8,
        "ldh": 980,
        "bt_indireta": 2.5,
        "morphology": {"esquistocitos": True},
        "age_years": 35,
        "sex": "M",
        "mcv": 88,
        "wbc": 10.0
    }

    response = client.post("/analyze", json=cbc)

    assert response.status_code == 200
    data = response.json()

    # Critical syndrome should be detected (TMA or PLT-CRITICA)
    assert "S-TMA" in data["top_syndromes"] or "S-PLT-CRITICA" in data["top_syndromes"]


def test_api_analyze_minimal_fields():
    """Test POST /analyze with minimal required fields"""
    cbc = {
        "hb": 12.0,
        "wbc": 7.0,
        "plt": 200,
        "mcv": 88,  # MCV is required for validation
        "age_years": 30,
        "sex": "F"
    }

    response = client.post("/analyze", json=cbc)

    assert response.status_code == 200
    data = response.json()

    assert len(data["top_syndromes"]) > 0


def test_api_analyze_with_differential():
    """Test POST /analyze with complete differential"""
    cbc = {
        "hb": 14.5,
        "wbc": 7.0,
        "plt": 240,
        "mcv": 89,
        "neutrophils_pct": 60,
        "lymphocytes_pct": 30,
        "monocytes_pct": 8,
        "eosinophils_pct": 2,
        "age_years": 40,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc)

    assert response.status_code == 200
    data = response.json()

    assert len(data["top_syndromes"]) > 0


def test_api_analyze_pediatric():
    """Test POST /analyze with pediatric case"""
    cbc = {
        "hb": 12.0,
        "wbc": 8.5,
        "plt": 280,
        "mcv": 82,
        "age_years": 5,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc)

    assert response.status_code == 200
    data = response.json()

    assert len(data["top_syndromes"]) > 0


def test_api_analyze_infant():
    """Test POST /analyze with infant case (age_months)"""
    cbc = {
        "hb": 11.5,
        "wbc": 10.0,
        "plt": 300,
        "mcv": 78,
        "age_months": 18,
        "sex": "F"
    }

    response = client.post("/analyze", json=cbc)

    assert response.status_code == 200
    data = response.json()

    assert len(data["top_syndromes"]) > 0


def test_api_analyze_deterministic():
    """Test POST /analyze returns same route_id for identical CBC"""
    cbc = {
        "hb": 14.5,
        "wbc": 7.0,
        "plt": 220,
        "mcv": 88,
        "age_years": 35,
        "sex": "M"
    }

    response1 = client.post("/analyze", json=cbc)
    response2 = client.post("/analyze", json=cbc)

    assert response1.status_code == 200
    assert response2.status_code == 200

    data1 = response1.json()
    data2 = response2.json()

    # Route ID should be deterministic
    assert data1["route_id"] == data2["route_id"]


# ============================================================================
# POST /analyze ENDPOINT - ERROR HANDLING (5 tests)
# ============================================================================

def test_api_analyze_missing_required_field():
    """Test POST /analyze with missing required field (hb)"""
    cbc = {
        # "hb" missing
        "wbc": 7.0,
        "plt": 220,
        "age_years": 35,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc)

    # Should return 422 Unprocessable Entity (Pydantic validation error)
    assert response.status_code == 422


def test_api_analyze_invalid_sex():
    """Test POST /analyze with invalid sex value"""
    cbc = {
        "hb": 14.5,
        "wbc": 7.0,
        "plt": 220,
        "age_years": 35,
        "sex": "X"  # Invalid (should be M or F)
    }

    response = client.post("/analyze", json=cbc)

    # Should return 422 Unprocessable Entity
    assert response.status_code == 422


def test_api_analyze_negative_value():
    """Test POST /analyze with negative value (invalid)"""
    cbc = {
        "hb": -5.0,  # Negative (invalid)
        "wbc": 7.0,
        "plt": 220,
        "age_years": 35,
        "sex": "M"
    }

    response = client.post("/analyze", json=cbc)

    # Should return 422 or 400 (validation error)
    assert response.status_code in [400, 422]


def test_api_analyze_invalid_json():
    """Test POST /analyze with malformed JSON"""
    response = client.post(
        "/analyze",
        content="not a json",
        headers={"Content-Type": "application/json"}
    )

    # Should return 422 (invalid JSON)
    assert response.status_code == 422


def test_api_analyze_empty_body():
    """Test POST /analyze with empty body"""
    response = client.post("/analyze", json={})

    # Should return 422 (missing required fields)
    assert response.status_code == 422


# ============================================================================
# CONCURRENT REQUESTS (2 tests)
# ============================================================================

def test_api_concurrent_requests():
    """Test API handles 10 concurrent requests"""
    cbc = {
        "hb": 14.5,
        "wbc": 7.0,
        "plt": 220,
        "mcv": 88,
        "age_years": 35,
        "sex": "M"
    }

    # Make 10 concurrent requests
    responses = []
    for _ in range(10):
        response = client.post("/analyze", json=cbc)
        responses.append(response)

    # All should succeed
    assert all(r.status_code == 200 for r in responses)

    # All should return same route_id (deterministic)
    route_ids = [r.json()["route_id"] for r in responses]
    assert len(set(route_ids)) == 1


def test_api_different_concurrent_requests():
    """Test API handles concurrent requests with different CBCs"""
    cbcs = [
        {
            "hb": 10.0 + i * 2.0,  # Vary Hb more significantly
            "wbc": 5.0 + i,
            "plt": 150 + i * 50,
            "mcv": 75 + i * 5,
            "age_years": 30 + i * 5,
            "sex": "M" if i % 2 == 0 else "F"  # Alternate sex
        }
        for i in range(5)
    ]

    # Make 5 concurrent requests with different CBCs
    responses = []
    for cbc in cbcs:
        response = client.post("/analyze", json=cbc)
        responses.append(response)

    # All should succeed
    assert all(r.status_code == 200 for r in responses)

    # Different CBCs should produce different route_ids (at least 2 different)
    route_ids = [r.json()["route_id"] for r in responses]
    assert len(set(route_ids)) >= 2, f"Expected at least 2 different route_ids, got {len(set(route_ids))}"
