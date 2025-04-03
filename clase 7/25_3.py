def hacer_auto(fabricante, modelo, **info_extra):
    auto = {"fabricante": fabricante, "modelo": modelo}
    auto.update(info_extra)
    return auto
auto = hacer_auto('toyota', 'corolla', color='gris', airbags=True)
print(auto)