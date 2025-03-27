edad = 0
while edad != -1:
    edad = int(input("Ingrese su edad:"))
    if edad == -1:
        break
    elif edad >= 0 and edad < 3:
        print("Tu entrada es gratis🤑")
    elif edad >= 3 and edad <= 12:
        print("Tu entrada sale 10 pesos😋")
    else:
        print("Tu entrada sale 15 pesos😥")