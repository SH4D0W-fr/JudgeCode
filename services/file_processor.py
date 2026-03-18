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

    if language == 'Others':
        ai_syntax_raw = groq_provider.validate_syntax_with_ai(code, language)
        ai_syntax = parse_ai_response(ai_syntax_raw)

        if isinstance(ai_syntax, dict):
            is_valid = ai_syntax.get("is_valid")
            if is_valid is False:
                return {
                    "type": "syntax_error",
                    "line": ai_syntax.get("line"),
                    "error": ai_syntax.get("error") or "Syntax error detected by AI",
                }
            if is_valid is not True:
                return {
                    "type": "review_error",
                    "line": None,
                    "error": "AI syntax validation returned an invalid format",
                }
        else:
            return {
                "type": "review_error",
                "line": None,
                "error": "AI syntax validation returned a non-JSON response",
            }

        syntax_error = None
    else:
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

    result = check_error(file_path, code_language)

    if result.get("type") in ["syntax_error", "review_error"]:
        print_error(file_path, result.get("line"), result.get("error"))
        return

    print_success(file_path)
    print_review(result.get("review", {}))