def normalize_input(value):
    return value.strip().replace(",", ".")

def is_valid_number(value):
    value = normalize_input(value)
    return value.count(".") <= 1 and value.replace("-", "").replace(".", "").isdigit()

def string_to_float(value):
    return float(normalize_input(value))

def celsius_to_fahrenheit(celsius_float):
    return (celsius_float * 1.8) + 32

def main():

    while True:
        raw_input_value = input("Ingrese el valor celsius a convertir a fahrenheit (o escriba 'salir'): ")
        
        if raw_input_value.lower() == "salir":
            break

        if is_valid_number(raw_input_value):
            celsius = string_to_float(raw_input_value)
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Celsius: {celsius:.2f} -> fahrenheit: {fahrenheit:.2f}")
        else:
            print(f"Error: Numero no valido")

if __name__ == "__main__":
    main()