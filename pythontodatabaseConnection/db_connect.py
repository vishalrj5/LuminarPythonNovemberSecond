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