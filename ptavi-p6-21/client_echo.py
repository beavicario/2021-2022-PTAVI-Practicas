#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket

# Cliente UDP simple.

# Dirección IP y puerto del servidor.
SERVER = 'localhost'
PORT = 6001


def main():
    # Creamos el socket y lo configuramos
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        # Envía cinco mensajes
        for mesg in ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco']:
            data = f"Hola\r\n{mesg}\r\n"
            print("Enviando:")
            print(data + ".")
            my_socket.sendto(data.encode('utf-8'), (SERVER, PORT))

        # Recibe cinco mensajes
        for count in range(5):
            data = my_socket.recv(2048)
            print("Recibido:")
            print(data.decode('utf-8') + ".")

    print("Terminando programa...")


if __name__ == "__main__":
    main()
