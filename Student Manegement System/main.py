from model.teacher import Teacher
from model.student import Student
from model.admin import Admin

s1=[]
t1=[]
a1=[]

while True:
    print("\n----Student Management System----")
    ch=int(input("Enter Your Choice\n1.Add Student\t2.Show Student\t3.Update Student\t4.Delete Student\n5.Add Teacher\t6.Show Teacher\t7.Update Teacher\t8.Delete Teacher\n9.Add Admin\t10.Show Admin\t11.Update Admin\t\t12.Delete Admin\n13.Exit : "))
    if ch==1:
        name=input("\nEnter Student Name : ")
        age=int(input("Enter Student Age : "))
        sid=int(input("Enter Student ID : "))
        grade=input("Enter Student Grade : ")
        s=Student(name,age,sid,grade)
        s1.append(s)
        print("**Student Record Inserted!**")
    elif ch==2:
        print("\n-----Student Details-----")
        for student in s1:
            student.showstudent()
            print("--------------------------")
    elif ch==3:
        sid=int(input("Enter Student ID : "))
        for s in s1:
            if s.sid==sid:
                s.name=input("\nEnter Student Name : ")
                s.age=int(input("Enter Student Age : "))
                s.grade=input("Enter Student Grade : ")
                print("Record Updated")
                break
        else:
            print("Student Id Not Found")
    elif ch==4:
        sid = int(input("Enter Student ID to delete : "))
        for s in s1:
            if s.sid == sid:
                sid=sid-1
                del s1[sid]
                print("Student record deleted.")
                break
        else:
            print("Student ID not found.")
    elif ch==5:
        name=input("\nEnter Teacher Name : ")
        age=int(input("Enter Teacher Age : "))
        tid=int(input("Enter Teacher ID : "))
        sub=input("Enter Teacher Subject : ")
        sal=float(input("Enter Teacher Salary : "))
        t=Teacher(name,age,tid,sub,sal)
        t1.append(t)
        print("**Teacher Record Inserted!**")
    elif ch==6:
        print("\n-----Teacher Details-----")
        for teacher in t1:
            teacher.showteacher()
            print("--------------------------")
    elif ch==7:
        tid=int(input("Enter Teacher ID : "))
        for t in t1:
            if t.tid==tid:
                t.name=input("\nEnter Teacher Name : ")
                t.age=int(input("Enter Teacher Age : "))
                t.subject=input("Enter Teacher Subject : ")
                t.salary=float(input("Enter Teacher Salary : "))
                print("Record Updated")
                break
        else:
            print("Teacher ID Not Found")
    elif ch==8:
        tid=int(input("Enter Teacher ID : "))
        for t in t1:
            if t.tid == tid:
                tid=tid-1
                del t1[tid]
                print("Teacher record deleted.")
                break
        else:
            print("Teacher ID not found.")
    elif ch==9:
        name=input("\nEnter Admin Name : ")
        age=int(input("Enter Admin Age : "))
        aid=int(input("Enter Admin ID : "))
        sub=input("Enter Admin Subject : ")
        sal=float(input("Enter Admin Salary : "))
        dept=input("Enter Admin Departement : ")
        a=Admin(name,age,aid,sub,sal,dept)
        a1.append(a)
        print("**Admin Record Inserted!**")
    elif ch==10:
        print("\n-----Admin Details-----")
        for admin in a1:
            admin.showadmin()
            print("--------------------------")
    elif ch==11:
        aid=int(input("Enter Admin ID : "))
        for a in a1:
            if a.aid==aid:
                a.name=input("\nEnter Admin Name : ")
                a.age=int(input("Enter Teacher Age : "))
                a.salary=float(input("Enter Teacher Salary : "))
                a.subject=input("Enter Teacher Subject : ")
                a.dept=input("Enter Admin Departement : ")
                print("Record Updated")
                break
        else:
            print("Admin ID Not Found")
    elif ch==12:
        aid=int(input("Enter Admin ID : "))
        for a in a1:
            if a.aid == aid:
                aid=aid-1
                del a1[aid]
                print("Admin record deleted.")
                break
        else:
            print("Admin ID not found.")
    elif ch==13:
        print("Exiting....")
        break
    else:
        print("Invalid Choice!")
