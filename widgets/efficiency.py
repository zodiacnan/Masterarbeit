# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 13:03:02 2017

@author: DINGNAN
"""

#effizient

'''
Input: Angel Belta, Speed
Calculate:Cu_Losses, Fe_Losses, Mechanical Power, Effizienz
'''


import sys
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import subprocess

class Eff(QWidget):
    def __init__(self,*args,**kwargs):
        super(Eff, self).__init__()
        self.setWindowTitle("Efficiency Table and Plot")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.setGeometry(100,100,700,400)
        self.initUI()


    def initUI(self):
        self.grid1_text()
        self.grid3_text()
        self.Box()
        main = QVBoxLayout()
        child1 = QVBoxLayout()
        child1.addWidget(self.input)
        child3 = QVBoxLayout()
        child3.addWidget(self.output)
        main.addLayout(child1)
        main.addLayout(child3)
        main.addWidget(self.buttonbox)
        self.setLayout(main)
        
    def grid1_text(self):
        self.input = QGroupBox("Inputs:", self)
        self.grid1 = QGridLayout()
        self.angel = QLabel("Angel_Belta [Up/I]")
        self.angel_1 = QLabel("Initial [deg]")
        self.angel_2 = QLabel("End [deg]")
        self.angel_3 = QLabel("Unit [deg]")
        self.angel_s = QLineEdit("0")
        self.angel_e = QLineEdit("50")
        self.angel_a = QLineEdit("10")
        
        
        self.speed = QLabel("Speed    [rad/min]")
        self.speed_1 = QLabel("Initial [rad/min]")
        self.speed_2 = QLabel("End [rad/min]")
        self.speed_3 = QLabel("Unit [rad/min]")
        self.speed_s = QLineEdit("0")
        self.speed_e = QLineEdit("1600")
        self.speed_a = QLineEdit("200")
        self.current = QLabel("Current [A]")
        self.current_c = QComboBox(self)
        self.list = [self.tr('abc-Phase Current'), self.tr('dq-Phase Current')]
        self.current_c.addItems(self.list)
        self.current_t = QLineEdit("10")
        
        self.loss = QLabel("Losses")
        self.ironbutton = QPushButton("Losses Calculation Setup")
        self.ironbutton.clicked.connect(self.open_ironforeff)
        self.grid1.addWidget(self.angel, 1, 0)
        self.grid1.addWidget(self.angel_1, 1, 1)
        self.grid1.addWidget(self.angel_2, 1, 2)
        self.grid1.addWidget(self.angel_3, 1, 3)
        self.grid1.addWidget(self.angel_s, 2, 1)
        self.grid1.addWidget(self.angel_e, 2, 2)
        self.grid1.addWidget(self.angel_a, 2, 3)
        self.grid1.addWidget(self.speed,3,0)
        self.grid1.addWidget(self.speed_1,3,1)
        self.grid1.addWidget(self.speed_2,3,2)
        self.grid1.addWidget(self.speed_3,3,3)
        self.grid1.addWidget(self.speed_s,4,1)
        self.grid1.addWidget(self.speed_e,4,2)
        self.grid1.addWidget(self.speed_a,4,3)
        self.grid1.addWidget(self.current,5,0)
        self.grid1.addWidget(self.current_c,5,1)
        self.grid1.addWidget(self.current_t,5,2)
        
        
        self.grid1.addWidget(self.loss,6,0)
        self.grid1.addWidget(self.ironbutton,6,1)
        self.input.setLayout(self.grid1)

    def grid3_text(self):
        self.output = QGroupBox("Output:",self)
        self.equ = QVBoxLayout()
        self.output.setLayout(self.equ)
        self.equation = QLabel("Torque\nMechnical Power\nLosses[Fe and Cu]\nEfficient")
        self.equ.addWidget(self.equation)
    
    
    def Box(self):
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.calbutton = QPushButton("Calculate", self)
        self.tablebutton = QPushButton("Create Value Table", self)
        self.plotbutton = QPushButton("Create Efficiency Plot", self)
        self.cancelbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.calbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.tablebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.plotbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.cancelbutton,QDialogButtonBox.ActionRole)
        self.calbutton.clicked.connect(self.cancel)
        
        
        
        
    def open_ironforeff(self):
        command = "widgets\\ironforeff.py"
        subprocess.Popen(command, shell = True)
        
    def cancel(self):
        self.close()
        

        

        

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Eff()
    window.show()
    app.exec_()
    sys.exit(0)