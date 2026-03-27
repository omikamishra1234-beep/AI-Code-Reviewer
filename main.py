from fastapi import FastAPI
from models import CodeInput, AnalysisResponse
from services import analyze_code_logic
from config import GEMINI_MODEL_NAME

app = FastAPI(title="Gemini Code Analyzer API")

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_code(input_data: CodeInput):
    """
    Accepts code input and returns structured feedback using Gemini.
    """
    return await analyze_code_logic(input_data)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": GEMINI_MODEL_NAME}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
