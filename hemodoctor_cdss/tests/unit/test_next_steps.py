"""
Next Steps Engine Tests

Tests clinical next steps prioritization and formatting.

IEC 62304 Class C Compliance:
- Tests trigger evaluation
- Tests prioritization logic
- Tests output formatting

Author: Dr. Abel Costa
"""

import pytest
from hemodoctor.engines.next_steps import (
    evaluate_trigger_condition,
    format_next_steps,
    count_by_level,
    prioritize_suggestions,
)
from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.models.syndrome import SyndromeResult


# Test 1: evaluate_trigger_condition - Empty Condition


def test_evaluate_trigger_condition_empty():
    """Test evaluate_trigger_condition with empty condition."""
    context = {"evidences": []}

    # Empty string condition should return False
    result = evaluate_trigger_condition("", context)
    assert result is False

    # None condition should return False
    result = evaluate_trigger_condition(None, context)
    assert result is False


def test_evaluate_trigger_condition_valid():
    """Test evaluate_trigger_condition with valid condition."""
    context = {
        "test_var": True,
        "value": 10
    }

    # Simple boolean condition
    condition = "test_var == True and value > 5"
    result = evaluate_trigger_condition(condition, context)

    assert result is True


def test_evaluate_trigger_condition_false():
    """Test evaluate_trigger_condition that evaluates to False."""
    evidences = [
        EvidenceResult(id="E-PLT-CRIT-LOW", status="present", strength="critical", requires=[])
    ]

    context = {"evidences": evidences}

    # Should evaluate to False
    condition = "'E-ANC-CRIT' in [e.id for e in evidences]"
    result = evaluate_trigger_condition(condition, context)

    assert result is False


def test_evaluate_trigger_condition_error():
    """Test evaluate_trigger_condition handles errors gracefully."""
    context = {}

    # Invalid condition (undefined variable)
    condition = "undefined_variable == True"
    result = evaluate_trigger_condition(condition, context)

    # Should return False on error (fail-safe)
    assert result is False


# Test 2: format_next_steps


def test_format_next_steps_empty():
    """Test format_next_steps with empty list."""
    config = {"templates": {}}

    output = format_next_steps([], config)

    assert "Nenhum próximo passo recomendado" in output


def test_format_next_steps_single_critical():
    """Test format_next_steps with single critical step."""
    next_steps = [
        {
            "level": "critical",
            "test": "Hemograma em 6h",
            "rationale": "PLT crítica (<20)",
            "cost": "low",
            "turnaround": "<6h"
        }
    ]

    config = {"templates": {}}

    output = format_next_steps(next_steps, config)

    assert "CRÍTICO" in output
    assert "Hemograma em 6h" in output
    assert "PLT crítica" in output
    assert "low" in output
    assert "<6h" in output


def test_format_next_steps_multiple_levels():
    """Test format_next_steps with multiple priority levels."""
    next_steps = [
        {
            "level": "critical",
            "test": "Test A",
            "rationale": "Critical reason",
            "cost": "low",
            "turnaround": "fast"
        },
        {
            "level": "priority",
            "test": "Test B",
            "rationale": "Priority reason",
            "cost": "mid",
            "turnaround": "medium"
        },
        {
            "level": "routine",
            "test": "Test C",
            "rationale": "Routine reason",
            "cost": "high",
            "turnaround": "slow"
        }
    ]

    config = {"templates": {}}

    output = format_next_steps(next_steps, config)

    assert "🔴 CRÍTICO" in output
    assert "🟠 PRIORIDADE" in output
    assert "🟢 ROTINA" in output
    assert "Test A" in output
    assert "Test B" in output
    assert "Test C" in output


def test_format_next_steps_with_prereq():
    """Test format_next_steps with prerequisite."""
    next_steps = [
        {
            "level": "priority",
            "test": "Blood culture",
            "rationale": "Suspected infection",
            "cost": "mid",
            "turnaround": "24h",
            "prereq": "Collect before antibiotics"
        }
    ]

    config = {"templates": {}}

    output = format_next_steps(next_steps, config)

    assert "Pré-requisito" in output
    assert "Collect before antibiotics" in output


def test_format_next_steps_without_rationale():
    """Test format_next_steps without rationale."""
    next_steps = [
        {
            "level": "routine",
            "test": "CBC follow-up",
            "cost": "low",
            "turnaround": "24h"
        }
    ]

    config = {"templates": {}}

    output = format_next_steps(next_steps, config)

    assert "CBC follow-up" in output
    # Should not crash without rationale


def test_format_next_steps_custom_templates():
    """Test format_next_steps with custom templates."""
    next_steps = [
        {
            "level": "critical",
            "test": "Test",
            "rationale": "Reason",
            "cost": "low",
            "turnaround": "fast"
        }
    ]

    config = {
        "templates": {
            "header": "### NEXT STEPS ({count} items)",
            "item": "{level} - {test}: {rationale}"
        }
    }

    output = format_next_steps(next_steps, config)

    assert "### NEXT STEPS (1 items)" in output


# Test 3: count_by_level


def test_count_by_level_empty():
    """Test count_by_level with empty list."""
    counts = count_by_level([])

    assert counts == {}


def test_count_by_level_single():
    """Test count_by_level with single step."""
    next_steps = [
        {"level": "critical", "test": "A"}
    ]

    counts = count_by_level(next_steps)

    assert counts == {"critical": 1}


def test_count_by_level_multiple():
    """Test count_by_level with multiple steps."""
    next_steps = [
        {"level": "critical", "test": "A"},
        {"level": "critical", "test": "B"},
        {"level": "priority", "test": "C"},
        {"level": "priority", "test": "D"},
        {"level": "priority", "test": "E"},
        {"level": "routine", "test": "F"}
    ]

    counts = count_by_level(next_steps)

    assert counts == {
        "critical": 2,
        "priority": 3,
        "routine": 1
    }


def test_count_by_level_default():
    """Test count_by_level with missing level (defaults to routine)."""
    next_steps = [
        {"test": "A"},  # No level specified
        {"level": "critical", "test": "B"}
    ]

    counts = count_by_level(next_steps)

    assert counts == {
        "routine": 1,
        "critical": 1
    }


# Test 4: prioritize_suggestions (basic coverage)


def test_prioritize_suggestions_basic():
    """Test prioritize_suggestions with basic config."""
    suggestions = [
        {"level": "critical", "test": "Test A", "cost": "low", "turnaround": "fast"}
    ]

    config = {"max_items": 8}

    result = prioritize_suggestions(suggestions, config)

    # Should return suggestions (function doesn't crash)
    assert isinstance(result, list)
