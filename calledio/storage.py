import os
from calledio.constants import STORE_DIR


class Storage(object):

    def __init__(self):
        if not os.path.isdir(STORE_DIR):
            os.mkdir(STORE_DIR)

    def append(self, channel, text):
        '''
        appends to local channel log
        '''
        pass
