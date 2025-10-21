"""
Output Renderer - Clinical Report Generator

Generates clinical reports in multiple formats (Markdown, HTML, JSON).
Implements CDSS-compliant microcopy (not diagnostic language).

Based on: 04_output_templates_hybrid.yaml v2.3.1-cdss

Formats:
    - Markdown: Human-readable text
    - HTML: Web/PDF rendering
    - JSON: API/integration
    - FHIR: Future (DiagnosticReport resource)

Microcopy Rules:
    - Allowed: "padrão compatível com", "sugere", "considerar"
    - Forbidden: "diagnóstico de", "tem (doença)", "confirma"
    - Audience: Non-hematologist physicians
    - Disclaimer: CDSS support tool, not diagnostic

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from typing import Dict, Any, List
from datetime import datetime


def render_output(
    syndromes: list,
    next_steps: List[Dict[str, Any]],
    cbc_data: Dict[str, Any],
    evidences: list,
    route_id: str,
    format: str = "markdown"
) -> str:
    """
    Render clinical output in specified format.

    Args:
        syndromes: List of detected syndromes
        next_steps: List of next step recommendations
        cbc_data: Original CBC data
        evidences: List of present evidences
        route_id: Deterministic routing hash
        format: Output format ("markdown", "html", "json")

    Returns:
        str: Formatted output

    Example:
        >>> syndromes = [SyndromeResult(id="S-TMA", criticality="critical", ...)]
        >>> next_steps = [{"level": "critical", "test": "Esfregaço urgente", ...}]
        >>> cbc = {"hb": 8.2, "plt": 8}
        >>> evidences = [EvidenceResult(id="E-PLT-CRIT-LOW", ...)]
        >>> route_id = "abc123..."
        >>> output = render_output(syndromes, next_steps, cbc, evidences, route_id, "markdown")
        >>> "CRÍTICO" in output or "TMA" in output
        True
    """
    if format == "markdown":
        return render_markdown(syndromes, next_steps, cbc_data, evidences, route_id)
    elif format == "html":
        return render_html(syndromes, next_steps, cbc_data, evidences, route_id)
    elif format == "json":
        return render_json(syndromes, next_steps, cbc_data, evidences, route_id)
    else:
        raise ValueError(f"Unsupported format: {format}")


def render_markdown(
    syndromes: list,
    next_steps: List[Dict[str, Any]],
    cbc_data: Dict[str, Any],
    evidences: list,
    route_id: str
) -> str:
    """
    Render clinical report as Markdown.

    Args:
        syndromes: List of detected syndromes
        next_steps: List of next step recommendations
        cbc_data: Original CBC data
        evidences: List of present evidences
        route_id: Deterministic routing hash

    Returns:
        str: Markdown-formatted report

    Example:
        >>> syndromes = [SyndromeResult(id="S-TMA", criticality="critical", ...)]
        >>> next_steps = [{"level": "critical", "test": "Esfregaço", ...}]
        >>> cbc = {"hb": 8.2, "plt": 8}
        >>> evidences = [EvidenceResult(id="E-PLT-CRIT-LOW", ...)]
        >>> route_id = "abc123"
        >>> md = render_markdown(syndromes, next_steps, cbc, evidences, route_id)
        >>> "# HemoDoctor" in md
        True
    """
    lines = []

    # Header
    lines.append("# HemoDoctor - Relatório de Análise CBC")
    lines.append("")
    lines.append(f"**Data:** {datetime.utcnow().strftime('%d/%m/%Y %H:%M UTC')}")
    lines.append(f"**Route ID:** `{route_id[:16]}...`")
    lines.append(f"**Versão:** v2.4.0")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Top syndrome
    if syndromes:
        top_syndrome = syndromes[0]
        criticality = top_syndrome.criticality if hasattr(top_syndrome, 'criticality') else "unknown"
        syndrome_id = top_syndrome.id if hasattr(top_syndrome, 'id') else str(top_syndrome)

        # Header based on criticality
        if criticality == "critical":
            lines.append("## 🔴 CRÍTICO — Achados Tempo-Sensíveis")
        elif criticality == "priority":
            lines.append("## 🟠 PRIORIDADE — Requer Investigação")
        else:
            lines.append("## 🟢 ROTINA — Sem Achados Críticos")

        lines.append("")
        lines.append(f"**Hipótese:** {syndrome_id}")
        lines.append("")

        # Evidence summary
        evidence_count = len([e for e in evidences if hasattr(e, 'status') and e.status == "present"])
        lines.append(f"**Por quê:** {evidence_count} evidências presentes")
        lines.append("")

        # Key values
        key_values = extract_key_values(cbc_data, syndrome_id)
        if key_values:
            lines.append("**Valores chave:**")
            for key, value in key_values.items():
                lines.append(f"- {key.upper()}: {value}")
            lines.append("")

    # Next steps
    if next_steps:
        lines.append("## Próximos Passos Recomendados")
        lines.append("")

        for i, step in enumerate(next_steps[:4], 1):  # Max 4 steps
            level = step.get("level", "routine")
            test = step.get("test", "Não especificado")
            rationale = step.get("rationale", "")

            level_emoji = {
                "critical": "🔴 CRÍTICO",
                "priority": "🟠 PRIORIDADE",
                "routine": "🟢 ROTINA"
            }.get(level, level.upper())

            lines.append(f"{i}. **{level_emoji}** — {test}")
            if rationale:
                lines.append(f"   - {rationale}")
            lines.append("")

    # Disclaimer
    lines.append("---")
    lines.append("")
    lines.append("*⚠️ Este é um sistema de apoio à decisão clínica (CDSS). Não substitui o julgamento clínico. Resultado não é diagnóstico.*")
    lines.append("")

    return "\n".join(lines)


def render_html(
    syndromes: list,
    next_steps: List[Dict[str, Any]],
    cbc_data: Dict[str, Any],
    evidences: list,
    route_id: str
) -> str:
    """
    Render clinical report as HTML.

    Args:
        syndromes: List of detected syndromes
        next_steps: List of next step recommendations
        cbc_data: Original CBC data
        evidences: List of present evidences
        route_id: Deterministic routing hash

    Returns:
        str: HTML-formatted report

    Example:
        >>> syndromes = [SyndromeResult(id="S-TMA", criticality="critical", ...)]
        >>> next_steps = []
        >>> cbc = {"hb": 8.2}
        >>> evidences = []
        >>> route_id = "abc123"
        >>> html = render_html(syndromes, next_steps, cbc, evidences, route_id)
        >>> "<html>" in html
        True
    """
    # Convert Markdown to HTML (simple conversion for V0)
    md = render_markdown(syndromes, next_steps, cbc_data, evidences, route_id)

    # Simple Markdown → HTML conversion (V0)
    # V1: Use proper Markdown library (markdown-it-py, mistune, etc.)
    html = md.replace("# ", "<h1>").replace("\n", "</h1>\n", 1)
    html = html.replace("## ", "<h2>").replace("\n", "</h2>\n")
    html = html.replace("**", "<strong>").replace("**", "</strong>")
    html = html.replace("- ", "<li>").replace("\n", "</li>\n")
    html = html.replace("---", "<hr>")

    # Wrap in HTML template
    output = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>HemoDoctor - Relatório CBC</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; margin-top: 30px; }}
        hr {{ border: none; border-top: 2px solid #ecf0f1; margin: 30px 0; }}
        .disclaimer {{ background: #fff3cd; padding: 15px; border-left: 5px solid #ffc107; margin-top: 30px; }}
    </style>
</head>
<body>
{html}
</body>
</html>"""

    return output


