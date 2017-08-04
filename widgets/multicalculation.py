# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 13:00:55 2017

@author: DINGNAN
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:05:32 2017

@author: DINGNAN
"""

#Field Calculation Solver

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
import subprocess
import pickle

class Field_Cal(QWidget):
    def __init__(self,*args,**kwargs):
        super(Field_Cal, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()
    
    def initUI(self):
        self.createGridGroupBox()
        self.creatVboxGroupBox()
        self.creatFormGroupBox()
        mainLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.gridGroupBox)
        hboxLayout.addWidget(self.vboxGroupBox)
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.buttonbox)
        self.setLayout(mainLayout)
        
    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Mode")
        self.gridGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.gridGroupBox.setMaximumWidth(450)
        self.gridGroupBox.setMinimumHeight(400)
        self.content_createGridGroupBox()
        layout = QGridLayout()
        layout.addWidget(self.mv, 1, 0)
        layout.addWidget(self.l_analysis, 2, 0)
        layout.addWidget(self.cmb_analysis, 2, 1)
        layout.addWidget(self.start_rotor_angel, 3, 0)
        layout.addWidget(self.start_rotor_angel_text, 3, 1)
        layout.addWidget(self.end_rotor_angel, 4, 0)
        layout.addWidget(self.end_rotor_angel_text, 4 ,1)
        layout.addWidget(self.step, 5, 0)
        layout.addWidget(self.step_text, 5 ,1)
        layout.addWidget(self.time_step, 6, 0)
        layout.addWidget(self.time_step_nr, 6 ,1)
        layout.addWidget(self.cb_save, 7 ,0, 1, 2)
        layout.addWidget(self.cb_clean, 8, 0)
        layout.addWidget(self.parameter,9, 0)
        layout.addWidget(self.parameter_data, 9, 1)
        layout.addWidget(self.frequenz, 10, 0)
        layout.addWidget(self.frequenz_data, 10, 1)
        
        layout.addWidget(self.base_I, 11, 0)
        layout.addWidget(self.src_stator, 12, 0)
        layout.addWidget(self.src_stator_op, 12, 1)
        
        layout.addWidget(self.Id_text, 13 ,0)
        layout.addWidget(self.Id_set, 13, 1)
        layout.addWidget(self.Iq_text, 14, 0)
        layout.addWidget(self.Iq_set, 14, 1)
        
        layout.addWidget(self.base_rotor, 15, 0)
        layout.addWidget(self.src_rotor, 15, 1)
        layout.addWidget(self.ie, 16, 0)
        layout.addWidget(self.ie_text, 16, 1)
        
        self.gridGroupBox.setLayout(layout)
        self.start_rotor_angel_text.textChanged.connect(self.time_step_func)
        self.end_rotor_angel_text.textChanged.connect(self.time_step_func)
        self.step_text.textChanged.connect(self.time_step_func)
        self.cmb_analysis.currentTextChanged.connect(self.Analysis_Text)
        self.src_stator_op.currentTextChanged.connect(self.Scr_TEXT)
        self.parameter_data.textChanged.connect(self.rpm_f)
    
    def rpm_f(self):
        NbrPolePair = 4
        #must read from motor setuo and calculate
        rpm = int(self.parameter_data.text())
        Freq = rpm*NbrPolePair/60
        self.frequenz_data.setText(str(Freq))
    def time_step_func(self):
        start = float(str(self.start_rotor_angel_text.text()))
        end = float(str(self.end_rotor_angel_text.text()))
        angel = float(str(self.step_text.text()))
        time_step = int((end-start)/angel)
        self.time_step_nr.setText(str(time_step))

    def Scr_TEXT(self):
        text = self.src_stator_op.currentText()
        if text == 'Current':
            self.Id_set.setEnabled(True)
            self.Id_text.setEnabled(True)
            self.Iq_set.setEnabled(True)
            self.Iq_text.setEnabled(True)
        else:
            self.Id_set.setEnabled(False)
            self.Id_text.setEnabled(False)
            self.Iq_set.setEnabled(False)
            self.Iq_text.setEnabled(False)
    
    def Analysis_Text(self):
        text = self.cmb_analysis.currentText()
        if text == 'Static':

            self.end_rotor_angel.setEnabled(False)
            self.end_rotor_angel_text.setEnabled(False)
            self.step.setEnabled(False)
            self.step_text.setEnabled(False)
            self.cb_save.setEnabled(False)
            self.cb_clean.setEnabled(False)
            self.time_step.setEnabled(False)
            self.time_step_nr.setEnabled(False)
            self.parameter.setEnabled(False)
            self.parameter_data.setEnabled(False)
        else:
            self.end_rotor_angel.setEnabled(True)
            self.end_rotor_angel_text.setEnabled(True)
            self.step.setEnabled(True)
            self.step_text.setEnabled(True)
            self.time_step.setEnabled(True)
            self.time_step_nr.setEnabled(True)
            self.parameter.setEnabled(True)
            self.parameter_data.setEnabled(True)
            self.cb_save.setEnabled(True)
            self.cb_clean.setEnabled(True)
    
    def content_createGridGroupBox(self):
        self.mv = QLabel("[Movement]", self)
        # Analysis Type of getdp
        self.l_analysis = QLabel('Type of Analysis', self)
        self.cmb_analysis = QComboBox(self)
        self.analysis_list = [self.tr('Static'), self.tr('Time domain'),self.tr('Frequence domain')]
        self.cmb_analysis.addItems(self.analysis_list)
        self.cmb_analysis.setCurrentIndex(0)
        
        self.start_rotor_angel = QLabel("Start  Angel    [deg]", self)
        self.start_rotor_angel_text = QLineEdit("0", self)
        self.end_rotor_angel = QLabel("End    Angel    [deg]", self)
        self.end_rotor_angel_text = QLineEdit("180", self)
        self.step = QLabel("Step   Angel    [deg]", self)
        self.step_text = QLineEdit("1", self)
        self.time_step = QLabel("Time Steps", self)
        self.time_step_nr = QLineEdit("180")
        self.cb_save = QCheckBox("Save all results [Time Domain]", self)
        self.cb_save.setChecked(QtCore.Qt.Checked) 
        #clean previous results
        self.cb_clean = QCheckBox("Clean previous results", self)
        self.cb_clean.setChecked(QtCore.Qt.Checked)
        
        self.cb_save.setEnabled(False)
        self.cb_clean.setEnabled(False)
        self.end_rotor_angel.setEnabled(False)
        self.end_rotor_angel_text.setEnabled(False)
        self.step.setEnabled(False)
        self.step_text.setEnabled(False)
        self.time_step.setEnabled(False)
        self.time_step_nr.setEnabled(False)
         
        self.parameter = QLabel("Speed           [rpm]", self)
        self.parameter_data = QLineEdit("1500", self)
        self.parameter.setEnabled(False)
        self.parameter_data.setEnabled(False)
        
        self.frequenz = QLabel("Frequence        [Hz]", self)
        self.frequenz_data = QLineEdit("100", self)
        
        
        
        self.base_I = QLabel("[Base Source]", self)

        self.src_stator = QLabel("Source Type of Stator", self)
        self.src_stator_op = QComboBox(self)
        self.src_list = [self.tr('None'), self.tr('Current'),]
        self.src_stator_op.addItems(self.src_list)
        self.src_stator_op.setCurrentIndex(0)
        self.stored_cmb_analysis_index = 0
        
        self.Id_text = QLabel("Id Stator Current [A]", self)
        self.Id_set = QLineEdit("0", self)
        self.Iq_text = QLabel("Iq Stator Current [A]", self)
        self.Iq_set = QLineEdit("3.9", self)

        self.Id_set.setEnabled(False)
        self.Id_text.setEnabled(False)
        self.Iq_set.setEnabled(False)
        self.Iq_text.setEnabled(False)

        
        self.base_rotor = QLabel("Source Type of Rotor", self)
        self.src_rotor = QComboBox(self)
        self.src_rotor_list = [self.tr('None [Permanent Magenet]'), self.tr('Wound Field ')]
        self.src_rotor.addItems(self.src_rotor_list)
        self.src_rotor.setCurrentIndex(0)
        self.ie = QLabel("Ie Rotor Excitation Current [A]", self)
        self.ie_text = QLineEdit("0", self)
        
    def creatVboxGroupBox(self):
        #show the infomation of motor
        fp = open("shared.pkl")
        shared = pickle.load(fp)
        a = str(shared["Fast"]).replace("'","").replace("[","").replace("]","")
        b = str(shared["Field"]).replace("'","").replace("[","").replace("]","")
        c = str(shared["Plot"]).replace("'","").replace("[","").replace("]","")
        d = str(shared["Values"]).replace("'","").replace("[","").replace("]","")
        self.vboxGroupBox = QGroupBox()
        self.vboxGroupBox.setAlignment(QtCore.Qt.AlignCenter)
        
        self.select = QGroupBox("Selected Functions")
        self.label_1 = QLabel(self)
        self.label_2 = QLabel(self)
        self.label_3 = QLabel(self)
        self.label_4 = QLabel(self)
        self.label_1.setText(a)
        self.label_2.setText(b)
        self.label_3.setText(c)
        self.label_4.setText(d)
        layout = QGridLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.label_3)
        layout.addWidget(self.label_4)
        self.vboxGroupBox.setLayout(layout)
        
    def creatFormGroupBox(self):
        self.buttonbox = QDialogButtonBox()
        self.buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.savebutton = QPushButton("Save", self)
        self.returnbutton = QPushButton("Return", self)
        self.buttonbox.addButton(self.savebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)
        self.savebutton.clicked.connect(self.save_data)
        self.returnbutton.clicked.connect(self.return_last)
    def save_data(self):
        toa = self.cmb_analysis.currentIndex()
        if toa == 0:
            toa_i = 'Flag_AnalysisType = 0 ;\n'
            sa = str(self.start_rotor_angel_text.text())
            sa_i = 'InitialRotorAngel_deg = ' + sa + ';\n'
            ea_i = ''
            ns_i = ''
            save = ''
            clean = ''
            speed_data = ''
            speed_i = ''
            
        if toa == 1:
            toa_i = 'Flag_AnalysisType = 1 ;\n'
            sa = str(self.start_rotor_angel_text.text())
            sa_i = 'InitialRotorAngel_deg = ' + sa + ';\n'
            ea = str(self.end_rotor_angel_text.text())
            ea_i = 'thetaMax_deg = ' + ea + ';\n'
            ns = str(self.time_step_nr.text())
            ns_i = 'NbSteps = ' + ns + ';\n'
            if self.cb_save.isChecked():
                save = 'Flag_SaveAllSteps = 1 ;\n'
            else:
                save = 'Flag_SaveAllSteps = 0 ;\n'
            if self.cb_clean.isChecked():
                clean = 'Clean_Results = 1 ;\n'
            else:
                clean = 'Clean_Results = 0 ;\n'
                
            speed = str(self.parameter_data.text())
            speed_data = 'rpm_nominal =' + speed + ';\n'
            if speed == 0:
                speed_i = 'Flag_ImposedSpeed = 0;\n'
            else:
                speed_i = 'Flag_ImposedSpeed = 1;\n'
            
        freq = str(self.frequenz_data.text())
        freq_i = 'Freq = ' + freq + ';\n'
            
        stos = self.src_stator_op.currentIndex()
        Id = str(self.Id_set.text())
        Iq = str(self.Iq_set.text())
        if stos == 0:
            stos_i = 'Flag_SrcType_Stator = 0 ;\n'
            flag_cir = 'Flag_Cir = 1 ;'
            Id_i = ''
            Iq_i = ''
            I0_i = ''
        if stos == 1:
            stos_i = 'Flag_SrcType_Stator = 1 ;\n'
            flag_cir = 'Flag_Cir = 0 ;\n'
            Id_i = 'ID = ' + Id + ';\n'
            Iq_i = 'ID = ' + Iq + ';\n'
            I0_i = 'I0 = 0;\n'
        
        stor = self.src_rotor.currentIndex()
        if stor == 0:
            stor_i = 'Flag_SrcType_Rotor = 0 ;\n'
            Ie_i = 'Ie = 0;\n'
        else:
            ie = str(self.ie_text.text())
            stor_i = 'Flag_SrcType_Rotor = 0 ;\n'
            Ie_i = 'Ie = ' + ie + ';\n'
        
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\moduls\\temp')
        filename_1 = 'inputdata' + '.geo'
        filename_2 = 'solverdata.pro'
        try: 
            file_1 = open(filename_1, 'w')
            file_1.truncate()
            file_1.close()
        except:
            print('Something went wrong')
        
        f1 = open(filename_1, 'a')
        f2 = open(filename_2, 'a')
        add_geo = [sa_i, speed_data]
        add_pro = [toa_i, save, clean, speed_i, stos_i, flag_cir, stor_i, ea_i
                   , ns_i,freq_i, Id_i, Iq_i, I0_i, Ie_i]
        f1.writelines(add_geo)
        f2.writelines(add_pro)
        f1.close()
        f2.close()
        
        
        self.close()
        
        


        
    
    def return_last(self):
        #return to the GUI of Solver Setup
        self.close()
    


        
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Field_Cal()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle('Multicalculation')
    window.show()
    app.exec_()
    sys.exit(0)