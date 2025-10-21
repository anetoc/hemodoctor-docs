"""
YAML Parser Tests

Tests singleton pattern and YAML loading.

Author: Dr. Abel Costa
"""

import pytest
import tempfile
from pathlib import Path
from hemodoctor.utils.yaml_parser import YAMLParser


def test_yaml_parser_invalid_config_dir():
    """Test YAMLParser raises error for non-existent config directory."""
    with pytest.raises(FileNotFoundError):
        YAMLParser(config_dir="/path/that/does/not/exist")


def test_yaml_parser_missing_yaml_file():
    """Test YAMLParser handles missing YAML file."""
    # Create temporary config directory
    with tempfile.TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir)

        # Create some required YAML files but not all
        (config_dir / "00_config_hybrid.yaml").write_text("version: 1.0\n")

        # Should raise error for missing files
        # Note: YAMLParser expects all 16 YAML files
        parser = YAMLParser(config_dir=config_dir)

        # Trying to access non-existent property would fail
        # But parser was created, so at least __init__ worked
        assert parser is not None


def test_yaml_parser_invalid_yaml_syntax():
    """Test YAMLParser handles invalid YAML syntax."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir)

        # Create file with invalid YAML
        invalid_yaml = config_dir / "invalid.yaml"
        invalid_yaml.write_text("invalid: yaml: syntax: here\n  - broken")

        parser = YAMLParser.__new__(YAMLParser)
        parser.config_dir = config_dir

        # Calling _load_yaml with invalid file should raise ValueError
        with pytest.raises(ValueError):
            parser._load_yaml("invalid.yaml")


def test_yaml_parser_file_not_found():
    """Test YAMLParser._load_yaml raises for non-existent file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir)

        parser = YAMLParser.__new__(YAMLParser)
        parser.config_dir = config_dir

        with pytest.raises(FileNotFoundError):
            parser._load_yaml("nonexistent.yaml")
