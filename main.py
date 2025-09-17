import user_data
import user_shell
import commands
import logo
import os
import platform
import sys
from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style as PTStyle
import psutil
import socket
from tabulate import tabulate

BIN_PATH = "bin"  # folder where I keep all the py files
TWEAK_PATH = "tweak"  # fake tweak directory

# global tweak settings
tweak_settings = {
    "bg": "",
    "fg": ""
}

# list of colors
color_map = {
}

def get_local_ip():
    """
    Get the local IP address of the machine.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

def get_public_ip():
    """
    Get the public IP address using an external service (like an API).
    This can be replaced with any service like 'http://ifconfig.me'
    or similar. If you prefer not to use an external service, 
    you could handle it differently.
    """
    import requests
    try:
        response = requests.get('https://api.ipify.org?format=text')
        public_ip = response.text
    except requests.RequestException:
        public_ip = 'N/A'
    return public_ip

def get_disk_usage():
    """
    Get the disk usage for each disk and return it in a formatted way.
    """
    disks_info = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        # Skip loopback and virtual disks
        if 'loop' in partition.device or 'tmpfs' in partition.device:
            continue

        # Get disk usage
        usage = psutil.disk_usage(partition.mountpoint)
        disk_total_gb = usage.total / (1024 ** 3)  # Total disk space in GB
        disk_free_gb = usage.free / (1024 ** 3)  # Free disk space in GB
        disk_used_gb = usage.used / (1024 ** 3)  # Used disk space in GB
        disk_usage_percent = usage.percent  # Disk usage percentage

        # Determine color based on available space
        available_percent = (disk_free_gb / disk_total_gb) * 100
        if available_percent < 20:
            storage_color = Fore.RED  # Red for low storage
        elif available_percent < 50:
            storage_color = Fore.YELLOW  # Yellow for moderate storage
        else:
            storage_color = Fore.GREEN  # Green for healthy storage

        disks_info.append({
            "Device": partition.device,
            "Free (GB)": f"{disk_free_gb:.2f}",
            "Total (GB)": f"{disk_total_gb:.2f}",
            "Used (GB)": f"{disk_used_gb:.2f}",
            "Percent Used": f"{disk_usage_percent:.1f}%",
            "Storage": storage_color + f"{available_percent:.1f}%" + Style.RESET_ALL
        })
    
    return disks_info

def get_system_info():
    """
    Get system information to display alongside the logo.
    """
    user = os.getlogin()
    python_version = sys.version.split()[0]
    system = platform.system()  # Windows, Linux, Darwin (macOS)
    architecture = platform.architecture()[0]
    machine = platform.machine()  # x86_64, ARM, etc.
    processor = platform.processor()  # CPU information

    # Memory info
    try:
        memory = psutil.virtual_memory().total  # Total RAM in bytes
        memory_gb = memory / (1024 ** 3)  # Convert to GB
    except ImportError:
        memory_gb = "N/A"  # If psutil isn't available, show "N/A"

    # Get disk information for each disk
    disks_info = get_disk_usage()

    # System Info Table
    system_info = [
        ["User", user],
        ["OS", system],
        ["Python", python_version],
        ["Machine", machine],
        ["RAM", f"{memory_gb:.2f} GB"],
        ["Architecture", architecture],
        ["Processor", processor]
    ]

    # Display system info as a table
    sys_info_table = tabulate(system_info, headers=["Attribute", "Value"], tablefmt="pretty")

    # Disk Info Table
    disk_info_table = []
    for disk in disks_info:
        disk_info_table.append([disk["Device"], disk["Free (GB)"], disk["Total (GB)"], disk["Used (GB)"], disk["Percent Used"], disk["Storage"]])

    disk_info_table_str = tabulate(disk_info_table, headers=["Device", "Free (GB)", "Total (GB)", "Used (GB)", "Percent Used", "Storage"], tablefmt="pretty")

    # Combine both tables
    full_system_info = f"{sys_info_table}\n\nDisk Usage:\n{disk_info_table_str}"

    return full_system_info


    '''
        Color Preview:
        The function below will print all available colors from color_map.
        Colors are displayed as solid background blocks with their hex code text inside.
        Layout format:
           → 7 color blocks per row
           → 5 rows in total
           → A grid of 35 blocks maximum shown at once
        Each block automatically adjusts text color (white/black) depending on brightness,
        ensuring the hex code inside remains readable with the background.

    '''
color_map = {
    "Black": "#000000", "White": "#FFFFFF", "Gray": "#808080", "Light Gray": "#D3D3D3", "Dark Gray": "#333333",
    "Red": "#FF0000", "Dark Red": "#8B0000", "Pink": "#FFC0CB", "Light Pink": "#FFB6C1",
    "Hot Pink": "#FF69B4", "Deep Pink": "#FF1493", "Magenta": "#FF00FF",
    "Green": "#008000", "Lime": "#00FF00", "Dark Green": "#006400",
    "Light Green": "#90EE90", "Spring Green": "#00FF7F",
    "Blue": "#0000FF", "Navy": "#000080", "Royal Blue": "#4169E1",
    "Sky Blue": "#87CEEB", "Light Blue": "#ADD8E6", "Cyan": "#00FFFF",
    "Yellow": "#FFFF00", "Gold": "#FFD700", "Orange": "#FFA500", "Dark Orange": "#FF8C00",
    "Purple": "#800080", "Violet": "#EE82EE", "Orchid": "#DA70D6", "Indigo": "#4B0082",
    "Brown": "#A52A2A", "Saddle Brown": "#8B4513", "Chocolate": "#D2691E", "Tan": "#D2B48C"
}

def build_style():
    """
    Build prompt_toolkit style based on tweak_settings.
    """
    fg = tweak_settings["fg"].replace("\033[38;2;", "").replace("m", "")
    bg = tweak_settings["bg"].replace("\033[48;2;", "").replace("m", "")

    fg_parts = fg.split(";") if fg else []
    bg_parts = bg.split(";") if bg else []

    fg_hex = "#{:02x}{:02x}{:02x}".format(*map(int, fg_parts)) if len(fg_parts) == 3 else None
    bg_hex = "#{:02x}{:02x}{:02x}".format(*map(int, bg_parts)) if len(bg_parts) == 3 else None

    color_str = ""
    if fg_hex:
        color_str += f"fg:{fg_hex} "
    if bg_hex:
        color_str += f"bg:{bg_hex}"

    styles = {"": color_str.strip()} if color_str else {}
    return PTStyle.from_dict(styles) if styles else None


def tweaked_input(prompt_text: str) -> str:
    """
    Input with tweaks applied to the whole input area (while typing).
    """
    style = build_style()
    return prompt(prompt_text, style=style).strip()


def show_bin_file_info(filename):
    descriptions = {
        "commands.py": "commands.py handles root commands like clear, list, exit, and invalid command messages.",
        "user_shell.py": "user_shell.py contains the user shell loop and user command handling logic.",
        "user_data.py": "user_data.py manages user data loading, saving, and storage.",
    }
    return descriptions.get(filename, f"No description available for {filename}")


def hex_to_rgb(hex_code: str):
    """Convert #RRGGBB to tuple (r,g,b)"""
    hex_code = hex_code.lstrip("#")
    return int(hex_code[0:2], 16), int(hex_code[2:4], 16), int(hex_code[4:6], 16)


