from tkinter import *
root =Tk()

f=open("exams.csv","r")
dict={}
num=1
for word in f:
    data=word.rstrip("\n").rsplit(",")
    sem=data[0]
    slot=data[1]
    course=data[2]
    term=data[3]
    if word not in dict:
        dict[num]={"Semester":sem,"slot":slot,"course":course,"Term":term}
    else:
        dict[sem, slot, course, term] = sem, slot, course, term
    #dict[course]={"Semester":sem,"slot":slot,"course":course,"Term":term}
    # #
    num+=1
#print(dict)

#print("\n- - - - Data Values Are - - - -\n \n\t\tSemester\n\t\tslot\n\t\tcourse\n\t\tTerm\n")
def Seme(a,b):
#a="Term"
#b="even"
    b=e.get()
    a=e2.get()
    count=0
    for k,v in dict.items():
        #print(k,v)
        for data,vata in v.items():
            if data==a:
                if vata==b:
                    print(k,v)
                    count += 1
                #elif b!=("even" or "odd"):
                 #   print("ok bei")
                  #  break
    print("You have",count,"Exams")
#a="Term"
#b=input("Enter odd or even")
#Seme(a,b)


#GUI part

root.geometry("500x500")
root.title("Vishal Examinations")
bframe=Frame(root)
l1=Label(root,text="Data Value : ")
e=Entry(root,width=50,bg="yellow",borderwidth=8)
l2=Label(root,text="Attribute : ")
e2=Entry(root,width=50,bg="lightgreen",borderwidth=8)
l1.grid(row=0,column=0)
e2.grid(row=0,column=1)
l2.grid(row=2,column=0)
e.grid(row=2,column=1)
e2.insert(1,"Type here")
e.insert(1,"Type here")
myLabel = Label(bframe,text="\n- - - - Data Values Are - - - -\n \nSemester\nslot\ncourse\nTerm\n")
def myClick():
    print("Done man, Congrats")

#ComboBox
OptionList=[
    "Semester",
    "slot",
    "course",
    "Term"
]
variable=StringVar(root)
variable.set(OptionList[0])
opt = OptionMenu(root, variable, *OptionList)
#w=OptionMenu(root,str,"Semester","slot","course","Term")
opt.grid(row=6)

b=StringVar()
b_entry=Entry(textvariable = b)
#b_entry.pack()

a=StringVar()
a_entry=Entry(textvariable = a)
#a_entry.pack()
bframe.grid(row=5,column=1)
myButton = Button(root,text="Exam",command=myClick)
myButton.config(command=lambda:Seme(a,b))
myLabel.grid()
myButton.grid(row=4,column=1)
root.mainloop()

