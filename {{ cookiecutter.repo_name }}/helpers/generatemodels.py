from sqlalchemy import create_engine
from sqlacodegen import CodeGenerator
from .helpers import urlgenerator_postgres


def create_models(dbtype: str, fileout: str):
    # Create an SQLAlchemy engine to connect to your PostgreSQL database
    engine = create_engine(urlgenerator_postgres())
    # Create a CodeGenerator instance and generate models
    generator = CodeGenerator(engine)
    models = generator.generate_code()
    # Print the generated models
    with open(fileout, "w") as f:
        f.write(models)
