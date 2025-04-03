class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.clientes_atendidos = 0

    def describir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' está ahora abierto.")

    def establecer_clientes_atendidos(self, cantidad):
        self.clientes_atendidos = cantidad

    def incrementar_clientes_atendidos(self, cantidad):
        self.clientes_atendidos += cantidad

restaurante = Restaurante("LOS PAPUS", "Venezolana")
print(f"Nombre del restaurante: {restaurante.nombre_restaurante}")
print(f"Tipo de cocina: {restaurante.tipo_cocina}")
restaurante.describir_restaurante()
restaurante.abrir_restaurante()

print(f"Clientes atendidos 1: {restaurante.clientes_atendidos}")
restaurante.clientes_atendidos = 20
print(f"Clientes atendidos 2: {restaurante.clientes_atendidos}")
restaurante.establecer_clientes_atendidos(50)
print(f"Clientes atendidos 3: {restaurante.clientes_atendidos}")
restaurante.incrementar_clientes_atendidos(15)
print(f"Clientes atendidos 4: {restaurante.clientes_atendidos}")