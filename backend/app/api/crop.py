"""
Crop Recommendation API
"""
from fastapi import APIRouter

from backend.app.schemas.common import APIResponse
from backend.app.schemas.crop import CropRecommendationRequest, CropRecommendationResponse
from backend.app.services.crop_service import recommend_crop

router = APIRouter()


@router.post("/recommend", response_model=APIResponse[CropRecommendationResponse])
async def crop_recommend(request: CropRecommendationRequest):
    """Recommend suitable crop based on soil and climate conditions"""
    try:
        user_conditions = {
            "soil_type": request.soil_type.lower(),
            "soil_ph": request.soil_ph,
            "temperature": request.temperature,
            "humidity": request.humidity,
            "rainfall": request.rainfall,
            "water_availability": request.water_availability.lower(),
            "season": request.season.lower(),
            "location": request.location.lower(),
            "previous_crop": request.previous_crop.lower()
        }

        result = recommend_crop(user_conditions)

        return APIResponse(
            data=CropRecommendationResponse(**result),
            message="Crop recommendation completed successfully."
        )
    except Exception as exc:
        raise Exception(f"Crop recommendation failed: {exc}") from exc