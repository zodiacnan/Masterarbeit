Group {
  Stator_Fe     = Region[STATOR_FE] ;
  Stator_Al     = Region[{}];
  Stator_Cu     = Region[{}];
  Stator_Air    = Region[STATOR_AIR] ;
  Stator_Airgap = Region[STATOR_AIRGAP] ;
  Stator_Bnd_A0 = Region[STATOR_BND_A0] ;
  Stator_Bnd_A1 = Region[STATOR_BND_A1] ;

  Rotor_Fe     = Region[ROTOR_FE] ;
  Rotor_Al     = Region[{}];
  Rotor_Cu     = Region[{}];
  Rotor_Fe     = Region[ROTOR_FE] ;
  Rotor_Air    = Region[ROTOR_AIR] ;
  Rotor_Airgap = Region[ROTOR_AIRGAP] ;
  Rotor_Bnd_A0 = Region[ROTOR_BND_A0] ;
  Rotor_Bnd_A1 = Region[ROTOR_BND_A1] ;

  MovingBand_PhysicalNb = Region[MOVING_BAND] ;  // Fictitious number for moving band, not in the geo file
  Surf_Inf = Region[SURF_EXT] ;
  Surf_bn0 = Region[SURF_INT] ;
  Surf_cutA0 = Region[{STATOR_BND_A0, ROTOR_BND_A0}];
  Surf_cutA1 = Region[{STATOR_BND_A1, ROTOR_BND_A1}];

  Dummy = Region[NICEPOS]; // For getting the movement of the rotor

  nbMagnets = NbrPolesTot/SymmetryFactor ;
  For k In {1:nbMagnets}
    Rotor_Magnet~{k} = Region[ (ROTOR_MAGNET+k-1) ];
    Rotor_Magnets += Region[ Rotor_Magnet~{k} ];
  EndFor

  nbInds = (Flag_Symmetry) ? NbrPolesInModel*NbrSectTotStator/NbrPolesTot : NbrSectTotStator ;
  Printf("NbrPolesInModel=%g, nbInds=%g SymmetryFactor=%g",
    NbrPolesInModel, nbInds, SymmetryFactor);

  Stator_Ind_Ap = Region[{}];            Stator_Ind_Am = Region[STATOR_IND_AM];
  Stator_Ind_Bp = Region[{}];            Stator_Ind_Bm = Region[STATOR_IND_BM];
  Stator_Ind_Cp = Region[STATOR_IND_CP]; Stator_Ind_Cm = Region[{}];
  If(NbrPolesInModel > 1)
    Stator_Ind_Ap += Region[STATOR_IND_AP];
    Stator_Ind_Bp += Region[STATOR_IND_BP];
    Stator_Ind_Cm += Region[STATOR_IND_CM];
  EndIf

  PhaseA = Region[{Stator_Ind_Ap, Stator_Ind_Am}];
  PhaseB = Region[{Stator_Ind_Bp, Stator_Ind_Bm}];
  PhaseC = Region[{Stator_Ind_Cp, Stator_Ind_Cm}];

  // FIXME: Just one physical region for nice graph in Onelab
  PhaseA_pos = Region[Stator_Ind_Am];
  PhaseB_pos = Region[Stator_Ind_Bm];
  PhaseC_pos = Region[Stator_Ind_Cp];

  Stator_IndsP = Region[{Stator_Ind_Ap, Stator_Ind_Bp, Stator_Ind_Cp}];
  Stator_IndsN = Region[{Stator_Ind_Am, Stator_Ind_Bm, Stator_Ind_Cm}];

  Stator_Inds = Region[{PhaseA, PhaseB, PhaseC}] ;
  Rotor_Inds  = Region[{}] ;

  StatorC  = Region[{}] ;
  StatorCC = Region[{Stator_Fe}] ;
  RotorC   = Region[{}] ;
  RotorCC  = Region[{Rotor_Fe, Rotor_Magnets}] ;

  // Moving band:  with or without symmetry, these BND lines must be complete
  Stator_Bnd_MB = Region[STATOR_BND_MOVING_BAND];
  For k In {1:SymmetryFactor}
    Rotor_Bnd_MB~{k} = Region[ (ROTOR_BND_MOVING_BAND+k-1) ];
    Rotor_Bnd_MB += Region[ Rotor_Bnd_MB~{k} ];
  EndFor
  Rotor_Bnd_MBaux = Region[ {Rotor_Bnd_MB, -Rotor_Bnd_MB~{1}}];

}
