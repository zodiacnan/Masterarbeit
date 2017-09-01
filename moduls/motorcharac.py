# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:24:41 2017

@author: DINGNAN
"""

import numpy as np

class PMSM(object):
    """
    ::param NbrPhase: number of winding phase
    ::
    """
    

class characteristics():
    """Standard set of PMSM given by Is and beta(Lastwinkel):
        NbrPolesTot number of Pol
        NbrPolePairs number of pole pair
        ld d-inductance in H
        lq q-inductance in H
        beta angel Is vs Up in degrees
        Is Current in A
        
        psid D-Flux in Vs
        psid Q-Flux in Vs
    """
    r = dict(id=[], iq=[], beta=[],psid=[],psiq=[],T=[])
    beta = np.array(beta)/180.0*np.pi
    def idiq(self,NbrPolePairs,Is, beta):
        id = Is*np.sin(beta)/np.sin(np.pi-np.pi/NbrPolePairs)
        iq = Is*np.sin(np.pi/NbrPolePairs-beta)/np.sin(np.pi-np.pi/NbrPolePairs)
        return id,iq
    def torque_idq(self,NbrPolePairs, id, iq, psid, psiq):
        """
        Torque from id iq psid psidq
        """
        t_sim = (3/2)*NbrPolePairs*(psid*iq-psiq*iq)
        return t_sim
    
    