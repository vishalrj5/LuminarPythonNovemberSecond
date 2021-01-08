from tkinter import *

root=Tk()

def click_btn():
    print("btn clicked")
ulabel=Label(root,text="Username")
plabel=Label(root,text="Password")

uentry=Entry(root)
pentry=Entry(root)

btn=Button(root,text="Login",command=click_btn)

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)

btn.grid(columnspan=2)


root.mainloop()