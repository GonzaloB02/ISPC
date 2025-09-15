from Validating import validating_price, validating_discount

def main():

    price = validating_price("Ingrese el precio del producto: ")

    discount = validating_discount("Ingrese el porcentaje del descuento a hacer: ")

    final_price = (lambda x, y : x - (x * y / 100)) (price, discount)

    print(f"El total a pagar es de: ${final_price}")

if __name__ == "__main__":
    main()