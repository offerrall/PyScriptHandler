import sys
from utils import *
from os.path import exists
import subprocess

def handle_execute(script_name: str, target_folder: str, extra_args: list[str]) -> None:
    script_path = os.path.join(target_folder, script_name)
    if os.path.exists(script_path):
        subprocess.run(['python', script_path] + extra_args)
    else:
        print(f"No such script: {script_name}")

def handle_add(script_path: str, target_folder: str) -> None:
    add_script(script_path, target_folder)

def handle_remove(script_name: str, target_folder: str) -> None:
    remove_script(script_name, target_folder)

def handle_list(target_folder: str) -> None:
    scripts = list_scripts(target_folder)
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

def handle_export(zip_name: str, target_folder: str) -> None:
    export_scripts(target_folder, zip_name)

def handle_import(zip_name: str, target_folder: str) -> None:
    import_scripts(zip_name, target_folder)

def main() -> None:
    script_folder = 'scripts/'

    if not os.path.exists(script_folder):
        os.mkdir(script_folder)

    if len(sys.argv) < 2:
        print("No command provided. Use -h for help.")
        return

    command = sys.argv[1]
    
    if os.path.exists(os.path.join(script_folder, f"{command}.py")):
        handle_execute(f"{command}.py", script_folder, sys.argv[2:])
        
    elif command == 'add':
        if len(sys.argv) < 3:
            print("No script path provided.")
        else:
            handle_add(sys.argv[2], script_folder)
            
    elif command == 'remove':
        if len(sys.argv) < 3:
            print("No script name provided.")
        else:
            handle_remove(sys.argv[2], script_folder)
            
    elif command == 'list':
        handle_list(script_folder)
        
    elif command == 'find':
        if len(sys.argv) < 3:
            print("No query provided.")
        else:
            handle_find(sys.argv[2], script_folder)
            
    elif command == 'export':
        if len(sys.argv) < 3:
            print("No zip file name provided.")
        else:
            handle_export(sys.argv[2], script_folder)
            
    elif command == 'import':
        if len(sys.argv) < 3:
            print("No zip file name provided.")
        else:
            handle_import(sys.argv[2], script_folder)
    
    else:
        print(f"Unknown command or script: {command}")

if __name__ == "__main__":
    main()



