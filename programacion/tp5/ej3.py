my_list = []

try:
    element = my_list[0] 
    print("Elemento en la posición 0:", element)
except IndexError:
    print("Error: El índice está fuera del rango de la lista.")
