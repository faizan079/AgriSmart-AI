"""
Crop Recommendation Schemas
"""
from pydantic import BaseModel, Field


class CropRecommendationRequest(BaseModel):
    """Request schema for crop recommendation"""
    soil_type: str = Field(..., description="Soil type (e.g., 'clay', 'sandy', 'loamy', 'black')")
    soil_ph: float = Field(..., ge=0.0, le=14.0, description="Soil pH value (0-14)")
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., ge=0.0, le=100.0, description="Humidity percentage")
    rainfall: float = Field(..., description="Annual rainfall in mm")
    water_availability: str = Field(..., description="Water availability (e.g., 'high', 'medium', 'low')")
    season: str = Field(..., description="Season (e.g., 'summer', 'winter', 'monsoon', 'spring')")
    location: str = Field(default="", description="Location/region (optional)")
    previous_crop: str = Field(default="", description="Previous crop grown (optional)")


class CropRecommendationResponse(BaseModel):
    """Response schema for crop recommendation"""
    recommended_crop: str = Field(..., description="Recommended crop")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    reasoning: str = Field(..., description="Explanation for recommendation")
    alternative_crops: list[str] = Field(default_factory=list, description="Alternative crop options")
    tips: list[str] = Field(default_factory=list, description="Farming tips for recommended crop")