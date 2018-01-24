from calledio.mainframe import Mainframe
from calledio.constants import PORT_DEFAULT


def run():
    mainframe = Mainframe(PORT_DEFAULT)
    mainframe.start()
