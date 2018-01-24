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
            "calledio = calledio.client:run_client"
        ]
    }
)
