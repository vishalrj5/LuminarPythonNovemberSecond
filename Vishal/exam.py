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

print("\n- - - - Data Values Are - - - -\n \n\t\tSemester\n\t\tslot\n\t\tcourse\n\t\tTerm\n")
def Seme(a,b):
#a="Term"
#b="even"
    b=e.get()
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
a="Term"
#b=input("Enter odd or even")
#Seme(a,b)


#GUI part

root.geometry("500x500")
root.title("Vishal Examinations")
e=Entry(root,width=50,bg="yellow",borderwidth=8)
e.pack()
e.insert(0,"odd or even")
myLabel = Label(root,text="\n- - - - Data Values Are - - - -\n \nSemester\nslot\ncourse\nTerm\n")
def myClick():
    myLabel= Label(root,text="Done man, Congrats")
    myLabel.pack()

b=StringVar()
b_entry=Entry(textvariable = b)

myButton = Button(root,text="Exam",command=myClick)
myButton.config(command=lambda:Seme(a,b))
myLabel.pack()
myButton.pack()
root.mainloop()

