def encontrar_palabra_mas_comun(texto):
    palabras = texto.split()

    frecuencia_palabras = {}

    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    palabra_mas_comun = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_mas_alta = frecuencia_palabras[palabra_mas_comun]

    return palabra_mas_comun, frecuencia_mas_alta

texto_ejemplo = "Los exploradores descubren un manuscrito antiguo y desean encontrar la palabra más común en él. Implementa un programa que utilice un diccionario para encontrar la palabra con la frecuencia más alta en el texto."

palabra_mas_comun, frecuencia_mas_alta = encontrar_palabra_mas_comun(texto_ejemplo)

print("Palabra más común:", palabra_mas_comun)
print("Frecuencia más alta:", frecuencia_mas_alta)
