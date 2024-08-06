import time
from busqimg import busqueda_en_imagen

#Función de prueba para comparar tiempos de ejecución
def prueba_busqueda(imagen, tono):
    inicio = time.time()
    resultados = busqueda_en_imagen(imagen, tono)
    tiempo_total = time.time() - inicio
    print(f"Tiempo de ejecución para imagen: {tiempo_total} segundos")
    return resultados

#Ejemplo
if __name__ == "__main__":
    imagen1 = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    imagen2 = [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ]
    
    tono_buscado = 1
    resultados_imagen1 = prueba_busqueda(imagen1, tono_buscado)
    resultados_imagen2 = prueba_busqueda(imagen2, tono_buscado)