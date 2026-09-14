"""
Innovation Features API
"""
from fastapi import APIRouter

from backend.app.schemas.common import APIResponse
from backend.app.schemas.innovation import (
    CropStressRequest, CropStressResponse,
    CropRotationRequest, CropRotationResponse,
    WaterYieldPredictionRequest, WaterYieldPredictionResponse
)
from backend.app.services.innovation_service import (
    analyze_crop_stress,
    recommend_crop_rotation,
    predict_water_yield
)

router = APIRouter()


@router.post("/stress", response_model=APIResponse[CropStressResponse])
async def crop_stress_analyze(request: CropStressRequest):
    """Analyze crop stress levels and provide recommendations"""
    try:
        stress_data = {
            "crop_type": request.crop_type,
            "disease_status": request.disease_status,
            "soil_moisture": request.soil_moisture,
            "temperature": request.temperature,
            "humidity": request.humidity,
            "growth_stage": request.growth_stage,
            "water_stress_indicators": request.water_stress_indicators
        }

        result = analyze_crop_stress(stress_data)

        return APIResponse(
            data=CropStressResponse(**result),
            message="Crop stress analysis completed successfully."
        )
    except Exception as exc:
        raise Exception(f"Crop stress analysis failed: {exc}") from exc


@router.post("/rotation", response_model=APIResponse[CropRotationResponse])
async def crop_rotation_recommend(request: CropRotationRequest):
    """Recommend next crop based on rotation principles"""
    try:
        rotation_data = {
            "current_crop": request.current_crop,
            "previous_crop": request.previous_crop,
            "soil_type": request.soil_type,
            "soil_ph": request.soil_ph,
            "season": request.season,
            "pest_history": request.pest_history
        }

        result = recommend_crop_rotation(rotation_data)

        return APIResponse(
            data=CropRotationResponse(**result),
            message="Crop rotation recommendation completed successfully."
        )
    except Exception as exc:
        raise Exception(f"Crop rotation recommendation failed: {exc}") from exc


@router.post("/prediction", response_model=APIResponse[WaterYieldPredictionResponse])
async def water_yield_predict(request: WaterYieldPredictionRequest):
    """Predict water requirements and yield estimates"""
    try:
        prediction_data = {
            "crop_type": request.crop_type,
            "area_hectares": request.area_hectares,
            "current_water_usage": request.current_water_usage,
            "soil_quality": request.soil_quality,
            "weather_conditions": request.weather_conditions,
            "irrigation_method": request.irrigation_method
        }

        result = predict_water_yield(prediction_data)

        return APIResponse(
            data=WaterYieldPredictionResponse(**result),
            message="Water and yield prediction completed successfully."
        )
    except Exception as exc:
        raise Exception(f"Water and yield prediction failed: {exc}") from exc