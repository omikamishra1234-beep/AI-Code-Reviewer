import json
import google.generativeai as genai
from fastapi import HTTPException
from models import AnalysisResponse, CodeInput
from config import GEMINI_MODEL_NAME, GEMINI_API_KEY
from prompts import ANALYSIS_PROMPT

def flatten_feedback(items) -> list[str]:
    """
    Ensures that items in keep, remove, and improve are strings.
    If the model returns objects, flattens them into 'feature & explanation' format.
    """
    flattened = []
    for item in items:
        if isinstance(item, dict):
            feature = item.get("feature", item.get("issue", item.get("item", "")))
            explanation = item.get("explanation", item.get("reason", item.get("recommendation", "")))
            if feature and explanation:
                flattened.append(f"{feature} & {explanation}")
            elif feature:
                flattened.append(str(feature))
            elif explanation:
                flattened.append(str(explanation))
            else:
                flattened.append(json.dumps(item))
        else:
            flattened.append(str(item))
    return flattened

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
        print(result_json)
        
        # Post-process to ensure list of strings as requested
        for key in ["keep", "remove", "improve"]:
            if key in result_json and isinstance(result_json[key], list):
                result_json[key] = flatten_feedback(result_json[key])
        
        return AnalysisResponse(**result_json)

    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Gemini returned invalid JSON.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
