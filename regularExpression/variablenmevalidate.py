#variable name rule
#starting with alphabet a-kA-Z
#second character should be a digit and it must be divisible by 3
#followed by any number of characters
# z2rggg ==> invalid
# B7vggg ==> invalid
# a3rgggg==> valid
from re import *
rule="[a-kA-K][369]\w*"

variablename=input("Enter variable name")

matcher=fullmatch(rule,variablename)
if matcher != None:
    print("Valid")
else:
    print("invalid")
