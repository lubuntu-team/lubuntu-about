#!/usr/bin/python3
# -*- coding: utf-8 -*-

from distutils.core import setup
import glob
import os
from DistUtilsExtra.command import *

setup(name='lubuntu-about',
      version='1.0.0',
      packages=['src'],
      scripts=['src/lubuntu-about'],
      cmdclass = { "build" : build_extra.build_extra }
)
