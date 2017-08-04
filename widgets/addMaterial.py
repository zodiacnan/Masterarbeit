# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:23:38 2017

@author: DINGNAN
"""

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
sys.path.append('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\moduls\\Material\\')
import subprocess

class Add_Material(QWidget):
    def __init__(self,*args,**kwargs):
        super(Add_Material, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.setGeometry(300, 300, 600, 800)
        self.GUI()
    def GUI(self):
        layout_GUI = QVBoxLayout()
        self.layout1 = QGridLayout()
        self.layout2 = QGroupBox('Linear Properties')
        self.layout3 = QGroupBox('Nonlinear Properties')
        self.layout3.setEnabled(False)
        self.layout5 = QGroupBox('Lamination')
        self.buttonbox = QDialogButtonBox()
        self.buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.savebutton = QPushButton("Save", self)
        self.returnbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.savebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)
        
        
        layout_GUI.addLayout(self.layout1)
        layout_GUI.addWidget(self.layout2)
        layout_GUI.addWidget(self.layout3)
        layout_GUI.addWidget(self.layout5)
        layout_GUI.addWidget(self.buttonbox)
        
        self.nameLabel = QLabel('  Name', self)
        self.name = QLineEdit('', self)
        self.bh_curve = QLabel('  B-H Curve', self)
        self.bh_box = QComboBox(self)
        self.bh_boxlist = [self.tr('Linear B-H Relationship'), self.tr('Nonlinear B-H Curve')]
        self.bh_box.addItems(self.bh_boxlist)
        self.bh_box.setCurrentIndex(0)
        
        self.layout1.addWidget(self.nameLabel,1,0)
        self.layout1.addWidget(self.name, 1, 1)
        self.layout1.addWidget(self.bh_curve,2,0)
        self.layout1.addWidget(self.bh_box, 2, 1)
        
        
        self.mur = QLabel('Relativ Permeability μ[r]')
        self.mur_text = QLineEdit('')
        self.mur0 = QLabel('Air Permeability     μ[0]')
        self.mur0_text = QLineEdit('4π*10e-7')
        layout2_child = QGridLayout()
        layout2_child.addWidget(self.mur, 1, 0)
        layout2_child.addWidget(self.mur_text, 1, 1)
        layout2_child.addWidget(self.mur0, 2, 0)
        layout2_child.addWidget(self.mur0_text, 2, 1)
        self.layout2.setLayout(layout2_child)
        
        self.chooseLabel = QLabel('Type of B-H Curve')
        self.curveButton = QComboBox()
        self.curvelist = [self.tr('Analytical'), self.tr('Interpolated'), self.tr('Analytical VH800-65D'), self.tr('Interpolated VH800-65D'),]
        self.curveButton.addItems(self.curvelist)
        self.curveButton.setCurrentIndex(0)
        self.b_r = QLabel("Br[Remanence]-[T]",self)
        self.b_r_text = QLineEdit("1.2",self)
        self.showButton = QPushButton('Plot Curve')
        self.addcurve = QPushButton('Load new B-H Curve')
        
        layout3_child = QGridLayout()
        layout3_child.addWidget(self.chooseLabel, 1, 0)
        layout3_child.addWidget(self.curveButton, 1, 1)
        layout3_child.addWidget(self.b_r, 2, 0)
        layout3_child.addWidget(self.b_r_text, 2, 1)
        layout3_child.addWidget(self.showButton, 3, 1)
        layout3_child.addWidget(self.addcurve, 4, 1)
        self.layout3.setLayout(layout3_child)
        
        self.laminationButton = QComboBox()
        self.laminationButton_list = [self.tr('Not Laminated'), self.tr('Laminated in plane'),]
        self.laminationButton.addItems(self.laminationButton_list)
        self.laminationButton.setCurrentIndex(0)
        self.sigma = QLabel('[σ]     ')
        self.sigma_text = QLineEdit('0')
        layout5_child = QGridLayout()
        layout5_child.addWidget(self.laminationButton, 1, 0, 1, 0)
        layout5_child.addWidget(self.sigma, 2, 0)
        layout5_child.addWidget(self.sigma_text, 2, 1)
        self.layout5.setLayout(layout5_child)
        self.setLayout(layout_GUI)
        
        self.bh_box.currentIndexChanged.connect(self.Group_1)
        
        self.savebutton.clicked.connect(self.output)
        self.returnbutton.clicked.connect(self.cancel)
    
    def cancel(self):
        self.close()
        
    def Group_1(self):
        bh_index = self.bh_box.currentIndex()
        if bh_index == 0:
            self.layout2.setEnabled(True)
            self.layout3.setEnabled(False)
        else:
            self.layout3.setEnabled(True)
            self.layout2.setEnabled(False)
        #linear properties
    def Group_2(self):
        #nolinear properties
        pass
    
    def output(self):
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\moduls\\Material\\')
        name = str(self.name.text())
        nr_bh = self.bh_box.currentIndex()
        if nr_bh == 0:
            air = "mu0 = 4.e-7*Pi ; \n"
            r = str(self.mur_text.text())
            mu_r =  "mur" + name + " = " + r + ";\n"
            add1 = [air, r ,mu_r]
        else:
            br = str(self.b_r_text.text())
            flag = self.curveButton.currentIndex()
            add1 = [br]
        sigma = str(self.sigma_text.text())
        sigma_i = "sigma" + name + " = " + sigma + ";\n"
        add2 = [sigma_i]
        if name == "":
            print("Input the filename of new Material")
            return
        filename = name + '.pro'
        try: 
            file = open(filename, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        f = open(filename, 'w+')
        f.writelines(add1)
        f.writelines(add2)
        f.close()
        print("finish")
        
    
        
    
    def edit_curve(self):
        pass
    
    

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Add_Material()
    window.setWindowTitle('Material')
    window.setGeometry(300,300,400,600)
    window.show()
    app.exec_()
    sys.exit(0)