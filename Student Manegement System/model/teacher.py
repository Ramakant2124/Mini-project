from .person import Person

class Teacher(Person):
    def __init__(self,n,a,i,sub,sal):
        self.tid=i
        self.subject=sub
        self.salary=sal
        super().__init__(n,a)

    def showteacher(self):
        super().showinfo()
        print(f"ID : {self.tid}")
        print(f"Subject : {self.subject}")
        print(f"Salary : {self.salary}")
