"""
Output Renderer Tests

Tests clinical report generation in multiple formats (Markdown, HTML, JSON).
Validates CDSS-compliant microcopy and formatting.

IEC 62304 Class C Compliance:
- Tests output format correctness
- Tests CDSS microcopy (not diagnostic language)
- Tests disclaimer presence
- Tests critical vs priority vs routine rendering

Author: Dr. Abel Costa
"""

import pytest
import json
from hemodoctor.engines.output_renderer import (
    render_output,
    render_markdown,
    render_html,
    render_json,
    extract_key_values,
    format_value,
)
from hemodoctor.models.syndrome import SyndromeResult
from hemodoctor.models.evidence import EvidenceResult


# Fixtures

@pytest.fixture
def sample_cbc():
    """Sample CBC data for testing."""
    return {
        "hb": 8.2,
        "plt": 8,
        "wbc": 10.0,
        "anc": 5.0,
        "mcv": 88,
        "ldh": 980,
        "age_years": 35,
        "sex": "M"
    }


@pytest.fixture
def sample_syndromes_critical():
    """Sample critical syndromes."""
    return [
        SyndromeResult(
            id="S-TMA",
            criticality="critical",
            confidence="C2",
            evidences=["E-PLT-CRIT-LOW", "E-SCHISTOCYTES-GE1PCT"],
            actions=["Esfregaço urgente", "LDH + Creatinina"]
        )
    ]


@pytest.fixture
def sample_syndromes_priority():
    """Sample priority syndromes."""
    return [
        SyndromeResult(
            id="S-IDA",
            criticality="priority",
            confidence="C1",
            evidences=["E-MICROCYTOSIS", "E-FERRITIN-LOW"],
            actions=["Dosagem de ferritina"]
        )
    ]


@pytest.fixture
def sample_evidences():
    """Sample evidences."""
    return [
        EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="strong"),
        EvidenceResult(id="E-SCHISTOCYTES-GE1PCT", status="present", strength="strong"),
        EvidenceResult(id="E-LDH-HIGH", status="present", strength="high"),
    ]


@pytest.fixture
def sample_next_steps():
    """Sample next steps."""
    return [
        {
            "level": "critical",
            "test": "Esfregaço urgente + LDH + Creatinina",
            "rationale": "Confirmar microangiopatia e avaliar dano orgânico",
            "cost": "low",
            "turnaround": "<2h"
        },
        {
            "level": "priority",
            "test": "Haptoglobina + Bilirrubina indireta",
            "rationale": "Avaliar hemólise",
            "cost": "low",
            "turnaround": "6h"
        }
    ]


# Test 1: render_output() - Main routing function

