import copy

def inches(x):
    """converts inches to mm"""
    return 25.4 * x

def boolStr(abool):
    """retuns a lower case string of 'true' or 'false'"""
    if abool: #OSCad needs lower case
        return "true"
    else:
        return "false"

class Defaults(object):
    tab = " " * 4
    includeFiles = []
    fs = None
    fn = None
    fa = None
    autoColor = False
    augment = False
    diffColor = ["red", 0.25] #for augmentation of difference(){}
    colors = ["blue", "green", "orange", "yellow", "SpringGreen",
            "purple", "DarkOrchid", "MistyRose"]
##resistor color codes good for troubleshooting...?
##    colors=["black","brown","red","orange","yellow","green",
##            "blue","purple","grey","white"]

    colorCnt = 0
    augList = []

def Use(fileName):
    Defaults.includeFiles.append(fileName)


class SolidPyObj(object):

    def __init__(self):
        self._transformStack = []
        self.root = False
        self.disable = False
        self.parent = None
        self.background = False
        self.debug = False
        self.comment = ""
        if Defaults.autoColor:
            self.color(Defaults.colors[Defaults.colorCnt % len(Defaults.colors)])
            Defaults.colorCnt += 1

#ToDo add __str__ to Solid object model

    def __add__(self, solidObj1):
            """a=x+y (union)"""
            self      = self.copy()
            solidObj1 = solidObj1.copy()

            if isinstance(self, Union):
                self.add(solidObj1)
                return self
            #if isinstance(solidObj1, Union):
            #    solidObj1.add(self)
            #    return solidObj1
            newUnion = Union(self, solidObj1)
            return newUnion

    def __sub__(self, solidObj1):
            """a=x-y (difference)"""
            self      = self.copy()
            solidObj1 = solidObj1.copy()

            if isinstance(self, Difference):
                self.add(solidObj1)
                return self
            newDifference = Difference(self, solidObj1)
            return newDifference

    def __mul__(self, solidObj1):
            """a=x*y (intersection)"""
            self      = self.copy()
            solidObj1 = solidObj1.copy()

            if isinstance(self, Intersection):
                self.add(solidObj1)
                return self
            if isinstance(solidObj1, Intersection):
                solidObj1.add(self)
                return solidObj1
            newIntersection = Intersection(self, solidObj1)
            return newIntersection

    # some convenience unary operators (- = disable, + = background, ~ = debug)

    def __neg__(self):
      self = self.copy()
      self.disable = True
      return self

    def __pos__(self):
      self = self.copy()
      self.background = True
      return self

    def __invert__(self):
      self = self.copy()
      self.debug = True
      return self

    def copy(self):
        X = copy.deepcopy(self)

        if Defaults.autoColor == True:
            X.color(Defaults.colors[Defaults.colorCnt % len(Defaults.colors)])
            Defaults.colorCnt += 1
        return X

    def getTabLvl(self):
        here = self
        lvl = 0
        while here.parent != None:
          lvl += 1
          here = here.parent
        return lvl

    def rotate(self, x, y = None, z = None, v = None):
        """Puts a rotate transform on the transform stack"""
        self = self.copy()

        rStr = ""
        if type(x) == list:
            loc = x
        else:
            if y == None or z == None:
                loc = [x, x, x]
            else:
                loc = [x, y, z]
            x, y, z = loc

        if v:
            q, r, s = v
            rStr = "rotate(a = [%.2f,%.2f,%.2f], v = [%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z, 1.0 * q, 1.0 * r, 1.0 * s)
        else:
            rStr = "rotate(%s)" % str(loc)
        self._transformStack.append(rStr)

        return self

    def release(self):

