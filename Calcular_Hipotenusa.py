def normalize_number(msg_1, msg_2):
    leg_1 = input(msg_1).strip().replace(",", ".")
    leg_2 = input(msg_2).strip().replace(",", ".")
    return leg_1, leg_2

def is_valid_number(leg_1, leg_2):
        if leg_1.count(".") <= 1 and leg_1.replace(".", "").isdigit() and float(leg_1) > 1:
            if leg_2.count(".") <= 1 and leg_2.replace(".", "").isdigit() and float(leg_2) > 1:
                leg_1, leg_2 = string_to_number(leg_1, leg_2)
                if leg_1 >= 0 and leg_2 >= 0:
                    return leg_1, leg_2
                return False

def string_to_number(leg_1, leg_2):
    return float(leg_1), float(leg_2)

def calculate_hypotenuse(leg_1, leg_2):
    return (leg_1 ** 2 + leg_2 ** 2) ** 0.5

def question(msg):
    while True:
        answer = input(msg).strip().lower()
        if answer == 'si':
            return True
        elif answer =='no':
            return False
        else:
            print("Error: La respuesta no coincide con 'SI' o 'NO'")

def main():
    while True:
        raw_input = normalize_number("Ingrese el valor del 1er cateto: ", "\nIngrese el valor del 2do cateto: ")

        if is_valid_number(raw_input[0], raw_input[1]):
            hypotenuse = calculate_hypotenuse(raw_input[0], raw_input[1])
            print(f"La hipotenusa del triangulo es: {hypotenuse:.2f}")
        else:
            print("Error: Los catetos no deben ser negativos y mayores a cero (0)")
        if question("Desea calcular otra hipotenusa? (SI/NO): "):
            continue
        else:
            break

if __name__ == "__main__":
    main()