Include "BH_data.pro"
Function{
  // nu = 100. + 10. * exp ( 1.8 * b * b )
  // analytical
  nu_1a[] = 100. + 10. * Exp[1.8*SquNorm[$1]] ;
  dnudb2_1a[] = 18. * Exp[1.8*SquNorm[$1]] ;
  h_1a[] = nu_1a[$1]*$1 ;
  dhdb_1a[] = TensorDiag[1,1,1] * nu_1a[$1#1] + 2*dnudb2_1a[#1] * SquDyadicProduct[#1]  ;
  dhdb_1a_NL[] = 2*dnudb2_1a[$1#1] * SquDyadicProduct[#1]  ;

  // interpolated

  Mat1_b2 = Mat1_b()^2;
  Mat1_nu = Mat1_h()/Mat1_b();
  Mat1_nu(0) = Mat1_nu(1);

  Mat1_nu_b2 = ListAlt[Mat1_b2(), Mat1_nu()] ;
  nu_1[] = InterpolationLinear[ SquNorm[$1] ]{Mat1_nu_b2()} ;
  dnudb2_1[] = dInterpolationLinear[SquNorm[$1]]{Mat1_nu_b2()} ;
  h_1[] = nu_1[$1] * $1 ;
  dhdb_1[] = TensorDiag[1,1,1] * nu_1[$1#1] + 2*dnudb2_1[#1] * SquDyadicProduct[#1]  ;
  dhdb_1_NL[] = 2*dnudb2_1[$1#1] * SquDyadicProduct[#1] ;
}
