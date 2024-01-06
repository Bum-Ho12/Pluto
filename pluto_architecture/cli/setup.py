
'''setup file '''
from setuptools import setup

setup(
    name = 'pluto',
    version = '0.2',
    package = ['pluto'],
    entry_points = {
        'console_scripts':[
            'pluto=pluto.__main__:cli',
        ],
    },
    install_requires=[
        'click',
        'toml',
    ],
    extras_require = {
        'dev':[
            'pytest',
        ],
    },
)
