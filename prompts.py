ANALYSIS_PROMPT = """
Analyze the following code snippet and provide a structured JSON response identifying bugs, inefficiencies, or potential improvements.

Code to analyze:
```
{code}
```

Respond strictly in valid JSON format with the following keys:
"summary": A brief high-level overview of the code's quality.
"feedback": A list of objects, each containing:
  - "category": Choose one of ["Bugs", "Inefficiencies", "Improvements"]
  - "issue": A concise description of the problem or opportunity.
  - "recommendation": Actionable steps to address the issue.

JSON Response:
"""
