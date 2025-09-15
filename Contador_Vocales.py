def counter_vocals(msg):
    count = 0
    value = input(msg).lower()
    for char in value:
        if char in "aeiou":
            count += 1
    return count
        

def main():
    string = counter_vocals("Escribe una cadena de caracteres para contar la cantidad de vocales: ")
    print(string)

if __name__ == "__main__":
    main()