import os
import subprocess

from db{{ cookiecutter.__db1normalname__ }}.urlgen import urlgenerator as urlgen{{ cookiecutter.__db1normalname__ }}
{% if cookiecutter.add_db2 == "yes" %}
from db{{ cookiecutter.__db2normalname__ }}.urlgen import urlgenerator as urlgen{{ cookiecutter.__db2normalname__ }}
{% endif %}

def create_models(connectionstring: str, fileout: str):
    command = f"sqlacodegen {connectionstring} --outfile {fileout}"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Models generated successfully: {fileout}")
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed with error: {e}")



if __name__ == "__main__":
    # Models for DB 1
    print("Generating models for db{{ cookiecutter.__db1normalname__ }}")
    file_db1 = os.path.join( 
            "db{{ cookiecutter.__db1normalname__ }}",
            "models.py"
    )    
    url_db1 = urlgen{{ cookiecutter.__db1normalname__ }}()
    create_models(connectionstring=url_db1, fileout=file_db1)
    {% if cookiecutter.add_db2 == "yes" %}    
    print("Generating models for db{{ cookiecutter.__db2normalname__ }}")
    file_db2 = os.path.join( 
            "db{{ cookiecutter.__db2normalname__ }}",
            "models.py"
    )    
    url_db2 = urlgen{{ cookiecutter.__db2normalname__ }}()
    create_models(connectionstring=url_db2, fileout=file_db2)
    {% endif %}    