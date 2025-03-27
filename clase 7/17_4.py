ciudades = {
    "Buenos Aires" : {
        "pais" : "Argentina",
        "poblacion" : "13.985.794"
    },
    "Londres" : {
        "pais" : "Inglaterra",
        "poblacion" : "9.002.488"
    },
    "Amsterdam" : {
        "pais" : "Holanda",
        "poblacion" : "18.032.658"
    }
}
for info1,ciu in ciudades.items():
    print(info1)
    for datos, info2 in ciu.items():
        print(datos, ":", info2)