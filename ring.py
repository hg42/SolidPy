
from solidpy import *

#def Ring(h, ra, ri):
#  return Cylinder(h, ra) - Cylinder(h+Dh, ri).move(0,0,-Do)

def Ring(h, ra1, ri1=None, ra2=None, ri2=None):
  if ra2 is None:
    ra2 = ra1
  if ri1 is None:
    ri1 = ra1
  if ri2 is None:
    ri2 = ri1
  return Cylinder(h, ra1, ra2) - Cylinder(h+Dh, ri1, ri2).move(0,0,-Do)
