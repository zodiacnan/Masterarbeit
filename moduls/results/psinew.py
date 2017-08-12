# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 09:53:26 2017

@author: DINGNAN
"""

#Psid_q
import matplotlib.pyplot as plt


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
            x.append((float(data[0])*float(10000)))
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
p1 = plt.subplot(211)
p2 = plt.subplot(221)
p3 = plt.subplot(222)

p1.plot(x,y,'red',label = 'Flux_d')
p1.plot(x,n,'blue',label = 'Flux_q')
p1.set_xlabel('Rotor Position -- [deg]')
p1.set_ylabel('Psi_d')
p1.legend()

p2.plot(x,y,'red',label = 'Flux_d')
p2.set_xlabel('Rotor Position -- [deg]')
p2.set_ylabel('Psi_d')
p2.legend()

p3.plot(x,n,'blue',label = 'Flux_q')
p3.set_xlabel('Rotor Position -- [deg]')
p3.set_ylabel('Psi_q')
p3.legend()

plt.suptitle("Psi_d and Psi_q")
plt.show()