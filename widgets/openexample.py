# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:32:02 2017

@author: DINGNAN
"""

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess
import sys
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')

class open_motor(QWidget):
    def __init__(self,parent = None, modal = False):
        super(open_motor, self).__init__()
        self.initUI()
    
    def initUI(self):  
        self.motor_type()
        self.motor_info()
        self.ok_and_cancel()
        mainLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()
        hboxLayout.addLayout(self.motor_type_win)
        hboxLayout.addWidget(self.motor_info_win)
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.box)
        self.setLayout(mainLayout)
        
        
        
        
    def motor_type(self):
        self.tree_1()
        self.tree_2()
        self.motor_type_win = QVBoxLayout()
        self.motor_type_win.addWidget(self.tree1)
        self.motor_type_win.addWidget(self.tree2)
        
        
        
        
    def tree_1(self):
        self.tree1 = QTreeWidget()
        self.tree1.setHeaderHidden(True)
        #self.tree1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree1.setMaximumWidth(250)
        self.tree1.setItemsExpandable(True)
        stator = QTreeWidgetItem(self.tree1, ['Stator'])
        self.stator1 = QTreeWidgetItem(stator, ["Stator1"])
        self.stator2 = QTreeWidgetItem(stator, ["Stator2"])
        self.stator3 = QTreeWidgetItem(stator, ["Stator [WFSM]"])
        self.tree1.expandAll()
        self.tree1.itemSelectionChanged.connect(self.change_pic_s)
    
    def tree_2(self):
        self.tree2 = QTreeWidget()
        self.tree2.setHeaderHidden(True)
        #self.tree2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree2.setMaximumWidth(250)
        self.tree2.setItemsExpandable(True)
        rotor = QTreeWidgetItem(self.tree2, ['Rotor'])
        self.rotor1 = QTreeWidgetItem(rotor, ["Rotor1"])
        self.rotor2 = QTreeWidgetItem(rotor, ["Rotor2"])
        self.rotor3 = QTreeWidgetItem(rotor, ["Rotor [WFSM]"])
        self.tree2.expandAll()
        self.tree2.itemSelectionChanged.connect(self.change_pic_r)
  
    def motor_info(self):
        pic_s = 'moduls\\icon\\Stator1.jpg'
        pic_r = 'moduls\\icon\\Rotor1.jpg'
        
        self.motor_info_win = QGroupBox("Layout")
        self.label_1 = QLabel()
        self.label_2 = QLabel()
        self.label_1.setPixmap(QPixmap(pic_s))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)  
        self.label_2.setPixmap(QPixmap(pic_r))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter) 

        layout = QVBoxLayout()
        splitter = QSplitter(QtCore.Qt.Vertical)
        splitter.addWidget(self.label_1)
        splitter.addWidget(self.label_2)
        layout.addWidget(splitter)
        self.motor_info_win.setLayout(layout)
        return
        
    def change_pic_s(self):
        if self.stator1.isSelected():
            pic_s = "moduls\\icon\\Stator1.jpg"
            self.label_1.setPixmap(QPixmap(pic_s))
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        if self.stator2.isSelected():
            pic_s = "moduls\\icon\\Stator2.jpg"
            self.label_1.setPixmap(QPixmap(pic_s))
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        if self.stator3.isSelected():
            pic_s = "moduls\\icon\\Stator_wf.jpg"
            self.label_1.setPixmap(QPixmap(pic_s))
            self.label_1.setAlignment(QtCore.Qt.AlignCenter)  
        return

    def change_pic_r(self):
        if self.rotor1.isSelected():
            pic_r = "moduls\\icon\\Rotor1.jpg"
            self.label_2.setPixmap(QPixmap(pic_r))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        if self.rotor2.isSelected():
            pic_r = "moduls\\icon\\Rotor2.jpg"
            self.label_2.setPixmap(QPixmap(pic_r))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        if self.rotor3.isSelected():
            pic_r = "moduls\\icon\\Rotor_wf.jpg"
            self.label_2.setPixmap(QPixmap(pic_r))
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        return
    def ok_and_cancel(self):
        self.box = QDialogButtonBox()
        self.box = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.save = QPushButton("Dimension", self)
        self.returnb = QPushButton("Return", self)
        self.box.addButton(self.save, QDialogButtonBox.ActionRole)
        self.box.addButton(self.returnb, QDialogButtonBox.ActionRole)
        self.save.clicked.connect(self.open_MD)
        self.returnb.clicked.connect(self.cancel_button)
        
    def open_MD(self):
        if self.stator1.isSelected() and self.rotor1.isSelected():
            print("geo.pos")
            print("msh.pos")
            command = "widgets\\motordata.py"
            subprocess.Popen(command, shell = True)
        elif self.stator2.isSelected() and self.rotor2.isSelected():
            command = "widgets\\motordata2.py"
            subprocess.Popen(command, shell = True)
        elif self.stator3.isSelected() and self.rotor3.isSelected():
            command = "motordata.py"
            subprocess.Popen(command, shell = True)
        else:
            print("Stator and rotor may not suit")

    def cancel_button(self):
        self.close()

if __name__=="__main__":    
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
        app.aboutToQuit.connect(app.deleteLater)
    ex = open_motor()
    ex.setGeometry(250,150,800,800)
    ex.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
    ex.setWindowTitle("Examples")
    ex.show()
    app.exec_()
