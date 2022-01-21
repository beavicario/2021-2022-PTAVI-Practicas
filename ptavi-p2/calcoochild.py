#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

import calcoo


class CalcChild(calcoo.Calc):

    def mul(self, operand1, operand2):
        return operand1 * operand2

    def div(self, operand1, operando2):
        try:
            return operand1 / operand2

        except ZeroDivisionError:
            print("Division by zero is not allowed")
        raise ValueError('Division by zero is not allowed')


if __name__ == "__main__":
    try:
        operand1 = float(sys.argv[1])
        operand2 = float(sys.argv[3])
        calculadora = CalcChild()

    except ValueError:
        sys.exit("Error: first and third arguments should be numbers")

    if sys.argv[2] == "+":
        result = calculadora.add(operand1, operand2)
    elif sys.argv[2] == "-":
        result = calculadora.sub(operand1, operand2)
    elif sys.argv[2] == "*":
        result = calculadora.mul(operand1, operand2)
    elif sys.argv[2] == "/":
        result = calculadora.div(operand1, operand2)
    else:
        sys.exit('Operand should be + or - or * or /')

    print(result)
