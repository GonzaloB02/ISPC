from Validating import validating_number

def search_number(random_number):
    attempts = 0
    while True:
        attempts += 1
        number = validating_number("Adivine el numero entre 1-100: ")
        if number < random_number:
            print("El numero elegido es menor al numero a adivinar")
        elif number > random_number:
            print("El numero elegido es mayor al numero a adivinar")
        else:
            print(f"Felicidades, adivinaste el numero en {attempts} intentos")
            return
