def leer_en_linea(path):
    l = ""
    f = open(path)
    for linea in f:
        l = l + linea
    f.close()
    return l.replace("\n", " ")
