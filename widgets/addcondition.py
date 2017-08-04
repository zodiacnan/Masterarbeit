# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:24:07 2017

@author: DINGNAN
"""

#addcondition

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class add_bc(QWidget):
    def __init__(self,parent = None, modal = False):
        super(add_bc, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.setGeometry(300, 300, 400, 600)
        self.GUI()
        
    def GUI(self):
        layout_GUI = QVBoxLayout()
        self.layout1 = QGroupBox('Type')
        self.layout2 = QGroupBox('Equation')
        self.layout3 = QGroupBox('Parameters')
        
        
        self.buttonbox = QDialogButtonBox()
        self.buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.savebutton = QPushButton("OK", self)
        self.returnbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.savebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)

        
        layout_GUI.addWidget(self.layout1)
        layout_GUI.addWidget(self.layout2)
        layout_GUI.addWidget(self.layout3)
        layout_GUI.addWidget(self.buttonbox)
        
        self.nameLabel = QLabel('Name', self)
        self.nameCombo =QLineEdit('')
        self.nameCombo.textChanged.connect(self.Group_2)
        
        self.tip = QLineEdit('')
        self.tip.setText('Dirichlet')
        
        self.type_name = QLabel('Type of BC')
        self.typeCombo = QComboBox(self)
        self.typeList = [self.tr('Magnetic Vektorpotential'), self.tr('Surface Current')]
        self.typeCombo.addItems(self.typeList)
        self.typeCombo.setCurrentIndex(0)
        layout_T = QGridLayout()
        layout_T.addWidget(self.nameLabel,1,0)
        layout_T.addWidget(self.nameCombo, 1, 1)
        
        layout_T.addWidget(self.type_name, 3, 0)
        layout_T.addWidget(self.typeCombo, 3, 1)
        layout_T.addWidget(self.tip, 2, 1)
        self.layout1.setLayout(layout_T)
        self.typeCombo.currentIndexChanged.connect(self.Group_1)
        
        
        self.layout_E = QGridLayout()
        self.E_Label = QLabel('A = 0', self)
        self.layout_E.addWidget(self.E_Label, 1, 0)
        self.layout2.setLayout(self.layout_E)
        
        layout_P = QGridLayout()
        self.ar = QLabel('Ar [Wb/m]',self)
        self.ar_line = QLineEdit('0',self)
        self.jr = QLabel('Jr [A/m]',self)
        self.jr_line = QLineEdit('0', self)
        layout_P.addWidget(self.ar, 1, 0)
        layout_P.addWidget(self.ar_line, 1, 1)
        layout_P.addWidget(self.jr, 2, 0)
        layout_P.addWidget(self.jr_line, 2, 1)
        self.layout3.setLayout(layout_P)
        
        self.setLayout(layout_GUI)
        
        
        self.savebutton.clicked.connect(self.output)
        self.returnbutton.clicked.connect(self.cancel)
    def Group_1(self):
        nr = self.typeCombo.currentIndex()
        if nr == 0:
            currentText = 'A = A0'
        else:
            currentText = 'A...'
        self.E_Label.setText(currentText)
        
    
    def Group_2(self):
        inputofbc = self.nameCombo.text()
        pass
    
        
    def output(self):
        pass
    
    def cancel(self):
        self.close()    

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = add_bc()
    window.setWindowTitle('Boundary Condition')
    window.setGeometry(300,300,300,400)
    window.show()
    app.exec_()