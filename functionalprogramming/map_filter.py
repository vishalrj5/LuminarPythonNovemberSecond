#map()
#filter()
#reduce()
lst=[10,11,12,13,14,15]

#squares
#map(function, iterables)

#squares=list(map(lambda num:num**2,lst))
#print(squares)

#cubes=list(map(lambda num:num**3,lst))
#print(cubes)

even=list(filter(lambda num:num%2==0,lst))
print(even)


# employees=["ajay","vijay","anil","danie","tom","joy"]

#convert all employee names to uppercase
#print all employee name starting with a
#

employees=["ajay","vijay","anil","danie","tom","joy"]
upper=list(map(lambda name:name.upper(),employees))
print(upper)
start=list(filter(lambda nam:nam[0]=="a",employees))
print(start)