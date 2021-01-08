from tkinter import *

root=Tk() #creating object for class Tk()
root.title("GUI")
label1=Label(root,text="username") #label
label2=Label(root,text="email-address")
label3=Label(root,text="password")

entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)

label1.pack() #for packing label
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()

root.mainloop() #for existing the o/p window until we close the window