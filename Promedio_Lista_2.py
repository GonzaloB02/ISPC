def validating_int_number(msg):
    while True:
        value = input(msg).strip()
        if value.isnumeric and int(value) > 0:
            return int(value)
        print("Error: Numero no valido, asegurese de escribir un numero mayor a 0 (cero)")
        
def validating_float_number(msg):
    while True:
        value = input(msg).replace(",", ".")
        if value.count(".") <= 1 and value.replace("-", "").replace(".", "").isdigit():
            return float(value)
        print("Error: Numero no valido, asegurese de escribir un numero sin simbolos o letras")
    
def filling_list(msg):
    list_1 = []
    num = validating_int_number(msg)
    for i in range(num):
        list_1.append(validating_float_number("Escriba el numero que desea agregar a la lista: "))
    return list_1

def main():

    list_1 = filling_list("Escriba la cantidad de de numeros que desea ingresar: ")
    print((lambda list_1 : sum(list_1) / len(list_1))(list_1))

if __name__ == "__main__":
    main()