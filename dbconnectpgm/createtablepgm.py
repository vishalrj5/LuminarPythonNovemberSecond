import mysql.connector
#we need database connection
from dbconnectpgm.dbconnect import get_connection
db=get_connection()
cursor=db.cursor()

sql="CREATE TABLE faculty(id varchar(25),name varchar(50),subject varchar(50))"
try:
    cursor.execute(sql)
    print("TABLE SUCCESSFULLY CREATED")
except Exception as e:
    print(e.args)
finally:
    db.close()