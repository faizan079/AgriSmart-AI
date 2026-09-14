from typing import List, Optional

from pydantic import BaseModel, Field


class TopPrediction(BaseModel):
    class_label: str
    confidence: float


class DiseasePrediction(BaseModel):
    class_label: str = Field(..., description="Predicted disease/healthy class")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    is_healthy: bool = Field(False, description="Whether the crop is healthy")
    precaution: str = Field(..., description="Recommended precaution/action")
    top_predictions: List[TopPrediction] = Field(
        default_factory=list,
        description="Top 3 predictions with confidence",
    )
