"""
Data Models for HemoDoctor CDSS.

Pydantic models for:
- CBC input data (54 fields)
- Evidence results
- Syndrome results
- Analysis results
"""

from hemodoctor.models.evidence import EvidenceResult
from hemodoctor.models.syndrome import SyndromeResult

__all__ = [
    "EvidenceResult",
    "SyndromeResult",
]
