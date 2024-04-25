def agregar_tarea(tareas, descripcion, fecha_limite, prioridad):
    tarea = {"descripcion": descripcion, "fecha_limite": fecha_limite, "prioridad": prioridad}
    tareas.append(tarea)

def mostrar_tarea(tarea):
    for tarea in tareas:
        print("Descripción:", tarea["descripcion"])
        print("Fecha límite:", tarea["fecha_limite"])
        print("Prioridad:", tarea["prioridad"])
        print()

tareas = []

while True:
    print("Menú:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_limite = input("Ingrese la fecha límite de la tarea: ")
        prioridad = input("Ingrese la prioridad de la tarea: ")
        agregar_tarea(tareas, descripcion, fecha_limite, prioridad)
    elif opcion == "2":
        mostrar_tarea(tareas)
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")