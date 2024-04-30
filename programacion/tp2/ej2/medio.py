print("ingrese potencia del hechizo primero y dps la resistencia del enemigo:")
pot = int(input())
resistencia = int(input())

def funcion (pot, resistencia):
  if pot > resistencia:
    print("el hechizo ha sido efectivo")
  elif resistencia <= pot:
    print("el hechizo no ha sido efectivo")

funcion(pot, resistencia)