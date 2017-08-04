# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:28:25 2017

@author: DINGNAN
"""

#calculate of iron losses

import sys

sys.path.append('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls')
from dataoflosses import *

Bmax = 2
V = 607*50/1000000000
PvStein = (((f/f0)*((Bmax/b0)**bc)))
PT = (ch*((Bmax/b0)**hfe)*(f/f0))
PvJordan = (((((ch*(f/f0)*((Bmax/b0)**bc))+(((f/f0)**hfe)*((Bmax/b0)**bc))*cw))*rho))*V

print(PvStein)
print(PT)
print(PvJordan)