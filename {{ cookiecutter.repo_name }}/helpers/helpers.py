import ast

# Define a function to extract class names from a Python file
def extract_class_names(filename):
    class_names = []
    with open(filename, 'r') as file:
        tree = ast.parse(file.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_names.append(node.name)
    return class_names

def urlgenerator_postgres(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_DB):
    return f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"


if __name__ == "__main__":
    # Specify the path to your Python file
    filename = 'models.py'  # Replace with the path to your Python file

    # Call the function to extract class names
    class_names = extract_class_names(filename)

    # Print the list of class names
    print("Classes defined in", filename)
    for class_name in class_names:
        print(class_name)


