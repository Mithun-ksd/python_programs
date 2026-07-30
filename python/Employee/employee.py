class employee:
    def getdata(self):
        self.empno=int(input("\n Enter Employee number: "))
        self.name=input("\n Enter the Employee name: ")
        self.depname=input("\n Enter Employee department: ")
        self.designation=input("\n Enter Employee designation: ")
        self.age=int(input("\n Enter the age of Employee: "))
        self.salary=int(input("\n Enter Employee Salary: "))
    def showdata(self):
        print("\n",self.empno,"\t",self.name,"\t",self.depname,"\t",self.designation,"\t",self.age,"\t",self.salary)
    def search_data(self):
        print("Employee Number : ",self.empno)
        print("Employee Name : ",self.name)
        print("Employee Department : ",self.depname)
        print("Employee Designation : ",self.designation)
        print("Employee Age : ",self.age)
        print("Employee Salary : ",self.salary)
        print("Employee Name : ",self.empno)
emp_list=[]
n=int(input("Enter number of employee :"))
for i in range(n):
    e=employee()
    e.getdata()
    emp_list.append(e)
    print("\n Showing Employee Details :")
    print("\n Empno \t Name \t Department \t Designation \t Age \t Salary")
    print("")
    for e in emp_list:
        e.showdata()
eid=int(input("\n Enter Employee number to search Employee data: "))
for e in emp_list:
    if eid==e.empno:
        e.search_data()
        print()

        
