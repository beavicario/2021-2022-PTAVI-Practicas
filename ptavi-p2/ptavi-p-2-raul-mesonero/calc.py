#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Simple calculator.

This module provides two functions, add and sub, to add or substract
two operands.
The main code of the module taks operands and operation (+ or -)
from the command line, as arguments when running the program.
The format for calling the module from the command line is:
calc.py op1 op op2
For example:
calc.py 4 + 7
11
"""

import sys


def add(op1, op2):
    """ Function to add the operands"""
    return op1 + op2


def sub(op1, op2):
    """ Function to substract the operands """
    return op1 - op2


if __name__ == "__main__":
    try:
        operand1 = float(sys.argv[1])
        operand2 = float(sys.argv[3])
    except ValueError:
        sys.exit("Error: first and third arguments should be numbers")

    if sys.argv[2] == "+":
        result = add(operand1, operand2)
    elif sys.argv[2] == "-":
        result = sub(operand1, operand2)
    else:
        sys.exit('Operand should be + or -')

    print(result)
