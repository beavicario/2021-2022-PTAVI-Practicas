#!/usr/bin/python3
# -*- coding: utf-8 -*-

import contextlib
from io import StringIO
import os
import unittest
import calccsv

this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(this_dir, '..')

result_operations = """8.0
8.0
8.0
8.0
8.0
8.0
Division by zero is not allowed
Bad format
Bad format
Bad format
Bad format
8.0
"""


class TestCalcCount(unittest.TestCase):

    def test_csv(self):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            calccsv.process_csv(os.path.join(parent_dir, 'operations.csv'))
        output = stdout.getvalue()
        self.assertEqual(output, result_operations)


if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
