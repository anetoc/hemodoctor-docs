"""
CBC Model Tests

Tests Pydantic CBC data model validation.

Author: Dr. Abel Costa
"""

import pytest
from pydantic import ValidationError


def test_cbc_model_import():
    """Test CBC model can be imported."""
    from hemodoctor.models.cbc import CBCInput

    assert CBCInput is not None


def test_cbc_model_basic():
    """Test CBC model with basic valid data."""
    from hemodoctor.models.cbc import CBCInput

    cbc = CBCInput(
        hb=15.0,
        mcv=88,
        wbc=7.5
    )

    assert cbc.hb == 15.0
    assert cbc.mcv == 88
    assert cbc.wbc == 7.5


def test_cbc_model_with_optional_fields():
    """Test CBC model with optional fields."""
    from hemodoctor.models.cbc import CBCInput

    cbc = CBCInput(
        hb=15.0,
        mcv=88,
        wbc=7.5,
        plt=250,
        age_years=35,
        sex="M"
    )

    assert cbc.plt == 250
    assert cbc.age_years == 35
    assert cbc.sex == "M"
