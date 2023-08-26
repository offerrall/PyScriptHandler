import os
import zipfile
import shutil

def add_script(script_path: str, target_folder: str) -> None:
    shutil.copy(script_path, target_folder)

def remove_script(script_name: str, target_folder: str) -> None:
    os.remove(os.path.join(target_folder, script_name))

def list_scripts(target_folder: str) -> list[str]:
    return [s for s in os.listdir(target_folder) if s.endswith('.py')]

def find_script(query: str, target_folder: str) -> list[str]:
    return [s for s in os.listdir(target_folder) if query.lower() in s.lower()]

def export_scripts(target_folder: str, zip_name: str) -> None:
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(target_folder):
            for file in files:
                zipf.write(os.path.join(root, file))

def import_scripts(zip_name: str, target_folder: str) -> None:
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(target_folder)
