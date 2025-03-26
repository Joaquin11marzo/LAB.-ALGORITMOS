edad = int(input("Ingrese su edad:"))
if edad < 2:
    print("Eres un@ bebe")
elif edad >= 2 and edad < 4:
    print("Eres un@ nen@ chiquit@")
elif edad >= 4 and edad < 13:
    print("Eres un@ nen@")
elif edad >= 13 and edad < 20:
    print("Eres un@ adolescente")
elif edad >= 20 and edad < 65:
    print("Eres un@ adult@")
else: 
    print("Eres un@ adult@ mayor")
