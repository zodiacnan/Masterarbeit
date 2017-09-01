# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:55:07 2017

@author: DINGNAN
"""

#write the excel table of Ld-Lq identifikation
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\machines\\res\\')
import xlwt
import numpy as np
import matplotlib
from datetime import date,datetime
import pandas as pd
import math

NbrPolePairs = 4.0 #NbrPolePairs = 8
speed = 500.0 #rad/s
fact = speed*360/60
Iseff = 10.9
beta = np.pi/8
Id = []
Iq = []
Is = []
deg = []
Beta = []
Fd = []
Fq = []
Tr = []
Ts = []
Ta = []
T_sim = []
deg_r = []
file_tr = "Tr.dat"
file_ts = "Ts.dat"
file_fd = "Flux_d.dat"
file_fq = "Flux_q.dat"

with open(file_fd, "r") as fig:
    count = 0
    for line in fig:
        count+=1
        if count%2 == 0:
            data = line.split()
            Fd.append((float(data[1])))
        else:
            pass
with open(file_fq, "r") as fig:
    count = 0
    for line in fig:
        count+=1
        if count%2 == 0:
            data = line.split()
            Fq.append((float(data[1])))
        else:
            pass

with open(file_ts, "r") as fig:
    for line in fig:
        data = line.split()
        Ts.append((float(data[1])))

with open(file_tr, "r") as fig:
    for line in fig:
        data = line.split()
        Tr.append((float(data[1])))

with open(file_tr, "r") as fig:
    for line in fig:
        data = line.split()
        deg.append((float(fact)*float(data[0])))
        deg_r = np.around(deg).astype(int)

def set_style(name,height,bold = True):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font
    return style
        
def write_excel():
    f = xlwt.Workbook()
    col_width = 256*15
    sheet_1 = f.add_sheet('LdandLq' , cell_overwrite_ok = True)
    row_0 = ['Is_eff','Theta[Last]','Id[A]','Iq[A]','Flux_d[Vs]','Flux_q[Vs]',
             'Torque_Air[Nm]', 'T_Simulation[Nm]']
    Is = [float(Iseff)]*len(deg_r)
    Id_i = Iseff*np.sin(beta)/np.sin(np.pi-np.pi/NbrPolePairs)
    Id = [Id_i]*len(deg_r)
    Iq_i = Iseff*np.sin(np.pi/NbrPolePairs-beta)/np.sin(np.pi-np.pi/NbrPolePairs)
    Iq = [Iq_i]*len(deg_r)
    Beta = [beta]*len(deg_r)
    Ta = map(lambda (Tr,Ts): (Tr+Ts)/2, zip(Tr, Ts))
    T_sim = map(lambda (Fd, Fq, Id, Iq): 1.5*NbrPolePairs*(Fd*Iq-Fq*Id), zip(Fd, Fq, Id,Iq))
    for i in range(0,len(row_0)):
        sheet_1.col(i).width = col_width
        sheet_1.write(0,i,row_0[i],set_style('Time New Roman',220,True))
    for j in range(0,len(deg_r)):
        sheet_1.write(j+1,0,Is[j])
        sheet_1.write(j+1,1,Beta[j])
        sheet_1.write(j+1,2,Id[j])
        sheet_1.write(j+1,3,Iq[j])
        sheet_1.write(j+1,4,Fd[j])
        sheet_1.write(j+1,5,Fq[j])
        sheet_1.write(j+1,6,Ta[j])
        sheet_1.write(j+1,7,T_sim[j])
    name = 'LdandLq'+str(int(Iseff))+str(int(beta))+'pm'
    f.save(name+'.xls')

    df_excel = pd.ExcelFile(name+'.xls')
    df = df_excel.parse('LdandLq')  # give summary sheet name
    df.to_html('LdandLq.html')
    print(1)


if __name__ == '__main__':
    write_excel()