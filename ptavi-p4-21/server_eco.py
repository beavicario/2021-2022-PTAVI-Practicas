#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):

    def handle(self):
        line = self.rfile.read().decode('utf-8')
        ip = self.client_address[0]
        port = self.client_address[1]
        print(ip, port, line)

        self.wfile.write(line.encode('utf-8'))


def main():
    # Listens at port PORT (my address)
    # and calls the EchoHandler class to manage the request
    if len(sys.argv) < 2:
        sys.exit('Usage: python3 server_eco.py <port> ')

    try:
        port = int(sys.argv[1])
    except ValueError:
        sys.exit('Not valid port')

    try:
        serv = socketserver.UDPServer(('', port), EchoHandler)
        print(f"Server listening in port {port}...")
    except OSError as e:
        sys.exit(f"Error empezando a escuchar: {e.args[1]}.")

    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
        sys.exit(0)


if __name__ == "__main__":
    main()
