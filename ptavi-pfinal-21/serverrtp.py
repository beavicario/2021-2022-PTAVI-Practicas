#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP mediante terminal.
"""

import socketserver
import socket
import sys
import time
import multiprocessing
import  threading
import simplertp

WORKING = True

def write_log(message):
    date = time.strftime('%Y%d%m%H%M%S')
    with open('serverrtp.txt', 'a') as log_file:
        log_file.write(date + ' ' + message + '\n')


class RTPHandler(socketserver.DatagramRequestHandler):

    rtp_data = []
    sender = multiprocessing.Process()

    # Definimos parámetros del cliente.
    def handle(self):
        line = self.rfile.read().decode('utf-8')
        print(line)
        write_log('SIP from ' + self.client_address[0] + ':' + str(self.client_address[1]) + ': ' + line.replace('\r\n', ' '))

        method = line.split()[0]

        if method.lower() == 'invite':
            ip = self.client_address[0]
            port = int(line.split('\r\n')[8].split()[1])
            self.rtp_data.append(ip)
            self.rtp_data.append(port)

        if method.lower() == 'ack':
            self.sender = multiprocessing.Process(target=send_rtp, args=(self.rtp_data[0], self.rtp_data[1], sys.argv[2]))
            self.sender.start()
            write_log('RTP to ' + self.rtp_data[0] + ':' + str(self.rtp_data[1]))
            while len(self.rtp_data) != 0:
                self.rtp_data.pop()
            return

        if method.lower() == 'bye':
            self.sender.close()

        write_log('SIP to ' + self.client_address[0] + ':' + str(self.client_address[1]) + ': SIP/2.0 200 OK')

        self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')

def send_rtp(ip, port, file_name):
    RTP_header = simplertp.RtpHeader()
    RTP_header.set_header(pad_flag=0, ext_flag=0, cc=0)
    audio = simplertp.RtpPayloadMp3(file_name)
    simplertp.send_rtp_packet(RTP_header, audio, ip, port)

def send_register(user_src, ip, port, first=True):
    message = 'REGISTER sip:' + user_src + ' SIP/2.0\r\nExpired: 62\r\n\r\n'
    global WORKING
    for i in range(60000):
        if not WORKING: break
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
                if first:
                    my_socket.bind(('', 6002))
                my_socket.connect((ip, port))
                my_socket.send(message.encode('utf-8'))
                write_log('SIP to 127.0.0.1:6002: ' + message.replace('\r\n', ' '))
                data = my_socket.recv(1024).decode('utf-8')
                write_log('SIP from ' + ip + ':' + str(port) + ': ' + data.replace('\r\n', ' '))
        except ConnectionRefusedError:
            sys.exit("Connection refused")
        if not first:
            time.sleep(30.0)
        else:
            break

def main():
    write_log('Starting...')
    global WORKING
    # Creamos la instrucción del terminal.
    if len(sys.argv) != 3:
        sys.exit('Usage: python3 serverrtp.py <IPServidorSIP>:<puertoServidorSIP> <fichero>')

    ip = sys.argv[1].split(':')[0]

    try:
        port = int(sys.argv[1].split(':')[1])
    except ValueError:
        sys.exit('Not valid port')

    file_name = sys.argv[2]

    user_src = file_name.split('.')[0] + '@singasong.net'

    send_register(user_src, ip, port)
    t = threading.Thread(target=send_register, args=[user_src, ip, port, False])
    t.start()

    # Listens at port PORT (my address)
    # and calls the EchoHandler class to manage the request
    try:
        serv = socketserver.UDPServer(('', 6002), RTPHandler)
        print("Server listening in port 6002...")
    except OSError as e:
        WORKING = False
        sys.exit(f"Error start listening: {e.args[1]}.")

    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Server finish")
        WORKING = False
        sys.exit(0)


if __name__ == "__main__":
    main()