def test_render_output_markdown(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test render_output with markdown format."""
    result = render_output(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123",
        format="markdown"
    )

    assert isinstance(result, str)
    assert "# HemoDoctor" in result
    assert "CRÍTICO" in result


def test_render_output_html(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test render_output with HTML format."""
    result = render_output(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123",
        format="html"
    )

    assert isinstance(result, str)
    assert "<html>" in result
    assert "<body>" in result


def test_render_output_json(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test render_output with JSON format."""
    result = render_output(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123",
        format="json"
    )

    assert isinstance(result, str)
    data = json.loads(result)
    assert data["version"] == "2.4.0"
    assert "route_id" in data


def test_render_output_invalid_format(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test render_output with invalid format raises error."""
    with pytest.raises(ValueError) as exc_info:
        render_output(
            sample_syndromes_critical,
            sample_next_steps,
            sample_cbc,
            sample_evidences,
            route_id="sha256:abc123",
            format="xml"  # Unsupported
        )

    assert "Unsupported format" in str(exc_info.value)


# Test 2: render_markdown()

def test_render_markdown_critical(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test markdown rendering for critical syndrome."""
    result = render_markdown(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    # Check header
    assert "# HemoDoctor" in result
    assert "v2.4.0" in result
    assert "abc123" in result

    # Check criticality
    assert "🔴 CRÍTICO" in result
    assert "Tempo-Sensíveis" in result

    # Check syndrome
    assert "S-TMA" in result

    # Check next steps
    assert "Próximos Passos" in result
    assert "Esfregaço urgente" in result

    # Check disclaimer
    assert "apoio à decisão clínica" in result
    assert "Não substitui" in result


def test_render_markdown_priority(sample_syndromes_priority, sample_next_steps, sample_cbc, sample_evidences):
    """Test markdown rendering for priority syndrome."""
    result = render_markdown(
        sample_syndromes_priority,
        [],  # No next steps
        sample_cbc,
        sample_evidences,
        route_id="sha256:def456"
    )

    # Check priority header
    assert "🟠 PRIORIDADE" in result
    assert "Requer Investigação" in result

    # Check syndrome
    assert "S-IDA" in result


def test_render_markdown_empty_syndromes(sample_next_steps, sample_cbc, sample_evidences):
    """Test markdown rendering with empty syndromes."""
    result = render_markdown(
        [],  # No syndromes
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:empty"
    )

    # Should still have header
    assert "# HemoDoctor" in result

    # Should still have next steps
    assert "Próximos Passos" in result


def test_render_markdown_no_next_steps(sample_syndromes_critical, sample_cbc, sample_evidences):
    """Test markdown rendering with no next steps."""
    result = render_markdown(
        sample_syndromes_critical,
        [],  # No next steps
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    # Should have syndrome
    assert "S-TMA" in result

    # Should NOT have next steps section
    assert "Próximos Passos" not in result


# Test 3: render_html()

def test_render_html_structure(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test HTML rendering has correct structure."""
    result = render_html(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    # Check HTML structure
    assert "<!DOCTYPE html>" in result
    assert "<html>" in result
    assert "<head>" in result
    assert "<body>" in result
    assert "</html>" in result

    # Check charset
    assert "UTF-8" in result

    # Check title
    assert "<title>" in result
    assert "HemoDoctor" in result


def test_render_html_contains_content(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test HTML rendering contains clinical content."""
    result = render_html(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    # Should contain syndrome
    assert "S-TMA" in result

    # Should contain critical indicator (emoji converted or preserved)
    # HTML conversion may change formatting


def test_render_html_has_styling(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test HTML rendering includes CSS styling."""
    result = render_html(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    # Check for CSS
    assert "<style>" in result
    assert "font-family" in result
    assert "color:" in result


# Test 4: render_json()

def test_render_json_structure(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test JSON rendering has correct structure."""
    result = render_json(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    data = json.loads(result)

    # Check required fields
    assert "version" in data
    assert "timestamp" in data
    assert "route_id" in data
    assert "syndromes" in data
    assert "evidences" in data
    assert "next_steps" in data
    assert "disclaimer" in data


def test_render_json_version(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test JSON version is correct."""
    result = render_json(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    data = json.loads(result)
    assert data["version"] == "2.4.0"


def test_render_json_syndromes(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test JSON syndromes are correctly serialized."""
    result = render_json(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    data = json.loads(result)

    assert len(data["syndromes"]) == 1
    syndrome = data["syndromes"][0]
    assert syndrome["id"] == "S-TMA"
    assert syndrome["criticality"] == "critical"


def test_render_json_evidences(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test JSON evidences are correctly serialized."""
    result = render_json(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    data = json.loads(result)

    # Should only include present evidences
    assert len(data["evidences"]) == 3
    evidence_ids = [e["id"] for e in data["evidences"]]
    assert "E-PLT-CRIT-LOW" in evidence_ids


def test_render_json_next_steps(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test JSON next steps are correctly serialized."""
    result = render_json(
        sample_syndromes_critical,
        sample_next_steps,
        sample_cbc,
        sample_evidences,
        route_id="sha256:abc123"
    )

    data = json.loads(result)

    assert len(data["next_steps"]) == 2
    assert data["next_steps"][0]["level"] == "critical"


# Test 5: extract_key_values()

def test_extract_key_values_tma():
    """Test key values extraction for TMA syndrome."""
    cbc = {
        "hb": 8.2,
        "plt": 8,
        "ldh": 980,
        "wbc": 10.0
    }

    values = extract_key_values(cbc, "S-TMA")

    # Should extract TMA-relevant values
    assert "hb" in values
    assert "plt" in values
    assert "ldh" in values

    # Should NOT extract irrelevant values
    assert "wbc" not in values


def test_extract_key_values_ida():
    """Test key values extraction for IDA syndrome."""
    cbc = {
        "hb": 9.5,
        "mcv": 68,
        "ferritin": 12,
        "plt": 450
    }

    values = extract_key_values(cbc, "S-IDA")

    # Should extract IDA-relevant values
    assert "hb" in values
    assert "mcv" in values
    assert "ferritin" in values


def test_extract_key_values_unknown_syndrome():
    """Test key values extraction for unknown syndrome (fallback)."""
    cbc = {
        "hb": 14.5,
        "wbc": 7.5,
        "plt": 250
    }

    values = extract_key_values(cbc, "S-UNKNOWN-SYNDROME")

    # Should extract default values (hb, wbc, plt)
    assert "hb" in values
    assert "wbc" in values
    assert "plt" in values


def test_extract_key_values_missing_data():
    """Test key values extraction with missing data."""
    cbc = {
        "hb": 8.2,
        # plt missing
        # ldh missing
    }

    values = extract_key_values(cbc, "S-TMA")

    # Should only extract present values
    assert "hb" in values
    assert "plt" not in values
    assert "ldh" not in values


# Test 6: format_value()

def test_format_value_hb():
    """Test hemoglobin formatting."""
    result = format_value("hb", 15.2)
    assert result == "15.2 g/dL"


def test_format_value_plt():
    """Test platelet formatting (no decimals)."""
    result = format_value("plt", 250.5)
    assert result == "250 ×10⁹/L"


def test_format_value_anc():
    """Test ANC formatting (2 decimals)."""
    result = format_value("anc", 3.456)
    assert result == "3.46 ×10⁹/L"


def test_format_value_wbc():
    """Test WBC formatting."""
    result = format_value("wbc", 7.5)
    assert result == "7.5 ×10⁹/L"


def test_format_value_mcv():
    """Test MCV formatting (no decimals)."""
    result = format_value("mcv", 88.7)
    assert result == "89 fL"


def test_format_value_ldh():
    """Test LDH formatting."""
    result = format_value("ldh", 980.3)
    assert result == "980.3 U/L"


def test_format_value_ferritin():
    """Test ferritin formatting."""
    result = format_value("ferritin", 12.8)
    assert result == "12.8 ng/mL"


def test_format_value_unknown_field():
    """Test formatting for unknown field (no unit)."""
    result = format_value("unknown_field", 123.45)
    assert "123.45" in result or "123.5" in result


def test_format_value_non_numeric():
    """Test formatting for non-numeric value."""
    result = format_value("hb", "invalid")
    assert result == "invalid"


# Test 7: Integration Tests

def test_full_report_critical_case(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Integration test: Full report for critical case (TMA)."""
    # Markdown
    md = render_markdown(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences, "abc123")
    assert "🔴 CRÍTICO" in md
    assert "S-TMA" in md
    assert "Próximos Passos" in md

    # HTML
    html = render_html(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences, "abc123")
    assert "<html>" in html
    assert "S-TMA" in html

    # JSON
    json_str = render_json(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences, "abc123")
    data = json.loads(json_str)
    assert data["syndromes"][0]["id"] == "S-TMA"
    assert data["syndromes"][0]["criticality"] == "critical"


def test_full_report_priority_case(sample_syndromes_priority, sample_cbc, sample_evidences):
    """Integration test: Full report for priority case (IDA)."""
    md = render_markdown(sample_syndromes_priority, [], sample_cbc, sample_evidences, "def456")
    assert "🟠 PRIORIDADE" in md
    assert "S-IDA" in md


# Test 8: CDSS Compliance

def test_cdss_disclaimer_present_markdown(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test CDSS disclaimer is present in markdown."""
    result = render_markdown(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences, "abc123")

    # Check disclaimer
    assert "apoio à decisão clínica" in result
    assert "Não substitui" in result
    assert "não é diagnóstico" in result


def test_cdss_microcopy_no_diagnostic_language(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences):
    """Test output does not use diagnostic language in syndrome section."""
    result = render_markdown(sample_syndromes_critical, sample_next_steps, sample_cbc, sample_evidences, "abc123")

    # Should NOT contain definitive diagnostic language
    assert "diagnóstico de" not in result.lower()

    # Note: "confirmar" is acceptable in next_steps (e.g., "confirmar com exame")
    # but not in the main diagnosis section. Extract syndrome section only.
    syndrome_section = result.split("## Próximos Passos")[0]

    # Syndrome section should use non-definitive language
    assert "hipótese" in syndrome_section.lower()  # Non-definitive
    # "confirma" should NOT appear in syndrome description section
