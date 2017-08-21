# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:25:22 2017

@author: DINGNAN
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:52:21 2017

@author: DINGNAN
"""

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MotorData(QWidget):
    def __init__(self):
        super(MotorData, self).__init__()
        self.setWindowTitle("Geometry dimension [Stator2]/[Rotor2]")
        self.initUI()
        
    def __del__(self):
        return
    
    def initUI(self):
        layout = QVBoxLayout()
        stator = QGroupBox('Stator')
        rotor = QGroupBox('Rotor')
        form = QFormLayout()
        layout.addWidget(rotor)
        layout.addWidget(stator)
        layout.addLayout(form)
        # set the input parameter of motor (pmsm)
        # Radiu iron yoke inside
        self.l_cmd_rR1 = QLabel("[Rotor] Inner Radius                   -- rR1 [mm]", self)
        self.le_cmd_rR1 = QLineEdit(self)
        self.le_cmd_rR1.setToolTip("Radius iron yoke inside")
        self.le_cmd_rR1.setText("10.5")
        
        # RADIU OF Magenet inside of iron
        self.l_cmd_rR2 = QLabel("[Rotor] Radius of Magenet inside iron  -- rR2 [mm]", self)
        self.le_cmd_rR2 = QLineEdit(self)
        self.le_cmd_rR2.setToolTip("RADIUs OF Magenet inside of iron")
        self.le_cmd_rR2.setText("rRext-lm")
        # Radiu of rotor without magnet
        self.l_cmd_rR3 = QLabel("[Rotor] Radius of rotor blech          -- rR4 [mm]", self)
        self.le_cmd_rR3 = QLineEdit(self)
        self.le_cmd_rR3.setToolTip("Radius of rotor without magnet")
        self.le_cmd_rR3.setText("rRext-0.72278*lm")

        self.l_cmd_rRext = QLabel("[Rotor] Outer Radius                 -- rRext [mm]", self)
        self.le_cmd_rRext = QLineEdit(self)
        self.le_cmd_rRext.setToolTip("Radiu of rotor to Airgap Side")
        self.le_cmd_rRext.setText("25.6")
        
        self.lm = QLabel("[Rotor] Magnet heigth                   -- lm [mm]", self)
        self.lm_text = QLineEdit(self)
        self.lm_text.setToolTip("[Rotor] Magnet heigth")
        self.lm_text.setText("2.352")
        
        self.m_theta = QLabel("[Rotor] Magnet Angel                 -- Theta [deg]",self)
        self.m_theta_text = QLineEdit(self)
        self.m_theta_text.setText("32.67")
        
        layout1 = QGridLayout()
        layout1.addWidget(self.l_cmd_rR1, 3 ,0)
        layout1.addWidget(self.le_cmd_rR1, 3, 1)
        layout1.addWidget(self.l_cmd_rR2, 4 ,0)
        layout1.addWidget(self.le_cmd_rR2, 4, 1)
        layout1.addWidget(self.l_cmd_rR3, 5 ,0)
        layout1.addWidget(self.le_cmd_rR3, 5, 1)
        layout1.addWidget(self.l_cmd_rRext, 6 ,0)
        layout1.addWidget(self.le_cmd_rRext, 6, 1)
        layout1.addWidget(self.lm, 7 ,0)
        layout1.addWidget(self.lm_text, 7, 1)
        layout1.addWidget(self.m_theta, 8 ,0)
        layout1.addWidget(self.m_theta_text, 8, 1)
        rotor.setLayout(layout1)
        
        # Inner Diameter
        self.l_cmd_rS1 = QLabel("Inner Radius of Stator              -- rS1 [mm]", self)
        self.le_cmd_rS1 = QLineEdit(self)
        self.le_cmd_rS1.setToolTip("Inner Diameter")
        self.le_cmd_rS1.setText("rRext + Gap")
        
        # Winding Height
        self.l_cmd_Hw = QLabel("Blech Height                       -- Hext [mm]",self)
        self.le_cmd_Hw = QLineEdit(self)
        self.le_cmd_Hw.setToolTip("Winding Height")
        self.le_cmd_Hw.setText("5.98")
        # Totol height
        self.l_cmd_H = QLabel("Winding Region Height                 -- H [mm]",self)
        self.le_cmd_H = QLineEdit(self)
        self.le_cmd_H.setToolTip("Totol Height")
        self.le_cmd_H.setText("11.2")
        # Outer diameter
        self.l_cmd_rSext = QLabel("Outer Radius of Stator            -- rSext [mm]", self)
        self.le_cmd_rSext = QLineEdit(self)
        self.le_cmd_rSext.setToolTip("Outer Diameter")
        self.le_cmd_rSext.setText("46")
        #slot openning width
        self.l_cmd_ws1 = QLabel("Slot Opening Width                   -- Ws [mm]", self)
        self.le_cmd_ws1 = QLineEdit(self)
        self.le_cmd_ws1.setToolTip("Slot opening Width")
        self.le_cmd_ws1.setText("3.7")
        
        #slot width
        self.l_cmd_wsS1 = QLabel("Slot Opening Height                  -- Wh [mm]", self)
        self.le_cmd_wsS1 = QLineEdit(self)
        self.le_cmd_wsS1.setToolTip("Slot opening Width")
        self.le_cmd_wsS1.setText("0.94")
        
        # Layout        
        layout2 = QGridLayout()
        

        layout2.addWidget(self.l_cmd_rS1, 12, 0)
        layout2.addWidget(self.le_cmd_rS1, 12, 1)
        layout2.addWidget(self.l_cmd_Hw, 13, 0)
        layout2.addWidget(self.le_cmd_Hw, 13, 1)
        layout2.addWidget(self.l_cmd_H, 15, 0)
        layout2.addWidget(self.le_cmd_H, 15, 1)
        layout2.addWidget(self.l_cmd_rSext, 16, 0)
        layout2.addWidget(self.le_cmd_rSext, 16, 1)
        layout2.addWidget(self.l_cmd_ws1, 17, 0)
        layout2.addWidget(self.le_cmd_ws1, 17, 1)
        layout2.addWidget(self.l_cmd_wsS1, 18, 0)
        layout2.addWidget(self.le_cmd_wsS1, 18, 1)
        stator.setLayout(layout2)
        
        self.buttonbox = QDialogButtonBox()
        self.buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.savebutton = QPushButton("Save", self)
        self.returnbutton = QPushButton("Return", self)
        self.buttonbox.addButton(self.savebutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)
        form.addWidget(self.buttonbox)
        
        self.setLayout(layout)
        self.returnbutton.clicked.connect(self.close)
        self.savebutton.clicked.connect(self.write_geo)
    def cancel(self):
        self.close()
        
    def write_geo(self):
        pass

            


if __name__=="__main__":    
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
        app.aboutToQuit.connect(app.deleteLater)
    window = MotorData()
    window.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
    window.show()
    app.exec_()
    sys.exit(0)
