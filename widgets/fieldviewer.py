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

class F_Viewer(QWidget):
    def __init__(self,*args,**kwargs):
        super(F_Viewer, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()
    
    def initUI(self):
        self.leftLayout()
        self.rightLayout()
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.left)
        self.mainLayout.addLayout(self.right)
        self.mainLayout.setStretch(0,1)
        self.mainLayout.setStretch(1,5)
        
        self.setLayout(self.mainLayout)
        
    def leftLayout(self):
        self.left = QGridLayout()
        button1 = QPushButton("Geometry")
        button2 = QPushButton("Mesh Geo")
        button3 = QPushButton("Boundary")
        button4 = QPushButton("Vector Potential")
        button5 = QPushButton("B-Field")
        button6 = QPushButton("B-radial")
        button7 = QPushButton("B-tangent")
        button8 = QPushButton("Flux Line")
        button9 = QPushButton("Demagnetization")
        button10 = QPushButton("Clear")
        
        self.left.addWidget(button1)
        self.left.addWidget(button2)
        self.left.addWidget(button3)
        self.left.addWidget(button4)
        self.left.addWidget(button5)
        self.left.addWidget(button6)
        self.left.addWidget(button7)
        self.left.addWidget(button8)
        self.left.addWidget(button9)
        self.left.addWidget(button10)
        
    def rightLayout(self):
        self.right = QVBoxLayout()
        os.chdir("D:\\Onelab\\machines\\res\\")
        vp = "az.png"
        self.label = QLabel()
        self.label.setPixmap(QPixmap(vp))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.right.addWidget(self.label)

        
        
        
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = F_Viewer()
    window.setGeometry(100, 100, 800, 640)
    window.setWindowTitle('Field Viewer')
    window.show()
    app.exec_()
    sys.exit(0)