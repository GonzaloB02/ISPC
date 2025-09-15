def validating_string(string):
    while True:
        name = input(string).strip()
        if name.replace(" ", "").isalpha():
            return "".join(name.split())
        print("Error: El nombre no es valido, asegurese de no utilizar numeros ni simbolos")

def personalized_greeting(msg):
    name = validating_string(msg)
    print(f"Hola {name} bienvenido, este es mi programa")

def main():

    personalized_greeting("Escriba su nombre: ")

if __name__ == "__main__":
    main()