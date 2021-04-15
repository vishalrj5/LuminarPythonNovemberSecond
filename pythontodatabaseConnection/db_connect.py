#step 1 import mysql package
#step 2 establish connection
#step 3 cursor object
#execute queries

#close DB connection

import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password123",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
sql="SELECT VERSION()"

cursor.execute(sql)
data=cursor.fetchone()
print(data)

f=open("employee")
for line in f:
    data=line.rstrip("\n").split(",")
    sql="insert into employee(eid,ename,desig,salary)values(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(data))
    db.commit()
db.close()