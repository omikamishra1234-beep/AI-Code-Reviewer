from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import CodeInput, AnalysisResponse
from services import analyze_code_logic
from config import GEMINI_MODEL_NAME

app = FastAPI(title="Gemini Code Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

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