def render_json(
    syndromes: list,
    next_steps: List[Dict[str, Any]],
    cbc_data: Dict[str, Any],
    evidences: list,
    route_id: str
) -> str:
    """
    Render clinical report as JSON.

    Args:
        syndromes: List of detected syndromes
        next_steps: List of next step recommendations
        cbc_data: Original CBC data
        evidences: List of present evidences
        route_id: Deterministic routing hash

    Returns:
        str: JSON-formatted report

    Example:
        >>> import json
        >>> syndromes = [SyndromeResult(id="S-TMA", criticality="critical", ...)]
        >>> next_steps = []
        >>> cbc = {"hb": 8.2}
        >>> evidences = []
        >>> route_id = "abc123"
        >>> json_str = render_json(syndromes, next_steps, cbc, evidences, route_id)
        >>> data = json.loads(json_str)
        >>> data["version"]
        '2.4.0'
    """
    import json

    # Extract syndrome data
    syndrome_data = []
    for s in syndromes:
        syndrome_data.append({
            "id": s.id if hasattr(s, 'id') else str(s),
            "criticality": s.criticality if hasattr(s, 'criticality') else "unknown",
            "actions": s.actions if hasattr(s, 'actions') else [],
            "next_steps": s.next_steps if hasattr(s, 'next_steps') else [],
        })

    # Extract evidence data
    evidence_data = []
    for e in evidences:
        if hasattr(e, 'status') and e.status == "present":
            evidence_data.append({
                "id": e.id if hasattr(e, 'id') else str(e),
                "strength": e.strength if hasattr(e, 'strength') else "unknown",
            })

    # Build JSON structure
    output = {
        "version": "2.4.0",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "route_id": route_id,
        "syndromes": syndrome_data,
        "evidences": evidence_data,
        "next_steps": next_steps,
        "disclaimer": "CDSS de apoio à decisão. Não substitui julgamento clínico."
    }

    return json.dumps(output, ensure_ascii=False, indent=2)


