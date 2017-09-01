# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 09:53:26 2017

@author: DINGNAN
"""

#Psid_q
import matplotlib.pyplot as plt
import pandas as pd

file_1 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Flux_d.dat"
file_2 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Flux_q.dat"

with open(file_1, "r") as fig:
    x = []
    count = 0
    y = []
    for line in fig:
        count+=1
        if count%2 == 0:
            data = line.split()
            x.append((float(data[0])*float(3000)))
            y.append((float(data[1])))
        else:
            pass
        
with open(file_2, "r") as fig:
    n = []
    count = 0
    for line in fig:
        count+=1
        if count%2 == 0:
            data = line.split()
            n.append((float(data[1])))
        else:
            pass

plt.figure(figsize = (16,9),dpi=98)

plt.plot(x,y,'red',label = 'Flux_d')
plt.plot(x,n,'blue',label = 'Flux_q')
plt.xlabel('Rotor Position -- [deg]')
plt.ylabel('Psi_d/q')
plt.grid(True)
plt.legend()
plt.savefig('Fluxdq.png')
plt.show()

