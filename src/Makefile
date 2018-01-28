#!/usr/bin/make -f

all:
	pyuic5 main.ui -o aboutlubuntu_autowidgets.py
	pyrcc5 main.qrc -o aboutlubuntu_autoresources.py
	sed -i "s/main_rc/aboutlubuntu_autoresources/g" aboutlubuntu_autowidgets.py

clean:
	rm -rvf aboutlubuntu_auto*.py __pycache__
