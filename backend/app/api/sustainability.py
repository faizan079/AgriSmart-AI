"""
Sustainability Score API
"""
from fastapi import APIRouter

from backend.app.schemas.common import APIResponse
from backend.app.schemas.sustainability import SustainabilityRequest, SustainabilityResponse
from backend.app.services.sustainability_service import calculate_sustainability_score

router = APIRouter()


@router.post("/score", response_model=APIResponse[SustainabilityResponse])
async def sustainability_score(request: SustainabilityRequest):
    """Calculate sustainability score based on farming practices"""
    try:
        farming_data = {
            "crop_type": request.crop_type,
            "water_usage": request.water_usage,
            "fertilizer_usage": request.fertilizer_usage,
            "pesticide_usage": request.pesticide_usage,
            "crop_yield": request.crop_yield,
            "irrigation_efficiency": request.irrigation_efficiency,
            "soil_health": request.soil_health,
            "energy_usage": request.energy_usage
        }

        result = calculate_sustainability_score(farming_data)

        return APIResponse(
            data=SustainabilityResponse(**result),
            message="Sustainability score calculated successfully."
        )
    except Exception as exc:
        raise Exception(f"Sustainability analysis failed: {exc}") from exc