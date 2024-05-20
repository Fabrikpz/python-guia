def tabla_mult ():
    while True:
        try:
            num = int(input("Introduce un num entre el 1 y 10:"))
            num2 = int(input("Introduce otro num entre el 1 y 10:"))
            if 1 <= num <= 10 and 1 <= num2 <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    
    nombre_archivo = f"tabla-{num}.txt"
    
    try:
        with open (nombre_archivo, "r") as archivo:
            print(f"Línea {num2} de la tabla de multiplicar del {num}:")
            contador = 0
            for linea in archivo:
                contador += 1
                if contador == num2:
                    print(linea.strip())
                    break
            
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    
tabla_mult()