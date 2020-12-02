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
num=1
for k,v in dict.items():
    if(v>num):
        num+=1
        s=k
print("\n","'",s,"'","is the word with a count of",num)
