#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP que abre un socket a un servidor.
"""

import socket

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = 'localhost'
PORT = 6001
HELLO = 'Hola'
BYE = 'Adiós'


def main():
    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
            my_socket.connect((SERVER, PORT))
            print(f"Enviando a {SERVER}:{PORT}:", HELLO)
            my_socket.send(HELLO.encode('utf-8') + b'\r\n')
            data = my_socket.recv(1024)
            print('Recibido: ', data.decode('utf-8'))
            print(f"Enviando a {SERVER}:{PORT}:", BYE)
            my_socket.send(BYE.encode('utf-8') + b'\r\n')
            data = my_socket.recv(1024)
            print('Recibido: ', data.decode('utf-8'))
        print("Cliente terminado.")
    except ConnectionRefusedError:
        print("Error conectando a servidor")


if __name__ == "__main__":
    main()
