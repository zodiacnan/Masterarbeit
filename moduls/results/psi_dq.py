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
    y = []
    count = 0
    for line in fig:
        count+=1
        if count%2 == 0:
            data = line.split()
            x.append((float(data[0])))
            y.append((float(data[1])))
        else:
            pass
with open(file_2, "r") as fig:
    m = []
    n = []
    count = 0
    for line in fig:
        count+=1
        if count%2 == 0:
            data = line.split()
            m.append((float(data[0])))
            n.append((float(data[1])))
        else:
            pass

plt.figure(figsize = (16,9),dpi=98)
p1 = plt.subplot(211)
p2 = plt.subplot(212)

p1.plot(x,y)
p1.set_xlabel('t -- Time')
p1.set_ylabel('Psi_d')
p1.legend()

p2.plot(m,n)
p2.set_xlabel('t -- Time')
p2.set_ylabel('Psi_q')
p2.legend()


plt.suptitle("Psi_d and Psi_q")
plt.show()
