"""
Next Steps Engine - Clinical Recommendations Generator

Generates prioritized clinical next steps (tests, consultations) based on
detected syndromes and evidences. Implements intelligent prioritization.

Based on: 09_next_steps_engine_hybrid.yaml v2.3.1 (40 triggers)

Prioritization:
- Critical > Priority > Routine
- Tie-break: Cost (low > mid > high), then Turnaround (fast > medium > slow)
- Max 8 items in output
- Deduplication by test name

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from typing import List, Dict, Any
from simpleeval import SimpleEval, NameNotDefined, DEFAULT_NAMES
from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.models.syndrome import SyndromeResult
from hemodoctor.utils.yaml_parser import YAMLParser


def generate_next_steps(
    syndromes: List[SyndromeResult],
    evidences: List[EvidenceResult],
    cbc_data: Dict[str, Any],
    yaml_parser: YAMLParser
) -> List[Dict[str, Any]]:
    """
    Generate prioritized clinical next steps.

    Args:
        syndromes: List of detected syndromes
        evidences: List of evaluated evidences
        cbc_data: Original CBC data (for 'when' condition evaluation)
        yaml_parser: YAMLParser singleton instance

    Returns:
        List of next step recommendations (max 8, prioritized)

    Algorithm:
        1. Load 40 triggers from YAML
        2. Evaluate 'when' conditions using simpleeval (NEVER eval())
        3. Collect all suggestions from fired triggers
        4. Prioritize: Critical > Priority > Routine
        5. Tie-break: Low cost > Mid cost > High cost, then Fast > Medium > Slow
        6. Deduplicate by test name
        7. Return top 8

    Example:
        >>> syndromes = [SyndromeResult(id="S-TMA", criticality="critical", ...)]
        >>> evidences = [EvidenceResult(id="E-PLT-CRIT-LOW", status="present", ...)]
        >>> cbc = {"plt": 8, "ldh": 980}
        >>> next_steps = generate_next_steps(syndromes, evidences, cbc, parser)
        >>> len(next_steps) <= 8
        True
        >>> next_steps[0]["level"]
        'critical'
    """
    # Load next steps YAML
    next_steps_config = yaml_parser.next_steps

    # Get triggers
    triggers = next_steps_config.get("triggers", [])

    # Build context for 'when' evaluation
    # CRITICAL: Pass full object lists (not just IDs)
    # YAML triggers expect: evidences[0].id, evidences[0].status, etc.
    eval_context = {
        **cbc_data,  # Include all CBC fields (hb, plt, anc, etc.)
        "syndromes": syndromes,  # List of SyndromeResult objects
        "evidences": evidences,  # List of EvidenceResult objects
    }

    # Collect all suggestions from fired triggers
    all_suggestions = []

    for trigger in triggers:
        trigger_id = trigger.get("id", "unknown")
        when_condition = trigger.get("when", "")

        # Evaluate 'when' condition
        if evaluate_trigger_condition(when_condition, eval_context):
            # Trigger fired - collect suggestions
            suggestions = trigger.get("suggest", [])
            for suggestion in suggestions:
                # Add trigger metadata
                suggestion_with_meta = {
                    **suggestion,
                    "trigger_id": trigger_id,
                }
                all_suggestions.append(suggestion_with_meta)

    # Prioritize and deduplicate
    prioritized = prioritize_suggestions(all_suggestions, next_steps_config)

    # Return top 8
    max_items = next_steps_config.get("render", {}).get("max_items", 8)
    return prioritized[:max_items]


def evaluate_trigger_condition(condition: str, context: Dict[str, Any]) -> bool:
    """
    Safely evaluate trigger 'when' condition.

    Args:
        condition: Python expression (e.g., "hb < 6.5 and sex == 'M'")
        context: Dictionary with variables (CBC data, syndromes, evidences)

    Returns:
        bool: True if condition satisfied, False otherwise

    Safety:
        - Uses SimpleEval (NEVER eval())
        - Allows attribute access for Pydantic models (e.id, e.status)
        - Returns False on error (fail-safe)
        - Handles missing variables gracefully

    Example:
        >>> context = {"hb": 6.0, "sex": "M"}
        >>> evaluate_trigger_condition("hb < 6.5 and sex == 'M'", context)
        True
        >>> context = {"evidences": [EvidenceResult(id="E-ANC", status="present", strength="high")]}
        >>> evaluate_trigger_condition("'E-ANC' in [e.id for e in evidences]", context)
        True
    """
    if not condition:
        return False

    try:
        # Use SimpleEval (not simple_eval) to enable attribute access
        s = SimpleEval(names=context)

        # Enable attribute access for Pydantic models (e.id, e.status, etc.)
        # This allows: [e.id for e in evidences if e.status == 'present']
        s.ATTR_INDEX_FALLBACK = True

        result = s.eval(condition)
        return bool(result)
    except (NameNotDefined, KeyError, TypeError, ValueError, AttributeError):
        # Missing variable or evaluation error - fail-safe to False
        return False
    except Exception:
        # Unexpected error - fail-safe to False
        return False


def prioritize_suggestions(
    suggestions: List[Dict[str, Any]],
    config: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Prioritize and deduplicate suggestions.

    Args:
        suggestions: List of suggestion dictionaries
        config: Next steps configuration (prioritization rules)

    Returns:
        List of prioritized suggestions (deduplicated)

    Prioritization:
        1. Level: critical > priority > routine
        2. Cost: low > mid > high
        3. Turnaround: fast > medium > slow

    Deduplication:
        - Remove duplicates by test name
        - Keep highest priority instance

    Example:
        >>> suggestions = [
        ...     {"level": "critical", "test": "CBC", "cost": "low", "turnaround": "fast"},
        ...     {"level": "priority", "test": "CBC", "cost": "low", "turnaround": "fast"},
        ...     {"level": "critical", "test": "LDH", "cost": "mid", "turnaround": "medium"},
        ... ]
        >>> prioritized = prioritize_suggestions(suggestions, config)
        >>> len(prioritized)
        2
        >>> prioritized[0]["test"]
        'CBC'
    """
    # Define priority orders
    level_order = {"critical": 0, "priority": 1, "routine": 2}
    cost_order = {"low": 0, "mid": 1, "high": 2}
    turnaround_order = {"fast": 0, "medium": 1, "slow": 2}

    # Sort suggestions
    def sort_key(suggestion):
        level = suggestion.get("level", "routine")
        cost = suggestion.get("cost", "high")
        turnaround = suggestion.get("turnaround", "slow")

        return (
            level_order.get(level, 99),
            cost_order.get(cost, 99),
            turnaround_order.get(turnaround, 99),
        )

    sorted_suggestions = sorted(suggestions, key=sort_key)

    # Deduplicate by test name (keep first occurrence = highest priority)
    seen_tests = set()
    deduplicated = []

    for suggestion in sorted_suggestions:
        test_name = suggestion.get("test", "")
        if test_name and test_name not in seen_tests:
            seen_tests.add(test_name)
            deduplicated.append(suggestion)

    return deduplicated


