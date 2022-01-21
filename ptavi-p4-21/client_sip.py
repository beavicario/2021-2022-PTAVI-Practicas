#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente SIP que abre un socket a un servidor mediante terminal.
"""

import socket
import sys


def send(ip, port, line):
    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
            my_socket.connect((ip, port))
            print(f"Enviando a {ip}:{port}:", line)
            my_socket.send(line.encode('utf-8') + b'\r\n')
            data = my_socket.recv(1024)
            print('Recibido: ', data.decode('utf-8'))
        print("Cliente terminado.")
    except ConnectionRefusedError:
        print("Error conectando a servidor")


def get_register(user_name, expires):
    # Creamos la instrucción de registro.
    return 'REGISTER sip:' + user_name + ' SIP/2.0\r\nExpires: ' + str(expires) + '\r\n\r\n'


def main():
    # Creamos la instrucción del terminal.
    if len(sys.argv) != 6:
        sys.exit('Usage: python3 client_sip.py <IP> <PORT> <METHOD> <USER> <EXPIRES>')

    ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
        expires = int(sys.argv[5])
    except ValueError:
        sys.exit('Not valid port or expires')

    method = sys.argv[3]
    user = sys.argv[4]

    # Asociamos registro a instrucción terminal.
    if method.lower() == 'register':
        line = get_register(user, expires)

    send(ip, port, line)


if __name__ == "__main__":
    main()
