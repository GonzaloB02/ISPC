def validating_password(msg):
    while True:
        value = input(msg)
        if all(not char.isspace() and char.isalnum() for char in value):
            return value
        print("Error: ")

def verifing_password():
    while True:
        password = validating_password("Escriba la contraseña: ")
        confirm_password = validating_password("Confirme la contraseña: ")
        if password == confirm_password:
            return print("Contraseña confirmada")
        print("Error: Las contraseñas no coinciden")

def main():
    verifing_password()

if __name__ == "__main__":
    main()