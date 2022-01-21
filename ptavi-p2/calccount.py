#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Calc:

    def __init__(self):
        self.count = 0

    def add(self, operand1, operand2):
        self.count = self.count + 1
        return operand1 + operand2

    def sub(self, operand1, operand2):
        self.count = self.count + 1
        return operand1 - operand2

    def mul(self, operand1, operand2):
        self.count = self.count + 1
        return operand1 * operand2

    def div(self, operand1, operand2):
        self.count = self.count + 1
        try:
            return operand1 / operand2

        except ZeroDivisionError:
            print("Division by zero is not allowed")
        raise ValueError('Division by zero is not allowed')
