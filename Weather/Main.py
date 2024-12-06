from task_managment.weather import obtener_clima
from weather_managment.tasks import agregar_tarea, completar_tarea, listar_tareas
from task_managment.log import setup_logging

def main():
    setup_logging()
    tareas = []
    
    print("Bienvenido al Gestor de Clima y Tareas!")
    
    while True:
        print("\nOpciones:")
        print("1. Consultar clima")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Listar tareas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            latitud = input("Ingresa la latitud: ")
            longitud = input("Ingresa la longitud: ")
            try:
                clima = obtener_clima(latitud, longitud)
                print(f"Temperatura: {clima['temperatura']}°C")
                print(f"Viento: {clima['viento']} km/h")
                print(f"Código de clima: {clima['descripcion']}")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "2":
            descripcion = input("Descripción de la tarea: ")
            agregar_tarea(tareas, descripcion)
        elif opcion == "3":
            listar = listar_tareas(tareas)
            for tarea in listar:
                print(tarea)
            index = int(input("Índice de la tarea a completar: "))
            completar_tarea(tareas, index)
        elif opcion == "4":
            listar = listar_tareas(tareas)
            for tarea in listar:
                print(tarea)
        elif opcion == "5":
            print("Adiós!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
