#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''

def _requires_from_file(filename):
    return open(filename).read().splitlines()

# version
here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'python_movie_transformer',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.dev1')

setup(
    name="python_movie_transformer",
    version=version,
    url='https://github.com/Fufuhu/python_movie_transcoder',
    author='e238058r',
    author_email='e238058r@hotmail.co.jp',
    maintainer='e238058r',
    maintainer_email='e238058r@hotmail.co.jp',
    description='Movie file filtering package wrapping ffmpy',
    long_description=readme,
    packages=find_packages(),
    install_requires=[
        "ffmpy",
    ],
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points="""
    """,
)