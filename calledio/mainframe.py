from calledio.constants import MSGLEN
from threading import Thread
import socket
import json


'''
Handles incoming connections from clients
'''


class Mainframe(Thread):

    def __init__(self, port):
        self.port = port
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'  # socket.gethostname()
        self.socket.bind((host, self.port))

        self.run()

    def run(self):
        c = None

        while True:
            if c is None:
                self.socket.listen(5)
                # Halts
                print('[Waiting for connection...]')
                c, addr = self.socket.accept()
                print('Got connection from', addr)

                # TODO: create new thread with `c`
            else:
                # Halts
                incoming = c.recv(MSGLEN)

                try:
                    data = json.loads(incoming)
                except ValueError:
                    c.close()
                    c = None
                    continue

                if data['message'] == '<join>':
                    c.send(json.dumps({
                        'channel': data['channel'],
                        'username': data['username'],
                        'message': '- ** {} joined! ** -'
                        .format(data['username']),
                        'notice': True
                    }))

                    continue

                c.send(json.dumps(data))
