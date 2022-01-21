#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calc


class CalcChild(Calc):
    def mul(self, operando1, operando2):
        return operando1 * operando2

    def div(self, operando1, operando2):
        try:
            return operando1 / operando2
        except ZeroDivisionError:
            print("Division by zero is not allowed")
            raise ValueError('Error')


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    calcchild = CalcChild()
    if sys.argv[2] == "+":
        resultado = calcchild.add(operando1, operando2)
    elif sys.argv[2] == "-":
        resultado = calcchild.sub(operando1, operando2)
    elif sys.argv[2] == "x":
        resultado = calcchild.mul(operando1, operando2)
    elif sys.argv[2] == "/":
        resultado = calcchild.div(operando1, operando2)
    else:
        sys.exit('Operación sólo puede sumar, restar, multiplicar o dividir')
    print(resultado)
