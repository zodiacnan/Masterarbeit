# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 17:58:01 2017

@author: DINGNAN
"""

#current abc
import matplotlib.pyplot as plt


file_1 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ia.dat"
file_2 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ib.dat"
file_3 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ic.dat"
with open(file_1, "r") as fig:
    x = []
    y = []
    for line in fig:
        data = line.split()
        x.append((float(data[0])))
        y.append((float(data[1])))

with open(file_2, "r") as fig:
    a = []
    b = []
    for line in fig:
        data = line.split()
        a.append((float(data[0])))
        b.append((float(data[1])))

with open(file_3, "r") as fig:
    m = []
    n = []
    for line in fig:
        data = line.split()
        m.append((float(data[0])))
        n.append((float(data[1])))

plt.figure(figsize = (16,9),dpi=98)
p1 = plt.subplot(221)
p2 = plt.subplot(222)
p3 = plt.subplot(223)

p1.plot(x,y)
p1.grid(True)
p1.set_xlabel('t -- Time')
p1.set_ylabel('Ia -- Current in Phase A')
p1.legend()

p2.plot(a,b)
p2.grid(True)
p2.set_xlabel('t -- Time')
p2.set_ylabel('Ib -- Current in Phase B')
p2.legend()

p3.plot(m,n)
p3.grid(True)
p3.set_xlabel('t -- Time')
p3.set_ylabel('Ic -- Current in Phase C')
p3.legend()

plt.suptitle("Current Plot")
plt.show()
