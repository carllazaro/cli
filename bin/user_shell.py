import user_data
from colorama import init, Fore, Style

def clear_screen():
    # Clear the terminal screen (works on Windows and Unix)
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_user_command(command):
    # Handle commands typed by the user in the user shell

    if command == "cd .." or command == "exit":
        # Exit the user shell and go back to root
        return "exit"

    elif command == "clear":
        # Clear the screen when user types clear
        clear_screen()

    elif command == "list user":
        # Show a list of all users
        #print("users:")
        for username in user_data.users:
            print(Style.BRIGHT + Fore.GREEN + username + Style.RESET_ALL)

    elif command.startswith("set "):
        # Switch to a different user if they exist
        new_user = command.split(" ", 1)[1]
        if new_user in user_data.users:
            user_data.current_user = new_user
            print(f"switched to user: {new_user}")
        else:
            print(f"user '{new_user}' does not exist, use 'add' to create it.")

    elif command.startswith("add "):
        # Add a new user by asking for details
        new_user = command.split(" ", 1)[1]
        if new_user in user_data.users:
            print(f"user '{new_user}' already exists.")
        else:
            full_name = input("Enter full name: ").strip()
            contact = input("Enter contact number: ").strip()
            address = input("Enter address: ").strip()
            email = input("Enter email: ").strip()

            user_data.users[new_user] = {
                "full_name": full_name,
                "contact": contact,
                "address": address,
                "email": email,
                "directories": {}
            }
            user_data.save_users()
            print(f"User '{new_user}' added.")

    elif command.startswith("remove "):
        # Remove a file or folder from current user's directories
        name = command.split(" ", 1)[1]
        if user_data.current_user not in user_data.users:
            print(Fore.RED + "error: Current user does not exist." + Style.RESET_ALL)
            return

        directories = user_data.users[user_data.current_user].get("directories", {})
        if name in directories:
            del directories[name]
            user_data.save_users()
            print(f"'{name}' removed.")
        else:
            print(f"'{name}' not found.")

    elif command == "list":
        # List files/folders for current user
        if user_data.current_user not in user_data.users:
            print(Fore.RED + "error: Current user does not exist." + Style.RESET_ALL)
            return

        directories = user_data.users[user_data.current_user].get("directories", {})
        if not directories:
            print("no files or folders.")
        else:
            print("contents:")
            for name, dtype in directories.items():
                print(f"  [{dtype}] {name}")

    elif command.startswith("create "):
        # Create a new file or folder for the current user
        parts = command.split(" ", 2)
        if len(parts) < 3:
            print("usage: create <file|folder> <name>")
        else:
            dtype, name = parts[1], parts[2]
            if dtype not in ("file", "folder"):
                print("type must be 'file' or 'folder'.")
            else:
                if user_data.current_user not in user_data.users:
                    print("error: Current user does not exist.")
                    return

                directories = user_data.users[user_data.current_user].setdefault("directories", {})
                if name in directories:
                    print(f"{name} already exists.")
                else:
                    directories[name] = dtype
                    user_data.save_users()
                    print(f"{dtype.capitalize()} '{name}' created.")

    elif command.startswith("info "):
        # Show details about a user
        query_user = command.split(" ", 1)[1]
        if query_user in user_data.users:
            info = user_data.users[query_user]
            print(f"Username: {query_user}")
            print(f"Full Name: {info['full_name']}")
            print(f"Contact: {info['contact']}")
            print(f"Address: {info['address']}")
            print(f"Email: {info['email']}")
        else:
            print(f"user '{query_user}' not found.")

    else:
        # Just print "sent to the void: command" if command is unknown
        print(f"sent to the void: {Fore.MAGENTA + command + Style.RESET_ALL}")

    return None

def user_shell_loop():
    # Main loop to keep accepting user commands
    while True:
        command = input(f"{Fore.GREEN + user_data.current_user + Style.RESET_ALL}@user$ ").strip()
        result = handle_user_command(command)
        if result == "exit":
            print("returning to root...")
            break
