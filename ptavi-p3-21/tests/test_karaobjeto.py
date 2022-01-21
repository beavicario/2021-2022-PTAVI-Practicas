#!/usr/bin/python3
# -*- coding: utf-8 -*-

import contextlib
from io import StringIO
import json
import os
import sys
import unittest
from unittest.mock import patch

import karaobjeto

from tests.common import karaoke_str, karaoke_json, calls_urlretrieve, \
    parent_dir


class TestToStringOutput(unittest.TestCase):
    """Class to test karaobjeto JSON output

    All tests patched with a mocked karaobjeto.urlretrieve to avoid actually
    downloading files when testing (too many downloads)
    """

    @patch.object(karaobjeto, 'urlretrieve')
    def test_output(self, test_patch):
        stdout = StringIO()
        with patch.object(sys, 'argv', ['karaobjeto.py', 'karaoke.smil']):
            os.chdir(parent_dir)
            with contextlib.redirect_stdout(stdout):
                karaobjeto.main()
            output = stdout.getvalue()
            self.assertEqual(output, karaoke_str)


class TestToJSONOutput(unittest.TestCase):
    """Class to test karaobjeto JSON output

    All tests patched with a mocked karaobjeto.urlretrieve to avoid actually
    downloading files when testing (too many downloads)
    """

    @patch.object(karaobjeto, 'urlretrieve')
    def test_output(self, test_patch):
        stdout = StringIO()
        with patch.object(sys, 'argv', ['karaobjeto.py', '--json', 'karaoke.smil']):
            os.chdir(parent_dir)
            with contextlib.redirect_stdout(stdout):
                karaobjeto.main()
            output = stdout.getvalue()
            output_json = json.loads(output)
            self.assertEqual(output_json, karaoke_json)


class TestDownload(unittest.TestCase):

    @patch.object(karaobjeto, 'urlretrieve')
    def test_download(self, test_patch):
        with patch.object(sys, 'argv', ['karaoke.py', 'karaoke.smil']):
            os.chdir(parent_dir)
            test_patch.return_value = True
            karaobjeto.main()
            test_patch.assert_has_calls(calls_urlretrieve)
