ANALYSIS_PROMPT = """
Analyze the following code snippet and provide a structured JSON response evaluating its quality.

Code to analyze:
```
{code}
```

Respond strictly in valid JSON format with the following keys:
- "score": A score from 0 to 100 representing overall code quality.
- "keep": A list of strings. DO NOT provide objects or dictionaries. Each string should be in the format: "Feature name & Explanation".
- "remove": A list of strings. DO NOT provide objects or dictionaries. Each string should be in the format: "Feature name & Explanation".
- "improve": A list of strings. DO NOT provide objects or dictionaries. Each string should be in the format: "Feature name & Explanation".

JSON Response Example:
{{
  "score": 90,
  "keep": ["Function modularity & Improves testability", "Type hints & Enhances reliability"],
  "remove": ["Redundant comments & Reduces clutter"],
  "improve": ["Error handling & Prevents crashes"]
}}
"""
