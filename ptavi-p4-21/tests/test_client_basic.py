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
import client_basic


class TestSocket(unittest.TestCase):
    """Test how the socket used works"""

    @patch('client_basic.socket.socket')
    @patch('client_basic.socket.socket.recv')
    def test_creation(self, mock_recv, mock_socket):
        """Check that a socket is created"""

        with patch.object(sys, 'argv', ['client_basic.py', 'server', '6001', 'Hola']):
            os.chdir(parent_dir)
            client_basic.main()
            mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_DGRAM)

    @patch('client_basic.socket.socket.connect')
    @patch('client_basic.socket.socket.send')
    @patch('client_basic.socket.socket.recv')
    def test_sendrecv(self, mock_recv, mock_send, mock_connect):
        """Check that message is sent, and then something is received"""
        message = 'Hola'
        server = 'server'
        port = 6001
        mock_recv.return_value = f"Message: {message}".encode('utf-8')
        with patch.object(sys, 'argv', ['client_basic.py', server, str(port), message]):
            os.chdir(parent_dir)
            client_basic.main()
            mock_connect.assert_called_once_with((server, port))
            mock_send.assert_called_once_with(message.encode('utf-8'))
            mock_recv.assert_called_once()


class TestOutput(unittest.TestCase):
    """Test the output produced by the program in stdout"""

    @patch('client_basic.socket.socket.connect')
    @patch('client_basic.socket.socket.send')
    @patch('client_basic.socket.socket.recv')
    def test_sendrecv(self, mock_recv, mock_send, mock_connect):
        """Check that message is sent, then received, and properly printed"""

        message = ['Hola', 'y', 'Adiós']
        server = 'server'
        port = 6001
        mock_recv.return_value = f"Message: {' '.join(message)}".encode('utf-8')
        with patch.object(sys, 'argv', ['client_basic.py', server, str(port), *message]):
            os.chdir(parent_dir)
            stdout = StringIO()
            with contextlib.redirect_stdout(stdout):
                client_basic.main()
                output = stdout.getvalue()
            mock_connect.assert_called_once_with((server, port))
            mock_send.assert_called_once_with(' '.join(message).encode('utf-8'))
            mock_recv.assert_called_once()
            self.assertEqual(f"Message: {' '.join(message)}\n", output)


if __name__ == '__main__':
    unittest.main()
