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
    db2folder_cookiecutter = "db{{ cookiecutter.__db2normalname__ }}"
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

def add_to_gitignore(line):
    file_path = os.path.join(
            parent_path, 
            "{{ cookiecutter.repo_name }}", 
            ".gitignore"
        )
    with open(file_path, 'a') as gitignore_file:
        gitignore_file.write('\n' + line)
        print(f"Added {line} to gitignore!")

if __name__ == "__main__":
    print("Post Repo Creation Cleanup...")
    remove_db2 = remove_db2()
    add_to_gitignore("secret.py")
    print("Repo created! Make sure you check the README.md to init the models")
    print("WARNING: Create a virtual environment and install the created template dependencies before proceeding")