def validating_password(msg):
    while True:
        value = input(msg)
        if all(not char.isspace() for char in value) and 15 >= len(value) >= 8:
            return value
        print("Error: Contraseña no valida, asegurese de que no tenga espacios y tenga entre 8 y 15 caracteres")

def add_user(users):
    while True:
        name = input("Escribe un nombre de usuario: ").lower()
        password = validating_password("Escribe una contraseña: ")
        user = {"Usuario" : name, "Contraseña" : password}
        if not any(u["Usuario"] == name for u in users):
            users.append(user)
            return
        else:
            print("Error: El usuario ya se encuentra registrado")

def show_users(users):
    print("-" * 30)
    print(f" {'Usuario':<15} {'Contraseña':<15}")
    print("-" * 30)
    for i in range(len(users)):
        print(f"{users[i].get("Usuario"):<10} {users[i].get("Contraseña")}\n")
    print("-" * 30)

def delete_user(users):
    while True:
        name = input("Ingrese el nombre del usuario que desea eliminar: ").lower()
        for i, user in enumerate(users):
            if user["Usuario"] == name:
                password = input("Ingrese la contraseña para confirmar la eliminacion: ")
                if user["Contraseña"] == password:
                    users.pop(i)
                    print("Usuario eliminado")
                    return
                else:
                    code("Contraseña incorrecta, desea volver al menu? (Y/N)")

        code("Error:Usuario no encontrado, desea volver al menu? (Y/N)", users)
            
def code(msg, users):
    while True: 
        value = input(msg).strip().lower()   
        if value == 'y':
            return delete_user(users)
        elif value == 'n':
            return menu(users)
        else:
            print("Codigo no reconocido")

def menu(msg, users):
    while True:
        value = input(msg).strip()
        if value == '1':
            add_user(users)
        elif value == '2':
            show_users(users)
        elif value == '3':
            delete_user(users)
        elif value == '0':
            return
        else:
            print("Error: Codigo no valido")

def main():

    users = []

    menu('''
    Ingrese uno de los siguientes codigos:
    1. Agregar usuario 
    2. Mostrar usuarios 
    3. Eliminar usuario
    0. Salir
            ''', users)



if __name__ == "__main__":
    main()