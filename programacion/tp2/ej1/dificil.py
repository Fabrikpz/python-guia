def factorial(n):
  if n == 0 or n == 1:
      return 1
  else:
      return n * factorial(n - 1)

def calcular_combinaciones(total_personas, tamano_equipo):
  if total_personas < tamano_equipo:
      return 0
  else:
      combinaciones = factorial(total_personas) / (factorial(tamano_equipo) * factorial(total_personas - tamano_equipo))
      return combinaciones

total_personas = 10  # Número total de personas
tamano_equipo = 3    # Tamaño del equipo
num_combinaciones = calcular_combinaciones(total_personas, tamano_equipo)
print("El número total de combinaciones posibles es:", num_combinaciones)