#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Programa cliente UDP que abre un socket a un servidor mediante terminal.
"""

import socket
import socketserver
import sys
import threading
import time


def write_log(message):
    date = time.strftime('%Y%d%m%H%M%S')
    with open('client.txt', 'a') as log_file:
        log_file.write(date + ' ' + message + '\n')


class RTPHandler(socketserver.BaseRequestHandler):
    """Clase para manejar los paquetes RTP que nos lleguen.

    Atención: Heredamos de BaseRequestHandler porque UDPRequestHandler
    siempre termina enviando una respuesta al cliente, algo que aquí no
    queremos hacer. Al usar BaseRequestHandler no podemos usar self.rfile
    (porque esta clase no lo tiene), así que leemos el mensaje directamente
    de self.request (que es una lista, cuyo primer elemento es el mensaje
    recibido)"""

    def handle(self):
        msg = self.request[0]
        # sólo nos interesa lo que hay a partir del byte 54 del paquete UDP
        # que es donde está la payload del paquete RTP qeu va dentro de él
        payload = msg[12:]
        # Escribimos esta payload en el fichero de salida
        self.output.write(payload)
        print("Received")

    @classmethod
    def open_output(cls, filename):
        """Abrir el fichero donde se va a escribir lo recibido.

        Lo abrimos en modo escritura (w) y binario (b)
        Es un método de la clase para que podamos invocarlo sobre la clase
        antes de empezar a recibir paquetes."""

        cls.output = open(filename, 'wb')

    @classmethod
    def close_output(cls):
        """Cerrar el fichero donde se va a escribir lo recibido.

        Es un método de la clase para que podamos invocarlo sobre la clase
        después de terminar de recibir paquetes."""
        cls.output.close()


class SipClient:

    def __init__(self, server_address, address_src, address_dst, file_name):
        self.server_address = server_address
        self.address_src = address_src
        self.address_dst = address_dst
        self.file_name = file_name
        self.sdp_body = self.get_sdp()

    def get_sdp(self):
        return {
            'v': 0,
            'o': self.address_src + ' 127.0.0.1',
            's': self.address_dst.split(':')[1].split('@')[0],
            't': 0,
            'm': 'audio 34543 RTP'
        }

    def send_register(self, expired=0):
        line = 'REGISTER ' + self.address_src + ' SIP/2.0\r\n'
        if expired != 0:
            line += 'Expired: ' + str(expired) + '\r\n\r\n'
        else:
            line += '\r\n'
        return self.send(line)

    def send_invite(self):
        line = 'INVITE ' + self.address_dst + ' SIP/2.0\r\n'
        line += 'Content-Type: application/sdp\r\n'
        sdp_body = 'v=' + str(self.sdp_body['v']) + '\r\n' + 'o=' + self.sdp_body['o'] + '\r\n' + 's=' + self.sdp_body[
            's'] \
                   + '\r\n' + 't=' + str(self.sdp_body['t']) + '\r\n' + 'm=' + self.sdp_body['m'] + '\r\n\r\n'
        line += 'Content-Length: ' + str(sys.getsizeof(sdp_body)) + '\r\n\r\n' + sdp_body
        return self.send(line)

    def send_ack(self):
        line = 'ACK ' + self.address_dst + ' SIP/2.0\r\n\r\n'
        return self.send(line)

    def send_bye(self):
        line = 'BYE ' + self.address_dst + ' SIP/2.0\r\n\r\n'
        return self.send(line)

    def send(self, line):
        # Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
        ip = self.server_address[0]
        port = self.server_address[1]
        write_log('SIP to ' + ip + ':' + str(port) + ': ' + line.replace('\r\n', ' '))
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
                my_socket.connect((ip, port))
                print(line)
                my_socket.send(line.encode('utf-8'))
                data = my_socket.recv(1024).decode('utf-8')
                if data:
                    write_log('SIP from ' + ip + ':' + str(port) + ': ' + data.replace('\r\n', ' '))
        except ConnectionRefusedError:
            print("Connection refused")
            return ''
        return data


def main():
    # Creamos la instrucción del terminal.
    usage_error = 'python3 client.py <IPServidorSIP>:<puertoServidorSIP> <dirCliente> <dirServidorRTP> <tiempo> <fichero>'

    if len(sys.argv) != 6:
        sys.exit(usage_error)

    ip = sys.argv[1].split(':')[0]
    try:
        port = int(sys.argv[1].split(':')[1])
    except ValueError:
        sys.exit('Not valid port')

    address_src = sys.argv[2]
    address_dst = sys.argv[3]

    try:
        expires = int(sys.argv[4])
    except ValueError:
        sys.exit('Not valid expires time')

    file_name = sys.argv[5]

    client = SipClient((ip, port), address_src, address_dst, file_name)

    response = client.send_register(expires)

    if '200 OK' in response:
        response = client.send_invite()
    else:
        return

    if '200 OK' in response:
        response = client.send_ack()
    else:
        return

    write_log('RTP ready 34543')

    # Abrimos un fichero para escribir los datos que se reciban
    RTPHandler.open_output('output.mp3')
    with socketserver.UDPServer(('', 34543), RTPHandler) as serv:
        print("Listening...")
        # El bucle de recepción (serv_forever) va en un hilo aparte,
        # para que se continue ejecutando este programa principal,
        # y podamos interrumpir ese bucle más adelante
        threading.Thread(target=serv.serve_forever).start()
        # Paramos un rato. Igualmente podríamos esperar a recibir BYE,
        # por ejemplo
        time.sleep(expires)
        print("Time passed, shutting down receiver loop.")
        # Paramos el bucle de recepción, con lo que terminará el thread,
        # y dejamos de recibir paquetes
        serv.shutdown()
    # Cerramos el fichero donde estamos escribiendo los datos recibidos
    RTPHandler.close_output()

    response = client.send_bye()


if __name__ == "__main__":
    main()
