#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver

# Puerto
PORT = 6001


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    UDP echo handler class
    """

    def handle(self):
        msg = self.rfile.read()
        client = self.client_address
        print(f"Recibido de {str(client)}:")
        print(f"{msg.decode('utf-8')}.")
        self.wfile.write(msg)


def main():
    # Creamos servidor de eco y escuchamos
    with socketserver.UDPServer(('', PORT), EchoHandler) as serv:
        print("Lanzando servidor UDP de eco...")
        serv.serve_forever()


if __name__ == "__main__":
    main()
