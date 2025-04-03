class Usuario:
    def __init__(self, nombre, apellido, edad, ciudad, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ciudad = ciudad
        self.ocupacion = ocupacion
        self.intentos_login = 0

    def describir_usuario(self):
        print(f"Perfil del usuario:")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Ciudad: {self.ciudad}")
        print(f"Ocupación: {self.ocupacion}")

    def saludar_usuario(self):
        print(f"Hola {self.nombre} {self.apellido}, que tengas un buen día papu :D")

    def incrementar_intentos_login(self):
        self.intentos_login += 1

    def reiniciar_intentos_login(self):
        self.intentos_login = 0

usuario1 = Usuario("Ivan", "Perez", 30, "Buenos Aires", "Estudiante")
usuario1.incrementar_intentos_login()
usuario1.incrementar_intentos_login()
usuario1.incrementar_intentos_login()
print(f"Intentos de login de {usuario1.nombre}: {usuario1.intentos_login}")
usuario1.reiniciar_intentos_login()
print(f"Intentos de login después de reiniciar: {usuario1.intentos_login}")