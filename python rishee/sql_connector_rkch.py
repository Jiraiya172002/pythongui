import mysql.connector as m
conn =m.connect(host ='localhost', user ='root', database='12th', password='rkch172002')
if(conn.is_connected()):
    print("our connection is established successfullly.........")
else:
    print("somerthing is wrong")
cur = conn.cursor()
sq = "select * from rishi"
cur.execute(sq)
t = cur.fetchall()
for i in t:
    for j in i:
        print(j, sep ='  ',  end='  ')
    print()
conn.close()

