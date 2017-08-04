
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:49:56 2017

@author: DINGNAN
"""

# -*-# -*- coding: utf-8 -*-
# Mesh with GMSH inside of FreeCAD
# Run GetDp after Meshing
# License: LGPL v 2.1


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class MeshGmsh(QWidget):
    def __init__(self,*args,**kwargs):
        super(MeshGmsh, self).__init__()
        self.setWindowTitle("Mesh Options")
        self.setWindowIcon(QIcon('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls\icon\main.jpg'))
        self.initUI()


    def initUI(self):
        main = QVBoxLayout()
        
        
        # Optimized:
        self.cb_optimized = QCheckBox("  Optimized 2D", self)
        self.cb_optimized.setChecked(QtCore.Qt.Checked)
        # Algorithm:
        self.l_algorithm =QLabel("  Mesh Algorithm ", self)
        self.cmb_algorithm = QComboBox(self)
        self.algorithm_list = [ self.tr('Meshadapt'),  self.tr('Delaunay'), self.tr('Front'), ]
        self.cmb_algorithm.addItems(self.algorithm_list)
        self.cmb_algorithm.setCurrentIndex(0)
        # Format:
        self.l_format = QLabel("  Mesh Format ", self)
        self.cmb_format = QComboBox(self)
        self.format_list = [ self.tr('msh'), self.tr('unv'), self.tr('stl') ,self.tr('bdf'), self.tr('med'),]
        self.cmb_format.addItems(self.format_list)
        self.cmb_format.setCurrentIndex(0)
        self.stored_cmb_format_index = 0
        # Element max size:
        self.cb_max_elme_size = QCheckBox("  Maximum mesh element size", self)
        self.cb_max_elme_size.setChecked(QtCore.Qt.Checked)
        self.sb_max_element_size = QDoubleSpinBox(self)
        self.sb_max_element_size.setValue(5.0)
        self.sb_max_element_size.setMaximum(10000000.0)
        self.sb_max_element_size.setMinimum(0.00000001)
        # Element min size:
        self.cb_min_elme_size = QCheckBox("  Minimum mesh element size", self)
        self.cb_min_elme_size.setChecked(QtCore.Qt.Checked)
        self.sb_min_element_size = QDoubleSpinBox(self)
        self.sb_min_element_size.setValue(1.0)
        self.sb_min_element_size.setMaximum(10000000.0)
        self.sb_min_element_size.setMinimum(0.00000001)
        # Set Mesh Order:
        self.cb_mesh_order = QLabel("    Mesh Order", self)
        self.sb_mesh_order = QSpinBox(self)
        self.sb_mesh_order.setValue(1)
        self.sb_mesh_order.setMaximum(5)
        self.sb_mesh_order.setMinimum(1)
        
        self.auto_save = QCheckBox("  Show Last Mesh Step ", self)
        self.auto_save.setChecked(QtCore.Qt.Checked)
        
        self.l_cmd_line_opt = QPushButton("Custom Options", self)
        self.le_cmd_line_opt = QLineEdit(self)
        self.le_cmd_line_opt.setToolTip("Those option will be appended to gmsh command line call")

        # Mesh Button:
        
        self.buttonbox = QDialogButtonBox()
        self.buttonBox = QDialogButtonBox(QtCore.Qt.Horizontal)
        self.meshbutton = QPushButton("Save", self)
        self.returnbutton = QPushButton("Return", self)
        self.showbutton = QPushButton("Mesh", self)
        self.buttonbox.addButton(self.meshbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.returnbutton,QDialogButtonBox.ActionRole)
        self.buttonbox.addButton(self.showbutton,QDialogButtonBox.ActionRole)
        
        # show the mesh result 
        
        # Layout:
        layout = QGridLayout()
        layout.addWidget(self.cb_optimized, 2, 0)
        layout.addWidget(self.l_algorithm, 3, 0)
        layout.addWidget(self.cmb_algorithm, 3, 1)
        layout.addWidget(self.l_format, 4, 0)
        layout.addWidget(self.cmb_format, 4, 1)
        layout.addWidget(self.cb_max_elme_size, 5, 0)
        layout.addWidget(self.sb_max_element_size, 5, 1)
        layout.addWidget(self.cb_min_elme_size, 6, 0)
        layout.addWidget(self.sb_min_element_size, 6, 1)
        layout.addWidget(self.cb_mesh_order, 7, 0)
        layout.addWidget(self.sb_mesh_order, 7, 1)
        layout.addWidget(self.auto_save, 8, 0)
        layout.addWidget(self.l_cmd_line_opt, 9, 0)
        layout.addWidget(self.le_cmd_line_opt, 9, 1) 
        
        
        main.addLayout(layout)
        main.addWidget(self.buttonbox)
        self.setLayout(main)
        # Connectors:
        self.meshbutton.clicked.connect(self.setup_gmsh)
        self.showbutton.clicked.connect(self.run_gmsh)
        self.cb_max_elme_size.stateChanged.connect(self.max_size_state)
        self.cb_min_elme_size.stateChanged.connect(self.min_size_state)
        self.l_cmd_line_opt.clicked.connect(self.custom_options)
        
    def max_size_state(self, state):
        if state == QtCore.Qt.Checked:
            self.sb_max_element_size.setEnabled(True)
        else:
            self.sb_max_element_size.setEnabled(False)

    def min_size_state(self, state):
        if state == QtCore.Qt.Checked:
            self.sb_min_element_size.setEnabled(True)
        else:
            self.sb_min_element_size.setEnabled(False)

    def custom_options(self):
        import webbrowser
        webbrowser.open('http://www.manpagez.com/info/gmsh/gmsh-2.4.0/gmsh_76.php#SEC76')
    
	
    def cancel(self):
        self.close()
        
    def run_gmsh(self):
        os.chdir('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\')
        import subprocess
        filename = "moduls\\PMSM1\\pmsm_cbmag.geo"
        command_1 = "gmsh.exe -run "+ filename
        subprocess.Popen(command_1, shell = True)
        #command_2 = "gmsh.exe msh.pos"
        #subprocess.Popen(command_2, shell = True)
    def setup_gmsh(self):
        algo = self.cmb_algorithm.currentText()
        file_format = self.cmb_format.currentText()
        clmax = self.sb_max_element_size.text()
        clmin = self.sb_min_element_size.text()
        cmd_line_opt = self.le_cmd_line_opt.text()
        
        mesh_order = self.sb_mesh_order.text()
        if algo == 'Meshadapt':
            algo_in = 'Mesh.Algorithm = 1 ;\n'
        if algo == 'Delaunay':
            algo_in = 'Mesh.Algorithm = 5 ;\n'
        if algo == 'Front':
            algo_in = 'Mesh.Algorithm = 6 ;\n'
            
        if file_format == 'msh':
            format_m = 'Mesh.Format = 1 ;\n'
        if file_format == 'unv':
            format_m = 'Mesh.Format = 2 ;\n'
        if file_format == 'stl':
            format_m = 'Mesh.Format = 27 ;\n'
        if file_format == 'med':
            format_m = 'Mesh.Format = 33 ;\n'
        
        mesh_order_in = 'Mesh.ElementOrder = ' + str(mesh_order) + ';\n'
        
        if self.cb_optimized.isChecked():
            cmd_optimize = 'Mesh.Optimize = 1 ;\n'
        else:
            cmd_optimize = ''
            
        if self.cb_max_elme_size.isChecked():
            max_size = 'Mesh.CharacteristicLengthMax =  ' + str(clmax) + ';\n'
        else:
            max_size = ''
        if self.cb_min_elme_size.isChecked():
            min_size = 'Mesh.CharacteristicLengthMin =  ' + str(clmin) + ';\n'
        else:
            min_size = ''
            
        if self.auto_save.isChecked():
            Auto = 'Solver.AutoShowLastStep = 1; \n'
        else:
            Auto = 'Solver.AutoShowLastStep = 0; \n'
        
        os.chdir('C:\Users\DINGNAN\Desktop\NanDing\MA\moduls')
        filename = 'mesh' + '.geo'
        try: 
            file = open(filename, 'w')
            file.truncate()
            file.close()
        except:
            print('Something went wrong')
        
        f1 = open(filename, 'w+')
        add_content = [algo_in, format_m,  cmd_optimize, max_size, min_size,cmd_line_opt, Auto]
        f1.writelines(add_content)
        f1.close()
        
        

if __name__=="__main__":
    # Create Qt App
    app= QApplication.instance()
    if app == None:
        app = QApplication(sys.argv)
    window = MeshGmsh()
    window.show()
    app.exec_()
    sys.exit(0)