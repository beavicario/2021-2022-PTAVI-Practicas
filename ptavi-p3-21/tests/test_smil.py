#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import unittest

from xml.sax import make_parser, parseString
import smil

from tests.common import karaoke_xml, karaoke_tags, smil_xml, smil_tags, \
    parent_dir


class TestSmil(unittest.TestCase):

    def test_file(self):
        parser = make_parser()
        smil_handler = smil.SMILHandler()
        parser.setContentHandler(smil_handler)
        parser.parse(open(os.path.join(parent_dir, 'karaoke.smil')))
        result = smil_handler.get_tags()
        self.assertEqual(result, karaoke_tags)

    def test_string(self):
        smil_handler = smil.SMILHandler()
        parseString(karaoke_xml, smil_handler)
        result = smil_handler.get_tags()
        self.assertEqual(result, karaoke_tags)

    def test_string2(self):
        smil_handler = smil.SMILHandler()
        parseString(smil_xml, smil_handler)
        result = smil_handler.get_tags()
        self.assertEqual(result, smil_tags)


if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True, exit=False)
