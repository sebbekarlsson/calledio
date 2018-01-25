import os
from calledio.constants import MSGLEN
from calledio.config import config
from calledio.storage_receiver import Receiver
from threading import Thread
import socket
import json


STORE_DIR = config['directory']


class Storage(Thread):

    def __init__(
        self,
        host,
        port,
        username='anonymous',
        channel='general',
        daemon=True
    ):
        Thread.__init__(self)

        if not os.path.isdir(STORE_DIR):
            os.mkdir(STORE_DIR)

        self.host = host
        self.port = port
        self.username = username
        self.channel = channel
        self.killed = False
        self.receiver = Receiver(self)

    def append(self, channel, text):
        '''
        appends to local channel log
        '''
        channel_file = os.path.join(
            STORE_DIR,
            channel + '.log'
        )

        with open(channel_file, 'a') as _file:
            _file.write(text + '\n')
        _file.close()

    def run(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        print('Connected to', self.host)

        self.socket.send(json.dumps({
            'channel': self.channel,
            'username': self.username,
            'message': '<join>'
        }))

        incoming = self.socket.recv(MSGLEN)

        try:
            data = json.loads(incoming)
        except ValueError:
            data = {}

        if 'notice' in data:
            if data['notice']:
                self.append(
                    data['channel'],
                    data['message']
                )

        self.receiver.setDaemon(True)
        self.receiver.start()

        while not self.killed:
            z = raw_input("message: ")
            self.socket.send(json.dumps({
                'channel': self.channel,
                'username': self.username,
                'message': z
            }))
