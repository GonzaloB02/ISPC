from Validating import validating_number, validating_number_list

def filling_list(list_1):
    length_list = validating_number("Ingrese la cantidad de numeros que desea añadir a la lista: ")
    for i in range (length_list):
        number = validating_number_list("Ingrese el valor que desea almacenar: ")
        list_1.append(number) 
    return list_1

def filtering_list(list_1):
    return list(filter(lambda num : num % 2 == 0, list_1))
