#!/usr/bin/env python
# 
# setup.py for pymtp
#

from distutils.core import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = "pymtp",
      version = "0.1.0",
      description = "LibMTP bindings in Python",
      long_description=read('README'),
      author = "Nick Devito",
      author_email = "nick@nick125.com",
      url = "https://pypi.python.org/pypi/pymtp",
      py_modules = ["pymtp"])
