#! /usr/bin/env python
# -*- coding: utf-8 -*-

import string

def a_palabras(frase):

    permitidos = "abcdefghijklmnñopqrstuvwxyz áéíóú"
    frase_limp = ""
    frase_min = frase.lower()

    for i in frase_min:
        if i in permitidos:
            frase_limp += i

    palabras = frase_limp.split()

    return palabras


def main():

    diccionario = {}
    lengua = raw_input("¿Qué idioma usaremos para la traducción?: ")

    while True:

        print
        frase = raw_input("Escriba una frase completa ('*' para terminar): ")

        if frase == "*":
            break
        else:
            palabras = a_palabras(frase)


        print
        for i in palabras:
            i = unicode(i, 'utf-8')
            i = i.title()

            if i not in diccionario:
                significado = raw_input("¿Cómo se escribe '%s' en %s?: " % (i,lengua))
                significado = significado.lower()
                significado = unicode(significado, 'utf-8')
                significado = significado.title()
                diccionario[i] = significado

    print "\nDiccionario: \n"
    for i in diccionario:
        print i, "\t=", diccionario[i].title()

main()
