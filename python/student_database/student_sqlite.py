import sqlite3

def upload(regno, name, mark1, mark2, mark3):
    str = "insert into student(regno, name, mark1, mark2, mark3) values('%d','%s','%d','%d','%d')"
    args = (regno, name, mark1, mark2, mark3)
    try:
        cursor.execute(str % args)
        conn.commit()
        print("students Details Uploaded..")
    except:
        print("not uploaded...")
        conn.rollback()

def display():
    str = "select * from student"
    cursor.execute(str)
    rows = cursor.fetchall()
    for row in rows:
        regno = row[0]
        name = row[1]
        mark1 = row[2]
        mark2 = row[3]
        mark3 = row[4]
        print('%-6d%-10s%6d%6d%6d' % (regno, name, mark1, mark2, mark3))

def delete_row(regno):
    flag = 0
    cursor.execute("select regno from student")
    rows = cursor.fetchall()
    for row in rows:
        i = row[0]
        if i == regno:
            str = "delete from student where regno='%d'"
            args = (regno)
            cursor.execute(str % args)
            print("\n student details deleted\n")
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        print("error in deletion...Student details doesnot exist...")


conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS student")
cursor.execute("create table student(regno int, name text, mark1 int, mark2 int, mark3 int)")

while True:
    print("\n 1.Upload student details")
    print("\n 2.Display student details")
    print("\n 3.Delete particular student details")
    print("\n 4.exit")
    ch = int(input("\n Enter your choice:"))

    if ch == 1:
        rno = int(input("\n Enter the register number:"))
        sname = input("\n Enter the name:")
        m1 = int(input("\n Enter mark in subject-1:"))
        m2 = int(input("\n Enter mark in subject-2:"))
        m3 = int(input("\n Enter mark in subject-3:"))
        upload(rno, sname, m1, m2, m3)

    elif ch == 2:
        print("\n-------------------STUDENT DETAILS-------------------\n")
        print("Reg no\tName\tSUB1\tSUB2\tSUB3")
        print("\n-----------------------------------------------------\n")
        display()
        print("\n-----------------------------------------------------\n")

    elif ch == 3:
        rno = int(input("\n enter the register number:"))
        delete_row(rno)

    elif ch == 4:
        break

    else:
        print("invalid choice....")

cursor.close()
conn.close()
