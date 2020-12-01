students=[

    [100,"arun","bca",145],
    [101,"arjun", "bca", 125],
    [102,"arun", "bca", 150],
    [103,"tinu","mca",140],
    [104,"jeena","bcom",120],

]
#print student names

for student in students:
    print(student[1])


 #print total of all student
total=0
for student in students:
    total=total+student[3]
print(total)

#list the details of student whose course=mca

for student in students:
    if(student[2]=='mca'):
        print(student)

#mca ? bca? bcom ?
mca=0
bca=0
bcom=0
for student in students:
    if(student[2]=='mca'):
        mca+=1
    if (student[2]=='bca'):
        bca+= 1
    if (student[2]=='bcom'):
        bcom+= 1
print("mca=",mca)
print("bca=",bca)
print("bcom=",bcom)

#highest total
lst=[]
for student in students:
    lst.append(student[3])
lst.sort()
print(lst)
length=len(lst)
print("Highest total is",lst[length-1])
