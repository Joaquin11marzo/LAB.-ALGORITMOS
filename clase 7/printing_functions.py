def imprimir_modelos(diseños_no_impresos, modelos_completados):
    while diseños_no_impresos:
        diseño_actual = diseños_no_impresos.pop()
        print(f"Imprimiendo modelo: {diseño_actual}")
        modelos_completados.append(diseño_actual)

def mostrar_modelos_completados(modelos_completados):
    print("Los siguientes modelos han sido impresos:")
    for modelo_completado in modelos_completados:
        print(modelo_completado)