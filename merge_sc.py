import script_principale as sp

def callfunction_merge():
  """
  A1 and B1 for secondary
  A2 and B2 for primary
  """
  line_val = "dataMatrix=0000000000"
  condition = "No"
  process,A1,B1,A2,B2,d1r1,d1r2,d2r1,d2r2,id1,id2 = sp.fonc_decoding() 
  if (A1 == line_val):
    if B1 == B2:
      condition = "Yes"
    else:
      condition = "No"
  else:
    if A1 == A2:
      condition = "Yes"
    else:
      condition = "No"
  return A1,B1,A2,B2,d1r1,d1r2,d2r1,d2r2,id1,id2, condition


