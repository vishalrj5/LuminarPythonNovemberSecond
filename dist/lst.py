#find common elements from this two list


lst=[10,20,30,40,50]
lst2=[8,9,10,20,21]
asd=[]
# for i in lst:
#     for j in lst2:
        # if i==j:
        #     asd.append(i)

a=[element for element in lst if element in lst2]

print(a,"are two common elements from lst and lst2")            
            