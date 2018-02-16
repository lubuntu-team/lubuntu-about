#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Copyright 2018 Lubuntu Developers <lubuntu-devel@lists.ubuntu.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
