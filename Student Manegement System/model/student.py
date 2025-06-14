from .person import Person

class Student(Person):
    def __init__(self,n,a,i,g):
        self.sid=i
        self.grade=g
        super().__init__(n,a)
    def showstudent(self):
        super().showinfo()
        print(f"ID : {self.sid}")
        print(f"Grade : {self.grade}")
