#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Tests for server.py

Tests use mocking to avoid launching a real client.
"""

import contextlib
from io import StringIO
import json
import os
import shutil
import sys
import tempfile
import time
import unittest
from unittest.mock import patch, ANY

from tests.common import parent_dir
import server

handler_class = server.SIPRegisterHandler
port = 6001
client = "127.0.0.1"
address = 'luke@polismassa.com'
expiration = 3600
requests = [
    f"REGISTER sip:{address} SIP/2.0\r\n" \
    + f"Expires: {expiration}\r\n\r\n",
    f"REGISTER sip:{address} SIP/2.0\r\n" \
    + f"Expires: 0\r\n\r\n"
]
response = "SIP/2.0 200 OK\r\n\r\n"
register_time = 1635791004
expiration_string =time.strftime('%Y-%m-%d %H:%M:%S +0000',
                                 time.gmtime(register_time+expiration))
registered = {address: {'client': client, 'expires': expiration_string}}
expected = f"""Server listening in port {port}
"""


class TestSocket(unittest.TestCase):
    """Test how the server socket works"""

    @patch('server.socketserver.UDPServer')
    def test_creation(self, mock_udpserver):
        """Check that an object of class UDPServer is created"""

        with patch.object(sys, 'argv', ['server.py', '6001']):
            os.chdir(parent_dir)
            server.main()
            mock_udpserver.assert_called_once_with(('', 6001), ANY)

    @patch('server.socketserver.UDPServer')
    @patch('server.socketserver.DatagramRequestHandler.finish')
    def test_reception(self, mock_handler_finish, mock_udpserver):
        """Check the handler object

        The handler object should be created every time a datagram is reseived.
        First, find the name of the class (by checking how UDPServer receives it
        when created), and then create a handler object (simulating the reception
        of a datagram), and check that the right answer is written back (in wfile)."""

        with patch.object(sys, 'argv', ['server.py', str(port)]):
            os.chdir(parent_dir)
            server.main()
        handler_class = mock_udpserver.call_args.args[1]
        handler = handler_class((requests[0].encode(), None), (client, port), 'server')
        self.assertEqual(response.encode(), handler.wfile.getvalue())


class TestRegistered(unittest.TestCase):
    """Test the registered dictionary"""

    def setUp(self) -> None:
        self.dir = tempfile.mkdtemp()
        os.chdir(self.dir)

    def tearDown(self) -> None:
        shutil.rmtree(self.dir)

    @patch('server.time.time')
    @patch('server.socketserver.DatagramRequestHandler.finish')
    def test_new(self, mock_finish, mock_time):
        """Check a new address is inserted"""
        mock_time.return_value = register_time
        handler_class((requests[0].encode(), None), (client, port), 'server')
        self.assertEqual(registered, handler_class.registered)

    @patch('server.time.time')
    @patch('server.socketserver.DatagramRequestHandler.finish')
    def test_expired(self, mock_finish, mock_time):
        """Check a new address with 0 expire is not inserted"""
        mock_time.return_value = register_time
        handler_class((requests[1].encode(), None), (client, port), 'server')
        self.assertEqual({}, handler_class.registered)

    @patch('server.time.time')
    @patch('server.socketserver.DatagramRequestHandler.finish')
    def test_new_expired(self, mock_finish, mock_time):
        """Check a new address is inserted, then removed when set to expire"""
        mock_time.return_value = register_time
        handler_class((requests[0].encode(), None), (client, port), 'server')
        self.assertEqual(registered, handler_class.registered)
        handler_class((requests[1].encode(), None), (client, port), 'server')
        self.assertEqual({}, handler_class.registered)

class TestJSON(unittest.TestCase):
    """Test JSON files"""

    def setUp(self) -> None:
        self.dir = tempfile.mkdtemp()
        os.chdir(self.dir)

    def tearDown(self) -> None:
        shutil.rmtree(self.dir)

    @patch('server.time.time')
    @patch('server.socketserver.DatagramRequestHandler.finish')
    def test_new(self, mock_finish, mock_time):
        """Check a new address is inserted in JSON file"""
        mock_time.return_value = register_time
        handler_class((requests[0].encode(), None), (client, port), 'server')
        self.assertEqual(registered, handler_class.registered)
        with open('registered.json', 'r') as file:
            registered_file = json.load(file)
            self.assertEqual(registered, registered_file)

    @patch('server.socketserver.UDPServer')
    def test_loaded(self, mock_udpserver):
        """Check file is loaded into registered"""
        with open('registered.json', 'w') as file:
            json.dump(registered, file, indent=4)
        with patch.object(sys, 'argv', ['server.py', str(port)]):
            server.main()
        self.assertEqual(registered, handler_class.registered)

    @patch('server.socketserver.UDPServer')
    @patch('server.socketserver.DatagramRequestHandler.finish')
    def test_loaded_expire(self, mock_finish, mock_udpserver):
        """Check file is loaded into registered, then address expired and removed"""
        with open('registered.json', 'w') as file:
            json.dump(registered, file, indent=4)
        with patch.object(sys, 'argv', ['server.py', str(port)]):
            server.main()
        self.assertEqual(registered, handler_class.registered)
        handler_class((requests[1].encode(), None), (client, port), 'server')
        self.assertEqual({}, handler_class.registered)
        with open('registered.json', 'r') as file:
            registered_file = json.load(file)
            self.assertEqual({}, registered_file)

class TestOutput(unittest.TestCase):
    """Test the output produced by the program in stdout"""

    def setUp(self) -> None:
        self.dir = tempfile.mkdtemp()
        os.chdir(self.dir)

    def tearDown(self) -> None:
        shutil.rmtree(self.dir)

    @patch('server.socketserver.UDPServer')
    @patch('server.socketserver.DatagramRequestHandler.finish')
    def test_reception(self, mock_handler_finish, mock_udpserver):
        """Check the handler object

        Call the handler object (see technique used in TestSocket.test:reception),
        and check if the overall output produced by the program is as expected."""

        with patch.object(sys, 'argv', ['server.py', str(port)]):
            os.chdir(parent_dir)
            stdout = StringIO()
            with contextlib.redirect_stdout(stdout):
                server.main()
                handler_class = mock_udpserver.call_args.args[1]
                handler = handler_class((requests[0].encode(), None), (client, port), 'server')
            output = stdout.getvalue()
            output = output.splitlines()[0] + '\n'
            self.assertEqual(response.encode(), handler.wfile.getvalue())
            self.assertEqual(expected,
                             output)


if __name__ == '__main__':
    unittest.main()
