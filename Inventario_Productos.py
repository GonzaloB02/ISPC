def validating_price(msg):
    while True:
        value = input(msg).replace(",", ".").replace("$", "")
        if value.isdigit() and int(value) >= 0:
            return int(value)
        print("Error: El valor ingresado no es valido")

def validating_quantity(msg):
    while True:
        value = input(msg).strip()
        if value.isdigit() and int(value) >= 0:
            return int(value)
        print("Error: El valor ingresado no es valido")

def code(msg, inventory):
    while True:
        value = input(msg).strip()
        if value == '1':
            add_new_product(inventory)
        elif value == '2':
            show_inventory(inventory)
        elif value == '3':
            search_product(inventory)
        elif value == '4':
            delete_product(inventory)
        elif value == '0':
            return
        else:
            print("Error: Codigo no valido, asegurese de que el codigo este en el rango y sin simbolos")

def add_new_product(inventory):
    while True:
        product = input("Ingrese el nombre del producto que desea agregar: ").lower()
        quantity = validating_quantity("Ingrese la cantidad que desea agregar: ")
        price = validating_price("Ingrese el precio del producto: ")
        if not product in inventory.values():
            while True:
                choice = input(f"Esta seguro que desea agregar el producto {product}? (Y/N)").lower()
                if choice == 'y':    
                    inventory["Producto"].append(product)
                    inventory["Cantidad"].append(quantity)
                    inventory["Precio"].append(price)
                    return
                elif choice == 'n':
                    continue
                print("Error: Codigo no reconocido")
        else:
            print("Error: El nombre del producto ya se ha agregado con anterioridad")

def show_inventory(inventory):
    print("-" * 40)
    keys = list(inventory.keys())
    header = "".join(f"{key:<15}" for key in keys)
    print(header)
    print("-" * 40)
    num_items = len(next(iter(inventory.values())))
    for i in range(num_items):
        row = "".join(f"{str(inventory[key][i]):<15}" for key in keys)
        print(row)
    print("-" * 40)

def search_product(inventory):
    while True:
        product = input("Ingrese el nombre del producto que desea buscar: ").lower()
        if product in inventory["Producto"]:
            print("-" * 40)
            keys = list(inventory.keys())
            header = "".join(f"{key:<15}" for key in keys)
            print(header)
            print("-" * 40)
            for i in range(len(inventory.values())):
                if product == inventory["Producto"][i]:
                    row = "".join(f"{str(inventory[key][i]):<15}" for key in keys)
                    print(row)
                    print("-" * 40)
                    return
        else:
            print("Error: Producto no encontrado: ")
        while True:
            choice = input("¿Desea volver al menu? (Y/N): ").lower()
            if choice == 'y':
                return
            elif choice == 'n':
                break
            else:
                print("Error: Codigo no reconocido")

def delete_product(inventory):
    while True:
        product = input("Ingrese el nombre del producto que desea eliminar: ").lower()
        if product in inventory["Producto"]:
            choice = input(f"Esta seguro de que desea eliminar el producto {product}? (Y/N): ").lower()
            if choice == 'y':
                index = inventory["Producto"].index(product) 
                inventory["Producto"].pop(index)
                inventory["Cantidad"].pop(index)
                inventory["Precio"].pop(index)
                print(f"El producto {product} fue eliminado exitosamente")
            elif choice == 'n':
                break
            else:
                print("Error: Codigo no reconocido")
        
def main():

    inventory = {"Producto" : [], "Cantidad" : [], "Precio" : []}

    code('''
    Ingrese uno de los siguientes codigos:
    1. Agregar producto 
    2. Mostrar inventario 
    3. Buscar producto 
    4. Eliminar producto 
    0. Salir
            ''', inventory) 

if __name__ == "__main__":
    main()