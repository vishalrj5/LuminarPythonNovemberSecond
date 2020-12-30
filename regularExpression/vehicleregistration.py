#KL08BN1375 -> valid
#GJ08BN2211 -> invalid

from re import *

rule= "KL\d{2}[A-Z]{2,2}\d{1,4}"
number=input("Enter the number")
matcher=fullmatch(rule,number)
if matcher != None:
    print("Valid number")
else:
    print("Invalid Number in Kerala")
