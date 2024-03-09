from setuptools import setup

APP = ['Campus Job Finder.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'bs4', 'pync', 'chardet', 'charset_normalizer']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
