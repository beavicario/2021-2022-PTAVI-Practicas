#!/usr/bin/python3
# -*- coding: utf-8 -*-

import contextlib
from io import StringIO
import os
import unittest

from xml.sax import make_parser
import chistes

this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(this_dir, '..')

result_text = """malo
Papapapaco. ¿Eres tartamudo?.
Yo no, mi padre. Y el del Registro Civil, un mamoncete
malisimo
Mamá, ¿por que te casaste con papá?
Ahhhh... ¡tú tampoco te lo explicas!
malillo
En que el elefante es un paquidermo y la cama es 'pakiduermas'
¿En que se parece un elefante a una cama?
malo
Subanestrujenbajen
¿Sabes cómo se dice "metro" en alemán?
"""


class TestChistes(unittest.TestCase):

    def test_class(self):
        stdout = StringIO()
        parser = make_parser()
        cHandler = chistes.ChistesHandler()
        parser.setContentHandler(cHandler)
        with contextlib.redirect_stdout(stdout):
            parser.parse(open(os.path.join(parent_dir, 'chistes.xml')))
        output = stdout.getvalue()
        self.assertEqual(output, result_text)

    def test_main(self):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            os.chdir(parent_dir)
            chistes.main()
        output = stdout.getvalue()
        self.assertEqual(output, result_text)

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
