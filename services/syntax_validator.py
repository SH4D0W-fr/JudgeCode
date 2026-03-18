############################################################################################
## SYNTAX_VALIDATOR.PY                                                                    ##
## This file contains the logic for validating syntax in different programming languages. ##
############################################################################################


import ast
import esprima
import json


def detect_language(file_path):
    if file_path.endswith('.py'):
        return 'Python'
    if file_path.endswith('.js'):
        return 'JavaScript'
    if file_path.endswith('.json'):
        return 'JSON'
    return 'Others'


def validate_syntax(code, language):
    if language == 'Python':
        try:
            ast.parse(code)
            return None
        except SyntaxError as e:
            return {
                "line": e.lineno,
                "error": e.msg,
            }

    if language == 'JavaScript':
        try:
            esprima.parseScript(code)
            return None
        except esprima.Error as e:
            return {
                "line": getattr(e, 'lineNumber', None),
                "error": getattr(e, 'description', None) or getattr(e, 'message', None) or str(e),
            }

    if language == 'JSON':
        try:
            json.loads(code)
            return None
        except json.JSONDecodeError as e:
            return {
                "line": e.lineno,
                "error": e.msg,
            }

    return {
        "line": None,
        "error": f"Unsupported file type for language: {language}",
    }
