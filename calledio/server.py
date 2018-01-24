from calledio.mainframe import Mainframe
from calledio.config import config


def run():
    mainframe = Mainframe(config['port'])
    mainframe.start()
