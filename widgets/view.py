# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:54:44 2017

@author: DINGNAN
"""

import sys
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess

class ViewGUI(QWidget):
    def __init__(self,*args,**kwargs):
        super(ViewGUI, self).__init__()
        self.setWindowTitle("Result Viewer")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()


    def initUI(self):
        main = QVBoxLayout()
        font = QFont("Roman times",10,QFont.Bold)
        self.l1 = QLabel("Fast Calculation")
        self.l1.setFont(font)
        self.button1 = QPushButton("Create Results in HTML")
        self.open1 = QPushButton("Open")
        self.open1.clicked.connect(self.fast_open)
        self.l2 = QLabel("MultiCalculation")
        self.l2.setFont(font)
        self.l21 = QPushButton("Create Value Tabel")
        self.l211 = QPushButton("Convert to HTML")
        self.l212 = QPushButton("Open")
        self.l22 = QPushButton("Create Plot")
        self.l221 = QPushButton("Convert to HTML")
        self.l222 = QPushButton("Open")
        self.l23 = QPushButton("Field Viewer")
        self.l23.clicked.connect(self.field_viewer)
        
        gridview = QGridLayout()
        gridview.addWidget(self.l1,1,0)
        gridview.addWidget(self.button1,1,1,1,2)
        gridview.addWidget(self.open1,1,3)
        gridview.addWidget(self.l2,2,0)
        gridview.addWidget(self.l21,2,1)
        gridview.addWidget(self.l211,2,2)
        gridview.addWidget(self.l212,2,3)
        
        gridview.addWidget(self.l22,3,1)
        gridview.addWidget(self.l221,3,2)
        gridview.addWidget(self.l222,3,3)
        
        gridview.addWidget(self.l23,4,1)
        main.addLayout(gridview)
        
        hbox = QHBoxLayout()
        self.label = QLabel("Save all results as")
        self.line = QLineEdit("Motor1")
        self.toolbutton = QPushButton()
        self.toolbutton.setText("Save")
        self.toolbutton2 = QToolButton()
        self.toolbutton2.setText("Restart")
        self.toolbutton2.setFixedSize(92,30)
        hbox.addWidget(self.label)
        hbox.addWidget(self.line)
        hbox.addWidget(self.toolbutton)
        hbox.addWidget(self.toolbutton2)
        main.addLayout(hbox)
        self.setLayout(main)    

    def fast_open(self):
        import webbrowser
        webbrowser.open('moduls\\results\\LdandLq.html')
        
    def field_viewer(self):
        command = "widgets\\fieldviewer.py"
        subprocess.Popen(command, shell = True)
        
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = ViewGUI()
    window.show()
    app.exec_()
    sys.exit(0)