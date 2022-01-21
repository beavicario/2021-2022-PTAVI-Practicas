#!/usr/bin/python3
# -*- coding: utf-8 -*-

import calccount


class CalcCalls(calccount.Calc):

    def __init__(self):
        calccount.Calc.__init__(self)

    def calls(self):
        return self.count
