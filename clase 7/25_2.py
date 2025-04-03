def construir_perfil(nombre, apellido, **info_usuario):
    info_usuario['nombre'] = nombre
    info_usuario['apellido'] = apellido
    return info_usuario

perfil_usuario = construir_perfil('Ivan', 'Perez',
                                  edad=30,
                                  ciudad='Buenos Aires',
                                  aficion='fotografía')

print(perfil_usuario)