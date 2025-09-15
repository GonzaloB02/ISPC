def validating_name(msg):
    while True:
        value = input(msg).strip()
        if all(char.isalpha() and char.isspace() for char in value):
            return value
        print("Error: Nombre invalido")

def validating_age(msg):
    while True:
        value = input(msg)
        if value.isdigit() and not value.isspace() and 0 < int(value) <= 120:
            return int(value)
        print("Error: Edad fuera de rango")

def validating_number(msg):
    while True:
        value = input(msg)
        if value.isdigit() and not value.isspace() and 1 <= len(value) <= 15:
            return int(value)
        print("Error: Numero telefonico fuera de rango")

def main():
    name = validating_name("Escriba su nombre: ")
    age = validating_age("Escriba su edad: ")
    number_cellphone = validating_number("Escriba su numero telefonico: ")
    print(name, age, number_cellphone)

if __name__ == "__main__":
    main()