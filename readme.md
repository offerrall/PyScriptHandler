## Description

PyScriptHandler is an ultra-lightweight CLI tool designed to make managing Python scripts as simple and straightforward as possible.

The idea is that you can have a list of scripts that work on Windows, macOS, and Linux, and you can run them from anywhere on your system.

### Key Features:

- **Simplicity**: With fewer than 200 lines of code, PyScriptHandler is extremely easy to understand and modify to suit your needs.
- **Portability**: The aim is to unify the way Python scripts are run across any operating system.
- **Zero Configuration**: There are no configuration files to edit, no dependencies to install. Simply install the script and start using it.
- **Simple Commands**: The commands are simple and easy to remember. No need to look up documentation every time you want to run a script.
- **Alias Friendly**: You can create aliases for commands and run your scripts with a single command.

### Why Use PyScriptHandler?
This project was born out of my own need for a simple tool where I could store and run my Python scripts, which was as minimalist as possible and required no additional configuration. If you find yourself in a similar situation, then PyScriptHandler is for you.

### Installation

PyScriptHandler can be easily installed by cloning the repository and running the installation script.


```bash
git clone https://github.com/offerrall/PyScriptHandler.git
cd PyScriptHandler
pip install .

```

### Comandos

- `psh -h`: Shows the help message.
- `psh <script_name>`: Runs the specified script.
- `psh list`: Lists all the scripts in the list.
- `psh add <script_path>`: Adds a new script to the list.
- `psh remove <script_name>`: Removes a script from the list.
- `psh find <script_name>`: Searches for a script in the list.
- `psh pwd`: Shows the current script directory path.

### Examples

```bash
# Runs a script
psh hello_world

# Shows the list of scripts
psh list

# Adds a new script
psh add /path/to/script.py

# Removes a script
psh remove hello_world

# Finds a script
psh find hello_world

# Shows the current script directory path
psh pwd
```

### Licencia
[MIT](https://choosealicense.com/licenses/mit/)