from re import *
f=open("phonenumbers","r")
fout=open("validphone","w")
phone=set()
for num in f:
    phone.add(num.rstrip("\n"))
#print(phone)
rule="\d{10}"
for n in phone:
    matcher=fullmatch(rule,n)
    if matcher != None:
        fout.write(n+"\n")
    else:
        pass