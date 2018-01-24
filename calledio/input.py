from calledio.constants import DATA_DIR, MSGLEN
from threading import Thread
import socket
import json


'''
Listens for incoming messages and apppends them to their channel file.
'''


class Input(Thread):

    def __init__(self):
        pass

    def append(self, channel, text):
        channel_file = DATA_DIR + '/{}.txt'.format(channel)

        with open(channel_file, 'a') as _file:
            _file.write(text)
        _file.close()

    def start(self, ip, port, channel):
        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        s.connect((ip, port))

        s.send(json.dumps({
            'channel': channel,
            'msg': 'hello!'
        }))

        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = s.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)

        _data = chunks.join('')
        # data = json.loads(_data)

        self.append(_data)
