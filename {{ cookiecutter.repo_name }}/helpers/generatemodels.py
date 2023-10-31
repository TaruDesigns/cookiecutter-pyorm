from sqlalchemy import create_engine
from sqlacodegen import CodeGenerator


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
