from Validating import validating_number
from Factorial import factorial

def main():

    num = validating_number("Escriba un numero para devolver su factorial: ")
    result = (factorial(num))
    print((lambda number: number)(result))
if __name__ == "__main__":
    main()
    