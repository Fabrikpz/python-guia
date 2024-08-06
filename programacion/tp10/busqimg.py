def busqueda_en_imagen(img, tono):
    resultados = {}
    for y, fila in enumerate(img):
        for x, valor in enumerate(fila):
            if valor == tono:
                resultados[(x, y)] = valor

    return resultados    