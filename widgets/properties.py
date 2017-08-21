# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 08:21:24 2017

@author: DINGNAN
"""

#properties
import sys
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\widgets')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import subprocess

class Pro_Button(QWidget):
    def __init__(self,*args,**kwargs):
        super(Pro_Button, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.setWindowTitle("Properties")
        self.initUI()


    def initUI(self):
        
        self.group = QGroupBox('')
        self.material = QPushButton('Material')
        self.material.setFixedSize(250,75)
        self.bc = QPushButton('Boundary Condition')
        self.bc.setFixedSize(250,75)
        self.winding = QPushButton('Windings [Stator]')
        self.winding.setFixedSize(250,75)
        self.buttons = QVBoxLayout()
        self.buttons.addWidget(self.material)
        self.buttons.addWidget(self.bc)
        self.buttons.addWidget(self.winding)
        self.group.setLayout(self.buttons) 
        
        layout = QVBoxLayout()
        layout.addWidget(self.group)
        self.setLayout(layout)
        
        self.material.clicked.connect(self.open_materialGUI)
        self.bc.clicked.connect(self.open_bcGUI)
        self.winding.clicked.connect(self.open_windings)
        
    def open_materialGUI(self):
        command = "material.py"
        subprocess.Popen(command, shell = True)
    
    def open_bcGUI(self):
        command = "condition.py"
        subprocess.Popen(command, shell = True)
    
    def open_windings(self):
        command = "winding.py"
        subprocess.Popen(command, shell = True)
        

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Pro_Button()
    window.show()
    app.exec_()
    sys.exit(0)