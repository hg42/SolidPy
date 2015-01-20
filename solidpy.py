
"""
  TODO:

    HG:

      Surface     surface(file = "surface.dat", center = true, convexity = 5);
                  surface(file = "example010.dat", center = true, convexity = 5);
                  surface(file = "smiley.png", center = true, invert = true);
      Echo?

    $t

    $vpr shows rotation
    $vpt shows translation (i.e. won't be affected by rotate and zoom)
    $vpd shows the camera distance [Note: Requires version 2014.QX(see [1])]
        update at rendering time (e.g. animation but not interactive)

    version() and version_num()
    parent_module(n) and $parent_modules

    showDiff: call renderOSC with special parameter?
              only use transform and negative objects
"""


from __future__ import print_function

import os
import glob
import subprocess
import re
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath('../../../lib'))
sys.path.insert(0, os.path.abspath('../../..'))
sys.path.insert(0, os.path.abspath('../../lib'))
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../lib'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('lib'))
sys.path.insert(0, os.path.abspath('.'))
print(sys.path)

import copy

def show(what):
  try:
    print("---", what, " "*max(0, 20-len(what)) + "=", eval(what, script_globals, script_locals))
  except:
    print("---", what, " "*max(0, 20-len(what)) + "=", eval(what))

def iround(x):
  return int(round(x))

def frange(start, stop = None, step = 1.0):
  """frange generates a set of floating point values over the
  range [start, stop) with step size step

  frange([start,] stop [, step ])"""

  if stop is None:
    start, stop = 0.0, start

  n = iround((stop-start)/step)+1

  # create a generator expression for the index values
  indices = (i for i in range(0, n))
  # yield results
  for i in indices:
    yield start + step*i

def inches(x):
  """converts inches to mm"""
  return 25.4 * x

def OSC_boolStr(abool):
  """retuns a lower case string of 'true' or 'false'"""
  if abool: #OSCad needs lower case
    return "true"
  else:
    return "false"

class Defaults(object):

  tab = "  "
  includeFiles = []
  fs = None
  fn = None
  fa = None
  autoColor = False
  showDiff = False
  diffColor = ["yellow", 0.25]
  colors = ["blue", "green", "orange", "yellow", "SpringGreen",
            "purple", "DarkOrchid",   "MistyRose"]
##resistor color codes good for troubleshooting...?
##    colors=["black","brown","red","orange","yellow","green",
##            "blue","purple","grey","white"]

  colorCnt = 0

def tab(level):
  return level * Defaults.tab

def PrintConfig(name = None, value = None):
  if name is None:
    for f in glob.glob("config-*.ini"):
      os.remove(f)
  else:
    open("-".join(["config", str(name), str(value)]) + ".ini", "w").close()

def Use(name):
  #print(dir(sys.modules['solidpy'])); exit()
  if name.endswith(".solid.py"):
    with open(name) as f:
      code = compile(f.read(), name, 'exec')
      exec(code, script_globals) #, script_locals)
  elif name.endswith(".scad"):
    Defaults.includeFiles.append(name)
  else:
    import imp
    try:
      fname = imp.find_module(name)[1]
    except:
      try:
        fname = imp.find_module(name + ".solid")[1]
      except:
        fname = imp.find_module(name + "/" + name + ".solid")[1]
    if fname is None:
      code = "from " + name + " import *"
      exec(code, script_globals) #, script_locals)
    else:
      with open(fname) as f:
        code = compile(f.read(), fname, 'exec')
        exec(code, script_globals) #, script_locals)

