class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' ofrece comida {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print(f"El restaurante '{self.nombre_restaurante}' está ahora abierto.")

class PuestoDeHelados(Restaurante):
    def __init__(self, nombre_restaurante, tipo_cocina, sabores):
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"\nSabores disponibles en '{self.nombre_restaurante}':")
        for sabor in self.sabores:
            print(f"- {sabor}")

heladeria = PuestoDeHelados("Los Papus Helados", "Heladería", ["Chocolate", "Crema Americana", "Frutilla", "Dulce de leche"])
heladeria.describir_restaurante()
heladeria.abrir_restaurante()
heladeria.mostrar_sabores()