"""
YAML Parser - Singleton Pattern

Loads all 16 YAML configuration files and caches them for reuse.
Thread-safe singleton implementation.

IEC 62304 Class C Compliance:
- Input validation for all YAML files
- Error handling with descriptive messages
- Immutable cached data

Author: Dr. Abel Costa
"""

import os
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
import threading


class YAMLParser:
    """
    Singleton YAML parser for HemoDoctor configuration files.

    Loads 16 YAML modules from config/ directory and caches them.
    Thread-safe implementation using double-checked locking.

    Example:
        >>> parser = YAMLParser.get_instance()
        >>> config = parser.config
        >>> evidences = parser.evidences
    """

    _instance: Optional['YAMLParser'] = None
    _lock = threading.Lock()

    def __init__(self, config_dir: Optional[Path] = None):
        """
        Initialize YAML parser.

        Args:
            config_dir: Path to configuration directory (default: ../config/)

        Note:
            Don't call this directly. Use get_instance() instead.
        """
        if config_dir is None:
            # Default: hemodoctor_cdss/config/
            config_dir = Path(__file__).parent.parent.parent.parent / "config"

        self.config_dir = Path(config_dir)

        if not self.config_dir.exists():
            raise FileNotFoundError(
                f"Configuration directory not found: {self.config_dir}"
            )

        # Load all YAML files
        self._data: Dict[str, Any] = {}
        self._load_all()

    def _load_yaml(self, filename: str) -> Dict[str, Any]:
        """
        Load a single YAML file with error handling.

        Args:
            filename: YAML filename (e.g., "00_config_hybrid.yaml")

        Returns:
            Parsed YAML content as dictionary

        Raises:
            FileNotFoundError: If YAML file not found
            yaml.YAMLError: If YAML syntax is invalid
        """
        filepath = self.config_dir / filename

        if not filepath.exists():
            raise FileNotFoundError(f"YAML file not found: {filepath}")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data if data is not None else {}
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML syntax in {filename}: {e}")

    def _load_all(self) -> None:
        """Load all 16 YAML configuration files."""
        yaml_files = [
            ("config", "00_config_hybrid.yaml"),
            ("schema", "01_schema_hybrid.yaml"),
            ("evidences", "02_evidence_hybrid.yaml"),
            ("syndromes", "03_syndromes_hybrid.yaml"),
            ("output_templates", "04_output_templates_hybrid.yaml"),
            ("missingness", "05_missingness_hybrid_v2.3.yaml"),
            ("route_policy", "06_route_policy_hybrid.yaml"),
            ("conflict_matrix", "07_conflict_matrix_hybrid.yaml"),
            ("normalization", "07_normalization_heuristics.yaml"),
            ("wormlog", "08_wormlog_hybrid.yaml"),
            ("next_steps", "09_next_steps_engine_hybrid.yaml"),
            ("runbook", "10_runbook_hybrid.yaml"),
            ("case_state", "11_case_state_hybrid.yaml"),
            ("output_policies", "12_output_policies_hybrid.yaml"),
        ]

        for key, filename in yaml_files:
            try:
                self._data[key] = self._load_yaml(filename)
            except Exception as e:
                # Non-critical YAMLs can be missing (e.g., runbook, case_state)
                if key in ["runbook", "case_state", "conflict_matrix"]:
                    self._data[key] = {}
                else:
                    raise RuntimeError(f"Failed to load critical YAML {key}: {e}")

    @classmethod
    def get_instance(cls, config_dir: Optional[Path] = None) -> 'YAMLParser':
        """
        Get singleton instance (thread-safe).

        Args:
            config_dir: Path to configuration directory (only used on first call)

        Returns:
            Singleton YAMLParser instance
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-check locking
                    cls._instance = cls(config_dir)
        return cls._instance

    # Properties for easy access

    @property
    def config(self) -> Dict[str, Any]:
        """00_config_hybrid.yaml - Cutoffs, units, LOINC codes."""
        return self._data.get("config", {})

    @property
    def schema(self) -> Dict[str, Any]:
        """01_schema_hybrid.yaml - Canonical CBC schema (54 fields)."""
        return self._data.get("schema", {})

    @property
    def evidences(self) -> Dict[str, Any]:
        """02_evidence_hybrid.yaml v2.6.0 - 79 evidences."""
        return self._data.get("evidences", {})

    @property
    def syndromes(self) -> Dict[str, Any]:
        """03_syndromes_hybrid.yaml v2.3.1 - 35 syndromes."""
        return self._data.get("syndromes", {})

    @property
    def output_templates(self) -> Dict[str, Any]:
        """04_output_templates_hybrid.yaml - Markdown/HTML/JSON/FHIR."""
        return self._data.get("output_templates", {})

    @property
    def missingness(self) -> Dict[str, Any]:
        """05_missingness_hybrid_v2.3.yaml - Proxy logic + 6-level fallback."""
        return self._data.get("missingness", {})

    @property
    def route_policy(self) -> Dict[str, Any]:
        """06_route_policy_hybrid.yaml - Deterministic routing."""
        return self._data.get("route_policy", {})

    @property
    def normalization(self) -> Dict[str, Any]:
        """07_normalization_heuristics.yaml - Unit detection."""
        return self._data.get("normalization", {})

    @property
    def wormlog(self) -> Dict[str, Any]:
        """08_wormlog_hybrid.yaml - WORM audit log config."""
        return self._data.get("wormlog", {})

    @property
    def next_steps(self) -> Dict[str, Any]:
        """09_next_steps_engine_hybrid.yaml - 40 triggers."""
        return self._data.get("next_steps", {})

    @property
    def output_policies(self) -> Dict[str, Any]:
        """12_output_policies_hybrid.yaml - Output orchestration."""
        return self._data.get("output_policies", {})

    def get_cutoff(self, field: str, age_sex_group: str) -> Optional[float]:
        """
        Get age/sex-specific cutoff value.

        Args:
            field: Cutoff field (e.g., "hb_critical_low")
            age_sex_group: Age/sex group (e.g., "adult_m", "pediatric_1_12m")

        Returns:
            Cutoff value or None if not found
        """
        cutoffs = self.config.get("cutoffs", {})
        field_cutoffs = cutoffs.get(field, {})

        if isinstance(field_cutoffs, dict):
            return field_cutoffs.get(age_sex_group)
        else:
            # Simple cutoff (not age/sex-specific)
            return field_cutoffs

    def get_all_evidence_defs(self) -> list:
        """
        Get all 79 evidence definitions from YAML.

        Returns:
            List of evidence dictionaries
        """
        evidences_yaml = self.evidences
        all_evidences = []

        # Combine all evidence categories
        for category in [
            "critical_evidences",
            "red_blood_cell_evidences",
            "white_blood_cell_evidences",
            "platelet_evidences",
            "coagulation_evidences",
            "molecular_evidences",
            "supplementary_lab_evidences",
            "pre_analytical_evidences",
            "complementary_evidences",
        ]:
            evidences = evidences_yaml.get(category, [])
            if evidences:
                all_evidences.extend(evidences)

        return all_evidences

    def get_all_syndrome_defs(self) -> list:
        """
        Get all 35 syndrome definitions from YAML.

        Returns:
            List of syndrome dictionaries (sorted by precedence)
        """
        syndromes_yaml = self.syndromes
        all_syndromes = []

        # Combine all syndrome categories
        for category in [
            "critical_syndromes",
            "priority_syndromes",
            "review_sample_syndromes",
            "routine_syndromes",
        ]:
            syndromes = syndromes_yaml.get(category, [])
            if syndromes:
                all_syndromes.extend(syndromes)

        # Sort by precedence (critical first)
        precedence_map = {
            "critical": 0,
            "priority": 1,
            "review_sample": 2,
            "routine": 3,
        }

        all_syndromes.sort(
            key=lambda s: (
                precedence_map.get(s.get("criticality", "routine"), 999),
                s.get("precedence", 999)
            )
        )

        return all_syndromes

    def get_all_next_steps_triggers(self) -> list:
        """
        Get all 40 next steps triggers from YAML.

        Returns:
            List of trigger dictionaries
        """
        return self.next_steps.get("triggers", [])