#        if isinstance(self.parent, Difference):
#            #No longer a candidate for augmentation
#            Defaults.augList.remove(self)
#            self.color("yellow", 1)

        if self.parent != None:
            self.parent.children.remove(self)
            self.parent = None

    def scale(self, x, y = None, z = None):
        """Puts a scale transform on the transform stack"""
        self = self.copy()

        if type(x) == list:
            loc = x
        else:
            if y == None or z == None:
                loc = [x, x, x]
            else:
                loc = [x, y, z]
        x, y, z = loc
        rStr = "scale([%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z)
        self._transformStack.append(rStr)

        return self

    def translate(self, x, y = None, z = None):
        """
        Puts a translate transform on the transform stack
        translate( [x,y,z]) or translate(x,y,z)
        translate (1) -> [1,1,1]
        """
        self = self.copy()

        if type(x) == list:
            loc = x
        else:
            if  y == None or z == None:
                loc = [x, x, x]
            else:
                loc = [x, y, z]

        x, y, z = loc
        rStr = "translate([%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z)
        self._transformStack.append(rStr)

        return self

    move = translate    # alias

    def mirror(self, x, y = None, z = None):
        """Puts a mirror transform on the transform stack
        mirror( [x,y,z]) or mirror(x,y,z)
        mirror (1) -> [1,1,1]
        """
        self = self.copy()

        if type(x) == list:
            loc = x
        else:
            if y == None or z == None:
                loc = [x, x, x]
            else:
                loc = [x, y, z]
        x, y, z = loc
        rStr = "mirror([%.2f,%.2f,%.2f])" % (1.0 * x, 1.0 * y, 1.0 * z)
        self._transformStack.append(rStr)

        return self

    def multmatrix(self, m):
        """Puts a multmatrix transform on the transform stack
        *** not tested ***"""
        self = self.copy()

        rStr = "multmatrix(%s)" % str(m)
        self._transformStack.append(rStr)

        return self

    def color(self, color = "yellow", alpha = 1.0):
        self = self.copy()

        if type(color) == str:
            rStr = 'color("%s", %s)' % (color, str(alpha))

            if len(self._transformStack) > 0:
                if self._transformStack[0].startswith('color'):
                    self._transformStack.pop(0)
                    self._transformStack.insert(0, rStr)
            else:
                self._transformStack.append(rStr)

        if type(color) == list:
            rStr = 'color(%s, %s)' % (str(color), str(alpha))
            self._transformStack.append(rStr)

        return self

    def OSCString(self, protoStr):
        """Returns the OpenSCAD string to make the object"""
        #look for any modifiers
        OSCstr = ""

        for each in self._transformStack:
            OSCstr = each + " " + OSCstr

        modStr = ""
        if self.background:
            modStr += "%"
        if self.debug:
            modStr += "#"
        if self.disable:
            modStr += "*"
        if self.root:
            modStr += "!"
        OSCstr = +self.getTabLvl() * Defaults.tab + modStr + OSCstr

        OSCstr += protoStr

        if self.comment != "":
            OSCstr += " //%s\n" % self.comment
        else:
            OSCstr += "\n"

        return OSCstr


class Cube(SolidPyObj):
    """
    Cube( [x,y,z],center=True) or Cube( x,y,z,center)
    size = 1 -> [1,1,1]
    center: If True, object is centered at (0,0,0)
    """
##    def __init__(self, size = [1,1,1], center = False)
    def __init__(self, x, y = None, z = None, center = None):
        SolidPyObj.__init__(self)
        if type(x) == list:
            self.size = x
        else:
            if y == None:
                self.size = [x, x, x]
            else:
                self.size = [x, y, z]

        self.center = center

    def renderOSC(self):
        protoStr = "cube(size=%s, center=%s);" % (self.size, boolStr(self.center))
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

    def renderOSC(self):
        protoStr = "sphere(r = %s" % str(self.r)
        if self.fa:
            protoStr += ", $fa = %s" % str(self.fa)
        if self.fs:
            protoStr += ", $fs = %s" % str(self.fs)
        if self.fn:
            protoStr += ", $fn = %s" % str(self.fn)
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

    def renderOSC(self):
        if not self.r2:
            protoStr = "cylinder(h=%s, r=%s" % (str(self.h), str(self.r))
        else:
            protoStr = "cylinder(h=%s, r1=%s, r2=%s" % (str(self.h), str(self.r), str(self.r2))

        if self.fa:
            protoStr += ", $fa = %s" % str(self.fa)
        if self.fs:
            protoStr += ", $fs = %s" % str(self.fs)
        if self.fn:
            protoStr += ", $fn = %s" % str(self.fn)
        if self.center:
            protoStr += ", center = %s" % boolStr(self.center)
        protoStr += ");"
        return self.OSCString(protoStr)

