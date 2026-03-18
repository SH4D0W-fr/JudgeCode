import os


class ConsoleColors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GRAY = "\033[90m"


def enable_ansi_colors_on_windows():
    if os.name == "nt":
        # Enables ANSI escape sequences in many Windows terminals.
        os.system("")


def color_text(text, color):
    return f"{color}{text}{ConsoleColors.RESET}"


def cprint(text, color):
    print(color_text(text, color))
