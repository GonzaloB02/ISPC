def validating_number(msg):
    while True:
        num = input(msg)
        if num.isdigit() and int(num) >= 0:
            return int(num)
        print("Error: Numero no valido, asegurese de escribir un numero natural entero sin letras y/o simbolos")
