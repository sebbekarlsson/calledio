from calledio.mainframe_connection import Connection
from calledio.constants import MSGLEN
from threading import Thread
import socket
import json


'''
Handles incoming connections
'''


class Mainframe(Thread):

    def __init__(self):
        pass

    def broadcast(self, channel, msg):
        data_to_send = json.dumps({
            'channel': channel,
            'msg': msg
        })

        print(data_to_send)

        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(data_to_send[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def start(self, port):
        serversocket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        serversocket.bind(('localhost', port))
        serversocket.listen(5)

        while True:
            (clientsocket, address) = serversocket.accept()
            ct = Connection(clientsocket, self)
            ct.run()
