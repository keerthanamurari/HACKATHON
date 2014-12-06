import tkinter
from tkinter import *
def sel1():
   selection = "You selected the option " + str(varq1.get())
   label1.config(text = selection)
def sel2():
   selection = "You selected the option " + str(varq2.get())
   label2.config(text = selection)
 
def sel3():
   selection = "You selected the option " + str(varq3.get())
   label3.config(text = selection)

def sel4():
   selection = "You selected the option " + str(varq4.get())
   label4.config(text = selection)
   
def sel5():
   selection = "You selected the option " + str(varq5.get())
   label5.config(text = selection)
   
def sel6():
   selection = "You selected the option " + str(varq6.get())
   label6.config(text = selection)

def sel7():
   selection = "You selected the option " + str(varq7.get())
   label7.config(text = selection)

def sel8():
   selection = "You selected the option " + str(varq8.get())
   label8.config(text = selection)

def sel9():
   selection = "You selected the option " + str(varq9.get())
   label9.config(text = selection)

def sel10():
   selection = "You selected the option " + str(varq10.get())
   label10.config(text = selection)
   
root = Tk()
frame = tkinter.Frame(root)
frame.pack()
mainvar = StringVar()
mainvar.set("Enter user name")
mainlabel = Label(frame, textvariable = mainvar)
mainlabel.pack()
maintext = Entry(frame, textvariable = mainvar)
maintext.pack()

frame1 = tkinter.Frame(root)
frame1.pack()

var1 = StringVar()
var1.set('Which word does NOT belong with the others?')
l1 = Label(frame1, textvariable = var1)
l1.pack()
 
varq1 = IntVar()
g1_1 = Radiobutton(frame1, text="parsley", variable=varq1, value=1,command=sel1)
g1_1.pack(side=LEFT)
g1_2 = Radiobutton(frame1, text="basil", variable=varq1, value=2,command=sel1)
g1_2.pack(side=LEFT)
g1_3 = Radiobutton(frame1, text="dill", variable=varq1, value=3,command=sel1)
g1_3.pack(side=LEFT)
g1_4 = Radiobutton(frame1, text="mayonnaise", variable=varq1, value=4,command=sel1)
g1_4.pack(side=LEFT)

label1 = Label(root, text="Your selection will appear here")
label1.pack()

frame2 = tkinter.Frame(root)
frame2.pack()

var2 = StringVar()
var2.set('Which word does NOT belong with the others?')

l2 = Label(frame2, textvariable = var2)
l2.pack()

varq2 = IntVar()
g2_1 = Radiobutton(frame2, text="inch", variable=varq2, value=1,command=sel2)
g2_1.pack(side=LEFT)
g2_2 = Radiobutton(frame2, text="ounce", variable=varq2, value=2,command=sel2)
g2_2.pack(side=LEFT)
g2_3 = Radiobutton(frame2, text="centimeter", variable=varq2, value=3,command=sel2)
g2_3.pack(side=LEFT)
g2_4 = Radiobutton(frame2, text="yard", variable=varq2, value=4,command=sel2)
g2_4.pack(side=LEFT)
label2 = Label(root, text="Your selection will appear here")
label2.pack()
 
 
frame3 = tkinter.Frame(root)
frame3.pack()
 
var3 = StringVar()
var3.set('Which word does NOT belong with the others?')
l3 = Label(frame3, textvariable = var3)
l3.pack()
 
varq3 = IntVar()
g3_1 = Radiobutton(frame3, text="tyre", variable=varq3, value=1,command=sel3)
g3_1.pack(side=LEFT)
g3_2 = Radiobutton(frame3, text="steering wheel", variable=varq3, value=2,command=sel3)
g3_2.pack(side=LEFT)
g3_3 = Radiobutton(frame3, text="engine", variable=varq3, value=3,command=sel3)
g3_3.pack(side=LEFT)
g3_4 = Radiobutton(frame3, text="car", variable=varq3, value=4,command=sel3)
g3_4.pack(side=LEFT)
 
label3 = Label(root, text="Your selection will appear here")
label3.pack()

frame4 = tkinter.Frame(root)
frame4.pack()
 
var4 = StringVar()
var4.set('Which word does NOT belong with the others?')
l4 = Label(frame4, textvariable = var4)
l4.pack()
 
varq4 = IntVar()
g4_1 = Radiobutton(frame4, text="tulip", variable=varq4, value=1,command=sel4)
g4_1.pack(side=LEFT)
g4_2 = Radiobutton(frame4, text="rose", variable=varq4, value=2,command=sel4)
g4_2.pack(side=LEFT)
g4_3 = Radiobutton(frame4, text="bud", variable=varq4, value=3,command=sel4)
g4_3.pack(side=LEFT)
g4_4 = Radiobutton(frame4, text="daisy", variable=varq4, value=4,command=sel4)
g4_4.pack(side=LEFT)
 
label4 = Label(root, text="Your selection will appear here")
label4.pack()

frame5 = tkinter.Frame(root)
frame5.pack()
 
var5 = StringVar()
var5.set('Which word does NOT belong with the others?')
l5 = Label(frame5, textvariable = var5)
l5.pack()
 
