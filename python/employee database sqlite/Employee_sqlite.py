import sqlite3 
def upload(eno, ename, salary): 
    str = "insert into employee(eno,ename,salary) values('%d', '%s', '%f')" 
    args = (eno, ename, salary) 
    try: 
        cursor.execute(str % args) 
        conn.commit() 
        print("Employee Details Uploaded..") 
    except: 
        print('Not Uploaded') 
        conn.rollback() 
 
def display_eno(eno): 
    str = "select * from employee where eno='%d'" 
    args =(eno) 
    cursor.execute(str % args) 
    rows = cursor.fetchall() 
    for row in rows: 
        eno = row[0] 
        ename = row[1] 
        salary = row[2] 
        print('%-6d %10s %25f' % (eno, ename, salary)) 
 
def display_sal(min, max): 
    str = "select * from employee where salary between '%d' AND '%d'" 
    args = (min,max) 
    cursor.execute(str % args) 
    rows = cursor.fetchall() 
    for row in rows: 
        eno = row[0] 
        ename = row[1] 
        salary = row[2] 
        print('%-6d %10s %25f' % (eno,ename,salary))
conn = sqlite3.connect('mydatabase.db') 
cursor = conn.cursor() 
cursor.execute(" DROP TABLE IF EXISTS employee ") 
cursor.execute("create table employee(eno int, ename text, salary float)") 
 
while True: 
    print("\n1. Upload Employee Details") 
    print("2. Display Details Particular Employee") 
    print("3. Display Details Particular Employee(based on Salary)") 
    print("4. Exit") 
    ch = int(input("Enter Your Choice: ")) 
    if ch == 1: 
        no = int(input("\nEnter the Employee Number: ")) 
        name = input("Enter the Name: ") 
        sal = float(input("Enter the Salary: ")) 
        upload(no, name, sal) 
    elif ch == 2: 
        no = int(input("\nEnter the Employee Number: ")) 
        print("\n----------------Employee DETAILS--------------\n") 
        print("EMP No\t\tName\t\tSALARY") 
        print("\n---------------------------------------------\n") 
        display_eno(no) 
        print("\n---------------------------------------------\n") 
    elif ch == 3: 
        n = int(input("\nEnter the salary range(min): ")) 
        m = int(input("\nEnter the salary range(max): ")) 
        print("\n----------------Employee DETAILS--------------\n") 
        print("EMP No\t\tName\t\tSALARY") 
        print("\n---------------------------------------------\n") 
        display_sal(n, m) 
        print("\n---------------------------------------------\n") 
    elif ch == 4: 
        break 
    else: 
        print("invalid choice...") 
 
cursor.close() 
conn.close()
