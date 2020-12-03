f=open("data","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    print(words)
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
print(dict)

#find highest frequency word
lst=[]
for k,v in dict.items():
    lst.append(v)
high=max(lst)

for k,v in dict.items():
    if(v==high):
        print("\n","'",k,"'","is the word with a count of",v)
