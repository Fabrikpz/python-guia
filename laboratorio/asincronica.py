def agregar_tarea(tareas, descripcion, fecha_limite, prioridad, completada=False):
    tarea = {"descripcion": descripcion, "fecha_limite": fecha_limite, "prioridad": prioridad, "completada": completada}
    tareas.append(tarea)

def mostrar_tareas(tareas, completadas=None):
    if completadas is None:
        for i, tarea in enumerate(tareas, start=1):
            print(f"Tarea {i}:")
            print("Descripción:", tarea["descripcion"])
            print("Fecha límite:", tarea["fecha_limite"])
            print("Prioridad:", tarea["prioridad"])
            print("Completada:", tarea["completada"])
            print()
    elif completadas:
        completadas_tareas = [tarea for tarea in tareas if tarea["completada"]]
        if completadas_tareas:
            print("Tareas completadas:")
            for i, tarea in enumerate(completadas_tareas, start=1):
                print(f"Tarea {i}:")
                print("Descripción:", tarea["descripcion"])
                print("Fecha límite:", tarea["fecha_limite"])
                print("Prioridad:", tarea["prioridad"])
                print("Completada:", tarea["completada"])
                print()
        else:
            print("No hay tareas completadas.")
    else:
        pendientes_tareas = [tarea for tarea in tareas if not tarea["completada"]]
        if pendientes_tareas:
            print("Tareas pendientes:")
            for i, tarea in enumerate(pendientes_tareas, start=1):
                print(f"Tarea {i}:")
                print("Descripción:", tarea["descripcion"])
                print("Fecha límite:", tarea["fecha_limite"])
                print("Prioridad:", tarea["prioridad"])
                print("Completada:", tarea["completada"])
                print()
        else:
            print("No hay tareas pendientes.")

def marcar_completada(tareas):
    indice = int(input("Ingrese el número de tarea que desea marcar como completada: ")) - 1
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        print("La tarea ha sido marcada como completada.")
    else:
        print("Índice inválido. No se pudo marcar la tarea como completada.")

if __name__ == "__main__":
    tareas = []

    while True:
        print("Menú:")
        print("1. Agregar tarea")
        print("2. Mostrar todas las tareas")
        print("3. Mostrar tareas completadas")
        print("4. Mostrar tareas pendientes")
        print("5. Marcar tarea como completada")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            fecha_limite = input("Ingrese la fecha límite de la tarea: ")
            prioridad = input("Ingrese la prioridad de la tarea: ")
            completada_input = input("¿La tarea fue completada? (si/no): ")
            agregar_tarea(tareas, descripcion, fecha_limite, prioridad, completada_input)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas, completadas=True)
        elif opcion == "4":
            mostrar_tareas(tareas, completadas=False)
        elif opcion == "5":
            marcar_completada(tareas)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")