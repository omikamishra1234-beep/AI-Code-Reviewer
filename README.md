# AI-Code-Reviewer

PHD project for Generative AI with Large Language Models (MSAI-630-M50)

---

## **Gemini Code Analyzer API**

The **Gemini Code Analyzer API** is a FastAPI-based application that leverages Google's Gemini AI to analyze code snippets. It provides structured feedback on code quality, including areas to keep, remove, and improve.

---

## **Features**
- Analyze code snippets for quality, inefficiencies, and improvements.
- Provides structured feedback in JSON format with categories: `keep`, `remove`, and `improve`.
- Includes a health check endpoint to verify the API's status.

---

## **Technologies Used**
- **Backend**: FastAPI
- **LLM**: Google Gemini AI
- **Other Libraries**:
  - `uvicorn` (ASGI server)
  - `google-generativeai` (Gemini API integration)
  - `python-dotenv` (Environment variable management)
  - `pydantic` (Data validation and settings management)

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd AI-Code-Reviewer


### **2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
# On Windows:
# .\venv\Scripts\activate

### **3. Install Dependencies
```bash
pip install -r [requirements.txt](http://_vscodecontentref_/1)
