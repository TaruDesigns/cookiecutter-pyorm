# post_gen_project.py
import os
import shutil

from pathlib import Path

# Current path
path = Path(os.getcwd())

# Source path
parent_path = path.parent.absolute()

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)
        


# Check if user wants the folder
cookiecutter_var = "{{cookiecutter.add_db2}}"
db2folder_cookiecutter = "db{{ cookiecutter.db_2_name.lower().replace(' ', '_') }}"
add_folder = cookiecutter_var == "yes"

# User does not want folder so remove it
if not add_folder:
    folder_path = os.path.join(
        parent_path, 
        "{{ cookiecutter.repo_name }}", 
        db2folder_cookiecutter
    )
    print(folder_path)
    remove(folder_path)