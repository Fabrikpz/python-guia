def operacion_matematica(x, y):
    try:
        resultado = x + y
        return resultado 
    except TypeError:
        return "Error: Los argumentos no son del tipo de datos esperado para realizar la operación matemática."

print(operacion_matematica(5, 3))  # Suma dos números enteros
print(operacion_matematica("Hola", "mundo"))  # Intenta sumar dos cadenas de texto
