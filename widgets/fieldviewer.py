# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:27:59 2017

@author: DINGNAN
"""

# Field Viewer, only for pos to png file

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.chdir("C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\PMSM1")

class F_Viewer(QWidget):
    def __init__(self,*args,**kwargs):
        super(F_Viewer, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()
    
    def initUI(self):
        self.leftLayout()
        self.rightLayout()
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.buttonbox)
        self.mainLayout.addWidget(self.area)
        self.mainLayout.setStretch(0,1)
        self.mainLayout.setStretch(1,5)
        self.setLayout(self.mainLayout)
        
    def leftLayout(self):
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Vertical)
        self.button1 = QPushButton("Geometry")
        self.button2 = QPushButton("Mesh Geo")
        self.button3 = QPushButton("Boundary")
        self.button4 = QPushButton("Vector Potential")
        self.button5 = QPushButton("B-Field")
        self.button6 = QPushButton("B-radial")
        self.button7 = QPushButton("B-tangent")
        self.button8 = QPushButton("Flux Line")
        self.button9 = QPushButton("Demagnetization")
        self.button10 = QPushButton("Clear")
        self.buttonbox.addButton(self.button1,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button2,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button3,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button4,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button5,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button6,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button7,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button8,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button9,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.button10,QDialogButtonBox.ActionRole)
        self.button1.clicked.connect(self.geometry)
        self.button2.clicked.connect(self.mesh)
        self.button3.clicked.connect(self.boundary)
        self.button4.clicked.connect(self.vp)
        self.button5.clicked.connect(self.bfeld)
        self.button6.clicked.connect(self.b_radial)
        self.button7.clicked.connect(self.b_tangent)
        
    def rightLayout(self):
        self.area = QGroupBox()
        self.right = QVBoxLayout()
        vp = ""
        self.label = QLabel()
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.right.addWidget(self.label)
        self.area.setLayout(self.right)
        
    def geometry(self):
        vp = "pmsm_cbmag.png"
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
    def mesh(self):
        vp = "pmsm_cbmag_msh.png"
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
    
    def boundary(self):
        vp = "bnd.png"
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
    
    def vp(self):
        vp = "az.png"
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
    def bfeld(self):
        vp = "nb.png"
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
    
    def b_radial(self):
        vp = "b_radial.png"
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter) 
        
    def b_tangent(self):
        vp = "b_tangent.png"
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter) 
        
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = F_Viewer()
    window.setGeometry(100, 100, 810, 400)
    window.setWindowTitle('Field Viewer')
    window.show()
    app.exec_()
    sys.exit(0)