#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import calccount


class TestCalcCount(unittest.TestCase):

    def setUp(self):
        self.calc = calccount.Calc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)
        self.assertEqual(self.calc.count, 1)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 4), -2)
        self.assertEqual(self.calc.count, 1)

    def test_mul(self):
        self.assertEqual(self.calc.mul(2, 4), 8)
        self.assertEqual(self.calc.count, 1)

    def test_div(self):
        self.assertEqual(self.calc.div(2, 4), 0.5)
        self.assertEqual(self.calc.count, 1)

    def test_div_zero(self):
        with self.assertRaises(ValueError):
            self.calc.div(2, 0)

    def test_count(self):
        self.calc.add(2, 4)
        self.calc.sub(2, 4)
        self.calc.mul(2, 4)
        self.calc.div(2, 4)
        self.assertEqual(self.calc.count, 4)


if __name__ == '__main__':
    unittest.main()