class SolidPyObj(object):

  def __init__(self):
      self.children = []
      self.name = None

  def clone(self):
      return copy.deepcopy(self)

  def __repr__(self):
      if self.name:
          return "<" + self.name + ">"
      return object.__repr__(self)

  def find(self, obj):
      print("find", obj, "in", self)
      if self is obj:
        print("found " + repr(obj))
        return True
      for o in self.children:
          if o.find(obj):
              return True
      return False

  def add(self, obj):
      #if obj == self: obj = obj.clone()
      #print("add", obj, "to", self)
      #if self.find(obj):
      #    obj = obj.clone()
      #obj.release()

      if isinstance(obj, (list, tuple)):
          obj = Union(obj)

      self.children.append(obj)

  def autoColor(self):
      if Defaults.autoColor:
          Defaults.colorCnt += 1
          self = self.color(Defaults.colors[Defaults.colorCnt % len(Defaults.colors)], 0.75)
      return self

  #ToDo add __str__ to Solid object model

  def __add__(self, obj):
          """a=x+y (union)"""
          if isinstance(obj, (list, tuple)):
              obj = Union(obj)
          #if isinstance(self, Union):
          #    self.add(obj)
          #    return self
          #if isinstance(obj, Union):            # commutative
          #    obj.add(self)
          #    return obj
          newUnion = Union(self, obj)
          return newUnion

  def __sub__(self, obj):
          """a=x-y (difference)"""
          #if isinstance(self, Difference):
          #    self.add(obj)
          #    return self
          newDifference = Difference(self, obj)
          return newDifference

  def __mul__(self, obj):
          """a=x*y (intersection)"""
          #if isinstance(self, Intersection):
          #    self.add(obj)
          #    return self
          #if isinstance(obj, Intersection):     # commutative
          #    obj.add(self)
          #    return obj
          newIntersection = Intersection(self, obj)
          return newIntersection

  # universal convenience unary operator ~

  def __invert__(self):
    # ~~~~ = Disable
    if isinstance(self, Root):       return Disable(self.children[0])
    # ~~~  = Root
    if isinstance(self, Background): return Root(self.children[0])
    # ~~   = Background
    if isinstance(self, Debug):      return Background(self.children[0])
    # ~    = Debug
    return Debug(self)

  def scale(self, x, y = None, z = None):
      return Scale(self, x, y, z)

  def resize(self, x, y = None, z = None, auto = None):
      return Resize(self, x, y, z, auto)

  def translate(self, x, y = None, z = None):
      return Translate(self, x, y, z)

  def rotate(self, x, y = None, z = None, v = None):
      return Rotate(self, x, y, z)

  move = translate    # alias

  def mirror(self, x, y = None, z = None):
      return Mirror(self, x, y, z)

  def multmatrix(self, m):
      return MultMatrix(self, m)

  matrix = multmatrix

  def render(self, convexity = None):
      return Render(self, convexity)

  def color(self, color = None, alpha = None):
      return Color(self, color, alpha)

  def comment(self, text = None):
      if text:
          return Comment(self, text)
      return self

  def offset(self, obj, delta, join = None, limit = None):
      return Offset(self, obj, delta, join, limit)

  def OSCString(self, protoStr):
      """Returns the OpenSCAD string to make the object"""
      return protoStr


################################################################################ transforms

class Transform(SolidPyObj):

  def __init__(self, obj):
      SolidPyObj.__init__(self)
      self.add(obj)

  def renderOSC(self, level, protoStr):
      if protoStr:
          protoStr += " "
      else:
          protoStr = ""
      for child in self.children:
          protoStr += child.renderOSC(level)
      return self.OSCString(protoStr)


# transforms using vectors

class TransformVec(Transform):

  def __init__(self, obj, x, y=None, z=None):
      Transform.__init__(self, obj)
      if isinstance(x, list):
          self.vec = x
      else:
          if  y == None or z == None:
              self.vec = [x, x, x]
          else:
              self.vec = [x, y, z]

class Scale(TransformVec):

  def __init__(self, obj, x, y=None, z=None):
      TransformVec.__init__(self, obj, x, y, z)

  def renderOSC(self, level):

      x, y, z = self.vec
      rStr = "scale([%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z)
      return Transform.renderOSC(self, level, rStr)

class Resize(TransformVec):

  def __init__(self, obj, x, y=None, z=None, auto=None):
      TransformVec.__init__(self, obj, x, y, z)
      self.auto = auto

  def renderOSC(self, level):

      x, y, z = self.vec
      if self.auto:
        if isinstance(self.auto, list):
          ax, ay, az = self.auto
        else:
          ax = self.auto
          ay = self.auto
          az = self.auto
        rStr = "resize([%.2f,%.2f,%.2f], auto=[%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z, 1.0 * ax, 1.0 * ay, 1.0 * az)
      else:
        rStr = "resize([%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z)
      return Transform.renderOSC(self, level, rStr)

class Translate(TransformVec):

  def __init__(self, obj, x, y=None, z=None):
      TransformVec.__init__(self, obj, x, y, z)

  def renderOSC(self, level):

      x, y, z = self.vec
      rStr = "translate([%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z)
      return Transform.renderOSC(self, level, rStr)

