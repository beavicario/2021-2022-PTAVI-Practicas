#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import os
import sys

import calccount


def process_csv(filename):
    with open(filename, "r", encoding='utf-8') as a_file:
        datos = csv.reader(a_file, delimiter=',')

        cuenta = calccount.Calc()

        for operacion in datos:
            operador = operacion[0]
            result = float(operacion[1])
            Not_Allowed = False

            try:
                for number in operacion[2:]:
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
                        Not_Allowed = True

                if not Not_Allowed:
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
