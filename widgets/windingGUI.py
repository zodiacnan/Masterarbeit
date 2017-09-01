# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:17:52 2017

@author: DINGNAN
"""

#modelling windings

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class Winding(QWidget):
    def __init__(self,*args,**kwargs):
        super(Winding, self).__init__()
        self.setWindowTitle("Winding")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()


    def initUI(self):
        main = QVBoxLayout()
        grid = QGridLayout()
        
        self.fillfact = QLabel("Fill Factor [<=1]")
        self.fact3d = QLabel("Factor of Resistance for 3D Effect")
        self.nur_s = QLabel("[Stator] Number of wires in series per phase")
        self.nur_r = QLabel("[Rotor]  Number of wires in series per phase")
        self.nur_l = QLabel("Number of Layout")
        self.fillfact_t = QLineEdit("0.5")
        self.fact3d_t = QLineEdit("1.5")
        self.nur_l_t = QLineEdit("1")
        self.nur_s_t = QLineEdit("104")
        self.nur_r_t = QLineEdit("0")
        grid.addWidget(self.fillfact,1,0)
        grid.addWidget(self.fillfact_t,1,1)
        grid.addWidget(self.fact3d,2,0)
        grid.addWidget(self.fact3d_t,2,1)
        grid.addWidget(self.nur_l,3,0)
        grid.addWidget(self.nur_l_t,3,1)
        grid.addWidget(self.nur_s,4,0)
        grid.addWidget(self.nur_s_t,4,1)
        grid.addWidget(self.nur_r,5,0)
        grid.addWidget(self.nur_r_t,5,1)
        
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.meshbutton = QPushButton("Load", self)
        self.returnbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.meshbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)
        main.addLayout(grid)
        main.addWidget(self.buttonbox)
        self.setLayout(main)
        

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Winding()
    window.show()
    app.exec_()
    sys.exit(0)