from .utils import *
import os

def handle_execute(script_path: str, extra_args: list[str]) -> None:
    execute_script(script_path, extra_args)

def handle_add(script_path: str, target_folder: str) -> None:
    name_script = script_path.split("/")[-1].replace(".py", "")
    if name_script in list_scripts(target_folder):
        print(f"Script with name {name_script} already exists.")
        return
    if not script_path.endswith(".py"):
        print("Script must be a python file.")
        return
    add_script(script_path, target_folder)
    print(f"Added script: {script_path}")

def handle_remove(script_name: str, target_folder: str) -> None:
    full_path = os.path.join(target_folder, script_name + ".py")
    if not os.path.exists(full_path):
        print(f"Script with name {script_name} does not exist.")
        return
    remove_script(full_path)
    print(f"Removed script: {script_name}")

def handle_list(target_folder: str) -> None:
    scripts = list_scripts(target_folder)
    if not scripts:
        print("No scripts found.")
        return
    print("Scripts:")
    for script in scripts:
        print(script)

def handle_find(query: str, target_folder: str) -> None:
    results = find_script(query, target_folder)
    if results:
        print("Scripts found:")
        for result in results:
            print(result)
    else:
        print(f"No scripts found containing the query: {query}")

def handle_help() -> None:
    
    print("""
Usage: psh [command] [args]

Commands:

Show this help message.
    -h, --help:
Execute the script with the given name and arguments.
    ["script_name"] [args]:
Add a script to the script folder.
    add <script_path>
Remove a script from the script folder.
    remove <script_name>
List all scripts in the script folder
    list
Find all scripts containing the query.
    find <query>
Print the directory of the script folder.
    pwd
""")   