import time

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)
        print(f"Conexión agregada: {self.nombre} -> {nodo.nombre}")

    def eliminar_conexion(self, nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)
            print(f"Conexión eliminada: {self.nombre} -> {nodo.nombre}")
        else:
            print(f"Conexión no encontrada: {self.nombre} -> {nodo.nombre}")

    def enviar_mensaje(self, mensaje):
        print(f"{self.nombre} envía mensaje: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibió el mensaje de {remitente}: {mensaje}")

servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

servidor.enviar_mensaje("boenas")

print("\nSimulando desconexión y reconexión dinámica...")

servidor.eliminar_conexion(cliente2)

time.sleep(2)

servidor.agregar_conexion(cliente2)

servidor.enviar_mensaje("¡Hola de nuevo a todos!")

if __name__ == "__main__":
    servidor.enviar_mensaje("testing")
