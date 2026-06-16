import json
import re

from ai.llm import ask_llm


def extract_facts(text):

    prompt = f"""
Extract useful facts from the following entry.

Return ONLY JSON.

Entry:
{text}
"""

    response = ask_llm(prompt)

    # Remove markdown code fences
    response = re.sub(
        r"```json\s*|\s*```",
        "",
        response
    ).strip()

    try:
        return json.loads(response)

    except Exception as e:
        print("JSON Parse Error:", e)
        print("Response:", response)
        return {}