# JudgeCode - AI Code Reviewer
### Proudly Made in France - Educational Purpose

## Table of Contents
- [Presentation](#presentation)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Guide](#setup-guide)
- [Usage](#usage)
- [FAQ](#faq)
- [Contributions](#contributing)

## Presentation
**JudgeCode** is a CLI AI-powered code reviewer.

The workflow is:
- Detect the file language from extension.
- Validate syntax locally for Python, JavaScript, and JSON.
- Validate syntax with AI for other languages.
- If syntax is valid, ask the AI for a structured code review.

The review includes:
- A grade (0-10)
- Good points
- Detected issues
- Actionable improvement suggestions

## Tech Stack
- Python 3.x
- OpenAI Python SDK (`openai`) with Groq-compatible endpoint
- Environment variables with `python-dotenv`
- JavaScript parsing with `esprima` (for local JS syntax validation)
- Python standard library modules:
- `ast` for Python syntax parsing
- `json` for JSON syntax validation and response parsing
- `os` for filesystem/path checks

## Project Structure
- `main.py`: CLI entry point and interactive loop.
- `providers/groq.py`: AI provider calls (syntax validation for Others + code review).
- `services/file_processor.py`: end-to-end processing pipeline.
- `services/syntax_validator.py`: local syntax validation for Python/JavaScript/JSON.
- `services/review_parser.py`: robust parsing of JSON AI outputs (including fenced JSON).
- `services/output_formatter.py`: colored console rendering.
- `shared/console.py`: console color helpers.

## Setup Guide
1. Clone the repository.
```git
git clone https://github.com/SH4D0W-fr/JudgeCode.git
```

2. Install dependencies.
```powershell
cd JudgeCode
pip install -r requirements.txt
```

4. (Optional) Copy `.env.example` to `.env` and set your API key.
	If no key is found, JudgeCode will ask for it in the console on first run and save it for next launches.

5. Run the CLI.
```powershell
py main.py
```

## Usage
1. Start the program.
2. Enter a file path when prompted.
3. Read syntax result and AI review output.
4. Enter another file path to continue.
5. Press `Ctrl+C` to quit.

Supported detection by extension:
- `.py` -> Python (local syntax validation)
- `.js` -> JavaScript (local syntax validation)
- `.json` -> JSON (local syntax validation)
- Any other extension -> Others (AI syntax validation)

## FAQ
**Q: Why does syntax validation differ by language?**  
A: Python, JavaScript, and JSON are validated locally for fast and deterministic checks. Other languages are validated by AI to keep broad language coverage.

**Q: What happens if AI returns malformed JSON?**  
A: The app tries multiple parsing strategies (raw JSON, fenced JSON blocks, extracted object). If parsing still fails, it reports a clear AI response format error.

**Q: Does the app stop after one file?**  
A: No. The CLI runs in a loop and lets you review multiple files until you press `Ctrl+C`.

**Q: Is this production-ready?**  
A: It is designed for educational use and iterative improvements. You can use it at your own risk.

## Contributing
Contributions are welcome. This project is educational, so clear code and good explanations matter as much as features.

### How to contribute
1. Fork the repository.
2. Create a branch from `main`.
3. Implement your changes with focused commits.
4. Test manually with sample files from `tests/`.
5. Open a Pull Request with a clear description.

Example:

```powershell
git checkout -b feat/better-syntax-handling
git add .
git commit -m "feat: improve syntax handling for unsupported extensions"
git push origin feat/better-syntax-handling
```

### Contribution guidelines
- Keep changes small and atomic.
- Preserve the current CLI behavior unless the PR explicitly changes it.
- If you modify prompts or AI output parsing, include at least one real input/output example in the PR description.
- Update the README when behavior changes.
- Prefer explicit error messages over silent failures.

### Good first contributions
- Add support for more extensions in language detection.
- Add automated tests for syntax validation and parser robustness.
- Improve docs and examples for setup and troubleshooting.
- Add more AI provider support.

### Pull Request checklist
- [ ] I tested my changes locally.
- [ ] I updated documentation when needed.
- [ ] I kept backwards compatibility or documented breaking behavior.
- [ ] I used clear commit messages.

Thanks for helping improve JudgeCode.
