from . import secret



def urlgenerator(
    type: str = None,
    user: str = None,
    password: str = None,
    server: str = None,
    db: str = None,
    port: int = None,
) -> str:
    """Generate connection string

    Args:
        type (str): type of database
        user (str): username
        password (str): password
        server (str): server (hostname or ip)
        db (str): database name (or full path if SQLite)
        port (int): port (if left empty, it will use defaults)

    Returns:
        _type_: _description_
    """
    type = secret.type if type is None else type
    user = secret.username if user is None else user
    password = secret.password if password is None else password
    server = secret.host if server is None else server
    db = secret.name if db is None else db
    port = secret.port if port is None else port
    
    if type.lower() == "postgresql":
        # pip install psycopg2
        if port is None or port == "":
            port = 5432
        return f"postgresql://{user}:{password}@{server}:{port}/{db}"
    elif type.lower() == "mysql":
        # pip install mysql-connector-python
        if port is None or port == "":
            port = 3306
        return f"mysql+mysqlconnector://{user}:{password}@{server}:{port}/{db}"
    elif type.lower() == "sqlite":
        if port is None or port == "":
            port = 5432
        return f"sqlite:///{db}"
    elif type.lower() == "sqlserver":
        # pip install pyodbc
        if port is None or port == "":
            port = 1433
        return (
            f"mssql+pyodbc://{user}:{password}@{server}:{port}/{db}?driver=SQL+Server"
        )
