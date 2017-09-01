rpm_nominal = 1000;
II=50;
ID = 50.0;
IQ = 3.06161699787e-15;
thetaMax_deg =15;
theta0   = InitialRotorAngle  + 0. ;
delta_theta_deg = 1;
Flag_AnalysisType = 1 ;
Flag_SrcType_Stator =  1 ; 
Flag_Cir = !Flag_SrcType_Stator ; 
Flag_ImposedCurrentDensity = Flag_SrcType_Stator ; 
Flag_ParkTransformation = 1 ;
Include "inputsolverGUI.pro"