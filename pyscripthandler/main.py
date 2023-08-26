import sys
import os

from .commands import *

def main() -> None:
    script_folder = 'scripts/'

    if not os.path.exists(script_folder):
        os.mkdir(script_folder)

    if len(sys.argv) < 2:
        print("No command provided. Use -h for help.")
        return

    command = sys.argv[1]
    
    teorical_path = os.path.join(script_folder, command)
    if os.path.exists(teorical_path):
        handle_execute(teorical_path, script_folder, sys.argv[2:])
    
    elif command == '-h':
        handle_help()
    
    elif command == 'add':
        if len(sys.argv) < 3:
            print("No script path provided.")
        else:
            handle_add(sys.argv[2], script_folder)
    
    elif command == 'list':
        handle_list(script_folder)
            
    elif command == 'find':
        if len(sys.argv) < 3:
            print("No query provided.")
        else:
            handle_find(sys.argv[2], script_folder)

    elif command == 'pwd':
        full_path = os.path.abspath(script_folder)
        print(full_path)

    elif command == 'remove':
        if len(sys.argv) < 3:
            print("No script name provided.")
        else:
            handle_remove(sys.argv[2], script_folder)
    
    else:
        print(f"Unknown command or script: {command}")

if __name__ == "__main__":
    main()