def rfile(archivo):
    f = open(archivo)
    for linea in f:
        print linea
    f.close()

def wfile(archivo):
    f = open(archivo, 'w')
    f.write("En un lugar de la mancha del cual no me acuerdo su nombre\n")
    f.close()

def afile(archivo):
    f = open(archivo, 'a')
    f.write("En un lugar de la mancha del cual no me acuerdo su nombre\n")
    f.close()