class Rotate(TransformVec):

  def __init__(self, obj, x, y=None, z=None, v=None):
      TransformVec.__init__(self, obj, x, y, z)
      self.v = v

  def renderOSC(self, level):
      if self.v:
          vx, vy, vz = self.v
          rStr = "rotate(a=[%.2f,%.2f,%.2f], v=[%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z, 1.0 * vx, 1.0 * vy, 1.0 * vz)
      else:
          rStr = "rotate(%s)" % str(self.vec)
      return Transform.renderOSC(self, level, rStr)

class Mirror(TransformVec):

  def __init__(self, obj, x, y=None, z=None):
      TransformVec.__init__(self, obj, x, y, z)

  def renderOSC(self, level):

      x, y, z = self.vec
      rStr = "mirror([%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z)
      return Transform.renderOSC(self, level, rStr)

class MultMatrix(Transform):

  def __init__(self, obj, m):
      Transform.__init__(self, obj)
      self.m = m

  def renderOSC(self, level):
      rStr = "multmatrix(%s)" % str(m)
      return Transform.renderOSC(self, level, rStr)

Matrix = MultMatrix

# other transforms

class Render(Transform):

  def __init__(self, obj, convexity=None):
      Transform.__init__(self, obj)
      self.convexity = convexity

  def renderOSC(self, level):

      rStr  = 'render('
      if self.convexity:
          rStr += 'convexity=' + self.convexity
      rStr += ')'

      return Transform.renderOSC(self, level, rStr)

class Color(Transform):

  def __init__(self, obj, color=None, alpha=None):
      Transform.__init__(self, obj)
      self.color = color
      self.alpha = alpha

  def renderOSC(self, level):

      if self.color:
        if isinstance(self.color, list) and not self.alpha:
            if isinstance(self.color[0], str):
                self.color, self.alpha = self.color
        if isinstance(self.color, list):
            if self.alpha:
                self.color[3] = self.alpha
            rStr = 'color(%s)' % (str(self.color))
        elif isinstance(self.color, str):
            if self.alpha:
                rStr = 'color("%s", %s)' % (self.color, str(self.alpha))
            else:
                rStr = 'color("%s")' % (self.color)
        else:
            rStr = 'color(########## should be string or list but is <' + str(self.color) + '> ##########)'
      else:
        rStr = None

      return Transform.renderOSC(self, level, rStr)

class Comment(Transform):

  def __init__(self, obj, text=None):
      Transform.__init__(self, obj)
      self.text = text

  def renderOSC(self, level):

      if self.text:
          return Transform.renderOSC(self, level, None) + " // " + self.text
      return Transform.renderOSC(self, level, None)

# flag transforms: background %, debug #, disable *, root !

class Debug(Transform):

  def __init__(self, obj):
      Transform.__init__(self, obj)

  def renderOSC(self, level):
      return Transform.renderOSC(self, level, "#")

class Background(Transform):

  def __init__(self, obj):
      Transform.__init__(self, obj)

  def renderOSC(self, level):
      return Transform.renderOSC(self, level, "%")

class Root(Transform):

  def __init__(self, obj):
      Transform.__init__(self, obj)

  def renderOSC(self, level):
      return Transform.renderOSC(self, level, "!")

class Disable(Transform):

  def __init__(self, obj):
      Transform.__init__(self, obj)

  def renderOSC(self, level):
      return Transform.renderOSC(self, level, "*")

################################################################################ 3D

class Cube(SolidPyObj):
  """
  Cube( [x,y,z],center=True) or Cube( x,y,z,center)
  size = n -> [n,n,n]
  center: If True, object is centered at (0,0,0)
  """
  def __init__(self, x, y = None, z = None, center = None):
      SolidPyObj.__init__(self)
      if isinstance(x, list):
          self.size = x
      else:
          if y == None:
              self.size = [x, x, x]
          else:
              self.size = [x, y, z]
      self.center = center

  def renderOSC(self, level):
      protoStr = "cube(size=%s, center=%s);" % (self.size, OSC_boolStr(self.center))
      return self.OSCString(protoStr)