def print_color_blocks():
    """Print all colors in 7 columns with hex code inside each block (no extra spaces)."""
    items = list(color_map.items())
    per_row = 7

    for i in range(0, len(items), per_row):
        row = items[i:i+per_row]
        line = ""
        for name, hex_code in row:
            r, g, b = hex_to_rgb(hex_code)

            brightness = (r*0.299 + g*0.587 + b*0.114)
            text_color = "\033[38;2;0;0;0m" if brightness > 186 else "\033[38;2;255;255;255m"

            block = f"\033[48;2;{r};{g};{b}m{text_color} {hex_code} \033[0m"
            line += block + " "
        print(line)


def root_loop():
    current_dir = "root"

    while True:
        # choose prompt
        if current_dir == "root":
            prompt_text = ":root/ "
        elif current_dir == "bin":
            prompt_text = "?:bin/ "
        else:
            prompt_text = "~tweak/ "

        command = tweaked_input(prompt_text)

        # switch directory to bin
        if command == "cd bin" and current_dir == "root":
            if os.path.exists(BIN_PATH) and os.path.isdir(BIN_PATH):
                current_dir = "bin"
            else:
                print("bin directory does not exist.")
            continue

        # switch directory to tweak
        if command == "cd tweak" and current_dir == "root":
            current_dir = "tweak"
            continue

        # go back to root from bin or tweak
        if command == "cd .." and current_dir in ("bin", "tweak"):
            current_dir = "root"
            continue

        # exit program
        if command == "exit":
            print("exiting root...")
            break

        if current_dir == "root":
            match command:
                case "sys-shell peak":
                    logo_content = logo.logo
                    system_info = get_system_info()
                    print(f"{logo_content:<50} {system_info}")

                case "cd user":
                    if "user" in user_data.users:
                        user_data.current_user = "user"
                    elif user_data.users:
                        user_data.current_user = list(user_data.users.keys())[0]
                    else:
                        user_data.current_user = "user"
                        user_data.users["user"] = {
                            "full_name": "Default User",
                            "contact": "0000000000",
                            "address": "Default Address",
                            "email": "user@example.com",
                            "directories": {}
                        }
                        user_data.save_users()
                    user_shell.user_shell_loop()

                case "list":
                    print(Fore.CYAN + "user" + Style.RESET_ALL)
                    print(Fore.CYAN + "bin" + Style.RESET_ALL)
                    print(Fore.CYAN + "tweak" + Style.RESET_ALL)

                case _:
                    commands.handle_root_command(command)

        elif current_dir == "bin":
            if command in os.listdir(BIN_PATH):
                print(show_bin_file_info(command))
            elif command == "list":
                files = [f for f in os.listdir(BIN_PATH) if f.endswith(".py")]
                for f in files:
                    print(Fore.GREEN + f"  {f}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "[SYSTEM]: Command failed. Reason: Invalid syntax." + Style.RESET_ALL)

        elif current_dir == "tweak":
            if command.startswith("tweak:bg-color:"):
                color_code = command.split(":", 2)[2]
                tweak_settings["bg"] = f"\033[48;2;{int(color_code[1:3],16)};{int(color_code[3:5],16)};{int(color_code[5:7],16)}m"
                print(f"Background color set to {color_code}")
            elif command.startswith("tweak:f-color:"):
                color_code = command.split(":", 2)[2]
                tweak_settings["fg"] = f"\033[38;2;{int(color_code[1:3],16)};{int(color_code[3:5],16)};{int(color_code[5:7],16)}m"
                print(f"Foreground color set to {color_code}")
            elif command == "list":
                print("tweak:bg-color:<hex>")
                print("tweak:f-color:<hex>")
                print("colors")
            elif command == "colors":
                print_color_blocks()
            else:
                print(Fore.RED + "[TWEAK]: Unknown tweak command." + Style.RESET_ALL)


if __name__ == "__main__":
    user_data.load_users()
    root_loop()
    root_loop()
