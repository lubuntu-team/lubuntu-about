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

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from aboutlubuntu_auto import Ui_MainWindow

class LubuntuAbout(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    about = QApplication(sys.argv)
    aboutwindow = LubuntuAbout()
    aboutwindow.show()
    sys.exit(about.exec_())
