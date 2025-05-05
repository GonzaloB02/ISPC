from Constants import PENDING, COMPLETED

def add_task(tasks, name_task):
    name_task = name_task.lower().strip()
    if not name_task:
        return False
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
                return "ya_completada"
    return "no_encontrada"

def get_pending_tasks(tasks):
    return [task for task in tasks if task["Estado"] == PENDING]

def get_completed_tasks(tasks):
    return [task for task in tasks if task["Estado"] == COMPLETED]
