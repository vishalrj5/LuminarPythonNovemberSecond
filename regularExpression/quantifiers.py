#quantifiers

from re import *
#pattern="a+" #check for a and more than one a
#pattern="a*" #a + plus zero occurance of a
#pattern="a?" #a plus zero number of a

#pattern="^a" #check for starting with a
#pattern="a$"#ending with a

pattern="a{2,3}" #chk for minimum 2 a and maximum 3 a
matcter=finditer(pattern,"aaaabaabaaaaa")
for match in matcter:
    print(match.start(),end="\t")
    print(match.group())
    #print("\n")