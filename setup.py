#!/usr/bin/env python

from distutils.core import setup
from SMF import __version__

setup(name='python-smf',
      version=__version__,
      description='python-smf: Simple Model File structure and parser for python',
      author='Daniel Bugl',
      author_email='daniel.bugl@touchlay.com',
      maintainer='Daniel Bugl',
      maintainer_email='daniel.bugl@touchlay.com',
      url='http://omnidan.github.io/simple-code-generator',
      packages=['SMF'],
      long_description="Simple Model File structure and parser for python",
      license="BSD",
      platforms=["any"],
     )