from calledio.storage import Storage
from calledio.config import config
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--channel', help='What channel to chat in')
parser.add_argument('--username', help='Your username')
args = parser.parse_args()


def run():
    channel = args.channel if args.channel else 'general'
    username = args.username if args.username else 'anonymous'

    try:
        storage = Storage(
            'localhost',
            config['port'],
            channel=channel,
            username=username
        )
        storage.setDaemon(True)
        storage.start()

        while True:
            storage.join(1)

    except KeyboardInterrupt:
        storage.killed = True
        storage.socket.close()

        return True
