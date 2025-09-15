import time

def validating_string(msg):
    while True:
        value = input(msg)
        if all(char.isalpha() or char.isspace() for char in value):
            return value
        print("Error: El nombre no debe contener simbolos y/o numeros")           
    
def validating_year(birth_year):
    while True:
        value = input(birth_year)
        if value.replace('.','',1).isdigit() and int(value) != 0:
            if len(value) == 4 and 1900 <= int(value) <= time.localtime().tm_year:
                return int(value)
            elif len(value) == 2 and 0 <= int(value) <= 99:
                return 2000 + int(value)
        print("Error: Numero invalido, debe contener 2 o 4 digitos")     

def validating_month(birth_month):
    while True:
        value = input(birth_month)
        if value.replace('.','',1).isdigit() and int(value) != 0:
            if 1 <= int(value) <= 12:
                return int(value)
        print("Error: Mes no valido, debe ser entre 1-12")

def validating_day(birth_day, birth_month, birth_year):
    while True:
        day = input(birth_day)
        if day.replace('.','',1).isdigit() and int(day) != 0:
            if birth_month in [1, 3, 5, 7, 8, 10, 12]:
                if 1 <= int(day) <= 31:
                    return day
            elif birth_month in [4, 6, 9, 11]:
                if 1 <= int(day) <= 30:
                    return day
            elif int(birth_month) == 2:
                if (int(birth_year) % 4 == 0 and (int(birth_year) % 100 != 0 or int(birth_year) % 400 == 0)):
                    if 1 <= int(day) <= 29:
                        return day
                elif 1 <= int(day) <= 28:
                    return int(day)
        print("Error: Dia no valido, verifique la cantidad de dias del mes en el calendario")

def calculating_age(birth_year, birth_month, birth_day):
    current_year = int(time.localtime().tm_year)
    current_month = int(time.localtime().tm_mon)
    current_day = int(time.localtime().tm_mday)

    age = current_year - birth_year
    if (current_month < birth_month) or (current_month == birth_month and current_day < birth_day):
        age -= 1
    return age

def main():
    name = validating_string("Ingrese su nombre: ")
    birth_year = validating_year("Ingrese su año de nacimiento: ")
    birth_month = validating_month("Ingrese su mes de nacimiento: ")
    birth_day = validating_day("Ingrese su dia de nacimiento: ", birth_month, birth_year)

    age = calculating_age(birth_year, birth_month, birth_day)
    print(f"{name} tiene {age} años de edad")

if __name__ == "__main__":
    main()