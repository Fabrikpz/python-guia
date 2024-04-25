def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

frase = input("Ingrese una frase: ")
print("Número de palabras:", contar_palabras(frase))
