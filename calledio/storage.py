import os
from calledio.constants import STORE_DIR
from calledio.constants import MSGLEN
from threading import Thread
import socket


class Storage(Thread):

    def __init__(self, host, port):
        if not os.path.isdir(STORE_DIR):
            os.mkdir(STORE_DIR)

        self.host = host
        self.port = port

    def append(self, channel, text):
        '''
        appends to local channel log
        '''
        pass

    def start(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        print('Connected to', self.host)

        self.run()

    def run(self):
        while True:
            z = raw_input("Enter something for the server: ")
            self.socket.send(z)
            # Halts
            print('[Waiting for response...]')
            print(self.socket.recv(MSGLEN))