class Polyhedron(SolidPyObj):
    def __init__(self, points, triangles):
        SolidPyObj.__init__(self)
        self.points = points
        self.triangles = triangles

    def renderOSC(self):
        protoStr = ""
        protoStr += "polyhedron(points = %s,\n triangles = %s);" % (str(self.points), str(self.triangles))
        return self.OSCString(protoStr)

class Linear_extrude(SolidPyObj):
    def __init__ (self, solidObj, height, center = None, convexity = None, twist = None):
        SolidPyObj.__init__(self)
        self.solidObj = solidObj
        self.height = height
        self.center = center
        self.convexity = convexity
        self.twist = twist

    def renderOSC(self):
        protoStr = "linear_extrude(height=%s" % self.height
        if self.center:
            protoStr += ", center = %s" % boolStr(self.center)
        if self.convexity:
            protoStr += ", convexity = %s" % self.convexity
        if self.twist:
            protoStr += ", twist = %s" % self.twist
        protoStr += ") "
        protoStr += self.solidObj.renderOSC()
        return self.OSCString(protoStr)


class Rotate_extrude(SolidPyObj):
    def __init__ (self, solidObj, convexity = None, fn = None):
        SolidPyObj.__init__(self)
        self.solidObj = solidObj
        self.convexity = convexity
        self.fn = fn


    def renderOSC(self):
        protoStr = "rotate_extrude("
        if self.convexity:
            protoStr += " convexity=%s" % self.convexity
        if self.fn:
            protoStr += ", fn = %s" % self.fn
        protoStr += ") "
        protoStr += self.solidObj.renderOSC()
        return self.OSCString(protoStr)

##projection(cut = true)
class Projection(SolidPyObj):
    def __init__ (self, solidObj, cut):

        SolidPyObj.__init__(self)
        self.solidObj = solidObj
        self.cut = cut

    def renderOSC(self):
        protoStr = "projection(cut=%s)" % self.cut
        protoStr += self.SolidPyObj.renderOSC()
        return self.OSCString(protoStr)

class Import(SolidPyObj):
    def __init__(self, filename):
        SolidPyObj.__init__(self)
        self.filename = filename

    def renderOSC(self):
        protoStr = ""
        protoStr += 'import("%s");' % self.filename
        return self.OSCString(protoStr)


class Circle(SolidPyObj):
    def __init__(self, r, fn = None):
        SolidPyObj.__init__(self)
        self.fn = fn
        self.r = r

    def renderOSC(self):
        protoStr = "" + self.getTabLvl() * Defaults.tab
        protoStr += "circle(r = %s" % self.r
        if self.fn:
            protoStr += ", $fn=%s" % self.fn
        protoStr += ");"
        return self.OSCString(protoStr)

class Square(SolidPyObj):
    def __init__(self, x , y = None, center = None):
        if type(x) == list:
            self.size = x
        else:
            if y == None:
                self.size = [x, x, x]
            else:
                self.size = [x, y]

        SolidPyObj.__init__(self)

        self.center = center

    def renderOSC(self):
        protoStr = ""
        protoStr += "square(%s" % self.size
        if self.center:
            protoStr += ", center = %s" % boolStr(self.center)
        protoStr += ");"
        return self.OSCString(protoStr)

class Polygon(SolidPyObj):
    def __init__(self, points, paths = None, convexity = None):
        SolidPyObj.__init__(self)
        self.points = points
        self.paths = paths
        self.convexity = convexity

    def renderOSC(self):
        protoStr = ""
        protoStr += "polygon(points=%s" % self.points
        if self.paths:
            protoStr += ", paths= %s" % self.paths
        if self.convexity:
            protoStr += ", convexity= %s" % self.convexity
        protoStr += ");"
        return self.OSCString(protoStr)



class Import_dxf(SolidPyObj):
    def __init__(self, filename, layer = None, origin = None, scale = None):
        SolidPyObj.__init__(self)
        self.filename = filename
        self.layer = layer
        self.origin = origin
        self.scale = scale

    def renderOSC(self):
        protoStr = ""
        protoStr += 'import_dxf(file="%s"' % self.filename
        if self.layer:
            protoStr += ", layername = %s" % self.layer
        if self.origin:
            protoStr += ", origin = %s" % self.origin
        if self.scale:
            protoStr += ", scale = %s" % self.scale
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

    def renderOSC(self):
        protoStr = ""
        protoStr += 'dxf_linear_extrude(file="%s"' % self.filename
        if self.height:
            protoStr += ", height=%s" % self.height
        if self.convexity:
            protoStr += ", convexity=%s" % self.convexity
        if self.center:
            protoStr += ", center=%s" % boolStr(self.center)
        protoStr += ");"
        return self.OSCString(protoStr)


