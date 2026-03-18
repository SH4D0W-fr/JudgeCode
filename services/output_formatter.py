from shared.console import ConsoleColors, cprint


def print_error(file_path, line, error):
    cprint(f"Errors found in {file_path}:", ConsoleColors.RED)
    cprint(f"  Line {line}: {error}", ConsoleColors.RED)


def print_success(file_path):
    cprint(f"No syntax errors found in {file_path}.", ConsoleColors.GREEN)


def print_review(review):
    cprint("\nGROQ Review Response:", ConsoleColors.BLUE)

    if not isinstance(review, dict):
        cprint("Review format is invalid.", ConsoleColors.YELLOW)
        print(review)
        return

    if "error" in review and "raw" in review:
        cprint("AI returned a non-JSON response.", ConsoleColors.YELLOW)
        cprint("Raw response:", ConsoleColors.GRAY)
        print(review.get("raw"))
        return

    score = review.get("score")
    if isinstance(score, (int, float)):
        if score >= 8:
            score_color = ConsoleColors.GREEN
        elif score >= 5:
            score_color = ConsoleColors.YELLOW
        else:
            score_color = ConsoleColors.RED
        cprint(f"Score: {score}/10", score_color)

    good_points = review.get("good", [])
    if isinstance(good_points, list) and good_points:
        cprint("\nGood points:", ConsoleColors.GREEN)
        for item in good_points:
            cprint(f"  + {item}", ConsoleColors.GREEN)

    issues = review.get("issues", [])
    if isinstance(issues, list) and issues:
        cprint("\nIssues:", ConsoleColors.RED)
        for item in issues:
            cprint(f"  - {item}", ConsoleColors.RED)

    suggestions = review.get("suggestions", [])
    if isinstance(suggestions, list) and suggestions:
        cprint("\nSuggestions:", ConsoleColors.CYAN)
        for item in suggestions:
            cprint(f"  * {item}", ConsoleColors.CYAN)
