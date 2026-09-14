"""
Irrigation & Weather Schemas
"""
from pydantic import BaseModel, Field


class IrrigationRequest(BaseModel):
    """Request schema for irrigation analysis"""
    crop_type: str = Field(..., description="Crop type (e.g., 'rice', 'wheat', 'maize')")
    soil_moisture: float = Field(..., ge=0.0, le=100.0, description="Soil moisture percentage")
    growth_stage: str = Field(..., description="Growth stage (e.g., 'seedling', 'growing', 'mature')")
    temperature: float = Field(..., description="Current temperature in Celsius")
    humidity: float = Field(..., ge=0.0, le=100.0, description="Current humidity percentage")
    rainfall_forecast: float = Field(default=0.0, description="Expected rainfall in mm")


class IrrigationResponse(BaseModel):
    """Response schema for irrigation analysis"""
    irrigation_needed: bool = Field(..., description="Whether irrigation is needed")
    recommendation: str = Field(..., description="Detailed recommendation")
    water_amount: float = Field(..., description="Suggested water amount in mm")
    urgency: str = Field(..., description="Urgency level (low, medium, high)")
    next_check_time: str = Field(..., description="Suggested time for next check")


class WeatherRequest(BaseModel):
    """Request schema for weather intelligence"""
    location: str = Field(..., description="Location for weather data")
    current_temp: float = Field(..., description="Current temperature in Celsius")
    current_humidity: float = Field(..., ge=0.0, le=100.0, description="Current humidity percentage")
    rainfall_expected: bool = Field(default=False, description="Is rainfall expected?")
    wind_speed: float = Field(default=0.0, description="Wind speed in km/h")


class WeatherResponse(BaseModel):
    """Response schema for weather intelligence"""
    current_conditions: str = Field(..., description="Summary of current weather")
    risk_assessment: str = Field(..., description="Weather-related risk assessment")
    recommendations: list[str] = Field(default_factory=list, description="Weather-based recommendations")
    action_required: bool = Field(..., description="Whether immediate action is required")
    priority_actions: list[str] = Field(default_factory=list, description="Priority actions if any")