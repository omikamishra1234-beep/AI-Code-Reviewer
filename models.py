from typing import List, Optional
from pydantic import BaseModel, Field

class CodeInput(BaseModel):
    code: str
    language: Optional[str] = "python"

class AnalysisResponse(BaseModel):
    score: int = Field(..., description="A score from 0 to 100 representing code quality.")
    keep: List[str] = Field(..., description="Features to retain, with explanation.")
    remove: List[str] = Field(..., description="Features to remove, with explanation.")
    improve: List[str] = Field(..., description="Features to improve, with explanation.")
