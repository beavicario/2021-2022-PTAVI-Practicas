#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys


def send(ip, port, line):
    # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
            my_socket.connect((ip, port))
            my_socket.send(line.encode('utf-8'))
            data = my_socket.recv(1024)
        return data.decode('utf-8')
    except ConnectionRefusedError:
        sys.exit('Connection refused')


def check_response(response, method):
    # Generamos respuestas SIP para los métodos 'invite' y 'bye'.
    if method.lower() == 'invite':
        return '100 Trying' in response and '180 Ring' in response and '200 OK' in response
    elif method.lower() == 'bye':
        return '200 OK' in response
    else:
        return False


def main():
    # Creamos la instrucción del terminal.
    if len(sys.argv) != 3:
        sys.exit('Usage: python3 client.py <method> <receiver>@<IP>:<SIPport>')

    try:
        ip = sys.argv[2].split("@")[1].split(":")[0]
        port = int(sys.argv[2].split("@")[1].split(":")[1])
    except (ValueError, IndexError):
        sys.exit('Usage: python3 client.py <method> <receiver>@<IP>:<SIPport>')

    method = sys.argv[1]
    user_dst = sys.argv[2].split("@")[0]

    # Asociamos registro a instrucción terminal.
    line = ''
    if method.lower() == 'invite':
        line = 'INVITE sip:' + user_dst + '@' + ip + ' SIP/2.0\r\n'
        line += 'Content-Type: application/sdp\r\n'
        sdp_body = 'v=0\r\no=robin@gotham.com 127.0.0.1\r\ns=misesion\r\nt=0\r\nm=audio 34543 RTP'
        line += 'Content-Length: ' + str(sys.getsizeof(sdp_body))
        line += '\r\n\r\n' + sdp_body
    elif method.lower() == 'bye':
        line = 'BYE sip:' + user_dst + '@' + ip + ' SIP/2.0'

    if line:
        response = send(ip, port, line)
        print(response)
    else:
        sys.exit('Usage: python3 client.py <method> <receiver>@<IP>:<SIPport>')

    # Creamos ACK una vez enviadas las respuestas SIP del 'invite'.
    if check_response(response, method) and method.lower() == 'invite':
        send(ip, port, 'ACK sip:' + user_dst + '@' + ip + ' SIP/2.0')


if __name__ == "__main__":
    main()
