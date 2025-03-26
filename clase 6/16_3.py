lenguajes_favoritos = {
    "Juan": "python",
    "Sara": "c",
    "Eduardo": "rust",
    "Agustina": "c#"
}
personas = ["Ivan999", "Sara", "Jorge", "Juan", "Jesus"]
for indv in personas:
    if indv in lenguajes_favoritos:
        print("Muchas gracias", indv, "por participar")
    else:
        print("Te invito a que hagas la encuesta", indv)