text="hai how are you hai how are you"

#word count hai,2 how,2 are,2 you,2
dict={}
words=text.split(" ")#['hai', 'how', 'are', 'you', 'hai', 'how', 'are', 'you']
print(words)
for word in words:#word=hai,how...
    if(word not in dict):#if hai is not in dict hai,1
        dict[word]=1#dict{hai:1}
    else:
        dict[word]+=1
print(dict)



