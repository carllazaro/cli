import os
import json

USER_FILE = "users.txt"  # file to store user info

users = {}  # dictionary to hold all user data
current_user = "user"  # default current user

def load_users():
    global users
    # load users from file if it exists
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            for line in f:
                parts = line.strip().split('|')
                if len(parts) == 5:
                    # if directories missing, use empty dict
                    username, full_name, contact, address, email = parts
                    dir_json = "{}"
                elif len(parts) == 6:
                    # directories stored as json string
                    username, full_name, contact, address, email, dir_json = parts
                else:
                    # skip bad lines
                    continue

                users[username] = {
                    "full_name": full_name,
                    "contact": contact,
                    "address": address,
                    "email": email,
                    "directories": json.loads(dir_json)
                }
    else:
        # if no file, create a default user and save it
        users["user"] = {
            "full_name": "Default User",
            "contact": "0000000000",
            "address": "Default Address",
            "email": "user@example.com",
            "directories": {}
        }
        save_users()

def save_users():
    # save all users to the file
    with open(USER_FILE, "w") as f:
        for username, info in users.items():
            dir_json = json.dumps(info.get("directories", {}))
            line = f"{username}|{info['full_name']}|{info['contact']}|{info['address']}|{info['email']}|{dir_json}\n"
            f.write(line)
