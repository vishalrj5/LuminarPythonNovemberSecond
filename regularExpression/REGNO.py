from re import *

f=open("registrationnumbers","r")
fout=open("validreg","w")
regnum=set()
for numbers in f:
    regnum.add(numbers.rstrip("\n"))
print(regnum)
rule= "KL\d{2}[A-Z]{1,2}\d{1,4}"
for vehiclenum in regnum:
    matcher=fullmatch(rule,vehiclenum)
    if matcher != None:
        fout.write(vehiclenum+"\n")
    else:
        pass


#create rule for validating gmail ids
#file implimentation
#validate all phone numbers (10 numbers)


#exceptionhandling
#mysql (create, insert, update, delete)

#