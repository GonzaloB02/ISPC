from Normalize import normalize_number
from Validating import validating_numbers


def main():
    while True:

        raw_input = normalize_number("Ingrese el valor de la base: ","\nIngrese el valor de la altura: ")

        valid_input = validating_numbers(raw_input)

        if valid_input:
            break

    area = valid_input

    print(f"{area:.2f}")

if __name__ == "__main__":
    main()