import math

def cartesian_a_polar(x, y):
    # Calcula el radio utilizando el teorema de Pitágoras
    radio = math.sqrt(x**2 + y**2)
    
    # Calcula el ángulo en radianes utilizando la función arcotangente
    angulo_radianes = math.atan2(y, x)
    
    # Convierte el ángulo de radianes a grados
    angulo_grados = math.degrees(angulo_radianes)
    
    return radio, angulo_grados

# Coordenadas cartesianas del objeto misterioso
x = 3
y = 4

radio, angulo = cartesian_a_polar(x, y)

print("Coordenadas polares:")
print("Radio:", radio)
print("Ángulo (en grados):", angulo)
