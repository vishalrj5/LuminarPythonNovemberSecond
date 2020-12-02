f=open("data","r")
lst=[]
cnt=0
for lines in f:
    words=lines.split(" ")
    for word in words:
        cnt+=1
        lst.append(word.rstrip(".\n"))
print(lst)
print(cnt)