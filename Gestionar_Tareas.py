def add_task(tasks, name_task):
    name_task = name_task.lower().strip()
    if not any(u["Tarea"] == name_task and u["Estado"] == PENDING for u in tasks):
        tasks.append({"Estado" : PENDING, "Tarea" : name_task})
        return True
    return False

def mark_complete_tasks(tasks, name_task):
    name_task = name_task.lower().strip()
    if not name_task:
        return "vacio"
    for task in tasks:
        if task["Tarea"] == name_task:
            if task["Estado"] == PENDING:
                task["Estado"] = COMPLETED
                return "completada"
            else:
                return "ya completada"
    return "no_encontrada"

def get_pending_tasks(tasks):
    return [task for task in tasks if task["Estado"] == PENDING]

def get_completed_tasks(tasks):
    return [task for task in tasks if task["Estado"] == COMPLETED]

def show_tasks(tasks, text_state):
    if not tasks:
        print("No hay tareas")
        return 
    
    print("-" * 40)
    print(f"{'Tareas':<30} Estado")
    print("-" * 40)
    for task in tasks:
        print(f"{task['Tarea']:<30} {text_state}")
    print("-" * 40)

def menu(msg, tasks):
    while True:
        value = input(msg).strip()

        if value == '1':
            name = input("Ingrese la tarea que desea guardar: ")

            if add_task(tasks, name):
                print("Tarea guardada con éxito.")
            else:
                print("Error: Una tarea con el mismo nombre y en estado pendiente ya existe.")

        elif value == '2':
            name = input("Ingresa el nombre de la tarea que desee marcar como completada: ")
            estado = mark_complete_tasks(tasks, name)

            if estado == "completada":
                print("La tarea fue marcada como completada.")
            elif estado == "ya_completada":
                print("La tarea ya estaba completada.")
            elif estado == "no_encontrada":
                print("La tarea no fue encontrada.")
            elif estado == "vacio":
                print("Error: La tarea no puede estar vacia.")

        elif value == '3':
            tasks_pending = get_pending_tasks(tasks)
            show_tasks(tasks_pending, "PENDING")

        elif value == '4':
            tasks_completed = get_completed_tasks(tasks)
            show_tasks(tasks_completed, "COMPLETED")

        elif value == '0':
            return
        
        else:
            print("Error: El codigo ingresado esta fuera del rango, asegurese de ingresar un codigo valido")

PENDING = 0
COMPLETED = 1

def main():

    tasks = [] 

    menu('''
        1. Agregar tareas.
        2. Marcar tareas completadas.
        3. Mostrar tareas pendientes.
        4. Mostrar tareas completadas.
        0. Salir
        ''', tasks)

if __name__ == "__main__":
    main()