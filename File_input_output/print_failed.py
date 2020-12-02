names=open("names","r")
passed=open("passed","r")
snames=set()
spassed=set()
for line in names:
    snames.add(line.rstrip("\n"))
for lin in passed:
    spassed.add(lin.rstrip("\n"))
failed=snames.difference(spassed)
print(failed,"Are the failed students")