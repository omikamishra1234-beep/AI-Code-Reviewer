from typing import List, Optional
from pydantic import BaseModel, Field

class CodeInput(BaseModel):
    code: str
    language: Optional[str] = "python"

class FeedbackItem(BaseModel):
    category: str = Field(..., description="Bugs, Inefficiencies, or Improvements")
    issue: str
    recommendation: str

class AnalysisResponse(BaseModel):
    summary: str
    feedback: List[FeedbackItem]
