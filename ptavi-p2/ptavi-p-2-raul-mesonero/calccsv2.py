#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import calccount
import re
import csv

resultado = 0

with open(sys.argv[1], newline='') as csvfile:
    lineas = csv.reader(csvfile, delimiter=",")
    for info in lineas:
        stringer = "/n"
        eliminar = info[-1]
        stringer = re.sub("/|\n|", "", eliminar)
        info[-1] = stringer
        operador = info[0]
        if operador != '+' and operador != '-' and operador != '/' \
                and operador != 'x':
            print("Bad Format")
        if info[-1] == "error":
            print("Bad Format")
        else:
            lista_numeros = list(map(float, info[1:]))
            if operador == "+":
                resultado = 0
                for lista in lista_numeros[0:]:
                    heredero = calccount.Calc()
                    resultado = heredero.add(resultado, lista)
                print(resultado)
            if operador == "-":
                resultado = lista_numeros[0] - lista_numeros[1]
                for lista in lista_numeros[2:]:
                    heredero = calccount.Calc()
                    resultado = heredero.sub(resultado, lista)
                print(resultado)
            if operador == "x":
                resultado = lista_numeros[0] * lista_numeros[1]
                for lista in lista_numeros[2:]:
                    heredero = calccount.Calc()
                    resultado = heredero.mul(resultado, lista)
                print(resultado)
            if operador == "/":
                if lista_numeros[0] == 0 or lista_numeros[1] == 0:
                    print("Error: division by zero")
                else:
                    resultado = lista_numeros[0] / lista_numeros[1]
                for lista in lista_numeros[2:]:
                    if lista == 0:
                        print("Error: division by zero")
                    else:
                        heredero = calccount.Calc()
                        resultado = heredero.div(resultado, lista)
                        print(resultado)
