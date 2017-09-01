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
    deg = []
    y = []
    for line in fig:
        data = line.split()
        x.append((float(data[0])))
        deg.append((float(3000)*float(data[0])))
        y.append((float(data[1])))
        Tmax = max(y)
with open(file_2, "r") as fig:
    count = 0
    b = []
    for line in fig:
        count +=1
        if count%2 == 1:
            data = line.split()
            b.append((float(data[1])))
        else:
            pass

plt.figure(figsize = (16,9),dpi=98)
plt.plot(deg,y,"red",label = 'Torque[Rotor]')
plt.plot(deg,b,"blue",label = 'Torque[Stator]')
plt.grid(True)
plt.xlabel('Rotor Position -- [deg]')
plt.ylabel('T -- Torque [Nm]')
plt.ylim(-1,float(Tmax)+20)
plt.legend()
plt.savefig('Torque.png')
plt.show()


