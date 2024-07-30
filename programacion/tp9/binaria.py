def busqueda_binaria(lista, elemento):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

lista = [1, 3, 4, 6, 8, 10, 15, 20]
elemento = 6
resultado = busqueda_binaria(lista, elemento)
print(f"Índice del elemento {elemento}: {resultado}")
