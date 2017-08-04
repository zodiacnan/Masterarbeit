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
        self.setWindowTitle("Paramters of Motor")
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
        self.l_cmd_rS1 = QLabel("Inner Radius of Stator         -- rS1 [mm]", self)
        self.le_cmd_rS1 = QLineEdit(self)
        self.le_cmd_rS1.setToolTip("Inner Diameter")
        self.le_cmd_rS1.setText("rRext + 0.6")
        
        # Winding Height
        self.l_cmd_Hw = QLabel("Winding Height                  -- Hw [mm]",self)
        self.le_cmd_Hw = QLineEdit(self)
        self.le_cmd_Hw.setToolTip("Winding Height")
        self.le_cmd_Hw.setText("10")
        # Totol height
        self.l_cmd_H = QLabel("Total Height                     -- H [mm]",self)
        self.le_cmd_H = QLineEdit(self)
        self.le_cmd_H.setToolTip("Totol Height")
        self.le_cmd_H.setText("14")
        # Outer diameter
        self.l_cmd_rSext = QLabel("Outer Radius of Stator       -- rSext [mm]", self)
        self.le_cmd_rSext = QLineEdit(self)
        self.le_cmd_rSext.setToolTip("Outer Diameter")
        self.le_cmd_rSext.setText("46")
        #slot openning width
        self.l_cmd_ws1 = QLabel("Slot Opening Width             -- ws1 [mm]", self)
        self.le_cmd_ws1 = QLineEdit(self)
        self.le_cmd_ws1.setToolTip("Slot opening Width")
        self.le_cmd_ws1.setText("0.9")
        #slot width
        self.l_cmd_wsS1 = QLabel("Slot Width                    -- wsS1 [mm]", self)
        self.le_cmd_wsS1 = QLineEdit(self)
        self.le_cmd_wsS1.setToolTip("Slot opening Width")
        self.le_cmd_wsS1.setText("3.299/2")
        
        # Radius inside of Slot ws3
        self.l_cmd_ws3 = QLabel("Radius inside of Slot          -- ws3 [mm]", self)
        self.le_cmd_ws3 = QLineEdit(self)
        self.le_cmd_ws3.setToolTip("Slot opening Width")
        self.le_cmd_ws3.setText("1.861")
        
        # A Distance in Slot wsS3
        self.l_cmd_wsS3 = QLabel("A Distance in Slot            -- wsS3 [mm]", self)
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
        
        R_wrR3 = float(self.le_cmd_wrR3.text())
        R_wrR2 = float(self.le_cmd_wrR2.text()) 
        R_rR1 = float(self.le_cmd_rR1.text())
        R_rR2 = float(self.le_cmd_rR2.text())
        R_rR3 = float(self.le_cmd_rR3.text())
        R_rRext = float(self.le_cmd_rRext.text())
        S_rS1 = float(self.le_cmd_rRext.text()) + float(self.le_cmd_gap.text())
        S_Hw = float(self.le_cmd_Hw.text())
        S_H = float(self.le_cmd_H.text())
        S_rSext =  float(self.le_cmd_rSext.text()) 
        S_ws1 = float(self.le_cmd_ws1.text())
        S_ws3 = float(self.le_cmd_ws3.text())
        # CONDITIONS OF ROTOR
        if R_rR3 > R_rRext:
            #print("Magnet will be covered in Slot")
            self.outputBrowser.append("Error -- Magnet will be covered in Slot")
            return
        if R_rR2 > R_rR3:
            #print("Magnet will not inside of slot")
            self.outputBrowser.append("Error -- Magnet will not inside of slot")
            return
        if (R_rR1 > R_rR2) or (R_rR1 > R_rR3) or (R_rR2 > R_rRext) or (R_rR3 > R_rRext) or (R_rR1 > R_rRext):
            #print("The size of rotor is not right")
            self.outputBrowser.append("Error -- The size of rotor is not right")
            return
        if R_wrR3 < R_wrR2:
            #print("Width of Magnet should not be langer than Slot")
            self.outputBrowser.append("Error -- Width of Magnet should not be langer than Slot")
            return
        if R_rRext > S_rSext:
            #print("Radius of rotor should not be langer than stators")
            self.outputBrowser.append("Error -- Radius of rotor should not be langer than stators")
            return
        if S_ws1 > 1.2:
            #print("Opening Width of Stator Slot is big and please input a smaller one")
            self.outputBrowser.append("Error -- Opening Width of Stator Slot is big and please input a smaller one")
            return
        if S_ws3 > 2:
            #print("Upper part of Stator Slot is so big and plesae input a smaller one")
            self.outputBrowser.append("Error -- Upper part of Stator Slot is so big and plesae input a smaller one")
            return
        if (S_Hw > S_H) or (S_rS1 > S_rSext):
            #print("The size of stator is not right")
            self.outputBrowser.append("Error -- The size of stator is not right")
            return
        type_r = str(self.cmd_type_r.currentText())
        type_s = str(self.cmd_type_s.currentText())
        if (type_r == 'Rotor1_PMSM') and (type_s == 'Stator1_PMSM'):
            self.outputBrowser.append("Update -- The model of PMSM is accessible")
            #print("This type of PMSM is already")
        else:
            #print("We do not have this model")
            self.outputBrowser.append("Error -- We do not have this motor model")
            return
        # this part will be copyed to data geo
        rR1 = 'rR1  =  ' + str(self.le_cmd_rR1.text()) + '*mm;' 
        rR2 = 'rR2  =  ' +str(self.le_cmd_rR2.text()) + '*mm;' 
        rR3 = 'rR3  =  ' +str(self.le_cmd_rR3.text()) + '*mm;' 
        rRext = 'rRext  =  ' +str(self.le_cmd_rRext.text()) + '*mm;' 
        wrR3 = 'wrR3 =  ' + str(self.le_cmd_wrR3.text()) + '*mm;'
        wrR2 = 'wrR2 =  ' + str(self.le_cmd_wrR2.text()) + '*mm;'
        rS1 = 'rS1 =  ' + str(self.le_cmd_rS1.text()) + '*mm;'
        rS2 = 'rS2 = rRext + ' + str(self.le_cmd_Hw.text()) + '*mm;'
        rS3 = 'rS3 = rRext + ' + str(self.le_cmd_H.text()) + '*mm - ' + str(self.le_cmd_ws3.text()) + '*mm;'
        rS4 = 'rS4 = rRext + ' + str(self.le_cmd_H.text()) + '*mm;'
        rSext = 'rSext = ' + str(self.le_cmd_rSext.text()) + '*mm;'
        ws1 = 'ws1 =  ' + str(self.le_cmd_ws1.text()) + '*mm;'
        ws3 = 'ws3 =  ' + str(self.le_cmd_ws3.text()) + '*mm;'
        wsS1 = 'wsS1 =  ' + str(self.le_cmd_wsS1.text()) + '*mm;'
        wsS3 = 'wsS3 =  ' + str(self.le_cmd_wsS3.text()) + '*mm;'
        NbrPolesTot = 'NbrPolesTot  =  ' + str(self.le_cmd_numpole.text()) + ';'
        NbrSectTotStator = 'NbrSectTotStator  =  ' + str(self.le_cmd_numteeth.text()) + ';'
        # read 2 empty text to store the data
        f1 = file('C:\\Users\\DINGNAN\\Desktop\\NanDing\\FEMMaschinen\\pmsm\\new.txt','w+')
        f3 = file('C:\\Users\\DINGNAN\\Desktop\\NanDing\\FEMMaschinen\\pmsm\\new_1.txt','w+')
        add_content_1 = [rR1+'\n',rR2+'\n',rR3+'\n',rRext+'\n','\n',wrR3+'\n',wrR2+'\n',rS1+'\n',rS2 +'\n',rS3+'\n',rS4+'\n',rSext+'\n', ws1+'\n',ws3+'\n',wsS1+'\n',wsS3+'\n']
        add_content_2 = [NbrPolesTot +'\n',NbrSectTotStator+'\n']
        f1.writelines(add_content_1)
        f1.close()
        f3.writelines(add_content_2)
        f3.close()
        f1 = open('C:\\Users\\DINGNAN\\Desktop\\NanDing\\FEMMaschinen\\pmsm\\new.txt','r')
        f3 = open('C:\\Users\\DINGNAN\\Desktop\\NanDing\\FEMMaschinen\\pmsm\\new_1.txt','r')
        f2 = open('C:\\Users\\DINGNAN\\Desktop\\NanDing\\FEMMaschinen\\pmsm\\pmsm_cbmag_data.geo','r')
        content_1 = f1.read()
        content_2 = f3.read()
        content = f2.read()
        f2.close()
        pos_1 = content.find("// dimensions rotor")
        pos_2 = content.find("// dimensions stator")
        pos_3 = content.find("mm = 1e-3 ;")
        pos_4 = content.find("deg2rad = Pi/180 ;")
        if (pos_1 != -1) and (pos_2 != -1) and (pos_3 != -1) and (pos_4 != -1):
            content = content[:pos_3+11]+'\n'+ content_2+ '\n'+ content[pos_4:pos_1+20] + '\n' + content_1 + '\n' +content[pos_2:]
            f2 = open('C:\\Users\\DINGNAN\\Desktop\\NanDing\\FEMMaschinen\\pmsm\\pmsm_cbmag_data.geo','w')
            f2.write(content)
            f2.close()
            #print("success1")
            self.outputBrowser.append("Update -- The parameters are already added into Geometry File\nUpdate -- GUI of GMSH and GetDp will open")
        else:
            #print("sorry, can not find the position to add parameters")
            self.outputBrowser.append("Error -- Sorry, can not find the position to add parameters")
        

            


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