## CGS Modeling ##

class CGS(SolidPyObj):
    """Generic class that other CGS classes inherit from. Will accept
    lists or individual solid objects."""
    def __init__(self, *args):
        SolidPyObj.__init__(self)
        self.children = []

        for solidObj1 in args:
          if type(solidObj1) == list:
              for solid in solidObj1:
                  self.add(solid)
          elif solidObj1:
              self.add(solidObj1)

    def add(self, solidObj1):

        solidObj1 = solidObj1.copy()

        solidObj1.release()
        solidObj1.parent = self

#        if isinstance(self, Difference) and len(self.children) > 0:
#            color, alpha = Defaults.diffColor
#            solidObj1.color(color, alpha)
#            Defaults.augList.append(solidObj1)

        self.children.append(solidObj1)

    def renderOSC(self, protoStr):
        childrenStr = ""
        for child in self.children:
            childrenStr += child.renderOSC()
        childrenStr += self.getTabLvl() * Defaults.tab + "}\n"

        return self.OSCString(protoStr + childrenStr)

class Union(CGS):
    def __init__(self, *args):
        CGS.__init__(self, *args)

    def renderOSC(self):
        return CGS.renderOSC(self, "union() {\n")

class Difference(CGS):
    def __init__(self, *args):
        CGS.__init__(self, *args)

    def renderOSC(self):
        return CGS.renderOSC(self, "difference() {\n")

class Intersection(CGS):
    def __init__(self, *args):
        CGS.__init__(self, *args)

    def renderOSC(self):
        return CGS.renderOSC(self, "intersection() {\n")

class Minkowski(CGS):
    def __init__(self, *args):
        CGS.__init__(self, *args)

    def renderOSC(self):
        return CGS.renderOSC(self, "minkowski() {\n")

class Hull(CGS):
    def __init__(self, *args):
        CGS.__init__(self, *args)

    def renderOSC(self):
        return CGS.renderOSC(self, "hull() {\n")

class Module(SolidPyObj):
    def __init__(self, name, **kwargs):
        self.name = name
        self.kwargs = kwargs
        SolidPyObj.__init__(self)

    def renderOSC(self):
        protoStr = "" + self.getTabLvl() * Defaults.tab
        protoStr += self.name + "("
        cnt = 0
        for kws in self.kwargs:
            if cnt > 0:
                protoStr += ", \n" + (1 + self.getTabLvl()) * Defaults.tab
            protoStr += "%s = %s" % (kws, self.kwargs[kws])
            cnt += 1
        protoStr += ");"
        return self.OSCString(protoStr)

def writeSCADfile(fileName, *args):
    """fileName = the SCAD file to save to. Include the '.scad' extension
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
        if type(obj) == list: # A list of SolidPyObj
            for item in obj:
                theStr += item.renderOSC() + "\n"
        else: # it must be a SolidPyObj here
            theStr += obj.renderOSC() + "\n"

    if Defaults.augment:
        for item in Defaults.augList:
            if item.getTabLvl() < 2:
                item.color("red", 0.25)
                item.comment += " (from Augmentation)"
                theStr += item.renderOSC() + "\n"

    outF = open(fileName, 'w')
    outF.write(theStr)
    outF.close



def hull_path(*args):
  args = list(args)
  last = args.pop(0)
  if len(args) == 0:
    return last
  hulls = []
  while len(args) > 0:
    this = args.pop(0)
    hulls.append(Hull(last, this))
    last = this
  return Union(hulls)

def main():

    parts = hull_path(Sphere(1), Sphere(1).move(10,20,0), Sphere(1).move(0,50,20), Sphere(1).move(10,0,20))

    writeSCADfile("/tmp/test.scad", parts)
    print parts.renderOSC()


if __name__ == '__main__':
    main()
