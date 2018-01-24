from calledio.constants import MSGLEN
from threading import Thread
import socket


'''
Handles incoming connections from clients
'''


class Mainframe(Thread):

    def __init__(self, port):
        self.port = port
        self.socket = socket.socket()
        host = 'localhost'  # socket.gethostname()
        self.socket.bind((host, port))

    def start(self):
        pass

    def run(self):
        c = None

        while True:
            if c is None:
                # Halts
                print('[Waiting for connection...]')
                c, addr = self.socket.accept()
                print('Got connection from', addr)
            else:
                # Halts
                print('[Waiting for response...]')
                print(c.recv(MSGLEN))
                c.send('Welcome to the server')
