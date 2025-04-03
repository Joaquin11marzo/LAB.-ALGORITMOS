def hacer_sanguche(*ingredientes):
    print("Preparando un sanguche con los estos ingredientes:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")
    print("Tu sanguche está listo papu :D")

hacer_sanguche("jamón", "queso", "lechuga", "tomate")
hacer_sanguche("pollo", "mayonesa")
hacer_sanguche("atún", "aceitunas", "huevo", "cebolla", "pimiento")