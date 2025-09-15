def validating_string(msg, default_name = "Invitado"):
    while True:
        if not name:
            name = default_name
            return name
        name = input(msg).strip()
        if all(char.isalpha() or char.isspace()  for char in name):
            return name
        print("Error: El nombre no debe contener numeros y/o simbolos")