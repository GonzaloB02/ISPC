#Dado n, tome la suma de los dígitos de n. Si ese valor tiene más de un dígito, continúe reduciéndose de esta manera hasta que se produzca un número de un solo dígito. La entrada será un número entero no negativo.

def validating_number(msg):
    while True:
        value = input(msg)
        if value != '' and all(char.isdigit() and not char.isspace() for char in value):
            return value
        print("Error: Numero no valido, ingrese un numero que sea mayor a 0 (cero)")

def result_sum(number):
    sum = 0
    number = str(number)
    if len(number) > 1:
        for n in range(len(number)):
            sum = sum + int(number[n])
            print(sum)
        return result_sum(sum)
    else:
        print(number)


def main():

    number = validating_number("Ingrese un numero: ")
    result_sum(number)


if __name__ == "__main__":
    main()