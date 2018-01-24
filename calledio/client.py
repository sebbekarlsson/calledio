from calledio.input import Input


def run_client():
    input = Input()
    input.start('localhost', 5565, 'programming')


run_client()
