import json
import google.generativeai as genai
from fastapi import HTTPException
from models import AnalysisResponse, CodeInput
from config import GEMINI_MODEL_NAME, GEMINI_API_KEY
from prompts import ANALYSIS_PROMPT

async def analyze_code_logic(input_data: CodeInput) -> AnalysisResponse:
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API Key is not configured.")

    try:
        model = genai.GenerativeModel(GEMINI_MODEL_NAME)
        prompt = ANALYSIS_PROMPT.format(code=input_data.code)
        
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                response_mime_type="application/json",
            )
        )

        result_json = json.loads(response.text)
        return AnalysisResponse(**result_json)

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Gemini returned invalid JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
