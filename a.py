def conversor_factores_unidad(inicio: str, objetivo: str) -> str:
    """
    descripcion

    Args:
        inicio: un numero seguido de sus unidades. e.g.: 27GB
        objetivo: la unidad objetivo a la que hacer la conversión

    Returns:
        El valor convertido a la unidad objetivo junto a su unidad
    """

    UNIDADES = (
        ("m", 0.001),
        ("c", 0.01),
        ("d", 0.1),
        ("K", 1000),
        ("M", 1000000),
        ("G", 1000000000),
        ("T", 1000000000000),
        ("P", 1000000000000000),
        ("E", 1000000000000000000)
    )


    def separar_unidades(valor: str) -> tuple:
        num = ""
        unidad = ""

        for c in valor:
            if c in "0123456789":
                num += c
            elif c == "":
                continue
            else:
                unidad += c

        return (float(num), unidad)

    def factor_de_conversion(unidades_i, unidades_o):
        trobats = [None, None]
        i = 0

        print(unidades_i, unidades_o)

        while ((trobats[0] == None) or (trobats[1] == None)) and i < len(UNIDADES):
            if UNIDADES[i][0] == unidades_i:
                trobats[0] = UNIDADES[i][1]
            elif UNIDADES[i][0] == unidades_o:
                trobats[1] = UNIDADES[i][1]

            i += 1

        # Unidades objetivo / unidades iniciales = factor de conversión
        return (trobats[0] / trobats[1]) if ((trobats[0] != None) and (trobats[1] != None)) else "No es pot fer la conversió"
    
    n_inicio, u_inicio = separar_unidades(inicio)

    fc = factor_de_conversion(u_inicio[0], objetivo[0])

    return str(n_inicio * fc) + objetivo if str(fc).isnumeric() else fc
