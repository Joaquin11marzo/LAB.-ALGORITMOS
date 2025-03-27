ingredientes = ""
ingre = []
while ingredientes.lower() != "salir":
    ingredientes = str(input("Ingrese ingredientes para la :"))
    ingredientes.lower()
    if ingredientes.lower() == "salir":
        break
    ingre.append(ingredientes)
    print("Estas agregando a la pizza:", ingre)