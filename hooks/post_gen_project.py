# post_gen_project.py
import subprocess
import os
import platform
import sys
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
        
def remove_db2():
    # Check if user wants the folder
    cookiecutter_var = "{{cookiecutter.add_db2}}"
    db2folder_cookiecutter = "db{{ cookiecutter.db_2_name.lower().replace(' ', '_') }}"
    remove_db2 = cookiecutter_var == "no"

    # User does not want folder so remove it
    if remove_db2:
        folder_path = os.path.join(
            parent_path, 
            "{{ cookiecutter.repo_name }}", 
            db2folder_cookiecutter
        )
        remove(folder_path)
        print("Database 2 Files Removed!")
    return remove_db2



if __name__ == "__main__":
    print("Post Repo Creation Cleanup...")
    remove_db2 = remove_db2()
    print("Repo created! Make sure you check the README.md to init the models")
    