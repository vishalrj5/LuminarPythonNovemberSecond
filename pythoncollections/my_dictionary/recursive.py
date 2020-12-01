pattern="ABABAC"
#find first recursive Character
dict={}
for pat in pattern:
    print(pat)
    if(pat not in dict):
        dict[pat]=1
    else:
        print("first Recursive is",pat)
        break
