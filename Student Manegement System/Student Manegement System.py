class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def showinfo(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        
class Student(Person):
    def __init__(self,n,a,i,g):
        self.sid=i
        self.grade=g
        super().__init__(n,a)
    def showstudent(self):
        super().showinfo()
        print(f"ID : {self.sid}")
        print(f"Grade : {self.grade}")

        
class Teacher(Person):
    def __init__(self,n,a,sub,sal):
        self.subject=sub
        self.salary=sal
        super().__init__(n,a)

    def showteacher(self):
        super().showinfo()
        print(f"Subject : {self.subject}")
        print(f"Salary : {self.salary}")

class Admin(Teacher):
    def __init__(self,n,a,d,sub,sal):
        self.dept=d
        super().__init__(n,a,sub,sal)
    def showadmin(self):
        super().showteacher()
        print(f"Admin Department : {self.dept}")

s1=[]
t1=[]
a1=[]

while True:
    print("\n----Student Management System----")
    ch=int(input("Enter Your Choice\n1.Add Student\t2.Show Student\n3..Add Teacher\t4.Show Teacher\n5.Add Admin\t6.Show Admin\n7.Exit : "))
    if ch==1:
        name=input("\nEnter Student Name : ")
        age=int(input("Enter Student Age : "))
        sid=int(input("Enter Student ID : "))
        grade=input("Enter Student Grade : ")
        s=Student(name,age,sid,grade)
        s1.append(s)
        print("*Student Record Inserted!*")
    elif ch==2:
        print("\n-----Student Details-----")
        for student in s1:
            student.showstudent()
            print("--------------------------")
    elif ch==3:
        name=input("\nEnter Teacher Name : ")
        age=int(input("Enter Teacher Age : "))
        sub=input("Enter Teacher Subject : ")
        sal=float(input("Enter Teacher Salary : "))
        t=Teacher(name,age,sub,sal)
        t1.append(t)
        print("*Teacher Record Inserted!*")
    elif ch==4:
        print("\n-----Teacher Details-----")
        for teacher in t1:
            teacher.showteacher()
            print("--------------------------")
    elif ch==5:
        name=input("\nEnter Admin Name : ")
        age=int(input("Enter Admin Age : "))
        sub=input("Enter Admin Subject : ")
        sal=float(input("Enter Admin Salary : "))
        dept=input("Enter Admin Departement : ")
        a=Admin(name,age,sub,sal,dept)
        a1.append(a)
        print("*Admin Record Inserted!*")
    elif ch==6:
        print("\n-----Admin Details-----")
        for admin in a1:
            admin.showadmin()
            print("--------------------------")
    elif ch==7:
        print("Exiting....")
        break
    else:
        print("Invalid Choice!")
