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
        self.connections = []

    def broadcast(self, data):
        for connection in self.connections:
            if not connection.socket:
                self.connections.remove(connection)
                continue

            connection.socket.send(data)

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = 'localhost'
        self.socket.bind((host, self.port))

        c = None

        while not self.killed:
            self.socket.listen(5)
            print('Waiting for connections...')

            c, addr = self.socket.accept()
            print('Got connection from', addr)

            connection = Connection(socket=c, mainframe=self)
            connection.setDaemon(True)
            connection.start()
            self.connections.append(connection)

        return True
