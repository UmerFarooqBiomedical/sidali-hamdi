def callfunction_decod():
    import script_principale as sp
    process,A,B,C,D,d1r1,d1r2,d2r1,d2r2,id1,id2= sp.fonc_decoding()
    
    newtext = "\nDecoding\n\n"
    text = newtext+process[-1]
    error = ""
    state = 0
    if "OK" in str(process[-1]):

        bg_color = "green"
        state = 1
        error = ""

    if "NOK" in str(process[-1]):
        bg_color = "orange"
        state = 2
        error = " E9 : Last plate undecoded or not e-marked."

    
    return state, text, bg_color, error