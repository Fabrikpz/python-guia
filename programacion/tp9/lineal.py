lista = [3,4,6,1]

def busqlineal(lista, nro):
    for i, num in enumerate(lista):
        if num == nro:
            return i
    
    return -1
        
resultado = busqlineal(lista, 4)
print(f"{resultado}")