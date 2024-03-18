import random

pregs = ["¿Qué secreto guarda el antiguo dragón en lo profundo de su guarida en la cima de la montaña?",
         "¿Qué misterioso poder otorga el mago a aquellos que buscan la sabiduría en los oscuros bosques encantados?",
         "¿Qué maravillas y peligros aguardan a los valientes aventureros en las profundidades olvidadas de la antigua mazmorra?"]

rtas = ["riquezas incontables", "conocimiento infinito", "tesoros y monstruos"]

print("¡Bienvenido, aventurero! En lo profundo de los bosques, oculta entre sombras y misterios, se alza una antigua mazmorra. Allí, aguarda un desafío legendario: el juego de las tres adivinanzas. Solo aquellos con coraje y astucia podrán superarlo. Pero ten cuidado, solo tienes dos vidas. ¿Estás listo para ganar riquezas y poder más allá de tus sueños? Entonces, adéntrate, y que la fortuna te acompañe en tu búsqueda. Que comience el juego.")

vidas = 2

def verifRtas():
    global vidas
    preguntas_seleccionadas = random.sample(pregs, 3)
    respuestas_seleccionadas = []
    for pregunta in preguntas_seleccionadas:
        indice = pregs.index(pregunta)
        respuestas_seleccionadas.append(rtas[indice])

    while vidas > 0:
        for i in range(3):
            print("Pregunta", i + 1, ":", preguntas_seleccionadas[i])
            respuesta = input("Ingrese su respuesta: ").lower()
            if respuesta == respuestas_seleccionadas[i]:
                print("¡Correcto! Pasas a la siguiente pregunta...")
            else:
                vidas -= 1
                if vidas == 0:
                    print("¡Has perdido todas tus vidas! Serás sacrificado.")
                    return
                print("Incorrecto. Te quedan", vidas, "vida(s).")

# Llamar a la función para verificar las respuestas
verifRtas()
