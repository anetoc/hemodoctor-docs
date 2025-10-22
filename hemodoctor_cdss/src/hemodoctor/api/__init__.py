"""
API Layer Module

Main pipeline orchestration and FastAPI endpoints.

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from hemodoctor.api.pipeline import (
    analyze_cbc,
    compute_route_id,
    get_analysis_summary,
)

# Note: normalize_cbc and validate_schema moved to engines/
# Import from engines if needed:
#   from hemodoctor.engines.normalization import normalize_cbc
#   from hemodoctor.engines.schema_validator import validate_schema

__all__ = [
    "analyze_cbc",
    "compute_route_id",
    "get_analysis_summary",
]
