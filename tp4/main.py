class JugadorDeFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numero_camiseta, estadisticas=None, premios=None):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo_actual = equipo
        self.pais_origen = pais
        self.numero_camiseta = numero_camiseta
        self.estadisticas = estadisticas if estadisticas is not None else {'goles': 0, 'asistencias': 0, 'amarillas': 0, 'rojas': 0}
        self.premios = premios if premios is not None else []

    def actualizar_informacion(self, nombre=None, edad=None, posicion=None, equipo=None, pais=None, numero_camiseta=None):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if posicion:
            self.posicion = posicion
        if equipo:
            self.equipo_actual = equipo
        if pais:
            self.pais_origen = pais
        if numero_camiseta:
            self.numero_camiseta = numero_camiseta

    def calcular_promedio_goles_por_partido(self, partidos_jugados):
        if partidos_jugados == 0:
            return 0
        return self.estadisticas['goles'] / partidos_jugados

    def es_goleador(self):
        return self.estadisticas['goles'] > 0

    def agregar_premio(self, premio):
        self.premios.append(premio)

    def eliminar_premio(self, premio):
        if premio in self.premios:
            self.premios.remove(premio)

    def actualizar_estadisticas(self, goles=0, asistencias=0, amarillas=0, rojas=0):
        self.estadisticas['goles'] += goles
        self.estadisticas['asistencias'] += asistencias
        self.estadisticas['amarillas'] += amarillas
        self.estadisticas['rojas'] += rojas
        self.actualizacion_estadisticas()

    def actualizacion_estadisticas(self):
        # Evento que se activa cuando se actualizan las estadísticas del jugador
        pass  # Aquí podrías agregar alguna lógica adicional si necesitas hacer algo cada vez que se actualizan las estadísticas

def crear_jugador():
    nombre = input("Ingrese el nombre del jugador: ")
    edad = int(input("Ingrese la edad del jugador: "))
    posicion = input("Ingrese la posición del jugador: ")
    equipo = input("Ingrese el equipo actual del jugador: ")
    pais = input("Ingrese el país de origen del jugador: ")
    numero_camiseta = int(input("Ingrese el número de camiseta del jugador: "))
    jugador = JugadorDeFutbol(nombre, edad, posicion, equipo, pais, numero_camiseta)
    return jugador

def mostrar_informacion_jugador(jugador):
    print("Información del jugador:")
    print(f"Nombre: {jugador.nombre}")
    print(f"Edad: {jugador.edad}")
    print(f"Posición: {jugador.posicion}")
    print(f"Equipo actual: {jugador.equipo_actual}")
    print(f"País de origen: {jugador.pais_origen}")
    print(f"Número de camiseta: {jugador.numero_camiseta}")
    print(f"Estadísticas: {jugador.estadisticas}")
    print(f"Premios y reconocimientos: {jugador.premios}")

def actualizar_informacion_jugador(jugador):
    print("Ingrese los nuevos datos del jugador (deje en blanco para mantener los valores actuales):")
    nombre = input(f"Nuevo nombre ({jugador.nombre}): ") or jugador.nombre
    edad = int(input(f"Nueva edad ({jugador.edad}): ")) or jugador.edad
    posicion = input(f"Nueva posición ({jugador.posicion}): ") or jugador.posicion
    equipo = input(f"Nuevo equipo actual ({jugador.equipo_actual}): ") or jugador.equipo_actual
    pais = input(f"Nuevo país de origen ({jugador.pais_origen}): ") or jugador.pais_origen
    numero_camiseta = int(input(f"Nuevo número de camiseta ({jugador.numero_camiseta}): ")) or jugador.numero_camiseta
    jugador.actualizar_informacion(nombre, edad, posicion, equipo, pais, numero_camiseta)
    print("Información actualizada exitosamente.")

def calcular_promedio_goles(jugador):
    partidos_jugados = int(input("Ingrese el número de partidos jugados: "))
    promedio = jugador.calcular_promedio_goles_por_partido(partidos_jugados)
    print(f"El promedio de goles por partido de {jugador.nombre} es: {promedio}")

def verificar_goleador(jugador):
    if jugador.es_goleador():
        print(f"{jugador.nombre} es un goleador.")
    else:
        print(f"{jugador.nombre} no es un goleador.")

def agregar_premio(jugador):
    premio = input("Ingrese el premio o reconocimiento a agregar: ")
    jugador.agregar_premio(premio)
    print(f"{premio} agregado a los premios y reconocimientos de {jugador.nombre}.")

def eliminar_premio(jugador):
    premio = input("Ingrese el premio o reconocimiento a eliminar: ")
    jugador.eliminar_premio(premio)
    print(f"{premio} eliminado de los premios y reconocimientos de {jugador.nombre}.")

def menu():
    print("\n--- Menú ---")
    print("1. Crear un nuevo jugador de fútbol")
    print("2. Mostrar la información de un jugador existente")
    print("3. Actualizar la información de un jugador existente")
    print("4. Calcular el promedio de goles por partido de un jugador")
    print("5. Verificar si un jugador es un goleador")
    print("6. Agregar un premio o reconocimiento a un jugador")
    print("7. Eliminar un premio o reconocimiento de un jugador")
    print("8. Salir")

jugadores = []

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        jugador_nuevo = crear_jugador()
        jugadores.append(jugador_nuevo)
        print("Jugador creado exitosamente.")

    elif opcion == '2':
        if jugadores:
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            jugador_encontrado = next((jugador for jugador in jugadores if jugador.nombre == nombre_jugador), None)
            if jugador_encontrado:
                mostrar_informacion_jugador(jugador_encontrado)
            else:
                print("El jugador no fue encontrado.")
        else:
            print("No hay jugadores registrados.")

    elif opcion == '3':
        if jugadores:
            nombre_jugador = input("Ingrese el nombre del jugador a actualizar: ")
            jugador_encontrado = next((jugador for jugador in jugadores if jugador.nombre == nombre_jugador), None)
            if jugador_encontrado:
                actualizar_informacion_jugador(jugador_encontrado)
            else:
                print("El jugador no fue encontrado.")
        else:
            print("No hay jugadores registrados.")

    elif opcion == '4':
        if jugadores:
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            jugador_encontrado = next((jugador for jugador in jugadores if jugador.nombre == nombre_jugador), None)
            if jugador_encontrado:
                calcular_promedio_goles(jugador_encontrado)
            else:
                print("El jugador no fue encontrado.")
        else:
            print("No hay jugadores registrados.")

    elif opcion == '5':
        if jugadores:
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            jugador_encontrado = next((jugador for jugador in jugadores if jugador.nombre == nombre_jugador), None)
            if jugador_encontrado:
                verificar_goleador(jugador_encontrado)
            else:
                print("El jugador no fue encontrado.")
        else:
            print("No hay jugadores registrados.")

    elif opcion == '6':
        if jugadores:
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            jugador_encontrado = next((jugador for jugador in jugadores if jugador.nombre == nombre_jugador), None)
            if jugador_encontrado:
                agregar_premio(jugador_encontrado)
            else:
                print("El jugador no fue encontrado.")
        else:
            print("No hay jugadores registrados.")

    elif opcion == '7':
        if jugadores:
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            jugador_encontrado = next((jugador for jugador in jugadores if jugador.nombre == nombre_jugador), None)
            if jugador_encontrado:
                eliminar_premio(jugador_encontrado)
            else:
                print("El jugador no fue encontrado.")
        else:
            print("No hay jugadores registrados.")

    elif opcion == '8':
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
