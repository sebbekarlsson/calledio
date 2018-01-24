from calledio.constants import MSGLEN
from threading import Thread
import json


class Connection(Thread):

    def __init__(self, socket, mainframe):
        Thread.__init__(self)
        self.socket = socket
        self.mainframe = mainframe

    def run(self):
        while True:
            # Halts
            incoming = self.socket.recv(MSGLEN)

            try:
                data = json.loads(incoming)
            except ValueError:
                self.socket.close()
                self.socket = None
                return False

            if data['message'] == '<join>':
                self.socket.send(json.dumps({
                    'channel': data['channel'],
                    'username': data['username'],
                    'message': '- ** {} joined! ** -'
                    .format(data['username']),
                    'notice': True
                }))

                continue

            self.socket.send(json.dumps(data))
