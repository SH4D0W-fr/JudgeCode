############################################################################################
## GROQ.PY                                                                                ##
## This file contains the implementation for the GROQ API provider.                       ##
############################################################################################

from openai import OpenAI
import os
from dotenv import load_dotenv
from shared.app_config import get_or_prompt_groq_api_key

load_dotenv()

class GroqProvider:
    def __init__(self):
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        api_key = get_or_prompt_groq_api_key()
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1"
        )

    def review(self, code: str):
        prompt = f"""
        You are a code review expert.

        Your task is to review the following code and provide feedback on its quality, potential issues, and suggestions for improvement. Please analyze the code and return a structured JSON response with the following format:
        {{
            "good": [],
            "issues": [],
            "suggestions": [],
            "score": number
        }}
        You absolutely must return a JSON object with this exact structure. Do not include any explanations, markdown, or code blocks. If you cannot review the code, return an object with an "error" field describing the issue.
        Please, provide specific feedback on the code, including any potential bugs, security vulnerabilities, performance issues, or areas for improvement. Also, give an overall score for the code quality on a scale from 0 to 10, where 10 is excellent and 0 is very poor.

        If the file contains others things than code, please ignore them and only review the code part.
        Please, write the response in the original language, even if the code is not in English.

        Code:
        {code}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    def validate_syntax_with_ai(self, code: str, language: str):
        prompt = f"""
        You are a strict syntax validator.

        Check only syntax for the given language. Do not review style, performance, architecture, or best practices.
        Return ONLY a JSON object with this exact shape:
        {{
            "is_valid": boolean,
            "line": number | null,
            "error": string | null
        }}

        Rules:
        - If syntax is valid: is_valid=true, line=null, error=null.
        - If syntax is invalid: is_valid=false, line=<best line number or null>, error=<clear syntax error message>.
        - Return no markdown, no code block, no explanation.

        Language: {language}

        Code:
        {code}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content