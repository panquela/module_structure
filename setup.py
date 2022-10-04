# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:54:58 2022

@author: PedroAnquela
"""

from setuptools import setup, find_packages

MAJOR = 1
MINOR = 0
PATCH = 0
COMMIT = 8

# from main import *

__version__ = f'{MAJOR}.{MINOR}.{PATCH}.{COMMIT}'
__author__  = 'Universidad Francisco de Vitoria'
__name__    = 'module_structure'

VERSION = __version__

setup(
    name='module_structure',
    version=VERSION,
    description='Brief description of your package',
    author='Pedro Anquela',
    author_email='pedro.anquela@ufv.es',
    license='MIT',
    python_requires='>=3.9.5',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['resources/*.csv','resources/clusters/*.csv']},
    install_requires=[
        'pandas',
        'numpy',
        'tensorflow-gpu',
        'torch'
        ]
)
