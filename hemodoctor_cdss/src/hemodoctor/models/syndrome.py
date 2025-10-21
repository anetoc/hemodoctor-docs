"""
Syndrome Result Model

Represents a detected hematological syndrome.

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional


class SyndromeResult(BaseModel):
    """
    Result of syndrome detection.

    Attributes:
        id: Syndrome ID (e.g., "S-TMA", "S-NEUTROPENIA-GRAVE")
        criticality: Severity level ("critical" | "priority" | "review_sample" | "routine")
        evidences: List of evidence IDs that support this syndrome
        actions: Immediate clinical actions recommended
        next_steps: Follow-up clinical steps
        confidence: Confidence level (C0/C1/C2) - V1 feature
        route_id: Deterministic SHA256 hash (for routing/audit)

    Example:
        >>> syndrome = SyndromeResult(
        ...     id="S-TMA",
        ...     criticality="critical",
        ...     evidences=["E-PLT-CRIT-LOW", "E-SCHISTOCYTES-GE1PCT"],
        ...     actions=["Esfregaço urgente", "LDH + Creatinina"],
        ... )
    """

    id: str = Field(..., description="Syndrome ID (e.g., S-TMA)")
    criticality: str = Field(..., description="Severity: critical | priority | review_sample | routine")
    evidences: List[str] = Field(default_factory=list, description="Supporting evidence IDs")
    actions: List[str] = Field(default_factory=list, description="Immediate clinical actions")
    next_steps: List[str] = Field(default_factory=list, description="Follow-up steps")
    confidence: Optional[str] = Field(default=None, description="Confidence level C0/C1/C2")
    route_id: Optional[str] = Field(default=None, description="Deterministic SHA256 hash")

    model_config = ConfigDict(
        frozen=False,
        extra="forbid"
    )
