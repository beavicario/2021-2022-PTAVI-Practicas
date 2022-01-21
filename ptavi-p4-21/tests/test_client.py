#!/usr/bin/python3
# -*- coding: utf-8 -*-

import contextlib
from io import StringIO
import os
import socket
import sys
import unittest
from unittest.mock import patch, MagicMock, ANY

from tests.common import parent_dir
import client


class TestSocket(unittest.TestCase):
    """Test how the socket used works"""

    @patch('client.socket.socket')
    @patch('client.socket.socket.recv')
    def test_creation(self, mock_recv, mock_socket):
        """Check that a socket is created"""

        with patch.object(sys, 'argv', ['client.py', '127.0.0.1', '6001',
                                        'register', 'luke@polismassa.com', '3600']):
            os.chdir(parent_dir)
            client.main()
            mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_DGRAM)

    @patch('client.socket.socket.connect')
    @patch('client.socket.socket.send')
    @patch('client.socket.socket.recv')
    def test_sendrecv(self, mock_recv, mock_send, mock_connect):
        """Check that message is sent, and then something is received"""
        server = 'server'
        port = 6001
        address = 'luke@polismassa.com'
        expiration = 3600
        message = f"REGISTER sip:{address} SIP/2.0\r\n" \
                  + f"Expires: {expiration}\r\n\r\n"
        mock_recv.return_value = b"Message"
        with patch.object(sys, 'argv', ['client.py', server, str(port),
                                        'register', f"{address}", str(expiration)]):
            os.chdir(parent_dir)
            client.main()
            mock_connect.assert_called_once_with((server, port))
            mock_send.assert_called_once_with(message.encode('utf-8'))
            mock_recv.assert_called_once()


class TestOutput(unittest.TestCase):
    """Test the output produced by the program in stdout"""

    @patch('client.socket.socket.connect')
    @patch('client.socket.socket.send')
    @patch('client.socket.socket.recv')
    def test_sendrecv(self, mock_recv, mock_send, mock_connect):
        """Check that message is sent, then received, and properly printed"""

        server = 'server'
        port = 6001
        address = 'luke@polismassa.com'
        expiration = 3600
        message = f"REGISTER sip:{address} SIP/2.0\r\n" \
                  + f"Expires: {expiration}\r\n\r\n"
        response = "SIP/2.0 200 OK\r\n\r\n"
        mock_recv.return_value = response.encode()
        with patch.object(sys, 'argv', ['client.py', server, str(port),
                                        'register', f"{address}", str(expiration)]):
            os.chdir(parent_dir)
            stdout = StringIO()
            with contextlib.redirect_stdout(stdout):
                client.main()
                output = stdout.getvalue()
            mock_connect.assert_called_once_with((server, port))
            mock_send.assert_called_once_with(message.encode('utf-8'))
            mock_recv.assert_called_once()
            self.assertEqual(response + '\n', output)


if __name__ == '__main__':
    unittest.main()
