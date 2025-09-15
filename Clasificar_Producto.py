def validating_product(msg):
    while True:
        value = input(msg)
        if value.isdigit() and (int(value) > 0 and int(value) != None):
            return int(value)
        print("Error: La cantidad del producto debe ser mayor a cero")

def validating_price(msg):
    while True:
        value = input(msg)
        if value.isdigit() and (float(value) > 0 and float(value) != None):
            return float(value)
        print("Error: El precio del producto debe ser mayor a cero")

def classify():
        product = validating_product("Escriba la cantidad del producto: ")
        price = validating_price("Escriba el precio del producto:$ ")
        if price > 100 or (price > 50 and product < 10):
            return "Caro"
        else:
            return "Barato"

def main():
    print(classify())

if __name__ == "__main__":
    main()