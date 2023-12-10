import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='Test@123',database="mydata")
if conn.is_connected():
    print('connection mapped')
    mycuror=conn.cursor()
    #mycuror.execute("insert into hospital(RefrenceNo,PatientName,lot) values(%s,%s,%s)",("ABC101","Monu","12"))
    conn.commit()
    conn.close()
else:
    print("Error")