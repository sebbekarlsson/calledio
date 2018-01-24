from calledio.constants import MSGLEN
from threading import Thread
import json


'''
Represents an incoming connection in the mainframe
'''


class Connection(Thread):

    def __init__(self, socket, mainframe):
        self.socket = socket
        self.mainframe = mainframe

    def run(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.socket.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == '':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            print(chunk)

        _data = chunks.join('')
        print(_data)
        data = json.loads(_data)

        if 'msg' in data and 'channel' in data:
            self.mainframe.broadcast(data['channel'], data['msg'])
