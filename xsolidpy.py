
from __future__ import print_function

import SolidPy
from SolidPy import *

import os
import subprocess
import re
from math import *

# defaults

Defaults.fn = 0
Defaults.fa = 5
Defaults.fs = 1
Do = 0.05
Dh = 2*Do

#SolidPyObj.move = SolidPyObj.translate

def assemble(assembly, solid_file = None, format = "openscad"):

  import inspect
  if solid_file is None:
    solid_file = inspect.stack()[1][1]

  if format == "openscad":
    output_file = re.sub(r'\.solid\.py$', '.scad', solid_file)

  if output_file == solid_file:
    print("file has wrong extension, must be .solid.py")
    exit(1)

  print("output to %s" % (output_file))

  if format == "openscad":
    writeSCADfile(output_file, assembly)

  try:
    if os.environ['SOLIDPY_SHOW']:
      processes = subprocess.check_output(['ps','ax'])
      #print processes
      #if not 'openscad' in processes:
      if not output_file in str(processes):
        os.setsid()
        process = subprocess.Popen(['openscad', output_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        assert not process.poll()
  except:
    pass
