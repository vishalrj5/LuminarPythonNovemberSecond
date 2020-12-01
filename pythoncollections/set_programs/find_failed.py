name=["a","b","c","d","e","f","g","H"]

passed=["a","b","c"]

nset=set(name)
pset=set(passed)
print(nset)
print(pset)

failed=nset.difference(pset)
print("failed students are",failed)