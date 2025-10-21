---
name: Documentation
description: Maintain technical documentation for HemoDoctor Hybrid V1.0 following regulatory standards (ANVISA/FDA/ISO). Use when updating specs, creating technical reports, or preparing submission documents.
---

# Documentation

Maintains technical documentation compliant with ANVISA RDC 657/2022, FDA 21 CFR Part 11, and ISO 13485:2016.

## Documentation structure

**Core technical docs:**
- `README.md` - Project overview
- `INDEX_COMPLETO.md` - Complete file index
- `QUICKSTART_IMPLEMENTACAO.md` - Dev quick start
- `CLAUDE.md` - AI context file

**Analysis docs:**
- `Analise_Comparativa/` - Design decisions
- `Especificacoes_Dev/` - Dev team specs

## Documentation standards

### Technical specifications

Follow IEC 62304 Class C structure:

```markdown
# [DOC-ID] [Document Title]

**Version:** X.Y.Z
**Date:** YYYY-MM-DD
**Author:** [Name]
**Status:** Draft | Review | Approved

## 1. Purpose

[Why this document exists]

## 2. Scope

[What is covered and what is not]

## 3. Technical details

[Main content with subsections]

## 4. References

[Links to other documents]

## 5. Revision history

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-10-19 | Abel Costa | Initial version |
```

### Code documentation

Use docstrings for all functions:

```python
def evaluate_evidence(evidence, cbc, config):
    """
    Evaluate a single evidence rule against CBC data.

    Args:
        evidence (dict): Evidence definition with 'id', 'rule', 'requires'
        cbc (dict): CBC laboratory data (hb, plt, wbc, etc.)
        config (dict): Configuration with cutoff values

    Returns:
        str: "present" if evidence condition met,
             "absent" if not met,
             "unknown" if required data missing

    Example:
        >>> evidence = {"id": "E-ANC-CRIT", "rule": "anc < 0.5", "requires": ["anc"]}
        >>> cbc = {"anc": 0.3}
        >>> evaluate_evidence(evidence, cbc, config)
        'present'
    """
    # Implementation
```

### YAML documentation

Include inline comments for complex logic:

```yaml
- id: S-TMA
  criticality: critical
  combine:
    all:
      - E-SCHISTOCYTES-GE1PCT    # Mandatory: schistocytes present
      - E-PLT-CRIT-LOW             # Mandatory: severe thrombocytopenia
    any:
      - E-HEMOLYSIS-PATTERN       # Hemolysis markers OR high LDH
      - E-LDH-HIGH
  threshold: 0.0                   # All required evidences must be present
```

## Regulatory compliance

### ANVISA RDC 657/2022

Required documentation:
- Technical documentation (TEC-001)
- Software requirements specification (SRS-001)
- Software design document (SDD-001)
- Verification & validation plan (VVP-001)
- Instructions for use (IFU-001)

### FDA 21 CFR Part 11

Electronic records requirements:
- Audit trails (WORM log)
- Data integrity (HMAC signatures)
- Traceability (route_id + data_lineage)

### ISO 13485:2016

Quality management system:
- Document control procedures
- Change management
- Training records
- Calibration records

## Documentation workflow

1. **Draft**: Author creates initial version
2. **Review**: Technical review by peers
3. **Clinical review**: Hematologist approval (if applicable)
4. **Approval**: Quality manager sign-off
5. **Release**: Version control + distribution
6. **Maintenance**: Regular updates per change control

## Versioning

Use semantic versioning:

- **Major (X.0.0)**: Breaking changes, architecture changes
- **Minor (0.X.0)**: New features, backward compatible
- **Patch (0.0.X)**: Bug fixes, typos, clarifications

## Templates

### Test report template

```markdown
# [TESTREP-XXX] [Test Name] Report

**Version:** 1.0.0
**Date:** YYYY-MM-DD
**Tester:** [Name]

## Test objective

[What is being tested and why]

## Test environment

- Python: 3.9+
- Dependencies: [List]
- Test data: [Source]

## Test cases

| ID | Description | Input | Expected | Actual | Status |
|----|-------------|-------|----------|--------|--------|
| TC-001 | [Description] | [Input] | [Expected] | [Actual] | ✅ Pass |
| TC-002 | [Description] | [Input] | [Expected] | [Actual] | ❌ Fail |

## Summary

- Total: X test cases
- Passed: Y (Z%)
- Failed: W

## Issues found

1. [Issue description]
   - Severity: Critical | High | Medium | Low
   - Resolution: [Plan]

## Conclusion

[Pass/Fail with justification]
```

### Technical note template

```markdown
# [TN-XXX] [Brief Title]

**Date:** YYYY-MM-DD
**Author:** [Name]

## Context

[Why this note exists]

## Problem

[What needs to be explained or decided]

## Analysis

[Technical details, options considered]

## Decision

[What was decided and why]

## Impact

[Affected components, migration plan if needed]

## References

- [Link to related docs]
```

## Best practices

1. **Write for the future**: Assume reader has no context
2. **Be specific**: Use examples, not abstractions
3. **Link liberally**: Reference related documents
4. **Keep updated**: Update docs with code changes
5. **Version everything**: Track all changes
6. **Review before commit**: No unreviewed docs in main branch

## Troubleshooting

**Inconsistent information:**
- Check document version and date
- Verify against authoritative source
- Update or mark as obsolete

**Missing documentation:**
- Check INDEX_COMPLETO.md for complete list
- Search in subdirectories
- Ask if document should exist

**Unclear technical description:**
- Add concrete examples
- Include diagrams if helpful
- Reference implementation code
