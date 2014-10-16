from sys import platform
from os import system

# Autor: Fernando Parada
# Funcion para borrar pantalla multiplataforma
def borrar_pantalla():
    if platform  == "linux" or platform == "linux2" or platform == "darwin":
        # Unix/linux/OS X/BSD
        system("clear")
    elif platform == "win32":
        # Windows...
        system("cls")


def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
        if os.name == "posix":
                    os.system ("clear")
                        elif os.name == ("ce", "nt", "dos"):
                                    os.system ("cls")

                                    clear()
