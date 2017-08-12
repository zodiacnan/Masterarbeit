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
        deg.append((float(10000)*float(data[0])))
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
p1 = plt.subplot(221)


p1.plot(deg,y,'red',label='Ua')
p1.plot(deg,b,'green',label='Ub')
p1.plot(deg,n,'blue',label='Uc')
p1.grid(True)
p1.set_xlabel('Rotor Postion -- [deg]')
p1.set_ylabel('Voltage in Phase')
p1.legend()

plt.suptitle("Voltage Plot")
plt.show()
