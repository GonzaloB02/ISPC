def validating_number(msg):
    while True:
        value = input(msg)
        if value.isdigit() and int(value) > 0 and int(value) < 101:
            return int(value)
        print("Error: Numero invalido, digite un numero entre 1-100")