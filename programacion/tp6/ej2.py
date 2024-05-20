def tabla_mult ():
    while True:
        try:
            num = int(input("Introduce un num entre el 2 y 4:"))
            if 2 <= num <= 4:
                break
            else:
                print("El número debe estar entre 2 y 4.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
                
    nombre_archivo = f"tabla-{num}.txt"
    
    with open(nombre_archivo, "r") as archivo:
        print(f"Tabla de multiplicar del {num}:")
        for linea in archivo:
            print(linea.strip())

tabla_mult()
