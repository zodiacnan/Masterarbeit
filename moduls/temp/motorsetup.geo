Include "motorsetupGUI.geo" ;
InitialRotorAngle = InitialRotorAngle_deg*deg2rad ; 
NbrPolePairs = NbrPolesTot/2 ;
Flag_Symmetry = (SymmetryFactor==1)?0:1 ;
NbrSectTot = NbrPolesTot ; 
NbrSect = NbrSectTot*NbrPolesInModel/NbrPolesTot ; 
NbrSectStator   = NbrSectTotStator*NbrPolesInModel/NbrPolesTot; 
Include "dimension.geo" ;
