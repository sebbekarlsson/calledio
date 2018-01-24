from calledio.storage import Storage
from calledio.constants import PORT_DEFAULT


def run():
    storage = Storage('localhost', PORT_DEFAULT)

    storage.start()
