def hacer_album(artista, titulo, canciones=None):
    album = {"artista": artista, "titulo": titulo}
    if canciones:
        album["canciones"] = canciones
    return album

while True:
    print("Ingresá los datos del álbum")
    artista = input("Nombre del artista: ")
    if artista.lower() == "salir":
        break

    titulo = input("Título del álbum: ")
    if titulo.lower() == "salir":
        break
    
    canciones = input("Cantidad de canciones:")
    canciones = int(canciones) if canciones.isdigit() else None
    album = hacer_album(artista, titulo, canciones)
    print("Álbum creado:", album)