from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
id=input("enter value for id")
name=input("enter name")
sql="insert into faculty(id,name,subject)values('101','vijay','datastructures')"

try:
    cursor.execute(sql)
    db.commit()
    print("Query executed")
except Exception as e:
    print(e.args)
finally:
    db.close()

