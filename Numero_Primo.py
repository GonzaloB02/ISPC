def validating_number(msg):
    while True:
        value = input(msg)
        if value.isdigit() and int(value) > 1:
            return int(value)
        print("Error: Numero invalido, debe escribir un numero mayor a 1")

def prime_number(number):
        if number == 2: 
            return ("Es primo")
        if number % 2 == 0: 
            return ("No es primo")
        for n in range (3, int(number ** 0.5) + 1, 2):
            if number % n == 0:
                return "No es primo"
        return "Es primo"

def main():
    number = validating_number("Escriba un numero para calcular si es primo o no: ")
    print(prime_number(number))

if __name__ == "__main__":
    main()