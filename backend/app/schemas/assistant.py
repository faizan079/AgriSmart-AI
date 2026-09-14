"""
Farmer Assistant Schemas
"""
from pydantic import BaseModel, Field


class AssistantRequest(BaseModel):
    """Request schema for farmer assistant"""
    question: str = Field(..., description="Farmer's question")
    context: str = Field(default="", description="Additional context (optional)")


class AssistantResponse(BaseModel):
    """Response schema for farmer assistant"""
    answer: str = Field(..., description="Assistant's answer")
    confidence: float = Field(..., description="Confidence in the answer")
    related_topics: list[str] = Field(default_factory=list, description="Related topics for further discussion")