class Sphere(SolidPyObj):
  """
  r=radius
  fa = Angle in degrees
  fs= Angle in mm
  """
  def __init__(self, r, fa = None, fs = None, fn = None):
      SolidPyObj.__init__(self)
      self.r = r
      self.fa = Defaults.fa
      self.fa = fa
      self.fs = fs
      self.fn = fn

  def renderOSC(self, level):
      protoStr = "sphere(r=%s" % str(self.r)
      if self.fa:
          protoStr += ", $fa=%s" % str(self.fa)
      if self.fs:
          protoStr += ", $fs=%s" % str(self.fs)
      if self.fn:
          protoStr += ", $fn=%s" % str(self.fn)
      protoStr += ");"
      return self.OSCString(protoStr)

class Cylinder(SolidPyObj):
  def __init__(self, h, r, r2 = None, fa = None, fs = None, fn = None, center = None):
      """
      h= height, r=radius note if r2 == None->r2=r
      fa = Angle in degrees
      fs= Angle in mm
      center: If True, object is centered at (0,0,0)
      """
      SolidPyObj.__init__(self)
      self.r = r
      self.h = h
      self.r2 = r2
      self.fa = fa
      self.fs = fs
      self.fn = fn
      self.center = center

  def renderOSC(self, level):
      if not self.r2:
          protoStr = "cylinder(h=%s, r=%s" % (str(self.h), str(self.r))
      else:
          protoStr = "cylinder(h=%s, r1=%s, r2=%s" % (str(self.h), str(self.r), str(self.r2))

      if self.fa:
          protoStr += ", $fa=%s" % str(self.fa)
      if self.fs:
          protoStr += ", $fs=%s" % str(self.fs)
      if self.fn:
          protoStr += ", $fn=%s" % str(self.fn)
      if self.center:
          protoStr += ", center=%s" % OSC_boolStr(self.center)
      protoStr += ");"
      return self.OSCString(protoStr)

class Polyhedron(SolidPyObj):
  def __init__(self, points, triangles):
      SolidPyObj.__init__(self)
      self.points = points
      self.triangles = triangles

  def renderOSC(self, level):
      protoStr = ""
      protoStr += "polyhedron(points=%s, triangles=%s);" % (str(self.points), str(self.triangles))
      return self.OSCString(protoStr)

class Linear_extrude(SolidPyObj):
  def __init__(self, obj, height, center = None, convexity = None, twist = None):
      SolidPyObj.__init__(self)
      self.obj = obj
      self.height = height
      self.center = center
      self.convexity = convexity
      self.twist = twist

  def renderOSC(self, level):
      protoStr = "linear_extrude(height=%s" % self.height
      if self.center:
          protoStr += ", center=%s" % OSC_boolStr(self.center)
      if self.convexity:
          protoStr += ", convexity=%s" % self.convexity
      if self.twist:
          protoStr += ", twist=%s" % self.twist
      protoStr += ") "
      protoStr += self.obj.renderOSC(level)
      return self.OSCString(protoStr)


class Rotate_extrude(SolidPyObj):
  def __init__(self, obj, convexity = None, fn = None):
      SolidPyObj.__init__(self)
      self.obj = obj
      self.convexity = convexity
      self.fn = fn

  def renderOSC(self, level):
      protoStr = "rotate_extrude("
      if self.convexity:
          protoStr += " convexity=%s" % self.convexity
      if self.fn:
          protoStr += ", fn=%s" % self.fn
      protoStr += ") "
      protoStr += self.obj.renderOSC(level)
      return self.OSCString(protoStr)

################################################################################ Other

##projection(cut = true)
class Projection(SolidPyObj):
  def __init__(self, obj, cut):

      SolidPyObj.__init__(self)
      self.obj = obj
      self.cut = cut

  def renderOSC(self, level):
      protoStr = "projection(cut=%s)" % (self.cut and "true" or "false")
      protoStr += self.obj.renderOSC(level)
      return self.OSCString(protoStr)

class Import(SolidPyObj):
  def __init__(self, filename):
      SolidPyObj.__init__(self)
      self.filename = filename

  def renderOSC(self, level):
      protoStr = ""
      protoStr += 'import("%s");' % self.filename
      return self.OSCString(protoStr)


################################################################################ 2D

class Circle(SolidPyObj):
  def __init__(self, r, fn = None):
      SolidPyObj.__init__(self)
      self.fn = fn
      self.r = r

  def renderOSC(self, level):
      protoStr = "" + tab(level)
      protoStr += "circle(r=%s" % self.r
      if self.fn:
          protoStr += ", $fn=%s" % self.fn
      protoStr += ");"
      return self.OSCString(protoStr)

