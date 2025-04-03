class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
        self.ocupacion = ocupacion

    def describir_usuario(self):
        print(f"Perfil del usuario:")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Ciudad: {self.ciudad}")
        print(f"Ocupación: {self.ocupacion}")

    def saludar_usuario(self):
        print(f"Hola {self.nombre} {self.apellido}, que tengas un buen dia papu :D")

usuario1 = Usuario("Ivan", "Perez", 30, "Buenos Aires", "estudiante")
usuario2 = Usuario("Eduardo", "Gomez", 25, "Madrid", "diseñador gráfico")
usuario3 = Usuario("Estefano", "López", 40, "Lima", "profesor")

usuario1.describir_usuario()
usuario1.saludar_usuario()
print("")
usuario2.describir_usuario()
usuario2.saludar_usuario()
print("")
usuario3.describir_usuario()
usuario3.saludar_usuario()