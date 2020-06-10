import automation_stuff.concepts.modules.definingFunctions as opp
import math
import sys
from math import *
from automation_stuff.concepts.modules.definingFunctions import add, sub

print(add(2, 3))
print(sub(2, 3))
print(opp.sub(2, 3))
print(opp.multi(2, 3))
print(opp.div(2, 3))
print(round(math.pi, 2))
print(pi)
print(dir(math))  # get the list of all functions in that file
print(dir(opp))
print((sys.path))
print(opp.__name__)  # an underscore are bydefault python attributes asscociated with modeule(ot user defined)

