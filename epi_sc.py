def e_func(primary,secondary):
  with open("emarking-platform-interface.log","r") as file:
    numofline = 0
    e1 = "000000"
    e2 = "000000"
    for line in file:
      numofline+=1
      if "ProductCode" in line and "GET" in line:
        if primary in line:
          e1 = line.split(",")
          e1 = e1[2].split(":")
          e1 = e1[1]
          e1 = e1[1:-1]
          
        if secondary in line:
          e2 = line.split(",")
          e2 = e2[2].split(":")
          e2 = e2[1]
          e2 = e2[1:-1]
    
    return e1,e2
