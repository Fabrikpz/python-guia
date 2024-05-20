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
    
    with open(nombre_archivo, "w") as fichero:
        for i in range(1,11):
            fichero.write(f"{num} x {i} = {num * i}\n")
        
    print(f"Tabla de multiplicar del {num} guardada en {nombre_archivo}")

tabla_mult()

        
            