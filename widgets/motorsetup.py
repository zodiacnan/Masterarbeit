# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 11:54:58 2017

@author: DINGNAN
"""

#motor setup
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pickle

class Motor_SetUp(QWidget):
    def __init__(self,*args,**kwargs):
        super(Motor_SetUp, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()
    
    def initUI(self):
        self.left()
        self.right()
        GUIlayout = QVBoxLayout()
        GUIlayout.addWidget(self.leftGUI)
        GUIlayout.addWidget(self.downGUI)
        self.setLayout(GUIlayout)
    
    def left(self):
        self.leftGUI = QGroupBox('Parameters')
        self.downGUI = QGroupBox()
        self.NPIM = QLabel('Number of Poles in Model')
        self.NPIM_nr = QLineEdit('1')
        self.IRA = QLabel('Initial Rotor Angel [deg]')
        self.IRA_text = QLineEdit('0')
        self.NPT = QLabel('[Rotor] Number of poles in cross-section')
        self.NPT_nr = QLineEdit('8')
        self.NST = QLabel('[Rotor] Number of rotor teeth')
        self.NST_nr = QLineEdit('8')   
        
        self.SymFactor = QLabel('[Rotor] SymmetryFactor', self)
        self.SymFactor_text = QLineEdit('8')
        self.NSTS = QLabel('[Stator] Number of stator teeth')
        self.NSTS_nr = QLineEdit('24')
        
        self.axial = QLabel('Axial length [mm]')
        self.axial_nr = QLineEdit('40')
        self.gap = QLabel('Airgap width [mm]')
        self.gap_nr = QLineEdit('0.55')
        self.NP = QLabel('Number of Phase')
        self.NP_nr = QLineEdit('3')
        
        self.buttonbox = QDialogButtonBox()
        self.buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.savebutton = QPushButton("Save", self)
        self.returnbutton = QPushButton("Return", self)
        self.showbutton = QPushButton("View Geometry in Gmsh", self)
        self.buttonbox.addButton(self.savebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.showbutton,QDialogButtonBox.ActionRole)
        
        self.leftgrid = QGridLayout()
        self.leftgrid.addWidget(self.NPIM, 1, 0)
        self.leftgrid.addWidget(self.NPIM_nr, 1, 1)
        self.leftgrid.addWidget(self.IRA, 2, 0)
        self.leftgrid.addWidget(self.IRA_text, 2, 1)
        self.leftgrid.addWidget(self.NPT, 3, 0)
        self.leftgrid.addWidget(self.NPT_nr, 3, 1)
        self.leftgrid.addWidget(self.SymFactor, 9, 0)
        self.leftgrid.addWidget(self.SymFactor_text, 9, 1)
        self.leftgrid.addWidget(self.NST, 4, 0)
        self.leftgrid.addWidget(self.NST_nr, 4, 1)
        self.leftgrid.addWidget(self.NSTS, 5, 0)
        self.leftgrid.addWidget(self.NSTS_nr, 5, 1)
        self.leftgrid.addWidget(self.axial, 6, 0)
        self.leftgrid.addWidget(self.axial_nr, 6, 1)
        self.leftgrid.addWidget(self.gap, 7, 0)
        self.leftgrid.addWidget(self.gap_nr, 7, 1)
        self.leftgrid.addWidget(self.NP, 8, 0)
        self.leftgrid.addWidget(self.NP_nr, 8, 1)
        self.leftgrid.setRowStretch(1, 8)
        self.leftGUI.setLayout(self.leftgrid)
        self.NPT_nr.textChanged.connect(self.change_1)
        self.NPT_nr.textChanged.connect(self.change_2)
        self.NPIM_nr.textChanged.connect(self.change_2)
        
        self.downlayout = QFormLayout()
        self.downlayout.addWidget(self.buttonbox)
        self.downGUI.setLayout(self.downlayout)
        self.showbutton.clicked.connect(self.show_geo)
        self.savebutton.clicked.connect(self.store_temp)
        
    def right(self):
        self.rightGUI = QLabel()
        pass
        
    def change_1(self):
        nptnr = int(self.NPT_nr.text())
        nstnr = nptnr
        self.NST_nr.setText(str(nstnr))
        
    def change_2(self):
        npim = float(str(self.NPIM_nr.text()))
        nptnr = float(str(self.NPT_nr.text()))
        sf = float(nptnr/npim)
        self.SymFactor_text.setText(str(sf))
    def show_geo(self):
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
        import subprocess
        filename = "moduls\\PMSM1\\geo.pos"
        command = "gmsh.exe "+ filename
        subprocess.Popen(command, shell = False)
        pass
    
    def store_temp(self):
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
        try:
            fp = open("temptoUI.pkl",'r')
            shared = pickle.load(fp)
            fp.close()
            shared.extend([str(self.NSTS_nr.text()),str(self.NST_nr.text()),str(self.gap_nr.text())])
            fp = open("temptoUI.pkl",'w')
            pickle.dump(shared,fp)
            print(shared)
            fp.close()

        except:
            print("No load")
            
        
        
        
    

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Motor_SetUp()
    window.setGeometry(100, 100, 600, 600)
    window.setWindowTitle('Field Calculation')
    window.show()
    app.exec_()
    sys.exit(0)