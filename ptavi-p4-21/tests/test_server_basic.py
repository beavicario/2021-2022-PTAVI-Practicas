#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Tests for server_basic.py

Tests use mocking to avoid launching a real client.
"""

import contextlib
from io import StringIO
import os
import sys
import unittest
from unittest.mock import patch, ANY

from tests.common import parent_dir
import server_basic

message = "Hola pepe"
port = 6001
client = "127.0.0.1"
expected = f"""Server listening in port {port}
{client} {port} {message}
"""


class TestSocket(unittest.TestCase):
    """Test how the server socket works"""

    @patch('server_basic.socketserver.UDPServer')
    def test_creation(self, mock_udpserver):
        """Check that an object of class UDPServer is created"""

        with patch.object(sys, 'argv', ['server_basic.py', '6001']):
            os.chdir(parent_dir)
            server_basic.main()
            mock_udpserver.assert_called_once_with(('', 6001), ANY)

    @patch('server_basic.socketserver.UDPServer')
    @patch('server_basic.socketserver.DatagramRequestHandler.finish')
    def test_reception(self, mock_handler_finish, mock_udpserver):
        """Check the handler object

        The handler object should be created every time a datagram is reseived.
        First, find the name of the class (by checking how UDPServer receives it
        when created), and then create a handler object (simulating the reception
        of a datagram), and check that the right answer is written back (in wfile)."""

        with patch.object(sys, 'argv', ['server_basic.py', str(port)]):
            os.chdir(parent_dir)
            server_basic.main()
        handler_class = mock_udpserver.call_args.args[1]
        handler = handler_class((message.encode(), None), ('client', 'port'), 'server')
        self.assertEqual(f"Message: {message}".encode(), handler.wfile.getvalue())


class TestOutput(unittest.TestCase):
    """Test the output produced by the program in stdout"""

    @patch('server_basic.socketserver.UDPServer')
    @patch('server_basic.socketserver.DatagramRequestHandler.finish')
    def test_reception(self, mock_handler_finish, mock_udpserver):
        """Check the handler object

        Call the handler object (see technique used in TestSocket.test:reception),
        and check if the overall output produced by the program is as expected."""

        with patch.object(sys, 'argv', ['server_basic.py', str(port)]):
            os.chdir(parent_dir)
            stdout = StringIO()
            with contextlib.redirect_stdout(stdout):
                server_basic.main()
                handler_class = mock_udpserver.call_args.args[1]
                handler = handler_class((message.encode(), None), (client, port), 'server')
            output = stdout.getvalue()
            self.assertEqual(f"Message: {message}".encode(), handler.wfile.getvalue())
            self.assertEqual(expected,
                             output)


if __name__ == '__main__':
    unittest.main()
