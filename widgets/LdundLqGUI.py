# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:03:02 2017

@author: DINGNAN
"""

#Ld and Lq Identifikation

'''
Input: Id, Iq, Speed
Calculate: Ld, Lq
'''


import sys
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import numpy as np
import xlwt
import matplotlib.pyplot as plt

class LDLQ(QWidget):
    def __init__(self,*args,**kwargs):
        super(LDLQ, self).__init__()
        self.setWindowTitle("Ld/Lq Identification")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()

    def initUI(self):
        self.Movement()
        self.case1()
        self.Box()
        main = QVBoxLayout()
        h = QHBoxLayout()
        v = QVBoxLayout()
        v.addWidget(self.casebox1)
        h.addWidget(self.mv)
        h.addLayout(v)
        main.addLayout(h)
        main.addWidget(self.buttonbox)        
        self.setLayout(main)
        
    def Movement(self):
        self.mv = QGroupBox("[Movement]", self)
        self.mvwidget = QFormLayout(self)
        # Analysis Type of getdp
        self.l_analysis = QLabel('Static Time Domain', self)
        self.start_rotor_angel = QLabel("Start  Angel    [deg]", self)
        self.start_rotor_angel_text = QLineEdit("0", self)
        self.end_rotor_angel = QLabel("End    Angel    [deg]", self)
        self.end_rotor_angel_text = QLineEdit("10", self)
        self.step = QLabel("Step   Angel    [deg]", self)
        self.step_text = QLineEdit("0.5", self)
        self.time_step = QLabel("Time Steps", self)
        self.time_step_nr = QLineEdit("60")
        self.parameter = QLabel("Speed           [rpm]", self)
        self.parameter_data = QLineEdit("500", self)
        
        self.frequenz = QLabel("Frequence        [Hz]", self)
        self.frequenz_data = QLineEdit("33.33", self)
        
        self.mvwidget.addRow(self.l_analysis)
        self.mvwidget.addRow(self.start_rotor_angel,self.start_rotor_angel_text)
        self.mvwidget.addRow(self.end_rotor_angel,self.end_rotor_angel_text)
        self.mvwidget.addRow(self.step,self.step_text)
        self.mvwidget.addRow(self.time_step,self.time_step_nr)
        self.mvwidget.addRow(self.parameter,self.parameter_data)
        self.mvwidget.addRow(self.frequenz,self.frequenz_data)
        self.mv.setLayout(self.mvwidget)
        
    def case1(self):
        self.casebox1 = QGroupBox("Input Parameters")
        self.grid1 = QGridLayout()
        self.id1 = QLabel("Is_eff [Current]")
        self.id1_s = QLabel("    Min Current  [A]")
        self.id1_e = QLabel("    Max Current  [A]")
        self.id1_u = QLabel("    Current Increment  [A]")
        self.id1_s_t = QLineEdit("10")
        self.id1_e_t = QLineEdit("50")
        self.id1_u_t = QLineEdit("10")
        self.theta = QLabel("Theta[Id/Iq]")
        self.theta_s = QLabel("    Theta_min  [deg]")
        self.theta_e = QLabel("    Theta_max  [deg]")
        self.theta_u = QLabel("    PhaseShift Increment  [deg]")
        self.theta_s_t = QLineEdit("-90")
        self.theta_e_t = QLineEdit("90")
        self.theta_u_t = QLineEdit("30")
        self.grid1.addWidget(self.id1,1,0)
        self.grid1.addWidget(self.id1_s,2,0)
        self.grid1.addWidget(self.id1_s_t,2,1)
        self.grid1.addWidget(self.id1_e,3,0)
        self.grid1.addWidget(self.id1_e_t,3,1)
        self.grid1.addWidget(self.id1_u,4,0)
        self.grid1.addWidget(self.id1_u_t,4,1)
        self.grid1.addWidget(self.theta,5,0)
        self.grid1.addWidget(self.theta_s,6,0)
        self.grid1.addWidget(self.theta_s_t,6,1)
        self.grid1.addWidget(self.theta_e,7,0)
        self.grid1.addWidget(self.theta_e_t,7,1)
        self.grid1.addWidget(self.theta_u,8,0)
        self.grid1.addWidget(self.theta_u_t,8,1)
        self.casebox1.setLayout(self.grid1)
                
    def Box(self):
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.calbutton = QPushButton("Calculate", self)
        self.tablebutton = QPushButton("Create Excel Table",self)
        self.plotbutton = QPushButton("Plot Torque/Theta")
        self.cancelbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.calbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.tablebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.plotbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.cancelbutton,QDialogButtonBox.ActionRole)
        self.calbutton.clicked.connect(self.calculate)
        self.tablebutton.clicked.connect(self.excel_tabel)
        self.plotbutton.clicked.connect(self.plot_Tandtheta)
        
    def calculate(self):
        rpm = "rpm_nominal = "+str(self.parameter_data.text())+";\n"
        tm = "thetaMax_deg ="+str(self.end_rotor_angel_text.text())+";\n"
        t0 = "theta0   = InitialRotorAngle  + 0. ;\n"
        deta = "delta_theta_deg = "+str(self.step_text.text())+";\n"
        extra1 = "Flag_AnalysisType = 1 ;\nFlag_SrcType_Stator =  1 ; \nFlag_Cir = !Flag_SrcType_Stator ; \nFlag_ImposedCurrentDensity = Flag_SrcType_Stator ; \nFlag_ParkTransformation = 1 ;\n"
        extra2 = 'Include "inputsolverGUI.pro"'
        Imin = int(self.id1_s_t.text())
        Imax = int(self.id1_e_t.text())
        detaI = int(self.id1_u_t.text())
        thetamin = int(self.theta_s_t.text())
        thetamax = int(self.theta_e_t.text())
        deltatheta = int(self.theta_u_t.text())
        print(Imin,Imax,detaI,thetamin,thetamax,deltatheta)
        i = Imin
        for i in range(Imin,int(Imax)+1,detaI):
            j = thetamin
            for j in range(thetamin,int(thetamax)+1,deltatheta):
                theta = j*2*np.pi/360
                #Id_i = i*np.sin(theta)/np.sin(np.pi-np.pi/4)
                #Iq_i = i*np.sin(np.pi/4-theta)/np.sin(np.pi-np.pi/4)
                Id_i = i*np.sin(theta)
                Iq_i = i*np.cos(theta)
                print(Id_i,Iq_i)
                txt1 = 'ResId = "/cpu1";\n'
                filename = "I"+str(i)+"Theta"+str(j)
                global filename
                txt2 = "ResDir = StrCat["+ '"res/LdandLq/'+str(filename)+'/"];\n'
                filename1 = 'moduls\\temp\\Nameofresult.pro'
                filename2 = 'moduls\\temp\\inputforpro.pro'
                try: 
                    file1 = open(filename1, 'w+')
                    file1.truncate()
                    file1.close()
                    file2 = open(filename1, 'w+')
                    file2.truncate()
                    file2.close()
                except:
                    print('Something went wrong')
                f1 = open(filename1, 'w+')
                add_content = [txt1,txt2]
                f1.writelines(add_content)
                f1.close()
                ii = "II="+str(int(i))+";\n"
                Id = "ID = "+str(Id_i)+";\n"
                Iq = "IQ = "+str(Iq_i)+";\n"
                f2 = open(filename2, 'w+')
                add_content2 = [rpm,ii,Id,Iq,tm,t0,deta,extra1,extra2]
                f2.writelines(add_content2)
                f2.close()
                command = "gmsh C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\moduls\\temp\\pmsm.pro -"
                os.system(command)
    def excel_tabel(self):
        f = xlwt.Workbook()
        col_width = 256*15
        sheet_1 = f.add_sheet('LdandLq' , cell_overwrite_ok = True)
        row_0 = ['Is_eff','Theta[Last]','Id[A]','Iq[A]','Flux_d[Vs]','Flux_q[Vs]','Flux_M[Vs]','Ld[Hm]','Lq[Hm]',
             'Torque_Air[FEM]', 'T_Sim[Cal]']
        Id = []
        Iq = []
        Is = []
        beta = []
        deg = []
        ta = []
        t_sim = []
        fm = []
        Ld = []
        Lq = []
        fd = []
        fq = []
        fact = int(self.parameter_data.text())*360/60
        Imin = int(self.id1_s_t.text())
        Imax = int(self.id1_e_t.text())
        detaI = int(self.id1_u_t.text())
        thetamin = int(self.theta_s_t.text())
        thetamax = int(self.theta_e_t.text())
        deltatheta = int(self.theta_u_t.text())
        i = Imin
        for i in range(Imin,int(Imax)+1,detaI):
            j = thetamin
            for j in range(thetamin,int(thetamax)+1,deltatheta):
                theta = j*2*np.pi/360
                Id_i = i*np.sin(theta)
                Iq_i = i*np.cos(theta)
                filename = "I"+str(i)+"Theta"+str(j)
                file_tr = "moduls\\temp\\res\\LdandLq\\"+str(filename)+"\\Tr.dat"
                file_ts = "moduls\\temp\\res\\LdandLq\\"+str(filename)+"\\Ts.dat"
                file_fd = "moduls\\temp\\res\\LdandLq\\"+str(filename)+"\\Flux_d.dat"
                file_fq = "moduls\\temp\\res\\LdandLq\\"+str(filename)+"\\Flux_q.dat"
                with open(file_tr, "r") as fig:
                    for line in fig:
                        data = line.split()
                        deg.append((float(fact)*float(data[0])))                        
                with open(file_fd, "r") as fig:
                    count = 0
                    for line in fig:
                        count+=1
                        if count%2 == 0:
                            data = line.split()
                            Fd = np.mean(float(data[1]))
                        else:
                            pass
                with open(file_fq, "r") as fig:
                    count = 0
                    for line in fig:
                        count+=1
                        if count%2 == 0:
                            data = line.split()
                            Fq = np.mean(float(data[1]))
                        else:
                            pass
                with open(file_ts, "r") as fig:
                    for line in fig:
                        data = line.split()
                        Ts = np.mean(float(data[1]))
                with open(file_tr, "r") as fig:
                    for line in fig:
                        data = line.split()
                        Tr = np.mean(float(data[1]))
                ID = Id_i
                IQ = Iq_i
                Ta = (Tr+Ts)/2
                T_sim = 1.5*4*(Fd*Iq_i-Fq*Id_i)
                Is.append(i)
                beta.append(j)
                Id.append(ID)
                Iq.append(IQ)
                fd.append(Fd)
                fq.append(Fq)
                ta.append(Ta)
                t_sim.append(T_sim)
                LQ = Fq/IQ
                Lq.append(LQ)
                if j == 0:
                    Fm = Fd
                    fm = fm+[Fm]*((thetamax-thetamin)/deltatheta+1)
        print len(fm)
        Ld = [(x-y)/z for x,y,z in zip(fd,fm,Id)]
        print len(Ld)
        for m in range(0,len(row_0)):
            sheet_1.col(m).width = col_width
            sheet_1.write(0,m,row_0[m])
        for n in range(0,len(Is)):
            sheet_1.write(n+1,0,Is[n])
            sheet_1.write(n+1,1,beta[n])
            sheet_1.write(n+1,2,Id[n])
            sheet_1.write(n+1,3,Iq[n])
            sheet_1.write(n+1,4,fd[n])
            sheet_1.write(n+1,5,fq[n])
            sheet_1.write(n+1,6,fm[n])
            sheet_1.write(n+1,7,Ld[n])
            sheet_1.write(n+1,8,Lq[n])
            sheet_1.write(n+1,9,ta[n])
            sheet_1.write(n+1,10,t_sim[n])
        f.save('LdandLq'+'.xls')

    def plot_Tandtheta(self):
        pass
    
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = LDLQ()
    window.show()
    app.exec_()
    sys.exit(0)