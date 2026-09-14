"""
Agentic Advisor API
"""
from fastapi import APIRouter

from backend.app.schemas.common import APIResponse
from backend.app.schemas.advisor import AdvisorRequest, AdvisorResponse
from backend.app.services.advisor_service import analyze_farm_situation

router = APIRouter()


@router.post("/analyze", response_model=APIResponse[AdvisorResponse])
async def advisor_analyze(request: AdvisorRequest):
    """Analyze farm situation and provide actionable recommendations"""
    try:
        advisor_data = {
            "crop_type": request.crop_type,
            "disease_status": request.disease_status,
            "soil_moisture": request.soil_moisture,
            "weather_forecast": request.weather_forecast,
            "growth_stage": request.growth_stage
        }

        result = analyze_farm_situation(advisor_data)

        return APIResponse(
            data=AdvisorResponse(**result),
            message="Advisor analysis completed successfully."
        )
    except Exception as exc:
        raise Exception(f"Advisor analysis failed: {exc}") from exc