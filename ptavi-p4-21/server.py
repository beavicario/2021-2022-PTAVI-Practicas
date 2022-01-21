#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa servidor UDP que escucha cliente mediante socket.
"""

import socketserver
import sys

# Constantes. Puerto.
PORT = 6001


class EchoHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        self.wfile.write("Hemos recibido tu petición".encode('utf-8'))
        for line in self.rfile:
            print("El cliente nos envía ", line.decode('utf-8'))


def main():
    # Listens at port PORT (my address)
    # and calls the EchoHandler class to manage the request
    try:
        serv = socketserver.UDPServer(('', PORT), EchoHandler)
        print(f"Lanzando servidor UDP de eco ({PORT})...")
    except OSError as e:
        sys.exit(f"Error empezando a escuchar: {e.args[1]}.")

    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
        sys.exit(0)


if __name__ == "__main__":
    main()
