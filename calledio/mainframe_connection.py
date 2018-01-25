from calledio.constants import MSGLEN
from threading import Thread
import json


'''
Holds a clients connection
'''


class Connection(Thread):

    def __init__(self, socket, mainframe):
        Thread.__init__(self)
        self.socket = socket
        self.mainframe = mainframe
        self.username = None
        self.channel = None

    def run(self):
        while True:
            incoming = self.socket.recv(MSGLEN)

            try:
                data = json.loads(incoming)
            except ValueError:
                self.socket.close()
                self.socket = None

                if self.channel and self.username:
                    self.mainframe.broadcast(json.dumps({
                        'channel': self.channel,
                        'username': self.username,
                        'message': '<leave>{}</leave>'
                        .format(self.username),
                        'notice': True
                    }))

                return False

            if data['message'] == '<join>':
                self.channel = data['channel']
                self.username = data['username']

                self.socket.send(json.dumps({
                    'channel': self.channel,
                    'username': self.username,
                    'message': '<join>{}</join>'
                    .format(self.username),
                    'notice': True
                }))

                continue

            self.socket.send(json.dumps(data))
