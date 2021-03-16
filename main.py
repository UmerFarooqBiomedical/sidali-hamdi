import time
import tkinter as tk
import decoding_sc as dcs
import detection_sc as dts
import merge_sc as mgs
import epi_sc as epi
import threading
import csv

class Fenetre(tk.Tk):
  def __init__(self):
      """
      Initialization function
      "self" means root window.
      """
      tk.Tk.__init__(self)
      self.title("INTERFACE PANEL PC") #window title
      self.minsize(990 , 460)
      
      self.sidebar = tk.Frame(self, width =200) #setting frame size and style
      self.sidebar.place(relx=0, rely=0 ,relheight=1, relwidth=0.25)
      
      self.b1= tk.Button(self.sidebar ,bg="#8CB6D8" , text="HOME", font=("Verdana", 15),state="disabled", command = self.f_home)
      self.b1.place(relx=0, rely=0 ,relheight=0.32, relwidth=1)
      self.b2= tk.Button(self.sidebar, bg="#8CB6D8", text="MERGE", font=("Verdana", 15),state="normal", command = self.f_merge)
      self.b2.place(relx=0, rely=0.32 ,relheight=0.32, relwidth=1)
      self.b3= tk.Button(self.sidebar, bg="#8CB6D8", text="PARSER",font=("Verdana", 15))
      self.b3.place(relx=0, rely=0.64 ,relheight=0.32, relwidth=1)
      self.elabel1= tk.Label(self.sidebar ,text="System log : ",font=("Verdana", 10), justify="center")
      self.elabel1.place(relx=0, rely=0.96 ,relheight=0.04, relwidth=1)
      
      text = "Decoding"
      self.error = "No issues. System working fine."
      self.ecolor = "Green"
      self.f_frame = tk.Frame(self)
      self.f_frame.place(relx=0.25, rely=0 ,relheight=1, relwidth=0.75)
      self.b4= tk.Label(self.f_frame ,text=text,font=("Verdana", 25), justify="center")
      self.b4.place(relx=0, rely=0 ,relheight=0.32, relwidth=1)
      self.b5= tk.Label(self.f_frame,  text="text",font=("Verdana", 25), justify="center")
      self.b5.place(relx=0, rely=0.32 ,relheight=0.32, relwidth=1)
      self.b7= tk.Button(self.f_frame, text="\nCLOUD\n",font=("Verdana", 25), justify="center")
      self.b7.place(relx=0, rely=0.64 ,relheight=0.32, relwidth=1)
      self.elabel2= tk.Label(self.f_frame, text=self.error, font=("Verdana", 10), fg = self.ecolor, justify="center")
      self.elabel2.place(relx=0, rely=0.96 ,relheight=0.04, relwidth=1)
      self.y = 0
      self.condition = False
      self.t2 = threading.Thread(target=self.worker2) #calling threading process
      self.t2.start() #Start thread
      
  def action1(self):
    """
    Secondary button function
    """
    print("Secondary button pressed")

  def confirm_click(self):
    """
    Confirm button function
    Creates csv file.
    """
    self.y +=1
    row_list = [["Label", "Frontplate","Rotation", "End Plate","Rotation","ID"],
             ["Primary",self.A2, self.d2r1,self.B2,self.d2r2,self.id2],
             ["Secondary",self.A1, self.d1r1,self.B1,self.d1r2,self.id1]]
    with open('output{}.csv'.format(self.y), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
      
  def f_home(self):
    """
    Home Button Function
    """
    self.b2.configure(state="normal")
    self.b1.configure(state="disabled")
    self.s_frame.place_forget()
    self.f_frame.place(relx=0.25, rely=0 ,relheight=1, relwidth=0.75)
    
  def f_merge(self):
    """
    Merge Button Function
    """
    self.b1.configure(state="normal")
    self.b2.configure(state="disabled")
    if self.condition ==False:
      self.l_text = "0000000000"
      self.number1 = "0000000000"
      self.number2 = "0000000000"
      self.condition = True
    else:
      self.l_text = self.B1[-10:]
      self.number1 = self.B2[-10:]
      self.number2 = self.B1[-10:]
    self.f_frame.place_forget()
    
    self.s_frame = tk.Frame(self)
    self.s_frame.place(relx=0.25, rely=0.1 ,relheight=1, relwidth=0.75)
    self.b8= tk.Label(self.s_frame ,text="Last DMC decoded : ",font=("Verdana", 15), justify="center")
    self.b8.place(relx=0.05, rely=0 ,relheight=0.1, relwidth=0.3)
    
    self.b9= tk.Label(self.s_frame ,text=self.l_text,font=("Verdana", 15),bg="#8CB6D8",fg="#ffffff", justify="center", borderwidth=4, relief="ridge")
    self.b9.place(relx=0.33, rely=0 ,relheight=0.08, relwidth=0.3)
    
    self.b10 = tk.Button(self.s_frame,bg="#8CB6D8", text="Secondary", font=("Verdana", 15), command = self.action1 )
    self.b10.place(relx=0.38, rely=0.15 ,relheight=0.08, relwidth=0.2)
    
    self.l_frame = tk.Frame(self.s_frame,highlightbackground="black",highlightthickness=3)
    self.l_frame.place(relx=0.1, rely=0.35 ,relheight=0.3, relwidth=0.8)
    
    
    self.product1 = "000000"
    self.product2 = "000000"
    self.label_text = ["Operator Choice:", "Plate", self.number1,"- Product # ", self.product1, 
                       "is", "primary", "Plate", self.number2, "- Product # ", self.product2, 
                       "is", "secondary"]
    self.label_color = ["red","black","green","red","red","black","black","black",
                        "green","red","red","black","black"]
    self.label_font = [("Verdana", 15),("Verdana", 15),("Verdana", 15),("Verdana", 15),("Verdana", 15),("Verdana", 15),
                       ("Verdana bold", 15),("Verdana", 15),("Verdana", 15),("Verdana", 15),("Verdana", 15),("Verdana", 15),
                       ("Verdana bold", 15)]
    
    self.label_y = [0.1,0.4,0.4,0.4,0.4,0.4,0.4,0.7,0.7,0.7,0.7,0.7,0.7]
    self.label_x = [0.3,0.0005,0.12,0.35,0.60,0.75,0.79,0.0005,0.12,0.35,0.60,0.75,0.79]
    self.label_width = [0.4,0.15,0.24,0.32,0.15,0.05,0.2,0.15,0.24,0.32,0.15,0.05,0.2]
    self.b11 = {}
    for i in range(13):
      self.b11[i]= tk.Label(self.l_frame ,text=self.label_text [i],font=self.label_font[i],fg=self.label_color[i], justify="center")
      self.b11[i].place(relx=self.label_x[i], rely=self.label_y[i] ,relheight=0.2, relwidth=self.label_width[i])
    
    self.b12 = tk.Button(self.s_frame,bg="#8CB6D8", text="Confirm", font=("Verdana", 15),state="normal", command = self.confirm_click )
    self.b12.place(relx=0.38, rely=0.75 ,relheight=0.08, relwidth=0.2)
    self.elabel2= tk.Label(self.s_frame, text=self.error, font=("Verdana", 10), fg = self.ecolor, justify="center")
    self.elabel2.place(relx=0, rely=0.86 ,relheight=0.04, relwidth=1)

    
  def worker2(self):
    """
    Worker function which performs different tasks in separate thread.
    """
    
    try:
      x = 0
      
      while True:
        if self.condition == True:
          self.A1,self.B1,self.A2,self.B2,self.d1r1,self.d1r2,self.d2r1,self.d2r2,self.id1,self.id2, condition = mgs.callfunction_merge()

          #secondary
          if self.B1[-10:] == "0000000000":
            self.b9.configure(text=self.A1[-10:])
            self.b11[8].configure(text=self.A1[-10:])
            secondary = self.A1[-10:]
          else:
            self.b9.configure(text=self.B1[-10:])
            self.b11[8].configure(text=self.B1[-10:])
            secondary = self.B1[-10:]
          
          #primary
          if self.B2[-10:] == "0000000000":
            self.b11[2].configure(text=self.A2[-10:])
            primary = self.A2[-10:]
          else:
            self.b11[2].configure(text=self.B2[-10:])
            primary = self.B2[-10:]
          self.number1, self.number2 = epi.e_func(primary,secondary)
          self.b11[4].configure(text=self.number1)
          self.b11[10].configure(text=self.number2)
          if condition == "Yes":
            self.b12.configure(state="disabled")
          else:
            self.b12.configure(state="normal")
        
        state, self.text_1, bg_color, error1 = dcs.callfunction_decod() # to initate first update
        self.b4.configure(text=self.text_1, font=("Verdana", 12), bg=bg_color)

        text1,text2, error2, self.ecolor = dts.callfunction_detection()
        text3 = "Plate Detection\n\n {} \n Indicator: {}".format(text2,text1)
        self.b5.configure(text=text3, font=("Verdana", 12), bg=text1)
        if len(error1) > 0:
          self.ecolor = "Red"
          if error2 == "No issues. System working fine.":
            error2 = ""
        self.error = error2 + error1
        self.elabel2.configure(text=self.error, font=("Verdana", 10), fg = self.ecolor)
        x+=1
        print("Checking # {}".format(x))
        time.sleep(5)
    except RuntimeError:
      pass
    
try:
  app = Fenetre()
  app.geometry("1080x720")
  app.mainloop()
except RuntimeError:
  pass
