def validating_number(msg):
    while True:
        num = input(msg)
        if num.isdigit() and int(num) >= 0:
            return int(num)
        print("Error: Numero no valido, asegurese de escribir un numero natural entero sin letras y/o simbolos")


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def main():

    num = validating_number("Escriba un numero para devolver su factorial: ")
    print(factorial(num))
if __name__ == "__main__":
    main()