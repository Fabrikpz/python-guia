informacion_personal = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "María", "edad": 30},
    {"nombre": "Pedro", "edad": 28}
]

primer_diccionario = informacion_personal[0]
nombre_primera_persona = primer_diccionario["nombre"]
edad_segunda_persona = informacion_personal[1]["edad"]

print("Nombre de la primera persona:", nombre_primera_persona)
print("Edad de la segunda persona:", edad_segunda_persona)

for diccionario in informacion_personal:
    for key, value in diccionario.items():
        print(key + ":", value)
    print()