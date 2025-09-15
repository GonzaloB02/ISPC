def validating_number(msg):
    while True:
        value = input(msg)
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("Error: Numero invalido, asegurese de escribir un numero mayor a cero")

def calculate_triangle(side_1, side_2, side_3):
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        if side_1 == side_2 and side_2 == side_3:
            return("El triangulo es equilatero")
        elif side_1 != side_2 and side_1 != side_3 and side_2 != side_3:
            return("El triangulo es escaleno")
        return ("El triangulo es isosceles")
    else:
        return print("Error: Las medidas de los lados no forman un triangulo")   

def main():
    side_1 = validating_number("Escriba el 1er lado del triangulo: ")
    side_2 = validating_number("Escriba el 2do lado del triangulo: ")
    side_3 = validating_number("Escriba el 3er lado del triangulo: ")

    print(calculate_triangle(side_1, side_2, side_3))

if __name__ == "__main__":
    main()