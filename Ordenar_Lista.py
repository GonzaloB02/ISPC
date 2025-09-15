def validating_number(msg, list_1):
    count = 0
    while count < 10:
        value = input(msg)
        if value.lstrip("-").replace(".", "", 1).isdigit():
            count += 1
            list_1.append(float(value))
        else:
            print("Error: Numero invalido")
    number_insert(list_1)

def number_insert(list_1):
    while True:
        choice = input("Lista completa, desea ordenar los numeros de manera descendente(D) o ascendente(A)?: ").lower()
        if choice == "a":
            return print(f"Lista original: {list_1}\nLista ordenada{sorted(list_1)}")
        elif choice == "d":
            return print(f"Lista original{list_1}\nLista ordenada{sorted(list_1, reverse = True)}")  
        else:
            print("Error: Numero invalido")

def main():

    list_1 = []
    validating_number("Inserte 10 numeros aleatorios para ordenarlos de manera ascendente o descendente: ", list_1)

if __name__ == "__main__":
    main()