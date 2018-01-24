from setuptools import setup


setup(
    name='calledio',
    version='1.0',
    install_requires=[
        ''
    ],
    packages=[
        'calledio'
    ],
    entry_points={
        "console_scripts": [
            "calledio-client = calledio.client:run_client",
            "calledio-server = calledio.server:run_server"
        ]
    }
)
