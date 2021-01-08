from tkinter import *

root=Tk()
Tframe=Frame(root)
Bframe=Frame(root)


Tframe.pack()
Bframe.pack(side=BOTTOM)

btn1=Button(Tframe,text="FirstButton",fg="green")
btn2=Button(Tframe,text="SirstButton",fg="blue")
btn3=Button(Tframe,text="ThirdButton",fg="yellow")
btn4=Button(Bframe,text="FourthButton",fg="cyan")

btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=BOTTOM)

root.mainloop()