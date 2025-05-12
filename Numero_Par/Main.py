from Validating import validating_number

def main():

    num = validating_number("Ingrese el numero que desea calcular: ")
    print((lambda num : "Par" if num % 2 == 0 else "Impar")(num))

if __name__ == "__main__":
    main()