Include "pmsm_data.geo";
Include "inputforpro.pro" ;
Include "boundary.pro" ;
Include "function.pro" ;
Include "Nameofresult.pro" ;
If(Flag_SrcType_Stator)
  UndefineConstant["Input/8Load resistance"];
EndIf
If(Flag_Cir)
  Include "pmsm_8p_circuit.pro" ;
EndIf
If(Flag_Calculation == 0)
  Include "machine_magstadyn_a.pro" ;
EndIf
If(Flag_Calculation == 1)
  Include "ldandlq.pro" ;
EndIf
If(Flag_Calculation == 2)
  Include "ironloss.pro" ;
EndIf