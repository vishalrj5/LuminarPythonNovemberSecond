#read csv file
#q1 find year wise release count

f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
print(dict)


#in which year highest number of movies released ?

#lst=[]
#for k,v in dict.items():
#    lst.append((v,k))
#lst=sorted(lst,reverse=True)
#print(lst[0])

#OR

highest=max(dict,key=dict.get)
print("\nYear",highest,"had released ",dict[highest],"movies ,which is the highest")