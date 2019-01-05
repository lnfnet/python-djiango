#!/usr/bin/python3
 
import math
import mysql.connector

conn = mysql.connector.connect(host='192.168.216.139',user='root',password='gkimfmnui',
                               database='employDB')
print(conn)
cursor=conn.cursor()
query=('select emid,lastname,firstname,salary from employers')

print('''Content-Type:text/html

<!DOCTYPE html>
<html>

<head>
<title>The area of a circle</title>
</head>

<body>

<h2>Calculating the area of circle:</h2>
<table>
<tr><th>EMID</th><th>lastname</th><th>firstname</th><th>salary</th></tr> ''')

cursor.execute(query)
myresult=cursor.fetchall()
for(empid,lastname,firstname,salary) in myresult:
    print('<tr><td>',empid,'</td>')
    print('<td>',lastname,'</td>')
    print('<td>',firstname,'</td>')
    print('<td>',salary,'</td></tr>')
print('</table>')
print('</body>')
print('</html>')
cursor.close()
conn.close()
