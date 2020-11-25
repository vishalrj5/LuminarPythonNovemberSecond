#print 1 to 12

#1 2 3 4
#5 6 7 8
#9 10 11 12
count=1
for i in range(1,13):
    print(i,end="\t")
    if count==4:
        print("\n")
        count=0
    count+=1

