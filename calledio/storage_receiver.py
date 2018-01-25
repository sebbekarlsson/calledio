from calledio.constants import MSGLEN
from threading import Thread
import json


'''
Handles incoming messsages
'''


class Receiver(Thread):

    def __init__(self, storage):
        Thread.__init__(self)
        self.storage = storage

    def run(self):
        while True:
            incoming = self.storage.socket.recv(MSGLEN)

            try:
                data = json.loads(incoming)
            except ValueError:
                continue

            self.storage.append(
                data['channel'],
                '{}: {}'.format(data['username'], data['message'])
            )
