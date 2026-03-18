############################################################################################
## FILE_PROCESSOR.PY                                                                      ##
## This file contains the logic for processing files.                                     ##
############################################################################################

# Imports
import os, sys
import ast # For parsing Python code
import esprima # For parsing JavaScript code

# Language detection based on file extension
def detect_language(file_path):
    if file_path.endswith('.py'):
        return 'Python'
    elif file_path.endswith('.js'):
        return 'JavaScript'
    elif file_path.endswith('.java'):
        return 'Java'
    else:
        return 'Unknown'

# Error checking based on language
def check_error(file_path, language):
    print(f"Checking for errors in {file_path} as {language} code...")
    if language == 'Python':
        try:
            ast.parse(open(file_path).read())
            return None
        except SyntaxError as e:
            return {
                "line": e.lineno,
                "error": e.msg
            }
    elif language == 'JavaScript':
        try:
            esprima.parseScript(open(file_path).read())
            return None
        except esprima.Error as e:
            return {
                "line": e.lineNumber,
                "error": e.description
            }
    else:
        return None

# Main function to process the file
def process_file(file_path):
    print(f"Processing file: {file_path}")
    code_language = detect_language(file_path)
    print(f"Detected language: {code_language}")

    if code_language == 'Unknown':
        print("Unsupported file type.")
        return
    elif code_language == 'Python':
        errors = check_error(file_path, code_language)
        if errors:
            print(f"Errors found in {file_path}:")
            for error in errors:
                print(f"  Line {error['line']}: {error['error']}")
        else:
            print(f"No errors found in {file_path}.")
    elif code_language == 'JavaScript':
        errors = check_error(file_path, code_language)
        if errors:
            print(f"Errors found in {file_path}:")
            for error in errors:
                print(f"  Line {error['line']}: {error['error']}")
        else:
            print(f"No errors found in {file_path}.")