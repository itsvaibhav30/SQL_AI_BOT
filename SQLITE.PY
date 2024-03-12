import sqlite3
# connecting to sqlite
connection=sqlite3.connect("student.db")

# creating a cursor object and decribe the table info 
cursor=connection.cursor()

# create a table
table_info="""create table STUDENT(Name varchar(20),Class varchar(20),Sec varchar(20));"""

cursor.execute(table_info)

# inserting some values into the table
cursor.execute('''insert into student values("Vaibhav","BCA","B");''')
cursor.execute('''insert into student values("Dharam","BCA","A");''')
cursor.execute('''insert into student values("Apurv","BBA","B");''')
cursor.execute('''insert into student values("Raj","BBA","B");''')
cursor.execute('''insert into student values("Ritesh","BCA","A");''')

print("The inserted records are")
data=cursor.execute('''Select * from student''')
for row in data:
    print(row)
    
# commit your changes in the database
connection.commit()
connection.close()
    
