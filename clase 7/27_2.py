class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' ofrece comida {self.tipo_cocina}")

    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' está ahora abierto")

restaurante1 = Restaurante("LOS PAPUS", "Venezolana")
restaurante2 = Restaurante("TROLLEADOS", "Peruana")
restaurante3 = Restaurante("PeladosFC", "Cubana")
restaurante1.describir_restaurante()
restaurante2.describir_restaurante()
restaurante3.describir_restaurante()