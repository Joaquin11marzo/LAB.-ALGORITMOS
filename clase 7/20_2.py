pedidos_sandwiches = ["Lomito", "Milanesa", "Pescado", "Vegano"]
sandwiches_terminados = []
for sanguches in  pedidos_sandwiches:
    print("Mi señor, le he preparado su emparedado estilo:",sanguches)
    sandwiches_terminados.append(sanguches)
print("Tus sanguches fueron preparados:", *sandwiches_terminados)