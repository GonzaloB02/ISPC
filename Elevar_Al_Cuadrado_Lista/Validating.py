def validating_number(msg):
    while True:
        num = input(msg).strip()
        if num.isdigit() and int(num) > 0:
            return int(num)
        print("Error: Numero no valido, asegurese de que el valor se un numero entero mayor a cero")
        
def validating_number_list(num):
    while True:
        number = input(num).strip()
        if number.count(".") < 1 and number.lstrip("-").isdigit():
            return int(number)
        print("Error: Numero no valido, asegurese de ingresar un numero sin simbolos ni comas")