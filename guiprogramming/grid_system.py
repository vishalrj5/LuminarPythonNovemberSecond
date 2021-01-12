from tkinter import *
from tkinter import messagebox
root=Tk()
import mysql.connector
from dbconnectpgm.dbconnect import get_connection
def db_connect(username,password):
    print("inside......................")
    #db connect logic
    db=get_connection()
    cursor=db.cursor()
    try:
        cursor.execute(("select * from users where username=%s And password=%s"),(username,password))
        user=cursor.fetchone()
        return user

    except Exception as e:
        print(e.args)
def authenticate_user():
    global uentry
    global pentry
    uname=uentry.get()
    pwd=pentry.get()
    user=db_connect(uname,pwd)
    if (user==None):
        messagebox.showerror("invalid User","Error")
    else:
        messagebox.showinfo("User Successfully Logged","Loggeddddd")

ulabel=Label(root,text="Username")
plabel=Label(root,text="Password")

uentry=Entry(root)
pentry=Entry(root)

btn=Button(root,text="Login",command=authenticate_user)

ulabel.grid(row=0,column=0)
plabel.grid(row=1,column=0)

uentry.grid(row=0,column=1)
pentry.grid(row=1,column=1)

btn.grid(columnspan=2)


root.mainloop()






#create table students
#rol name course total
#10     ajay  mca  140
#11     vijay bca   135
#12     tom   mca   145

#course wise group mca :2, bca:1

#in which course no of joinees <1 bca

#highest total course wise mca:145 , bca:135



