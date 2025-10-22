"""
Evidence Result Model

Represents the result of evaluating a single clinical evidence rule.

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List


class EvidenceResult(BaseModel):
    """
    Result of evaluating a clinical evidence rule.

    Attributes:
        id: Evidence ID (e.g., "E-ANC-CRIT")
        status: Tri-state evaluation result ("present" | "absent" | "unknown")
        strength: Evidence strength ("critical" | "strong" | "high" | "moderate" | "weak" | "low")
        requires: List of CBC fields required to evaluate this evidence
        clinical_significance: Clinical meaning of this evidence
        rule: Original rule expression (for debugging/audit)

    Example:
        >>> evidence = EvidenceResult(
        ...     id="E-ANC-CRIT",
        ...     status="present",
        ...     strength="strong",
        ...     requires=["anc"],
        ...     clinical_significance="Risk high infectious"
        ... )
    """

    id: str = Field(..., description="Evidence ID (e.g., E-ANC-CRIT)")
    status: str = Field(..., description="Evaluation result: present | absent | unknown")
    strength: str = Field(default="moderate", description="Evidence strength level")
    requires: List[str] = Field(default_factory=list, description="Required CBC fields")
    clinical_significance: str = Field(default="", description="Clinical meaning")
    rule: Optional[str] = Field(default=None, description="Original rule expression")

    model_config = ConfigDict(
        frozen=False,  # Allow modification for testing
        extra="forbid"  # Reject unknown fields
    )
