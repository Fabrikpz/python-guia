class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso

    def programar(self):
        print(f"El alumno {self.nombre} está programando")

    def __str__(self):
        return f"Alumno: {self.nombre} {self.apellido}, Edad: {self.edad}, Curso: {self.curso}"

nombre = input("Ingrese el nombre del alumno: ").strip().lower()
apellido = input("Ingrese el apellido del alumno: ").strip().lower()
edad = int(input("Ingrese la edad del alumno: "))
curso = input("Ingrese el curso del alumno: ").strip().lower()

alumno1 = Alumno(nombre, apellido, edad, curso)
alumno1.programar()
