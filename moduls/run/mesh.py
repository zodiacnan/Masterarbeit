# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 13:19:31 2017

@author: DINGNAN
"""
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
import subprocess

filename = "moduls\\PMSM1\\pmsm_cbmag.geo"
command = "gmsh.exe "+ filename + " pmsm_cbmag.msh"
subprocess.Popen(command, shell = False)
