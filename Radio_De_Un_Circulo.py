def calculate_area(radius):
    PI = 3.1416
    return PI * (radius ** 2)

def validating_number(msg):
    while True:
        value = input(msg)
        if value.replace('.','',1).isdigit():
            if value > 0:
                return float(value)
        print("Error: Numero invalido")

def main():
    radius = validating_number("Ingrese el radio del circulo para calcular su area: ")
    area = calculate_area(radius)
    print(f"El area del circulo es: {area:.2f}")

if __name__ == "__main__":
    main()