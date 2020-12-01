#values stored in key:value pairs


students={'rolno':100,"name":"ajay","course":"mca","total":100}

#updating total with value
students["total"]+=50#100+50 = 150
#dictionary keys rolno,name,course
#we can access the values only by using corresponding key
#name
print(students["name"])
#course
print(students["course"])
#duplicate keys are not allowed, duplicate values are allowed
print(students)
#checking for a key in dict
print("gender" in students)

print("name" in students)

#adding new key value pairs
students["gender"]="male"
print(students)


