#!/usr/bin/env python

import sys

sys.path.insert(0, 'src')

from setuptools import setup

setup(name='pyptlib',
      version='0.1',
      description='A python implementation of the Pluggable Transports for Circumvention specification for Tor',
      author='Brandon Wiley',
      author_email='brandon@blanu.net',
      url='http://stepthreeprivacy.org/',
      package_dir={'pyptlib': 'src/pyptlib'},
      packages=['pyptlib'],
     )
