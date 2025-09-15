def validating_int(msg):
    while True:
        value = input(msg)
        if value.replace("-", "").isdigit():
            return int(value)
        print("Error: Numero no valido")

def validating_binary(msg):
    while True:
        value = input(msg)
        if all(char.isnumeric() and int(char) <= 1 for char in value):
            return value
        print("Error: Numero no valido, deben ser secuencias de numeros entre 0-1")

def int_to_binary(num, binary):
    num = int(num)
    negative = num < 0
    if negative:
        num *= -1
    if num == 0:
        binary.append(0)
    while num > 0:
        binary.append(num % 2)
        num = num // 2
    binary.reverse()

    if negative:
        binary.insert(0, "-")

def binary_to_int(num):
    result = 0
    power = len(num) - 1
    for char in num:
        result += (int(char) * (2 ** power))
        power -= 1
    return result

def convert_list_to_string(list):
    return "".join(map(str, list))

def menu():
    while True:
        value = str(input('''
        1. Convertir entero a binario
        2. Convertir binario a entero
        0. Salir
        '''))

        if value == '1':
            num = validating_int("Escribe un numero para convertirlo de entero a binario: ")
            binary = []
            int_to_binary(num, binary)
            result = convert_list_to_string(binary)
            print(result)
        elif value == '2':
            num = validating_binary("Escribe un numero para convertirlo de binario a entero: ")
            print(binary_to_int(num))
        elif value == '0':
            return
        else:
            print("Error: Codigo no valido, asegurese de elegir un numero del siguiente menu")

def main():

    menu()

if __name__ == "__main__":
    main()