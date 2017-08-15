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
        deg.append((float(10000)*float(data[0])))
        y.append((float(data[1])))
    num = len(y)
    print(num)
    torque_r = sum(y)/num
    print(torque_r)
    compare = []
    compare.append(float(torque_r))
        
with open(file_2, "r") as fig:
    b = []
    for line in fig:
        data = line.split()
        b.append((float(data[1])))


plt.figure(figsize = (16,9),dpi=98)
p1 = plt.subplot(211)

p1.plot(deg,y,"red",label='Torque[Rotor]')
p1.plot(deg,b,"blue",label='Torque[Stator]')
p1.plot(deg,compare, "green", label='Torque_e')
p1.grid(True)
p1.set_xlabel('Rotor Position -- [deg]')
p1.set_ylabel('T -- Torque [Nm]')
p1.legend()


plt.suptitle("Torque Plot")
plt.show()