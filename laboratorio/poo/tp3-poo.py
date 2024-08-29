# Encapsulamiento: Atributos privados con acceso a través de métodos getter y setter
class Vehiculo():
    def __init__(self, marca, modelo, año):
        self.__marca = marca  # Encapsulamiento: atributo privado
        self.__modelo = modelo  # Encapsulamiento: atributo privado
        self.__año = año  # Encapsulamiento: atributo privado

    # Métodos para acceder y modificar los atributos privados (Encapsulamiento)
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_año(self):
        return self.__año

    def set_año(self, año):
        self.__año = año
        
    def detener(self):
        print(f"El vehículo {self.get_marca()} {self.get_modelo()} se está deteniendo.")

# Herencia: La clase Auto hereda de la clase Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)  # Herencia: llamada al constructor de la clase base
        self.__puertas = puertas  # Encapsulamiento: atributo privado

    # Encapsulamiento: Métodos getter y setter para el atributo privado
    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    # Polimorfismo: Método acelerar sobreescrito para Auto
    def acelerar(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} está acelerando.")
        
    def detener(self):
        print(f"El auto {self.get_marca()} {self.get_modelo()} se está deteniendo.")

# Herencia: La clase Motocicleta hereda de la clase Vehiculo
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)  # Herencia
        self.__cilindrada = cilindrada  # Encapsulamiento: atributo privado

    # Encapsulamiento: Métodos getter y setter para el atributo privado
    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    # Polimorfismo: Método acelerar sobreescrito para Motocicleta
    def acelerar(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} con cilindrada de {self.get_cilindrada()}cc está acelerando.")
        
    def detener(self):
        print(f"La motocicleta {self.get_marca()} {self.get_modelo()} se está deteniendo.")

# Herencia: La clase Camion hereda de la clase Vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada, capacidad_carga):
        super().__init__(marca, modelo, año)  # Herencia
        self.__cilindrada = cilindrada  # Encapsulamiento: atributo privado
        self.__capacidad_carga  = capacidad_carga  # Encapsulamiento: atributo privado
    
    # Encapsulamiento: Métodos getter y setter para los atributos privados
    def get_cilindrada(self):
        return self.__cilindrada
    
    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada
    
    def get_capacidad_carga(self):
        return self.__capacidad_carga
    
    def set_capacidad_carga(self, capacidad_carga):
        self.__capacidad_carga = capacidad_carga

    # Polimorfismo: Método acelerar sobreescrito para Camion
    def acelerar(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} con una cilindrada de {self.get_cilindrada()}cc está acelerando.")
        
    def detener(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} se está deteniendo.")

# Uso de un diccionario para almacenar los vehículos
if __name__ == "__main__":
    vehiculos_dict = {
        "Corolla": Auto("Toyota", "Corolla", 2020, 4),
        "MT-07": Motocicleta("Yamaha", "MT-07", 2019, 689),
        "FH": Camion("Volvo", "FH", 2017, 970, 2000)
    }
    
    # Polimorfismo: Cada objeto en el diccionario puede ser tratado de manera uniforme como Vehiculo
    for modelo, vehiculo in vehiculos_dict.items():
        vehiculo.acelerar()
        vehiculo.detener()
        
# Rta a pregunta: Se podría mejorar el diseño utilizando ABC y @abstractmethod para obligar a las subclases a implementar el método acelerar.