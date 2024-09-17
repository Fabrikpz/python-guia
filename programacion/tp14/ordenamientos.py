import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

def irsertion_sort(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x <= pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

def medir_tiempo(algoritmo, lista):
    inicio = time.time()
    algoritmo(lista.copy())  # Usar una copia para no modificar la lista original
    fin = time.time()
    return fin - inicio

# Crear listas de diferentes tamaños para pruebas
def generar_listas(tamanos):
    return [random.sample(range(10000), size) for size in tamanos]

# Probar los algoritmos con listas de diferentes tamaños y graficar los resultados
def comparar_algoritmos():
    tamanos = [100, 500, 1000, 5000, 10000]  # Tamaños de lista
    listas = generar_listas(tamanos)

    tiempos_burbuja = []
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_rapido = []
    tiempos_fusion = []

    for lista in listas:
        tiempos_burbuja.append(medir_tiempo(ordenamiento_burbuja, lista))
        tiempos_seleccion.append(medir_tiempo(ordenamiento_seleccion, lista))
        tiempos_insercion.append(medir_tiempo(ordenamiento_insercion, lista))
        tiempos_rapido.append(medir_tiempo(ordenamiento_rapido, lista))
        tiempos_fusion.append(medir_tiempo(ordenamiento_fusion, lista))

    # Graficar los resultados
    plt.plot(tamanos, tiempos_burbuja, label="Burbuja")
    plt.plot(tamanos, tiempos_seleccion, label="Selección")
    plt.plot(tamanos, tiempos_insercion, label="Inserción")
    plt.plot(tamanos, tiempos_rapido, label="Rápido (QuickSort)")
    plt.plot(tamanos, tiempos_fusion, label="Fusión (MergeSort)")

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de Algoritmos de Ordenamiento')
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejecutar comparación
comparar_algoritmos()
