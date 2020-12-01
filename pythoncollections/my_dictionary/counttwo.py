text="hello how is you hello can you hear me"
dict={}

words=text.split(" ")
print(words)

for word in words:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
print(dict)
for key,val in dict.items():
    if(val>1):
        print((key,val))