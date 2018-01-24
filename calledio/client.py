from calledio.input import Input
import socket


def run_client():
    input = Input()

    try:
        input.start('localhost', 1000)
    except (socket.error, RuntimeError):
        print('Could not connect')
        quit()


run_client()
