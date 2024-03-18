print("ingrese base:")
base = int(input())
print("ingrese altura:")
altura = int(input())

def calcArea(base, altura):
  area = (base * altura) / 2
  return area

print(calcArea(base, altura))