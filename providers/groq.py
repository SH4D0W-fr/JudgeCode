############################################################################################
## GROQ.PY                                                                                ##
## This file contains the implementation for the GROQ API provider.                       ##
############################################################################################

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class GroqProvider:
    def __init__(self):
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        self.client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
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