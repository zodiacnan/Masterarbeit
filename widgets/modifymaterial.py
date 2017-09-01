# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 21:18:54 2017

@author: DINGNAN
"""
import sys
import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Motify_M(QWidget):
    def __init__(self,parent = None, modal = False):
        super(Motify_M, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.setGeometry(300, 300, 400, 600)
        self.GUI()
    def GUI(self):
        self.main = QHBoxLayout()
        layout_GUI = QVBoxLayout()
        self.layouta = QGridLayout()
        self.layoutb = QGroupBox('Linear Properties')
        self.layoutc = QGroupBox('Nonlinear Properties')
        self.layoutd = QGroupBox('BH-Plot')
        self.layoutd.hide()
        self.layoutc.setEnabled(False)
        self.layoute = QGroupBox('Lamination')
        
        
        self.b_t = QLabel('Remanent induction [T]')
        self.b_t_text = QLineEdit('1.2')
        
        self.buttonbox = QDialogButtonBox()
        self.buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.savebutton = QPushButton("OK", self)
        self.returnbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.savebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)

        
        layout_GUI.addLayout(self.layouta)
        layout_GUI.addWidget(self.layoutb)
        layout_GUI.addWidget(self.layoutc)
        layout_GUI.addWidget(self.layoute)
        layout_GUI.addWidget(self.buttonbox)
        
        self.nameLabel = QLabel('  Name', self)
        self.name = QComboBox(self)
        self.name_list = [self.tr('Fe - [Blech]'), self.tr('Air - [Gaps]'), self.tr('Chopper - [Coil]'),self.tr('Aluminum')]
        self.name.addItems(self.name_list)
        self.bh_curve = QLabel('  B-H Curve', self)
        self.bh_box = QComboBox(self)
        self.bh_boxlist = [self.tr('Linear B-H Relationship'), self.tr('Nonlinear B-H Curve')]
        self.bh_box.addItems(self.bh_boxlist)
        self.bh_box.setCurrentIndex(0)
        
        self.layouta.addWidget(self.nameLabel,1,0)
        self.layouta.addWidget(self.name, 1, 1)
        self.layouta.addWidget(self.bh_curve,2,0)
        self.layouta.addWidget(self.bh_box, 2, 1)
        
        self.name.currentIndexChanged.connect(self.change_1)
        self.name.currentIndexChanged.connect(self.change_2)
        
        
        self.mur = QLabel('Relativ Permeability μ[r]')
        self.mur_text = QLineEdit('1000')
        self.mur0 = QLabel('Air Permeability     μ[0]')
        self.mur0_text = QLineEdit('4π*10e-7')
        layoutb_child = QGridLayout()
        layoutb_child.addWidget(self.mur, 1, 0)
        layoutb_child.addWidget(self.mur_text, 1, 1)
        layoutb_child.addWidget(self.mur0, 2, 0)
        layoutb_child.addWidget(self.mur0_text, 2, 1)
        self.layoutb.setLayout(layoutb_child)
        
        self.chooseLabel = QLabel('Type of Magnetic Material')
        self.curveButton = QComboBox()
        self.curvelist = [self.tr('From Equation'), self.tr('[Interpolated]'),self.tr('[Interpolated] TK_270-50_PP'),
                          self.tr('[Interpolated] TK_530-50_AP'),self.tr('[Interpolated] TKES_270-50_PP'),
                          self.tr('[Interpolated] TKES_330-35_A'),self.tr('[Interpolated] TKES_330-50_A'),
                          self.tr('[Interpolated] TKES_330-50_PP'),self.tr('[Interpolated] TKES_400-50_A'),]
        self.curveButton.addItems(self.curvelist)
        self.curveButton.setCurrentIndex(0)
        
        self.b_r = QLabel("Br[Remanence]-[T]",self)
        self.b_r_text = QLineEdit("1.2",self)
        
        self.showButton = QPushButton('Plot Curve')
        self.addcurve = QPushButton('Load new B-H Curve')
        self.load = QPushButton("Load B-H Data")
        
        layoutc_child = QGridLayout()
        layoutc_child.addWidget(self.chooseLabel, 1, 0)
        layoutc_child.addWidget(self.curveButton, 1, 1)
        layoutc_child.addWidget(self.b_r, 2, 0)
        layoutc_child.addWidget(self.b_r_text, 2, 1)
        layoutc_child.addWidget(self.showButton, 3, 1)
        layoutc_child.addWidget(self.addcurve, 4, 1)
        layoutc_child.addWidget(self.load, 5, 1)
        self.layoutc.setLayout(layoutc_child)
        
        
        self.laminationButton = QComboBox()
        self.laminationButton_list = [self.tr('Laminated in plane'), self.tr('Not Laminated'),]
        self.laminationButton.addItems(self.laminationButton_list)
        self.laminationButton.setCurrentIndex(0)
        self.sigma = QLabel('[σ] Conductivity [S/m]')
        self.sigma_text = QLineEdit('0')
        self.laminationButton.currentIndexChanged.connect(self.change_2)
        layoute_child = QGridLayout()
        layoute_child.addWidget(self.laminationButton, 1, 0, 1, 0)
        layoute_child.addWidget(self.sigma, 2, 0)
        layoute_child.addWidget(self.sigma_text, 2, 1)
        self.layoute.setLayout(layoute_child)
        self.main.addLayout(layout_GUI)
        self.main.addWidget(self.layoutd)
        self.setLayout(self.main)
        
        self.curveButton.currentIndexChanged.connect(self.plot_curve)
        self.showButton.clicked.connect(self.plot_button)
        self.load.clicked.connect(self.loadbhdata)
        self.bh_box.currentIndexChanged.connect(self.Group_1)
        self.savebutton.clicked.connect(self.output)
        
    def change_1(self):
        nr = self.name.currentIndex()
        if nr == 0:
            text = '1000'
        else:
            text = '1'
        self.mur_text.setText(text)
        
    def change_2(self):
        index = self.name.currentIndex()
        index_sigma = self.laminationButton.currentIndex()
        if index_sigma == 1:
            if index == 0:
                sigma = '10e7'
            if index == 1:
                sigma = '0'
            if index == 2:
                sigma = '5.9e7'
            if index == 3:
                sigma = '3.72e7'
        else:
            sigma = '0'
        self.sigma_text.setText(sigma)
            

    def Group_1(self):
        bh_index = self.bh_box.currentIndex()
        nr= self.name.currentIndex()
        if bh_index == 1 and nr == 0:
            self.layoutc.setEnabled(True)
            self.layoutb.setEnabled(False)
        else:
            self.layoutb.setEnabled(True)
            self.layoutc.setEnabled(False)


    def loadbhdata(self):
        typ = self.curveButton.currentIndex()
        if typ == 0:
            pass
        if typ == 2:
            subname = "TK_270-50_PP.txt"
        if typ == 3:
            subname = "TK_530-50_AP.txt"
        
        filename = "moduls\\B(H)curve\\"+subname
        
        with open(filename,"r") as fig:
            B = []
            H = []
            for line in fig:
                data = line.split()
                H.append((data[0]))
                B.append(float(data[1]))
        mathb = "Mat1_b = {"+str(B)+"};\n"
        mathh = "Mat1_h = {"+str(H)+"};\n"
        print mathb
        print mathh
        
        bhtxt = 'moduls\\B(H)curve\\BH_data.pro'
        try: 
            file = open(bhtxt, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        f1 = open(bhtxt, 'w+')
        add_content = [mathh,mathb]
        f1.writelines(add_content)
        f1.close()
    def plot_curve(self):
        pass
            
    def plot_button(self):
        pic = "moduls\\B(H)curve\\Interpoleted.jpg"
        area = QVBoxLayout()
        self.Grid = QLabel(self)
        self.Grid.setPixmap(QPixmap(pic))
        self.Grid.setAlignment(QtCore.Qt.AlignCenter)
        area.addWidget(self.Grid)
        self.layoutd.setLayout(area)
        self.layoutd.show()
    
    
    def output(self):
        nr = self.name.currentIndex()
        if nr == 0:
            name = "Fe"
            id1 = "mur_fe"
            id2 = "sigma_fe"
        elif nr == 1:
            name = "Air"
            
        elif nr == 2:
            name = "Cu"
            id1 = "mur_cu"
            id2 = "sigma_cu"
        elif nr == 3:
            name = "Al"
            id1 = "mur_al"
            id2 = "sigma_al"
        
        bh_index = self.bh_box.currentIndex()
        if bh_index == 1 and nr == 0:
            typ_nr = self.curveButton.currentIndex()
            br = self.b_r_text.text()
            br_i = "b_remanent = " + br + ";\n"
            FN = 'Flag_NL = 1 ; \n'
            m_id1 = ""
            m_id2 = ""
            m_id3 = "mu0 = 4.e-7 * Pi ; "
            if typ_nr == 0:
                print("Analytical")
                FNLLT = 'Flag_NL_law_Type = 0 ; \n'
            elif typ_nr == 1:
                print("Integrated")
                FNLLT = 'Flag_NL_law_Type = 1 ; \n'
            elif typ_nr == 2:
                print("Analytical VH800-65D")
                FNLLT = 'Flag_NL_law_Type = 2 ; \n'
            elif typ_nr == 3:
                print("Interpolated VH800-65D")
                FNLLT = 'Flag_NL_law_Type = 3 ; \n'
        else:
            mur_r = str(self.mur_text.text())
            sigma = str(self.sigma_text.text())
            m_id1 = id1+"="+mur_r+";\n"
            m_id2 = id2+"="+sigma+";\n"
            m_id3 = "mu0 = 4.e-7 * Pi ; "
            br_i = ""
            FN = "Flag_NL = 0 ; \n"
            FNLLT = ""
        
        add = [m_id1,m_id2,m_id3, br_i, FN, FNLLT]
        
        filename = name + '.pro'
        try: 
            file = open(filename, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        f = open(filename, 'w+')
        f.writelines(add)

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Motify_M()
    window.setWindowTitle('Material')
    window.show()
    app.exec_()
    sys.exit(0)