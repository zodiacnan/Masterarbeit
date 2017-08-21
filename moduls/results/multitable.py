# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:55:07 2017

@author: DINGNAN
"""

#write the excel table of Ld-Lq identifikation
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\moduls\\results')
import xlrd
import xlwt
import numpy as np
import matplotlib
from datetime import date,datetime
import pandas as pd

NPP = 4 #NbrPolePairs = 8
speed = 500 #rad/s
fact = speed*360/60
deg = []
Theta = []
Iq = []
Id = []
Ua = []
Ub = []
Uc = []
Fd = []
Fq = []
L = []
Tr = []
Ts = []
deg_r = []
Id.append(float(0))
Iq.append(float(10))
file_Ua = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ua.dat"
file_Ub = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ub.dat"
file_Uc = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Uc.dat"
file_tr = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Tr.dat"
file_ts = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Ts.dat"
file_fd = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Flux_d.dat"
file_fq = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\Flux_q.dat"
file_l = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\machines\\res\\inductance.dat"

with open(file_Ua, "r") as fig:
    for line in fig:
        data = line.split()
        Ua.append((float(data[1])))

with open(file_Ub, "r") as fig:
    for line in fig:
        data = line.split()
        Ub.append((float(data[1])))

with open(file_Uc, "r") as fig:
    for line in fig:
        data = line.split()
        Uc.append((float(data[1])))

with open(file_l, "r") as fig:
    for line in fig:
        data = line.split()
        L_value = float(data[1])

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
        Theta.append((float(fact)*float(data[0])+(np.pi/8)-(np.pi/6))*NPP)
        deg_r = np.around(deg).astype(int)
        Theta_r = np.around(Theta).astype(int)
    print(deg_r)
    print(Theta_r)
    



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
    sheet_1 = f.add_sheet('multifuction_table' , cell_overwrite_ok = True)
    row_0 = ['RotorPosition','Theta[Park]','Id[A]','Iq[A]','Ua[V]','Ub[V]','Uc[V]','Flux_d[Vs]','Flux_q[Vs]','Torque_S[Nm]','Torque_R[Nm]','Inductance from Flux[mH]']
    Id = [0]*len(deg_r)
    Iq = [10]*len(deg_r)
    L = [L_value]*len(deg_r)
    for i in range(0,len(row_0)):
        sheet_1.col(i).width = col_width
        sheet_1.write(0,i,row_0[i],set_style('Time New Roman',220,True))
    for j in range(0,len(deg_r)):
        sheet_1.write(j+1,0,deg_r[j])
        sheet_1.write(j+1,1,Theta_r[j])
        sheet_1.write(j+1,2,Id[j])
        sheet_1.write(j+1,3,Iq[j])
        sheet_1.write(j+1,4,Ua[j])
        sheet_1.write(j+1,5,Ub[j])
        sheet_1.write(j+1,6,Uc[j])
        sheet_1.write(j+1,7,Fd[j])
        sheet_1.write(j+1,8,Fq[j])
        sheet_1.write(j+1,9,Ts[j])
        sheet_1.write(j+1,10,Tr[j])
        sheet_1.write(j+1,11,L[j])
    f.save('multifuction_table.xls')
    
    df_excel = pd.ExcelFile('multifuction_table.xls')
    df = df_excel.parse('multifuction_table')  # give summary sheet name
    df.to_html('multifuction_table.html')


if __name__ == '__main__':
    write_excel()