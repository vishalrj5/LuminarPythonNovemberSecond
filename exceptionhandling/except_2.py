no1=int(input("Enter the number 1"))
no2=int(input("Enter the number 2"))
try:
    res=no1/no2
    print(res)
except:
    no2=int(input("Enter another value for no2"))
    res=no1/no2
    print(res)
finally:
    print("Done")