#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "fen",
    version = "0.1.8",
    author = "Patrick Sabin",
    author_email = "patricksabin@gmx.at",
    url = "http://pypi.python.org/pypi/fen",
    scripts = ["fen.py"],
    py_modules = ["images"],
    description = "Generate chessboard images from fen descriptions",
    install_requires = ["argparse"],
    long_description = """\
Chessboard Image Generator
-------------------------------------
This tool takes a fen string and generates a fen image.

This version requires Python 2.
""",
    classifiers = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 2 - Pre-Alpha"
    ],
)

