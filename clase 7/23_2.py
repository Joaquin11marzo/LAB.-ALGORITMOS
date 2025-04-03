def hacer_album(artista, titulo, canciones=None):
    album = {"artista": artista, "titulo": titulo}
    if canciones:
        album["canciones"] = canciones
    return album

album1 = hacer_album("Taylor Swift", "Midnights")
album2 = hacer_album("Bad Bunny", "Un Verano Sin Ti")
album3 = hacer_album("Dua Lipa", "Future Nostalgia")
album4 = hacer_album("The Weeknd", "After Hours", 14)

print(album1)
print(album2)
print(album3)
print(album4)