# 🤖 AI Code Reviewer

PHD Project for Generative AI with Large Language Models (MSAI-630-M50)

## 📌 Overview

The AI Code Reviewer is a FastAPI-based application that uses Google Gemini AI to analyze code snippets and provide structured feedback.

It helps developers:
- Identify code quality issues  
- Detect inefficiencies  
- Get actionable improvements  

## 🚀 Features

- Analyze code using Gemini LLM  
- Structured output: keep, remove, improve  
- FastAPI backend  
- Health check endpoint  
- Easy API integration  

## 🛠 Tech Stack

- Backend: FastAPI  
- LLM: Google Gemini  
- Server: Uvicorn  
- Validation: Pydantic  
- Env Management: python-dotenv  

## 📂 Project Structure

```
AI-Code-Reviewer/
│
├── main.py                  # FastAPI entry point
├── analyzer.py              # Gemini API logic
├── models.py                # Pydantic schemas
├── requirements.txt         # Dependencies
├── .env.dist                # Env template
├── .env                     # Secrets (ignored in git)
│
├── routes/
│   └── review.py            # API endpoints
│
└── README.md
```

## ⚙️ Setup Instructions (End-to-End)

### 1. Clone the Repository

```
git clone <repository-url>
cd AI-Code-Reviewer
```

### 2. Create Virtual Environment (IMPORTANT)

```
python3 -m venv venv
```

Activate it:

```
source venv/bin/activate      # macOS/Linux
# Windows:
# .\venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```
cp .env.dist .env
```

Edit `.env` file:

```
GEMINI_API_KEY="your_api_key_here"
GEMINI_MODEL_NAME="gemini-2.5-flash"
```

### 5. Run the Application

```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 🌐 API Endpoints

### Health Check

GET /health

Response:
```
{
  "status": "ok"
}
```

### Analyze Code

POST /analyze

Request:
```
{
  "code": "def add(a,b): return a+b"
}
```

## 📊 Example Response

```
{
  "keep": ["Simple function logic"],
  "remove": ["Poor spacing"],
  "improve": ["Add type hints", "Add docstring", "Follow PEP8"]
}
```

## 🧠 How It Works

1. Client sends code to API  
2. FastAPI receives request  
3. Code is sent to Gemini  
4. Gemini analyzes it  
5. Structured response returned  

## 🧪 Testing

### cURL

```
curl -X POST "http://localhost:8000/analyze" \
-H "Content-Type: application/json" \
-d '{"code": "def add(a,b): return a+b"}'
```

### Swagger UI

Open:
http://localhost:8000/docs

## 🐳 Docker (Optional)

Dockerfile:

```
FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Run:

```
docker build -t ai-code-reviewer .
docker run -p 8000:8000 ai-code-reviewer
```

## 🔐 Security Notes

- Do not commit `.env`  
- Keep API keys secure  

