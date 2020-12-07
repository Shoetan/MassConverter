from tkinter import *

# create Tk object from tkinter class
root = Tk()

root.title("Mass converter")

# create frist text box using the Entry class

e1 = Entry(root, width=20, borderwidth=5)

e1.grid(row=1, column=0)

label = Label(root, text = "=")
label.grid(row = 1, column = 1, padx = 10,  pady = 10)

e2 = Entry(root, width = 20, borderwidth=5)
e2.grid(row=1, column=2, padx = 10, pady  = 10)

global v
v = StringVar(root, "1")

def kgToPounds():
    num = int(e1.get())
    con = num * 2.205
    e2.insert(0, str(con))

def PoundsToKg():
    num = int(e1.get())
    con = num / 2.205
    e2.insert(0, str(con))

def KgToMg():
    num = int(e1.get())
    con = num * 1,000,000
    e2.insert(0, str(con))

def MgToKg():
    num = int(e1.get())
    con = num / 1,000,000
    e2.insert(0, str(con))

def TonneToPounds():
    num = int(e1.get())
    con = num * 2205
    e2.insert(0, str(con))

def PoundsToTonne():
    num = int(e1.get())
    con = num /2205
    e2.insert(0, str(con))

def KgToTonne():
    num = int(e1.get())
    con = num / 1000
    e2.insert(0, str(con))

def TonneToKg():
    num = int(e1.get())
    con = num * 1000
    e2.insert(0, str(con))
    
def button_cls():
    e1.delete(0, END)
    e2.delete(0, END)
def convert():
    pass

#create radio buttons for operations
r1 = Radiobutton(root, text="Ilbs to Kg", variable = v, value = 1, padx = 4, pady = 4, command = lambda: PoundsToKg())
r2 = Radiobutton(root, text ="Kg to ILbs",variable = v, value = 2 ,padx = 4, pady = 4, command = lambda: kgToPounds())
r3 = Radiobutton(root, text = "Kg to Mg", variable = v, value = 3, padx = 4, pady = 4, command = lambda: KgToMg())
r4 = Radiobutton(root, text = "Mg to Kg", variable = v, value = 4, padx = 4, pady = 4, command = lambda : MgToKg())
r5 = Radiobutton(root, text = "ILbs to Tonne",variable = v, value = 5, padx = 4, pady = 4,command = lambda: PoundsToTonne())
r6 = Radiobutton(root, text ="Tonne To ILbs",variable = v, value = 6, padx = 4, pady = 4, command = lambda:TonneToPounds())
r7 = Radiobutton(root, text = "Kg to Tonne",variable = v, value = 7, padx = 4, pady = 4, command = lambda : KgToTonne())
r8 = Radiobutton(root, text = "Tonne to Kg",variable = v, value = 8, padx = 4, pady = 4, command = lambda: TonneToKg())
#button_convert = Button(root, text = "convert", padx = 10, pady = 10)
button_reset = Button (root, text = "reset",width = 20, borderwidth = 5, padx = 10, pady = 10, command = lambda :button_cls())


#position radio buttons

r1.grid(row = 1 , column=3)
r2.grid(row = 2,  column=3)
r3.grid(row = 3,  column=3)
r4.grid(row = 4,  column=3)
r5.grid(row = 5,  column=3)
r6.grid(row = 6,  column=3)
r7.grid(row = 7,  column=3)
r8.grid(row = 8,  column=3)

#button_convert.grid(row = 4, column=0)
button_reset.grid(row = 4, column=0, columnspan=10)

root.mainloop()
