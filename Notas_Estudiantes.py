def validating_string(msg):
    while True:
        value = input(msg).strip()
        if value.replace(" ", "").isalpha():
            return "".join(value.split()).lower()
        print("Error: Nombre no valido")

def validating_number(msg):
    while True:
        num = input(msg).replace(",", ".")
        if num.lstrip("-").isdigit() and float(num) >= 0:
            return float(num)
        print("Error: Numero no valido")

def add_students(dict_1):
    classifications = []
    name = validating_string("Ingrese el nombre del estudiante: ")
    quantity_classifications = validating_number("Ingrese la cantidad de notas que desea ingresar: ")
    for i in range(int(quantity_classifications)):
        numbers = validating_number(f"Ingrese la nota N° {i + 1}: ")
        classifications.append(numbers)

    average = sum(classifications) / len(classifications)
    dict_1[name] = [classifications, average]
    print(dict_1)

def update_student(dict_1):
    classifications = []
    name = validating_string("Ingrese el nombre del estudiante que desea actualizar: ")
    if name in dict_1:
        quantity_classifications = validating_number("Ingrese la cantidad de notas que desea ingresar: ")
        if quantity_classifications > 0:
            for i in range(0, int(quantity_classifications), +1):
                numbers = validating_number(f"Ingrese la nota N° {i + 1}: ")
                classifications.append(numbers)
        else: 
            print("Error: La cantidad debe ser mayor a cero, cancelando operacion")
            return
        dict_1[name][0].extend(classifications)
        dict_1[name][1] = sum(dict_1[name][0]) / len(dict_1[name][0])
        print(f"{name}: {dict_1[name]}")
    else:
        print("Error: Estudiante no encontrado")

def show_average_student(dict_1):
    average = []
    name = validating_string("Ingrese el nombre del estudiante: ").lower()
    if name in dict_1:
        average = [str(string) for string in dict_1[name]]
        print(f"El promedio del estudiante {name} es: {dict_1[name][1]:.2f}")
    else:
        print("Error: Estudiante no encontrado")

def main():
    dict_1 = {"gonzalo" : [[7, 8, 8.5, 7.66], 7.79], "marcos" : [[6.66, 9, 7, 8], 7.66]}
    while True:
        
        code = input('''
        1. Agregar estudiante y clasificaciones
        2. Actualizar clasificaciones de estudiante
        3. Mostrar promedio de clasificaciones de estudiante
        0. Salir
        ''')

        if code == "1":
            add_students(dict_1)
        elif code == "2":
            update_student(dict_1)
        elif code == "3":
            show_average_student(dict_1)
        elif code == "0":
            return
        else:
            print("Error: Codigo no valido")

if __name__ == "__main__":
    main()