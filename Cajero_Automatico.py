def validating_number(msg):
    value = input(msg).strip()
    if value.lstrip("-").isdigit() and int(value) > 0:
        return True
    return False

def register(users, name_user, password):
    name_user = name_user.strip().lower()
    if not name_user:
        return
    if not any(u["Nombre"] == name_user for u in users):
        users.append({"Nombre" : name_user, "Contraseña" : password, "Dinero" : 0})
        return True
    else:
        return False

def log_in(users, name_user, password):
    name_user = name_user.strip().lower()
    if not name_user:
        return
    for u in users:
       if u["Nombre"] == name_user:
            if u["Contraseña"] == password:
                return "correct_session"
            else:
                return "wrong_password"
    return "non_existent_user"

def extraction(users, user_logged, money_to_extract):
    if not money_to_extract:
        return 
    user = next((u for u in users if u["Nombre"] == user_logged), None)
    if user:
        if money_to_extract <= user["Dinero"]:
            user["Dinero"] -= money_to_extract
            return True
        return False
    
def deposit(users, user_logged, money_to_deposit):
    if not money_to_deposit:
        return
    user = next((u for u in users if u["Nombre"] == user_logged), None)
    if user:
        users[user_logged("Dinero")] += money_to_deposit
        return

def get_user_money(users, user_logged):
    user = next((u for u in users if u["Nombre"] == user_logged), None)
    if user:
        return user["Dinero"]

def menu(msg, users):
    state_1 = None
    user_logged = None
    while True: 
        value = input(msg).strip().lower()
        
        if value == '1':
            name_user = input("Escriba su nombre de usuario: ")
            password = input("Escriba su contraseña: ")
            state = register(users, name_user, password)
            if state == True:
                print("Usuario registrado exitosamente")
            else:
                print("Usuario no registrado, elija otro nombre")

        elif value == '2':
            name_user = input("Escriba su numero de usuario: ")
            password = input("Escriba su contraseña: ")
            state_1 = log_in(users, name_user, password)
            
            if state_1 == "correct_session":
                user_logged = name_user
                print("Sesion iniciada.")
            elif state_1 == "wrong_password":
                print("Contraseña incorrecta.")
            elif state_1 == "non_existent_user":
                print("Usuario no existente.")
                

        elif value == '3':
            if state_1 == "correct_session":
                user_money = get_user_money(users, user_logged)
                print(f"Monto en caja: {user_money}")
                money_to_extract = float(input("Ingrese el monto que desea extraer: "))
                if validating_number(money_to_extract):
                    state_2 = extraction(users, user_logged, money_to_extract)
                else:
                    print("Error: Numero no valido")
                if state_2 == True:
                    print(f"Extraccion exitosa")
                else:
                    print("Extraccion fallida, asegurese de ingresar un monto valido")
            else:
                print("Error: Debe iniciar sesion")

        elif value == '4':
            if state_1 == "correct_session":
                money_to_deposit = float(input("Ingrese el monto que desea depositar: "))
                deposit(users, user_logged, money_to_deposit)
                if validating_number(money_to_extract):
                    user_money = get_user_money(users, user_logged)
                else:
                    print("Error: Numero no valido")
            else:
                print("Error: Debe iniciar sesion")

        elif value == '0':
            return
        
        else:
            print("Error: El codigo ingresado se encuentra fuera del rango, asegurese de poner un codigo valido")

def main():

    users = []

    menu('''
        1. Registrarse
        2. Iniciar sesion
        3. Realizar extracciones
        4. Realizar depositos
        0. Salir
        ''', users)

if __name__ == "__main__":
    main()