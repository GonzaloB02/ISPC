def validating_number(msg, list_1):
    while True:
        count = input(msg)
        if count.isnumeric() and int(count) > 0:
            count = int(count)
            while count > 0:
                number = input("Ingrese el numero que desea agregar a la lista: ")
                if number.lstrip("-").replace(".", "", 1).isdigit():
                    list_1.append(float(number))
                    count -= 1
                else:
                    print("Error: Numero invalido")
            return
        else:
            print("Error: Numero invalido")


def count_number_list(msg, list_1):
    while True:
        value = input(msg)
        if value.lstrip("-").replace(".", "", 1).isdigit():
            return print(f"La cantidad de veces que se repite el numero {value} en la lista es de {list_1.count(float(value))} veces")
            
def main():
    list_1 = []
    validating_number("Indique la cantidad de numeros que desea agregar a la lista: ", list_1)
    count_number_list("Indique que numero repetitivo desea contar: ", list_1)

if __name__ == "__main__":
    main()