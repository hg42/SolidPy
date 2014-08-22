
from xsolidpy import *
from ring import *

def Tube(ddhs):
  tube = Union()
  r1 = ddhs.pop(0)/2.0
  r2 = ddhs.pop(0)/2.0
  z = 0.0
  dz = 0.0
  while len(ddhs):
    h = ddhs.pop(0)
    r3 = ddhs.pop(0)/2.0
    r4 = ddhs.pop(0)/2.0
    h += dz
    tube += Ring(h, r1, r2, r3, r4).move(0,0,z-dz)
    r1 = r3
    r2 = r4
    z += h
    dz = 0
  return tube
