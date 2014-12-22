
from solidpy import *

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