varq5 = IntVar()
g5_1 = Radiobutton(frame5, text="rye", variable=varq5, value=1,command=sel5)
g5_1.pack(side=LEFT)
g5_2 = Radiobutton(frame5, text="sourdough", variable=varq5, value=2,command=sel5)
g5_2.pack(side=LEFT)
g5_3 = Radiobutton(frame5, text="pumpernickle", variable=varq5, value=3,command=sel5)
g5_3.pack(side=LEFT)
g5_4 = Radiobutton(frame5, text="loaf", variable=varq5, value=4,command=sel5)
g5_4.pack(side=LEFT)
 
label5 = Label(root, text="Your selection will appear here")
label5.pack()


frame6 = tkinter.Frame(root)
frame6.pack()
 
var6 = StringVar()
var6.set('Which word does NOT belong with the others?')
l6 = Label(frame6, textvariable = var6)
l6.pack()
 
varq6 = IntVar()
g6_1 = Radiobutton(frame6, text="guitar", variable=varq6, value=1,command=sel6)
g6_1.pack(side=LEFT)
g6_2 = Radiobutton(frame6, text="violin", variable=varq6, value=2,command=sel6)
g6_2.pack(side=LEFT)
g6_3 = Radiobutton(frame6, text="flute", variable=varq6, value=3,command=sel6)
g6_3.pack(side=LEFT)
g6_4 = Radiobutton(frame6, text="cello", variable=varq6, value=4,command=sel6)
g6_4.pack(side=LEFT)
 
label6 = Label(root, text="Your selection will appear here")
label6.pack()



frame7 = tkinter.Frame(root)
frame7.pack()
 
var7 = StringVar()
var7.set('Which word does NOT belong with the others?')
l7 = Label(frame7, textvariable = var7)
l7.pack()
 
varq7 = IntVar()
g7_1 = Radiobutton(frame7, text="dodge", variable=varq7, value=1,command=sel7)
g7_1.pack(side=LEFT)
g7_2 = Radiobutton(frame7, text="flee", variable=varq7, value=2,command=sel7)
g7_2.pack(side=LEFT)
g7_3 = Radiobutton(frame7, text="duck", variable=varq7, value=3,command=sel7)
g7_3.pack(side=LEFT)
g7_4 = Radiobutton(frame7, text="avoid", variable=varq7, value=4,command=sel7)
g7_4.pack(side=LEFT)
 
label7 = Label(root, text="Your selection will appear here")
label7.pack()


frame8 = tkinter.Frame(root)
frame8.pack()
 
var8 = StringVar()
var8.set('Which word does NOT belong with the others?')
l8 = Label(frame8, textvariable = var8)
l8.pack()
 
varq8 = IntVar()
g8_1 = Radiobutton(frame8, text="branch", variable=varq8, value=1,command=sel8)
g8_1.pack(side=LEFT)
g8_2 = Radiobutton(frame8, text="dirt", variable=varq8, value=2,command=sel8)
g8_2.pack(side=LEFT)
g8_3 = Radiobutton(frame8, text="leaf", variable=varq8, value=3,command=sel8)
g8_3.pack(side=LEFT)
g8_4 = Radiobutton(frame8, text="root", variable=varq8, value=4,command=sel8)
g8_4.pack(side=LEFT)
 
label8 = Label(root, text="Your selection will appear here")
label8.pack()


frame9 = tkinter.Frame(root)
frame9.pack()
 
var9 = StringVar()
var9.set('Which word does NOT belong with the others?')
l9 = Label(frame9, textvariable = var9)
l9.pack()
 
varq9 = IntVar()
g9_1 = Radiobutton(frame9, text="tape", variable=varq9, value=1,command=sel9)
g9_1.pack(side=LEFT)
g9_2 = Radiobutton(frame9, text="twine", variable=varq9, value=2,command=sel9)
g9_2.pack(side=LEFT)
g9_3 = Radiobutton(frame9, text="cord", variable=varq9, value=3,command=sel9)
g9_3.pack(side=LEFT)
g9_4 = Radiobutton(frame9, text="yarn", variable=varq9, value=4,command=sel9)
g9_4.pack(side=LEFT)
 
label9 = Label(root, text="Your selection will appear here")
label9.pack()


frame10 = tkinter.Frame(root)
frame10.pack()
 
var10 = StringVar()
var10.set('Which word does NOT belong with the others?')
l10 = Label(frame10, textvariable = var10)
l10.pack()
 
varq10 = IntVar()
g10_1 = Radiobutton(frame10, text="couch", variable=varq10, value=1,command=sel10)
g10_1.pack(side=LEFT)
g10_2 = Radiobutton(frame10, text="rug", variable=varq10, value=2,command=sel10)
g10_2.pack(side=LEFT)
g10_3 = Radiobutton(frame10, text="table", variable=varq10, value=3,command=sel10)
g10_3.pack(side=LEFT)
g10_4 = Radiobutton(frame10, text="chair", variable=varq10, value=4,command=sel10)
g10_4.pack(side=LEFT)
 
label10 = Label(root, text="Your selection will appear here")
label10.pack()


button = tkinter.Button(root, text="Submit", command=sys.exit)
button.pack()
root.mainloop()

