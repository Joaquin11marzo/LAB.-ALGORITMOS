nombres_usuarios = ["Admin", "Ivan999", "Pancioso343", "Ayalec07", "Milanesa333"]

if not nombres_usuarios:
    print("NOS QUEDAMOS SIN CHAMBEADORES, EMPRESA EN EL ANTIPRIME")
for usuario in nombres_usuarios:
    if usuario == "Admin":
        print("Hola señor papu admin, como estas?")
    if usuario != "Admin":
        print("A chambear",usuario ,"por no ser premium🤑")