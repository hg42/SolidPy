# SolidPy

## Overview
[OSC]:http://www.openscad.org
[OSCUM]:http://en.wikibooks.org/wiki/OpenSCAD_User_Manual

SolidPy is a python module that allows generates [OpenSCAD][OSC] code from python python code. The aim of developing this  python module is to simplify and enhance the design experience of code-based, parametric, solid modeling. 
### Features
* Simple, flexible syntax
* Treat objects like objects (not text)
* Use existing [OpenSCAD][OSC] modules
* Grow the object tree and pick the fruit you want (instead of taking the whole tree)
* AutoColoring mode
* Reference another solids attributes
* Copy solid objects
* Augmentation of difference() and intersection() **coming soon*

### SolidPy Classes
The SolidPy class was designed for maximum inheritance and flexibility. Below is an explanation of each classes interface. For specific OpenSCAD information see the [OpenSCAD Users Manual][OSCUM].

### 3D Objects
#### Cube
Creates a Cube object. Accepts two forms:

	Cube( [x,y,z],center) or Cube( x,y,z,center)
    	Cube(1) -> Cube(1,1,1)
    	center: If True, object is centered at (0,0,0). True by default.
#### Cylinder
		Cylinder(h,r, r2, fa, fs, fn, center )
        	h= height
        	r=radius note: if r2 == None->r2=rad
        	fa = Angle in degrees. None by default.
        	fs= Angle in mm. None by default.
       	 	center: If True, object is centered at (0,0,0)

#### Sphere
Creates a Sphere object.

    Sphere(r,fa=None,fs=None,fn=None)
    	r=radius
    	fa = Angle in degrees. None by default.
    	fs= Angle in mm, None by default.
    	center: If True, object is centered at (0,0,0). True by default.

#### DXF_linear_extrude 
####Linear Extrude
Uses the same syntax as OpenSCAD.

    Linear_extrude(height,center,convexity,twist)
    
#### Import
#### Import_dxf Linear_extrude
#### Module 
#### Polygon 
#### Polyhedron 
Uses the same syntax as OpenSCAD.

    Polyhedron(points,triangles)
#### Projection 
#### Rotate_extrude

###2D Objects
#### Square

### CGS

###Transforms

###Utility

####copy(SolidPyObj)
Copy creates an exact duplicate of the solid object except the parent of the duplicate is set to `None` and children are duplicates of the original.

     myBox = Cube(4,5,6)
	 myNewBox = myBox.copy()

####use("filename.scad")
This loads an OpenSCAD file in order to access modules within that file. 
####include()
is not implemented.

###Extras
####inches(x)
####autoColor


Everything in OpenSCAD is assumed to be millimeters(mm). inches(X) returns 25.4 * X to 
convert x that is in inches to mm.





`Cube([5,5,5])` can now be `Cube(5,5,5)`

SolidPy
Modules
copy
Classes
__builtin__.object SolidPyObj
CGS
Difference Hull Intersection Minkowski Union
Circle
 CGS(SolidPyObj)
           Generic class that other CGS classes inherit from. Will accept
           lists or individual solid objects.
Method resolution order:
CGS
SolidPyObj __builtin__.object
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Methods defined here:

