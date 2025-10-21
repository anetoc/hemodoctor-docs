"""
CBC Input Model

Complete Blood Count input data model with 54 fields.

Based on: 01_schema_hybrid.yaml v2.3.1

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict


class CBCInput(BaseModel):
    """
    Complete Blood Count (CBC) input data.

    54 fields total:
    - 15 core CBC fields (hb, wbc, plt, mcv, etc.)
    - 9 complementary tests (ferritin, tsat, crp, ldh, etc.)
    - 9 molecular markers (jak2_pos, bcr_abl_pos, etc.)
    - 17 morphology tokens (tri-state booleans)
    - 2 metadata (age_years, sex)
    - 2 coagulation (d_dimer, fibrinogenio) - V1.2

    All numeric fields are Optional (handle missing data).
    Tri-state booleans: True | False | None (unknown).
    """

    # Core CBC (15 fields)
    hb: Optional[float] = Field(default=None, ge=0, le=25, description="Hemoglobin (g/dL)")
    ht: Optional[float] = Field(default=None, ge=0, le=75, description="Hematocrit (%)")
    rbc: Optional[float] = Field(default=None, ge=0, le=10, description="Red Blood Cells (1e12/L)")
    mcv: Optional[float] = Field(default=None, ge=50, le=150, description="Mean Corpuscular Volume (fL)")
    mch: Optional[float] = Field(default=None, ge=15, le=50, description="Mean Corpuscular Hemoglobin (pg)")
    mchc: Optional[float] = Field(default=None, ge=25, le=38, description="MCHC (g/dL)")
    rdw: Optional[float] = Field(default=None, ge=9, le=20, description="RDW (%)")
    wbc: Optional[float] = Field(default=None, ge=0, le=200, description="White Blood Cells (1e9/L)")
    anc: Optional[float] = Field(default=None, ge=0, le=50, description="Absolute Neutrophil Count (1e9/L)")
    lymphocytes_abs: Optional[float] = Field(default=None, ge=0, le=50, description="Lymphocytes (1e9/L)")
    eosinophils_abs: Optional[float] = Field(default=None, ge=0, le=10, description="Eosinophils (1e9/L)")
    basophils_abs: Optional[float] = Field(default=None, ge=0, le=2, description="Basophils (1e9/L)")
    monocytes_abs: Optional[float] = Field(default=None, ge=0, le=10, description="Monocytes (1e9/L)")
    plt: Optional[float] = Field(default=None, ge=0, le=2000, description="Platelets (1e9/L)")
    mpv: Optional[float] = Field(default=None, ge=5, le=15, description="Mean Platelet Volume (fL)")
    reticulocytes: Optional[float] = Field(default=None, ge=0, le=500, description="Reticulocytes (1e9/L)")

    # Complementary tests (9 fields)
    ferritin: Optional[float] = Field(default=None, ge=0, le=10000, description="Ferritin (ng/mL)")
    tsat: Optional[float] = Field(default=None, ge=0, le=100, description="Transferrin Saturation (%)")
    crp: Optional[float] = Field(default=None, ge=0, le=500, description="C-Reactive Protein (mg/L)")
    ldh: Optional[float] = Field(default=None, ge=0, le=5000, description="LDH (U/L)")
    bt_indireta: Optional[float] = Field(default=None, ge=0, le=50, description="Indirect Bilirubin (mg/dL)")
    haptoglobin: Optional[float] = Field(default=None, ge=0, le=300, description="Haptoglobin (mg/dL)")
    b12: Optional[float] = Field(default=None, ge=0, le=2000, description="Vitamin B12 (pg/mL)")
    folate: Optional[float] = Field(default=None, ge=0, le=50, description="Folate (ng/mL)")
    hba2: Optional[float] = Field(default=None, ge=0, le=10, description="HbA2 (%)")
    epo: Optional[float] = Field(default=None, ge=0, le=200, description="Erythropoietin (mIU/mL)")

    # Molecular markers (9 tri-state booleans)
    coombs_pos: Optional[bool] = Field(default=None, description="Coombs Direct positive")
    bcr_abl_pos: Optional[bool] = Field(default=None, description="BCR-ABL positive (CML)")
    jak2_pos: Optional[bool] = Field(default=None, description="JAK2 V617F positive (MPN)")
    calr_pos: Optional[bool] = Field(default=None, description="CALR mutation positive (MPN)")
    mpl_pos: Optional[bool] = Field(default=None, description="MPL mutation positive (MPN)")
    hpn_pos: Optional[bool] = Field(default=None, description="PNH clone (CD55/CD59 deficient)")
    flc_ratio_abnormal: Optional[bool] = Field(default=None, description="Free Light Chains ratio abnormal")
    g6pd_deficient: Optional[bool] = Field(default=None, description="G6PD deficient")
    pk_deficient: Optional[bool] = Field(default=None, description="Pyruvate Kinase deficient")

    # Morphology tokens (17 tri-state booleans)
    morphology: Optional[Dict[str, Optional[bool]]] = Field(
        default_factory=dict,
        description="Morphology tokens: esquistocitos, esferocitos, dacriocitos, etc."
    )

    # Metadata (2 required)
    age_years: float = Field(..., ge=0, le=120, description="Age in years")
    sex: str = Field(..., pattern="^[MFU]$", description="Sex: M/F/U (Unknown)")

    # Coagulation (2 fields) - V1.2
    d_dimer: Optional[float] = Field(default=None, ge=0, description="D-dimer (ng/mL)")
    fibrinogenio: Optional[float] = Field(default=None, ge=0, description="Fibrinogen (mg/dL)")
    pt: Optional[float] = Field(default=None, ge=0, description="Prothrombin Time (s)")
    aptt: Optional[float] = Field(default=None, ge=0, description="APTT (s)")

    @field_validator("sex")
    @classmethod
    def validate_sex(cls, v: str) -> str:
        """Validate sex field."""
        if v not in ["M", "F", "U"]:
            raise ValueError("sex must be M (Male), F (Female), or U (Unknown)")
        return v

    @field_validator("mchc")
    @classmethod
    def validate_mchc(cls, v: Optional[float]) -> Optional[float]:
        """Validate MCHC physiological range (25-38 g/dL)."""
        if v is not None and (v < 25 or v > 38):
            # Flag as pre-analytical error (handled by missingness engine)
            pass  # Allow for review_sample syndrome detection
        return v

    class Config:
        frozen = False
        extra = "forbid"
        json_schema_extra = {
            "example": {
                "hb": 8.2,
                "wbc": 2.1,
                "plt": 45,
                "age_years": 7,
                "sex": "M",
            }
        }
