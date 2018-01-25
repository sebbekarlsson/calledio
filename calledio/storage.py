import os
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
        self._append = None

    def append(self, channel, text):
        '''
        appends to local channel log
        '''

        if self._append:
            return self._append(channel, text)

        user_dir = os.path.join(
            STORE_DIR,
            self.username
        )

        if not os.path.isdir(user_dir):
            os.mkdir(user_dir)

        channel_file = os.path.join(
            user_dir,
            channel + '.log'
        )

        with open(channel_file, 'a') as _file:
            _file.write(text + '\n')
        _file.close()

    def send_message(self, msg):
        return self.socket.send(json.dumps({
            'channel': self.channel,
            'username': self.username,
            'message': msg
        }))

    def run(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        print('Connected to', self.host)

        self.receiver.setDaemon(True)
        self.receiver.start()

        self.socket.send(json.dumps({
            'channel': self.channel,
            'username': self.username,
            'message': '<join>'
        }))

        while not self.killed:
            cli_input = raw_input("message: ")
            self.send_message(cli_input)
