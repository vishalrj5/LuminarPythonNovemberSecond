
# variable length argument methods

#def add(*num):
 #   sum=0
  #  for n in num:
   #     sum=sum+n
    #print(sum)


#add(10,20,30,40)

def print_data(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)
print_data(birth_place="kochi",desig="developer",salary=25000,work_place="aluva")