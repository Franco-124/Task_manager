from task_managment.decorators import log_function_call

@log_function_call
def agregar_tarea(tareas, descripcion):
    tarea = {"descripcion": descripcion, "completada": False}
    tareas.append(tarea)

@log_function_call
def completar_tarea(tareas, index):
    tareas[index]["completada"] = True

@log_function_call
def listar_tareas(tareas):
    return [f"{i}. {'✔️' if t['completada'] else '❌'} {t['descripcion']}" for i, t in enumerate(tareas)]
