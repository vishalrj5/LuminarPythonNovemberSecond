first=[1,2,3,4,6,7]
second=[4,5,6]

#(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)

#abocepairs
print([(i,j) for i in first for j in second])

#squares
squares=[ i**2 for i in first]
print(squares)

#012378
#num<5 num-1
#num>5 num+1
data=[i-1 if i<5 else i+1 for i in first]
print(data)