#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calc:
    """Clase madre"""

    def add(self, operando1, operando2):
        return operando1 + operando2

    def sub(self, operando1, operando2):
        return operando1 - operando2


if __name__ == "__main__":
    try:
        operando1 = float(sys.argv[1])
        operando2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    calc = Calc()                # se inicializa el objeto de la clase Calc
    if sys.argv[2] == "+":
        resultado = calc.add(operando1, operando2)
    elif sys.argv[2] == "-":
        resultado = calc.sub(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')
    print(resultado)
