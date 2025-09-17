# op-CLI 

A simple, modular Python shell-like interface with support for users, customizable prompts, command handling, and color tweaks via ANSI escape codes and `prompt_toolkit`.

---

## Requirements

Install the dependencies with:

```bash
pip install colorama prompt_toolkit
```

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/carllazaro/op-CLI.git
cd op-CLI
```

### Project Structure

```plaintext
📁 op-CLI/
├── main.py               # Entry point of the shell system
├── user_data.py          # Manages user information and storage
├── user_shell.py         # Handles user shell commands and operations
├── commands.py           # Handles root-level commands
├── bin/                  # Optional: store scripts to explore (e.g. test.py)
├── tweak/                # Optional: fake tweak directory (for prompt color customization)
└── users.txt             # Auto-generated user data file
```

### 3. Run the Application

```bash
python main.py
```

---

## Shell Commands Overview

### Root Shell (`:root/` prompt)

```bash
cd user            # Enters the user shell
cd bin             # Switch to bin directory
cd tweak           # Switch to tweak prompt
cd ..              # Go back to root
list               # Lists available root folders
clear              # Clears the terminal
exit               # Exits the root shell
```

### User Shell (`<username>@user$` prompt)

```bash
add carl           # Add a new user
set carl           # Switch to user 'carl'
list               # Show files/folders for current user
create file notes  # Create a file named 'notes'
create folder docs # Create a folder named 'docs'
remove notes       # Delete an item named 'notes'
list user          # List all users
info carl          # Show detailed info about 'carl'
exit               # Return to root
clear              # Clear screen
```

### Tweak Prompt (`~tweak/` prompt)

```bash
tweak:bg-color:#000000     # Change background color of prompt
tweak:f-color:#FFFFFF      # Change foreground/text color
colors                     # Show available color hex codes
list                       # List tweak commands
cd ..                      # Return to root
```

---

## Color Customization

From the `tweak` prompt, use color hex codes to personalize your shell:

```bash
tweak:bg-color:#1e1e1e
tweak:f-color:#00ffcc
```

Preview all supported colors:

```bash
colors
```
<div>
  <img width="501" height="158" alt="image" src="https://github.com/user-attachments/assets/c1077bf3-2ef6-421f-8150-f9268b8cdc45" />
</div>

---

## Optional: Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

Then install the required dependencies again:

```bash
pip install colorama prompt_toolkit
```

---

## Data Persistence

- All users are saved to `users.txt` (auto-generated).
- Each user can store named files/folders in their own "virtual directory."

---

## Tips

- Organize Python modules into `bin/` to simulate additional tools/scripts.
- Customize prompt styles via the `tweak` interface.
- Extend `commands.py` to add more system-wide commands.

---

## Done!

You're all set to build on top of this shell interface.
```bash
python main.py
```














=======
# op-CLI 

A simple, modular Python shell-like interface with support for users, customizable prompts, command handling, and color tweaks via ANSI escape codes and `prompt_toolkit`.

---

## Requirements

Install the dependencies with:

```bash
pip install colorama prompt_toolkit
```

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/carllazaro/op-CLI.git
cd op-CLI
```

### Project Structure

```plaintext
📁 op-CLI/
├── main.py               # Entry point of the shell system
├── user_data.py          # Manages user information and storage
├── user_shell.py         # Handles user shell commands and operations
├── commands.py           # Handles root-level commands
├── bin/                  # Optional: store scripts to explore (e.g. test.py)
├── tweak/                # Optional: fake tweak directory (for prompt color customization)
└── users.txt             # Auto-generated user data file
```

### 3. Run the Application

```bash
python main.py
```

---

## Shell Commands Overview

### Root Shell (`:root/` prompt)

```bash
cd user            # Enters the user shell
cd bin             # Switch to bin directory
cd tweak           # Switch to tweak prompt
cd ..              # Go back to root
list               # Lists available root folders
clear              # Clears the terminal
exit               # Exits the root shell
```

### User Shell (`<username>@user$` prompt)

```bash
add carl           # Add a new user
set carl           # Switch to user 'carl'
list               # Show files/folders for current user
create file notes  # Create a file named 'notes'
create folder docs # Create a folder named 'docs'
remove notes       # Delete an item named 'notes'
list user          # List all users
info carl          # Show detailed info about 'carl'
exit               # Return to root
clear              # Clear screen
```

### Tweak Prompt (`~tweak/` prompt)

```bash
tweak:bg-color:#000000     # Change background color of prompt
tweak:f-color:#FFFFFF      # Change foreground/text color
colors                     # Show available color hex codes
list                       # List tweak commands
cd ..                      # Return to root
```

---

## Color Customization

From the `tweak` prompt, use color hex codes to personalize your shell:

```bash
tweak:bg-color:#1e1e1e
tweak:f-color:#00ffcc
```

Preview all supported colors:

```bash
colors
```
<div>
  <img width="501" height="158" alt="image" src="https://github.com/user-attachments/assets/c1077bf3-2ef6-421f-8150-f9268b8cdc45" />
</div>

---

## Optional: Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

Then install the required dependencies again:

```bash
pip install colorama prompt_toolkit
```

---

## Data Persistence

- All users are saved to `users.txt` (auto-generated).
- Each user can store named files/folders in their own "virtual directory."

---

## Tips

- Organize Python modules into `bin/` to simulate additional tools/scripts.
- Customize prompt styles via the `tweak` interface.
- Extend `commands.py` to add more system-wide commands.

---

## Done!

You're all set to build on top of this shell interface.
```bash
python main.py
```
