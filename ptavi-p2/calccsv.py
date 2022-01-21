#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

import calccount


def process_csv(filename):
    with open(filename, "r", encoding='utf-8') as a_file:
        datos = a_file.read().split("\n")
        datos.pop()

    cuenta = calccount.Calc()

    for operacion in datos:
        operador = operacion.split(",")[0]
        result = float(operacion.split(",")[1])
        error = False

        try:
            for number in operacion.split(",")[2:]:
                operando = float(number)
                if operador == "+":
                    result = cuenta.add(result, operando)
                elif operador == "-":
                    result = cuenta.sub(result, operando)
                elif operador == "x":
                    result = cuenta.mul(result, operando)
                elif operador == "/":
                    result = cuenta.div(result, operando)
                else:
                    error = True

            if not error:
                print(result)
            else:
                print("Bad format")

        except ValueError:
            if operador != "/":
                print("Bad format")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        filename = 'fichero.csv'
    else:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            sys.exit("Error: File not found")

    process_csv(filename)
