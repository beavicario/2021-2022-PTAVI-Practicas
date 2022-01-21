#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from mock import patch

import download

from tests.common import calls_urlretrieve, parent_dir


class TestDownload(unittest.TestCase):

    @patch.object(download, 'urlretrieve')
    def test_download(self, test_patch):
        with patch.object(sys, 'argv', ['karaoke.py', 'karaoke.smil']):
            os.chdir(parent_dir)
            test_patch.return_value = True
            download.main()
            test_patch.assert_has_calls(calls_urlretrieve)


if __name__ == '__main__':
    unittest.main()
