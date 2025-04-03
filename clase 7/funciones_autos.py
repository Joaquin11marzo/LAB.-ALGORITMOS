def hacer_auto(fabricante, modelo, **info_extra):
    auto = {"fabricante": fabricante, "modelo": modelo}
    auto.update(info_extra)
    return auto