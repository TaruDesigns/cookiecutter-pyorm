import os
import ast

from sqlalchemy import create_engine
from sqlacodegen import CodeGenerator
from db{{ cookiecutter.__db1normalname__ }}.urlgen import urlgenerator as urlgen{{ cookiecutter.__db1normalname__ }}
{% if cookiecutter.add_db2 == "yes" %}
from db{{ cookiecutter.__db2normalname__ }}.urlgen import urlgenerator as urlgen{{ cookiecutter.__db2normalname__ }}
{% endif %}

def create_models(connectionstring: str, fileout: str):
    # Create an SQLAlchemy engine to connect to your PostgreSQL database
    if connectionstring is None:
        raise ValueError("Empty connection string")
    engine = create_engine(connectionstring)
    # Create a CodeGenerator instance and generate models
    generator = CodeGenerator(engine)
    models = generator.generate_code()
    # Print the generated models
    if fileout is None:
        fileout = "models.py"
    with open(fileout, "w") as f:
        f.write(models)


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