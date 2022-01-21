#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Calc:
    """Clase madre"""
    def __init__(self):
        self.count = 0

    def add(self, operando1, operando2):
        self.count = self.count + 1
        return operando1 + operando2

    def sub(self, operando1, operando2):
        self.count = self.count + 1
        return operando1 - operando2

    def mul(self, operando1, operando2):
        self.count = self.count + 1
        return operando1 * operando2

    def div(self, operando1, operando2):
        self.count = self.count + 1
        try:
            return operando1 / operando2
        except ZeroDivisionError:
            print("Division by zero is not allowed")
        raise ValueError('Division by zero is not allowed')
