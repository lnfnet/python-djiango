#!/usr/bin/python3

import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='gkimfmnui',
                               database='employeedb')
print(conn)
cursor=conn.cursor()
newemployee=('insert into employees''(empid,lastname,firstname,salary)'
             'values(%s,%s,%s,%s)')
employee1 = ('9','lai','nanfei','4500.00')
employee2 = ('10','lai','suiyan','4500.00')
query=('select empid,lastname,firstname,salary from employees')
try:
    cursor.execute(newemployee,employee1)
    cursor.execute(newemployee,employee2)
    conn.commit()
except:
    print('sorry,there was a problem adding the data!')
else:
    print("data values added")
cursor.execute(query)
myresult=cursor.fetchall()
for (empid,lastname,firstname,salary) in myresult:
    print(empid,lastname,firstname,salary)
cursor.close()
conn.close()
