#!/usr/bin/python3

import sys
import os

home = os.environ['HOME']

#print "> solidpy", sys.argv
#print home

sys.path = [
  home + '/3D-print/lib/solidpy',
  ] + sys.path

#print(sys.path)

from solidpy import *

parts = Sphere(r=33)

assemble(parts, show=1)

