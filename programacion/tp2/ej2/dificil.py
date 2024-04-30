import math

def calcular_combinaciones(n, k):
    """
    Función para calcular el número de combinaciones posibles de n elementos tomados de k en k.
    """
    combinaciones = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return combinaciones

def main():
    print("Ingrese el número total de personajes disponibles:")
    total_personajes = int(input())
    print("Ingrese el tamaño del equipo de aventureros:")
    tamano_equipo = int(input())

    # Calcula el número de combinaciones posibles
    num_combinaciones = calcular_combinaciones(total_personajes, tamano_equipo)

    print("El número total de combinaciones posibles de formar un equipo de aventureros es:", num_combinaciones)

if __name__ == "__main__":
    main()
