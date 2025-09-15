def validating_number(msg):
    while True:
        value = input(msg).strip()   
        if value.isdigit() and 15 >= len(value) >= 8:
            return int(value)
        else:
            print("Error: Ingrese un numero telefonico sin guiones ni espacios")

def add_new_contact(contact_list):
    while True:
        name = input("Ingrese el nombre del contacto que desee agregar: ").lower()
        number = validating_number("Ingrese en numero del contacto que desea agregar: ")
        contact = {"Nombre" : name, "Numero" : number}
        if not contact in contact_list:
            contact_list.append(contact)
            return
        else:
            print("Error: El contacto con ese nombre y numero se encuentra agendado")
            return

def show_contact(contact_list):
        print("-" * 30)
        print(f" {'Nombre':<15} {'Numero':<15}")
        print("-" * 30)
        for i in range(len(contact_list)):
            print(f"{contact_list[i].get("Nombre"):<10} {contact_list[i].get("Numero")}\n")
        print("-" * 30)
        return

def delete_contact(contact_list):
    while True:
        name = input("Ingrese el nombre del contacto que desea eliminar: ").lower()
        number = validating_number("Ingrese el numero del contacto que desea eliminar: ")
        contact = {"Nombre" : name, "Numero" : number}
        if contact in contact_list:
            index = contact_list.index(contact)
            contact_list.pop(index)
            print("Contacto eliminado")
            return
        else:
            print("Error: El contacto con este nombre y numero no se encuentra agendado")
            break

def menu(msg, contact_list):
    while True:
        value = input(msg).strip()
        if value == '1':
            add_new_contact(contact_list)
        elif value == '2':
            show_contact(contact_list)
        elif value == '3':
            delete_contact(contact_list)
        elif value == '0':
            return
        else:
            print("Error: Codigo no valido, asegurese de que el codigo este en el rango y sin simbolos")

def main():

    contact_list = []

    menu('''
    Ingrese uno de los siguientes codigos:
    1. Agregar contacto 
    2. Mostrar contacto 
    3. Eliminar contacto 
    0. Salir
            ''', contact_list)

if __name__ == "__main__":
    main()