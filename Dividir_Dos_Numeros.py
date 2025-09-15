def verificating_number(msg):
    while True:
        value = input(msg)
        if value.replace(',', '', 1).lstrip('-').isdigit():
            value = float(value)
            if value != 0:
                return value
        print("Error: Numero invalido, el numero debe ser distinto a cero")

def calculate_division(dividend, divider):
    print(dividend / divider)

def main():
    dividend = verificating_number("Ingrese el dividendo: ")
    divider = verificating_number("Ingrese el divisor: ")
    calculate_division(dividend, divider)

if __name__ == "__main__":
    main()