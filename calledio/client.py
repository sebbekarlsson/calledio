from calledio.storage import Storage
from calledio.config import config
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--channel', help='What channel to chat in')
args = parser.parse_args()


def run():
    channel = args.channel if args.channel else 'general'

    storage = Storage('localhost', config['port'], channel=channel)

    storage.start()
