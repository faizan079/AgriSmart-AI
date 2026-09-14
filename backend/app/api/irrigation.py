"""
Irrigation & Weather API
"""
from fastapi import APIRouter

from backend.app.schemas.common import APIResponse
from backend.app.schemas.irrigation import IrrigationRequest, IrrigationResponse, WeatherRequest, WeatherResponse
from backend.app.services.irrigation_service import analyze_irrigation_needs
from backend.app.services.weather_service import analyze_weather_conditions

router = APIRouter()


@router.post("/analyze", response_model=APIResponse[IrrigationResponse])
async def irrigation_analyze(request: IrrigationRequest):
    """Analyze irrigation needs based on crop and soil conditions"""
    try:
        user_conditions = {
            "crop_type": request.crop_type,
            "soil_moisture": request.soil_moisture,
            "growth_stage": request.growth_stage,
            "temperature": request.temperature,
            "humidity": request.humidity,
            "rainfall_forecast": request.rainfall_forecast
        }

        result = analyze_irrigation_needs(user_conditions)

        return APIResponse(
            data=IrrigationResponse(**result),
            message="Irrigation analysis completed successfully."
        )
    except Exception as exc:
        raise Exception(f"Irrigation analysis failed: {exc}") from exc


@router.post("/weather", response_model=APIResponse[WeatherResponse])
async def weather_analyze(request: WeatherRequest):
    """Analyze weather conditions and provide farming recommendations"""
    try:
        weather_data = {
            "location": request.location,
            "current_temp": request.current_temp,
            "current_humidity": request.current_humidity,
            "rainfall_expected": request.rainfall_expected,
            "wind_speed": request.wind_speed
        }

        result = analyze_weather_conditions(weather_data)

        return APIResponse(
            data=WeatherResponse(**result),
            message="Weather analysis completed successfully."
        )
    except Exception as exc:
        raise Exception(f"Weather analysis failed: {exc}") from exc