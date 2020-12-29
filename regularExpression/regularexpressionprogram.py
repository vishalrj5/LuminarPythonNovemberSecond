from re import *

#predefined character sets
#pattern='[a-z]'# check for lowercase a to z characters
#pattern='[0-9]' #check all digits
#pattern='[^0-9]' #except numbers
#pattern='[^a-z]' #except lower cases
#pattern='[a-zA-Z]' #check for both lower and upper cases

#lower case uppercase digit
#pattern='[a-zA-Z0-9]'
#special characters
#pattern='[^a-zA-z0-9]'
#predefined characters
#pattern="\s" #checking for spaces
#pattern="\S" #except space
#pattern="\d" #checking for digits
#pattern="\D" #except digit
#pattern="\w" #except special characters '[a-zA-z0-9]'
pattern="\W" #Except special characters '[^a-zA-z0-9]'
#character sets and characters
#quantifiers
mather=finditer(pattern,"abc Z@7k")
for match in mather:
    print(match.start(),end="\t") #0 1 2 7
    print(match.group()) #a b c k
#out=[(match.start(),match.group()) for match in mather]
#print(out)