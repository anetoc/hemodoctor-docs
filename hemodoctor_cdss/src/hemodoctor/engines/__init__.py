"""
Clinical Engines Module

Contains all clinical decision engines for HemoDoctor CDSS.

Engines:
    - Evidence Engine: Evaluates 79 clinical evidence rules
    - Syndrome Detector: Detects 35 hematological syndromes
    - (Future) Normalization, Schema Validation, Next Steps, WORM Log, Output Renderer

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from hemodoctor.engines.evidence import (
    evaluate_evidence,
    evaluate_all_evidences,
    get_present_evidences,
    get_unknown_evidences,
    get_missing_rate,
)

from hemodoctor.engines.syndrome import (
    detect_syndromes,
    is_syndrome_present,
    get_critical_syndromes,
    get_syndrome_by_id,
    count_syndromes_by_criticality,
)

__all__ = [
    # Evidence Engine
    "evaluate_evidence",
    "evaluate_all_evidences",
    "get_present_evidences",
    "get_unknown_evidences",
    "get_missing_rate",
    # Syndrome Detector
    "detect_syndromes",
    "is_syndrome_present",
    "get_critical_syndromes",
    "get_syndrome_by_id",
    "count_syndromes_by_criticality",
]
