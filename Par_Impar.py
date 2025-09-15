def validating_number(msg):
    while True:
        value = input(msg)
        if value.isdigit() and int(value) != 0:
            return int(value)
        print(f"Error: Numero invalido")

def calculate(number):
    return "El numero es par" if number % 2 == 0 else "El numero es impar"

def main():
    number = validating_number("Escriba un numero para verificar si es par o impar: ")
    print(calculate(number))

if __name__ == "__main__":
    main()