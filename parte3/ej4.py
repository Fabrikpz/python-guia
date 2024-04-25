def es_palindromo(palabra):
    palabra = palabra.lower()
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
