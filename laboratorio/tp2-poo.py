class Mago:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hechizos(self):
        print("Mago lanzando hechizos")


class Guerrero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def defensa(self):
        print("Guerrero defendiendo")


class Elfo:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def aura(self):
        print("Elfo con aura")


class DarkLord(Guerrero, Elfo):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hechizos(self):
        print("DarkLord lanzando hechizos")


dark_lord = DarkLord("Sauron", 1000)
dark_lord.defensa()
dark_lord.aura()    
dark_lord.hechizos() 

print(DarkLord.__mro__)

class DarkLord2(Elfo, Guerrero):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def hechizos(self):
        print("DarkLord lanzando hechizos")

dark_lord2 = DarkLord2("Sauron", 1000)
dark_lord2.defensa()  
dark_lord2.aura()     
dark_lord2.hechizos() 

print(DarkLord2.__mro__)