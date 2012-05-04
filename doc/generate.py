#!/usr/bin/env python

from os.path import abspath, dirname, join
from robot.libdoc import libdoc

docdir = dirname(abspath(__file__))
libpath = join(docdir, '..', 'src', 'SeleniumLibrary')
outpath = join(docdir, 'SeleniumLibrary.html')

libdoc(libpath, outpath)

