# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 13:19:16 2017

@author: DINGNAN
"""

import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
import subprocess

filename = "moduls\\PMSM1\\geo.pos"
command = "gmsh.exe "+ filename
subprocess.Popen(command, shell = False)