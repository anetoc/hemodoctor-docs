"""
HemoDoctor CDSS - FastAPI REST API

Production-ready REST API for CBC analysis.
Implements 4 core endpoints with OpenAPI documentation.

Endpoints:
    - POST /analyze: Analyze CBC data
    - GET /health: Health check
    - GET /version: System version
    - GET /docs: OpenAPI documentation (auto-generated)

Security:
    - CORS enabled (configure allowed origins)
    - Rate limiting (TODO: implement in production)
    - Input validation (Pydantic)
    - HTTPS only in production

Author: Dr. Abel Costa
IEC 62304 Class C
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from typing import Dict, Any, Optional, List
from datetime import datetime, timezone
import os

from hemodoctor.api.pipeline import analyze_cbc
from hemodoctor.engines.output_renderer import render_output


# Initialize FastAPI app
app = FastAPI(
    title="HemoDoctor CDSS API",
    description="Clinical Decision Support System for CBC Analysis (SaMD Class III)",
    version="2.6.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# CORS middleware (configure allowed origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Pydantic Models (Request/Response)
# ============================================================================

class CBCRequest(BaseModel):
    """
    CBC analysis request.

    Required fields:
        - hb: Hemoglobin (g/dL)
        - mcv: Mean Corpuscular Volume (fL)
        - wbc: White Blood Cells (×10⁹/L)

    Optional fields:
        - plt, anc, age_years, sex, etc. (54 total)
    """
    # Required fields
    hb: float = Field(..., description="Hemoglobin (g/dL)", ge=0, le=25)
    mcv: float = Field(..., description="Mean Corpuscular Volume (fL)", ge=50, le=150)
    wbc: float = Field(..., description="White Blood Cells (×10⁹/L)", ge=0, le=200)

    # Optional fields (subset for V0)
    plt: Optional[float] = Field(None, description="Plaquetas (×10⁹/L)", ge=0, le=2000)
    anc: Optional[float] = Field(None, description="Absolute Neutrophil Count (×10⁹/L)", ge=0, le=50)
    age_years: Optional[float] = Field(None, description="Idade (anos)", ge=0, le=120)
    sex: Optional[str] = Field(None, description="Sexo (M/F)")

    # Metadata (optional)
    case_id: Optional[str] = Field(None, description="Case ID (will be pseudonymized)")
    site_id: Optional[str] = Field(None, description="Site ID (will be pseudonymized)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "hb": 15.2,
                "mcv": 88,
                "wbc": 8.5,
                "plt": 250,
                "anc": 4.0,
                "age_years": 35,
                "sex": "M",
                "case_id": "CASE-12345",
                "site_id": "HOSPITAL-ABC"
            }
        }
    )


class AnalysisResponse(BaseModel):
    """CBC analysis response."""
    version: str = Field(..., description="Software version")
    timestamp: str = Field(..., description="Analysis timestamp (UTC)")
    route_id: str = Field(..., description="Deterministic routing hash")
    top_syndromes: List[str] = Field(..., description="Detected syndromes (sorted by precedence)")
    evidences_present: List[str] = Field(..., description="Present evidence IDs")
    next_steps: List[Dict[str, Any]] = Field(..., description="Recommended next steps")
    report: Dict[str, str] = Field(..., description="Formatted reports (markdown, html, json)")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "version": "2.6.0",
                "timestamp": "2025-10-20T12:34:56.789Z",
                "route_id": "sha256:abc123...",
                "top_syndromes": ["S-NORMAL"],
                "evidences_present": [],
                "next_steps": [],
                "report": {
                    "markdown": "# HemoDoctor - Relatório...",
                    "html": "<!DOCTYPE html>...",
                    "json": "{...}"
                }
            }
        }
    )


class HealthResponse(BaseModel):
    """Health check response."""
    status: str = Field(..., description="Service status")
    version: str = Field(..., description="Software version")
    timestamp: str = Field(..., description="Current timestamp (UTC)")
    yamls_loaded: int = Field(..., description="Number of YAML config files loaded")


class VersionResponse(BaseModel):
    """Version information response."""
    version: str = Field(..., description="Software version")
    release_date: str = Field(..., description="Release date")
    environment: str = Field(..., description="Environment (dev/staging/production)")


# ============================================================================
# API Endpoints
# ============================================================================

@app.post(
    "/analyze",
    response_model=AnalysisResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyze CBC Data",
    description="Analyzes complete blood count (CBC) data and returns clinical recommendations."
)
async def analyze_endpoint(request: CBCRequest):
    """
    Analyze CBC data.

    Args:
        request: CBC analysis request

    Returns:
        AnalysisResponse: Complete analysis result with syndromes, evidences, and next steps

    Raises:
        HTTPException 422: Invalid input data
        HTTPException 500: Internal server error

    Example:
        ```bash
        curl -X POST http://localhost:8000/analyze \\
          -H "Content-Type: application/json" \\
          -d '{"hb": 15.2, "mcv": 88, "wbc": 8.5, "plt": 250, "age_years": 35, "sex": "M"}'
        ```
    """
    try:
        # Convert request to dict
        cbc_data = request.model_dump(exclude_none=True)

        # Run analysis pipeline
        result = analyze_cbc(cbc_data)

        # Extract objects from pipeline result
        syndromes_detail = result.get("syndromes_detail", [])
        evidences_detail = result.get("evidences_detail", [])
        next_steps_data = result.get("next_steps", [])

        # Generate reports in multiple formats
        # render_output expects syndromes/evidences as objects (not dicts)
        # We'll pass the detail dicts directly (render_output handles both)
        reports = {
            "markdown": render_output(syndromes_detail, next_steps_data, cbc_data, evidences_detail, result["route_id"], "markdown"),
            "html": render_output(syndromes_detail, next_steps_data, cbc_data, evidences_detail, result["route_id"], "html"),
            "json": render_output(syndromes_detail, next_steps_data, cbc_data, evidences_detail, result["route_id"], "json"),
        }

        # Build response
        response = AnalysisResponse(
            version=result["version"],
            timestamp=result["timestamp"],
            route_id=result["route_id"],
            top_syndromes=result["top_syndromes"],
            evidences_present=result["evidences_present"],
            next_steps=next_steps_data,  # From pipeline
            report=reports
        )

        return response

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Invalid input data: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@app.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Returns service health status and basic system information."
)
async def health_check():
    """
    Health check endpoint.

    Returns:
        HealthResponse: Service health status

    Example:
        ```bash
        curl http://localhost:8000/health
        ```
    """
    try:
        from hemodoctor.utils.yaml_parser import YAMLParser

        # Load YAML parser to verify configs are accessible
        parser = YAMLParser.get_instance()
        yamls_loaded = 16  # TODO: Count actual loaded YAMLs

        return HealthResponse(
            status="healthy",
            version="2.6.0",
            timestamp=datetime.now(timezone.utc).isoformat() + "Z",
            yamls_loaded=yamls_loaded
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.now(timezone.utc).isoformat() + "Z"
            }
        )


@app.get(
    "/version",
    response_model=VersionResponse,
    status_code=status.HTTP_200_OK,
    summary="Version Information",
    description="Returns software version and release information."
)
async def version_info():
    """
    Version information endpoint.

    Returns:
        VersionResponse: Software version details

    Example:
        ```bash
        curl http://localhost:8000/version
        ```
    """
    environment = os.getenv("ENVIRONMENT", "development")

    return VersionResponse(
        version="2.6.0",
        release_date="2025-10-20",
        environment=environment
    )


@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="Root Endpoint",
    description="Returns API information and links."
)
async def root():
    """
    Root endpoint.

    Returns:
        dict: API information

    Example:
        ```bash
        curl http://localhost:8000/
        ```
    """
    return {
        "name": "HemoDoctor CDSS API",
        "version": "2.6.0",
        "description": "Clinical Decision Support System for CBC Analysis",
        "docs": "/docs",
        "health": "/health",
        "version_info": "/version"
    }


# ============================================================================
# Error Handlers
# ============================================================================

@app.exception_handler(ValueError)
async def value_error_handler(request, exc):
    """Handle ValueError exceptions."""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": str(exc)}
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    """Handle general exceptions."""
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"}
    )


# ============================================================================
# Main (for local development)
# ============================================================================

if __name__ == "__main__":
    import uvicorn

    # Run server (development only)
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
