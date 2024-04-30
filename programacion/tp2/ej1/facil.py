print("ingrese dist")
dist = float(input())
print("ingrese vel")
vel = float(input())

def calcTiempo (dist, vel):
  tiempo = dist/vel
  return tiempo

print(calcTiempo(dist, vel))