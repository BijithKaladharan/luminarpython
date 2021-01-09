from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="select * from faculty"

try:
    cursor.execute(sql)
    queryset=cursor.fetchone()
    for faculty in queryset:
        print(faculty[0])
except Exception as e:
    print(e.args)
finally:
    db.close()