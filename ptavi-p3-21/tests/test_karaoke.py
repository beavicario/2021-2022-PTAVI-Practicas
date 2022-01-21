#!/usr/bin/python3
# -*- coding: utf-8 -*-

import contextlib
from io import StringIO
import json
import os
import sys
import unittest
from unittest.mock import patch
from xml.sax import parseString

import smil
import karaoke

from tests.common import karaoke_xml, karaoke_str, karaoke_json, \
    smil_xml, smil_str, smil_json, parent_dir


class TestToString(unittest.TestCase):

    def setUp(self):
        self.smil_handler = smil.SMILHandler()

    def test_tostring(self):
        parseString(karaoke_xml, self.smil_handler)
        tags = self.smil_handler.get_tags()
        result = karaoke.to_string(tags)
        self.assertEqual(result, karaoke_str)

    def test_tostring2(self):
        parseString(smil_xml, self.smil_handler)
        tags = self.smil_handler.get_tags()
        result = karaoke.to_string(tags)
        self.assertEqual(result, smil_str)


class TestToStringOutput(unittest.TestCase):

    def test_output(self):
        stdout = StringIO()
        with patch.object(sys, 'argv', ['karaoke.py', 'karaoke.smil']):
            os.chdir(parent_dir)
            with contextlib.redirect_stdout(stdout):
                karaoke.main()
            output = stdout.getvalue()
            self.assertEqual(output, karaoke_str)


class TestToJSON(unittest.TestCase):

    def setUp(self):
        self.smil_handler = smil.SMILHandler()

    def test_tojson(self):
        parseString(karaoke_xml, self.smil_handler)
        tags = self.smil_handler.get_tags()
        result = karaoke.to_json(tags)
        result_json = json.loads(result)
        self.assertEqual(result_json, karaoke_json)

    def test_tojson2(self):
        parseString(smil_xml, self.smil_handler)
        tags = self.smil_handler.get_tags()
        result = karaoke.to_json(tags)
        result_json = json.loads(result)
        self.assertEqual(result_json, smil_json)


class TestToJSONOutput(unittest.TestCase):

    def test_output(self):
        stdout = StringIO()
        with patch.object(sys, 'argv', ['karaoke.py', '--json', 'karaoke.smil']):
            os.chdir(parent_dir)
            with contextlib.redirect_stdout(stdout):
                karaoke.main()
            output = stdout.getvalue()
            output_json = json.loads(output)
            self.assertEqual(output_json, karaoke_json)


if __name__ == '__main__':
    unittest.main()
