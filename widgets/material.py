# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 09:47:41 2017

@author: DINGNAN
"""

#material distibution

import sys
sys.path.append('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess

class Material(QWidget):
    def __init__(self,parent = None, modal = False):
        super(Material, self).__init__()
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()
    
    def initUI(self):
        self.material_list()
        mainlayout = QVBoxLayout()
        mainlayout.addWidget(self.list_box)
        self.setLayout(mainlayout)
    
    def material_list(self):
        self.list_box = QGroupBox("Materials")
        
        self.add_button = QPushButton('Add Material', self)
        self.modify_button = QPushButton('Modify Material', self)
        self.delete_button = QPushButton('Delete Material', self)
        self.buttonbox = QDialogButtonBox()
        self.buttonbox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.finishbutton = QPushButton("Finish", self)
        self.cancelbutton = QPushButton("Cancel", self)
        self.buttonbox.addButton(self.finishbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.cancelbutton,QDialogButtonBox.ActionRole)
        layout = QGridLayout()
        layout.addWidget(self.add_button, 2, 0)
        layout.addWidget(self.modify_button, 3, 0)
        layout.addWidget(self.delete_button, 4, 0)
        layout.addWidget(self.buttonbox, 5, 0)
        self.list_box.setLayout(layout)
        self.add_button.clicked.connect(self.add_function)
        self.modify_button.clicked.connect(self.modify_function)
        self.delete_button.clicked.connect(self.delete_function)
        self.finishbutton.clicked.connect(self.finish_function)
        self.cancelbutton.clicked.connect(self.cancel)
    
    
    def add_function(self):
        
        command = "addMaterial.py"
        subprocess.Popen(command, shell = True)
        
    
    def modify_function(self):
        command = "modifymaterial.py"
        subprocess.Popen(command, shell = True)
        
    
    def delete_function(self):
        pass
    
    def finish_function(self):
        os.chdir('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\examples')
        filename_m = 'material.pro'
        try: 
            file = open(filename_m, 'w')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        
        f1 = open(filename, 'w+')
        add_content = [add]
        f1.writelines(add_content)
        f1.close()
        self.close()
        
    def cancel(self):
        self.close()
    

        
        
if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = Material()
    window.setWindowTitle('Material')
    window.setGeometry(300,300,400,400)
    window.show()
    app.exec_()
    sys.exit(0)