import string

print("ingrese mensaje tallado en la piedra:")
mensaje = str(input())
abc = string.ascii_lowercase

def descifrarCoords(msj):
  coords = []
  for letra in msj:
    index = abc.index(letra)
    index+=1
    coords.append(index)
  return coords

print("Coordenadas del tesoro:", descifrarCoords(mensaje))