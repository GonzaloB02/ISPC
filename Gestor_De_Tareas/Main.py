from Tasks import (add_task, mark_complete_tasks, get_completed_tasks, get_pending_tasks)

from Constants import PENDING, COMPLETED

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
            print("-" * 40)
            print(f"{'Tareas':<30} Estado")
            print("-" * 40)
            for task in tasks_pending:
                print(f"{task['Tarea']:<30} Pendiente")
            print("-" * 40)

        elif value == '4':
            tasks_completed = get_completed_tasks(tasks)
            print("-" * 40)
            print(f"{'Tareas':<30} Estado")
            print("-" * 40)
            for task in tasks_completed:
                if task["Estado"] == COMPLETED:
                    print(f"{task['Tarea']:<30} Completada")
            print("-" * 40)

        elif value == '0':
            return
        
        else:
            print("Error: El codigo ingresado esta fuera del rango, asegurese de ingresar un codigo valido")

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