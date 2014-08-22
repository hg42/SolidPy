
from xsolidpy import *

def Ring(h, r1, r3, r2=None, r4=None):
  if r2 is None:
    r2 = r1
  if r4 is None:
    r4 = r3
  return Cylinder(h, r1, r2) - Cylinder(h+Dh, r3, r4).move(0,0,-Do)
