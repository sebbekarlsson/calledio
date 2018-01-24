from calledio.mainframe import Mainframe
from calledio.config import config


def run():
    try:
        mainframe = Mainframe(config['port'])
        mainframe.setDaemon(True)
        mainframe.start()

        while True:
            mainframe.join(1)

    except KeyboardInterrupt:
        mainframe.killed = True
        mainframe.socket.close()

        return True
