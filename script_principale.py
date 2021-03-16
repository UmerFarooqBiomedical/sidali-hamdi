def nettoyage_Front(x,y):
    Front_Datamatrix1 = x[6].lstrip('[')
    Front_Datamatrix_final1 = Front_Datamatrix1.replace(",", "")
    Front_Datamatrix2 = y[6].lstrip('[')
    Front_Datamatrix_final2 = Front_Datamatrix2.replace(",", "")
    return Front_Datamatrix_final1, Front_Datamatrix_final2

def nettoyage_Rear(x,y):
    Rear_Datamatrix1 = x[9].lstrip('[')
    Rear_Datamatrix_final1 = Rear_Datamatrix1.replace(",", "")
    Rear_Datamatrix2 = y[9].lstrip('[')
    Rear_Datamatrix_final2 = Rear_Datamatrix2.replace(",", "")
    return Rear_Datamatrix_final1,Rear_Datamatrix_final2

def rotation_val(x,y):
    d1r1 = x[7].replace(']',"")
    d2r1 = y[7].replace(']',"")
    d1r2 = x[10][:11].replace(']',"")
    d2r2 = y[10][:11].replace(']',"")   
    d1r1 = d1r1.replace(",", "")
    d2r1 = d2r1.replace(",", "")
    d1r2 = d1r2.replace(",", "")
    d2r2 = d2r2.replace(",", "")
    return d1r1,d1r2,d2r1,d2r2
  
def id_val(x,y):
    id1 = x[11]
    id1 = id1.replace(",", "")
    id2 = y[11]
    id2 = id2.replace(",", "")
    return id1,id2

data = []  # declaration d'un tablea1
# lire dans un fichier
def fonc_decoding():
    with open("camera-interface.log", "r") as fic:
        decod = fic.readlines()
        # decod1 = fic.readline()
        fic.close()

    numberofline = 0
    for line in decod:
        numberofline += 1

    x = (decod[(numberofline) - 1].split(" "))
    Last_plate1 = x[0]
    
    y = (decod[(numberofline) - 2].split(" "))
    Last_plate2 = y[0]
    A1,A2 = nettoyage_Front(x,y)
    B1,B2 = nettoyage_Rear(x,y)
    d1r1,d1r2,d2r1,d2r2 = rotation_val(x,y)
    id1,id2 = id_val(x,y)
    condition1 = "dataMatrix=0000000000"
    varPrint = ""    
    # une double condition pour verifier ce que vaut les deux Datamatrix
    if A1 == condition1:
        if B1 == condition1:
            varPrint = "Last plate " + str(Last_plate1) + "\n" + "Front " + str(A1) + "\n" + "Rear " + str(B1) + "\n" + "NOK"
        else:
            varPrint = "Last plate " + str(Last_plate1) + "\n" + "Front " + str(A1) + "\n" + "Rear " + str(B1) + "\n" + "OK"
    else:
        varPrint =  "Last plate " + str(Last_plate1) + "\n" + "Front " + str(A1) + "\n" + "Rear " + str(B1) + "\n" + "OK"
    data.append(varPrint)
    return data,A1,B1,A2,B2,d1r1,d1r2,d2r1,d2r2,id1,id2


