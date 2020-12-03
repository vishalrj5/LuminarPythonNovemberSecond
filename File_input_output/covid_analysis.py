f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split("\t")
    state=words[3].rstrip("***")
    confirmed_cases=int(words[8])
    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases
lst=[]
for k,v in dict.items():
    lst.append((v,k))
print(sorted(lst,reverse=True))

#high=max(dict,key=dict.get)
#print("\n",high,"scored high")