￼￼__init__(self, solidPyObj1, solidPyObj2) add(self, solidPyObj1)
renderOSC(self, protoStr) set__tabLvl(self, lvl)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼list of weak references to the object (if defined)
￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 2 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Circle(SolidPyObj)
Method resolution order:
Circle SolidPyObj __builtin__.object
Methods defined here: __init__(self, r, fn=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 3 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
          Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Cube(SolidPyObj)
    Cube( [x,y,z],center=True) or Cube( x,y,z,center)
    size = 1 -> [1,1,1]
    center: If True, object is centered at (0,0,0)
Method resolution order:
Cube SolidPyObj
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 4 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼__builtin__.object
￼￼￼￼￼Methods defined here:
__init__(self, x, y=None, z=None, center=False) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj:
__dict__
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼dictionary for instance variables (if defined)
￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 5 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Cylinder(SolidPyObj)
Method resolution order:
Cylinder SolidPyObj __builtin__.object
Methods defined here:
__init__(self, h, rad, r2=None, fa=None, fs=None, fn=None, center=None) h= height, r=radius note if r2 == None->r2=rad
fa = Angle in degrees
fs= Angle in mm
center: If True, object is centered at (0,0,0) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0)
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 6 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
￼￼￼￼￼￼￼￼￼￼￼￼￼￼class DXF_linear_extrude(SolidPyObj)
￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 7 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼￼##dxf_linear_extrude(file="finn.dxf", height=3, convexity=1, center=true);
Method resolution order:
DXF_linear_extrude SolidPyObj __builtin__.object
Methods defined here:
__init__(self, filename, height, convexity=None, center=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 8 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Difference(CGS)
Method resolution order:
Difference
CGS
SolidPyObj __builtin__.object
Methods defined here:
__init__(self, solidPyObj1=None, solidPyObj2=None) renderOSC(self)
Methods inherited from CGS: add(self, solidPyObj1) set__tabLvl(self, lvl)
Methods inherited from SolidPyObj:
OSCString(self, protoStr)
Returns the OpenSCAD string to make the object
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 9 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼__add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a
__mul__(self, solidPyObj1) __sub__(self, solidPyObj1) color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼fn = None
￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 10 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼fs = None includeFiles = []
class Hull(CGS)
Method resolution order:
Hull
CGS
SolidPyObj __builtin__.object
Methods defined here:
__init__(self, solidPyObj1=None, solidPyObj2=None) renderOSC(self)
Methods inherited from CGS: add(self, solidPyObj1) set__tabLvl(self, lvl)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼release(self)
￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 11 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼rotate(self, x, y=None, z=None, v=None)
Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Import(SolidPyObj)
Method resolution order:
Import SolidPyObj __builtin__.object
Methods defined here: __init__(self, filename) renderOSC(self)
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Methods inherited from SolidPyObj:
￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 12 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼OSCString(self, protoStr)
Returns the OpenSCAD string to make the object
__add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a
__mul__(self, solidPyObj1) __sub__(self, solidPyObj1) color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose']
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 13 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼fa = None
fn = None
fs = None includeFiles = []
class Import_dxf(SolidPyObj)
Method resolution order:
Import_dxf SolidPyObj __builtin__.object
Methods defined here:
__init__(self, filename, layer=None, origin=None, scale=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
Puts a rotate transform on the transform stack
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 14 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Intersection(CGS)
Method resolution order:
Intersection
CGS
SolidPyObj __builtin__.object
Methods defined here:
__init__(self, solidPyObj1=None, solidPyObj2=None) renderOSC(self)
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Methods inherited from CGS:
￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 15 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼add(self, solidPyObj1) set__tabLvl(self, lvl)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj: autoColor = False
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 16 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None
includeFiles = []
class Linear_extrude(SolidPyObj)
Method resolution order:
Linear_extrude SolidPyObj __builtin__.object
Methods defined here:
__init__(self, flatPyObj, height, center=None, convexity=None, twist=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼release(self)
￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 17 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼rotate(self, x, y=None, z=None, v=None)
Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Minkowski(CGS)
Method resolution order:
Minkowski
CGS
SolidPyObj __builtin__.object
Methods defined here:
__init__(self, solidPyObj1=None, solidPyObj2=None) renderOSC(self)
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 18 of 34

￼Python: module SolidPy 9/18/12 6:33 AM
￼￼￼￼￼Methods inherited from CGS: add(self, solidPyObj1) set__tabLvl(self, lvl)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼list of weak references to the object (if defined)
￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 19 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Module(SolidPyObj)
Method resolution order:
Module SolidPyObj __builtin__.object
Methods defined here: __init__(self, name, **kwargs) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼multmatrix(self, m)
￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 20 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼          Puts a multmatrix transform on the transform stack
          *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
          Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Polygon(SolidPyObj)
Method resolution order:
Polygon SolidPyObj __builtin__.object
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Methods defined here:
￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 21 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼__init__(self, points, paths=None, convexity=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Data and other attributes inherited from SolidPyObj:
￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 22 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None
includeFiles = []
class Polyhedron(SolidPyObj)
Method resolution order:
Polyhedron SolidPyObj __builtin__.object
Methods defined here: __init__(self, points, triangles) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 23 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼release(self)
rotate(self, x, y=None, z=None, v=None)
          Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Projection(SolidPyObj) ##projection(cut = true)
Method resolution order:
Projection SolidPyObj __builtin__.object
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Methods defined here:
￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 24 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼__init__(self, flatPyObj, cut) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Data and other attributes inherited from SolidPyObj:
￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 25 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None
includeFiles = []
class Rotate_extrude(SolidPyObj)
Method resolution order:
Rotate_extrude SolidPyObj __builtin__.object
Methods defined here:
__init__(self, flatPyObj, convexity=None, fn=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 26 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼release(self)
rotate(self, x, y=None, z=None, v=None)
          Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class SolidPyObj(__builtin__.object) Methods defined here:
OSCString(self, protoStr)
Returns the OpenSCAD string to make the object
__add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼__init__(self)
￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 27 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼__mul__(self, solidPyObj1) __sub__(self, solidPyObj1) color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors defined here:
__dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
Data and other attributes defined here:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None fs = None
￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 28 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼includeFiles = []
class Sphere(SolidPyObj)
    r=radius
    fa = Angle in degrees
    fs= Angle in mm
    center: If True, object is centered at (0,0,0)
Method resolution order:
Sphere SolidPyObj __builtin__.object
Methods defined here:
__init__(self, rad, fa=None, fs=None, fn=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
          Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 29 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
          dictionary for instance variables (if defined)
__weakref__
          list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
class Square(SolidPyObj)
Method resolution order:
Square SolidPyObj __builtin__.object
Methods defined here: __init__(self, x, y, center=None) renderOSC(self)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 30 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
release(self)
rotate(self, x, y=None, z=None, v=None)
     Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
set__tabLvl(self, lvl)
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
     dictionary for instance variables (if defined)
__weakref__
     list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼fn = None
￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 31 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼fs = None includeFiles = []
class Union(CGS)
Method resolution order:
Union
CGS
SolidPyObj __builtin__.object
Methods defined here:
__init__(self, solidPyObj1=None, solidPyObj2=None) renderOSC(self)
Methods inherited from CGS: add(self, solidPyObj1) set__tabLvl(self, lvl)
Methods inherited from SolidPyObj: OSCString(self, protoStr)
Returns the OpenSCAD string to make the object __add__(self, solidPyObj1)
a=x+y calls x.__add__(y)->a __mul__(self, solidPyObj1) __sub__(self, solidPyObj1)
color(self, color='yellow', alpha=1.0) copy(self)
mirror(self, x, y=None, z=None)
Puts a mirror transform on the transform stack mirror( [x,y,z]) or mirror(x,y,z)
mirror (1) -> [1,1,1]
multmatrix(self, m)
Puts a multmatrix transform on the transform stack *** not tested ***
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼release(self)
￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 32 of 34

Python: module SolidPy 9/18/12 6:33 AM
rotate(self, x, y=None, z=None, v=None)
Puts a rotate transform on the transform stack
scale(self, x, y=None, z=None)
Puts a scale transform on the transform stack
translate(self, x, y=None, z=None)
Puts a translate transform on the transform stack translate( [x,y,z]) or translate(x,y,z)
translate (1) -> [1,1,1]
Data descriptors inherited from SolidPyObj: __dict__
                  dictionary for instance variables (if defined)
__weakref__
                  list of weak references to the object (if defined)
Data and other attributes inherited from SolidPyObj:
autoColor = False
colorCnt = 0
colors = ['blue', 'green', 'orange', 'yellow', 'SpringGreen', 'purple', 'DarkOrchid', 'MistyRose'] fa = None
fn = None
fs = None includeFiles = []
Functions
Use(fileName) boolStr(abool)
             retuns a lower case string of 'true' or 'false'
inches(x)
converts inches to mm
main()
writeSCADfile(fileName, *args)
fileName = the SCAD file to save to. Include the '.scad' extension args can be SolidPyObj or lists of SolidPyObj
￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 33 of 34

Python: module SolidPy 9/18/12 6:33 AM
￼￼file:///Users/bjbsquared/Dropbox/SolidPy/SolidPy.htm Page 34 of 34
