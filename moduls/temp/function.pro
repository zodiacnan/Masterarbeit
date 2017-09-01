Function {

  // For a radial remanent b
  For k In {1:nbMagnets}
    br[ Rotor_Magnet~{k} ] = (-1)^(k-1) * b_remanent * Vector[ Cos[Atan2[Y[],X[]]], Sin[Atan2[Y[],X[]]], 0 ];
  EndFor

  NbWires[]  = 104 ; 
  nbSlots[] = Ceil[nbInds/NbrPhases/2] ;
  SurfCoil[] = SurfaceArea[]{STATOR_IND_AM}/nbSlots[] ;
  FillFactor_Winding = 0.5 ; 
  Factor_R_3DEffects = 1.5 ; 
  //--------------------------------------------------
/*
  Surface_PM[] = SurfaceArea[]{ROTOR_MAGNET};

  DefineConstant[ SurfPM = {Surface_PM[ROTOR_MAGNET], ReadOnly 1,
                          Path "Output/2", Highlight "LightYellow" } ];
*/
  //--------------------------------------------------




  rpm = rpm_nominal;
  wr = rpm/60*2*Pi ; // speed in rad_mec/s

  // supply at fixed position
  Freq = wr*NbrPolePairs/(2*Pi) ;
  Omega = 2*Pi*Freq ;
  T = 1/Freq ;


  thetaMax = thetaMax_deg * deg2rad ; // end rotor angle (used in doing a loop)

  NbTurns  = (thetaMax-theta0)/(2*Pi);
  delta_theta_deg =  1.;

  delta_theta[] = delta_theta_deg * deg2rad ;

  time0 = 0 ; // at initial rotor position
  delta_time = delta_theta_deg * deg2rad/wr;
  timemax = thetaMax/wr;

  NbSteps = Ceil[(timemax-time0)/delta_time];

  RotorPosition[] = InitialRotorAngle + $Time * wr ;
  RotorPosition_deg[] = RotorPosition[]*180/Pi;

  
  Theta_Park[] = ((RotorPosition[] + Pi/8) - Pi/6) * NbrPolePairs; // electrical degrees
  Theta_Park_deg[] = Theta_Park[]*180/Pi;

  
}