
# Name, Gewinde,  d,  di,  Mutter d flach, torx index

from solidpy import *

M_std = {
  "M2":  { 'g': 0.40,  'd':  2.0, 'di':  1.6, 'md':  5.0, 'ti': "T8" },
  "M3":  { 'g': 0.50,  'd':  3.0, 'di':  2.5, 'md':  6.0, 'ti': "T15"},
  "M4":  { 'g': 0.70,  'd':  4.0, 'di':  3.3, 'md':  7.0, 'ti': "T25"},
  "M5":  { 'g': 0.80,  'd':  5.0, 'di':  4.2, 'md':  8.0, 'ti': "T30"},
  "M6":  { 'g': 1.00,  'd':  6.0, 'di':  5.0, 'md': 10.0, 'ti': "T40"},
  "M7":  { 'g': 1.00,  'd':  7.0, 'di':  6.0, 'md': 12.0, 'ti': "T45"},
  "M8":  { 'g': 1.25,  'd':  8.0, 'di':  6.8, 'md': 13.0, 'ti': "T50"},
  "M10": { 'g': 1.50,  'd': 10.0, 'di':  8.5, 'md': 17.0, 'ti': "T55"},
  "M12": { 'g': 1.75,  'd': 12.0, 'di': 10.2, 'md': 22.0, 'ti': "T60"},
  "M14": { 'g': 2.00,  'd': 14.0, 'di': 12.0, 'md': 27.0, 'ti': "T70"},
  }

def DIN_get_(s, what):
  try:
    return s[what]
  except:
    d, di, md = s['d'], s['di'], s['md']
    if what == 'dm': return md * 9/8
    if what == 'dk': return (md + (md * 9/8))/2
    if what == 'hk': return d
    if what == 'hm': return d*4/5

def DIN_get(standard, what):
  return DIN_get_(M_std[standard], what)

def DIN_Schraube(standard, hg, hk = None):
  s = M_std[standard]
  d  = DIN_get_(s, 'd')
  dk = DIN_get_(s, 'dk')
  if hk is None:
    hk = DIN_get_(s, 'hk')
  return (Cylinder(h = hk, r = dk/2) + Cylinder(h = hg+hk+Do, r = d/2)).move(0, 0, -hk-Do)

def DIN_Mutter(standard, hm = None, space = 0):
  s = M_std[standard]
  dm = DIN_get_(s, 'dm')
  if hm is None:
    hm = DIN_get_(s, 'hm')
  return Cylinder(h = hm, r = dm/2 + space, fn = 6).rotate(0, 0, 30)

def DIN_KopfLoch(standard, hk = None, space = 0):
  s = M_std[standard]
  dk = DIN_get_(s, 'dk')
  if hk is None:
    hk = DIN_get_(s, 'hk')
  return Cylinder(h = hk, r = dk/2 + space).move(0, 0, -hk)

def DIN_FreiesLoch(standard, hg, space = 0):
  s = M_std[standard]
  d = DIN_get_(s, 'd')
  return Cylinder(h = hg, r = d/2 + space)

def DIN_GewindeLoch(standard, hg, space = 0):
  s = M_std[standard]
  di = DIN_get_(s, 'di')
  return Cylinder(h = hg, r = di/2 + space)

DIN_Screw       = DIN_Schraube
DIN_Nut         = DIN_Mutter
DIN_ThreadHole  = DIN_GewindeLoch
DIN_FreeHole    = DIN_FreiesLoch
DIN_HeadHole    = DIN_KopfLoch
