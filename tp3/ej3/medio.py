inscripcion = "La inscripcion antigua en el templo"

frecuencia_letras = {}

for letra in inscripcion:
    if letra != " ":
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        else:
            frecuencia_letras[letra] = 1

print("Frecuencia de cada letra en la inscripción:")
for letra, frecuencia in frecuencia_letras.items():
    print(f"{letra}: {frecuencia}")
