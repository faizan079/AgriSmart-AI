"""
Sustainability Score Schemas
"""
from pydantic import BaseModel, Field


class SustainabilityRequest(BaseModel):
    """Request schema for sustainability analysis"""
    water_usage: float = Field(default=5000.0, ge=0.0, description="Water usage in liters per day")
    fertilizer_usage: float = Field(default=50.0, ge=0.0, description="Fertilizer usage in kg per season")
    pesticide_usage: float = Field(default=20.0, ge=0.0, description="Pesticide usage in liters per season")
    crop_yield: float = Field(default=1000.0, ge=0.0, description="Crop yield in kg per season")
    crop_type: str = Field(default="tomato", description="Type of crop grown")
    irrigation_efficiency: float = Field(default=70.0, ge=0.0, le=100.0, description="Irrigation efficiency percentage")
    soil_health: str = Field(default="moderate", description="Soil health status (poor, moderate, good)")
    energy_usage: float = Field(default=100.0, description="Energy usage in kWh per season")


class SustainabilityResponse(BaseModel):
    """Response schema for sustainability analysis"""
    sustainability_score: float = Field(..., ge=0.0, le=100.0, description="Overall sustainability score (0-100)")
    score_breakdown: dict = Field(..., description="Breakdown of scores by category")
    rating: str = Field(..., description="Overall rating (Excellent, Good, Fair, Poor)")
    water_efficiency_score: float = Field(..., description="Water efficiency score")
    resource_usage_score: float = Field(..., description="Resource usage score")
    environmental_impact_score: float = Field(..., description="Environmental impact score")
    recommendations: list[str] = Field(default_factory=list, description="Recommendations for improvement")
    improvement_areas: list[str] = Field(default_factory=list, description="Areas needing improvement")