class Square(SolidPyObj):
  def __init__(self, x , y = None, center = None):
      SolidPyObj.__init__(self)
      if isinstance(x, list):
          self.size = x
      else:
          if y == None:
              self.size = [x, x, x]
          else:
              self.size = [x, y]
      self.center = center

  def renderOSC(self, level):
      protoStr = ""
      protoStr += "square(%s" % self.size
      if self.center:
          protoStr += ", center=%s" % OSC_boolStr(self.center)
      protoStr += ");"
      return self.OSCString(protoStr)

class Polygon(SolidPyObj):
  def __init__(self, points, paths = None, convexity = None):
      SolidPyObj.__init__(self)
      self.points = points
      self.paths = paths
      self.convexity = convexity

  def renderOSC(self, level):
      protoStr = ""
      protoStr += "polygon(points=%s" % self.points
      if self.paths:
          protoStr += ", paths=%s" % self.paths
      if self.convexity:
          protoStr += ", convexity=%s" % self.convexity
      protoStr += ");"
      return self.OSCString(protoStr)

################################################################################ 2D ops

class Offset(SolidPyObj):
  def __init__(self, obj, delta, join = None, limit = None):
      SolidPyObj.__init__(self)
      self.obj   = obj
      self.delta = delta
      self.join  = join
      self.limit = limit

  def renderOSC(self, level):
      protoStr = "offset("
      protoStr += "delta=%s" % self.delta
      if self.join:
          protoStr += ', join_type="%s"' % self.join
          if self.limit and join=="miter":
              protoStr += ', miter_limit="%s"' % self.limit
      protoStr += ") "
      protoStr += self.obj.renderOSC(level)
      return self.OSCString(protoStr)


class Import_dxf(SolidPyObj):
  def __init__(self, filename, layer = None, origin = None, scale = None):
      SolidPyObj.__init__(self)
      self.filename = filename
      self.layer = layer
      self.origin = origin
      self.scale = scale

  def renderOSC(self, level):
      protoStr = ""
      protoStr += 'import_dxf(file="%s"' % self.filename
      if self.layer:
          protoStr += ", layername=%s" % self.layer
      if self.origin:
          protoStr += ", origin=%s" % self.origin
      if self.scale:
          protoStr += ", scale=%s" % self.scale
      protoStr += ");"
      return self.OSCString(protoStr)

##dxf_linear_extrude(file="finn.dxf", height=3, convexity=1, center=true);
class DXF_linear_extrude(SolidPyObj):
  def __init__(self, filename, height, convexity = None, center = None):
      SolidPyObj.__init__(self)
      self.filename = filename
      self.height = height
      self.convexity = convexity
      self.center = center

  def renderOSC(self, level):
      protoStr = ""
      protoStr += 'dxf_linear_extrude(file="%s"' % self.filename
      if self.height:
          protoStr += ", height=%s" % self.height
      if self.convexity:
          protoStr += ", convexity=%s" % self.convexity
      if self.center:
          protoStr += ", center=%s" % OSC_boolStr(self.center)
      protoStr += ");"
      return self.OSCString(protoStr)


################################################################################ 3D ops

class CGS(SolidPyObj):
  """Generic class that other CGS classes inherit from. Will accept
  lists or individual solid objects."""
  def __init__(self, *args):
      SolidPyObj.__init__(self)
      for obj in args:
        if isinstance(obj, (list, tuple)):
            for item in obj:
                self.add(item)
        elif obj:
            self.add(obj)

  def renderOSC(self, level, protoStr, single_is_identity=True):
      if len(self.children) <= 0:
          return None
      if not single_is_identity or len(self.children) > 1:
          childrenStr = ""
          for child in self.children:
              childStr = child.renderOSC(level+1)
              if childStr:
                  childrenStr += tab(level+1) + childStr + "\n"

          return self.OSCString(
                    protoStr + "\n"
                    + tab(level+1) + "{\n"
                    + childrenStr
                    + tab(level+1) + "}"
                    )
      else:
          return self.children[0].renderOSC(level)

class Union(CGS):
  def __init__(self, *args):
      CGS.__init__(self, *args)

  def renderOSC(self, level):
      return CGS.renderOSC(self, level, "union()")

