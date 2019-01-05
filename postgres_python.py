#!/usr/bin/python

import psycopg2

conn = psycopg2.connect(database="pytest", user="postgres", password="gkimfmnui", host="127.0.0.1", port="5432")
print ("Opened database successfully")

cur = conn.cursor()

cur.execute("INSERT INTO employees (empid,lastname,firstname,salary) \
      VALUES (2, 'Paul', 'lai',1132.00 )");
cur.execute("SELECT empid,lastname,firstname,salary from employees")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
conn.commit()
print ("Records created successfully")
conn.close()
