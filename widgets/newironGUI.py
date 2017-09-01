# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:53:14 2017

@author: DINGNAN
"""

#newIron
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
sys.path.append('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\widgets\\')
from LdundLqGUI import *
import LdundLqGUI as dq
class Iron_Set(QWidget):
    def __init__(self,*args,**kwargs):
        super(Iron_Set, self).__init__()
        self.setWindowTitle("Iron Losses - EVALUATION")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()


    def initUI(self):
        self.modulgrip()
        self.text1()
        self.box_equation()
        self.box_comman()
        self.case1()
        self.Box()
        main = QVBoxLayout()
        mainup = QHBoxLayout()
        left = QVBoxLayout()
        right = QVBoxLayout()
        inputmatrix = QVBoxLayout()
        mainup.addLayout(left)
        mainup.addLayout(right)
        mainup.addLayout(inputmatrix)
        left.addWidget(self.box1)
        left.addWidget(self.box_e)
        right.addWidget(self.box_c)
        right.addWidget(self.box2)
        inputmatrix.addWidget(self.casebox1)
        main.addLayout(mainup)
        main.addWidget(self.buttonbox)
        self.setLayout(main)
        
    def modulgrip(self):
        self.box1 = QGroupBox("Calculate Modell")
        modell1 = QPushButton("FEMAG Modell")
        modell1.clicked.connect(self.FEMAG)
        modell2 = QPushButton("Jordan")
        modell2.clicked.connect(self.Jordan)
        modell3 = QPushButton("Bertotti")
        modell3.clicked.connect(self.Bertotti)
        modell4 = QPushButton("Custemor")
        modell4.clicked.connect(self.Customer)
        
        buttongrid = QGridLayout()
        buttongrid.addWidget(modell1,1,0)
        buttongrid.addWidget(modell2,1,1)
        buttongrid.addWidget(modell3,1,2)
        buttongrid.addWidget(modell4,1,3)
        self.box1.setLayout(buttongrid)
        
    def text1(self):
        self.box2 = QGroupBox("Additional Parameters")
        self.box2_child = QVBoxLayout()
        self.textarea = QTextEdit()
        self.box2_child.addWidget(self.textarea)
        self.box2.setLayout(self.box2_child)
    def box_equation(self):
        self.box_e = QGroupBox("Modell Equation")
        self.boxe_child = QVBoxLayout()
        self.textarea2 = QTextEdit()
        self.boxe_child.addWidget(self.textarea2)
        self.box_e.setLayout(self.boxe_child)
    def box_comman(self):
        self.box_c = QGroupBox("Same Parameters")
        self.input = QGridLayout()
        self.frequenz = QLabel("Frequency                          f [Hz]")
        self.frequenz_t = QLineEdit("100")
        self.bfeld = QLabel("B - Induction                      B [T]")
        self.bfeldx = QLabel("     Bx")
        self.bfeldy = QLabel("     By")
        self.bbutton = QPushButton("B-Feld Calculate")
        self.area = QLabel("A - Area of Iron Region            Ae [mm^2]")
        self.areabutton = QPushButton("A - Size Calculation")
        self.h_co = QLabel("Hysteresis-Coefficient           ch [W/kg]",self)
        self.e_co = QLabel("Eddycurrent-Coefficient          cw [W/kg]",self)
        self.h_co_t = QLineEdit("4.000",self)
        self.e_co_t = QLineEdit("2.000",self)
        self.input.addWidget(self.frequenz,1,0)
        self.input.addWidget(self.frequenz_t,1,1)
        self.input.addWidget(self.bfeld,2,0)
        self.input.addWidget(self.bfeldx,3,0)
        self.input.addWidget(self.bfeldy,4,0)
        self.input.addWidget(self.bbutton,2,1)
        self.input.addWidget(self.area,5,0)
        self.input.addWidget(self.areabutton,5,1)
        self.input.addWidget(self.h_co,6,0)
        self.input.addWidget(self.h_co_t,6,1)
        self.input.addWidget(self.e_co,7,0)
        self.input.addWidget(self.e_co_t,7,1)
        self.box_c.setLayout(self.input)
    def case1(self):
        self.casebox1 = QGroupBox("Input Parameters")
        self.grid1 = QGridLayout()
        self.id1 = QLabel("Is_eff [Current]")
        self.id1_s = QLabel("    Min Current  [A]")
        self.id1_e = QLabel("    Max Current  [A]")
        self.id1_u = QLabel("    Current Increment  [A]")
        self.id1_s_t = QLineEdit("10")
        self.id1_e_t = QLineEdit("50")
        self.id1_u_t = QLineEdit("10")
        self.theta = QLabel("Theta[Last]")
        self.theta_s = QLabel("    Theta_min  [deg]")
        self.theta_e = QLabel("    Theta_max  [deg]")
        self.theta_u = QLabel("    PhaseShift Increment  [deg]")
        self.theta_s_t = QLineEdit("0")
        self.theta_e_t = QLineEdit("90")
        self.theta_u_t = QLineEdit("10")
        self.grid1.addWidget(self.id1,1,0)
        self.grid1.addWidget(self.id1_s,2,0)
        self.grid1.addWidget(self.id1_s_t,2,1)
        self.grid1.addWidget(self.id1_e,3,0)
        self.grid1.addWidget(self.id1_e_t,3,1)
        self.grid1.addWidget(self.id1_u,4,0)
        self.grid1.addWidget(self.id1_u_t,4,1)
        self.grid1.addWidget(self.theta,5,0)
        self.grid1.addWidget(self.theta_s,6,0)
        self.grid1.addWidget(self.theta_s_t,6,1)
        self.grid1.addWidget(self.theta_e,7,0)
        self.grid1.addWidget(self.theta_e_t,7,1)
        self.grid1.addWidget(self.theta_u,8,0)
        self.grid1.addWidget(self.theta_u_t,8,1)
        self.casebox1.setLayout(self.grid1)
        
    def Box(self):
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.tablebutton = QPushButton("Calculate", self)
        self.cancelbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.tablebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.cancelbutton,QDialogButtonBox.ActionRole)
    def FEMAG(self):
        self.textarea.clear()
        bf = "Base Frequency :f0 = 50"
        bi = "Base Induction :B0 = 1.5"
        ID = "Iron Density   :rho = 7.86*1e3"
        cu = "Field Factor[>1.7] :cu = 2"
        Ve = "Volumn of Element [Stator/Rotor_Fe Region] : Ve = Ae*Axiallength"
        Ae = "Area of Element [Stator/Rotor_Fe Region] : Calculate Ae from Gmsh"
        equation1= "Pfemag = Sum((ch*(fv/fo)+cw*(fv/fo)^2)*((Bmax/B0)^2)*rho*Ve)*cu"
        self.textarea.append(bf)
        self.textarea.append(bi)
        self.textarea.append(ID)
        self.textarea.append(cu)
        self.textarea.append(Ae)
        self.textarea.append(Ve)
        self.textarea2.setText(equation1)
        
    def Jordan(self):
        self.textarea.clear()
        parameter2 = ""
        equation2= "Pfe = Ph + Pw = Bmax*f*ch + (Bmax^2)*(f^2)*cw"
        self.textarea.setText(parameter2)
        self.textarea2.setText(equation2)
    
    def Bertotti(self):
        self.textarea.clear()
        b = "Material-dependent coefficients: b = "
        cz = "Extra Factor: cz = "
        equation3= "Pfe = Ph + Pw + Pz = ((Bmax)^b)*f*ch + ((Bmax)^2)*(f^2)*cw + (f^1.5)*((Bmax)^1.5)*cz"
        self.textarea.append(b)
        self.textarea.append(cz)
        self.textarea2.setText(equation3)
    
    def Customer(self):
        self.textarea.clear()
        self.textarea2.clear()
        parameter4 = self.textarea.toPlainText()
        equation4 = self.textarea2.toPlainText()
        self.textarea.setPlainText(parameter4)
        with open('ironfunctionfromcustomer.txt', 'a') as f:
            f.writelines(parameter4)
            f.writelines(equation4)
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Iron_Set()
    window.setGeometry(100,100,800,500)
    window.show()
    app.exec_()
    sys.exit(0)