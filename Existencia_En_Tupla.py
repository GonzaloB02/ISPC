def validating_number(msg, tuple_1):
    while True:
        value = input(msg)
        if value.lstrip("-").replace(".", "", 1).isdigit():
            if (float(value)) in tuple_1:
                return (f"Numero existente en la posicion  {tuple_1.index(float(value)) + 1}")
            return "Numero no existente en la tupla"

def main():

    tuple_1 = (2, 5.8, 12, -7, 49, 90, 0)

    print(validating_number("Escriba el numero que desea verificar la existencia en la tupla: ", tuple_1))

if __name__ == "__main__":
    main()