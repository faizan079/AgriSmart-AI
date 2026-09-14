"""
Innovation Features Schemas
"""
from pydantic import BaseModel, Field


class CropStressRequest(BaseModel):
    """Request schema for crop stress analysis"""
    crop_type: str = Field(..., description="Crop type")
    disease_status: str = Field(..., description="Current disease status (healthy, diseased)")
    soil_moisture: float = Field(..., ge=0.0, le=100.0, description="Soil moisture percentage")
    temperature: float = Field(..., description="Current temperature in Celsius")
    humidity: float = Field(..., ge=0.0, le=100.0, description="Current humidity percentage")
    growth_stage: str = Field(..., description="Growth stage (seedling, growing, mature)")
    water_stress_indicators: str = Field(default="none", description="Visible water stress signs")


class CropStressResponse(BaseModel):
    """Response schema for crop stress analysis"""
    stress_level: str = Field(..., description="Overall stress level (low, medium, high)")
    stress_factors: list[str] = Field(default_factory=list, description="Identified stress factors")
    risk_assessment: str = Field(..., description="Risk assessment details")
    recommendations: list[str] = Field(default_factory=list, description="Recommendations to reduce stress")
    monitoring_required: bool = Field(..., description="Whether close monitoring is required")


class CropRotationRequest(BaseModel):
    """Request schema for crop rotation recommendation"""
    current_crop: str = Field(..., description="Current crop being grown")
    previous_crop: str = Field(default="", description="Previous crop grown")
    soil_type: str = Field(..., description="Soil type")
    soil_ph: float = Field(..., ge=0.0, le=14.0, description="Soil pH")
    season: str = Field(..., description="Current season")
    pest_history: str = Field(default="none", description="Any pest issues in current crop")


class CropRotationResponse(BaseModel):
    """Response schema for crop rotation recommendation"""
    recommended_next_crop: str = Field(..., description="Recommended next crop")
    rotation_benefits: list[str] = Field(default_factory=list, description="Benefits of this rotation")
    soil_health_impact: str = Field(..., description="Impact on soil health")
    timing_recommendation: str = Field(..., description="When to rotate")
    alternatives: list[str] = Field(default_factory=list, description="Alternative rotation options")


class WaterYieldPredictionRequest(BaseModel):
    """Request schema for water and yield prediction"""
    crop_type: str = Field(..., description="Crop type")
    area_hectares: float = Field(..., ge=0.0, description="Area in hectares")
    current_water_usage: float = Field(..., ge=0.0, description="Current water usage in liters")
    soil_quality: str = Field(..., description="Soil quality (poor, moderate, good)")
    weather_conditions: str = Field(..., description="Expected weather conditions")
    irrigation_method: str = Field(..., description="Irrigation method (drip, sprinkler, flood)")


class WaterYieldPredictionResponse(BaseModel):
    """Response schema for water and yield prediction"""
    estimated_water_requirement: float = Field(..., description="Estimated water requirement in liters")
    estimated_yield: float = Field(..., description="Estimated yield in kg")
    yield_range: str = Field(..., description="Expected yield range")
    water_efficiency_score: float = Field(..., description="Water efficiency score")
    optimization_tips: list[str] = Field(default_factory=list, description="Tips to optimize water and yield")