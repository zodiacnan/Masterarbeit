# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:05:32 2017

@author: DINGNAN
"""

#Field Calculation Solver
# this py will create a pro file, analysis.pro, which can be included by pmsm.pro 

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess
import pickle
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')

class Solver_Cal(QWidget):
    def __init__(self,*args,**kwargs):
        super(Solver_Cal, self).__init__()
        self.setWindowIcon(QIcon('icon\main.jpg'))
        self.initUI()
    
    def initUI(self):
        self.createGridGroupBox()
        self.creatVboxGroupBox()
        self.creatFormGroupBox()
        mainLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()
        vLayout = QVBoxLayout()
        hboxLayout.addWidget(self.gridGroupBox)
        hboxLayout.addLayout(vLayout)
        vLayout.addWidget(self.tree1)
        vLayout.addWidget(self.tree2)
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)
        
    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Solver Setup")
        self.gridGroupBox.setMaximumWidth(450)
        self.content_createGridGroupBox()
        layout = QGridLayout()
        layout.addWidget(self.cb_nl, 1, 0)
        layout.addWidget(self.cmb_NLLaw, 1, 1)
        layout.addWidget(self.nb_iter, 3, 0)
        layout.addWidget(self.nb_iter_text, 3, 1)
        layout.addWidget(self.re_fact, 4, 0)
        layout.addWidget(self.re_fact_text, 4, 1)
        layout.addWidget(self.stop_cri, 5, 0)
        layout.addWidget(self.stop_cri_text, 5, 1)
        layout.addWidget(self.ab_t, 6, 0)
        layout.addWidget(self.ab_text, 6, 1)
        layout.addWidget(self.re_t, 7 ,0)
        layout.addWidget(self.re_text, 7,1)
        layout.setRowStretch(1, 8)
        self.gridGroupBox.setLayout(layout)
        
        self.cb_nl.stateChanged.connect(self.NL_state)
        
        
        
    def creatVboxGroupBox(self):
        
        self.tree1 = QTreeWidget()
        self.tree1.setMinimumWidth(400)
        self.tree1.setHeaderLabel("Fast Calculation ")
        
        self.tree2 = QTreeWidget()
        self.tree2.setMinimumWidth(400)
        self.tree2.setHeaderLabel("Motor Calculate Functions")
        
        self.item0 = QTreeWidgetItem(self.tree1, ["[Functions]"])
        self.item0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        
        self.item00 = QTreeWidgetItem(self.item0, ["Iron Losses"])
        self.item00.setCheckState(0, QtCore.Qt.Unchecked)
        self.item00.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.item01 = QTreeWidgetItem(self.item0,["Ld-Lq Identification"])
        self.item01.setCheckState(0, QtCore.Qt.Unchecked)
        self.item02 = QTreeWidgetItem(self.item0,["Psid-Psiq Identification"])
        self.item02.setCheckState(0, QtCore.Qt.Unchecked)
        self.item03 = QTreeWidgetItem(self.item0, ["Efficience Feld"])
        self.item03.setCheckState(0, QtCore.Qt.Unchecked)
        self.item04 = QTreeWidgetItem(self.item0, ["Angle [Up/U] at maximal Torque"])
        self.item04.setCheckState(0, QtCore.Qt.Unchecked)
        
        self.item1 = QTreeWidgetItem(self.tree2, ["[Multiple Calculation-PMSM]"])
        self.item1.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
        self.item11 = QTreeWidgetItem(self.item1, ["Plots"])
        self.item111 = QTreeWidgetItem(self.item11, ["Voltage"])
        self.item111.setCheckState(0, QtCore.Qt.Unchecked)
        self.item112 = QTreeWidgetItem(self.item11,["Torque"])
        self.item112.setCheckState(0, QtCore.Qt.Unchecked)
        self.item113 = QTreeWidgetItem(self.item11, ["Flux Linkage"])
        self.item113.setCheckState(0, QtCore.Qt.Unchecked)
        self.item114 = QTreeWidgetItem(self.item11, ["Current"])
        self.item114.setCheckState(0, QtCore.Qt.Unchecked)
        
        self.item12 = QTreeWidgetItem(self.item1, ["Fields"])
        self.item121 = QTreeWidgetItem(self.item12, ["B - Induction [T]"])
        self.item121.setCheckState(0, QtCore.Qt.Unchecked)
        self.item122 = QTreeWidgetItem(self.item12, ["Vektor Potential"])
        self.item122.setCheckState(0, QtCore.Qt.Unchecked)
        self.item123 = QTreeWidgetItem(self.item12, ["H - Field Strength [kA/m]"])
        self.item123.setCheckState(0, QtCore.Qt.Unchecked)
        self.item124 = QTreeWidgetItem(self.item12, ["Current in Windings"])
        self.item124.setCheckState(0, QtCore.Qt.Unchecked)
        
        self.item13 = QTreeWidgetItem(self.item1, ["Values"])
        self.item132 = QTreeWidgetItem(self.item13, ["Ld/Lq"])
        self.item132.setCheckState(0, QtCore.Qt.Unchecked)
        self.item133 = QTreeWidgetItem(self.item13, ["Psi_d/Psi_q"])
        self.item133.setCheckState(0, QtCore.Qt.Unchecked)
        self.item134 = QTreeWidgetItem(self.item13, ["Voltage"])
        self.item134.setCheckState(0, QtCore.Qt.Unchecked)
        self.item135 = QTreeWidgetItem(self.item13,["Torque"])
        self.item135.setCheckState(0, QtCore.Qt.Unchecked)
        self.item136 = QTreeWidgetItem(self.item13,["Angel - Up/U"])
        self.item136.setCheckState(0, QtCore.Qt.Unchecked)
        self.item2 = QTreeWidgetItem(self.tree2, ["[Multiple Calculation- Wound Rotor SM]"])
        
        self.tree1.expandAll()
        self.tree2.expandAll()
        #self.tree.itemClicked.connect(self.find_checked)
        self.tree1.itemClicked.connect(self.handleItemChanged)
        self.tree2.itemClicked.connect(self.handleItemChanged)
        
    def handleItemChanged(self):
        Fast = []
        Plot = []
        Field = []
        Values = []
        if self.item00.checkState(0) == QtCore.Qt.Checked:
            a0 = str(self.item00.text(0))
            Fast.append(a0)
        if self.item01.checkState(0) == QtCore.Qt.Checked:
            a1 = str(self.item01.text(0))
            Fast.append(a1)
        if self.item02.checkState(0) == QtCore.Qt.Checked:
            a2 = str(self.item02.text(0))
            Fast.append(a2)
        if self.item03.checkState(0) == QtCore.Qt.Checked:
            a3 = str(self.item03.text(0))
            Fast.append(a3)
        if self.item111.checkState(0) == QtCore.Qt.Checked:
            a111 = str(self.item111.text(0))
            Plot.append(a111)
        if self.item112.checkState(0) == QtCore.Qt.Checked:
            a112 = str(self.item112.text(0))
            Plot.append(a112)
        if self.item113.checkState(0) == QtCore.Qt.Checked:
            a113 = str(self.item113.text(0))
            Plot.append(a113)
        if self.item114.checkState(0) == QtCore.Qt.Checked:
            a114 = str(self.item114.text(0))
            Plot.append(a114)
        if self.item121.checkState(0) == QtCore.Qt.Checked:
            a121 = str(self.item121.text(0))
            Field.append(a121)
        if self.item122.checkState(0) == QtCore.Qt.Checked:
            a122 = str(self.item122.text(0))
            Field.append(a122)
        if self.item123.checkState(0) == QtCore.Qt.Checked:
            a123 = str(self.item123.text(0))
            Field.append(a123)
        if self.item124.checkState(0) == QtCore.Qt.Checked:
            a124 = str(self.item124.text(0))
            Field.append(a124)
        if self.item132.checkState(0) == QtCore.Qt.Checked:
            a132 = str(self.item132.text(0))
            Values.append(a132)
        if self.item133.checkState(0) == QtCore.Qt.Checked:
            a133 = str(self.item133.text(0))
            Values.append(a133)
        if self.item134.checkState(0) == QtCore.Qt.Checked:
            a134 = str(self.item134.text(0))
            Values.append(a134)
        if self.item135.checkState(0) == QtCore.Qt.Checked:
            a135 = str(self.item135.text(0))
            Values.append(a135)
        if self.item136.checkState(0) == QtCore.Qt.Checked:
            a136 = str(self.item136.text(0))
            Values.append(a136)
        print Fast
        print Plot
        print Field
        print Values
        shared = {"Fast":Fast,"Plot":Plot,"Field":Field,"Values":Values}
        fp = open("shared.pkl","w")
        pickle.dump(shared,fp)
        return Fast
        return Plot
        return Field
        return Values
        
        
    def creatFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.ironbutton = QPushButton("Iron Loss Setup",self)
        
        self.savebutton = QPushButton("Save", self)
        self.returnbutton = QPushButton("Return", self)
        self.buttonbox.addButton(self.ironbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.savebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)
        layout = QFormLayout()
        layout.addWidget(self.buttonbox)
        self.formGroupBox.setLayout(layout)
        self.savebutton.clicked.connect(self.setup_getdp)
        self.savebutton.clicked.connect(self.setup_function)
        self.ironbutton.clicked.connect(self.open_iron)
        self.returnbutton.clicked.connect(self.close)
        
    def content_createGridGroupBox(self):
        self.cb_nl = QCheckBox("Nonlinear Curve", self)
        self.cmb_NLLaw = QComboBox(self)
        self.NLLaw_list = [self.tr('Analytical'), self.tr('Interpolated'), self.tr('Analytical VH800-65D'), self.tr('Interpolated VH800-65D'),]
        self.cmb_NLLaw.addItems(self.NLLaw_list)
        self.cmb_NLLaw.setCurrentIndex(0)
        self.stored_cmb_linear_index = 0  
        self.cmb_NLLaw.setEnabled(False)
        
        self.nb_iter = QLabel("Iterations [Max = 30]", self)
        self.nb_iter_text = QLineEdit("30", self)
        self.re_fact = QLabel("Relaxation Factor", self)
        self.re_fact_text = QLineEdit("1", self)
        self.stop_cri = QLabel("Stopping Criterion", self)
        self.stop_cri_text = QLineEdit("1e-5", self)
        self.ab_t = QLabel("Absolute Tolerance", self)
        self.ab_text = QLineEdit("1e-5", self)
        self.re_t = QLabel("Relative Tolerance", self)
        self.re_text = QLineEdit("1e-7", self)        
        #save time steps
        
        
    def NL_state(self, state):
        if state == QtCore.Qt.Checked:
            self.cmb_NLLaw.setEnabled(True)
        else:
            self.cmb_NLLaw.setEnabled(False)
            
    def setup_getdp(self):
        
        #Type of nicht linear
        if self.cb_nl.isChecked():
            FN = 'Flag_NL = 1 ; \n'
            print(FN)
            #select type of BH
            Flag_NL_law_Type = self.cmb_NLLaw.currentIndex()
            if Flag_NL_law_Type == 0:
                FNLLT = 'Flag_NL_law_Type = 0 ; \n'
            if Flag_NL_law_Type == 1:
                FNLLT = 'Flag_NL_law_Type = 1 ; \n'
            if Flag_NL_law_Type == 2:
                FNLLT = 'Flag_NL_law_Type = 2 ; \n'
            if Flag_NL_law_Type == 3:
                FNLLT = 'Flag_NL_law_Type = 3 ; \n'
            
            iter_max = str(self.nb_iter_text.text())
            re_fac = str(self.re_fact_text.text())
            cri = str(self.stop_cri_text.text())
            re_t = str(self.re_text.text())
            ab_t = str(self.ab_text.text())
            iter_i = 'Nb_max_iter = ' + iter_max + ';\n'
            re_i = 'relaxation_factor =' + re_fac + ';\n'
            cri_i = 'stop_criterion = '+ cri + ';\n'
            ret_i = 'reltol = ' + re_t + ';\n'
            ab_i = "abstol = " + ab_t + ';\n'
        else:
            FN = 'Flag_NL = 0 ; \n'
            FNLLT = ''
            iter_i = ''
            re_i = ''
            cri_i = ''
            ret_i = ''
            ab_i = ''


        print('A analysis File will be created')
        filename = 'moduls\\temp\\solverdata.pro'
        try: 
            file = open(filename, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        
        f1 = open(filename, 'w+')
        add_content = [FN, FNLLT,iter_i, re_i, cri_i, ret_i, ab_i]
        f1.writelines(add_content)
        f1.close()
        self.close()
        
        
    def open_iron(self):
        command = "widgets\\iron.py"
        subprocess.Popen(command, shell = True)
    
    def setup_function(self):
        self.creatVboxGroupBox()
        pass
    
    
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Solver_Cal()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle('Field Calculation')
    window.show()
    app.exec_()
    sys.exit(0)