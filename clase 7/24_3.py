def mostrar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje)

def enviar_mensajes(mensajes, mensajes_enviados):
    while mensajes:
        mensaje = mensajes.pop(0)
        print(f"Enviando mensaje: {mensaje}")
        mensajes_enviados.append(mensaje)

mensajes = [
    "Hola como estás papu?",
    "Nos vemos papu",
    "Tene buen dia papu",
    "A la noche nos vemos papu"
]

mensajes_enviados = []
enviar_mensajes(mensajes[:], mensajes_enviados)
print("Lista de mensajes originales después de enviar:", mensajes)
print("Lista de mensajes enviados:", mensajes_enviados)