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
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')


class MotorData(QWidget):
    def __init__(self):
        super(MotorData, self).__init__()
        self.setWindowTitle("Geometry dimension [Stator1]/[Rotor1]")
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
        self.le_cmd_rR2.setText("22.45")
        # Radiu of rotor without magnet
        self.l_cmd_rR3 = QLabel("[Rotor] Radius of rotor without magnet -- rR3 [mm]", self)
        self.le_cmd_rR3 = QLineEdit(self)
        self.le_cmd_rR3.setToolTip("Radius of rotor without magnet")
        self.le_cmd_rR3.setText("24.2")
        # Width of Nut for one Magnet(langer than Magnet)
        self.l_cmd_wrR3 = QLabel("[Rotor] Width of Nut for Magnet       -- wrR3 [mm]" ,self)
        self.le_cmd_wrR3 = QLineEdit(self)
        self.le_cmd_wrR3.setToolTip("[Rotor] Width of Nut for one Magnet(langer than Magnet)")
        self.le_cmd_wrR3.setText("7.175")
        # Width of Magnet
        self.l_cmd_wrR2 = QLabel("[Rotor] Width of Magnet               -- wrR2 [mm]", self)
        self.le_cmd_wrR2 = QLineEdit(self)
        self.le_cmd_wrR2.setToolTip("Width of Magnet")
        self.le_cmd_wrR2.setText("7.05")

        # Radiu Magnet Airgap Side
        self.l_cmd_rRext = QLabel("[Rotor] Outer Radius                 -- rRext [mm]", self)
        self.le_cmd_rRext = QLineEdit(self)
        self.le_cmd_rRext.setToolTip("Radiu of rotor to Airgap Side")
        self.le_cmd_rRext.setText("26")
        layout1 = QGridLayout()
        layout1.addWidget(self.l_cmd_rR1, 3 ,0)
        layout1.addWidget(self.le_cmd_rR1, 3, 1)
        layout1.addWidget(self.l_cmd_rR2, 4 ,0)
        layout1.addWidget(self.le_cmd_rR2, 4, 1)
        layout1.addWidget(self.l_cmd_rR3, 5 ,0)
        layout1.addWidget(self.le_cmd_rR3, 5, 1)
        layout1.addWidget(self.l_cmd_rRext, 6 ,0)
        layout1.addWidget(self.le_cmd_rRext, 6, 1)
        layout1.addWidget(self.l_cmd_wrR3, 7 ,0)
        layout1.addWidget(self.le_cmd_wrR3, 7, 1)
        layout1.addWidget(self.l_cmd_wrR2, 8 ,0)
        layout1.addWidget(self.le_cmd_wrR2, 8, 1)
        rotor.setLayout(layout1)
        
        # Inner Diameter
        self.l_cmd_rS1 = QLabel("Inner Radius of Stator                 -- rS1 [mm]", self)
        self.le_cmd_rS1 = QLineEdit(self)
        self.le_cmd_rS1.setToolTip("Inner Diameter")
        self.le_cmd_rS1.setText("rRext + Airgap")
        
        # Winding Height
        self.l_cmd_Hw = QLabel("Winding Height                          -- Hw [mm]",self)
        self.le_cmd_Hw = QLineEdit(self)
        self.le_cmd_Hw.setToolTip("Winding Height")
        self.le_cmd_Hw.setText("10")
        # Totol height
        self.l_cmd_H = QLabel("Total Height                             -- H [mm]",self)
        self.le_cmd_H = QLineEdit(self)
        self.le_cmd_H.setToolTip("Totol Height")
        self.le_cmd_H.setText("14")
        # Outer diameter
        self.l_cmd_rSext = QLabel("Outer Radius of Stator               -- rSext [mm]", self)
        self.le_cmd_rSext = QLineEdit(self)
        self.le_cmd_rSext.setToolTip("Outer Diameter")
        self.le_cmd_rSext.setText("46")
        #slot openning width
        self.l_cmd_ws1 = QLabel("Slot Opening Width                     -- ws1 [mm]", self)
        self.le_cmd_ws1 = QLineEdit(self)
        self.le_cmd_ws1.setToolTip("Slot opening Width")
        self.le_cmd_ws1.setText("0.9")
        #slot width
        self.l_cmd_wsS1 = QLabel("Slot Width                            -- wsS1 [mm]", self)
        self.le_cmd_wsS1 = QLineEdit(self)
        self.le_cmd_wsS1.setToolTip("Slot opening Width")
        self.le_cmd_wsS1.setText("3.299/2")
        
        # Radius inside of Slot ws3
        self.l_cmd_ws3 = QLabel("Radius inside of Slot                  -- ws3 [mm]", self)
        self.le_cmd_ws3 = QLineEdit(self)
        self.le_cmd_ws3.setToolTip("Slot opening Width")
        self.le_cmd_ws3.setText("1.861")
        
        # A Distance in Slot wsS3
        self.l_cmd_wsS3 = QLabel("A Distance in Slot                    -- wsS3 [mm]", self)
        self.le_cmd_wsS3 = QLineEdit(self)
        self.le_cmd_wsS3.setToolTip("A Distance in Slot")
        self.le_cmd_wsS3.setText("2.583/2")
        
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
        layout2.addWidget(self.l_cmd_ws3, 19, 0)
        layout2.addWidget(self.le_cmd_ws3, 19, 1)
        layout2.addWidget(self.l_cmd_wsS3, 20, 0)
        layout2.addWidget(self.le_cmd_wsS3, 20, 1)

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
        # this part will be copyed to data geo
        rR1 = 'rR1  =  ' + str(self.le_cmd_rR1.text()) + '*mm;\n' 
        rR2 = 'rR2  =  ' +str(self.le_cmd_rR2.text()) + '*mm;\n' 
        rR3 = 'rR3  =  ' +str(self.le_cmd_rR3.text()) + '*mm;\n' 
        rRext = 'rRext  =  ' +str(self.le_cmd_rRext.text()) + '*mm;\n' 
        wrR3 = 'wrR3 =  ' + str(self.le_cmd_wrR3.text()) + '*mm;\n'
        wrR2 = 'wrR2 =  ' + str(self.le_cmd_wrR2.text()) + '*mm;\n'
        rS1 = 'rS1 =  ' + str(self.le_cmd_rS1.text()) + ';\n'
        rS2 = 'rS2 = rRext + ' + str(self.le_cmd_Hw.text()) + '*mm;\n'
        rS3 = 'rS3 = rRext + ' + str(self.le_cmd_H.text()) + '*mm - ' + str(self.le_cmd_ws3.text()) + '*mm;\n'
        rS4 = 'rS4 = rRext + ' + str(self.le_cmd_H.text()) + '*mm;\n'
        rSext = 'rSext = ' + str(self.le_cmd_rSext.text()) + '*mm;\n'
        ws1 = 'ws1 =  ' + str(self.le_cmd_ws1.text()) + '*mm;\n'
        ws3 = 'ws3 =  ' + str(self.le_cmd_ws3.text()) + '*mm;\n'
        wsS1 = 'wsS1 =  ' + str(self.le_cmd_wsS1.text()) + '*mm;\n'
        wsS3 = 'wsS3 =  ' + str(self.le_cmd_wsS3.text()) + '*mm;\n'
        mm = "mm=1e-3;"
        
        filename = 'moduls\\temp\\geo_data.pro'
        try: 
            file = open(filename, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        
        f1 = open(filename, 'w+')
        add_content = [mm,rR1,rR2,rR3,rRext,wrR3,wrR2,rS1,rS2,rS3,rS4,rSext,ws1,ws3,wsS1,wsS3]
        f1.writelines(add_content)
        f1.close()
        
        
        


if __name__=="__main__":    
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
        app.aboutToQuit.connect(app.deleteLater)
    window = MotorData()
    window.setWindowIcon(QIcon('icon\main.jpg'))
    window.show()
    app.exec_()
    sys.exit(0)
