#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP que abre un socket a un servidor mediante terminal.
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


def main():
    # Creamos la instrucción del terminal.
    if len(sys.argv) < 4:
        sys.exit('Usage: python3 client_basic.py <IP> <PORT> <LINE>')

    ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        sys.exit('Not valid port')
    line = ' '.join(sys.argv[3:])
    send(ip, port, line)


if __name__ == "__main__":
    main()