class Difference(CGS):
  def __init__(self, *args):
      CGS.__init__(self, *args)

  def renderOSC(self, level):
      return CGS.renderOSC(self, level, "difference()")

class Intersection(CGS):
  def __init__(self, *args):
      CGS.__init__(self, *args)

  def renderOSC(self, level):
      return CGS.renderOSC(self, level, "intersection()")

class Minkowski(CGS):
  def __init__(self, *args):
      CGS.__init__(self, *args)

  def renderOSC(self, level):
      return CGS.renderOSC(self, level, "minkowski()")

class Hull(CGS):
  def __init__(self, *args):
      CGS.__init__(self, *args)

  def renderOSC(self, level):
      return CGS.renderOSC(self, level, "hull()", False)

################################################################################ IO

class Module(SolidPyObj):
  def __init__(self, name, **kwargs):
      SolidPyObj.__init__(self)
      self.name = name
      self.kwargs = kwargs

  def renderOSC(self, level):
      protoStr = "" + tab(level)
      protoStr += self.name + "("
      cnt = 0
      for kws in self.kwargs:
          if cnt > 0:
              protoStr += ", \n" + tab(level+1)
          protoStr += "%s=%s" % (kws, self.kwargs[kws])
          cnt += 1
      protoStr += ");"
      return self.OSCString(protoStr)

def writeSCADfile(fileName, *args):
  """fileName = the output file to save to. Include the extension
  args can be SolidPyObj or lists of SolidPyObj"""

  theStr = ""

  for f in Defaults.includeFiles:
      theStr += "use<%s>;\n\n" % f
  if Defaults.fa:
      theStr += '$fa=%s;\n' % Defaults.fa
  if Defaults.fn:
      theStr += '$fn=%s;\n' % Defaults.fn
  if Defaults.fs:
      theStr += '$fs=%s;\n' % Defaults.fs

  theStr += '\n'

  for obj in args:
      if isinstance(obj, (list, tuple)): # a collection of SolidPyObj
          for item in obj:
              theStr += item.renderOSC(0) + "\n"
      else: # it must be a SolidPyObj here
          theStr += obj.renderOSC(0) + "\n"

  outF = open(fileName, 'w')
  outF.write(theStr)
  outF.close

  if 0:
      iline = 0
      for line in theStr.splitlines():
          iline += 1
          print("%4d: %s" % (iline, line))



# modules

import inspect
#for i in range(-3, len(inspect.stack())):
#  print(i, inspect.stack()[i])
script_globals = inspect.stack()[-1][0].f_globals
script_locals  = inspect.stack()[-1][0].f_locals

from math import *
Use("math")

# defaults

Defaults.fn = 0
Defaults.fa = 5
Defaults.fs = 1

# constants

Do = 0.05
Dh = 2*Do

sqrt2           = sqrt(2)




def align(x, step = 0):
  sign = 1 if x >= 0 else -1
  x *= sign
  if step >= 0:
    return sign*int(x/step+0.5)*step
  else:
    step = -step
    return sign*int(x/step+0.5)*step

if 0:
  show("sin(1.5)")
  show("align(5.5,  5)")
  show("align(5.9,  5)")
  show("align(5.5, -5)")
  show("align(8,   -5)")
  show("align(-8,  -5)")
  exit()


def assemble(assembly, format = "openscad", file = None, show = None):

  if file is None:
    file = inspect.stack()[1][1]

  if format == "openscad":
    output_file = re.sub(r'\.solid\.py$', '.scad', file)

  if output_file == file:
    output_file = re.sub(r'\.py$', '.scad', file)

  if output_file == file:
    print("file has wrong extension, must be .solid.py or .py")
    exit(1)

  print("output to %s" % (output_file))

  if format == "openscad":
    writeSCADfile(output_file, assembly)

  if show is None:
    try:
      if os.environ['SOLIDPY_SHOW']:
        show = True
    except:
      show = False

  if show:
    processes = subprocess.check_output(['ps','ax'])
    #print processes
    #if not 'openscad' in processes:
    if not output_file in str(processes):
      os.setsid()
      process = subprocess.Popen(['openscad', output_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      assert not process.poll()



try:
  from configuration import *
  #Use("configuration")
except Exception as e:
  print("no global configuration, error: {0}".format(e))
  pass


