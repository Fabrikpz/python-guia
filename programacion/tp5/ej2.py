num = input("Ingrese un número: ")

try:
    num_int = int(num)
except ValueError:
    print("Error: Por favor, ingrese un valor válido.")