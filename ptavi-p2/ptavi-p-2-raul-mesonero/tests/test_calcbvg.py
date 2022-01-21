#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calcbvg


class TestCalcCount:

    def __init__(self):
        self.calc = calcbvg.CalcCalls()

    def count(self):
        self.calc.add(3, 2)
        self.calc.sub(5, 4)
        self.calc.mul(4, 1)
        print("Contador:", self.calc.calls())


if __name__ == '__main__':
    unittest = TestCalcCount()
    unittest.count()
