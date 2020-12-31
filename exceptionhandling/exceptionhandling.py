#exception

#error
#exception
#exception handling
no1=int(input("Enter value for no1"))
no2=int(input("Enter value for no2"))
try:
    res=no1/no2
    print(res)
except Exception as e:
    print(e.args)

#try:
#   doubtful code
#except:
#   exception handling code