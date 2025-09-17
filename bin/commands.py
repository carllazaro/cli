import os
import user_data
from colorama import init, Fore, Style

def clear_screen():
    # Clear terminal screen for Windows or Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_root_command(command):
    # Handle commands typed at the root prompt

    if command == "clear":
        clear_screen()

    elif command == "list":
        print("user")

    else:
        # Show error message for unknown commands
        print(Fore.RED + "[SYSTEM]: Command failed. Reason: Invalid syntax." + Style.RESET_ALL)
        '''
        CURRENT COMMANDS:
            user
            list
            clear
            exit
        '''
