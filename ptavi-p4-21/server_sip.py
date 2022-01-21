#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa servidor SIP y crea json.
"""

import json
import socketserver
import sys
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    user_dic = {}

    # Definimos estructura de .json y registro.
    def handle(self):
        self.json2registered()
        line = self.rfile.read().decode('utf-8')
        ip = self.client_address[0]
        port = self.client_address[1]

        user_name = line.split()[1].split(':')[1]
        expires = int(line.split('\r\n')[1].split()[1])

        # Eliminamos registro si expires es 0.
        # Dar de baja registro.
        if expires == 0:
            if user_name in self.user_dic:
                del self.user_dic[user_name]
        else:
            self.user_dic[user_name] = {
                'address': ip,
                'expires': time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + expires))
            }

        print(ip, port, line)

        ok = 'SIP/2.0 200 OK\r\n\r\n'
        self.wfile.write(ok.encode('utf-8'))
        self.registered2json()

    # Creamos un .json del registro.
    def registered2json(self):
        with open('registered.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.user_dic, json_file, indent=3)

    # Creamos registro de .json.
    def json2registered(self):
        try:
            with open('registered.json', 'r', encoding='utf-8') as json_file:
                self.user_dic = json.load(json_file)
        except:
            self.user_dic = {}


def main():
    # Creamos la instrucción del terminal.
    if len(sys.argv) < 2:
        sys.exit('Usage: python3 server_sip.py <port> ')

    try:
        port = int(sys.argv[1])
    except ValueError:
        sys.exit('Not valid port')

    # Listens at port PORT (my address)
    # and calls the EchoHandler class to manage the request
    try:
        serv = socketserver.UDPServer(('', port), SIPRegisterHandler)
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
