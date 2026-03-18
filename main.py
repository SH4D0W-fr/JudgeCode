############################################################################################
## MAIN.PY                                                                                ##
## This is the main entry point for the application. It initializes the application,      ##
## sets up the necessary configurations, and starts the main event loop.                  ##  
############################################################################################

import os

import services.file_processor as fp
from shared.console import ConsoleColors, cprint, enable_ansi_colors_on_windows

enable_ansi_colors_on_windows()

BANNER = r"""
    $$$$$\                 $$\                      $$$$$$\                  $$\           
    \__$$ |                $$ |                    $$  __$$\                 $$ |          
        $$ |$$\   $$\  $$$$$$$ | $$$$$$\   $$$$$$\  $$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\  
        $$ |$$ |  $$ |$$  __$$ |$$  __$$\ $$  __$$\ $$ |      $$  __$$\ $$  __$$ |$$  __$$\ 
$$\   $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|
\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$\ \$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ 
 \______/  \______/  \_______| \____$$ | \_______| \______/  \______/  \_______| \_______|
                                        $$\   $$ |                                                  
                                        \$$$$$$  |                                                  
                                         \______/                                                   
"""


def print_banner():
    print(ConsoleColors.RED + BANNER + ConsoleColors.RESET)
    cprint("Initializing application...", ConsoleColors.BLUE)

def prompt_file_path():
    while True:
        path = input("> File path : ").strip()
        if os.path.isfile(path):
            cprint(f"File found: {path}", ConsoleColors.GREEN)
            return path
        cprint("File not found. Try again.", ConsoleColors.YELLOW)


def main():
    print_banner()
    cprint("Everything ready !", ConsoleColors.CYAN)
    print("Please, enter the path to the file you want to review")

    while True:
        try:
            path = prompt_file_path()
            fp.process_file(path)
            print("\nYou can review another file, or press Ctrl+C to quit.")
        except KeyboardInterrupt:
            print("\nExiting JudgeCode. Bye!")
            break


if __name__ == "__main__":
    main()