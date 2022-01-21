#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP mediante terminal.
"""

import os
import random
import socketserver
import sys
import simplertp


def get_audio_file():
    return sys.argv[3]


class EchoHandler(socketserver.DatagramRequestHandler):
    dic = {}

    # Definimos parámetros del cliente.
    def handle(self):
        audio_file = get_audio_file()
        line = self.rfile.read().decode('utf-8')
        ip = self.client_address[0]
        port = self.client_address[1]
        method = line.split()[0]
        print(line)

        # Estructura para los métodos contemplados.
        # Declaramos los códigos de respuesta que puede enviar el Servidor.
        if method == 'INVITE':
            user_src = line.split('\r\n')[5].split('=')[1].split()[0]
            user_dst = line.split()[1].split(':')[1].split('@')[0]
            ip_src = line.split('\r\n')[5].split()[1]
            port_rtp = line.split('\r\n')[8].split()[1]
            try:
                self.dic[user_dst] = {'ip': ip_src, 'port': int(port_rtp)}
                response = 'SIP/2.0 100 Trying\r\n\r\nSIP/2.0 180 Ring\r\n\r\nSIP/2.0 200 OK\r\n\r\n'
                response += f'v=0\r\no={user_dst}@{user_src.split("@")[1]} 127.0.0.1\r\ns=misesion\r\nt=0\r\nm=audio 67876 RTP'
            except:
                response = 'SIP/2.0 400 Bad Request'
        elif method == 'ACK':
            user_dst = line.split()[1].split(':')[1].split('@')[0]
            if user_dst in self.dic:
                RTP_header = simplertp.RtpHeader()
                RTP_header.set_header(pad_flag=0, ext_flag=0, cc=0, ssrc=random.randint(1, 10))
                audio = simplertp.RtpPayloadMp3(audio_file)
                simplertp.send_rtp_packet(RTP_header, audio, self.dic[user_dst]['ip'], self.dic[user_dst]['port'])
            response = ''
        elif method == 'BYE':
            response = 'SIP/2.0 200 OK'
        else:
            if method.lower() in ['invite', 'ack', 'bye']:
                response = 'SIP/2.0 400 Bad Request'
            else:
                response = 'SIP/2.0 405 Method Not Allowed'

        if response:
            self.wfile.write(response.encode('utf-8'))
            # self.wfile.write('SIP/2.0 200 OK\r\n'.encode('utf-8'))


def main():
    # Creamos la instrucción del terminal.
    if len(sys.argv) < 4:
        sys.exit('Usage: python3 server.py <IP> <port> <audio_file>')

    try:
        ip = sys.argv[1]
        port = int(sys.argv[2])
    except (ValueError, IndexError):
        sys.exit('Usage: python3 server.py <IP> <port> <audio_file>')

    audio_file = sys.argv[3]

    if not os.path.exists(audio_file):
        sys.exit('Usage: python3 server.py <IP> <port> <audio_file>')

    # Listens at port PORT (my address)
    # and calls the EchoHandler class to manage the request
    try:
        serv = socketserver.UDPServer((ip, port), EchoHandler)
        print("Listening...")
    except OSError as e:
        sys.exit(f"Error starting server: {e.args[1]}.")

    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Server finish")
        sys.exit(0)


if __name__ == "__main__":
    main()
