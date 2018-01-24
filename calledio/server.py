from calledio.mainframe import Mainframe
import socket


def run_server():
    mainframe = Mainframe()

    try:
        mainframe.start(5565)
    except (socket.error, RuntimeError):
        print('Could not start')
        quit()


run_server()
