def menu(msg, inventory):
    while True:
        value = input(msg)
        if value == '1':
            add_new_product(inventory)    
        elif value == '2':
            update_quantity_products(inventory)
        elif value == '3':
            show_inventory(inventory)
        elif value == '0':
            return
        else:
            print("Error: Codigo invalido")

def add_new_product(inventory):
    product = input("Ingrese el nombre del producto: ").lower()
    if product in inventory["Producto"]:
        return print("Error: Producto ya existente")
    quantity = input("Ingrese la cantidad del producto: ")
    if not quantity.isnumeric() and quantity < 0: 
        print("Error: Numero invalido")
        return
    quantity = int(quantity)
    price = input("Ingrese el precio del producto: ")
    if not price.isdigit() and price < 0:
        print("Error: Numero invalido")
        return
    price = int(price)
    inventory["Producto"].append(product)
    inventory["Cantidad"].append(quantity)
    inventory["Precio"].append(price)
     
def update_quantity_products(inventory):
    product = input("Ingrese el nombre del producto cuya cantidad desea modificar: ").lower()
    if product in inventory["Producto"]:
        index = inventory["Producto"].index(product)
        quantity = input("Ingrese la cantidad que desea modificar: ")
        if not quantity.lstrip("-+").isdigit():
            print("Error: Numero invalido")
            return
        inventory["Cantidad"][index] += int(quantity)
        print(f"Nueva cantidad de {product}: {inventory["Cantidad"][index]}")
    else:
        print("Error: Producto no encontrado en el inventario")

def show_inventory(inventory):
    print("-" * 50)
    keys = list(inventory.keys())
    header = "".join(f"{key:<15}" for key in keys)
    print(header)
    print("-" * 50)
    num_items = len(next(iter(inventory.values())))
    for i in range(num_items):
        row = "".join(f"{str(inventory[key][i]):<15}" for key in keys)
        print(row)
    print("-" * 50)
                
def main():

    inventory = {"Producto" : ["harina", "huevos", "manteca"], "Cantidad" : [27, 18, 9], "Precio" : [20, 12, 11]}
    menu('''
    1. Agregar nuevos productos
    2. Actualizar cantidad productos
    3. Mostrar inventario
    0. Salir
    ''', inventory)

if __name__ == "__main__":
    main()