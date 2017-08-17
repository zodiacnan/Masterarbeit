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
import subprocess

class LDLQ(QWidget):
    def __init__(self,*args,**kwargs):
        super(LDLQ, self).__init__()
        self.setWindowTitle("Ld/Lq and Psid/Psiq Identification")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.setGeometry(100,100,700,400)
        self.initUI()


    def initUI(self):
        self.Movement()
        self.case1()
        self.case2()
        self.Box()
        main = QVBoxLayout()
        h = QHBoxLayout()
        v = QVBoxLayout()
        v.addWidget(self.casebox1)
        v.addWidget(self.casebox2)
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
        self.end_rotor_angel_text = QLineEdit("180", self)
        self.step = QLabel("Step   Angel    [deg]", self)
        self.step_text = QLineEdit("1", self)
        self.time_step = QLabel("Time Steps", self)
        self.time_step_nr = QLineEdit("180")
        self.parameter = QLabel("Speed           [rpm]", self)
        self.parameter_data = QLineEdit("1500", self)
        self.frequenz = QLabel("Frequence        [Hz]", self)
        self.frequenz_data = QLineEdit("100", self)
        
        self.mvwidget.addRow(self.l_analysis)
        self.mvwidget.addRow(self.start_rotor_angel,self.start_rotor_angel_text)
        self.mvwidget.addRow(self.end_rotor_angel,self.end_rotor_angel_text)
        self.mvwidget.addRow(self.step,self.step_text)
        self.mvwidget.addRow(self.time_step,self.time_step_nr)
        self.mvwidget.addRow(self.parameter,self.parameter_data)
        self.mvwidget.addRow(self.frequenz,self.frequenz_data)
        self.mv.setLayout(self.mvwidget)
        
    def case1(self):
        self.casebox1 = QGroupBox("Case 1")
        self.grid1 = QGridLayout()
        self.id1 = QLabel("Id = 0 ")
        self.id1_t = QLineEdit("0")
        self.iq1 = QLabel("Iq")
        self.iq1_t = QLineEdit("10")
        self.fulxm = QPushButton("Calculate Flux_Magenet")
        self.grid1.addWidget(self.id1,1,0)
        self.grid1.addWidget(self.id1_t,1,1)
        self.grid1.addWidget(self.iq1,2,0)
        self.grid1.addWidget(self.iq1_t,2,1)
        self.grid1.addWidget(self.fulxm,3,1)
        self.casebox1.setLayout(self.grid1)
        
        
    def case2(self):
        self.casebox2 = QGroupBox("Case 2")
        self.grid2 = QGridLayout()
        self.id2 = QLabel("Id != 0")
        self.id2_t = QLineEdit("10")
        self.iq2 = QLabel("Iq")
        self.iq2_t = QLineEdit("10")
        self.fluxdq = QPushButton("Calculate Ld/Lq")
        self.grid2.addWidget(self.id2,1,0)
        self.grid2.addWidget(self.id2_t,1,1)
        self.grid2.addWidget(self.iq2,2,0)
        self.grid2.addWidget(self.iq2_t,2,1)
        self.grid2.addWidget(self.fluxdq,3,1)
        self.casebox2.setLayout(self.grid2)
        
        
    def Box(self):
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.tablebutton = QPushButton("Create Value Table", self)
        self.cancelbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.tablebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.cancelbutton,QDialogButtonBox.ActionRole)


if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = LDLQ()
    window.show()
    app.exec_()
    sys.exit(0)