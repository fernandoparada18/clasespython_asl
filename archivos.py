# -*- coding: utf-8 -*-
import os
from __future__ import print_function

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


def existe_archivo(archivo):
    if os.path.exists(archivo):
        print(u"Si es un archivo válido")
    else:
        print(u"No soy capaz de encontrarlo")
