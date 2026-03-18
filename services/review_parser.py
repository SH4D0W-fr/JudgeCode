import json
import re


def parse_ai_response(ai_response):
    try:
        return json.loads(ai_response)
    except (json.JSONDecodeError, TypeError):
        if isinstance(ai_response, str):
            fenced_match = re.search(r"```(?:json)?\\s*(\\{[\\s\\S]*?\\})\\s*```", ai_response, re.IGNORECASE)
            if fenced_match:
                candidate = fenced_match.group(1)
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    pass

            object_match = re.search(r"(\\{[\\s\\S]*\\})", ai_response)
            if object_match:
                candidate = object_match.group(1)
                try:
                    return json.loads(candidate)
                except json.JSONDecodeError:
                    pass

        return {
            "raw": ai_response,
            "error": "Invalid JSON from AI",
        }
