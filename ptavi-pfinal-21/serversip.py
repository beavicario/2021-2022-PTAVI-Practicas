#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP mediante terminal.
"""

import socketserver
import socket
import sys
import json
import time

def write_log(message):
    date = time.strftime('%Y%d%m%H%M%S')
    with open('serversip.txt', 'a') as log_file:
        log_file.write(date + ' ' + message + '\n')


class SIPHandler(socketserver.DatagramRequestHandler):

    dicc = {}

    # Definimos parámetros del cliente.
    def handle(self):
        self.json2register()
        line = self.rfile.read().decode('utf-8')
        print(line)
        write_log('SIP from ' + self.client_address[0] + ':' + str(self.client_address[1]) + ': ' + line.replace('\r\n', ' '))

        method = line.split()[0]
        response = 'SIP/2.0 200 OK\r\n\r\n'

        if method in ['REGISTER', 'INVITE', 'ACK', 'BYE']:
            if method.lower() == 'register':
                ip = self.client_address[0]
                port = self.client_address[1]
                user_address = line.split()[1]
                try:
                    user_expired = int(line.split('\r\n')[1].split()[1])
                    date = time.time() + user_expired
                    if user_address not in self.dicc:
                        self.dicc[user_address] = (ip, port, date)
                    else:
                        self.dicc[user_address][2] = date
                    response = 'SIP/2.0 200 OK\r\n\r\n'
                except ValueError:
                    response = 'SIP/2.0 400 Bad Request\r\n\r\n'
            else:
                user_dst = line.split()[1]
                if user_dst in self.dicc:
                    response = self.resend(line, user_dst)
                    if not response:
                        return
                else:
                    response = 'SIP/2.0 404 User Not Found\r\n\r\n'
        else:
            response = 'SIP/2.0 405 Method Not Allowed\r\n\r\n'

        write_log('SIP to ' + self.client_address[0] + ':' + str(self.client_address[1]) + ': ' + response.replace('\r\n', ' '))
        self.wfile.write(response.encode('utf-8'))
        self.client_expired()
        self.register2json()

    def client_expired(self):
        c_expired = []
        now = time.time()
        for client in self.dicc:
            if self.dicc[client][2] <= now:
                c_expired.append(client)

        for client in c_expired:
            del self.dicc[client]

    def register2json(self):
        with open('registered.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.dicc, json_file, indent=3)

    def json2register(self):
        try:
            with open('registered.json', 'r', encoding='utf-8') as json_file:
                self.dicc = json.load(json_file)
        except:
            self.dicc = {}

    def resend(self, line, user_dst):
        ip = self.dicc[user_dst][0]
        port = self.dicc[user_dst][1]
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
                my_socket.connect((ip, port))
                my_socket.send(line.encode('utf-8'))
                write_log('SIP to ' + ip + ':' + str(port) + ': ' + line.replace('\r\n', ' '))
                data = my_socket.recv(1024).decode('utf-8')
                if data:
                    write_log('SIP from ' + ip + ':' + str(port) + ': ' + data.replace('\r\n', ' '))

        except ConnectionRefusedError:
            print("Connection refused")
            return ''
        return data

def main():
    write_log('Starting...')
    # Creamos la instrucción del terminal.
    if len(sys.argv) != 2:
        sys.exit('Usage: python3 serversip.py <port> ')

    try:
        port = int(sys.argv[1])
    except ValueError:
        sys.exit('Not valid port')

    # Listens at port PORT (my address)
    # and calls the EchoHandler class to manage the request
    try:
        serv = socketserver.UDPServer(('', port), SIPHandler)
        print(f"Server listening in port {port}...")
    except OSError as e:
        sys.exit(f"Error start listening: {e.args[1]}.")

    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Server finish")
        sys.exit(0)


if __name__ == "__main__":
    main()