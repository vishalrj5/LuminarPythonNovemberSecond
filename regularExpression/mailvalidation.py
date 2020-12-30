#gmail validation
from re import *
f=open("mails","r")
fout=open("validatedmails","w")
mails=set()
for id in f:
    mails.add(id.rstrip("\n"))
print(mails)
rule="[a-z0-9]{1,20}@gmail.com"
for mail in mails:
    matcher=fullmatch(rule,mail)
    if matcher != None:
        print("okay",mail)
        fout.write(mail+"\n")
    else:
        print(mail)
        pass