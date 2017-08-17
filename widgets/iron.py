# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:03:24 2017

@author: DINGNAN
"""
#iron
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class Iron_Set(QWidget):
    def __init__(self,*args,**kwargs):
        super(Iron_Set, self).__init__()
        self.setWindowTitle("Iron - and Cu-Losses - EVALUATION")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()


    def initUI(self):
        self.left()
        self.right()
        self.Box()
        main = QVBoxLayout()
        main1 = QHBoxLayout()
        main11 = QVBoxLayout()
        main12 = QVBoxLayout()
        main1.addLayout(main11)
        main1.addLayout(main12)
        main11.addLayout(self.layout1)
        main12.addLayout(self.form)
        main.addLayout(main1)
        main.addWidget(self.buttonbox)
        self.setLayout(main)
        
        
    def left(self):
        self.layout1 = QGridLayout()
        self.frq = QLabel("Frequency                             f   [Hz]",self)
        self.frq0 = QLabel("Base Frequency                        fo  [Hz]",self)
        self.ind = QLabel("Base Induction                        Bo   [T]",self)
        self.h_co = QLabel("Hysteresis-Coefficient               ch [W/kg]",self)
        self.e_co = QLabel("Eddycurrent-Coefficient              cw [W/kg]",self)
        self.hfh = QLabel("Hysteresis-Frequency-Coefficient      hfh (=1)",self)
        self.hfe = QLabel("Eddycurrent-Frequency-Coefficient     hfe (=2)",self)
        self.density = QLabel("Iron Density                      rho [kg/m3]",self)
        self.i_c = QLabel("Induction-Coefficient                  bc (=2)",self)
        self.mat_f = QLabel("FE-Material factor                  ff >= 1.0",self)
        self.ff = QLabel("Conductor space filling-factor:          <= 1",self)
        self.rcl = QLabel("Relative conductor length (core+end wdg) [%]",self)
        self.cc = QLabel("Conductor conductivity.               [1/Ohm m]",self)
        self.ncl = QLabel("Number of conductor layers              > = 1",self)
        self.ch = QLabel("Conductor height:",self)
        
        self.frq_t = QLineEdit("100.0",self)
        self.frq0_t = QLineEdit("50.00",self)
        self.ind_t = QLineEdit("1.500",self)
        self.h_co_t = QLineEdit("4.000",self)
        self.e_co_t = QLineEdit("2.000",self)
        self.hfh_t = QLineEdit("1.000",self)
        self.hfe_t = QLineEdit("2.000",self)
        self.i_c_t = QLineEdit("2.000",self)
        self.density_t =QLineEdit("7840",self)
        self.mat_f_t =QLineEdit("1.000",self) 
        self.ff_t = QLineEdit("0.400",self)
        self.rcl_t = QLineEdit("100.0",self)
        self.cc_t = QLineEdit("0.4540e8",self)
        self.ncl_t = QLineEdit("10.00",self)
        self.ch_t = QLineEdit("3.000",self)
        
        self.layout1 = QGridLayout()
        self.layout1.addWidget(self.frq, 1,0)
        self.layout1.addWidget(self.frq0,2,0)
        self.layout1.addWidget(self.ind,3,0)
        self.layout1.addWidget(self.h_co,4,0)
        self.layout1.addWidget(self.e_co,5,0)
        self.layout1.addWidget(self.hfh,6,0)
        self.layout1.addWidget(self.hfe,7,0)
        self.layout1.addWidget(self.i_c,8,0)
        self.layout1.addWidget(self.density,9,0)
        self.layout1.addWidget(self.mat_f,10,0)
        self.layout1.addWidget(self.ff,11,0)
        self.layout1.addWidget(self.rcl,12,0)
        self.layout1.addWidget(self.cc,13,0)
        self.layout1.addWidget(self.ncl,14,0)
        self.layout1.addWidget(self.ch,15,0)

        self.layout1.addWidget(self.frq_t, 1,1)
        self.layout1.addWidget(self.frq0_t,2,1)
        self.layout1.addWidget(self.ind_t,3,1)
        self.layout1.addWidget(self.h_co_t,4,1)
        self.layout1.addWidget(self.e_co_t,5,1)
        self.layout1.addWidget(self.hfh_t,6,1)
        self.layout1.addWidget(self.hfe_t,7,1)
        self.layout1.addWidget(self.i_c_t,8,1)
        self.layout1.addWidget(self.density_t,9,1)
        self.layout1.addWidget(self.mat_f_t,10,1)
        self.layout1.addWidget(self.ff_t,11,1)
        self.layout1.addWidget(self.rcl_t,12,1)
        self.layout1.addWidget(self.cc_t,13,1)
        self.layout1.addWidget(self.ncl_t,14,1)
        self.layout1.addWidget(self.ch_t,15,1)

        
    
    def right(self):
        self.layout2 = QGroupBox("Loss Equation")
        self.form = QFormLayout()
        self.angel = QLabel("Angel_Belta [Up/I]")
        self.angel_a = QLineEdit("10")
        self.speed = QLabel("Speed    [rad/min]")
        self.speed_e = QLineEdit("1500")
        self.current = QLabel("Current    [A]")
        self.current_c = QComboBox(self)
        self.list = [self.tr('abc-Phase Current'), self.tr('dq-Phase Current')]
        self.current_c.addItems(self.list)
        self.current_t = QLineEdit("10")
        self.form.addRow(self.angel,self.angel_a)
        self.form.addRow(self.speed,self.speed_e)
        self.form.addRow(self.current)
        self.form.addRow(self.current_c,self.current_t)
        self.form.addRow(self.layout2)
        
    def Box(self):
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.calbutton = QPushButton("Calculate B-Feld", self)
        self.tablebutton = QPushButton("Calculate Losses[Fe/Cu]", self)
        self.plotbutton = QPushButton("Create Result Table", self)
        self.cancelbutton = QPushButton("Cancel", self)
        self.cal_a = QPushButton("Calculate area of iron losses [mm2]",self)
        self.buttonbox.addButton(self.cal_a,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.calbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.tablebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.plotbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.cancelbutton,QDialogButtonBox.ActionRole)
        self.cancelbutton.clicked.connect(self.cancel)

    def cal_save(self):
        frq = self.frq_t.text()
        frq0 = self.frq0_t.text()
        ind = self.ind_t.text()
        h_co = self.h_co_t.text()
        e_co = self.e_co_t.text()
        hfh_i = self.hfh_t.text()
        hfe_i = self.hfe_t.text()
        i_c_i = self.i_c_t.text()
        density = self.density_t.text()
        mat_f = self.mat_f_t.text()
        ff = self.ff_t.text()
        a = self.cal_a_t.text()
        
        f = "f="+str(frq)
        f0 = "f0="+str(frq0)
        b0 = "b0="+str(ind)
        ch = "ch="+str(h_co)
        cw = "cw="+str(e_co)
        hfh = "hfh="+str(hfh_i)
        hfe = "hfe="+str(hfe_i)
        bc = "bc="+str(i_c_i)
        rho = "rho="+str(density)
        area = "A="+str(a)
        
        
        
        os.chdir('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls')
        filename = "dataoflosses.py"
        try: 
            file = open(filename, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        
        f1 = open(filename, 'w+')
        add_content = [f,f0,b0,ch,cw,hfh,hfe,rho,area,bc]
        for line in add_content:
            f1.write(line)
            f1.write('\n')
        f1.close()
        
        
    def cancel(self):
        self.close()
        
        
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Iron_Set()
    window.setGeometry(100,100,900,000)
    window.show()
    app.exec_()
    sys.exit(0)