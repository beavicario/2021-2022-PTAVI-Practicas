from bitstring import BitArray
import socket
import random

_bps_dict = {'0001': 32000, '0010': 40000, '0011': 48000, '0100':56000,
            '0101': 64000, '0110': 80000, '0111': 96000, '1000': 112000,
            '1001': 128000, '1010': 160000, '1011': 192000, '1100': 224000,
            '1101': 256000, '1110': 320000}

_bps_dict_2 = {'0001': 8000, '0010': 16000, '0011': 24000, '0100': 32000,
            '0101': 40000, '0110': 48000, '0111': 56000, '1000': 64000,
            '1001': 80000, '1010': 96000, '1011': 112000, '1100': 128000,
            '1101': 144000, '1110': 160000}

_sample_rate_dict = {'00': 44100, '01': 48000, '10': 32000}

_sample_rate_dict_25 = {'00': 11025, '01': 12000, '10': 8000}

_sample_rate_dict_2 = {'00': 22050, '01': 24000, '10': 16000}

def send_rtp_packet(header, payload, ip, port, packets_in_payload = 1, number = 0):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.connect((ip, port))
        if (number == 0):
            number = 100000000
        for i in range(number):
            packet = BitArray()
            packet.append(header.version)
            packet.append(header.pad_flag)
            packet.append(header.ext_flag)
            packet.append(header.cc)
            packet.append(header.marker)
            packet.append(header.payload_type)
            packet.append(BitArray(uint = header.seq_number, length = 16))
            packet.append(BitArray(uint = header.timestamp, length = 32))
            packet.append(header.ssrc)
            packet.append(header.csrc)
            if header.ext_flag.bin == '1':
                print('NotYetImplemented: Here the extension would come')
#            print('Size of RTP header: ' + str(len(packet.bin)))

            for j in range(packets_in_payload):
                if not payload._take_mp3_frame():
                    return
                packet.append(BitArray(bin = payload.frame))
#                print(payload.frame[0:32])
            packetBytes = packet.tobytes()
            try:
                my_socket.send(packetBytes)
                header.next(payload.frameTimeMs)
            except ConnectionRefusedError:
                print("Warning: Connection refused. Probably there is nothing listening on the other end.")


class RtpPayloadMp3:  # En principio para MP3

    def __init__(self, file_path):
        with open(file_path, "rb") as file:
            bytes = file.read()
            self.bits = BitArray(bytes).bin
            self.header_index = self.bits.find('11111111111')

    def _take_mp3_frame(self):

        header = self.bits[self.header_index:self.header_index+32]
        if not header:
            return None
        frame_sync = header[0:11]
        version = header[11:13]
        layer = header[13:15]
        protection = header[15]
        bitrate = header[16:20]
        sampling = header[20:22]
        padding = header[22]
        private = header[23]
        channel = header[24:26]
        modeext = header[26:28]
        copyright = header[28]
        original = header[29]
        emphasis = header[30:]

        # Se asume que es version 1 layer 3 (mp3)
        if version == '11':
            bps = _bps_dict[bitrate]
            sample_rate = _sample_rate_dict[sampling]
        elif version == '00':
            bps = _bps_dict_2[bitrate]
            sample_rate = _sample_rate_dict_25[sampling]
        elif version == '10':
            bps = _bps_dict_2[bitrate]
            sample_rate = _sample_rate_dict_2[sampling]
        else:
            print("version", version)

        # 144 * bit rate / sample rate * 8 (el 144 es en bytes)
        frame_length = int(144 * 8 * (bps/sample_rate))
        # tiempo por frame en milisegundos
        self.frameTimeMs = int(144/sample_rate * 1000 * 8)
        next_mp3_header_index = self.header_index + frame_length
        self.frame = self.bits[self.header_index:next_mp3_header_index]
        self.header_index = next_mp3_header_index
        return 1

class RtpHeader:

    def __init__(self, version=2, pad_flag=0, ext_flag=0, cc=0, marker=0, payload_type=14, ssrc=1000):
        self.seq_number = random.randint(1, 10000)  # Aleatorio
        self.timestamp = random.randint(1, 10000)  # Aleatorio
        self.set_header(version, pad_flag, ext_flag, cc, marker, payload_type, ssrc)

    def set_header(self, version=2, pad_flag=0, ext_flag=0, cc=0, marker=0, payload_type=14, ssrc=1000):
        self.version = BitArray(uint = version, length = 2)
        self.pad_flag = BitArray(uint = pad_flag, length = 1)
        self.ext_flag = BitArray(uint = ext_flag, length = 1)
        self.cc = BitArray(uint = cc, length = 4)
        self.marker = BitArray(uint = marker, length = 1)
        self.payload_type = BitArray(uint = payload_type, length = 7)
        self.ssrc = BitArray(uint = ssrc, length = 32)
        self.csrc = BitArray()

    def setVersion(self, version):
        self.version = BitArray(uint = version, length = 2)

    def setPaddingFlag(self, pad_flag):
        self.pad_flag = BitArray(uint = pad_flag, length = 1)

    def setExtensionFlag(self, ext_flag):
        self.ext_flag = BitArray(uint = ext_flag, length = 1)

    def setCsrcCount(self, cc):
        self.cc = BitArray(uint = cc, length = 4)

    def setMarker(self, marker):
        self.marker = BitArray(uint = marker, length = 1)

    def setPayloadType(self, payload_type):
        self.payload_type = BitArray(uint = marker, length = 7)

    def setSSRC(self, ssrc):
        self.ssrc = BitArray(uint = ssrc, length = 32)

    def setSequenceNumber(self, seq_number):
        self.seq_number = seq_number

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def setCSRC(self, csrcValues):
        for i in range(len(csrcValues)):
            self.csrc.append(BitArray(uint = csrcValues[i], length = 32))

    def next(self, frameTimeMs):
        self.seq_number += 1
        # Calculate next timestamp
        self.timestamp += int(8000 * (frameTimeMs/1000))


if __name__ == "__main__":
    print("NotImplemented. To be used as a library")
