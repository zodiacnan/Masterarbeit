# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:41:40 2017

@author: DINGNAN
"""
import numpy as np
import pylab as pl

Mat1_h = [0.0000e+00, 5.5023e+00, 1.1018e+01, 1.6562e+01, 2.2149e+01, 2.7798e+01, 3.3528e+01,
    3.9363e+01, 4.5335e+01, 5.1479e+01, 5.7842e+01, 6.4481e+01, 7.1470e+01, 7.8906e+01,
    8.6910e+01, 9.5644e+01, 1.0532e+02, 1.1620e+02, 1.2868e+02, 1.4322e+02, 1.6050e+02,
    1.8139e+02, 2.0711e+02, 2.3932e+02, 2.8028e+02, 3.3314e+02, 4.0231e+02, 4.9395e+02,
    6.1678e+02, 7.8320e+02, 1.0110e+03, 1.3257e+03, 1.7645e+03, 2.3819e+03, 3.2578e+03,
    4.5110e+03, 6.3187e+03, 8.9478e+03, 1.2802e+04, 1.8500e+04, 2.6989e+04, 3.9739e+04,
    5.9047e+04, 8.8520e+04, 1.3388e+05, 2.0425e+05, 3.1434e+05, 4.8796e+05, 7.6403e+05]

Mat1_b = [0.0000e+00, 5.0000e-02, 1.0000e-01, 1.5000e-01, 2.0000e-01, 2.5000e-01, 3.0000e-01,
    3.5000e-01, 4.0000e-01, 4.5000e-01, 5.0000e-01, 5.5000e-01, 6.0000e-01, 6.5000e-01,
    7.0000e-01, 7.5000e-01, 8.0000e-01, 8.5000e-01, 9.0000e-01, 9.5000e-01, 1.0000e+00,
    1.0500e+00, 1.1000e+00, 1.1500e+00, 1.2000e+00, 1.2500e+00, 1.3000e+00, 1.3500e+00,
    1.4000e+00, 1.4500e+00, 1.5000e+00, 1.5500e+00, 1.6000e+00, 1.6500e+00, 1.7000e+00,
    1.7500e+00, 1.8000e+00, 1.8500e+00, 1.9000e+00, 1.9500e+00, 2.0000e+00, 2.0500e+00,
    2.1000e+00, 2.1500e+00, 2.2000e+00, 2.2500e+00, 2.3000e+00, 2.3500e+00, 2.4000e+00]

pl.plot(Mat1_h, Mat1_b)
pl.grid(True)
pl.xlabel('H -- [A/m]')
pl.ylabel('B -- [T]')
pl.title('B(H) Curve Interpolated')
pl.savefig('C:\\Users\\DINGNAN\\Desktop\\NanDing\\MA\\moduls\\B(H)curve\\BH-Curve_Interpoleted.jpg')
pl.show()
