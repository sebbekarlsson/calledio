from calledio.mainframe_connection import Connection
from threading import Thread
import socket


'''
Handles incoming connections from clients
'''


class Mainframe(Thread):

    def __init__(self, port):
        Thread.__init__(self)
        self.port = port
        self.socket = None
        self.killed = False

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'  # socket.gethostname()
        self.socket.bind((host, self.port))

        c = None

        while not self.killed:
            self.socket.listen(5)
            # Halts
            print('[Waiting for connection...]')
            c, addr = self.socket.accept()
            print('Got connection from', addr)
            connection = Connection(socket=c, mainframe=self)
            connection.setDaemon(True)
            connection.start()
            print('continue')

        return True
