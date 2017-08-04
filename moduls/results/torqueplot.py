# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 11:22:00 2017

@author: DINGNAN
"""

#torqurplot
import matplotlib.pyplot as plt


file_1 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Tr.dat"
file_2 = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ts.dat"

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


plt.figure(figsize = (16,9),dpi=98)
p1 = plt.subplot(211)
p2 = plt.subplot(212)

p1.plot(x,y,"r")
p1.grid(True)
p1.set_xlabel('t -- Time')
p1.set_ylabel('Tr -- Rotor Torque [Nm]')
p1.legend()

p2.plot(a,b,"r")
p2.grid(True)
p2.set_xlabel('t -- Time')
p2.set_ylabel('Tr -- Stator Torque [Nm]')
p2.legend()


plt.suptitle("Torque Plot")
plt.show()
