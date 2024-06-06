class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)
        print(f"Conexión agregada: {self.nombre} -> {nodo.nombre}")

    def enviar_mensaje(self, mensaje):
        print(f"{self.nombre} envía mensaje: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, remitente):
        print(f"{self.nombre} recibió mensaje de {remitente}: {mensaje}")

servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente 1")
cliente2 = Nodo("Cliente 2")
cliente3 = Nodo("Cliente 3")

servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

servidor.enviar_mensaje("boenas")

if __name__ == "__main__":
    servidor.enviar_mensaje("testing")
