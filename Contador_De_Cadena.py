def string_counter(msg):
    value = input(msg)
    return print(len(value))

def main():
    string = string_counter("Escribe una palabra para contar la cantidad de caracteres: ")

if __name__ == "__main__":
    main()