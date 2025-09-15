def program_start(friends):
    while True:
        code_number = input('''
        1. Buscar indice de un amigo
        2. Mostrar lista de amigos
        3. Agregar un amigo nuevo
        4. Eliminar al ultimo amigo agregado
        5. Mostrar lista ordenada alfabeticamente
        0. Salir\n''')
        if code_number == '1':
            search_friend(friends)
        elif code_number == '2':
            show_friends(friends)
        elif code_number == '3':
            add_friend(friends)
        elif code_number == '4':
            delete_last_friend(friends)
        elif code_number == '5':
            show_alphabetically_ordered(friends)
        elif code_number == '0':
            return
        else:
            print("Error: Codigo invalido")

def search_friend(friends):
    string = input("Escriba el nombre del amigo a buscar: ").lower()
    if string in friends:
        print(f"El amigo que deseaba buscar se encuentra en el indice N°{friends.index(string) + 1}")
    else:
        print("El amigo no se encuentra en la lista")
        return
    
def show_friends(friends):
    if friends:
        print(friends)
    else:
        print("Error: Lista vacia")

def add_friend(friends):
    while True:
        string = input("Escriba el nombre del amigo que desea agregar (si desea regresar digite 0 (cero)): ").lower()
        if string.isalpha():
            friends.append(string)
            print(friends)
        elif string == '0':
            return
        else:
            print("Error: Caracteres no validos")

def delete_last_friend(friends):
    while True:
        string = input("Esta seguro que desea eliminar al ultimo amigo agregado? (Y/N)").lower()
        if friends:
            if string.isalpha() and string == 'y':
                friends.pop()
            elif string.isalpha and string == 'n':
                return
            else:
                print("Error: Caracter no valido")
        else:
            print("Error: Lista vacia")

def show_alphabetically_ordered(friends):
    print(sorted(friends))

def main():
    friends = ["ana", "monica", "jose", "camila", "raquel", "matias"]
    program_start(friends)

if __name__ == "__main__":
    main()