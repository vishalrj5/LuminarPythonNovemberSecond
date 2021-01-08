from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
id=int(input("enter value for id"))
for i in range(id):
    rol=input("\nenter rol")
    name=input("\nEnter name")
    subject=input("\nEnter subject")
    sql="insert into faculty(id,name,subject)values(%s,%s,%s)"

try:
    cursor.execute(sql)
    db.commit()
    print("Query executed")
except Exception as e:
    print(e.args)
finally:
    db.close()

