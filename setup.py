#!/usr/bin/env python

import distribute_setup
from distutils.core import setup
distribute_setup.use_setuptools()


setup(name='gitpass',
      version='0.1',
      description="Gitpass is an extension of the Python standard library's " \
      + "getpass, designed for keeping passwords out of your git repository.",
      author='Dustin Smith',
      author_email='dustin@media.mit.edu',
      download_url='https://github.com/dasmith/gitpass/tarball/master',
      url='https://github.com/dasmith/gitpass',
      packages=['gitpass'])


