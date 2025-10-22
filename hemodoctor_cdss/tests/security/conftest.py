"""
Security Tests - Shared Fixtures

Provides test clients and malicious payload generators for security testing.

Author: Dr. Abel Costa
"""

import pytest
from fastapi.testclient import TestClient
from hemodoctor.api.main import app


@pytest.fixture
def client():
    """FastAPI test client for security testing."""
    return TestClient(app)


@pytest.fixture
def malicious_payloads():
    """Common malicious payloads for security testing."""
    return {
        "sql_injection": [
            "' OR '1'='1",
            "'; DROP TABLE users--",
            "1' UNION SELECT NULL--",
            "admin'--",
            "' OR 1=1--",
            "1; DELETE FROM cases WHERE 1=1--",
        ],
        "xss": [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "javascript:alert('XSS')",
            "<svg onload=alert('XSS')>",
            "';alert(String.fromCharCode(88,83,83))//",
        ],
        "path_traversal": [
            "../../../etc/passwd",
            "..\\..\\..\\windows\\system32\\config\\sam",
            "....//....//....//etc/passwd",
            "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd",
        ],
        "command_injection": [
            "; ls -la",
            "| cat /etc/passwd",
            "`whoami`",
            "$(whoami)",
            "&& rm -rf /",
        ],
        "nosql_injection": [
            "{'$ne': null}",
            "{'$gt': ''}",
            "admin' || 'a'='a",
        ],
        "ldap_injection": [
            "*",
            "admin)(&(password=*))",
            "admin)(|(password=*))",
        ],
        "xml_injection": [
            "<?xml version='1.0'?><!DOCTYPE foo [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]><foo>&xxe;</foo>",
        ],
    }


@pytest.fixture
def extreme_values():
    """Extreme/edge case values for testing."""
    return {
        "very_large_numbers": [
            999999999999999999,
            1e308,  # Near float max
            float('inf'),
        ],
        "very_small_numbers": [
            -999999999999999999,
            1e-308,
            float('-inf'),
        ],
        "zero_variations": [
            0,
            -0,
            0.0,
            -0.0,
        ],
        "special_floats": [
            float('nan'),
            float('inf'),
            float('-inf'),
        ],
        "very_long_strings": [
            "A" * 10000,
            "A" * 100000,
            "A" * 1000000,
        ],
        "unicode_edge_cases": [
            "\u0000",  # Null character
            "\uFFFF",  # Special character
            "测试",  # Chinese
            "أختبار",  # Arabic
            "🔥" * 1000,  # Emojis
        ],
    }


@pytest.fixture
def valid_cbc_data():
    """Valid CBC data for baseline testing."""
    return {
        "hb": 15.2,
        "mcv": 88,
        "wbc": 8.5,
        "plt": 250,
        "age_years": 35,
        "sex": "M",
        "case_id": "TEST-001",
        "site_id": "HOSPITAL-ABC"
    }
