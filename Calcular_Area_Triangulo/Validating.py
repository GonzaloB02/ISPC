def validating_numbers(value):
    base, height = value

    if is_valid_number(base) and is_valid_number(height):
        base, height = string_to_number(base, height)
        if base > 0 and height > 0:
            return (lambda x, y : 0.5 * x * y)(base, height)
        else:
            print("Error: La base o altura debe ser un numero mayor a cero")
    else:
        print("Error: La base o la altura son invalidas, ingrese numeros mayores a cero sin letras ni simbolos")
    return False

def is_valid_number(value):
    return value.count(".") <= 1 and value.replace(".", "").isdigit() and float(value) >= 1

def string_to_number(base, height):
    return float(base), float(height)