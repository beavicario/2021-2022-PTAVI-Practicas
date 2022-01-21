#!/usr/bin/python3
# -*- coding: utf-8 -*-

import contextlib
from io import StringIO
import os
import unittest

from xml.sax import make_parser
import chistes2

this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(this_dir, '..')

result_text = """Chiste número: 1 (malo)
Pregunta: Papapapaco. ¿Eres tartamudo?.
Respuesta: Yo no, mi padre. Y el del Registro Civil, un mamoncete

Chiste número: 2 (malisimo)
Pregunta: Mamá, ¿por que te casaste con papá?
Respuesta: Ahhhh... ¡tú tampoco te lo explicas!

Chiste número: 3 (malillo)
Pregunta: ¿En que se parece un elefante a una cama?
Respuesta: En que el elefante es un paquidermo y la cama es 'pakiduermas'

Chiste número: 4 (malo)
Pregunta: ¿Sabes cómo se dice "metro" en alemán?
Respuesta: Subanestrujenbajen

"""


class TestChistes(unittest.TestCase):

    def test_class(self):
        stdout = StringIO()
        parser = make_parser()
        cHandler = chistes2.ChistesHandler()
        parser.setContentHandler(cHandler)
        with contextlib.redirect_stdout(stdout):
            parser.parse(open(os.path.join(parent_dir, 'chistes.xml')))
        output = stdout.getvalue()
        self.assertEqual(output, result_text)

    def test_main(self):
        stdout = StringIO()
        with contextlib.redirect_stdout(stdout):
            os.chdir(parent_dir)
            chistes2.main()
        output = stdout.getvalue()
        self.assertEqual(output, result_text)

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
