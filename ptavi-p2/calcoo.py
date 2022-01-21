#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calc():

    def add(self, operand1, operand2):
        return operand1 + operand2

    def sub(self, operand1, operand2):
        return operand1 - operand2


if __name__ == "__main__":
    try:
        operand1 = float(sys.argv[1])
        operand2 = float(sys.argv[3])
        calculadora = Calc()

    except ValueError:
        sys.exit("Error: first and third arguments should be numbers")

    if sys.argv[2] == "+":
        result = calculadora.add(operand1, operand2)
    elif sys.argv[2] == "-":
        result = calculadora.sub(operand1, operand2)
    else:
        sys.exit('Operand should be + or -')

    print(result)
