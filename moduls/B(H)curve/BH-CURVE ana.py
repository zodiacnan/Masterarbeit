# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 16:08:08 2017

@author: DINGNAN
"""

Br = 1.150
pu = 1.050
K = 20
Hc = 1500.

nu_1a[] = 100. + 10. * Exp[1.8*SquNorm[$1]] ;
dnudb2_1a[] = 18. * Exp[1.8*SquNorm[$1]] ;
h_1a[] = nu_1a[$1]*$1 ;
