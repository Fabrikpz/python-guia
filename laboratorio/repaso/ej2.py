def convertir_faren(temp_celsius):
    temp = float(temp_celsius)
    fahrenheit = (temp * 9/5) + 32.
    return print("Temp en fahrenheit: ", fahrenheit)

temp_celsius = input("Ingrese temp en celsius: ")
convertir_faren(temp_celsius)