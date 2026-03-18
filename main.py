############################################################################################
## MAIN.PY                                                                                ##
## This is the main entry point for the application. It initializes the application,      ##
## sets up the necessary configurations, and starts the main event loop.                  ##  
############################################################################################

# Welcome message and application banner
print(r"""
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
)
print("Initializing application...")

# Imports
import sys
import os
import services.file_processor as fp

# When everything is ready
print("Everything ready !")
print("Please, enter the path to the file you want to review")

# Main function to get the file path from the user
def main():
   path = input("> File path : ")
   return path

path = main()

# Check if the file exists
def check_file(path):
    if not os.path.isfile(path):
        print("File not found.")
        main()
    else:
        print(f"File found: {path}")
        fp.process_file(path)

check_file(path)