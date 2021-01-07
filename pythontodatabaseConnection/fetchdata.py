from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="select * from faculty"

try:
    cursor.execute(sql)
    queryset=cursor.fetchall()
    for fac in queryset:
        print(fac)
except Exception as e:
    print(e.args)
finally:
    db.close()