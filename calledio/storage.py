import os
from calledio.constants import MSGLEN
from calledio.config import config
from threading import Thread
import socket
import json


STORE_DIR = config['directory']


class Storage(Thread):

    def __init__(self, host, port, username='anonymous', channel='general'):
        if not os.path.isdir(STORE_DIR):
            os.mkdir(STORE_DIR)

        self.host = host
        self.port = port
        self.username = username
        self.channel = channel

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

    def start(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        print('Connected to', self.host)

        self.socket.send(json.dumps({
            'channel': self.channel,
            'username': self.username,
            'message': '<join>'
        }))

        incoming = self.socket.recv(MSGLEN)
        data = json.loads(incoming)

        if 'notice' in data:
            if data['notice']:
                self.append(
                    data['channel'],
                    data['message']
                )

        self.run()

    def run(self):
        while True:
            z = raw_input("Enter something for the server: ")
            self.socket.send(json.dumps({
                'channel': self.channel,
                'username': self.username,
                'message': z
            }))
            # Halts
            incoming = self.socket.recv(MSGLEN)
            data = json.loads(incoming)

            self.append(
                data['channel'],
                '{}: {}'.format(data['username'], data['message'])
            )
