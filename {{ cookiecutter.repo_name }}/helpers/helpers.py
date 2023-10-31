import ast


def extract_class_names(filename: str) -> list[str]:
    """Extract classes from a python file

    Args:
        filename (str): _description_

    Returns:
        list[str]: list of class names
    """
    class_names = []
    with open(filename, "r") as file:
        tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_names.append(node.name)
    return class_names


def urlgenerator(type: str, user: str, password: str, server: str, db: str, port: int):
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
    if type.lower() == "postgresql":
        # pip install psycopg2
        if port is None:
            port = 5432
        return f"postgresql://{user}:{password}@{server}:{port}/{db}"
    elif type.lower() == "mysql":
        # pip install mysql-connector-python
        if port is None:
            port = 3306
        return f"mysql://{user}:{password}@{server}:{port}/{db}"
    elif type.lower() == "sqlite":
        if port is None:
            port = 5432
        return f"sqlite:///{db}"
    elif type.lower() == "sqlserver":
        # pip install pyodbc
        if port is None:
            port = 1433
        return (
            f"mssql+pyodbc://{user}:{password}@{server}:{port}/{port}?driver=SQL+Server"
        )


if __name__ == "__main__":
    # Specify the path to your Python file
    filename = "models.py"  # Replace with the path to your Python file

    # Call the function to extract class names
    class_names = extract_class_names(filename)

    # Print the list of class names
    print("Classes defined in", filename)
    for class_name in class_names:
        print(class_name)
