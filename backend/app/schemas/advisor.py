"""
Agentic Advisor Schemas
"""
from pydantic import BaseModel, Field


class AdvisorRequest(BaseModel):
    """Request schema for agentic advisor"""
    crop_type: str = Field(default="tomato", description="Current crop type")
    disease_status: str = Field(default="healthy", description="Disease detection result")
    soil_moisture: float = Field(default=60.0, ge=0.0, le=100.0, description="Current soil moisture")
    weather_forecast: str = Field(default="good", description="Weather forecast (good, moderate, poor)")
    growth_stage: str = Field(default="growing", description="Current growth stage")


class AdvisorResponse(BaseModel):
    """Response schema for agentic advisor"""
    decision: str = Field(..., description="Recommended action/decision")
    reasoning: str = Field(..., description="Explanation for the decision")
    priority: str = Field(..., description="Priority level (low, medium, high, urgent)")
    action_steps: list[str] = Field(default_factory=list, description="Specific action steps")
    monitoring_required: bool = Field(..., description="Whether monitoring is required")
    follow_up_time: str = Field(..., description="Recommended follow-up time")