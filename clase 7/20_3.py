def encuesta_vaca():
    resp = []
    while True:
        destino = input("Destino soñado:")
        if destino.lower() == 'salir':
            break
        resp.append(destino)
    print("Resultados de la encuesta:")
    for numero, destino in enumerate(resp, 1):
        print(f"Persona {numero} quiere visitar {destino}")
encuesta_vaca()