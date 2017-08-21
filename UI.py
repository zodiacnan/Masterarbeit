
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 18:48:25 2017

@author: DINGNAN
"""

import os
os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import subprocess
import pickle

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
        command = "widgets\\openexample.py"
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
        subprocess.call('notepad new.pro',shell = True)
    
    def Material_B(self):
        pass
    
    def About_FEM(self):
        import webbrowser
        webbrowser.open('https://github.com/zodiacnan/Masterarbeit')
    
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
        self.MenuBox = QGroupBox()
        self.MenuBox.setMaximumWidth(120)
        self.MenuBox.setStyleSheet("border: no;")
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
        self.geo.clicked.connect(self.datatemp)
        self.mesh_button.clicked.connect(self.open_meshGUI)
        self.sol_button.clicked.connect(self.open_solver)
        self.cal_button.clicked.connect(self.open_cal)
        self.view_button.clicked.connect(self.open_view)
        self.geo.clicked.connect(self.show_geo)
        self.msh.clicked.connect(self.show_msh)
        
    
    def createChildGUI(self):
        self.info()
        self.geometry_chart()
        self.middleleftLayout = QHBoxLayout()
        self.middleleftLayout.addWidget(self.groupInfo)
        self.middleleftLayout.addWidget(self.groupGeo)
        
        
    def info(self):
        self.dimension()
        self.setup()
        self.function()
        self.groupInfo = QGroupBox('Information')
        self.groupInfo.setFixedWidth(500)
        self.infolayout = QVBoxLayout()
        self.infolayout.addWidget(self.text)
        self.infolayout.addLayout(self.layout1)
        self.infolayout.addWidget(self.text2)
        self.infolayout.addLayout(self.layout2)
        self.infolayout.addWidget(self.text3)
        self.infolayout.addLayout(self.layout3)
        self.infolayout.setStretch(1,1)
        self.infolayout.setStretch(2,1)
        self.infolayout.setStretch(3,1)
        self.infolayout.setStretch(4,1)
        self.groupInfo.setLayout(self.infolayout)
    
    
    def datatemp(self):
        a = ''
        b = ''
        c = ''
        d = ''
        e = ''
        f = ''
        g = ''
        try:
            fp = open("temptoUI.pkl",'r')
            shared = pickle.load(fp)
            print(shared)
            for i in range(0,len(shared)):
                print(len(shared))
                a = str(shared[0])
                b = str(shared[1])
                c = str(shared[2])
                d = str(shared[3])   
        except:
            print("No load")
            a = ''
            b = ''
            c = ''
            d = ''
        try:
            fp = open("temptoUI2.pkl",'r')
            shared2 = pickle.load(fp)
            print(shared2)
            for i in range(0,len(shared)):
                print(len(shared2))
                e = str(shared2[0])
                f = str(shared2[1])
                g = str(shared2[2])
        except:
            print("No load")
            e = ''
            f = ''
            g = ''
        self.outers_t.setText(d)
        self.inners_t.setText(c)
        self.outerr_t.setText(b)
        self.innerr_t.setText(a)
        self.slots_t.setText(e)
        self.slotr_t.setText(f)      
        self.shaft_d_t.setText(g)
        
    def dimension(self):
        self.layout1 = QVBoxLayout()
        self.layout11 = QHBoxLayout()
        font = QtGui.QFont("verdana",10)
        font.setUnderline(True)
        font2 = QtGui.QFont("verdana",9)
        font2.setUnderline(True)
        self.text = QLabel("Geometry and Preprocessor",self)
        self.text.setFont(font)
        self.main_dimension = QLabel("Main dimension",self)
        self.main_dimension.setFont(font2)
        self.property = QLabel("Properties",self)
        self.property.setFont(font2)
        self.outers = QLabel("Outer diameter",self)
        self.inners = QLabel("Inner diameter",self)
        self.slots = QLabel("Slot",self)
        
        self.outerr = QLabel("Outer diameter",self)
        self.innerr = QLabel("Inner diameter",self)
        self.slotr = QLabel("Slot",self)
        
        self.shaft_d = QLabel("Diameter",self)
        
        self.outers_t = QLabel(self)
        self.inners_t = QLabel(self)
        self.outerr_t = QLabel(self)
        self.innerr_t = QLabel(self)
        self.slots_t = QLabel('',self)
        self.slotr_t = QLabel('',self)        
        self.shaft_d_t = QLabel("",self)
        self.outers_t.setText('')
        self.inners_t.setText('')
        self.outerr_t.setText('')
        self.innerr_t.setText('')
        self.slots_t.setText('')
        self.slotr_t.setText('')      
        self.shaft_d_t.setText('')
        
        
        self.material_list = QLabel("Fe\nAir\nCu")
        self.boundary_list = QLabel("Magnetic potential\nA = 0")
        self.material = QGroupBox("Materials")
        self.boundary = QGroupBox("Boundary Condition")

        self.stator = QGroupBox("Stator",self)
        self.rotor = QGroupBox("Rotor",self)
        self.shaft = QGroupBox("Shaft",self)
        
        self.grid1 = QGridLayout()
        self.grid2 = QGridLayout()
        self.grid3 = QGridLayout()
        self.gridm = QGridLayout()
        self.gridbd = QGridLayout()
        self.layout1.addWidget(self.main_dimension)
        self.layout1.addWidget(self.stator)
        self.layout1.addWidget(self.rotor)
        self.layout1.addWidget(self.shaft)
        self.layout1.addWidget(self.property)
        self.material.setLayout(self.gridm)
        self.boundary.setLayout(self.gridbd)
        self.layout11.addWidget(self.material)
        self.layout11.addWidget(self.boundary)
        self.layout1.addLayout(self.layout11)
        
        self.grid1.addWidget(self.outers,1,0)
        self.grid1.addWidget(self.inners,2,0)
        self.grid1.addWidget(self.slots,3,0)
        self.grid2.addWidget(self.outerr,1,0)
        self.grid2.addWidget(self.innerr,2,0)
        self.grid2.addWidget(self.slotr,3,0)
        self.grid3.addWidget(self.shaft_d,1,0)
        
        self.grid1.addWidget(self.outers_t,1,1)
        self.grid1.addWidget(self.inners_t,2,1)
        self.grid1.addWidget(self.slots_t,3,1)
        self.grid2.addWidget(self.outerr_t,1,1)
        self.grid2.addWidget(self.innerr_t,2,1)
        self.grid2.addWidget(self.slotr_t,3,1)
        self.grid3.addWidget(self.shaft_d_t,1,1)
        
        self.gridm.addWidget(self.material_list,1,0)
        self.gridbd.addWidget(self.boundary_list,1,0)
        self.stator.setLayout(self.grid1)
        self.rotor.setLayout(self.grid2)
        self.shaft.setLayout(self.grid3)
        
    def setup(self):
        self.layout2 = QVBoxLayout()
        font = QtGui.QFont("verdana",10)
        font.setUnderline(True)
        self.text2 = QLabel("Solver",self)
        self.text2.setFont(font)
        
        self.s_name = QLabel("GetDp -- Linear/Nonlinear",self)
        self.field = QLabel("Electromagnitic field",self)
        self.analysis = QLabel("Steady State/Time domain/Frequency domain")
        
        self.gridsolve = QGridLayout()
        self.solverbox = QGroupBox("")
        self.solverbox.setLayout(self.gridsolve)
        self.gridsolve.addWidget(self.s_name,1,0)
        self.gridsolve.addWidget(self.field,2,0)
        self.gridsolve.addWidget(self.analysis,3,0)
        self.layout2.addWidget(self.solverbox)
        
    def function(self):
        self.layout3 = QVBoxLayout()
        font = QtGui.QFont("verdana",10)
        font.setUnderline(True)
        self.text3 = QLabel("Function")
        self.text3.setFont(font)
        self.label0 = QLabel("Special Fast",self)
        self.label1 = QLabel("Plot",self)
        self.label2 = QLabel("Field",self)
        self.label3 = QLabel("Value Table",self)
        
        self.label01 = QLabel("Induction Identification \nLoss Calculation \nEfficiency Plot ")
        
        self.funcform = QGridLayout()
        
        self.funcform.addWidget(self.label0,1,0)
        self.funcform.addWidget(self.label1,2,0)
        self.funcform.addWidget(self.label2,3,0)
        self.funcform.addWidget(self.label3,4,0)
        self.func_box = QGroupBox("")
        
        self.func_box.setLayout(self.funcform)
        self.layout3.addWidget(self.func_box)
    
    def geometry_chart(self):
        self.groupGeo = QGroupBox('Geometry and Chart')
        self.groupGeo.setFixedWidth(700)
        self.sublayout2 = QVBoxLayout()
        geo_pic = "C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\icon\\pmsm.JPG"
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
        command = "widgets\\view.py"
        subprocess.Popen(command, shell = True)
    def show_geo(self):
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
        geo_pic = "moduls\\PMSM1\\pmsm_cbmag.png"
        self.pic.setPixmap(QPixmap(geo_pic))
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
    
    def show_msh(self):
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
        geo_pic = "moduls\\PMSM1\\pmsm_cbmag_msh.png"
        self.pic.setPixmap(QPixmap(geo_pic))
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
    
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

