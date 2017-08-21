# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:48:30 2017

@author: DINGNAN
"""

#boundary condition


import sys
sys.path.append('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess

class Condition(QWidget):
    def __init__(self,parent = None, modal = False):
        super(Condition, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()
    
    def initUI(self):
        self.material_list()
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.list_box)
        self.setLayout(mainlayout)
    
    def material_list(self):
        self.list_box = QGroupBox("Name")
        self.add_button = QPushButton('Add Boundary Condition', self)
        self.modify_button = QPushButton('Modify Boundary Condition', self)
        self.delete_button = QPushButton('Delete Boundary Condition', self)
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.autobutton = QPushButton("Automatic", self)
        self.finishbutton = QPushButton("Finish", self)
        self.cancelbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.autobutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.finishbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.cancelbutton,QDialogButtonBox.ActionRole)
        layout = QGridLayout()
        #layout.addWidget(self.ex_file, 1, 0)
        layout.addWidget(self.add_button, 3, 0)
        layout.addWidget(self.modify_button, 4, 0)
        layout.addWidget(self.delete_button, 5, 0)
        layout.addWidget(self.buttonbox, 6, 0)
        self.list_box.setLayout(layout)
        self.add_button.clicked.connect(self.add_bc)
        self.modify_button.clicked.connect(self.modify_bc)
        self.delete_button.clicked.connect(self.delete_bc)
        self.finishbutton.clicked.connect(self.finish_bc)
        self.cancelbutton.clicked.connect(self.cancel)
    
        
    
    def add_bc(self):
        command = "addcondition.py"
        subprocess.Popen(command, shell = True)
    
    def modify_bc(self):
        command = "modifycondition.py"
        subprocess.Popen(command, shell = True)
    
    def delete_bc(self):
        command = ".py"
        subprocess.Popen(command, shell = True)
    
    def finish_bc(self):
        os.chdir('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\examples')
        filename_m = 'condition.pro'
        try: 
            file = open(filename_m, 'w')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        add = 'a'
        f1 = open(filename_m, 'w+')
        add_content = [add]
        f1.writelines(add_content)
        f1.close()
    
    def cancel(self):
        self.close()

        
        
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Condition()
    window.setWindowTitle('Boundary Condition')
    window.setGeometry(300,300,400,400)
    window.show()
    app.exec_()
    sys.exit(0)