# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:36:47 2017

@author: DINGNAN
"""


import matplotlib.pyplot as plt
file_1 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ua.dat"
file_2 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ub.dat"
file_3 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Uc.dat"
with open(file_1, "r") as fig:
    x = []
    deg = []
    y = []
    for line in fig:
        data = line.split()
        x.append((float(data[0])))
        deg.append((float(3000)*float(data[0])))
        y.append((float(data[1])))

with open(file_2, "r") as fig:
    b = []
    for line in fig:
        data = line.split()
        b.append((float(data[1])))

with open(file_3, "r") as fig:
    n = []
    for line in fig:
        data = line.split()
        n.append((float(data[1])))

plt.figure(figsize = (16,9),dpi=98)
plt.plot(deg,y,'red',label='Ua')
plt.plot(deg,b,'green',label='Ub')
plt.plot(deg,n,'blue',label='Uc')
plt.grid(True)
plt.xlabel('Rotor Postion -- [deg]')
plt.ylabel('Voltage in Phase')
plt.legend()
plt.savefig('Voltage.png')
plt.show()
