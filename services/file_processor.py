############################################################################################
## FILE_PROCESSOR.PY                                                                      ##
## This file contains the logic for processing files.                                     ##
############################################################################################

from providers.groq import GroqProvider
from shared.console import enable_ansi_colors_on_windows
from services.output_formatter import print_error, print_review, print_success
from services.review_parser import parse_ai_response
from services.syntax_validator import detect_language, validate_syntax

# Initialize the GROQ provider
groq_provider = GroqProvider()

# Error checking based on language
def check_error(file_path, language):
    print(f"Checking for errors in {file_path} as {language} code...")
    with open(file_path, encoding='utf-8') as f:
        code = f.read()

    syntax_error = validate_syntax(code, language)
    if syntax_error:
        return {
            "type": "syntax_error",
            **syntax_error
        }

    try:
        ai_response = groq_provider.review(code)
    except Exception as e:
        return {
            "type": "review_error",
            "line": None,
            "error": f"AI review failed: {str(e)}"
        }

    return {
        "type": "review",
        "review": parse_ai_response(ai_response)
    }

# Main function to process the file
def process_file(file_path):
    enable_ansi_colors_on_windows()

    print(f"Processing file: {file_path}")
    code_language = detect_language(file_path)
    print(f"Detected language: {code_language}")

    if code_language == 'Others':
        print("Unsupported file type.")
        return

    result = check_error(file_path, code_language)

    if result.get("type") in ["syntax_error", "review_error"]:
        print_error(file_path, result.get("line"), result.get("error"))
        return

    print_success(file_path)
    print_review(result.get("review", {}))