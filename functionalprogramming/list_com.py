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


lst=[1,2,3,4,5,6,7,8,5,0]
#return n-1 if n<5 n+1 if n>5 return 5 if n==5

data=[i+1 if i>5 else i-1 if i<5 and i!=0 else 0 if i==0 else i for i in lst
    ]
print("out",data)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#1,2,3,4,5,6,7,8,9
#flatten operation

flat=[j for i in matrix for j in i]
print(flat)

