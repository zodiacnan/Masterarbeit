# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 12:18:57 2017

@author: DINGNAN
"""

#HTML tabel
import matplotlib.pyplot as plt
file_Ua = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ua.dat"
file_Ub = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ub.dat"
file_Uc = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Uc.dat"
file_Fd = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Flux_d.dat"
file_Fq = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Flux_q.dat"
file_Ia = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ia.dat"
file_Ib = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ib.dat"
file_Ic = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ic.dat"
file_tr = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Tr.dat"
file_ts = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ts.dat"

with open(file_tr, "r") as fig:
    t = []
    deg = []
    tr = []
    for line in fig:
        data = line.split()
        t.append((float(data[0])))
        deg.append((float(10000)*float(data[0])))
        tr.append((float(data[1])))
        
plt.figure(figsize = (16,9),dpi=98)
p1 = plt.subplot(211)
p1.plot(deg,tr)
p1.set_xlabel('Rotor Position[deg]')
p1.set_ylabel('Psi_d')
p1.legend()
plt.suptitle("Psi_d and Psi_q")
plt.show()

