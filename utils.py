import os
import shutil
import subprocess
import platform

def execute_script(script_path: str, extra_args: list[str]) -> None:
    python_path = 'python' if platform.system() == 'Windows' else 'python3'
    subprocess.run([python_path, script_path] + extra_args)

def add_script(script_path: str, target_folder: str) -> None:
    shutil.copy(script_path, target_folder)

def remove_script(script_name: str, target_folder: str) -> None:
    os.remove(os.path.join(target_folder, script_name))

def list_scripts(target_folder: str) -> list[str]:
    return [s for s in os.listdir(target_folder) if s.endswith('.py')]

def find_script(query: str, target_folder: str) -> list[str]:
    return [s for s in os.listdir(target_folder) if query.lower() in s.lower()]