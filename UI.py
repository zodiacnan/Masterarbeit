
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 18:48:25 2017

@author: DINGNAN
"""

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
import subprocess

class UI_Main(QMainWindow):
    
    def __init__(self, parent = None):
        super(UI_Main, self).__init__(parent = parent)
        self.initUi()
        
    def initUi(self):      
        self.MenuUI()
        UI_widget = UI_Frame(self)
        self.CentralWidget = QWidget(self)
        self.hbox = QHBoxLayout()
        self.setCentralWidget(UI_widget)
        
    def MenuUI(self):
        self.statusBar()
        
        addAction = QAction(QIcon(''), '&New', self)
        addAction.setStatusTip('create new geometry in GMSH')
        addAction.triggered.connect(self.addFile)
        
        openAction = QAction(QIcon(''), '&Open Examples...', self)
        openAction.setStatusTip('create from Layout of Motor')
        openAction.triggered.connect(self.addFileEx)
        
        fileAction = QAction(QIcon(''), '&Open Scripts', self)
        fileAction.setStatusTip('Open from directory')
        fileAction.triggered.connect(self.addFileOpen)
        
        exitAction = QAction(QIcon(''), '&Exit', self)
        exitAction.setStatusTip('Exit the project')
        exitAction.triggered.connect(self.exitFile)
        
        geoAction = QAction(QIcon(''), '&Create geo File',self)
        geoAction.setStatusTip('open Python to write scripts')
        geoAction.triggered.connect(self.createGeo)
        
        proAction = QAction(QIcon(''), '&Create pro File',self)
        proAction.setStatusTip('open Python to write scripts')
        proAction.triggered.connect(self.createPro)
        
        MBAction = QAction(QIcon(''), 'Material Browser', self)
        MBAction.setStatusTip('open Material Library')
        MBAction.triggered.connect(self.Material_B)
        
        About_Project = QAction(QIcon(''), '&Github', self)
        About_Project.setStatusTip('Help about this project')
        About_Project.triggered.connect(self.About_FEM)
        
        About_Gmsh = QAction(QIcon(''), '&About Gmsh', self)
        About_Gmsh.setStatusTip('Help about Gmsh')
        About_Gmsh.triggered.connect(self.About_GMSH)
        
        About_GetDp = QAction(QIcon(''), '&About GetDp', self)
        About_GetDp.setStatusTip('Help about GetDp')
        About_GetDp.triggered.connect(self.About_GetDp)
        
        lincense = QAction(QIcon(''), '&License', self)
        lincense.setStatusTip('License of this software')
        lincense.triggered.connect(self.lincense)
        
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(addAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(fileAction)
        fileMenu.addAction(exitAction)
        
        toolMenu = menubar.addMenu('&Tools')
        toolMenu.addAction(geoAction)
        toolMenu.addAction(proAction)
        toolMenu.addAction(MBAction)
        
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(About_Project)
        helpMenu.addAction(About_Gmsh)
        helpMenu.addAction(About_GetDp)
        helpMenu.addAction(lincense)
        
        self.show()
        
    def exitFile(self):
        self.close()
    
    def addFile(self):
        #open gmsh geometry macro
        import subprocess
        command = "C:/Users/DINGNAN/Desktop/NanDing/MA/gmsh.exe"
        subprocess.Popen(command, shell = True)
        
    def addFileEx(self):
        #draw accounding to Geometry Examples, a new GUI
        import subprocess
        command = "openexample.py"
        subprocess.Popen(command, shell = True)
    
    def addFileOpen(self):
        #open examples in File, open File
        fileName = QtWidgets.QFileDialog.getOpenFileName()
        if fileName:
            print fileName
    
    def createGeo(self):
        filename_g = 'new' + '.geo'
        try: 
            file = open(filename_g, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        f1 = open(filename_g, 'w+')
        add_content = ['//Create a new geometry of motor']
        f1.writelines(add_content)
        f1.close()
        subprocess.call('notepad new.geo')
        
    
    def createPro(self):
        filename_p = 'new' + '.pro'
        try: 
            file = open(filename_p, 'w+')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        f1 = open(filename_p, 'w+')
        add_content = ['//Create a input file of motor for GetDp\n'
                       '//you can get help from GetDp online or PDF Book and see the format according to example\n']
        f1.writelines(add_content)
        f1.close()
        subprocess.call('notepad new.pro')
    
    def Material_B(self):
        pass
    
    def About_FEM(self):
        import webbrowser
        webbrowser.open('https://github.com/zodiacnan/MA')
    
    def About_GMSH(self):
        import webbrowser
        webbrowser.open('http://www.geuz.org/gmsh/doc/texinfo/gmsh.html#Command_002dline-options')
    
    def About_GetDp(self):
        import webbrowser
        webbrowser.open('http://getdp.info/doc/texinfo/getdp.html#Running-GetDP')
        
    def lincense(self):
        import subprocess
        subprocess.call('notepad C:\Users\DINGNAN\Desktop\NanDing\MA\LICENSE', shell = True)
        
class UI_Frame(QWidget):
    
    def __init__(self,parent = None):
        super(UI_Frame, self).__init__(parent)
        self.initUI()
    
    def initUI(self):  
        self.createMenuBox()
        self.createChildGUI()
        self.createErrorConsole()
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(self.MenuBox)
        mainLayout.addLayout(self.middleleftLayout)
        mainLayout.addWidget(self.ErrorConsole)
        self.setLayout(mainLayout)
        self.setWindowTitle("FE-Calculator for Motor")
        
        
    def createMenuBox(self):
        self.MenuBox = QGroupBox("Menu")
        self.MenuBox.setMaximumWidth(120)
        leftlayout = QVBoxLayout()
        
        self.motor_button = QToolButton()
        self.motor_button.adjustSize()
        self.motor_button.setStyleSheet("background-color: lightblue")
        self.motor_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\setup.png'))
        self.motor_button.setIcon(icon1)
        self.motor_button.setIconSize(QtCore.QSize(60,60))
        self.motor_button.setText("Motor Setup")
        
        #self.motor_button.setStyleSheet("background-color: lightblue")
        self.property_button = QToolButton()
        self.property_button.adjustSize()
        self.property_button.setStyleSheet("background-color: lightblue")
        self.property_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\property.png'))
        self.property_button.setIcon(icon1)
        self.property_button.setIconSize(QtCore.QSize(60,60))
        self.property_button.setText("Properties")
        
        self.mesh_button = QToolButton()
        self.mesh_button.adjustSize()
        self.mesh_button.setStyleSheet("background-color: lightblue")
        self.mesh_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\mesh.png'))
        self.mesh_button.setIcon(icon1)
        self.mesh_button.setIconSize(QtCore.QSize(60,60))
        self.mesh_button.setText("Mesh Setup")
        
        self.sol_button = QToolButton()
        self.sol_button.adjustSize()
        self.sol_button.setStyleSheet("background-color: lightblue")
        self.sol_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\function.png'))
        self.sol_button.setIcon(icon1)
        self.sol_button.setIconSize(QtCore.QSize(60,60))
        self.sol_button.setText("Solve Setup")
        
        self.cal_button = QToolButton()
        self.cal_button.adjustSize()
        self.cal_button.setStyleSheet("background-color: lightblue")
        self.cal_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\calculation.png'))
        self.cal_button.setIcon(icon1)
        self.cal_button.setIconSize(QtCore.QSize(60,60))
        self.cal_button.setText("Calculation")
        
        self.view_button = QToolButton()
        self.view_button.adjustSize()
        self.view_button.setStyleSheet("background-color: lightblue")
        self.view_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\chart.png'))
        self.view_button.setIcon(icon1)
        self.view_button.setIconSize(QtCore.QSize(60,60))
        self.view_button.setText("Postprocess")
        
        self.geo = QToolButton()
        self.geo.adjustSize()
        self.geo.setStyleSheet("background-color: white")
        self.geo.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\geo.png'))
        self.geo.setIcon(icon1)
        self.geo.setIconSize(QtCore.QSize(45,45))
        self.geo.setText("Geometry")
        
        self.msh = QToolButton()
        self.msh.adjustSize()
        self.msh.setStyleSheet("background-color: white")
        self.msh.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\motormesh.png'))
        self.msh.setIcon(icon1)
        self.msh.setIconSize(QtCore.QSize(45,45))
        self.msh.setText("MeshArea")
        
        self.solve = QToolButton()
        self.solve.adjustSize()
        self.solve.setStyleSheet("background-color: white")
        self.solve.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('icon\\solver.jpg'))
        self.solve.setIcon(icon1)
        self.solve.setIconSize(QtCore.QSize(45,45))
        self.solve.setText(" Solve  ")
        
        leftlayout.setSpacing(10)
        leftlayout.addWidget(self.motor_button)
        leftlayout.addWidget(self.property_button)
        leftlayout.addWidget(self.mesh_button)
        leftlayout.addWidget(self.sol_button)
        leftlayout.addWidget(self.cal_button)
        leftlayout.addWidget(self.view_button)
        leftlayout.addWidget(self.geo)
        leftlayout.addWidget(self.msh)
        leftlayout.addWidget(self.solve)
        self.MenuBox.setLayout(leftlayout)
        self.motor_button.clicked.connect(self.open_motorSetup)
        self.property_button.clicked.connect(self.open_pro)
        self.mesh_button.clicked.connect(self.open_meshGUI)
        self.sol_button.clicked.connect(self.open_solver)
        self.cal_button.clicked.connect(self.open_cal)
        self.view_button.clicked.connect(self.open_view)
        self.geo.clicked.connect(self.show_geo)
    
    def createChildGUI(self):
        self.info()
        self.geometry_chart()
        self.middleleftLayout = QHBoxLayout()
        self.middleleftLayout.addWidget(self.groupInfo)
        self.middleleftLayout.addWidget(self.groupGeo)
        
        
    def info(self):
        self.groupInfo = QGroupBox('Info')
    
    def geometry_chart(self):
        self.groupGeo = QGroupBox('Geometry and Chart')
        self.groupGeo.setFixedWidth(700)
        self.sublayout2 = QVBoxLayout()
        geo_pic = ""
        self.pic = QLabel()
        self.pic.setPixmap(QPixmap(geo_pic))
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.sublayout2.addWidget(self.pic)
        self.groupGeo.setLayout(self.sublayout2)
        
    
    def createErrorConsole(self):
        self.ErrorConsole = QGroupBox("Console")
        self.ErrorConsole.setMaximumWidth(350)
        underLayout = QGridLayout()
        output_console = QtWidgets.QTextBrowser()
        underLayout.addWidget(output_console, 1, 0)
        self.ErrorConsole.setLayout(underLayout)

    def open_motorSetup(self):
        command = "widgets\\motorsetup.py"
        subprocess.Popen(command, shell = True)
        
    def open_pro(self):
        command = "widgets\\properties.py"
        subprocess.Popen(command, shell = True)
    
    def open_meshGUI(self):
        command = "widgets\\meshGUI.py"
        subprocess.Popen(command, shell = True)
    
    def open_solver(self):
        #import fieldcalculationsolver
        command = "widgets\\fieldcalculationsolver.py"
        subprocess.Popen(command, shell = True)
    
    def open_cal(self):
        #import multicalculation
        command = "widgets\\multicalculation.py"
        subprocess.Popen(command, shell = True)
        
    def open_view(self):
        command = "widgets\\fieldviewer.py"
        subprocess.Popen(command, shell = True)
          
    def show_geo(self):
        print(1)
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
        geo_pic = "moduls\\PMSM1\\pmsm_cbmag.png"
        self.pic.setPixmap(QPixmap(geo_pic))
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
    
    def show_msh(self):
        pass
    
    def run_solver(self):
        pass
if __name__=="__main__":    
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
        app.aboutToQuit.connect(app.deleteLater)
    window = UI_Main()
    window.setGeometry(50,50,1800,900)
    window.setWindowTitle("FE-Calculator for Motor")
    window.setWindowIcon(QIcon('icon\\main.jpg'))
    window.show()
    app.exec_()
    sys.exit(0)

