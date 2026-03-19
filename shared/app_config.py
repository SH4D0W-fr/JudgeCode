############################################################################################
## APP_CONFIG.PY                                                                           ##
## This file manages persistent user configuration for CLI executable usage.               ##
############################################################################################

import json
import os

from shared.console import ConsoleColors, cprint


APP_NAME = "JudgeCode"
CONFIG_FILE_NAME = "config.json"


def _get_config_directory():
    if os.name == "nt":
        appdata = os.getenv("APPDATA")
        if appdata:
            return os.path.join(appdata, APP_NAME)

    return os.path.join(os.path.expanduser("~"), ".config", APP_NAME.lower())


def _get_config_file_path():
    return os.path.join(_get_config_directory(), CONFIG_FILE_NAME)


def _load_config():
    config_file = _get_config_file_path()
    if not os.path.exists(config_file):
        return {}

    try:
        with open(config_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def _save_config(config):
    config_dir = _get_config_directory()
    os.makedirs(config_dir, exist_ok=True)

    config_file = _get_config_file_path()
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def get_or_prompt_groq_api_key():
    env_api_key = os.getenv("GROQ_API_KEY", "").strip()
    if env_api_key:
        return env_api_key

    config = _load_config()
    stored_api_key = str(config.get("groq_api_key", "")).strip()
    if stored_api_key:
        return stored_api_key

    cprint("No GROQ API key found.", ConsoleColors.YELLOW)
    cprint("Please enter your GROQ API key for first-time setup.", ConsoleColors.CYAN)

    while True:
        try:
            api_key = input("> GROQ API key: ").strip()
        except EOFError as exc:
            raise RuntimeError(
                "No GROQ API key configured and interactive input is unavailable."
            ) from exc

        if not api_key:
            cprint("API key cannot be empty. Try again.", ConsoleColors.YELLOW)
            continue

        config["groq_api_key"] = api_key
        _save_config(config)
        cprint("API key saved for next runs.", ConsoleColors.GREEN)
        return api_key