def validating_price(msg):
    while True:
        value = input(msg).strip().replace(",", ".").lstrip("$")
        if value.replace(".", "").isdigit() and value.count(".") <= 1 and float(value) > 0:
            return float(value)
        print("Error: El precio que ha ingresado no es valido, recuerde que debe ser mayor a cero y sin simbolos o letras")

def validating_discount(msg, default_discount = 10):
    while True:
        value = input(msg).strip().replace(",", ".").lstrip("%")
        if not value:
            value = default_discount
            return value
        if value.replace(".", "").isdigit() and value.count(".") <= 1 and 100 >= float(value) > 0:
            return float(value)
        print("Error: El descuento que ha ingresado no es valido, recuerde que debe de estar dentro del rango de cien (100) y debe solo contener numeros")
