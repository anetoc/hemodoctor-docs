"""
HemoDoctor CDSS v2.4.0

Clinical Decision Support System for Complete Blood Count (CBC) Analysis.

Regulatory Compliance:
- ANVISA RDC 657/751 (SaMD Class III)
- IEC 62304:2006+A1:2015 (Software Class C)
- ISO 14971:2019 (Risk Management)
- ISO 13485:2016 (Quality Management System)

Author: Dr. Abel Costa (IDOR-SP)
Generated: 2025-10-20
"""

__version__ = "2.4.0"
__author__ = "Dr. Abel Costa"
__license__ = "Proprietary"

from hemodoctor.api.pipeline import analyze_cbc

__all__ = ["analyze_cbc", "__version__"]
