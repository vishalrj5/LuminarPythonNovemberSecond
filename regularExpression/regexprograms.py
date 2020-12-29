#regular expression
#pattern matching
#step 1
#package not in builtins.py it is in re
import re
matcher=re.finditer("ab","abababababaabbab")
#                         0123456789
cnt=0
for match in matcher:
    print(match.start(),end="\t")
    print(match.group())
    cnt+=1
print("There are",cnt,"patterns here")