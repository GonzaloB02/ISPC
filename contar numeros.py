
Tupla = (1, 3, 5, 2, 6, 1, 7, 9, 1, 5, 2, 2)
Repetido = 0

while True:
    try: 
        Numero = int(input("Ingrese un numero: "))

        for i in Tupla:
            if Numero == i:
                Repetido += 1
        print(f"El numero {Numero} se repitio {Repetido} veces en la tupla")
        Repetido = 0 
    except ValueError:
        print("Valor erroneo")