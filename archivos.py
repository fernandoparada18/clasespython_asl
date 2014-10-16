# -*- coding: utf-8 -*-
from __future__ import print_function
import os

def leer_f(archivo):
    f = open(archivo)
    for linea in f:
        print(linea)
    f.close()


def wfile(archivo):
    f = open(archivo, 'w')
    f.write("En un lugar de la mancha del cual no me acuerdo su nombre\n")
    f.close()


def afile(archivo):
    f = open(archivo, 'a')
    f.write("En un lugar de la mancha del cual no me acuerdo su nombre\n")
    f.close()


def rfile(archivo):
    f = open(archivo)
    print(f.readline())


def rfiles(archivo):
    f = open(archivo)
    print(f.readlines())

# Funcion para comprobar si existe un archivo.
def existe_archivo(archivo):
    existe = False
    if os.path.exists(archivo):
        print(u"Si es un archivo válido")
        existe = True
    else:
        print(u"No soy capaz de encontrarlo")
    return existe


def crear_archivo(archivo):
    if existe_archivo(archivo):
        print("Y ya existe!!!")
    else:
        r = raw_input("Desea crearlo? s/n ")
        if r == "s" or r == "S":
            archi = open(archivo,'w')
            archi.close()
            print("Archivo creado con exito!!!")
        else:
            print("Archivo no creado!!!")