def extract_key_values(cbc_data: Dict[str, Any], syndrome_id: str) -> Dict[str, str]:
    """
    Extract key CBC values relevant to syndrome.

    Args:
        cbc_data: CBC data dictionary
        syndrome_id: Syndrome ID (e.g., "S-TMA")

    Returns:
        Dict of key:value pairs (formatted strings)

    Example:
        >>> cbc = {"hb": 8.2, "plt": 8, "wbc": 10.5}
        >>> values = extract_key_values(cbc, "S-TMA")
        >>> "hb" in values
        True
        >>> "plt" in values
        True
    """
    # Define key values per syndrome (subset for V0)
    syndrome_keys = {
        "S-TMA": ["hb", "plt", "ldh", "schistocytes"],
        "S-NEUTROPENIA-GRAVE": ["anc", "wbc"],
        "S-PLT-CRITICA": ["plt"],
        "S-ANEMIA-GRAVE": ["hb", "mcv", "reticulocytes"],
        "S-IDA": ["hb", "mcv", "ferritin"],
    }

    # Get relevant keys
    keys = syndrome_keys.get(syndrome_id, ["hb", "wbc", "plt"])

    # Extract values
    key_values = {}
    for key in keys:
        value = cbc_data.get(key)
        if value is not None:
            key_values[key] = format_value(key, value)

    return key_values


def format_value(field: str, value: Any) -> str:
    """
    Format CBC value for display.

    Args:
        field: Field name (e.g., "hb")
        value: Field value

    Returns:
        str: Formatted value with unit

    Example:
        >>> format_value("hb", 15.2)
        '15.2 g/dL'
        >>> format_value("plt", 250)
        '250 ×10⁹/L'
    """
    # Define units
    units = {
        "hb": "g/dL",
        "ht": "%",
        "wbc": "×10⁹/L",
        "plt": "×10⁹/L",
        "anc": "×10⁹/L",
        "mcv": "fL",
        "rdw": "%",
        "ldh": "U/L",
        "ferritin": "ng/mL",
    }

    unit = units.get(field, "")

    # Format number
    try:
        value_float = float(value)
        # Determine decimal places
        if field in ["plt", "mcv"]:
            formatted = f"{value_float:.0f}"
        elif field in ["anc"]:
            formatted = f"{value_float:.2f}"
        else:
            formatted = f"{value_float:.1f}"

        return f"{formatted} {unit}".strip()
    except (ValueError, TypeError):
        return str(value)
