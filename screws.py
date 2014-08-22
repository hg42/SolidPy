
# Name, Gewinde,  d,  di,  Mutter d flach, torx index

from xsolidpy import *

M_std = {
  "M2":  [ 0.40,    2.0,  1.6,  5.0, "T8"],
  "M3":  [ 0.50,    3.0,  2.5,  6.0, "T15"],
  "M4":  [ 0.70,    4.0,  3.3,  7.0, "T25"],
  "M5":  [ 0.80,    5.0,  4.2,  8.0, "T30"],
  "M6":  [ 1.00,    6.0,  5.0, 10.0, "T40"],
  "M7":  [ 1.00,    7.0,  6.0, 12.0, "T45"],
  "M8":  [ 1.25,    8.0,  6.8, 13.0, "T50"],
  "M10": [ 1.50,   10.0,  8.5, 17.0, "T55"],
  "M12": [ 1.75,   12.0, 10.2, 22.0, "T60"],
  "M14": [ 2.00,   14.0, 12.0, 27.0, "T70"],
  }

def DIN_Mutter(standard):
  xxx, d, di, da, xxx = M_std[standard]
  dm = da * 1.125
  dk = (dm+da)/2
  hk = d
  hm = d*0.8
  print "Mutter", "d,di,da", d, di, da, "dm,dk,hk,hm", dm, dk, hk, hm
  return Cylinder(h = hm, r = dm/2, fn = 6).rotate(0, 0, 30)

def DIN_Schraube(standard, hg):
  xxx, d, di, da, xxx = M_std[standard]
  dm = da * 9/8
  dk = (dm+da)/2
  hk = d
  hm = d*4/5
  return Cylinder(h = hk, r = dk/2) + Cylinder(h = hg+hk, r = d/2)

