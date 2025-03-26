usuarios_actuales = ["XxIsagiXKurona4everxX", "Ivan999", "Pancioso343", "Ayalec07", "Milanesa333"]
usuarios_nuevos = ["Ivan999", "DonSilenZZZioXLuffy", "HioriChad111", "Lavicho", "NagiPTW"]
usuarios_actuales2 = []
usuarios_nuevos2 = []
for nuevos_usuarios in usuarios_nuevos:
    nuevos_usuarios = nuevos_usuarios.lower()
    usuarios_nuevos2.append(nuevos_usuarios)
for actuales_usuarios in usuarios_actuales:
    actuales_usuarios = actuales_usuarios.lower()
    usuarios_actuales2.append(actuales_usuarios)
for nuevos_nombres_usuarios in usuarios_nuevos2:
    if nuevos_nombres_usuarios in usuarios_actuales2:
        print(f"{nuevos_nombres_usuarios}: Este nombre no se va a poder usar papu🥺")
    elif nuevos_nombres_usuarios != usuarios_actuales2:
        print(f"{nuevos_nombres_usuarios}: NOMBRE DE USUARIO DISPONIBLE🤓")