def format_next_steps(next_steps: List[Dict[str, Any]], config: Dict[str, Any]) -> str:
    """
    Format next steps as human-readable markdown.

    Args:
        next_steps: List of next step dictionaries
        config: Next steps configuration (render templates)

    Returns:
        str: Markdown-formatted next steps

    Example:
        >>> next_steps = [
        ...     {
        ...         "level": "critical",
        ...         "test": "Reticulócitos",
        ...         "rationale": "Diferenciar regenerativa vs hiporregenerativa",
        ...         "cost": "mid",
        ...         "turnaround": "medium",
        ...         "prereq": "CBC"
        ...     }
        ... ]
        >>> output = format_next_steps(next_steps, config)
        >>> "CRÍTICO" in output or "critical" in output
        True
    """
    if not next_steps:
        return "Nenhum próximo passo recomendado."

    # Get templates
    templates = config.get("templates", {})
    header_template = templates.get("header", "## PRÓXIMOS PASSOS RECOMENDADOS ({count} exames)")
    item_template = templates.get("item", "{level} · {test} — {rationale}")

    # Build output
    lines = []
    lines.append(header_template.format(count=len(next_steps)))
    lines.append("")

    for i, step in enumerate(next_steps, 1):
        # Format level
        level = step.get("level", "routine")
        level_emoji = {
            "critical": "🔴 CRÍTICO",
            "priority": "🟠 PRIORIDADE",
            "routine": "🟢 ROTINA"
        }.get(level, level.upper())

        # Build item line
        item_line = f"{i}. **{level_emoji}** · {step.get('test', 'Exame não especificado')}"
        lines.append(item_line)

        # Add rationale
        rationale = step.get("rationale", "")
        if rationale:
            lines.append(f"   - **Motivo:** {rationale}")

        # Add cost/turnaround
        cost = step.get("cost", "N/A")
        turnaround = step.get("turnaround", "N/A")
        lines.append(f"   - **Custo:** {cost} | **Prazo:** {turnaround}")

        # Add prereq
        prereq = step.get("prereq", "")
        if prereq:
            lines.append(f"   - **Pré-requisito:** {prereq}")

        lines.append("")

    return "\n".join(lines)


def count_by_level(next_steps: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count next steps by priority level.

    Args:
        next_steps: List of next step dictionaries

    Returns:
        Dictionary mapping level → count

    Example:
        >>> next_steps = [
        ...     {"level": "critical", "test": "A"},
        ...     {"level": "critical", "test": "B"},
        ...     {"level": "priority", "test": "C"},
        ... ]
        >>> counts = count_by_level(next_steps)
        >>> counts
        {'critical': 2, 'priority': 1}
    """
    counts = {}
    for step in next_steps:
        level = step.get("level", "routine")
        counts[level] = counts.get(level, 0) + 1
    return counts
