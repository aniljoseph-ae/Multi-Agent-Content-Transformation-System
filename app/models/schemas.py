from pydantic import BaseModel, Field
from typing import Optional, Dict

class TransformRequest(BaseModel):
    """pydantic model: transformation request"""
    content: str = Field(..., description="Input content to transform")
    target_style: str = Field(..., description="Target style (e.g., formal, casual)")
    target_format: str = Field(..., description="Target format (e.g., markdown, html)")
    complexity_level: Optional[str] = Field(
        "medium", 
        description="Complexity level (low, medium, high)"
    )
    feedback: Optional[str] = Field(
        None, 
        description="User feedback for refinement"
    )

class TransformResponse(BaseModel):
    """pydantic model:  transformation results"""
    transformed_content: str = Field(..., description="Transformed content")
    quality_metrics: Dict[str, float] = Field(
        ..., 
        description="Quality assessment metrics"
    )